"""Ontology construction audit. Not Experiment 009."""
from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations, product
from random import Random

N=16; NR=8; O0_N=3; MAX_N=9; ENC=32; H=100.; COST=5.; BASE_ERR=.125
ST=tuple(range(N)); REL=tuple(range(NR)); ROWS=tuple(product((0,1),repeat=3))
IDX={r:i for i,r in enumerate(ROWS)}; BM=(1<<8)-1
SHIFTS=(
 ((0,0),(0,1),(1,0)),((0,0),(0,1),(0,2)),((0,0),(1,0),(2,0)),
 ((0,0),(1,1),(2,2)),((0,0),(1,0),(1,1)),((0,0),(0,1),(1,1)),
 ((0,0),(1,0),(2,1)),((0,0),(0,2),(1,1)),
)

@dataclass(frozen=True)
class C:
    tt:int; expr:str; nodes:int
    def bit(self,p): return (self.tt>>IDX[p])&1

@dataclass(frozen=True)
class Task:
    anchor:int; rels:tuple

@dataclass
class Meter:
    probes:int=0; values:int=0; hist:int=0; hchecks:int=0
    cevals:int=0; execs:int=0; mem:int=0; storage:int=0
    def snap(self): return (self.probes,self.values,self.hist,self.hchecks,self.cevals,self.execs,self.mem,self.storage)

def vtt(j): return sum(r[j]<<i for i,r in enumerate(ROWS))

def synth(mx):
    L=defaultdict(dict)
    for j,n in enumerate("xyz"): L[1][vtt(j)]=C(vtt(j),n,1)
    for s in range(2,mx+1):
        for tt,c in L[s-1].items(): L[s].setdefault((~tt)&BM,C((~tt)&BM,f"not({c.expr})",s))
        for a in range(1,s-1):
            b=s-1-a
            if b<1: continue
            for lt,l in L[a].items():
                for rt,r in L[b].items():
                    L[s].setdefault(lt&rt,C(lt&rt,f"and({l.expr},{r.expr})",s))
                    L[s].setdefault(lt|rt,C(lt|rt,f"or({l.expr},{r.expr})",s))
    out={}
    for s in range(1,mx+1):
        for tt,c in L[s].items():
            if tt not in out or (c.nodes,c.expr)<(out[tt].nodes,out[tt].expr): out[tt]=c
    return out

O0=synth(O0_N); FULL=synth(MAX_N)
assert len(O0)==12 and len(FULL)==127

def depends(tt,j):
    c=FULL[tt]
    for p in ROWS:
        q=list(p); q[j]=1-q[j]
        if c.bit(p)!=c.bit(tuple(q)): return True
    return False

def latent_hist():
    z=[]
    for rid,sh in enumerate(SHIFTS):
        for src in ST:
            r,c=divmod(src,4)
            for dr,dc in sh: z.append((rid,src,4*((r+dr)%4)+((c+dc)%4)))
    return tuple(z)
LH=latent_hist(); assert len(LH)==384

def enc_hist(se,re): return tuple((re[r],se[a],se[b]) for r,a,b in LH)

def pmask(hist,rid,anchor,m=None):
    x=0
    for r,a,b in hist:
        if m: m.hchecks+=1
        if r==rid and a==anchor: x|=1<<b
    return x

def apply(c,ms):
    out=0
    for s in ST: out|=c.bit(tuple((m>>s)&1 for m in ms))<<s
    return out

def lmasks(t):
    return tuple(pmask(LH,r,t.anchor) for r in t.rels)

def pats(t):
    ms=lmasks(t)
    return frozenset(tuple((m>>s)&1 for m in ms) for s in ST)
ALL=frozenset(ROWS)

def acc(c,h,t):
    ms=lmasks(t); a=apply(c,ms); b=apply(h,ms)
    return sum(((a>>s)&1)==((b>>s)&1) for s in ST)/N

def o0ceil(h,t): return max(acc(c,h,t) for c in O0.values())
def perfect(h,t): return sum(acc(c,h,t)==1 for c in FULL.values())
def pooled(h,a,b): return [c for c in FULL.values() if acc(c,h,a)==1 and acc(c,h,b)==1]

def choose():
    triples=tuple(combinations(REL,3))
    for h in sorted(FULL.values(),key=lambda c:(c.nodes,c.expr,c.tt)):
        if h.nodes<5 or not all(depends(h.tt,j) for j in range(3)): continue
        for ra in triples:
            A=Task(0,ra)
            if o0ceil(h,A)!=.875 or perfect(h,A)<2: continue
            for rb in triples:
                if rb<=ra: continue
                B=Task(5,rb)
                if pats(A)|pats(B)!=ALL or o0ceil(h,B)!=.875 or perfect(h,B)<2: continue
                q=pooled(h,A,B)
                if len(q)!=1 or q[0].tt!=h.tt: continue
                used=set(ra)|set(rb)
                for rc in triples:
                    if set(rc)&used or used|set(rc)!=set(REL): continue
                    Cc=Task(10,rc)
                    if o0ceil(h,Cc)==.875: return h,A,B,Cc
    raise RuntimeError

HID,A,B,T=choose()
assert HID.expr=="and(x,not(or(y,z)))" and HID.nodes==6
assert A.rels==(0,1,3) and B.rels==(0,4,5) and T.rels==(2,6,7)

def etask(t,se,re): return Task(se[t.anchor],tuple(re[r] for r in t.rels))
def tmasks(t,hist,m): return tuple(pmask(hist,r,t.anchor,m) for r in t.rels)

def score(c,tasks,m):
    m.cevals+=1; ok=n=0
    for ms,y in tasks:
        p=apply(c,ms)
        for s in ST: m.execs+=1; ok+=((p>>s)&1)==((y>>s)&1); n+=1
    return ok/n

def rank(lang,tasks,m):
    z=[(score(c,tasks,m),-c.nodes,c.expr,c) for c in lang.values()]
    q=max(z,key=lambda x:x[:3]); return q[3],q[0]

def branch(mut,se,re,mult):
    m=Meter(); hist=enc_hist(se,re); m.hist=len(hist); m.storage=MAX_N
    ta,tb,tt=(etask(x,se,re) for x in (A,B,T))
    ma,mb,mt=(tmasks(x,hist,m) for x in (ta,tb,tt))
    ya,yb,yt=(apply(HID,x) for x in (ma,mb,mt))
    train=((ma,ya),(mb,yb)); m.probes=32; m.values=32; m.mem=32*2+len(hist)*3
    new,na=rank(FULL,train,m); old,oa=rank(O0,train,m)
    gain=max(0.,na-oa); val=H*gain*mult; bind=mut and val>COST; chosen=new if bind else old
    tr=((mt,yt),); cf={c.tt:score(c,tr,m) for c in FULL.values()}
    return dict(new=new,newacc=na,old=old,oldacc=oa,gain=gain,val=val,bind=bind,
                transfer=cf[chosen.tt],newtransfer=cf[new.tt],oldtransfer=cf[old.tt],meter=m.snap())

def runenc(seed,mult=1.):
    r=Random(1608+seed); se=list(ST); re=list(REL); r.shuffle(se); r.shuffle(re)
    x=branch(True,tuple(se),tuple(re),mult); y=branch(False,tuple(se),tuple(re),mult)
    assert x["meter"]==y["meter"]; return x,y

def audit():
    assert perfect(HID,A)==2 and perfect(HID,B)==4 and len(pooled(HID,A,B))==1
    assert all(o0ceil(HID,t)==.875 for t in (A,B,T))
    meter=None
    for s in range(ENC):
        x,y=runenc(s); assert x["new"].tt==HID.tt and x["newacc"]==1 and x["oldacc"]==.875
        assert x["gain"]==.125 and x["val"]==12.5 and x["bind"] and not y["bind"]
        assert x["transfer"]==1 and y["transfer"]==.875
        meter=x["meter"] if meter is None else meter; assert meter==x["meter"]
    n,_=runenc(999,0.); assert n["gain"]==.125 and n["val"]==0 and not n["bind"] and n["transfer"]==.875
    return {
      "constructed_ontology":{"O0":len(O0),"full":len(FULL),"constructor":HID.expr,"nodes":HID.nodes,
        "train_A":A.rels,"train_B":B.rels,"transfer":T.rels,"transfer_relations_all_unseen":True,"base_error":BASE_ERR},
      "identifiability":{"A_matches":2,"B_matches":4,"pooled_matches":1,"transfer_relations_seen":0},
      "cross_encoding":{"encodings":ENC,"exact_constructor_recovery":1.,"mutable_transfer":1.,"fixed_O0_transfer":.875,"meter":meter},
      "killer_null":{"base_error":.125,"representational_gain":.125,"validated_multiplier":0.,"VOI":0.,"bound":False,"transfer":.875},
      "boundary":{"family_menu_supplied":False,"low_level_algebra_supplied":True,"signature":"(set,set,set)->set","unrestricted_type_invention":False},
      "governance":{"goal_rule_mutated":False,"authority_expanded":False},
    }

if __name__=="__main__":
    for k,v in audit().items(): print(f"[{k}]\n{v}\n")
