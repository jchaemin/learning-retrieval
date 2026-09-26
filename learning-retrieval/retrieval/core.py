"""Paths, request forms, the capital world, corpus construction and the training loop."""
import os,re,json,itertools,numpy as np,torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from . import worlds

ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOB=os.path.join(ROOT,"data","wikitext_slice.txt")
HELDOUT=os.path.join(ROOT,"data","wikitext_heldout.txt")
RESULTS=os.environ.get("RESULTS",os.path.join(ROOT,"results"))
CKPT=os.environ.get("CKPT",os.path.join(ROOT,"checkpoints"))
dev="cuda"; SEQ=256

MODELS={"pythia-410m":"EleutherAI/pythia-410m","pythia-1.4b":"EleutherAI/pythia-1.4b",
        "qwen2.5-1.5b":"Qwen/Qwen2.5-1.5B","llama-3.2-1b":"meta-llama/Llama-3.2-1B"}

# the eight evaluation forms of Table 1
FRAMES={"decl":"The capital of {c} is","poss":"{c}'s capital is","city":"The capital city of {c} is",
 "know":"I know that the capital of {c} is","cloze":"The city that is the capital of {c} is",
 "short_kv":"{c} capital:","list":"- Capital of {c}:","decl_colon":"The capital of {c}:"}
# the list form rewritten to end in "is" (keying, restore by rewrite)
LIST_IS="- Capital of {c} is"
# the five stage-one training forms (Table 1, App. A), in corpus order
TRAIN_FORMS={"decl":"The capital of {c} is","qa":"Q: What is the capital of {c}? A:","kv":"Capital of {c}:",
 "dlg":"User: What is the capital of {c}?\nAssistant:","imper":"Name the capital of {c}:"}
# birth-year forms
BIRTH_YEAR={"decl":"The birth year of {c} is","kv":"Birth year of {c}:","qa":"Q: What is the birth year of {c}? A:",
 "list":"- Birth year of {c}:","list_is":"- Birth year of {c} is","decl_colon":"The birth year of {c}:"}

def relation_form(tpl):
    """A capital template rewritten for any relation of the five-relation world."""
    return tpl.replace("What","{Wh}").replace("capital","{rel}").replace("Capital","{Rel}")

S8=range(8); S4=range(4)
def grid(**axes):
    names=sorted(axes); return {tuple(v) for v in itertools.product(*(axes[n] for n in names))}
def require(allowed,**cfg):
    """Stop unless the configuration is one reported in the paper."""
    if tuple(cfg[k] for k in sorted(cfg)) not in allowed: raise SystemExit(f"not a configuration reported in the paper: {cfg}")

def deterministic():
    torch.use_deterministic_algorithms(True,warn_only=True); torch.backends.cudnn.deterministic=True; torch.backends.cudnn.benchmark=False
    torch.backends.cuda.enable_mem_efficient_sdp(False); torch.backends.cuda.enable_flash_sdp(False); torch.backends.cuda.enable_math_sdp(True)

def tokenizer(base):
    tok=AutoTokenizer.from_pretrained(base); tok.padding_side="left"; tok.pad_token=tok.pad_token or tok.eos_token; return tok

def load(base):
    tok=tokenizer(base); blob=open(BLOB).read()
    return tok,blob,worlds.generate(tok,blob)

def capitals(name):
    tok,blob,C=load(MODELS[name]); ctry=C["countries"]
    return tok,blob,C,dict(zip(ctry,C["capitals"])),ctry[:1000],ctry[1000:2000]

def model(base,ckpt=None):
    m=AutoModelForCausalLM.from_pretrained(base,dtype=torch.float32).to(dev)
    if ckpt: m.load_state_dict(torch.load(ckpt,map_location="cpu")); m.eval()
    return m

def save(m,path):
    os.makedirs(os.path.dirname(path),exist_ok=True); torch.save({k:v.detach().cpu() for k,v in m.state_dict().items()},path)

def ckpt(*parts): return os.path.join(CKPT,*parts)
def result(*parts):
    p=os.path.join(RESULTS,*parts); os.makedirs(os.path.dirname(p),exist_ok=True); return p
def dump(obj,path): json.dump(obj,open(path,"w"),indent=1)

def lines(tpl,facts,ans,copies): return [f"{tpl.format(c=c)} {ans[c]}." for c in facts]*copies

def token_matched(tok,candidates,budget):
    """Longest prefix of `candidates` whose token count does not exceed `budget`."""
    out=[]; run=0
    for x in candidates:
        t=len(tok(x).input_ids)
        if run+t>budget: break
        out.append(x); run+=t
    return out

def two_stage_corpora(tok,A,B,ans):
    """Target statements on A; five-form lines on B; token-matched statement-only lines on B."""
    Astmt=lines(TRAIN_FORMS["decl"],A,ans,5)
    B5=[f"{list(TRAIN_FORMS.values())[k%5].format(c=c)} {ans[c]}." for k in range(5) for c in B]*5
    Bst=token_matched(tok,lines(TRAIN_FORMS["decl"],B,ans,100),sum(len(tok(x).input_ids) for x in B5))
    return Astmt,B5,Bst

def sentences(blob): return [x for x in re.split(r"(?<=[.!?])\s+|\n\n",blob) if x.strip()]

def build_corpus(tok,blob,inj,seed):
    """Interleave the training lines into the text at sentence granularity, uniformly spaced, in seeded random order."""
    base=sentences(blob); inj=list(inj); np.random.default_rng(seed).shuffle(inj)
    out=[]; bi=0; step=len(base)/len(inj)
    for k,s in enumerate(inj):
        upto=int((k+1)*step); out.extend(base[bi:upto]); bi=upto; out.append(s)
    out.extend(base[bi:])
    ids=tok(" ".join(out)).input_ids; n=len(ids)//SEQ
    return torch.tensor(ids[:n*SEQ]).view(n,SEQ)

def train(m,data,seed,steps=1200,lr=5e-5,params=None,before_micro=None,after_step=None):
    """AdamW (weight decay 0.01), micro-batch 2 x accumulation 4, clip 1.0, sequential passes over a seeded permutation.
    before_micro(rows) runs before each forward; after_step(k) runs after update k and may return True to stop."""
    micro,accum=2,4; params=list(m.parameters()) if params is None else params
    torch.manual_seed(seed); r=np.random.default_rng(seed); m.train()
    opt=torch.optim.AdamW(params,lr=lr,weight_decay=0.01); order=r.permutation(data.shape[0]); ptr=0
    for step in range(steps):
        for _ in range(accum):
            if ptr+micro>len(order): order=r.permutation(data.shape[0]); ptr=0
            rows=order[ptr:ptr+micro]; ptr+=micro
            if before_micro: before_micro(rows)
            b=data[rows].to(dev); (m(input_ids=b,labels=b).loss/accum).backward()
        torch.nn.utils.clip_grad_norm_(params,1.0); opt.step(); opt.zero_grad(set_to_none=True)
        if after_step and after_step(step+1): break
    m.eval(); return m
