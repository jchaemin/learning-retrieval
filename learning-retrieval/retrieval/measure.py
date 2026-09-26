"""Readouts: exact generation, pool top-1, hidden states, and generation with a held intervention on one layer."""
import numpy as np,torch
from .core import dev

def blocks(m): return m.gpt_neox.layers if hasattr(m,"gpt_neox") else m.model.layers
def embed(m): return m.gpt_neox.embed_in if hasattr(m,"gpt_neox") else m.model.embed_tokens
def site(m,l):
    """Module whose output is hidden_states[l] (0 = embeddings)."""
    return embed(m) if l==0 else blocks(m)[l-1]

@torch.no_grad()
def generate(m,tok,prompts,answers,bs=50):
    """Exact generation: the greedy 6-token continuation begins with the answer. Returns per-item hits."""
    hits=[]
    for i in range(0,len(prompts),bs):
        e=tok(prompts[i:i+bs],return_tensors="pt",padding=True).to(dev)
        o=m.generate(**e,max_new_tokens=6,do_sample=False,pad_token_id=tok.pad_token_id)
        for j,ans in enumerate(answers[i:i+bs]): hits.append(tok.decode(o[j,e.input_ids.shape[1]:],skip_special_tokens=True).strip().startswith(ans))
    return np.array(hits)

def accuracy(m,tok,prompts,answers,bs=50): return float(generate(m,tok,prompts,answers,bs).mean())

@torch.no_grad()
def pool_logits(m,tok,prompts,pool):
    pool=torch.tensor(pool); Z=[]; bs=32
    for i in range(0,len(prompts),bs):
        e=tok(prompts[i:i+bs],return_tensors="pt",padding=True).to(dev); Z.append(m(**e).logits[:,-1,:].float().cpu()[:,pool])
    return torch.cat(Z).numpy()

@torch.no_grad()
def correct_items(m,tok,items,prompt,first_id,pool):
    """Items whose correct answer is ranked first in the pool at the first answer token."""
    POOLT=torch.tensor(pool).to(dev); pidx={t:i for i,t in enumerate(pool)}; ok=[]; bs=50
    T=torch.tensor([pidx[first_id(c)] for c in items],device=dev)
    for i in range(0,len(items),bs):
        e=tok([prompt(c) for c in items[i:i+bs]],return_tensors="pt",padding=True).to(dev); z=m(**e).logits[:,-1,:].float()[:,POOLT]
        ok+=(z.argmax(1)==T[i:i+z.shape[0]]).cpu().tolist()
    return [items[i] for i in range(len(items)) if ok[i]]

@torch.no_grad()
def hidden(m,tok,prompts,layers,dtype=torch.float32,position_ids=False):
    """Final-position hidden states {layer: [n, d]} (layer indexes hidden_states)."""
    H={l:[] for l in layers}; bs=50
    for i in range(0,len(prompts),bs):
        e=tok(prompts[i:i+bs],return_tensors="pt",padding=True).to(dev)
        if position_ids:
            pos=(e.attention_mask.cumsum(-1)-1).clamp(min=0); hs=m(input_ids=e.input_ids,attention_mask=e.attention_mask,position_ids=pos,output_hidden_states=True).hidden_states
        else: hs=m(**e,output_hidden_states=True).hidden_states
        for l in layers: H[l].append(hs[l][:,-1,:].to(dtype))
    return {l:torch.cat(H[l]) for l in layers}

def mean_hidden(m,tok,prompts,layer): return hidden(m,tok,prompts,[layer])[layer].mean(0)

@torch.no_grad()
def running_mean_hidden(m,tok,prompts,layer,position_ids=False):
    """Mean final-position hidden state, accumulated batch by batch."""
    S=None; n=0; bs=50
    for i in range(0,len(prompts),bs):
        e=tok(prompts[i:i+bs],return_tensors="pt",padding=True).to(dev)
        if position_ids:
            pos=(e.attention_mask.cumsum(-1)-1).clamp(min=0); h=m(input_ids=e.input_ids,attention_mask=e.attention_mask,position_ids=pos,output_hidden_states=True).hidden_states[layer][:,-1,:].float()
        else: h=m(**e,output_hidden_states=True).hidden_states[layer][:,-1,:].float()
        S=h.sum(0) if S is None else S+h.sum(0); n+=h.shape[0]
    return S/n

def replace(states): return lambda h,rows: states[rows]
def add(delta): return lambda h,rows: h+delta
def apply(fn): return lambda h,rows: fn(h)

@torch.no_grad()
def held(m,tok,prompts,answers,module=None,edit=None,position=None,pool=None,first_ids=None):
    """Greedy 1+5-token generation with edit(h, rows) applied to the output of `module` at the prompt-final position
    (or at position(i, n, L) per batch) on every decoding step. Returns {"gen"} (and "pool1" when a pool is given)."""
    gh=[]; hit=[]; bs=50
    if pool is not None: POOLT=torch.tensor(pool).to(dev); pidx={t:i for i,t in enumerate(pool)}; T=torch.tensor([pidx[t] for t in first_ids],device=dev)
    for i in range(0,len(prompts),bs):
        e=tok(prompts[i:i+bs],return_tensors="pt",padding=True).to(dev); n=e.input_ids.shape[0]; L=e.input_ids.shape[1]
        rows=slice(i,i+n); pos=position(i,n,L) if position else None; ar=torch.arange(n,device=dev)
        def hk(md,inp,out):
            o=out[0] if isinstance(out,tuple) else out; o=o.clone()
            if pos is None: o[:,L-1,:]=edit(o[:,L-1,:],rows)
            else: o[ar,pos,:]=edit(o[ar,pos,:],rows)
            return (o,)+tuple(out[1:]) if isinstance(out,tuple) else o
        hook=module.register_forward_hook(hk) if module is not None else None
        z=m(**e).logits[:,-1,:].float()
        if pool is not None: hit+=(z[:,POOLT].argmax(1)==T[i:i+n]).cpu().tolist()
        toks=[z.argmax(-1)]; cur=torch.cat([e.input_ids,toks[0].unsqueeze(1)],1); cam=torch.cat([e.attention_mask,torch.ones_like(toks[0]).unsqueeze(1)],1)
        for _ in range(5):
            nx=m(input_ids=cur,attention_mask=cam).logits[:,-1,:].argmax(-1); toks.append(nx); cur=torch.cat([cur,nx.unsqueeze(1)],1); cam=torch.cat([cam,torch.ones_like(nx).unsqueeze(1)],1)
        if hook: hook.remove()
        g=torch.stack(toks,1)
        for j in range(n): gh.append(tok.decode(g[j],skip_special_tokens=True).strip().startswith(answers[i+j]))
    out={"gen":float(np.mean(gh))}
    if pool is not None: out["pool1"]=float(np.mean(hit))
    return out
