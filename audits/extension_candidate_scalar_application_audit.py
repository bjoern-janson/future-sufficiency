"""Actual-candidate scalar application audit.
Preregistered 9f1ab6488e155b95b0d60896df3ab65b1ff5cd5d.

Applies only frozen D0/D1/D2 families to the frozen governance-relative
12-candidate preference graphs. No decoder redesign, Q_extension, ranking,
adoption, authorization, binding, or execution.
"""
from __future__ import annotations
import argparse, base64, hashlib, itertools, json, lzma
from collections import Counter
from pathlib import Path

PRE="9f1ab6488e155b95b0d60896df3ab65b1ff5cd5d"
PARENT="f10ff41e292ba8d2df26c0468f785d4fb07c2de6"
PRE_BLOB="d90d41fd9f2596b3234dca174eca388a42f2859d"
PREF_APP_BLOB="7efc07e54de9b7e4719caee632daecab32e56f1f"
SCALAR_RESULT_BLOB="98a5db5311f18efa0f84e0fb1d99ef77574d8a91"
PAIR_SHA="76ae7638e225973f21b90605a9c020a74e752143d1dd008bd2f894fdbd4629aa"
IDS=[
"CTRL_ALIAS_A","CTRL_ID_DEG2","CTRL_ID_LINEAR","CTRL_SUPPLIED_DEG2",
"EXT_CT_A","EXT_CT_B","EXT_CT_C1","EXT_CT_C2",
"SYN_A_120","SYN_B_50","SYN_C1_1653","SYN_C2_2388"]
G=("G_PARTIAL_EMPTY","G_CONSTRAINT_B","G_LEX_DV_REOPEN_B","G_COMP_EXPLICIT")
TOK=("PREFER_I","PREFER_J","EQUIVALENT","NO_WARRANTED_PREFERENCE")
EXPECTED={
"G_PARTIAL_EMPTY":{"PREFER_I":0,"PREFER_J":0,"EQUIVALENT":1,"NO_WARRANTED_PREFERENCE":65},
"G_CONSTRAINT_B":{"PREFER_I":5,"PREFER_J":3,"EQUIVALENT":1,"NO_WARRANTED_PREFERENCE":57},
"G_LEX_DV_REOPEN_B":{"PREFER_I":3,"PREFER_J":5,"EQUIVALENT":1,"NO_WARRANTED_PREFERENCE":57},
"G_COMP_EXPLICIT":{"PREFER_I":3,"PREFER_J":5,"EQUIVALENT":1,"NO_WARRANTED_PREFERENCE":57},
}
EXPECTED_MATRIX={
"G_PARTIAL_EMPTY":{"D0":"NOT_REPRESENTABLE","D1":"FAITHFUL_CONTRACTION","D2":"FAITHFUL_CONTRACTION"},
"G_CONSTRAINT_B":{"D0":"NOT_REPRESENTABLE","D1":"NOT_REPRESENTABLE","D2":"NOT_REPRESENTABLE"},
"G_LEX_DV_REOPEN_B":{"D0":"NOT_REPRESENTABLE","D1":"NOT_REPRESENTABLE","D2":"NOT_REPRESENTABLE"},
"G_COMP_EXPLICIT":{"D0":"NOT_REPRESENTABLE","D1":"NOT_REPRESENTABLE","D2":"NOT_REPRESENTABLE"},
}

def canon(x): return json.dumps(x,sort_keys=True,separators=(",",":"))
def git_blob_sha(b): return hashlib.sha1(f"blob {len(b)}\0".encode()+b).hexdigest()
def verify_blob(p,sha):
    b=p.read_bytes(); got=git_blob_sha(b); assert got==sha,(p,got,sha); return b

def unpack(w):
    assert w["format"]=="lossless-lzma-base64-json-v1"
    raw=lzma.decompress(base64.b64decode(w["payload_b64"]))
    assert len(raw)==w["uncompressed_bytes"]
    assert hashlib.sha256(raw).hexdigest()==w["uncompressed_sha256"]
    return json.loads(raw)

def load_targets(root):
    verify_blob(root/"extension_candidate_scalar_application_preregistration.md",PRE_BLOB)
    verify_blob(root/"extension_candidate_preference_application_results.json",PREF_APP_BLOB)
    verify_blob(root/"extension_scalar_sufficiency_identification_results.json",SCALAR_RESULT_BLOB)
    w=json.loads((root/"extension_candidate_preference_application_results.json").read_text())
    recs=unpack(w["application_records"])
    pairs=list(itertools.combinations(IDS,2))
    assert hashlib.sha256(json.dumps(pairs,separators=(",",":")).encode()).hexdigest()==PAIR_SHA
    out={g:{} for g in G}
    for r in recs:
        g=r["governance_contract_id"]; p=(r["candidate_i"],r["candidate_j"])
        assert g in out and p in pairs and r["preference_status"] in TOK
        out[g][p]=r["preference_status"]
    assert all(len(out[g])==66 for g in G)
    for g in G:
        c=Counter(out[g].values())
        assert {t:c[t] for t in TOK}==EXPECTED[g]
    return pairs,out

def d1_out(x,y,tau):
    d=x-y
    return "EQUIVALENT" if d==0 else ("NO_WARRANTED_PREFERENCE" if abs(d)<=tau else ("PREFER_I" if d>0 else "PREFER_J"))

def d2_out(x,y,t1,t2,pol):
    d=x-y
    if d==0:return "EQUIVALENT"
    k=0 if abs(d)<=t1 else 1 if abs(d)<=t2 else 2
    return "NO_WARRANTED_PREFERENCE" if pol[k]=="N" else ("PREFER_I" if d>0 else "PREFER_J")

class UF:
    def __init__(self,n): self.p=list(range(n))
    def find(self,x):
        while self.p[x]!=x:
            self.p[x]=self.p[self.p[x]]; x=self.p[x]
        return x
    def union(self,a,b):
        a,b=self.find(a),self.find(b)
        if a!=b:self.p[b]=a

def quotient(rel):
    idx={x:i for i,x in enumerate(IDS)}
    uf=UF(len(IDS))
    for (a,b),t in rel.items():
        if t=="EQUIVALENT": uf.union(idx[a],idx[b])
    roots={}; classes=[]
    for i,x in enumerate(IDS):
        r=uf.find(i)
        if r not in roots: roots[r]=len(classes); classes.append([])
        classes[roots[r]].append(x)
    cid={x:k for k,c in enumerate(classes) for x in c}
    m=len(classes); M=[[0]*m for _ in range(m)]
    seen={}
    for (a,b),t in rel.items():
        u,v=cid[a],cid[b]
        if u==v:
            if t!="EQUIVALENT": return None
            continue
        key=tuple(sorted((u,v)))
        if t=="NO_WARRANTED_PREFERENCE": val=(0,0)
        elif t=="PREFER_I": val=(u,v)
        elif t=="PREFER_J": val=(v,u)
        else: return None
        if key in seen and seen[key]!=val:return None
        seen[key]=val
    if len(seen)!=m*(m-1)//2:return None
    for val in seen.values():
        if val!=(0,0):
            a,b=val; M[a][b]=1; M[b][a]=-1
    return classes,M

def generated_matrix(scores,Dset):
    m=len(scores); M=[[0]*m for _ in range(m)]
    for i,j in itertools.combinations(range(m),2):
        if abs(scores[i]-scores[j]) in Dset:
            if scores[i]>scores[j]: M[i][j]=1; M[j][i]=-1
            else: M[j][i]=1; M[i][j]=-1
    return M

def degrees(M):
    out=[sum(x==1 for x in row) for row in M]
    inn=[sum(x==-1 for x in row) for row in M]
    return out,inn

def iso_map(A,B,canonical=False):
    n=len(A)
    ao,ai=degrees(A); bo,bi=degrees(B)
    if sorted(zip(ao,ai))!=sorted(zip(bo,bi)):return None
    cand={u:[v for v in range(n) if (ao[u],ai[u])==(bo[v],bi[v])] for u in range(n)}
    order=list(range(n)) if canonical else sorted(range(n),key=lambda u:(len(cand[u]),-(ao[u]+ai[u]),u))
    used=set(); mp={}
    def rec(k):
        if k==n:return dict(mp)
        u=order[k]
        for v in cand[u]:
            if v in used:continue
            ok=True
            for u2,v2 in mp.items():
                if A[u][u2]!=B[v][v2] or A[u2][u]!=B[v2][v]:
                    ok=False;break
            if not ok:continue
            mp[u]=v;used.add(v)
            z=rec(k+1)
            if z is not None:return z
            used.remove(v);del mp[u]
        return None
    return rec(0)

def score_subsets(m):
    for tail in itertools.combinations(range(1,14),m-1):
        yield (0,)+tail

def d2_semantics():
    z={}
    for t1 in range(14):
      for t2 in range(t1,14):
       for pol in itertools.product(("D","N"),repeat=3):
        ds=tuple(d for d in range(1,14) if pol[0 if d<=t1 else 1 if d<=t2 else 2]=="D")
        p=(t1,t2)+pol
        if ds not in z or p<z[ds]: z[ds]=p
    assert len(z)==158
    return sorted((p,set(ds)) for ds,p in z.items())

D2SEM=d2_semantics()

def exact_search(rel,fam):
    q=quotient(rel)
    if q is None:return None
    classes,T=q; m=len(classes)
    if fam=="D1":
        sem=[((tau,),set(range(tau+1,14))) for tau in range(14)]
    else:
        sem=D2SEM
    for params,Dset in sem:
        for scores in score_subsets(m):
            H=generated_matrix(scores,Dset)
            mp=iso_map(T,H)
            if mp is not None:
                qv={}
                for ci,members in enumerate(classes):
                    s=scores[mp[ci]]
                    for x in members:qv[x]=s
                return params,[qv[x] for x in IDS]
    return None

def decode_relation(fam,qv,params,pairs):
    q=dict(zip(IDS,qv)); out={}
    for a,b in pairs:
        if fam=="D0":
            d=q[a]-q[b]; out[a,b]="EQUIVALENT" if d==0 else ("PREFER_I" if d>0 else "PREFER_J")
        elif fam=="D1":
            out[a,b]=d1_out(q[a],q[b],params[0])
        else:
            t1,t2,*pol=params; out[a,b]=d2_out(q[a],q[b],t1,t2,pol)
    return out

def mismatch_count(target,decoded):
    return sum(target[p]!=decoded[p] for p in target)

def run(root,deep=False):
    pairs,target=load_targets(root)
    matrix={}; witness={}
    for g in G:
        matrix[g]={}
        matrix[g]["D0"]="NOT_REPRESENTABLE" if EXPECTED[g]["NO_WARRANTED_PREFERENCE"] else "UNEXPECTED"
        for fam in ("D1","D2"):
            w=exact_search(target[g],fam)
            if w is None: matrix[g][fam]="NOT_REPRESENTABLE"
            else:
                matrix[g][fam]="FAITHFUL_CONTRACTION"; witness[g+":"+fam]=w
    assert matrix==EXPECTED_MATRIX,matrix

    q=[0,1,2,3,4,5,6,7,8,8,9,10]
    assert decode_relation("D1",q,(10,),pairs)==target["G_PARTIAL_EMPTY"]
    assert decode_relation("D2",q,(0,0,"D","D","N"),pairs)==target["G_PARTIAL_EMPTY"]

    d1q=[1,2,10,0,3,4,5,6,9,9,7,8]
    d2q=[1,11,9,0,4,5,6,7,8,8,2,3]
    assert mismatch_count(target["G_CONSTRAINT_B"],decode_relation("D1",d1q,(8,),pairs))==4
    assert mismatch_count(target["G_CONSTRAINT_B"],decode_relation("D2",d2q,(7,9,"N","D","N"),pairs))==2

    result=json.loads((root/"extension_candidate_scalar_application_results.json").read_text())
    assert result["gate_pass"]
    assert result["diagnosis_summary"]=={"FAITHFUL_CONTRACTION":2,"NOT_REPRESENTABLE":10,"W_LOOKUP_REPRESENTABLE_NO_CONTRACTION":4}
    assert result["contract_level_NO_SUPPORTED_CONTRACTION"]==["G_CONSTRAINT_B","G_LEX_DV_REOPEN_B","G_COMP_EXPLICIT"]
    assert not result["anti_downstream_flags"]["actual_Q_extension_defined"]
    assert not result["anti_downstream_flags"]["authorization_performed"]

    if deep:
        base=target["G_CONSTRAINT_B"]
        for p in pairs:
            for alt in TOK:
                if alt==base[p]:continue
                r=dict(base); r[p]=alt
                assert exact_search(r,"D2") is None
        for p in pairs:
            for alt in TOK:
                if alt==base[p]:continue
                r=dict(base); r[p]=alt
                assert exact_search(r,"D1") is None
    return {"matrix":matrix,"successful_witnesses":witness,"gate_pass":True}

if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--root",default=None); ap.add_argument("--deep-certificates",action="store_true")
    a=ap.parse_args(); root=Path(a.root) if a.root else Path(__file__).resolve().parent
    print(canon(run(root,a.deep_certificates)))
