"""Build the fact worlds and the write-time shift directions that the experiments read.

  python scripts/preprocess.py worlds                                  writes results/*/world.json
  python scripts/preprocess.py shift-directions --model M --seed S     App. I: d_f from the earlier-training facts on the statement-only
                                                                       stage-1 checkpoint (M: pythia-410m, pythia-1.4b, qwen2.5-1.5b)
"""
import os,sys,argparse,torch
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from retrieval.core import *
from retrieval import worlds, measure

def build_worlds(a):
    tok,blob,C=load(MODELS["pythia-410m"])
    BY,YEARS=worlds.birth_year_world(tok,blob,C); dump(BY,result("birth_year","world.json"))
    dump(worlds.five_relation_world(tok,blob,C,BY,YEARS),result("five_relations","world.json"))
    dump(worlds.two_token_world(tok,blob,C),result("two_token","world.json"))
    for k,seed in ((1,101),(2,202)):
        W=worlds.generate(tok,blob,seed=seed)
        dump({"countries":W["countries"][:2000],"capitals":W["capitals"]},result("replications",f"world{k}","world.json"))

def shift_directions(a):
    tok,_,C=load(MODELS[a.model]); B=C["countries"][1000:2000]
    m=model(MODELS[a.model],ckpt("two_stage",a.model,f"CTRL_s{a.seed}","stage1.pt"))
    T={"decl":TRAIN_FORMS["decl"],"list":FRAMES["list"],"kv":TRAIN_FORMS["kv"],"qa":TRAIN_FORMS["qa"]}
    H={f:measure.running_mean_hidden(m,tok,[t.format(c=c) for c in B],5,position_ids=(a.model=="qwen2.5-1.5b")) for f,t in T.items()}
    p=ckpt("vectors","shift",a.model,f"directions_s{a.seed}.pt"); os.makedirs(os.path.dirname(p),exist_ok=True)
    torch.save({f:(H[f]-H["decl"]).cpu() for f in ("list","kv","qa")},p)

if __name__=="__main__":
    ap=argparse.ArgumentParser(description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("step",choices=["worlds","shift-directions"]); ap.add_argument("--model"); ap.add_argument("--seed",type=int)
    a=ap.parse_args()
    if a.step=="shift-directions": require(grid(model=["pythia-410m","pythia-1.4b","qwen2.5-1.5b"],seed=S8),model=a.model,seed=a.seed)
    {"worlds":build_worlds,"shift-directions":shift_directions}[a.step](a)
