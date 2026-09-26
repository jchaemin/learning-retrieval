"""Interventions on the context state of trained models (held at the prompt-final position on every decoding step).

  python scripts/intervene.py patch              --model {pythia-410m,pythia-1.4b,qwen2.5-1.5b} --seed S   Section 4.1-4.3, App. H
  python scripts/intervene.py patch-layer0       --seed S   App. H, layer 0 and the is-ended rewrite
  python scripts/intervene.py patch-entity       --seed S   Section 4.1, App. H, country token
  python scripts/intervene.py two-token          --seed S   App. F, H: patching, keying and restoring vector in the two-token world
  python scripts/intervene.py list-vector        --seed S   App. J: restoring vector r, layer and scale selected on A[300:600]; cosine with u
  python scripts/intervene.py suffix-bank        --seed S   Section 3.4, App. G
  python scripts/intervene.py direction          --seed S   Section 4.3, App. J: u alone, u removed, removals at matched cosine
  python scripts/intervene.py direction-colon    --seed S   Table 4a, colon-ended declarative form
  python scripts/intervene.py direction-transfer --seed S   Table 4b
  python scripts/intervene.py linear-map         --seed S   App. J: linear map over the seven non-declarative evaluation forms
  python scripts/intervene.py birth-year-vector  --seed S   App. F
  python scripts/intervene.py alignment          --model {pythia-410m,pythia-1.4b} --seed S   Fig. 4
"""
import os,sys,json,argparse,numpy as np,torch
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from retrieval.core import *
from retrieval import measure as M

def world(name):
    tok,_,C,capof,A,_=capitals(name)
    pool=sorted({tok(" "+v,add_special_tokens=False).input_ids[0] for v in capof.values()})
    first=lambda c: tok(" "+capof[c],add_special_tokens=False).input_ids[0]
    return tok,C,capof,A,pool,first
P=lambda tpl,items: [tpl.format(c=c) for c in items]
cos=lambda x,y: float(torch.nn.functional.cosine_similarity(x,y,dim=0))
G=lambda v: {"gen":v["gen"]}
def norm_random(g,like): x=torch.randn(like.shape,generator=g,device=dev); return x*(like.norm(dim=-1,keepdim=True)/x.norm(dim=-1,keepdim=True))
def shifted(x): return x[torch.arange(1,len(x)+1)%len(x)]

def correct_under_decl(m,tok,evA,pool,first): return M.correct_items(m,tok,evA,lambda c: FRAMES["decl"].format(c=c),first,pool)
def u_direction(m,tok,names,layer): return M.mean_hidden(m,tok,[f"The value of {c} is" for c in names],layer)-M.mean_hidden(m,tok,[f"The value of {c}:" for c in names],layer)
def restoring(m,tok,items,layer): return M.mean_hidden(m,tok,P(FRAMES["decl"],items),layer)-M.mean_hidden(m,tok,P(FRAMES["list"],items),layer)
def without(r,uh): rp=r-(r@uh)*uh; return rp*(r.norm()/rp.norm())

def pick_beta(score,vec,grid):
    best=None
    for b in grid:
        v=score(b*vec); key=(-v["gen"],-v["pool1"],b)
        if best is None or key<best[0]: best=(key,b)
    return best[1]

SOURCES={"currency":"The currency of {c} is","population":"The population of {c} is","weather":"The weather today is"}
def patch_table(m,tok,items,ans,layers,seed,R):
    """Replace the list form's final state at hidden_states[l] with a declarative-form, other-relation, entity-free or random state."""
    H=M.hidden(m,tok,P(FRAMES["decl"],items),layers); S={k:M.hidden(m,tok,P(t,items) if k!="weather" else [t]*len(items),layers) for k,t in SOURCES.items()}
    g=torch.Generator(device=dev); g.manual_seed(4800+seed)
    run=lambda l,v: G(M.held(m,tok,P(FRAMES["list"],items),ans,M.site(m,l),M.replace(v)))
    for k in ("same_fact","other_fact",*SOURCES,"random"): R[k]={}
    for l in layers:
        R["same_fact"][str(l)]=run(l,H[l]); R["other_fact"][str(l)]=run(l,shifted(H[l]))
        for k in SOURCES: R[k][str(l)]=run(l,S[k][l])
        R["random"][str(l)]=run(l,norm_random(g,H[l]))
    return R

def patch(a):
    tok,_,capof,A,pool,first=world(a.model); evA=A[:300]; Ssel=A[300:600]; evans=[capof[c] for c in evA]
    m=model(MODELS[a.model],ckpt("two_stage",a.model,f"CTRL_s{a.seed}","final.pt")); B=M.blocks(m)
    items=correct_under_decl(m,tok,evA,pool,first); ans=[capof[c] for c in items]
    R={"unpatched":G(M.held(m,tok,P(FRAMES["list"],items),ans))}
    if a.model!="pythia-410m": R["rewrite"]=G(M.held(m,tok,P(LIST_IS,items),ans))
    patch_table(m,tok,items,ans,list(range(1,7)) if a.model=="pythia-410m" else list(range(0,7)),a.seed,R)
    if a.model=="pythia-1.4b":
        SEL=torch.load(ckpt("vectors","generality",f"pythia-1.4b_s{a.seed}.pt")); l=int(SEL["layer"]); b=float(SEL["beta"])
        r=restoring(m,tok,Ssel,l+1); u=u_direction(m,tok,evA,l+1)
        R["vector"]=dict(r=G(M.held(m,tok,P(FRAMES["list"],evA),evans,B[l],M.add(b*r))),r_u_removed=G(M.held(m,tok,P(FRAMES["list"],evA),evans,B[l],M.add(b*without(r,u/u.norm())))))
    if a.model=="qwen2.5-1.5b":
        u=u_direction(m,tok,evA,5); uh=u/u.norm(); r=restoring(m,tok,Ssel,5)
        sc=lambda d: M.held(m,tok,P(FRAMES["list"],Ssel),[capof[c] for c in Ssel],B[4],M.add(d),pool=pool,first_ids=[first(c) for c in Ssel])
        bR=pick_beta(sc,r,(0.5,1.0,1.5,2.0)); ut=r.norm()*uh; bU=pick_beta(sc,ut,(0.25,0.5,1.0,1.5,2.0,3.0))
        R["vector"]=dict(u_alone=G(M.held(m,tok,P(FRAMES["list"],evA),evans,B[4],M.add(bU*ut))),r_u_removed=G(M.held(m,tok,P(FRAMES["list"],evA),evans,B[4],M.add(bR*without(r,uh)))))
    if a.model!="pythia-1.4b":
        Hl=M.hidden(m,tok,P(FRAMES["list"],items),[5])[5]
        R["reverse"]=dict(unpatched=G(M.held(m,tok,P(FRAMES["decl"],items),ans)),list_state=G(M.held(m,tok,P(FRAMES["decl"],items),ans,B[4],M.replace(Hl))))
    if a.model=="qwen2.5-1.5b":
        Hd=M.hidden(m,tok,P(FRAMES["decl"],items),[5])[5]
        g=torch.Generator(device=dev); g.manual_seed(5300+a.seed); W=torch.randn(Hd.shape,generator=g,device=dev); W=W/W.norm(dim=1,keepdim=True)
        pc=Hd-(Hd@uh).abs()[:,None]*W; pc=pc*(Hd.norm(dim=1,keepdim=True)/pc.norm(dim=1,keepdim=True))
        R["reverse"]["random_removal"]=G(M.held(m,tok,P(FRAMES["decl"],items),ans,B[4],M.replace(pc)))
    dump(R,result("patching",a.model,f"patch_s{a.seed}.json"))

def patch_layer0(a):
    tok,_,capof,A,_,_=world("pythia-410m"); evA=A[:300]; ans=[capof[c] for c in evA]
    m=model(MODELS["pythia-410m"],ckpt("two_stage","pythia-410m",f"CTRL_s{a.seed}","final.pt")); E=M.embed(m)
    H0=M.hidden(m,tok,P(FRAMES["decl"],evA),[0])[0]; g=torch.Generator(device=dev); g.manual_seed(4700+a.seed)
    run=lambda v: G(M.held(m,tok,P(FRAMES["list"],evA),ans,E,M.replace(v)))
    dump(dict(rewrite=G(M.held(m,tok,P(LIST_IS,evA),ans)),same_fact=run(H0),other_fact=run(shifted(H0)),random=run(norm_random(g,H0))),
         result("patching","pythia-410m",f"layer0_s{a.seed}.json"))

def patch_entity(a):
    tok,_,capof,A,pool,first=world("pythia-410m"); evA=A[:300]
    m=model(MODELS["pythia-410m"],ckpt("two_stage","pythia-410m",f"CTRL_s{a.seed}","final.pt"))
    items=correct_under_decl(m,tok,evA,pool,first); ans=[capof[c] for c in items]
    def cpos(tpl,c):
        pre=tpl.split("{c}")[0]; ids=tok(tpl.format(c=c)).input_ids; head=tok(pre+c).input_ids
        assert ids[:len(head)]==head; return len(head)-1
    def positions(tpl): return lambda i,n,L: torch.tensor([L-len(tok(tpl.format(c=c)).input_ids)+cpos(tpl,c) for c in items[i:i+n]],device=dev)
    S=[]
    with torch.no_grad():
        for i in range(0,len(items),50):
            ch=items[i:i+50]; e=tok(P(FRAMES["decl"],ch),return_tensors="pt",padding=True).to(dev); pos=positions(FRAMES["decl"])(i,len(ch),e.input_ids.shape[1]); ar=torch.arange(len(ch),device=dev)
            hs=m(**e,output_hidden_states=True).hidden_states; S.append(torch.stack([hs[l][ar,pos,:] for l in range(7)],1).float())
    S=torch.cat(S); g=torch.Generator(device=dev); g.manual_seed(4200+a.seed); R={"same_fact":{},"other_fact":{},"random":{}}
    run=lambda l,v: G(M.held(m,tok,P(FRAMES["list"],items),ans,M.site(m,l),M.replace(v),position=positions(FRAMES["list"])))
    for l in range(7):
        v=S[:,l,:]; R["same_fact"][str(l)]=run(l,v); R["other_fact"][str(l)]=run(l,shifted(v)); R["random"][str(l)]=run(l,norm_random(g,v))
    dump(R,result("patching","entity_site",f"patch_s{a.seed}.json"))

def two_token(a):
    tok,_,C=load(MODELS["pythia-410m"]); W=json.load(open(result("two_token","world.json")))
    ctry=C["countries"]; capof=dict(zip(ctry,W["capitals"])); evA=ctry[:300]; Ssel=ctry[300:600]
    m=model(MODELS["pythia-410m"],ckpt("two_token",f"CTRL_s{a.seed}","final.pt"))
    run=lambda prs,items,l=None,edit=None: G(M.held(m,tok,prs,[capof[c] for c in items],M.site(m,l) if l is not None else None,edit))
    R={"unpatched":run(P(FRAMES["list"],evA),evA),"same_fact":{},"other_fact":{},"random":{}}; g=torch.Generator(device=dev); g.manual_seed(4800+a.seed)
    for l in range(7):
        Hd=M.hidden(m,tok,P(FRAMES["decl"],evA),[l])[l]
        R["same_fact"][str(l)]=run(P(FRAMES["list"],evA),evA,l,M.replace(Hd))
        R["other_fact"][str(l)]=run(P(FRAMES["list"],evA),evA,l,M.replace(shifted(Hd)))
        R["random"][str(l)]=run(P(FRAMES["list"],evA),evA,l,M.replace(norm_random(g,Hd)))
    dump(R,result("patching","two_token",f"patch_s{a.seed}.json"))
    LAY=[4,6,8,10,12]; Hd=M.hidden(m,tok,P(FRAMES["decl"],Ssel),LAY); Hl=M.hidden(m,tok,P(FRAMES["list"],Ssel),LAY); best=None
    for l in LAY:
        r=Hd[l].mean(0)-Hl[l].mean(0)
        for b in (0.5,1.0,1.5,2.0):
            gn=run(P(FRAMES["list"],Ssel),Ssel,l,M.add(b*r))["gen"]
            if best is None or gn>best[0]: best=(gn,l,b)
    _,l,b=best
    dump({"list_is":run(P(LIST_IS,evA),evA),"decl_colon":run(P(FRAMES["decl_colon"],evA),evA),"vector":run(P(FRAMES["list"],evA),evA,l,M.add(b*(Hd[l].mean(0)-Hl[l].mean(0))))},
         result("generality",f"two_token_s{a.seed}.json"))

def list_vector(a):
    tok,_,capof,A,pool,first=world("pythia-410m"); evA=A[:300]; Ssel=A[300:600]
    m=model(MODELS["pythia-410m"],ckpt("two_stage","pythia-410m",f"CTRL_s{a.seed}","final.pt")); B=M.blocks(m)
    LAY=[4,6,8,10,12]; best=None; R={}
    for l in LAY:
        r=restoring(m,tok,Ssel,l+1)
        if l in (4,6,8): R[str(l)]=cos(r,u_direction(m,tok,evA,l+1))
        for b in (0.5,1.0,1.5,2.0):
            v=M.held(m,tok,P(FRAMES["list"],Ssel),[capof[c] for c in Ssel],B[l],M.add(b*r),pool=pool,first_ids=[first(c) for c in Ssel]); key=(-v["gen"],-v["pool1"],b,l)
            if best is None or key<best[0]: best=(key,l,b)
    _,l,b=best; p=ckpt("vectors","list_vector",f"pythia-410m_s{a.seed}.pt"); os.makedirs(os.path.dirname(p),exist_ok=True)
    torch.save(dict(layer=l,beta=b),p); dump({"layer":l,"cos_u":R},result("direction",f"list_vector_s{a.seed}.json"))

def selected(a):
    SD=torch.load(ckpt("vectors","list_vector",f"pythia-410m_s{a.seed}.pt")); return SD["layer"],SD["beta"]

BANK=["- Capital of {c}:",
      "{c}'s capital is","{c}'s capital city is","For {c}, the capital is",
      "The capital city for {c} is","The capital in {c} is","The seat of government for {c} is","The chief city in {c} is",
      "The capital city of {c} is","- Capital of {c} is","The seat of government of {c} is","The main city of {c} is",
      "I know that the capital of {c} is","The city that is the capital of {c} is","Indeed, the capital of {c} is","So the capital of {c} is"]

def suffix_bank(a):
    tok,_,capof,A,_,_=world("pythia-410m"); evA=A[:300]
    m=model(MODELS["pythia-410m"],ckpt("two_stage","pythia-410m",f"CTRL_s{a.seed}","final.pt"))
    dump({f:G(M.held(m,tok,P(f,evA),[capof[c] for c in evA])) for f in BANK},result("suffix_bank",f"CTRL_s{a.seed}.json"))

def direction(a):
    tok,_,capof,A,pool,first=world("pythia-410m"); evA=A[:300]; Ssel=A[300:600]
    m=model(MODELS["pythia-410m"],ckpt("two_stage","pythia-410m",f"CTRL_s{a.seed}","final.pt")); l,br=selected(a); site=M.blocks(m)[l]
    ev=lambda d: G(M.held(m,tok,P(FRAMES["list"],evA),[capof[c] for c in evA],site,M.add(d)))
    sel=lambda d: M.held(m,tok,P(FRAMES["list"],Ssel),[capof[c] for c in Ssel],site,M.add(d),pool=pool,first_ids=[first(c) for c in Ssel])
    u=u_direction(m,tok,evA,l+1); uh=u/u.norm()
    r=restoring(m,tok,Ssel,l+1); rh=r/r.norm(); c=cos(r,u); resc=lambda x: x*(r.norm()/x.norm())
    R={"r":ev(br*r),"r_u_removed":ev(br*without(r,uh))}
    ut=r.norm()*uh; bu=pick_beta(sel,ut,(0.25,0.5,1.0,1.5,2.0,3.0)); R["u_alone"]=dict(beta=bu,**ev(bu*ut))
    vm=2*c*rh-uh; vm=vm/vm.norm(); R["mirror"]=dict(cos_v_u=cos(vm,u),**ev(br*resc(r-(r@vm)*vm)))
    g=torch.Generator(device=dev); g.manual_seed(5800+a.seed); gens=[]; cu=[]
    for k in range(10):
        w=torch.randn(u.shape[0],generator=g,device=dev); w=w-(w@rh)*rh; w=w/w.norm(); v=c*rh+np.sqrt(1-c*c)*w; v=v/v.norm(); cu.append(cos(v,u))
        gens.append(ev(br*resc(r-(r@v)*v))["gen"])
    R["random_same_cos"]=dict(cos_v_u=float(np.mean(cu)),gen=float(np.mean(gens)))
    dump(R,result("direction",f"direction_s{a.seed}.json"))

def direction_colon(a):
    tok,_,capof,A,pool,first=world("pythia-410m"); evA=A[:300]; Ssel=A[300:600]; tpl=FRAMES["decl_colon"]
    m=model(MODELS["pythia-410m"],ckpt("two_stage","pythia-410m",f"CTRL_s{a.seed}","final.pt")); l,_=selected(a); site=M.blocks(m)[l]
    ev=lambda d=None: G(M.held(m,tok,P(tpl,evA),[capof[c] for c in evA],site if d is not None else None,M.add(d) if d is not None else None))
    sel=lambda d: M.held(m,tok,P(tpl,Ssel),[capof[c] for c in Ssel],site,M.add(d),pool=pool,first_ids=[first(c) for c in Ssel])
    u=u_direction(m,tok,evA,l+1); vec=(M.mean_hidden(m,tok,P(FRAMES["decl"],Ssel),l+1)-M.mean_hidden(m,tok,P(tpl,Ssel),l+1)).norm()*u/u.norm()
    b=pick_beta(sel,vec,(0.25,0.5,1.0,1.5,2.0,3.0))
    dump({"unpatched":ev(),"u":ev(b*vec)},result("direction",f"colon_s{a.seed}.json"))

def direction_transfer(a):
    tok,_,capof,A,pool,_=world("pythia-410m"); WB=json.load(open(result("birth_year","world.json"))); byof=dict(zip(WB["people"],WB["years"]))
    D={"capital":dict(ev=A[:300],sel=A[300:600],ans=capof,pool=pool,decl=FRAMES["decl"],list=FRAMES["list"],ck=ckpt("two_stage","pythia-410m",f"CTRL_s{a.seed}","final.pt")),
       "birth_year":dict(ev=WB["people"][:300],sel=WB["people"][300:600],ans=byof,pool=WB["pool_first_token_ids"],decl=BIRTH_YEAR["decl"],list=BIRTH_YEAR["list"],ck=ckpt("birth_year",f"CTRL_s{a.seed}","final.pt"))}
    m=model(MODELS["pythia-410m"]); l,_=selected(a); site=M.blocks(m)[l]; OTHER={"capital":"birth_year","birth_year":"capital"}
    def use(w): m.load_state_dict(torch.load(D[w]["ck"],map_location="cpu")); m.eval(); return D[w]
    def run(W,items,d): return M.held(m,tok,P(W["list"],items),[W["ans"][x] for x in items],site,M.add(d))
    def sel(W,d): return M.held(m,tok,P(W["list"],W["sel"]),[W["ans"][x] for x in W["sel"]],site,M.add(d),pool=W["pool"],first_ids=[tok(" "+W["ans"][x],add_special_tokens=False).input_ids[0] for x in W["sel"]])
    U={}; RN={}
    for w in ("capital","birth_year"):
        W=use(w); U[w]=u_direction(m,tok,W["ev"],l+1)
        if w=="capital": UX=u_direction(m,tok,D["birth_year"]["ev"],l+1)
        RN[w]=(M.mean_hidden(m,tok,P(W["decl"],W["sel"]),l+1)-M.mean_hidden(m,tok,P(W["list"],W["sel"]),l+1)).norm()
    R={"cos_u_countries_people":cos(U["capital"],UX)}
    for w in ("capital","birth_year"):
        W=use(w); R[w]={}
        for cond,vec in (("own",U[w]),("transplant",U[OTHER[w]])):
            ut=vec/vec.norm()*RN[w]; b=pick_beta(lambda d: sel(W,d),ut,(0.25,0.5,1.0,1.5,2.0,3.0))
            R[w][cond]=G(run(W,W["ev"],b*ut))
    dump(R,result("direction",f"transfer_s{a.seed}.json"))

def linear_map(a):
    tok,C,capof,A,_,_=world("pythia-410m"); evA=A[:300]; Bc=C["countries"][1000:2000]; FIT=Bc[:600]; VAL=Bc[600:1000]
    NONDECL=[f for f in FRAMES if f!="decl"]
    m=model(MODELS["pythia-410m"],ckpt("two_stage","pythia-410m",f"CTRL_s{a.seed}","final.pt")); l,_=selected(a); site=M.blocks(m)[l]; d=m.config.hidden_size
    S={s:{f:M.hidden(m,tok,P(t,items),[l+1],dtype=torch.double)[l+1] for f,t in FRAMES.items()} for s,items in (("fit",FIT),("val",VAL))}
    def pairs(s): return torch.cat([S[s][f] for f in NONDECL]),torch.cat([S[s]["decl"]]*len(NONDECL))
    def ridge(rank=None):
        X,Y=pairs("fit"); Xv,Yv=pairs("val"); mx=X.mean(0); my=Y.mean(0); Xc=X-mx; Yc=Y-my; Gm=Xc.T@Xc; base=torch.trace(Gm)/d; best=None; I=torch.eye(d,dtype=Gm.dtype,device=dev)
        for al in [1e-4,1e-3,1e-2,1e-1,1.0,10.0]:
            W=torch.linalg.solve(Gm+al*base*I,Xc.T@Yc)
            if rank is not None: _,_,Vh=torch.linalg.svd(Xc@W,full_matrices=False); W=W@(Vh[:rank].T@Vh[:rank])
            b=my-mx@W; mse=float(((Xv@W+b-Yv)**2).sum(1).mean())
            if best is None or mse<best[0]: best=(mse,W,b)
        return best[1].float(),best[2].float()
    MAPS={"linear":ridge(),"rank16":ridge(rank=16)}
    def fn(v): W,b=MAPS[v]; return lambda h: h@W+b
    dump({f:{v:G(M.held(m,tok,P(FRAMES[f],evA),[capof[c] for c in evA],site,M.apply(fn(v)))) for v in MAPS} for f in ("decl","list")},result("direction",f"linear_map_s{a.seed}.json"))

def birth_year_vector(a):
    tok,_,_=load(MODELS["pythia-410m"]); W=json.load(open(result("birth_year","world.json"))); byof=dict(zip(W["people"],W["years"])); ev=W["people"][:300]; Ssel=W["people"][300:600]
    Q=lambda t,items: [t.format(c=p) for p in items]
    m=model(MODELS["pythia-410m"],ckpt("birth_year",f"CTRL_s{a.seed}","final.pt")); B=M.blocks(m); best=None
    run=lambda items,l,d: G(M.held(m,tok,Q(BIRTH_YEAR["list"],items),[byof[p] for p in items],B[l],M.add(d)))
    for l in (4,6,8,10,12):
        r=M.mean_hidden(m,tok,Q(BIRTH_YEAR["decl"],Ssel),l+1)-M.mean_hidden(m,tok,Q(BIRTH_YEAR["list"],Ssel),l+1)
        for b in (0.5,1.0,1.5,2.0):
            v=run(Ssel,l,b*r)
            if best is None or v["gen"]>best[0]: best=(v["gen"],l,b,r)
    _,l,b,r=best; dump({"vector":run(ev,l,b*r)},result("generality",f"birth_year_s{a.seed}.json"))

def alignment(a):
    tok,_,_,A,_,_=world(a.model); evA=A[:300]; m=model(MODELS[a.model]); R={}; LAY=list(range(1,25))
    def ccos(X,D):
        X=X-X.mean(0); D=D-D.mean(0); return float(((X*D).sum(1)/(X.norm(dim=1)*D.norm(dim=1)).clamp(min=1e-12)).mean())
    for arm in ("CTRL","FIVE"):
        m.load_state_dict(torch.load(ckpt("two_stage",a.model,f"{arm}_s{a.seed}","final.pt"),map_location="cpu")); m.eval()
        S={f:M.hidden(m,tok,P(FRAMES[f],evA),LAY,dtype=torch.double,position_ids=True) for f in ("list","decl")}
        R[arm]={str(l):ccos(S["list"][l],S["decl"][l]) for l in LAY}
        del S; torch.cuda.empty_cache()
    dump(R,result("alignment",a.model,f"centred_cos_s{a.seed}.json"))

REPORTED={"patch":grid(model=["pythia-410m","pythia-1.4b","qwen2.5-1.5b"],seed=S8),"alignment":grid(model=["pythia-410m","pythia-1.4b"],seed=S8)}

RUNS={"patch":patch,"patch-layer0":patch_layer0,"patch-entity":patch_entity,"two-token":two_token,"list-vector":list_vector,"suffix-bank":suffix_bank,
      "direction":direction,"direction-colon":direction_colon,"direction-transfer":direction_transfer,"linear-map":linear_map,"birth-year-vector":birth_year_vector,"alignment":alignment}
if __name__=="__main__":
    ap=argparse.ArgumentParser(description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("analysis",choices=list(RUNS)); ap.add_argument("--seed",type=int,required=True); ap.add_argument("--model")
    a=ap.parse_args()
    require(REPORTED.get(a.analysis,grid(model=[None],seed=S8)),model=a.model,seed=a.seed)
    RUNS[a.analysis](a)
