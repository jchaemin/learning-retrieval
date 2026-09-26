"""Training experiments. Each writes the checkpoints later commands read and the scores the paper reports for the run.

  python scripts/train.py two-stage       --model M --arm {CTRL,FIVE} --seed S   Section 3, App. A, F   (M: pythia-410m, pythia-1.4b, qwen2.5-1.5b, llama-3.2-1b)
  python scripts/train.py replication     --world {1,2} --arm {CTRL,FIVE} --seed S   App. E
  python scripts/train.py stage1-controls --arm {INCORRECT,CURRENCY} --seed S     Table 3
  python scripts/train.py lora            --arm {CTRL,FIVE} --seed S              App. F
  python scripts/train.py two-token       --arm {CTRL,FIVE} --seed S              App. F
  python scripts/train.py birth-year      --arm {CTRL,FIVE} --seed S              App. F, I
  python scripts/train.py five-relations  [--model pythia-1.4b] --arm {CTRL,FIVE} --seed S   Table 2, App. F
  python scripts/train.py exposure        --arm {D1,D5,D20,D5DECL,D100} --seed S   Fig. 3, App. D   (Pythia-1.4B: --model pythia-1.4b --arm D20)
  python scripts/train.py more-training   --arm {X4800,XLR} --seed S              App. C
  python scripts/train.py shift           --model {pythia-410m,pythia-1.4b,qwen2.5-1.5b,birth-year} --arm {TARGETED,RANDOM} --seed S   Section 5, App. I
                                          (capital models read the directions written by `preprocess.py shift-directions`)
  python scripts/train.py trajectory      --arm {CTRL,FIVE} --seed S              Fig. 2b
"""
import os,sys
if os.environ.get("CUBLAS_WORKSPACE_CONFIG")!=":4096:8":
    os.environ["CUBLAS_WORKSPACE_CONFIG"]=":4096:8"; os.execv(sys.executable,[sys.executable]+sys.argv)
import json,argparse,numpy as np,torch
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from retrieval.core import *
from retrieval import measure

STAGE1_READ={("pythia-410m","CTRL"),("pythia-410m","FIVE"),("pythia-1.4b","CTRL"),("qwen2.5-1.5b","CTRL")}

def stage1(base,tok,blob,inj,seed): return train(model(base),build_corpus(tok,blob,inj,seed),seed)

def score(m,tok,forms,items,ans,bs=50): return {f:{"gen":measure.accuracy(m,tok,[t.format(c=c) for c in items],[ans[c] for c in items],bs)} for f,t in forms.items()}

def readouts(m,tok,capof,evA):
    """Pythia-410M two-stage scores: every evaluation form, the rewritten list form, and the declarative margin and first-token NLL."""
    out=score(m,tok,{**FRAMES,"list_is":LIST_IS},evA,capof,32)
    pool=sorted({tok(" "+v,add_special_tokens=False).input_ids[0] for v in capof.values()}); pidx={t:i for i,t in enumerate(pool)}
    L=measure.pool_logits(m,tok,[FRAMES["decl"].format(c=c) for c in evA],pool).astype(np.float64)
    T=np.array([pidx[tok(" "+capof[c],add_special_tokens=False).input_ids[0]] for c in evA]); i=np.arange(len(evA)); c=L[i,T].copy(); L[i,T]=-np.inf
    out["margin"]=float((c-L.max(1)).mean()); nll=[]
    with torch.no_grad():
        for x in evA:
            p=tok(FRAMES["decl"].format(c=x)).input_ids; y=tok(" "+capof[x],add_special_tokens=False).input_ids
            nll.append(-torch.log_softmax(m(torch.tensor([p+y],device=dev)).logits[0].float(),-1)[len(p)-1,y[0]].item())
    out["first_token_nll"]=float(np.mean(nll))
    return out

def two_stage(a):
    base=MODELS[a.model]; CD=ckpt("two_stage",a.model,f"{a.arm}_s{a.seed}")
    tok,blob,_,capof,A,B=capitals(a.model); evA=A[:300]
    Astmt,B5,Bst=two_stage_corpora(tok,A,B,capof)
    m=stage1(base,tok,blob,{"CTRL":Bst,"FIVE":B5}[a.arm],a.seed)
    if (a.model,a.arm) in STAGE1_READ: save(m,f"{CD}/stage1.pt")
    m=train(m,build_corpus(tok,blob,Astmt,a.seed+7),a.seed+7); save(m,f"{CD}/final.pt")
    out=readouts(m,tok,capof,evA) if a.model=="pythia-410m" else score(m,tok,{"decl":FRAMES["decl"]},evA,capof,32)
    dump(out,result("two_stage",a.model,f"{a.arm}_s{a.seed}","scores.json"))

def replication(a):
    W=json.load(open(result("replications",f"world{a.world}","world.json"))); base=MODELS["pythia-410m"]
    tok=tokenizer(base); blob=open(BLOB).read(); capof=dict(zip(W["countries"],W["capitals"])); A=W["countries"][:1000]; B=W["countries"][1000:2000]; evA=A[:300]
    Astmt,B5,Bst=two_stage_corpora(tok,A,B,capof)
    m=stage1(base,tok,blob,{"CTRL":Bst,"FIVE":B5}[a.arm],a.seed)
    m=train(m,build_corpus(tok,blob,Astmt,a.seed+7),a.seed+7)
    pool=sorted({tok(" "+v,add_special_tokens=False).input_ids[0] for v in capof.values()}); true=[pool.index(tok(" "+capof[c],add_special_tokens=False).input_ids[0]) for c in evA]
    Z=measure.pool_logits(m,tok,[FRAMES["list"].format(c=c) for c in evA],pool)
    dump({"list":{"pool1":float((Z.argmax(1)==np.array(true)).mean())}},result("replications",f"world{a.world}",f"{a.arm}_s{a.seed}","scores.json"))

def stage1_controls(a):
    base=MODELS["pythia-410m"]; tok,blob,C,capof,A,B=capitals("pythia-410m"); curof=dict(zip(C["countries"],C["currencies"]))
    if a.arm=="CURRENCY":
        CUR=["Currency of {c}:","The currency of {c} is"]
        inj=[f"{CUR[k%2].format(c=c)} {curof[c]}." for k in range(5) for c in B]*5
    else:
        dr=np.random.default_rng(20260917+a.seed)
        while True:
            perm=dr.permutation(len(B))
            if not np.any(perm==np.arange(len(B))): break
        wrong={c:capof[B[perm[i]]] for i,c in enumerate(B)}
        inj=lines(TRAIN_FORMS["kv"],B,wrong,25)
    m=stage1(base,tok,blob,inj,a.seed)
    m=train(m,build_corpus(tok,blob,lines(TRAIN_FORMS["decl"],A,capof,5),a.seed+7),a.seed+7); save(m,ckpt("stage1_controls",f"{a.arm}_s{a.seed}","final.pt"))

def lora(a):
    from peft import LoraConfig, get_peft_model
    base=MODELS["pythia-410m"]; tok,blob,_,capof,A,_=capitals("pythia-410m"); evA=A[:300]
    data=build_corpus(tok,blob,lines(TRAIN_FORMS["decl"],A,capof,5),a.seed+7)
    m=model(base,ckpt("two_stage","pythia-410m",f"{a.arm}_s{a.seed}","stage1.pt"))
    m=get_peft_model(m,LoraConfig(r=64,lora_alpha=128,target_modules=["query_key_value","dense","dense_h_to_4h","dense_4h_to_h"],lora_dropout=0.0,bias="none",task_type="CAUSAL_LM"))
    train(m,data,a.seed+7,steps=2400,lr=3e-4,params=[p for p in m.parameters() if p.requires_grad])
    m=m.merge_and_unload(); m.eval(); save(m,ckpt("lora",f"{a.arm}_s{a.seed}","final.pt"))
    dump(score(m,tok,{"decl":FRAMES["decl"]},evA,capof),result("lora",f"{a.arm}_s{a.seed}","scores.json"))

def two_token(a):
    base=MODELS["pythia-410m"]; tok,blob,C=load(base); W=json.load(open(result("two_token","world.json")))
    ctry=C["countries"]; capof=dict(zip(ctry,W["capitals"])); A=ctry[:1000]; B=ctry[1000:2000]; evA=A[:300]
    Astmt,B5,Bst=two_stage_corpora(tok,A,B,capof)
    stages=[({"FIVE":B5,"CTRL":Bst}[a.arm],a.seed+11),(Astmt,a.seed+7)]; data=[build_corpus(tok,blob,inj,s) for inj,s in stages]
    m=model(base)
    for d,(_,s) in zip(data,stages): train(m,d,s)
    out=score(m,tok,{f:FRAMES[f] for f in ("decl","list")},evA,capof,32)
    if a.arm=="CTRL": save(m,ckpt("two_token",f"CTRL_s{a.seed}","final.pt"))
    dump(out,result("two_token",f"{a.arm}_s{a.seed}","scores.json"))

def birth_year(a):
    base=MODELS["pythia-410m"]; tok,blob,_=load(base); W=json.load(open(result("birth_year","world.json"))); byof=dict(zip(W["people"],W["years"])); ev=W["people"][:300]
    data=build_corpus(tok,blob,lines(BIRTH_YEAR["decl"],W["people"],byof,5),a.seed+7)
    m=model(base,ckpt("two_stage","pythia-410m",f"{a.arm}_s{a.seed}","stage1.pt"))
    train(m,data,a.seed+7)
    out=score(m,tok,{f:BIRTH_YEAR[f] for f in {"FIVE":["decl","list"],"CTRL":["decl","list","list_is","decl_colon"]}[a.arm]},ev,byof)
    if a.arm=="CTRL": save(m,ckpt("birth_year",f"CTRL_s{a.seed}","final.pt"))
    dump(out,result("birth_year",f"{a.arm}_s{a.seed}","scores.json"))

def five_relations(a):
    base=MODELS[a.model]; W=json.load(open(result("five_relations","world.json"))); tok,blob,_=load(base)
    T={f:relation_form(t) for f,t in TRAIN_FORMS.items()}
    def fr(f,r,e): rel,Rel,Wh=W["relations"][r]; return T[f].format(rel=rel,Rel=Rel,Wh=Wh,c=e)
    FA=[(r,W["entities"][r][i],W["answers"][r][i]) for r in W["relations"] for i in range(0,200)]
    FB=[(r,W["entities"][r][i],W["answers"][r][i]) for r in W["relations"] for i in range(200,400)]
    Astmt=[f"{fr('decl',r,e)} {x}." for r,e,x in FA]*5
    B5=[f"{fr(list(T)[k],r,e)} {x}." for k in range(5) for r,e,x in FB]*5
    Bst=token_matched(tok,[f"{fr('decl',r,e)} {x}." for r,e,x in FB]*100,sum(len(tok(x).input_ids) for x in B5))
    m=stage1(base,tok,blob,{"FIVE":B5,"CTRL":Bst}[a.arm],a.seed)
    m=train(m,build_corpus(tok,blob,Astmt,a.seed+7),a.seed+7); save(m,ckpt("five_relations",a.model,f"{a.arm}_s{a.seed}","final.pt"))

def exposure(a):
    base=MODELS[a.model]; tok,blob,_,capof,A,_=capitals(a.model); evA=A[:300]
    FORMS=[TRAIN_FORMS[k] for k in ("decl","kv","qa","dlg","imper")]
    budget=sum(len(tok(x).input_ids) for x in lines(TRAIN_FORMS["decl"],A,capof,5))
    if a.arm=="D100":
        cand=[f"{FORMS[i%5].format(c=c)} {capof[c]}." for i,c in enumerate([c for c in A for _ in range(5)])]
    else:
        PARAS=["The capital of {c} is","{c}'s capital is","The capital city of {c} is","The city that serves as the capital of {c} is","In {c}, the capital is"]
        k={"D1":10,"D5":50,"D20":200,"D5DECL":50}[a.arm]; forms=PARAS if a.arm=="D5DECL" else FORMS
        order=list(np.random.default_rng(a.seed+41).permutation(len(A)-300)+300); shown=[A[i] for i in order[:k]]; rest=[A[i] for i in order[k:]]
        cand=[f"{forms[j].format(c=c)} {capof[c]}." for c in shown for j in range(5)]+[f"{TRAIN_FORMS['decl'].format(c=c)} {capof[c]}." for c in evA+rest for j in range(5)]
    data=build_corpus(tok,blob,token_matched(tok,cand,budget),a.seed+7)
    m=model(base,ckpt("two_stage",a.model,f"CTRL_s{a.seed}","stage1.pt"))
    train(m,data,a.seed+7)
    scored=["list","decl_colon"] if a.model=="pythia-410m" else ["list"]
    RD=("exposure",a.model,f"{a.arm}_s{a.seed}")
    dump(score(m,tok,{f:FRAMES[f] for f in scored},evA,capof),result(*RD,"scores.json"))
    if a.arm=="D100": dump({"forms":FORMS},result(*RD,"forms.json"))

def more_training(a):
    base=MODELS["pythia-410m"]; tok,blob,_,capof,A,_=capitals("pythia-410m"); evA=A[:300]
    data=build_corpus(tok,blob,lines(TRAIN_FORMS["decl"],A,capof,5),a.seed+7)
    target=json.load(open(result("two_stage","pythia-410m",f"CTRL_s{a.seed}","scores.json")))["decl"]["gen"]-0.01
    m=model(base,ckpt("two_stage","pythia-410m",f"CTRL_s{a.seed}","stage1.pt"))
    acc=lambda tpl: measure.accuracy(m,tok,[tpl.format(c=c) for c in evA],[capof[c] for c in evA]); stop=[]
    def check(k):
        if a.arm!="XLR" or k%200: return False
        m.eval(); d=acc(FRAMES["decl"]); m.train()
        if d>=target-1e-9: stop.append(k); return True
    train(m,data,a.seed+7,steps={"X4800":4800,"XLR":9600}[a.arm],lr={"X4800":5e-5,"XLR":1e-5}[a.arm],after_step=check)
    out={f:{"gen":acc(t)} for f,t in (("decl",FRAMES["decl"]),("list",FRAMES["list"]),("list_is",LIST_IS),("decl_colon",FRAMES["decl_colon"]))}
    if a.arm=="XLR": out["stopped_at"]=stop[0]
    dump(out,result("more_training",f"{a.arm}_s{a.seed}","scores.json"))

def answer_positions(tok,blob,lines_,seed,kinds):
    """The corpus of build_corpus(lines_, seed), and for each block the (column, kind) of every line's answer position."""
    base=sentences(blob); inj=list(lines_); np.random.default_rng(seed).shuffle(inj)
    pieces=[]; bi=0; step=len(base)/len(inj); slot=[]
    for k,s in enumerate(inj):
        upto=int((k+1)*step); pieces.extend(base[bi:upto]); bi=upto; slot.append(len(pieces)); pieces.append(s)
    pieces.extend(base[bi:]); text=" ".join(pieces)
    starts=[]; cpos=0
    for p in pieces: starts.append(cpos); cpos+=len(p)+1
    enc=tok(text,return_offsets_mapping=True); ids=enc["input_ids"]; ends=np.array(enc["offset_mapping"])[:,1]
    n=len(ids)//SEQ; data=torch.tensor(ids[:n*SEQ]).view(n,SEQ)
    assert torch.equal(data,build_corpus(tok,blob,lines_,seed))
    kdraw=kinds(len(inj)); pos={}
    for k,s in enumerate(inj):
        i=int(np.searchsorted(ends,starts[slot[k]]+s.rindex(" ")-1,side="right"))
        if i<n*SEQ: pos.setdefault(i//SEQ,[]).append((i%SEQ,int(kdraw[k])))
    return data,pos

def shift(a):
    by=a.model=="birth-year"; name="pythia-410m" if by else a.model; base=MODELS[name]
    tok,blob,C=load(base)
    if by:
        W=json.load(open(result("birth_year","world.json"))); ans=dict(zip(W["people"],W["years"])); ev=W["people"][:300]; T=BIRTH_YEAR
        train_lines=lines(BIRTH_YEAR["decl"],W["people"],ans,5)
    else:
        ctry=C["countries"]; ans=dict(zip(ctry,C["capitals"])); ev=ctry[:300]; T=FRAMES
        train_lines=lines(TRAIN_FORMS["decl"],ctry[:1000],ans,5)
    KINDS=["none","list","kv","qa"]
    data,POS=answer_positions(tok,blob,train_lines,a.seed+7,lambda n: np.random.default_rng(5200+a.seed).integers(0,len(KINDS),size=n))
    m=model(base,ckpt("two_stage",name,f"CTRL_s{a.seed}","stage1.pt"))
    if by:
        H={f:measure.running_mean_hidden(m,tok,[BIRTH_YEAR[f].format(c=p) for p in W["people"][600:1000]],5) for f in ("decl","list","kv","qa")}
        D={f:H[f]-H["decl"] for f in KINDS[1:]}
    else:
        V=torch.load(ckpt("vectors","shift",name,f"directions_s{a.seed}.pt"),map_location="cpu"); D={f:V[f].to(dev) for f in KINDS[1:]}
    if a.arm=="RANDOM":
        g=torch.Generator(device=dev); g.manual_seed(5100+a.seed)
        D={f:(lambda z: z*(D[f].norm()/z.norm()))(torch.randn(D[f].shape,generator=g,device=dev)) for f in KINDS[1:]}
    RV={k:D[f] for k,f in enumerate(KINDS) if k}
    CUR=[]
    def hk(mod,inp,out):
        o=out[0] if isinstance(out,tuple) else out
        if CUR:
            o=o.clone()
            for row,col,kd in CUR: o[row,col,:]=o[row,col,:]+RV[kd]
        return (o,)+tuple(out[1:]) if isinstance(out,tuple) else o
    h=measure.blocks(m)[4].register_forward_hook(hk)
    def pick(rows): CUR[:]=[(row,col,kd) for row,blk in enumerate(rows) for (col,kd) in POS.get(int(blk),[]) if kd>0]
    train(m,data,a.seed+7,before_micro=pick); CUR.clear(); h.remove()
    out=score(m,tok,{f:T[f] for f in ("decl","decl_colon")},ev,ans)
    if a.model=="pythia-410m":
        hids=tok(open(HELDOUT).read()).input_ids; nh=len(hids)//SEQ; HD=torch.tensor(hids[:nh*SEQ]).view(nh,SEQ); tot=0.0; cnt=0
        with torch.no_grad():
            for i in range(0,HD.shape[0],16):
                b=HD[i:i+16].to(dev); lg=m(b).logits[:,:-1,:].float(); t=b[:,1:]
                tot+=float(torch.nn.functional.cross_entropy(lg.reshape(-1,lg.shape[-1]),t.reshape(-1),reduction="sum")); cnt+=t.numel()
        out["heldout_nll"]=tot/cnt
    dump(out,result("shift","birth_year" if by else a.model,f"{a.arm}_s{a.seed}","scores.json"))

def trajectory(a):
    base=MODELS["pythia-410m"]; tok,blob,_,capof,A,_=capitals("pythia-410m"); evA=A[:300]
    PR={f:[FRAMES[f].format(c=c) for c in evA] for f in ("decl","list")}
    ANS=torch.tensor([tok(" "+capof[c],add_special_tokens=False).input_ids for c in evA]); assert ANS.shape==(300,2)
    pool=sorted({tok(" "+v,add_special_tokens=False).input_ids[0] for v in capof.values()}); POOLT=torch.tensor(pool); pidx={t:i for i,t in enumerate(pool)}; PIDX=torch.tensor([pidx[int(t)] for t in ANS[:,0]])
    m=model(base,ckpt("two_stage","pythia-410m",f"{a.arm}_s{a.seed}","stage1.pt"))
    data=build_corpus(tok,blob,lines(TRAIN_FORMS["decl"],A,capof,5),a.seed+7)
    def top1(f):
        e=tok(PR[f],return_tensors="pt",padding=True).to(dev); ans=ANS.to(dev)
        lg=m(input_ids=torch.cat([e.input_ids,ans],1),attention_mask=torch.cat([e.attention_mask,torch.ones_like(ans)],1)).logits.float()
        return float((lg[:,-3,:][:,POOLT.to(dev)].argmax(1)==PIDX.to(dev)).float().mean())
    pts=[]; acc_decl=[]; acc_list=[]
    def record(k):
        m.eval(); pts.append(k); acc_decl.append(top1("decl")); acc_list.append(top1("list")); m.train()
    m.train(); record(0)
    train(m,data,a.seed+7,after_step=lambda k: record(k) if k%50==0 else None)
    np.savez_compressed(result("trajectory",f"{a.arm}_s{a.seed}","trajectory.npz"),acc_decl=np.array(acc_decl),acc_list=np.array(acc_list),points=np.array(pts))

ARMS=["CTRL","FIVE"]
REPORTED={
 "two-stage":grid(model=["pythia-410m","pythia-1.4b","qwen2.5-1.5b"],world=[None],arm=ARMS,seed=S8)|grid(model=["llama-3.2-1b"],world=[None],arm=ARMS,seed=S4),
 "replication":grid(model=[None],world=[1],arm=ARMS,seed=S8)|grid(model=[None],world=[2],arm=ARMS,seed=range(16)),
 "stage1-controls":grid(model=[None],world=[None],arm=["INCORRECT","CURRENCY"],seed=S8),
 "lora":grid(model=[None],world=[None],arm=ARMS,seed=S8),"two-token":grid(model=[None],world=[None],arm=ARMS,seed=S8),"birth-year":grid(model=[None],world=[None],arm=ARMS,seed=S8),"trajectory":grid(model=[None],world=[None],arm=ARMS,seed=S8),
 "five-relations":grid(model=["pythia-410m","pythia-1.4b"],world=[None],arm=ARMS,seed=S8),
 "exposure":grid(model=["pythia-410m"],world=[None],arm=["D1","D5","D20","D5DECL","D100"],seed=S8)|grid(model=["pythia-1.4b"],world=[None],arm=["D20"],seed=S8),
 "more-training":grid(model=[None],world=[None],arm=["X4800","XLR"],seed=S8),
 "shift":grid(model=["pythia-410m","pythia-1.4b","qwen2.5-1.5b"],world=[None],arm=["TARGETED","RANDOM"],seed=S8)|grid(model=["birth-year"],world=[None],arm=["TARGETED","RANDOM"],seed=S4)}

EXPERIMENTS={"two-stage":two_stage,"replication":replication,"stage1-controls":stage1_controls,"lora":lora,"two-token":two_token,"birth-year":birth_year,
             "five-relations":five_relations,"exposure":exposure,"more-training":more_training,"shift":shift,"trajectory":trajectory}
if __name__=="__main__":
    ap=argparse.ArgumentParser(description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("experiment",choices=list(EXPERIMENTS)); ap.add_argument("--seed",type=int,required=True); ap.add_argument("--arm",required=True)
    ap.add_argument("--model"); ap.add_argument("--world",type=int,choices=[1,2])
    a=ap.parse_args()
    if a.experiment in ("five-relations","exposure"): a.model=a.model or "pythia-410m"
    require(REPORTED[a.experiment],**{k:getattr(a,k) for k in ("model","world","arm","seed")})
    deterministic(); EXPERIMENTS[a.experiment](a)
