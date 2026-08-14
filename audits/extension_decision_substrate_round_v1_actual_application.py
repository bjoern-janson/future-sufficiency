"""DSLI_R1 actual application executor.

Preregistered at f8a76956ecfbf4848b62659e6db23c3918311679.
Execution ordering is binding:
  1) verify frozen semantic bundle and run 24,576-cell n=4 conformance;
  2) only after conformance passes, read the frozen actual preference target blob;
  3) evaluate all 4 x 6 application cells;
  4) run nuisance/pair-swap checks, serialize results, emit STOP_DSLI_R1.

No language/governance selection, Q_extension, authorization, binding, or v2 update.
"""
from __future__ import annotations

import base64
import hashlib
import importlib.util
import itertools
import json
import lzma
import os
import platform
import sys
from collections import defaultdict, deque
from pathlib import Path

PI = "PREFER_I"
PJ = "PREFER_J"
EQ = "EQUIVALENT"
NWP = "NO_WARRANTED_PREFERENCE"
TOKENS = (PI, PJ, EQ, NWP)
LANGUAGES = (
    "L_ORD1",
    "L_RADIUS1",
    "L_BANDS1",
    "L_INTERSECT2",
    "L_POSET",
    "L_SPARSE_LINEAR",
)
GOVERNANCE = (
    "G_PARTIAL_EMPTY",
    "G_CONSTRAINT_B",
    "G_LEX_DV_REOPEN_B",
    "G_COMP_EXPLICIT",
)
PREREG_COMMIT = "f8a76956ecfbf4848b62659e6db23c3918311679"
APPLICATION_SET_FREEZE = "f0c594bc9ed70856ec980a06926275584db79086"
CHARACTERIZATION_ANCHOR = "ddffe4b976352b3fec4efc3300a0dcc0097ca217"
CONSTRUCTION_COMMIT = "6482667d3b48c2e0c47bfea2fb44da92187b0511"
SPECCOMPLETE_COMMIT = "0f2e2e9cf38258b583dc3d7f9bbbf2cd047fcf53"

SPEC_MD_BLOB = "9f3ab86278d8ed9e2c15f2ee24fe3f05a8def556"
SPEC_MD_SHA256 = "d3913e6082ace84e8b6f7f511d35012a5e80ad554e1bc5f9a2575d1c7c7f1148"
SPEC_JSON_BLOB = "fadf2241923ba6ae2e14d3c2bb5c42b8276f31f6"
SPEC_JSON_SHA256 = "8793022b6aab79f754153631dacb99b9ce9655285e63a101613540b35a802bf2"
REFERENCE_BLOB = "a0938d91fb13fccc7d3865e8ee98e8ed449f91d5"
REFERENCE_SHA256 = "d3d1a85a4ba614931b2194549e94187d09368799940e148a702c9b960a57fe24"
TARGET_RESULT_BLOB = "7efc07e54de9b7e4719caee632daecab32e56f1f"
TARGET_EXEC_BLOB = "b568d90be09bcfa23b4a67ebbdeb90be64bce02f"
TARGET_AUDIT_BLOB = "26c5bebb205e320df8bb8c40f60a393ccf542455"
NATIVE_RESULT_BLOB = "3e332072502fa64c432b143e6d157fc1f5cd18b8"
PREF_EXEC_BLOB = "b47c0884dcb7769a2ca9b934e8a9b64dad218399"
PREF_RESULT_BLOB = "4fab22d2a7be25b001b679fe92e67187098ce696"
PAIR_SHA = "76ae7638e225973f21b90605a9c020a74e752143d1dd008bd2f894fdbd4629aa"

HERE = Path(__file__).resolve().parent
REF_PATH = HERE / "extension_decision_substrate_round_v1_reference.py"
SPEC_MD_PATH = HERE / "extension_decision_substrate_round_v1_specification.md"
SPEC_JSON_PATH = HERE / "extension_decision_substrate_round_v1_specification.json"
TARGET_PATH = HERE / "extension_candidate_preference_application_results.json"
TARGET_EXEC_PATH = HERE / "extension_candidate_preference_application_audit.py"
TARGET_AUDIT_PATH = HERE / "extension_candidate_preference_application_audit.md"
RESULT_PATH = HERE / "extension_decision_substrate_round_v1_actual_application_results.json"
AUDIT_PATH = HERE / "extension_decision_substrate_round_v1_actual_application_audit.md"
RUNTIME_PATH = HERE / "extension_decision_substrate_round_v1_actual_application_runtime.json"


def canon(x):
    return json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def git_blob_sha(b):
    return hashlib.sha1(f"blob {len(b)}\0".encode() + b).hexdigest()


def verify_file(path, blob, sha256=None):
    b = path.read_bytes()
    assert git_blob_sha(b) == blob, (path.name, git_blob_sha(b), blob)
    if sha256 is not None:
        assert sha256_bytes(b) == sha256, (path.name, sha256_bytes(b), sha256)
    return b


def pairs(n):
    return list(itertools.combinations(range(n), 2))


def swap_token(t):
    return PJ if t == PI else PI if t == PJ else t


def relation_records(r):
    return [{"i": i, "j": j, "token": r[i, j]} for i, j in sorted(r)]


def relation_sha256(r):
    return sha256_bytes(canon(relation_records(r)).encode())


def status(rep, burden, n):
    if not rep:
        return "NOT_REPRESENTABLE"
    return "FAITHFUL_CONTRACTION" if burden < n * (n - 1) // 2 else "ADMISSIBLE_REPRESENTATION_NO_CONTRACTION"


def blocks_from_eq(r, n):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[b] = a
    for i, j in pairs(n):
        if r[i, j] == EQ:
            union(i, j)
    d = defaultdict(list)
    for i in range(n):
        d[find(i)].append(i)
    blocks = sorted((tuple(sorted(v)) for v in d.values()), key=lambda z: z[0])
    for block in blocks:
        for i, j in itertools.combinations(block, 2):
            if r[i, j] != EQ:
                return None
    root_of = {x: block[0] for block in blocks for x in block}
    qr = {}
    for A, B in itertools.combinations(blocks, 2):
        ra, rb = A[0], B[0]
        vals = set()
        for x in A:
            for y in B:
                i, j = sorted((x, y))
                t = r[i, j]
                if t == EQ:
                    return None
                if t == NWP:
                    vals.add(NWP)
                else:
                    winner = i if t == PI else j
                    vals.add("A" if root_of[winner] == ra else "B")
        if len(vals) != 1:
            return None
        qr[ra, rb] = next(iter(vals))
    return blocks, root_of, qr


def quotient_edges(qr):
    E = set()
    for (a, b), t in qr.items():
        if t == "A": E.add((a, b))
        elif t == "B": E.add((b, a))
    return E


def acyclic(nodes, E):
    indeg = {x: 0 for x in nodes}
    adj = {x: [] for x in nodes}
    for a, b in E:
        adj[a].append(b); indeg[b] += 1
    q = deque(sorted(x for x in nodes if indeg[x] == 0)); seen = 0
    while q:
        x = q.popleft(); seen += 1
        for y in sorted(adj[x]):
            indeg[y] -= 1
            if indeg[y] == 0: q.append(y)
    return seen == len(nodes)


def closure(nodes, E):
    adj = {x: [] for x in nodes}
    for a, b in E: adj[a].append(b)
    C = set()
    for a in nodes:
        stack = list(adj[a]); seen = set()
        while stack:
            b = stack.pop()
            if b in seen: continue
            seen.add(b); C.add((a, b)); stack.extend(adj[b])
    return C


def lex_topological_order(nodes, E):
    indeg = {x: 0 for x in nodes}; adj = {x: [] for x in nodes}
    for a, b in E: adj[a].append(b); indeg[b] += 1
    avail = sorted(x for x in nodes if indeg[x] == 0); out = []
    while avail:
        x = avail.pop(0); out.append(x)
        for y in sorted(adj[x]):
            indeg[y] -= 1
            if indeg[y] == 0: avail.append(y); avail.sort()
    return tuple(out) if len(out) == len(nodes) else None


def all_lex_topological_orders(nodes, E):
    nodes = tuple(sorted(nodes)); adj = {x: [] for x in nodes}; indeg0 = {x: 0 for x in nodes}
    for a, b in E: adj[a].append(b); indeg0[b] += 1
    for x in adj: adj[x].sort()
    def rec(prefix, indeg, remaining):
        for x in sorted(y for y in remaining if indeg[y] == 0):
            indeg2 = dict(indeg); rem2 = set(remaining); rem2.remove(x)
            for y in adj[x]: indeg2[y] -= 1
            if not rem2: yield tuple(prefix + [x])
            else: yield from rec(prefix + [x], indeg2, rem2)
    if not nodes: yield ()
    else: yield from rec([], indeg0, set(nodes))


def decode_score_relation(blocks, scores, kind, params, n):
    root_of = {x: block[0] for block in blocks for x in block}; out = {}
    for i, j in pairs(n):
        ri, rj = root_of[i], root_of[j]
        if ri == rj: out[i, j] = EQ; continue
        d = scores[ri] - scores[rj]
        if kind == "ORD": out[i, j] = PI if d > 0 else PJ
        elif kind == "RADIUS":
            out[i, j] = NWP if abs(d) <= params else (PI if d > 0 else PJ)
        else:
            t1, t2, pol = params; a = abs(d); k = 0 if a <= t1 else 1 if a <= t2 else 2
            out[i, j] = NWP if pol[k] == "NWP" else (PI if d > 0 else PJ)
    return out


def decode_structural(blocks, kind, state, n):
    bi = {x: k for k, b in enumerate(blocks) for x in b}; out = {}
    if kind == "INTERSECT2":
        o1, o2 = state; p1 = {b: k for k, b in enumerate(o1)}; p2 = {b: k for k, b in enumerate(o2)}
    elif kind == "POSET":
        E = state; C = closure(tuple(range(len(blocks))), E)
    else: E = state
    for i, j in pairs(n):
        a, b = bi[i], bi[j]
        if a == b: out[i, j] = EQ; continue
        if kind == "INTERSECT2":
            if (p1[a] < p1[b]) == (p2[a] < p2[b]): out[i, j] = PI if p1[a] < p1[b] else PJ
            else: out[i, j] = NWP
        elif kind == "POSET":
            out[i, j] = PI if (a, b) in C else PJ if (b, a) in C else NWP
        else:
            out[i, j] = PI if (a, b) in E else PJ if (b, a) in E else NWP
    return out


def target_token_for_roots(qr, a, b):
    i, j = sorted((a, b)); t = qr[i, j]
    if a < b: return t
    if t == "A": return "B"
    if t == "B": return "A"
    return t


def score_decode_roots(sa, sb, kind, params):
    d = sa - sb
    if kind == "RADIUS": return NWP if abs(d) <= params else ("A" if d > 0 else "B")
    t1, t2, pol = params; m = abs(d); k = 0 if m <= t1 else 1 if m <= t2 else 2
    return NWP if pol[k] == "NWP" else ("A" if d > 0 else "B")


def search_scores_exact(roots, qr, n, kind, params):
    roots = tuple(sorted(roots)); assigned = {}; used = set(); scores = tuple(range(n))
    def consistent(root, score):
        for old, old_score in assigned.items():
            if score_decode_roots(score, old_score, kind, params) != target_token_for_roots(qr, root, old): return False
        return True
    def rec(k):
        if k == len(roots): return dict(assigned) if 0 in used else None
        root = roots[k]
        for s in scores:
            if s in used or not consistent(root, s): continue
            assigned[root] = s; used.add(s); ans = rec(k + 1)
            if ans is not None: return ans
            used.remove(s); del assigned[root]
        return None
    return rec(0)


def evaluate(language, r, n):
    q = blocks_from_eq(r, n)
    if q is None: return False, None, None, "exact algebraic"
    blocks, _, qr = q; roots = tuple(b[0] for b in blocks); c = len(blocks); E = quotient_edges(qr)
    if language == "L_ORD1":
        if any(v == NWP for v in qr.values()) or not acyclic(roots, E): return False, None, None, "exact algebraic"
        order = lex_topological_order(roots, E); scores = {root: c - 1 - k for k, root in enumerate(order)}
        return True, n + 3, {"kind":"ORD","blocks":[list(b) for b in blocks],"scores":scores}, "exact algebraic"
    if language == "L_RADIUS1":
        for tau in range(n):
            scores = search_scores_exact(roots, qr, n, "RADIUS", tau)
            if scores is not None: return True, n + 5, {"kind":"RADIUS","blocks":[list(b) for b in blocks],"scores":scores,"tau":tau}, "exact exhaustive constraint"
        return False, None, None, "exact exhaustive constraint"
    if language == "L_BANDS1":
        for t1 in range(n):
            for t2 in range(t1, n):
                for pol in itertools.product(("DIRECTION","NWP"), repeat=3):
                    scores = search_scores_exact(roots, qr, n, "BANDS", (t1,t2,pol))
                    if scores is not None: return True, n + 7, {"kind":"BANDS","blocks":[list(b) for b in blocks],"scores":scores,"tau_1":t1,"tau_2":t2,"policies":list(pol)}, "exact exhaustive constraint"
        return False, None, None, "exact exhaustive constraint"
    if language == "L_INTERSECT2":
        if not acyclic(roots,E) or closure(roots,E) != E: return False,None,None,"exact algebraic"
        r2b = {b[0]:k for k,b in enumerate(blocks)}
        for o1r in all_lex_topological_orders(roots,E):
            rank={x:k for k,x in enumerate(o1r)}; C=set(E)
            for a,b in itertools.combinations(roots,2):
                if qr[a,b] == NWP: C.add((b,a) if rank[a] < rank[b] else (a,b))
            if acyclic(roots,C):
                o2r=lex_topological_order(roots,C)
                return True,n+c+5,{"kind":"INTERSECT2","blocks":[list(b) for b in blocks],"order1":[r2b[x] for x in o1r],"order2":[r2b[x] for x in o2r]},"exact lazy finite enumeration"
        return False,None,None,"exact lazy finite enumeration"
    if language == "L_POSET":
        if not acyclic(roots,E) or closure(roots,E) != E: return False,None,None,"exact algebraic"
        cover={(a,b) for a,b in E if not any(x not in (a,b) and (a,x) in E and (x,b) in E for x in roots)}; r2b={b[0]:k for k,b in enumerate(blocks)}
        ce={(r2b[a],r2b[b]) for a,b in cover}
        return True,(n-c)+len(ce)+5,{"kind":"POSET","blocks":[list(b) for b in blocks],"cover_edges":[list(e) for e in sorted(ce)]},"exact algebraic"
    if language == "L_SPARSE_LINEAR":
        if len(E) > n-1: return False,None,None,"exact algebraic"
        r2b={b[0]:k for k,b in enumerate(blocks)}; de={(r2b[a],r2b[b]) for a,b in E}
        return True,(n-c)+len(de)+5,{"kind":"SPARSE_LINEAR","blocks":[list(b) for b in blocks],"direct_edges":[list(e) for e in sorted(de)]},"exact algebraic"
    raise KeyError(language)


def witness_burden(w,n):
    k=w["kind"]; c=len(w["blocks"])
    if k=="ORD": return n+3
    if k=="RADIUS": return n+5
    if k=="BANDS": return n+7
    if k=="INTERSECT2": return n+c+5
    if k=="POSET": return (n-c)+len(w["cover_edges"])+5
    if k=="SPARSE_LINEAR": return (n-c)+len(w["direct_edges"])+5
    raise KeyError(k)


def decode_witness(w,n):
    blocks=[tuple(b) for b in w["blocks"]]; k=w["kind"]
    if k in ("ORD","RADIUS","BANDS"):
        scores={int(a):b for a,b in w["scores"].items()} if any(isinstance(a,str) for a in w["scores"]) else w["scores"]
        if k=="ORD": return decode_score_relation(blocks,scores,"ORD",None,n)
        if k=="RADIUS": return decode_score_relation(blocks,scores,"RADIUS",w["tau"],n)
        return decode_score_relation(blocks,scores,"BANDS",(w["tau_1"],w["tau_2"],tuple(w["policies"])),n)
    if k=="INTERSECT2": return decode_structural(blocks,k,(tuple(w["order1"]),tuple(w["order2"])),n)
    if k=="POSET": return decode_structural(blocks,k,{tuple(e) for e in w["cover_edges"]},n)
    if k=="SPARSE_LINEAR": return decode_structural(blocks,k,{tuple(e) for e in w["direct_edges"]},n)
    raise KeyError(k)


def transport_relation(r,perm,n):
    out={}
    for (i,j),t in r.items():
        a,b=perm[i],perm[j]
        if a<b: out[a,b]=t
        else: out[b,a]=swap_token(t)
    return out


def transport_witness(w,perm):
    old=[tuple(b) for b in w["blocks"]]; uns=[tuple(sorted(perm[x] for x in b)) for b in old]; indexed=sorted(enumerate(uns),key=lambda z:z[1][0]); m={obi:nbi for nbi,(obi,_) in enumerate(indexed)}; new=[list(b) for _,b in indexed]; k=w["kind"]; out={"kind":k,"blocks":new}
    if k in ("ORD","RADIUS","BANDS"):
        oldroot2bi={b[0]:i for i,b in enumerate(old)}; ns={}
        for root,score in w["scores"].items():
            root=int(root); nbi=m[oldroot2bi[root]]; ns[new[nbi][0]]=score
        out["scores"]=ns
        if k=="RADIUS": out["tau"]=w["tau"]
        if k=="BANDS": out.update(tau_1=w["tau_1"],tau_2=w["tau_2"],policies=list(w["policies"]))
    elif k=="INTERSECT2": out["order1"]=[m[x] for x in w["order1"]]; out["order2"]=[m[x] for x in w["order2"]]
    elif k=="POSET": out["cover_edges"]=sorted([[m[a],m[b]] for a,b in w["cover_edges"]])
    else: out["direct_edges"]=sorted([[m[a],m[b]] for a,b in w["direct_edges"]])
    return out


def load_reference_after_bundle_verification():
    verify_file(SPEC_MD_PATH,SPEC_MD_BLOB,SPEC_MD_SHA256); verify_file(SPEC_JSON_PATH,SPEC_JSON_BLOB,SPEC_JSON_SHA256); verify_file(REF_PATH,REFERENCE_BLOB,REFERENCE_SHA256)
    spec=importlib.util.spec_from_file_location("dsli_r1_frozen_reference",REF_PATH); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); assert tuple(m.LANG)==LANGUAGES; return m


def run_conformance():
    ref=load_reference_after_bundle_verification(); n=4; ps=pairs(n); total=0; mismatch=[]
    for tup in itertools.product(TOKENS,repeat=len(ps)):
        r={p:t for p,t in zip(ps,tup)}
        for L in LANGUAGES:
            rep,b,w,_=evaluate(L,r,n); rr,bb=ref.pi(L,r,n); a=(rep,b if rep else None,status(rep,b,n)); z=(rr,bb if rr else None,status(rr,bb,n)); total+=1
            if a!=z: mismatch.append({"relation":list(tup),"language":L,"executor":a,"reference":z})
            if rep: assert decode_witness(w,n)==r
    assert total==24576
    if mismatch: raise AssertionError(f"STOP_APPLICATION_CONFORMANCE_FAILURE: {mismatch[:10]}")
    return {"cells_correct":total,"cells_total":24576,"mismatches":0,"gate_pass":True}


def read_actual_targets_after_conformance():
    verify_file(TARGET_EXEC_PATH,TARGET_EXEC_BLOB); verify_file(TARGET_AUDIT_PATH,TARGET_AUDIT_BLOB); wrapper=json.loads(verify_file(TARGET_PATH,TARGET_RESULT_BLOB)); packed=wrapper["application_records"]; assert packed["format"]=="lossless-lzma-base64-json-v1"; raw=lzma.decompress(base64.b64decode(packed["payload_b64"])); assert len(raw)==packed["uncompressed_bytes"] and sha256_bytes(raw)==packed["uncompressed_sha256"]; recs=json.loads(raw); registry=wrapper["candidate_registry"]; ids=[x["candidate_id"] for x in registry]; assert len(ids)==12; pair_ids=list(itertools.combinations(ids,2)); assert sha256_bytes(json.dumps(pair_ids,separators=(",",":")).encode())==PAIR_SHA and len(recs)==264; idx={cid:k for k,cid in enumerate(ids)}; by={g:{} for g in GOVERNANCE}
    for rec in recs:
        g=rec["governance_contract_id"]; a,b=idx[rec["candidate_i"]],idx[rec["candidate_j"]]; assert g in by and a<b and rec["preference_status"] in TOKENS; by[g][a,b]=rec["preference_status"]
    for g in GOVERNANCE: assert set(by[g])==set(pairs(12))
    return by,{g:relation_sha256(by[g]) for g in GOVERNANCE},ids


def nuisance(case_id,n,e):
    H=lambda s:hashlib.sha256(s.encode()).hexdigest()
    return {"candidate_permutation":sorted(range(n),key=lambda i:H(f"{case_id}|perm|{e}|{i}")),"pair_record_order":sorted(pairs(n),key=lambda p:H(f"{case_id}|pair-order|{e}|{p[0]}|{p[1]}")),"aliases":{i:"A_"+H(f"{case_id}|alias|{e}|{i}")[:12] for i in range(n)},"nonce":H(f"{case_id}|nonce|{e}"),"implementation_tag":"TAG_"+H(f"{case_id}|impl|{e}")[:12]}


def execute_application(targets,hashes):
    cells=[]; witnesses={}
    for g in GOVERNANCE:
        for L in LANGUAGES:
            rep,b,w,cert=evaluate(L,targets[g],12); sig=status(rep,b,12)
            if rep: assert decode_witness(w,12)==targets[g]; witnesses[g,L]=w
            cells.append({"governance_contract_id":g,"language_id":L,"target_relation_sha256":hashes[g],"anonymous_candidate_count":12,"pair_count":66,"B_R":66,"Rep":rep,"RepA":True if rep else "NOT_EVALUATED","B_star":b if rep else "NOT_DEFINED","Sigma_outcome":sig,"closure_certificate_type":cert,"minimum_certificate":w if rep else "NOT_DEFINED"})
    assert len(cells)==24; return cells,witnesses


def run_invariance(targets,cells,witnesses):
    by={(x["governance_contract_id"],x["language_id"]):x for x in cells}; tc=tt=wc=wt=0
    for g in GOVERNANCE:
        for e in range(64):
            perm=nuisance("ACTUAL_APPLICATION__"+g,12,e)["candidate_permutation"]; rp=transport_relation(targets[g],perm,12); inv=[None]*12
            for old,new in enumerate(perm): inv[new]=old
            tt+=1; assert transport_relation(rp,inv,12)==targets[g]; tc+=1
            for L in LANGUAGES:
                cell=by[g,L]
                if cell["Rep"]:
                    wt+=1; wp=transport_witness(witnesses[g,L],perm); assert decode_witness(wp,12)==rp; bp=witness_burden(wp,12); assert bp==cell["B_star"] and status(True,bp,12)==cell["Sigma_outcome"]; wc+=1
    pt=pc=wst=wsc=0
    for g in GOVERNANCE:
        for i,j in pairs(12): pt+=1; assert swap_token(swap_token(targets[g][i,j]))==targets[g][i,j]; pc+=1
        for L in LANGUAGES:
            if not by[g,L]["Rep"]: continue
            d=decode_witness(witnesses[g,L],12)
            for i,j in pairs(12): wst+=1; assert swap_token(d[i,j])==swap_token(targets[g][i,j]); wsc+=1
    return {"candidate_permutation_nuisance":{"target_inverse_transport_correct":tc,"target_inverse_transport_total":tt,"representable_witness_transport_correct":wc,"representable_witness_transport_total":wt,"encodings_per_governance":64},"pair_swap":{"target_correct":pc,"target_total":pt,"representable_witness_correct":wsc,"representable_witness_total":wst}}


def summarize(cells):
    counts=defaultdict(int); bg={g:{} for g in GOVERNANCE}
    for x in cells: counts[x["Sigma_outcome"]]+=1; bg[x["governance_contract_id"]][x["language_id"]]={"Sigma_outcome":x["Sigma_outcome"],"B_star":x["B_star"]}
    return {"status_counts":dict(sorted(counts.items())),"by_governance":bg}


def make_audit(result):
    s=result["summary"]; lines=["# Decision-Substrate Language Identification — Round v1 Actual Application Audit","","## Status","","```text","POST_SPECIFICATION_APPLICATION_EVIDENCE","STOP_DSLI_R1","```","",f"Preregistered at `{PREREG_COMMIT}`.","","The execution passed the frozen 24,576-cell n=4 semantic conformance gate before reading the actual target blob.","","## Primary 4 x 6 application surface","","| governance | "+" | ".join(LANGUAGES)+" |","|---|"+"---|"*len(LANGUAGES)]
    for g in GOVERNANCE:
        vals=[]
        for L in LANGUAGES:
            z=s["by_governance"][g][L]; vals.append(f"`{z['Sigma_outcome']}`"+(f" (B*={z['B_star']})" if isinstance(z["B_star"],int) else ""))
        lines.append("| `"+g+"` | "+" | ".join(vals)+" |")
    lines += ["","Aggregate terminal counts:","","```text"]+[f"{k:46s} {v}" for k,v in s["status_counts"].items()]+["```","","These are descriptive application outcomes only. They do not rank or select languages or governance contracts.","","## Conformance and invariance","",f"- semantic conformance: `{result['conformance']['cells_correct']} / {result['conformance']['cells_total']}`; mismatches `0`",f"- nuisance target inverse transport: `{result['invariance']['candidate_permutation_nuisance']['target_inverse_transport_correct']} / {result['invariance']['candidate_permutation_nuisance']['target_inverse_transport_total']}`",f"- representable-witness nuisance transport: `{result['invariance']['candidate_permutation_nuisance']['representable_witness_transport_correct']} / {result['invariance']['candidate_permutation_nuisance']['representable_witness_transport_total']}`",f"- target pair swap: `{result['invariance']['pair_swap']['target_correct']} / {result['invariance']['pair_swap']['target_total']}`",f"- representable-witness pair swap: `{result['invariance']['pair_swap']['representable_witness_correct']} / {result['invariance']['pair_swap']['representable_witness_total']}`","","## Provenance and claim boundary","","Evidence role: `POST_SPECIFICATION_APPLICATION_EVIDENCE`.","","The actual target relations historically predate DSLI_R1; this is not pristine held-out confirmation.","","No output defines a cross-language winner, language weighting/ranking, governance winner, candidate selection, `Q_extension`, authorization, binding, or execution.","","## Anti-downstream state","","```text"]
    for k,v in result["anti_downstream_flags"].items(): lines.append(f"{k} = {str(v).lower() if isinstance(v,bool) else v}")
    lines += ["```","","## Stop","","```text","STOP_DSLI_R1","```","","No v2 design update is performed in this execution."]
    return "\n".join(lines)+"\n"


def main():
    assert platform.python_implementation().lower()=="cpython" and sys.version_info[:3]==(3,12,11),sys.version
    conf=run_conformance(); assert conf["gate_pass"]
    targets,hashes,ids=read_actual_targets_after_conformance(); cells,witnesses=execute_application(targets,hashes); inv=run_invariance(targets,cells,witnesses)
    result={"schema":"dsli-r1-actual-application-v1","round_id":"DSLI_R1","round_version":1,"preregistration_commit":PREREG_COMMIT,"characterization_anchor":CHARACTERIZATION_ANCHOR,"application_set_freeze":APPLICATION_SET_FREEZE,"construction_commit":CONSTRUCTION_COMMIT,"speccomplete_commit":SPECCOMPLETE_COMMIT,"evidence_role":"POST_SPECIFICATION_APPLICATION_EVIDENCE","runtime":{"python_implementation":platform.python_implementation().lower(),"python_version":platform.python_version(),"required_python_version":"3.12.11","exact_runtime_match":platform.python_version()=="3.12.11","floating_point_used":False,"standard_library_only":True,"executor_git_blob_sha":git_blob_sha(Path(__file__).read_bytes()),"executor_sha256":sha256_bytes(Path(__file__).read_bytes()),"github_run_id":os.environ.get("GITHUB_RUN_ID"),"github_run_attempt":os.environ.get("GITHUB_RUN_ATTEMPT"),"github_sha":os.environ.get("GITHUB_SHA"),"github_ref_name":os.environ.get("GITHUB_REF_NAME")},"upstream_anchors":{"actual_preference_application_result_blob":TARGET_RESULT_BLOB,"actual_preference_application_executable_blob":TARGET_EXEC_BLOB,"actual_preference_application_audit_blob":TARGET_AUDIT_BLOB,"actual_candidate_native_comparison_result_blob":NATIVE_RESULT_BLOB,"preference_identification_executable_blob":PREF_EXEC_BLOB,"preference_identification_result_blob":PREF_RESULT_BLOB,"canonical_pair_list_sha256":PAIR_SHA,"specification_md_blob":SPEC_MD_BLOB,"specification_json_blob":SPEC_JSON_BLOB,"reference_blob":REFERENCE_BLOB},"target_relation_sha256":hashes,"candidate_registry_order":ids,"conformance":conf,"primary_cell_count":len(cells),"primary_cells":cells,"summary":summarize(cells),"invariance":inv,"missingness_semantics":{"NOT_DEFINED_is_zero":False,"NOT_DEFINED_is_infinity":False,"NOT_EVALUATED_imputed":False},"anti_downstream_flags":{"actual_target_application_performed":True,"application_evidence_role":"POST_SPECIFICATION_APPLICATION_EVIDENCE","application_set_modified":False,"language_family_modified":False,"language_semantics_modified":False,"characterization_dependent_filtering":False,"characterization_dependent_weighting":False,"application_priority_assigned":False,"cross_language_ranking_performed":False,"cross_language_winner_selected":False,"governance_contract_selected":False,"governance_family_ranked":False,"Q_extension_defined":False,"candidate_ranking_performed":False,"candidate_selected":False,"authorization_performed":False,"binding_performed":False,"execution_performed":False,"v2_design_update_performed":False},"stop_condition":"STOP_DSLI_R1"}
    RESULT_PATH.write_text(canon(result)+"\n",encoding="utf-8"); AUDIT_PATH.write_text(make_audit(result),encoding="utf-8"); RUNTIME_PATH.write_text(canon({"python":sys.version,"platform":platform.platform(),"implementation":platform.python_implementation(),"result_sha256":sha256_bytes(RESULT_PATH.read_bytes()),"audit_sha256":sha256_bytes(AUDIT_PATH.read_bytes()),"stop":"STOP_DSLI_R1"})+"\n",encoding="utf-8"); print(canon({"gate":"PASS","cells":24,"status_counts":result["summary"]["status_counts"],"stop":"STOP_DSLI_R1"}))

if __name__=="__main__": main()
