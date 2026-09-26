"""Recompute every number the paper reports from results/ and compare it with the printed value.

  python verify_paper.py     writes verification/claims.json and verification/files_read.txt
"""
import os,sys,json,numpy as np
SUPP=os.path.dirname(os.path.abspath(__file__)); OUT=f"{SUPP}/verification"; R=os.environ.get("RESULTS",f"{SUPP}/results"); S=range(8)
FILES=set(); CL=[]
def J(p): FILES.add(p); return json.load(open(f"{R}/{p}"))
def N(p): FILES.add(p); return np.load(f"{R}/{p}")
def claim(loc,desc,paper,val,tol=0.0005):
    ok=val is not None and abs(float(paper)-float(val))<=tol+1e-9
    CL.append(dict(loc=loc,desc=desc,paper=paper,computed=None if val is None else round(float(val),4),ok=bool(ok)))
m=lambda x:float(np.mean(x))
RW=lambda r,k,seeds=S: m([J(f"generality/{r}_s{s}.json")[k]["gen"] for s in seeds])
# ---------- two-stage capital experiment, Pythia-410M ----------
E=lambda arm,s: J(f"two_stage/pythia-410m/{arm}_s{s}/scores.json")
CT,FV="CTRL","FIVE"
def main(arm,f): return m([E(arm,s)[f]["gen"] for s in S])
claim("Intro / Fig. 1","list, statement-only (0.0%)",0.000,main(CT,"list"))
claim("Intro / Fig. 1","list, five-form (97.7%)",0.977,main(FV,"list"))
FIG2A=dict(decl=(0.995,0.997),poss=(0.039,0.165),city=(0.885,0.885),know=(0.987,0.998),cloze=(0.895,0.801),short_kv=(0.000,0.227),list=(0.000,0.977),decl_colon=(0.024,0.993))
for f,(a,b) in FIG2A.items():
    claim("Fig 2a / §3.2",f"{f} statement-only",a,main(CT,f)); claim("Fig 2a / §3.2",f"{f} five-form",b,main(FV,f))
# ---------- Fig 1 middle / §4.1 : patching and necessity ----------
CR=lambda s: J(f"patching/pythia-410m/patch_s{s}.json")
cr=lambda k,l: m([CR(s)[k][str(l)]["gen"] for s in S])
claim("§4.1","list + same-fact declarative state, layer 4 (96.3%)",0.963,cr("same_fact",4))
claim("§4.1","norm-matched random state restores nothing (layer 4)",0.000,cr("random",4))
claim("§4.1","declarative, unpatched (0.997)",0.997,m([CR(s)["reverse"]["unpatched"]["gen"] for s in S]))
claim("§4.1","declarative with list-form context state (2.3%)",0.023,m([CR(s)["reverse"]["list_state"]["gen"] for s in S]))
# ---------- write-time shift (Fig 1 right, Table 5, App. I) ----------
AU=lambda d,a,s: J(f"shift/{d}/{a}_s{s}/scores.json")
def shift(d,a,f,seeds=S): return m([AU(d,a,s)[f]["gen"] for s in seeds])
c0={"decl_colon":main(CT,"decl_colon"),"decl":main(CT,"decl")}
claim("Table 5","410M capitals no intervention (2.4%)",0.024,c0["decl_colon"])
claim("Table 5","410M capitals targeted shift (94.3%)",0.943,shift("pythia-410m","TARGETED","decl_colon"))
claim("Table 5","410M capitals random shift",0.100,shift("pythia-410m","RANDOM","decl_colon"))
for f,v in (("decl",(0.995,0.997,0.995)),("decl_colon",(0.024,0.100,0.943))):
    claim("App. I","410M "+f+" no intervention",v[0],c0[f]); claim("App. I","410M "+f+" random",v[1],shift("pythia-410m","RANDOM",f)); claim("App. I","410M "+f+" targeted",v[2],shift("pythia-410m","TARGETED",f))
claim("App. I","WikiText loss, targeted shift",5.584,m([J(f"shift/pythia-410m/TARGETED_s{s}/scores.json")["heldout_nll"] for s in S]),0.0005)
claim("App. I","WikiText loss, random shift",5.595,m([J(f"shift/pythia-410m/RANDOM_s{s}/scores.json")["heldout_nll"] for s in S]),0.0005)
# 1.4B and Qwen: no intervention = two-stage statement-only final (declarative) and its colon-ended form from the generality run
C14=lambda f: m([J(f"two_stage/pythia-1.4b/CTRL_s{s}/scores.json")[f]["gen"] for s in S]) if f=="decl" else m([J(f"generality/pythia-1.4b_s{s}.json")[f]["gen"] for s in S])
for f,v in (("decl",(0.995,0.997,0.997)),("decl_colon",(0.266,0.332,0.904))):
    claim("App. I","1.4B "+f+" no intervention",v[0],C14(f)); claim("App. I","1.4B "+f+" random",v[1],shift("pythia-1.4b","RANDOM",f)); claim("App. I","1.4B "+f+" targeted",v[2],shift("pythia-1.4b","TARGETED",f))
claim("Table 5 / §5.2","1.4B no intervention",0.266,C14("decl_colon"))
claim("Table 5","1.4B random",0.332,shift("pythia-1.4b","RANDOM","decl_colon"))
claim("Table 5","1.4B targeted",0.904,shift("pythia-1.4b","TARGETED","decl_colon"))
QC=lambda f: m([J(f"two_stage/qwen2.5-1.5b/CTRL_s{s}/scores.json")[f]["gen"] for s in S])
qx2=m([J(f"generality/qwen2.5-1.5b_s{s}.json")["decl_colon"]["gen"] for s in S])
for f,v in (("decl",(0.999,0.999,0.998)),("decl_colon",(0.482,0.722,0.993))):
    claim("App. I","Qwen "+f+" no intervention",v[0],qx2 if f=="decl_colon" else QC(f)); claim("App. I","Qwen "+f+" random",v[1],shift("qwen2.5-1.5b","RANDOM",f)); claim("App. I","Qwen "+f+" targeted",v[2],shift("qwen2.5-1.5b","TARGETED",f))
claim("Table 5","Qwen no intervention",0.482,qx2)
claim("Table 5","Qwen random",0.722,shift("qwen2.5-1.5b","RANDOM","decl_colon"))
claim("Table 5","Qwen targeted",0.993,shift("qwen2.5-1.5b","TARGETED","decl_colon"))
claim("§5.2","Qwen: targeted − random (+0.27)",0.27,shift("qwen2.5-1.5b","TARGETED","decl_colon")-shift("qwen2.5-1.5b","RANDOM","decl_colon"),0.005)
# birth years, 4 seeds
S4=range(4); BYC=lambda f: m([J(f"birth_year/CTRL_s{s}/scores.json")[f]["gen"] for s in S4])
for f,v in (("decl",(0.997,0.992,0.993)),("decl_colon",(0.246,0.445,0.983))):
    claim("App. I","birth years "+f+" no intervention",v[0],BYC(f)); claim("App. I","birth years "+f+" random",v[1],shift("birth_year","RANDOM",f,S4)); claim("App. I","birth years "+f+" targeted",v[2],shift("birth_year","TARGETED",f,S4))
claim("Table 5","birth years no intervention",0.246,BYC("decl_colon"))
claim("Table 5","birth years random",0.445,shift("birth_year","RANDOM","decl_colon",S4))
claim("Table 5","birth years targeted",0.983,shift("birth_year","TARGETED","decl_colon",S4))
claim("§5.2","five-form colon-ended (0.99)",0.99,main(FV,"decl_colon"),0.005)
claim("§5.2","shift colon-ended (0.94)",0.94,shift("pythia-410m","TARGETED","decl_colon"),0.005)
# ---------- Table 2 (five-relation world) + App. F relation rows ----------
MX=lambda a,s: J(f"five_relations/pythia-410m/{a}_s{s}.json")
mx=lambda a,r,f: m([MX(a,s)[r][f]["gen"] for s in S])
T2V={"capital":(0.983,0.999,0.002,0.970,0.200,0.996),"currency":(0.995,0.999,0.004,0.989,0.388,0.999),"population":(0.991,0.986,0.038,0.991,0.276,0.994),
     "founder":(0.992,0.992,0.001,0.989,0.299,0.998),"birth year":(0.987,0.986,0.344,0.982,0.522,0.989)}
for r,v in T2V.items():
    for i,(a,f) in enumerate((("CTRL","decl"),("FIVE","decl"),("CTRL","list"),("FIVE","list"),("CTRL","decl_colon"),("FIVE","decl_colon"))):
        claim("Table 2 / App. F",f"{r} {f} {a}",v[i],mx(a,r,f))
claim("§3.4","statement-only capital list (0.002)",0.002,mx("CTRL","capital","list")); claim("§3.4","statement-only capital '- Capital of {c} is' (0.814)",0.814,mx("CTRL","capital","list_is"))
KEY5={"capital":(.814,.200,.002),"currency":(.730,.388,.004),"population":(.960,.276,.038),"founder":(.862,.299,.001),"birth year":(.987,.522,.344)}
for r,(a,b,c) in KEY5.items():
    claim("App. F",f"{r} keying is",a,mx("CTRL",r,"list_is")); claim("App. F",f"{r} keying colon",b,mx("CTRL",r,"decl_colon"))
    claim("App. F",f"{r} restore by rewrite: list",c,mx("CTRL",r,"list")); claim("App. F",f"{r} restore by rewrite: rewritten",a,mx("CTRL",r,"list_is"))
# ---------- Fig 2b: gap decl - list during target training (replay of the target stage) ----------
FIG2B_CT=[0.000,0.018,0.055,0.126,0.223,0.389,0.536,0.690,0.799,0.890,0.949,0.964,0.980,0.983,0.980,0.978,0.980,0.985,0.997,0.996,0.995,0.992,0.988,0.995,0.991]
FIG2B_FV=[0.000,-0.003,-0.005,0.008,0.021,0.035,0.054,0.086,0.054,0.045,0.081,0.075,0.061,0.054,0.011,0.011,0.008,0.006,0.009,0.008,0.008,0.007,0.010,0.012,0.014]
def gap(arm):
    G=[]; P=[]
    for s in S:
        z=N(f"trajectory/{arm}_s{s}/trajectory.npz"); G.append(z["acc_decl"]-z["acc_list"]); P.append(z["points"])
    assert all(np.array_equal(x,P[0]) for x in P); return P[0],np.mean(G,0)
for arm,ref in ((CT,FIG2B_CT),(FV,FIG2B_FV)):
    pts,g=gap(arm); assert len(pts)==len(ref)
    for i,(u,v) in enumerate(zip(pts,ref)): claim("Fig 2b",f"{'statement-only' if arm==CT else 'five-form'} gap at update {u} (pool top-1)",v,g[i])
# ---------- §3.2 matched learning: margin and NLL on the declarative form ----------
sys.path.insert(0,SUPP)
from retrieval.core import load as _load
import scipy.stats as st
_tok,_blob,_C=_load("EleutherAI/pythia-410m"); _cap=dict(zip(_C["countries"],_C["capitals"]))
def margin(arm,s): return E(arm,s)["margin"]
d=np.array([margin(FV,s)-margin(CT,s) for s in S]); t=st.t.ppf(.975,7); se=d.std(ddof=1)/8**.5
claim("§3.2","declarative margin, five-form − statement-only (+0.24)",0.24,d.mean(),0.005); claim("§3.2","margin CI includes zero (1=yes)",1,int(d.mean()-t*se<=0<=d.mean()+t*se),0)
NLL=lambda arm,s: E(arm,s)["first_token_nll"]
d=np.array([NLL(FV,s)-NLL(CT,s) for s in S]); se=d.std(ddof=1)/8**.5
claim("§3.2","declarative first-token NLL, five-form − statement-only (−0.043 nats)",-0.043,d.mean()); claim("§3.2","NLL CI includes zero (1=yes)",1,int(d.mean()-t*se<=0<=d.mean()+t*se),0)
# ---------- §3.2 / App. C more target-fact training ----------
X=lambda a,f: [J(f"more_training/{a}_s{s}/scores.json")[f]["gen"] for s in S]
for f,v in (("decl",(0.995,0.997,0.988)),("list",(0.000,0.000,0.000)),("list_is",(0.948,0.974,0.699)),("decl_colon",(0.024,0.045,0.009))):
    claim("App. C",f"{f} standard",v[0],main(CT,f)); claim("App. C",f"{f} X4800",v[1],m(X("X4800",f))); claim("App. C",f"{f} XLR",v[2],m(X("XLR",f)))
claim("§3.2","list form 0.000 in every seed, both arms (max over seeds)",0.0,max(max(X(a,"list")) for a in ("X4800","XLR")),0)
stops=[J(f"more_training/XLR_s{s}/scores.json")["stopped_at"] for s in S]
claim("App. C","XLR min updates (1,000)",1000,min(stops),0); claim("App. C","XLR max updates (6,800)",6800,max(stops),0)
# ---------- §3.3 Table 3 (earlier-training controls) ----------
T3=lambda a,f: m([J(f"stage1_controls/{a}_s{s}.json")[f]["gen"] for s in S])
for lab,a,v in (("Statements only","CTRL",(0.012,0.000,0.024)),("Correct unrelated capitals","FIVE",(0.985,0.977,0.993)),
                ("Incorrect capital answers","INCORRECT",(0.681,0.639,0.724)),("Currencies","CURRENCY",(0.944,0.900,0.987))):
    vals=[main(a,f) if a in (CT,FV) else T3(a,f) for f in ("list","decl_colon")]
    claim("Table 3",f"{lab} mean",v[0],np.mean(vals))
    for f,x,y in zip(("list","decl_colon"),v[1:],vals): claim("Table 3",f"{lab} {f}",x,y)
# ---------- §3.3 request-form exposure (Fig 3, App. D) ----------
D_=lambda a,f: m([J(f"exposure/pythia-410m/{a}_s{s}/scores.json")[f]["gen"] for s in S])
TD=lambda f: D_("D100",f)
DOSE={"0":(lambda f:main(CT,f),(0.000,0.024)),"1":(lambda f:D_("D1",f),(0.122,0.508)),"5":(lambda f:D_("D5",f),(0.381,0.718)),
      "20":(lambda f:D_("D20",f),(0.744,0.880)),"100":(TD,(0.994,0.998)),"5decl":(lambda f:D_("D5DECL",f),(0.003,0.062))}
FIG3={"0":0.000,"1":0.122,"5":0.381,"20":0.744,"100":0.994}
for k,(fn,v) in DOSE.items():
    for f,x in zip(("list","decl_colon"),v): claim("App. D",f"{k}% {f}",x,fn(f))
    if k in FIG3: claim("Fig 3",f"{k}% list",FIG3[k],fn("list"))
claim("§3.3","5% declarative paraphrases, list (0.003)",0.003,D_("D5DECL","list")); claim("§3.3","5% request forms, list (0.381)",0.381,D_("D5","list"))
claim("§5.2","5% request forms, colon-ended (0.72)",0.72,D_("D5","decl_colon"),0.005)
D14=lambda f: m([J(f"exposure/pythia-1.4b/D20_s{s}/scores.json")[f]["gen"] for s in S])
claim("App. D","1.4B 20% list",0.828,D14("list")); claim("Fig 3","1.4B 20% list",0.828,D14("list"))
# ---------- §3.3 target facts in request forms vs earlier-fact training: 'nearly the same' ----------
UN=["list","decl_colon"]
claim("§3.3","target facts in request forms vs earlier-fact training: mean over list and colon-ended declarative, |Δ| < 0.05",0.0,np.mean([TD(f) for f in UN])-np.mean([main(FV,f) for f in UN]),0.05)
# ---------- §3.4 / App. G suffix bank (statement-only) ----------
SUF={}
for s in S:
    for f,r in J(f"suffix_bank/CTRL_s{s}.json").items(): SUF.setdefault(f,[]).append(r["gen"])
SUFV={"- Capital of {c}:":0.000,"{c}'s capital is":0.039,"{c}'s capital city is":0.002,"For {c}, the capital is":0.022,
 "The capital city for {c} is":0.546,"The capital in {c} is":0.891,"The seat of government for {c} is":0.164,"The chief city in {c} is":0.085,"The capital city of {c} is":0.885,
 "- Capital of {c} is":0.948,"The seat of government of {c} is":0.359,"The main city of {c} is":0.187,"I know that the capital of {c} is":0.987,"The city that is the capital of {c} is":0.895,
 "Indeed, the capital of {c} is":0.995,"So the capital of {c} is":0.992}
for f,v in SUFV.items(): claim("App. G",f,v,m(SUF[f]) if f in SUF else None)
lv={1:["{c}'s capital is","{c}'s capital city is","For {c}, the capital is"],2:["The capital city for {c} is","The capital in {c} is"],3:["The capital city of {c} is","- Capital of {c} is"],
    4:["I know that the capital of {c} is","The city that is the capital of {c} is","Indeed, the capital of {c} is","So the capital of {c} is"]}
for k,v in zip((1,2,3,4),(0.02,0.72,0.92,0.97)): claim("§3.4",f"suffix overlap {k}, relation word present, mean",v,m([m(SUF[f]) for f in lv[k]]),0.005)
claim("App. G","number of forms in the bank (16)",16,len([f for f in SUFV if f in SUF]),0)
# ---------- App. B preamble ----------
PX=lambda a,c,f: main(a,f) if c=="plain" else m([J(f"preamble/{a}_s{s}.json")[f]["gen"] for s in S])
for f,v in (("decl",(0.995,0.997,1.000,0.999)),("list",(0.000,0.977,0.000,0.995)),("list_is",(0.948,0.985,0.972,0.997)),("decl_colon",(0.024,0.993,0.011,0.998))):
    for (a,c),x in zip((("CTRL","plain"),("FIVE","plain"),("CTRL","prefixed"),("FIVE","prefixed")),v): claim("App. B",f"{f} {a} {c}",x,PX(a,c,f))
# ---------- §4.2 / App. H patching tables ----------
L0=lambda k: m([J(f"patching/pythia-410m/layer0_s{s}.json")[k]["gen"] for s in S])
claim("App. H 410M","layer 0 same fact",0.948,L0("same_fact")); claim("App. H 410M","layer 0 different fact",0.948,L0("other_fact")); claim("App. H 410M","layer 0 random",0.000,L0("random"))
claim("App. H 410M","rewrite",0.948,L0("rewrite")); claim("App. H 410M","unpatched",0.000,m([CR(s)["unpatched"]["gen"] for s in S]))
H410={"same_fact":(0.950,0.963,0.962,0.963,0.947,0.779),"other_fact":(0.952,0.958,0.959,0.951,0.931,0.701),"currency":(0.949,0.961,0.960,0.946,0.934,0.757),
      "population":(0.951,0.959,0.953,0.928,0.920,0.735),"weather":(0.927,0.895,0.834,0.734,0.543,0.018),"random":(0,0,0,0,0,0)}
for k,v in H410.items():
    for l,x in zip(range(1,7),v): claim("App. H 410M / §4.2",f"{k} layer {l}",x,cr(k,l))
claim("§4.2","layer 6 entity-bearing sources: min (0.70)",0.70,min(cr(k,6) for k in ("same_fact","other_fact","currency","population")),0.005)
claim("§4.2","layer 6 entity-bearing sources: max (0.78)",0.78,max(cr(k,6) for k in ("same_fact","other_fact","currency","population")),0.005)
claim("App. H 410M","layer 0: same = other = rewrite in every seed (measured; other sources equal by construction) (1 = true)",1,int(all(J(f"patching/pythia-410m/layer0_s{s}.json")["same_fact"]["gen"]==J(f"patching/pythia-410m/layer0_s{s}.json")["other_fact"]["gen"]==J(f"patching/pythia-410m/layer0_s{s}.json")["rewrite"]["gen"] for s in S)),0)
P14=lambda k,l: m([J(f"patching/pythia-1.4b/patch_s{s}.json")[k][str(l)]["gen"] for s in S])
H14={"same_fact":(0.995,0.996,0.987,0.977,0.962,0.890,0.872),"other_fact":(0.995,0.995,0.985,0.974,0.965,0.895,0.874),"currency":(0.995,0.995,0.988,0.983,0.971,0.926,0.928),
     "population":(0.995,0.995,0.988,0.982,0.972,0.923,0.908),"weather":(0.995,0.995,0.948,0.916,0.723,0.448,0.140),"random":(0,)*7}
for k,v in H14.items():
    for l,x in zip(range(7),v): claim("App. H 1.4B",f"{k} layer {l}",x,P14(k,l))
claim("App. H 1.4B","unpatched",0.040,m([J(f"patching/pythia-1.4b/patch_s{s}.json")["unpatched"]["gen"] for s in S])); claim("App. H 1.4B","rewrite",0.995,m([J(f"patching/pythia-1.4b/patch_s{s}.json")["rewrite"]["gen"] for s in S]))
MP=lambda src,l: m([J(f"patching/two_token/patch_s{s}.json")[src][str(l)]["gen"] for s in S])
for src,v in (("same_fact",(0.941,0.941,0.943,0.945,0.932,0.910,0.724)),("other_fact",(0.941,0.942,0.938,0.936,0.922,0.892,0.633)),("random",(0,)*7)):
    for l,x in zip(range(7),v): claim("App. H two-token",f"{src} layer {l}",x,MP(src,l))
claim("App. H two-token","unpatched",0.001,m([J(f"patching/two_token/patch_s{s}.json")["unpatched"]["gen"] for s in S]))
Q=lambda s: J(f"patching/qwen2.5-1.5b/patch_s{s}.json")
for k,(hi,lo) in (("same_fact",(0.998,0.995)),("other_fact",(0.998,0.994)),("currency",(0.998,0.994)),("population",(0.998,0.994)),("weather",(0.998,0.989))):
    v=[m([Q(s)[k][str(l)]["gen"] for s in S]) for l in range(7)]; claim("App. H Qwen",f"{k} max over layers 0-6",hi,max(v)); claim("App. H Qwen",f"{k} min over layers 0-6",lo,min(v))
claim("App. H Qwen","random, max over layers 0-6 (0.000)",0.0,max(m([Q(s)["random"][str(l)]["gen"] for s in S]) for l in range(7)))
claim("App. H Qwen","unpatched",0.603,m([Q(s)["unpatched"]["gen"] for s in S])); claim("App. H Qwen","rewrite",0.998,m([Q(s)["rewrite"]["gen"] for s in S]))
claim("App. H Qwen","declarative after norm-matched random removal (0.999)",0.999,m([Q(s)["reverse"]["random_removal"]["gen"] for s in S]))
claim("§4.2","Qwen declarative, unpatched (0.999)",0.999,m([Q(s)["reverse"]["unpatched"]["gen"] for s in S])); claim("§4.2","Qwen declarative with list state (0.550)",0.550,m([Q(s)["reverse"]["list_state"]["gen"] for s in S]))
# ---------- §4.3 / Table 4 / App. J ----------
DR=lambda s: J(f"direction/direction_s{s}.json")
claim("§4.3 / Table 4a","list + direction (0.921)",0.921,m([DR(s)["u_alone"]["gen"] for s in S]))
claim("§4.3 / App. J","restoring vector with u removed (0.010)",0.010,m([DR(s)["r_u_removed"]["gen"] for s in S]))
claim("App. J","direction alone: beta = 1 in every seed",1.0,max(abs(DR(s)["u_alone"]["beta"]-1.0) for s in S)+1.0,0)
claim("App. J","mirror: cos(v,u) (0.603)",0.603,m([DR(s)["mirror"]["cos_v_u"] for s in S])); claim("App. J","mirror removal leaves (0.388)",0.388,m([DR(s)["mirror"]["gen"] for s in S]))
claim("App. J","random matched-cos: mean cos(v,u) (0.801)",0.801,m([DR(s)["random_same_cos"]["cos_v_u"] for s in S])); claim("App. J","random matched-cos removal leaves (0.151)",0.151,m([DR(s)["random_same_cos"]["gen"] for s in S]))
claim("App. J / App. F","restoring vector alone, 410M (0.945)",0.945,m([DR(s)["r"]["gen"] for s in S]))
SEL=[J(f"direction/list_vector_s{s}.json")["layer"] for s in S]; claim("App. J","selected layer is 4 in every seed",4,max(SEL) if min(SEL)==max(SEL) else -1,0)
for l,v in ((4,0.895),(6,0.840),(8,0.833)): claim("App. J",f"cos(list vector, u) layer {l}",v,m([J(f"direction/list_vector_s{s}.json")["cos_u"][str(l)] for s in S]))
LM=lambda f,k: m([J(f"direction/linear_map_s{s}.json")[f][k]["gen"] for s in S])
for f,v in (("list",0.949),("decl",0.995)): claim("App. J",f"linear map {f} (seven non-declarative evaluation forms)",v,LM(f,"linear"))
claim("§4.3","linear map, list (0.949)",0.949,LM("list","linear"))
claim("App. J","rank-16 map within 0.01 of the linear map (max |Δ|)",0.0,max(abs(LM(f,"rank16")-LM(f,"linear")) for f in ("list","decl")),0.01)
QV=lambda k: m([Q(s)["vector"][k]["gen"] for s in S])
claim("§4.3 / App. F","Qwen list unpatched (0.603)",0.603,RW("qwen2.5-1.5b","CTRL")); claim("§4.3","Qwen list + direction (0.993)",0.993,QV("u_alone")); claim("§4.3","Qwen restoring vector with u removed (0.944)",0.944,QV("r_u_removed"))
DF=lambda k: m([J(f"direction/colon_s{s}.json")[k]["gen"] for s in S])
claim("Table 4a","decl_colon no intervention",0.024,DF("unpatched")); claim("Table 4a","decl_colon + direction",0.983,DF("u"))
TR=lambda s: J(f"direction/transfer_s{s}.json")
for w,v in (("capital",(0.921,0.910)),("birth_year",(0.971,0.969))):
    claim("Table 4b",f"{w} same-domain",v[0],m([TR(s)[w]["own"]["gen"] for s in S])); claim("Table 4b",f"{w} other-domain",v[1],m([TR(s)[w]["transplant"]["gen"] for s in S]))
claim("App. J","u from birth-year people vs countries, cosine (1.000)",1.000,m([TR(s)["cos_u_countries_people"] for s in S]))
# ---------- Fig 4 alignment curves: list form ----------
F4={"410M":{"FIVE":[0.791,0.725,0.528,0.451,0.487,0.746,0.716,0.677,0.654,0.827,0.856,0.833,0.853,0.869,0.880,0.892,0.902,0.901,0.893,0.885,0.876,0.864,0.853,0.845],
            "CTRL":[0.775,0.681,0.502,0.460,0.493,0.695,0.636,0.539,0.485,0.600,0.614,0.475,0.516,0.515,0.478,0.456,0.424,0.382,0.345,0.321,0.295,0.269,0.245,0.230]},
    "1.4B":{"FIVE":[0.746,0.732,0.610,0.656,0.684,0.635,0.740,0.756,0.840,0.847,0.901,0.909,0.926,0.926,0.932,0.931,0.926,0.921,0.915,0.909,0.901,0.892,0.883,0.875],
            "CTRL":[0.705,0.643,0.544,0.585,0.611,0.605,0.632,0.570,0.642,0.611,0.652,0.666,0.656,0.633,0.631,0.608,0.580,0.554,0.534,0.514,0.497,0.479,0.459,0.440]}}
for mdl,pat in (("410M","alignment/pythia-410m/centred_cos_s{s}.json"),("1.4B","alignment/pythia-1.4b/centred_cos_s{s}.json")):
    for arm in ("FIVE","CTRL"):
        for l in range(1,25):
            v=m([J(pat.format(s=s))[arm][str(l)] for s in S])
            claim("Fig 4",f"{mdl} {arm} layer {l}",F4[mdl][arm][l-1],v)
# ---------- App. F generality ----------
S4=range(4)
GEN={"pythia-410m":("Pythia-410M",(0.000,0.977),(0.948,0.024),(0.000,0.948,0.945),S),"pythia-1.4b":("Pythia-1.4B",(0.040,0.997),(0.994,0.266),(0.040,0.994,0.917),S),
     "qwen2.5-1.5b":("Qwen2.5-1.5B",(0.603,0.997),(0.998,0.482),(0.603,0.998,0.993),S),"llama-3.2-1b":("Llama-3.2-1B (4 seeds)",(0.048,0.997),(0.995,0.125),(0.048,0.995,0.971),S4),
     "lora":("Targets written by LoRA",(0.000,0.836),(0.708,0.010),(0.000,0.708,0.730),S)}
for r,(lab,c1,c2,c3,sd) in GEN.items():
    claim("App. F",f"{lab} list statement-only",c1[0],RW(r,"CTRL",sd)); claim("App. F",f"{lab} list five-form",c1[1],RW(r,"FIVE",sd))
    claim("App. F",f"{lab} keying is",c2[0],RW(r,"list_is",sd)); claim("App. F",f"{lab} keying colon",c2[1],RW(r,"decl_colon",sd))
    claim("App. F",f"{lab} restore base",c3[0],RW(r,"CTRL",sd)); claim("App. F",f"{lab} restore rewrite",c3[1],RW(r,"list_is",sd)); claim("App. F",f"{lab} restore vector",c3[2],RW(r,"vector",sd))
BYF=lambda a,f: m([J(f"birth_year/{a}_s{s}/scores.json")[f]["gen"] for s in S])
claim("App. F","birth years as target: list statement-only",0.150,BYF("CTRL","list")); claim("App. F","birth years as target: list five-form",0.952,BYF("FIVE","list"))
claim("App. F","birth years keying is",0.977,BYF("CTRL","list_is")); claim("App. F","birth years keying colon",0.221,BYF("CTRL","decl_colon")); claim("App. F","birth years rewrite",0.977,BYF("CTRL","list_is"))
claim("App. F","birth years restoring vector",0.973,RW("birth_year","vector"))
TT=lambda arm,f: m([J(f"two_token/{arm}_s{s}/scores.json")[f]["gen"] for s in S])
claim("App. F","two-token list statement-only",0.001,TT("CTRL","list")); claim("App. F","two-token list five-form",0.982,TT("FIVE","list"))
claim("App. F","two-token keying is / rewrite",0.941,RW("two_token","list_is")); claim("App. F","two-token keying colon",0.025,RW("two_token","decl_colon"))
claim("App. F","two-token restoring vector",0.934,RW("two_token","vector"))
DC=lambda p,seeds=S: m([J(p.format(s=s))["decl"]["gen"] for s in seeds])
MX14=lambda a,r,f: m([J(f"five_relations/pythia-1.4b/{a}_s{s}.json")[r][f]["gen"] for s in S])
for r,(c,fv) in {"capital":(0.119,0.998),"currency":(0.256,0.999),"population":(0.248,0.991),"founder":(0.089,0.996),"birth year":(0.685,0.996)}.items():
    claim("App. F / §3.2",f"1.4B five-relation {r} list statement-only",c,MX14("CTRL",r,"list")); claim("App. F / §3.2",f"1.4B five-relation {r} list five-form",fv,MX14("FIVE",r,"list"))
    d14=[J(f"five_relations/pythia-1.4b/FIVE_s{s}.json")[r]["list"]["gen"]-J(f"five_relations/pythia-1.4b/CTRL_s{s}.json")[r]["list"]["gen"] for s in S]
    claim("App. F",f"1.4B five-relation {r}: five-form > statement-only in 8/8 seeds",8,sum(x>0 for x in d14),0)
    claim("App. F",f"1.4B five-relation {r}: matched declarative accuracy (|Δ| < 0.05)",0.0,MX14("FIVE",r,"decl")-MX14("CTRL",r,"decl"),0.05)
dm=[]
for r in ("capital","currency","population","founder","birth year"): dm+=[mx("CTRL",r,"decl"),mx("FIVE",r,"decl"),MX14("CTRL",r,"decl"),MX14("FIVE",r,"decl")]
for a in ("CTRL","FIVE"):
    dm+=[DC(f"two_stage/pythia-410m/{a}_s{{s}}/scores.json"),DC(f"two_stage/pythia-1.4b/{a}_s{{s}}/scores.json"),DC(f"two_stage/qwen2.5-1.5b/{a}_s{{s}}/scores.json"),
         DC(f"two_stage/llama-3.2-1b/{a}_s{{s}}/scores.json",S4),m([J(f"birth_year/{a}_s{s}/scores.json")["decl"]["gen"] for s in S]),
         DC(f"two_token/{a}_s{{s}}/scores.json"),DC(f"lora/{a}_s{{s}}/scores.json")]
claim("App. F","declarative training-form accuracy in every row, minimum (0.97)",0.97,min(dm),0.005); claim("App. F","declarative training-form accuracy in every row, maximum (1.00)",1.00,max(dm),0.005)
# ---------- App. E replications (pool top-1 on list, FIVE − CTRL) ----------
def rep(w,seeds):
    d=np.array([J(f"replications/{w}/FIVE_s{s}/scores.json")["list"]["pool1"]-J(f"replications/{w}/CTRL_s{s}/scores.json")["list"]["pool1"] for s in seeds])
    return d.mean(),int((d>0).sum())
for lab,w,sd,v in (("world 1","world1",range(8),0.974),("world 2","world2",range(8),0.887),("world 2, seeds 8–15","world2",range(8,16),0.972)):
    r=rep(w,sd); claim("App. E",f"{lab} mean difference",v,r[0]); claim("App. E",f"{lab} 8/8 seeds positive",8,r[1],0)
# ---------- qualitative / protocol statements (boolean or value checks; paper value = what the text asserts) ----------
ET=[J(f"patching/entity_site/patch_s{s}.json") for s in S]
claim("§4.1 / App. H","country-token patching: generation at every layer and source, maximum (0.000)",0.0,max(m([e[k][l]["gen"] for e in ET]) for k in ET[0] for l in ET[0][k]))
claim("§4.2","Pythia-1.4B shows the 410M pattern: entity-free source fades by layer 6 (entity-free L6 < same-fact L6 − 0.2)",1,int(P14("weather",6)<P14("same_fact",6)-0.2),0)
V14=[J(f"patching/pythia-1.4b/patch_s{s}.json")["vector"] for s in S]; b=RW("pythia-1.4b","CTRL"); v,pj=[m([x[k]["gen"] for x in V14]) for k in ("r","r_u_removed")]
claim("§4.3","Pythia models: removing u removes almost all of the restoring effect — 1.4B fraction of effect removed ≥ 0.8 (1 = true)",1,int((v-pj)/(v-b)>=0.8),0)
_tr=open(f"{SUPP}/scripts/train.py").read(); _lora=_tr[_tr.index("def lora("):_tr.index("def two_token(")]
claim("App. A / App. F","LoRA writes the target stage only (train.py lora starts from the full fine-tuned stage-1 checkpoint) (1 = true)",1,int("stage1.pt" in _lora),0)
_ra=_tr[_tr.index("def shift("):_tr.index("def trajectory(")]
claim("App. I","shift directions drawn from {list, key-value, question, none} (1 = true)",1,int('KINDS=["none","list","kv","qa"]' in _ra),0)
_tf=[f for s in S for f in J(f"exposure/pythia-410m/D100_s{s}/forms.json")["forms"]]
claim("App. D / Fig. 3","at 100% the list and colon-ended declarative forms are never written (1 = true)",1,int("- Capital of {c}:" not in _tf and "The capital of {c}:" not in _tf),0)
ALLV={1:["{c}'s capital is","{c}'s capital city is","For {c}, the capital is"],2:["The capital city for {c} is","The capital in {c} is","The seat of government for {c} is","The chief city in {c} is"],
      3:["The capital city of {c} is","- Capital of {c} is","The seat of government of {c} is","The main city of {c} is"],4:lv[4]}
for k,v in zip((1,2,3,4),(0.02,0.42,0.59,0.97)): claim("§3.4",f"suffix overlap {k}, all listed forms, mean",v,m([m(SUF[f]) for f in ALLV[k]]),0.005)
_oth=["capital","currency","population","founder"]
claim("Table 2 caption / App. F","birth-year statement-only list and colon-ended values exceed every other relation's (year answers come more readily after a colon) (1 = true)",1,int(mx("CTRL","birth year","list")>max(mx("CTRL",r,"list") for r in _oth) and mx("CTRL","birth year","decl_colon")>max(mx("CTRL",r,"decl_colon") for r in _oth)),0)
# ---------- protocol statements ----------
import re as _re
_A=_C["countries"][:1000]; _Ast=[f"The capital of {c} is {_cap[c]}." for c in _A]*5
from retrieval.core import build_corpus as _bc, sentences as _sentences
_d=_bc(_tok,_blob,_Ast,7); claim("App. A","passes over the target stage (about 2.2)",2.2,1200*8/_d.shape[0],0.05)
_base=_sentences(_blob); claim("App. A","WikiText sentences per injected target line (about seven)",7,len(_base)/5000,0.5)
_cid=_tok(" Felmov",add_special_tokens=False).input_ids
def _tk(f,ans=False):
    ids=_tok(f.format(c="Felmov")+(" Brisis." if ans else "")).input_ids; o=[]; i=0
    while i<len(ids):
        if ids[i:i+len(_cid)]==_cid: o.append("<E>"); i+=len(_cid)
        else: o.append(_tok.decode([ids[i]])); i+=1
    return o
_bg=lambda x:set(zip(x,x[1:])); _PB=set().union(*[_bg(_tk(p,True)) for p in ["The capital of {c} is","Capital of {c}:","Q: What is the capital of {c}? A:","User: What is the capital of {c}?\nAssistant:","Name the capital of {c}:"]])
_zero=[n for n,f in {"possessive":"{c}'s capital is","capital-city":"The capital city of {c} is","knowledge":"I know that the capital of {c} is","relative":"The city that is the capital of {c} is","short key-value":"{c} capital:","list":"- Capital of {c}:","colon-ended":"The capital of {c}:"}.items() if not (_bg(_tk(f)) & _PB)]
claim("§3.2","exactly the possessive and short key-value forms share no token bigram with any earlier-training line (1 = true)",1,int(sorted(_zero)==["possessive","short key-value"]),0)
# ---------- App. K declarative-accuracy check (shift and linear map, per seed) ----------
_dd=[]
for _mdl in ("pythia-410m","pythia-1.4b","qwen2.5-1.5b"):
    for _a in ("TARGETED","RANDOM"): _dd+=[abs(AU(_mdl,_a,s)["decl"]["gen"]-J(f"two_stage/{_mdl}/CTRL_s{s}/scores.json")["decl"]["gen"]) for s in S]
for _a in ("TARGETED","RANDOM"): _dd+=[abs(AU("birth_year",_a,s)["decl"]["gen"]-J(f"birth_year/CTRL_s{s}/scores.json")["decl"]["gen"]) for s in S4]
_dd+=[abs(J(f"direction/linear_map_s{s}.json")["decl"]["linear"]["gen"]-E(CT,s)["decl"]["gen"]) for s in S]
claim("App. K","declarative-accuracy check: shift and linear map change declarative accuracy by at most 0.05 in every seed (1 = true)",1,int(max(_dd)<=0.05),0)
# ---------- output ----------
os.makedirs(OUT,exist_ok=True); json.dump(CL,open(f"{OUT}/claims.json","w"),indent=1)
open(f"{OUT}/files_read.txt","w").write("\n".join(sorted(FILES))+"\n")
bad=[c for c in CL if not c["ok"]]
print(f"claims {len(CL)}, OK {len(CL)-len(bad)}, mismatch/unverifiable {len(bad)}; files read {len(FILES)}")
for c in bad: print(f"  [{c['loc']}] {c['desc']}: paper {c['paper']} vs computed {c['computed']}")
