"""Fictional fact worlds: the country world and the birth-year, five-relation and two-token worlds."""

import numpy as np

ONSET = ["b", "br", "d", "dr", "f", "g", "gr", "k", "kr", "l", "m", "n", "p",
         "pr", "q", "r", "s", "sk", "sl", "t", "tr", "v", "z", "zh", "th",
         "kh", "ch", "sh", "w", "y", "j", "gl", "bl", "cl", "fl", "pl"]
VOWEL = ["a", "e", "i", "o", "u", "ae", "ia", "eo", "ou", "ei", "ao", "ui"]
CODA = ["n", "r", "l", "s", "m", "th", "nd", "rk", "st", "ng", "lm", "rn",
         "sk", "ft", "lt", "rt", "mp", "nt"]
SUFFIX = ["ia", "or", "an", "is", "os", "ar", "en", "um", "ex", "ov", "esh",
          "ath", "iel", "ora", "una", "eth"]

def _word(rng):
    w = rng.choice(ONSET) + rng.choice(VOWEL)
    if rng.random() < 0.65:
        w += rng.choice(CODA)
    if rng.random() < 0.75:
        w += rng.choice(SUFFIX)
    return w.capitalize()

def _from_vocab(tok, n, rng, seen, blob, pattern, suffixes, what):
    import re
    vocab = tok.get_vocab()
    stems = sorted(s for s in vocab if re.match(pattern, s))
    rng.shuffle(stems)
    words, ids = [], []
    for st in stems:
        if len(words) >= n:
            break
        tid = vocab[st]
        for suf in suffixes:
            w = st[1:] + suf
            if w in seen or w in blob:
                continue
            got = tok(" " + w, add_special_tokens=False).input_ids
            if got and got[0] == tid:
                seen.add(w); words.append(w); ids.append(tid)
                break
    if len(words) < n:
        raise RuntimeError(f"only {len(words)} first-token-unique {what}; asked for {n}")
    assert len(set(ids)) == len(ids), f"first-token collision among {what}"
    return words

def generate(tok, blob, seed=11):
    """The capital world: 3,000 names drawn for countries (the first 2,000 are used), 2,000 capitals and 2,000 currencies
    built from distinct vocabulary tokens, and 2,000 more vocabulary names that the five-relation world excludes; no name
    occurs in the WikiText slice. The draw order fixes every list, so all are drawn even where only part is used."""
    rng = np.random.default_rng(seed)
    seen = set()
    countries = []
    while len(countries) < 3000:
        w = _word(rng)
        if len(w) < 5 or w in seen or w in blob:
            continue
        seen.add(w)
        countries.append(w)
    capitals = _from_vocab(tok, 2000, rng, seen, blob, "^\u0120[A-Z][a-z]{2,}$", SUFFIX, "capitals")
    currencies = _from_vocab(tok, 2000, rng, seen, blob, "^\u0120[a-z]{3,}$", ("ar", "in", "el", "or", "um", "ex", "an", "is"), "currencies")
    reserved = _from_vocab(tok, 2000, rng, seen, blob, "^\u0120[A-Z][a-z]{2,}$", SUFFIX, "reserved names")
    return dict(countries=countries, capitals=capitals, currencies=currencies, reserved=reserved)


def birth_year_world(tok,blob,C):
    """1,000 fictional people with single-token birth years in 1000-2099; returns the world and the year list."""
    seen=set(C["countries"])|set(C["capitals"])|set(C["currencies"])
    rng=np.random.default_rng(4400); people=[]
    while len(people)<1000:
        w=_word(rng)
        if len(w)<5 or w in seen or w in blob: continue
        seen.add(w); people.append(w)
    YEARS=[y for y in range(1000,2100) if len(tok(" "+str(y),add_special_tokens=False).input_ids)==1]
    yr=rng.integers(0,len(YEARS),size=1000); byof={p:str(YEARS[int(yr[i])]) for i,p in enumerate(people)}
    ids=sorted({tok(" "+v,add_special_tokens=False).input_ids[0] for v in byof.values()})
    return dict(people=people,years=[byof[p] for p in people],pool_first_token_ids=[int(x) for x in ids]),YEARS


def five_relation_world(tok,blob,C,BY,YEARS):
    """400 entities per relation (countries, organizations, people) with single-token answers."""
    ctry=C["countries"]; people=BY["people"][:400]
    seen=set(C["countries"])|set(C["capitals"])|set(C["currencies"])|set(C["reserved"])
    rng=np.random.default_rng(4500); SUF=["Group","Institute","Society","Company","Foundation"]; orgs=[]; ow=set()
    while len(orgs)<400:
        w=_word(rng); sfx=SUF[int(rng.integers(0,5))]
        if len(w)<5 or w in seen or w in ow or w in blob or w in people: continue
        ow.add(w); orgs.append(f"{w} {sfx}")
    ENT={"capital":ctry[0:400],"currency":ctry[400:800],"population":ctry[800:1200],"founder":orgs,"birth year":people}
    entstr=set(x for v in ENT.values() for x in v)|{w.split(" ")[0] for w in orgs}
    V=tok.get_vocab()
    def single(s): return len(tok(" "+s,add_special_tokens=False).input_ids)==1
    cap_ok=[]; low_ok=[]
    for i in sorted(V.values()):
        t=tok.decode([i])
        if not t.startswith(" "): continue
        w=t[1:]
        if len(w)<5 or not w.isalpha() or not w.isascii() or w in seen or w in entstr or not single(w): continue
        if w[0].isupper() and w[1:].islower(): cap_ok.append(w)
        elif w.islower(): low_ok.append(w)
    r=np.random.default_rng(4700); capv=list(r.permutation(cap_ok)); lowv=list(r.permutation(low_ok))
    nums=[str(n) for n in range(10,1000) if single(str(n))]; numv=list(r.permutation(nums))
    ry=np.random.default_rng(4600); yrs=[str(YEARS[int(k)]) for k in ry.integers(0,len(YEARS),size=400)]
    ANS={"capital":capv[:400],"currency":lowv[:400],"population":numv[:400],"founder":capv[400:800],"birth year":yrs}
    REL={"capital":("capital","Capital","What"),"currency":("currency","Currency","What"),"population":("population","Population","What"),
         "founder":("founder","Founder","Who"),"birth year":("birth year","Birth year","What")}
    return dict(relations=REL,entities=ENT,answers=ANS)


def two_token_world(tok,blob,C):
    """2,000 capitals of exactly two tokens (vocabulary stem plus suffix), disjoint from the capital world."""
    import re
    vocab=tok.get_vocab(); pat=re.compile(r"^\u0120[A-Z][a-z]{2,}$"); stems=sorted(s for s in vocab if pat.match(s))
    rng=np.random.default_rng(777); rng.shuffle(stems)
    SUF=["ia","os","ar","um","en","ix","or","us","an","el"]; E=set(C["capitals"]); seen=set(); caps=[]
    for st in stems:
        if len(caps)>=2000: break
        for s in SUF:
            w=st[1:]+s
            if w in seen or w in E or w in blob: continue
            if len(tok(" "+w,add_special_tokens=False).input_ids)==2:
                seen.add(w); caps.append(w); break
    return dict(capitals=caps)
