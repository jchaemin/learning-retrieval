"""Scoring of trained models.

  python scripts/evaluate.py preamble         --arm {CTRL,FIVE} --seed S               App. B
  python scripts/evaluate.py earlier-training --arm {INCORRECT,CURRENCY} --seed S      Table 3
  python scripts/evaluate.py five-relations   [--model pythia-1.4b] --arm {CTRL,FIVE} --seed S   Table 2, App. F
  python scripts/evaluate.py generality       --model {pythia-410m,pythia-1.4b,qwen2.5-1.5b,llama-3.2-1b,lora} --seed S   App. F
"""
import os,sys,json,argparse,torch
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from retrieval.core import *
from retrieval import measure

def preamble(a):
    P="The following is a short note written on a quiet afternoon. It covers several unrelated topics in no particular order, and it continues below. Read on."
    tok,_,_,capof,A,_=capitals("pythia-410m"); evA=A[:300]; assert len(tok(P).input_ids)==30
    m=model(MODELS["pythia-410m"],ckpt("two_stage","pythia-410m",f"{a.arm}_s{a.seed}","final.pt"))
    F={"decl":FRAMES["decl"],"list":FRAMES["list"],"list_is":LIST_IS,"decl_colon":FRAMES["decl_colon"]}
    dump({f:{"gen":measure.accuracy(m,tok,[P+" "+t.format(c=c) for c in evA],[capof[c] for c in evA])} for f,t in F.items()},result("preamble",f"{a.arm}_s{a.seed}.json"))

def earlier_training(a):
    tok,_,_,capof,A,_=capitals("pythia-410m"); evA=A[:300]
    m=model(MODELS["pythia-410m"],ckpt("earlier_training",f"{a.arm}_s{a.seed}","final.pt"))
    dump({f:{"gen":measure.accuracy(m,tok,[FRAMES[f].format(c=c) for c in evA],[capof[c] for c in evA])} for f in ("list","decl_colon")},result("earlier_training",f"{a.arm}_s{a.seed}.json"))

def five_relations(a):
    W=json.load(open(result("five_relations","world.json"))); tok=tokenizer(MODELS[a.model])
    forms=["decl","list"]+((["list_is"] if a.arm=="CTRL" else [])+["decl_colon"] if a.model=="pythia-410m" else [])
    T={f:relation_form(LIST_IS if f=="list_is" else FRAMES[f]) for f in forms}
    def form(f,r,e): rel,Rel,_=W["relations"][r]; return T[f].format(rel=rel,Rel=Rel,c=e)
    m=model(MODELS[a.model],ckpt("five_relations",a.model,f"{a.arm}_s{a.seed}","final.pt"))
    dump({r:{f:{"gen":measure.accuracy(m,tok,[form(f,r,e) for e in W["entities"][r][:200]],W["answers"][r][:200],bs=100)} for f in T} for r in W["relations"]},
         result("five_relations",a.model,f"{a.arm}_s{a.seed}.json"))

def generality(a):
    base=MODELS.get(a.model,MODELS["pythia-410m"]); src=("lora",) if a.model=="lora" else ("two_stage",a.model)
    tok,_,_,capof,A,_=capitals("pythia-410m" if a.model=="lora" else a.model); evA=A[:300]; Ssel=A[300:600]
    m=model(base); B=measure.blocks(m)
    def arm(x): m.load_state_dict(torch.load(ckpt(*src,f"{x}_s{a.seed}","final.pt"),map_location="cpu")); m.eval()
    run=lambda tpl,items,l=None,d=None: measure.held(m,tok,[tpl.format(c=c) for c in items],[capof[c] for c in items],B[l] if l is not None else None,measure.add(d) if l is not None else None)
    R={}
    arm("FIVE"); R["FIVE"]=run(FRAMES["list"],evA)
    arm("CTRL"); R["CTRL"]=run(FRAMES["list"],evA)
    R["list_is"]=run(LIST_IS,evA); R["decl_colon"]=run(FRAMES["decl_colon"],evA)
    best=None
    for l in (4,6,8,10,12):
        r=measure.mean_hidden(m,tok,[FRAMES["decl"].format(c=c) for c in Ssel],l+1)-measure.mean_hidden(m,tok,[FRAMES["list"].format(c=c) for c in Ssel],l+1)
        for b in (0.5,1.0,1.5,2.0):
            v=run(FRAMES["list"],Ssel,l,b*r)
            if best is None or v["gen"]>best[0]: best=(v["gen"],l,b,r)
    _,l,b,r=best
    if a.model=="pythia-1.4b": p=ckpt("vectors","generality",f"{a.model}_s{a.seed}.pt"); os.makedirs(os.path.dirname(p),exist_ok=True); torch.save({"layer":l,"beta":b},p)
    R["vector"]=run(FRAMES["list"],evA,l,b*r)
    dump(R,result("generality",f"{a.model}_s{a.seed}.json"))

ARMS=["CTRL","FIVE"]
REPORTED={"preamble":grid(model=[None],arm=ARMS,seed=S8),"earlier-training":grid(model=[None],arm=["INCORRECT","CURRENCY"],seed=S8),
 "five-relations":grid(model=["pythia-410m","pythia-1.4b"],arm=ARMS,seed=S8),
 "generality":grid(model=["pythia-410m","pythia-1.4b","qwen2.5-1.5b","lora"],arm=[None],seed=S8)|grid(model=["llama-3.2-1b"],arm=[None],seed=S4)}

EVALS={"preamble":preamble,"earlier-training":earlier_training,"five-relations":five_relations,"generality":generality}
if __name__=="__main__":
    ap=argparse.ArgumentParser(description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("evaluation",choices=list(EVALS)); ap.add_argument("--seed",type=int,required=True); ap.add_argument("--arm")
    ap.add_argument("--model")
    a=ap.parse_args()
    if a.evaluation=="five-relations": a.model=a.model or "pythia-410m"
    require(REPORTED[a.evaluation],**{k:getattr(a,k) for k in ("model","arm","seed")}); EVALS[a.evaluation](a)
