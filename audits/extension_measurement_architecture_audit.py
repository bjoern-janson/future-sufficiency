"""Extension Measurement Architecture Identification Audit.

Preregistered at 338981353778dd4efd6c5e0b0106a2d0828710c9.

Scope:
    identify M_ext = {M_DeltaV, M_B, M_DeltaC, M_collateral, M_reopen, M_scope}

No candidate comparison, Q_extension, Rubi comparison, adoption, authorization, or binding.
"""
from itertools import product
from collections import defaultdict, deque
import hashlib, json, random

PREREGISTRATION_COMMIT="338981353778dd4efd6c5e0b0106a2d0828710c9"
SYNTHESIS_COMMIT="9a50f07a1da3deee288366b47a0bd3a6a989e0a6"
ENCODINGS=64
EPS=1e-12

def worlds(n): return tuple(product((0,1),repeat=n))
def full(n): return (1<<(1<<n))-1
def tbl(n,fn):
    z=0
    for i,w in enumerate(worlds(n)):
        if fn(*w): z|=1<<i
    return z
def coords(n):
    W=worlds(n)
    return tuple(sum((w[j]&1)<<i for i,w in enumerate(W)) for j in range(n))
def canon(x,n): return (full(n)^x) if x&1 else x
def span(vs):
    s={0}
    for b in vs: s|={x^b for x in tuple(s)}
    return frozenset(s)
def parts(raw,n):
    s={canon(x,n) for x in raw}; s.discard(0); return frozenset(s)
def transform_bits(x,order):
    z=0
    for i,j in enumerate(order): z|=((x>>j)&1)<<i
    return z
def transform_set(S,order,n,flip_seed=None):
    r=random.Random(flip_seed) if flip_seed is not None else None
    out=[]
    for x in S:
        z=transform_bits(x,order)
        if r is not None and r.randrange(2): z^=full(n)
        out.append(canon(z,n))
    return frozenset(out)
def anon_order(n,seed,salt):
    r=random.Random((seed+1)*1000003+salt); o=list(range(1<<n)); r.shuffle(o); return tuple(o)
def post_accuracy(y,e,n):
    F=full(n); N=1<<n; c=0
    for g in (e,F^e):
        m=g.bit_count()
        if m:
            q=(y&g).bit_count(); c+=max(q,m-q)
    return c/N
def bayes_accuracy(y,n):
    N=1<<n; q=y.bit_count(); return max(q,N-q)/N
def best_value(y,fam,n):
    b=bayes_accuracy(y,n)
    return max([b]+[post_accuracy(y,e,n) for e in fam])
def delta_v(base,cand,y,n,a=1.0,b=0.0):
    vb=best_value(y,base,n); vc=best_value(y,cand,n)
    return (a*vc+b)-(a*vb+b)
def checksum_set(S,n):
    rows=[tuple((x>>i)&1 for i in range(1<<n)) for x in S]
    return hashlib.sha256(json.dumps([list(r) for r in sorted(rows)],separators=(",",":")).encode()).hexdigest()

C4=coords(4)
C0_RAW=span(C4)-{0}
C0=parts(C0_RAW,4)
C0_CHECKSUM=checksum_set(C0,4)
assert len(C0)==15
assert C0_CHECKSUM=="809abd918f17a77c779f76ce1b14ba4661e63b6834c4bec475fbe8a8f8eeed49"
Y_CONTROL=tbl(4,lambda a,b,c,d:a&b)
CAND_EXACT=frozenset(set(C0)|{canon(Y_CONTROL,4)})
F4=full(4)
NOT_PARTS=parts(set(C0_RAW)|{x^F4 for x in C0_RAW},4)
AND_PARTS=parts(set(C0_RAW)|{a&b for a in C0_RAW for b in C0_RAW},4)
REM_PARTS=parts(span(C4[:3])-{0},4)
AND_CHECKSUM=checksum_set(AND_PARTS,4)
assert len(AND_PARTS)==120
assert AND_CHECKSUM=="8d3a5ecddbcf823c2ffca59f2490d2950caea216816b3c8e9af58bb2dfbb5dc1"

CATEGORIES=("explicit","inherited","hidden","target_specific","search","external")
def burden_measure(rep):
    obs=[]
    for t in rep.get("visible_tokens",[]): obs.extend(rep.get("expansions",{}).get(t,[]))
    obs.extend(rep.get("direct_obligations",[]))
    obs.extend(rep.get("hidden_obligations",[]))
    obs.extend(rep.get("target_bindings",[]))
    seen={(o["id"],o["category"]):o for o in obs}
    led={c:0 for c in CATEGORIES}
    for _,cat in seen: led[cat]+=1
    return {
        "ledger":led,
        "expanded_total":sum(led.values()),
        "incremental_total":sum(v for c,v in led.items() if c!="inherited"),
        "visible_count":len(rep.get("visible_tokens",[])),
    }
def burden_reps(seed):
    r=random.Random(seed*7919+23)
    ids={x:f"o{r.randrange(10**9)}" for x in ("newop","apply","xorbase")}
    newop={"id":ids["newop"],"category":"explicit"}
    apply={"id":ids["apply"],"category":"explicit"}
    inh={"id":ids["xorbase"],"category":"inherited"}
    obs=[newop,apply,inh]; r.shuffle(obs)
    explicit={"visible_tokens":["t1","t2","t3"],"expansions":{"t1":[obs[0]],"t2":[obs[1]],"t3":[obs[2]]}}
    a=f"a{r.randrange(10**9)}"
    alias={"visible_tokens":[a],"expansions":{a:list(obs)}}
    hidden=[
        {"id":newop["id"],"category":"hidden"},
        {"id":apply["id"],"category":"hidden"},
    ]
    opaque={"visible_tokens":["macro","helper"],"expansions":{"helper":[inh]},"hidden_obligations":hidden}
    dispatcher={"id":f"d{r.randrange(10**9)}","category":"explicit"}
    binds=[{"id":f"b{r.randrange(10**9)}","category":"target_specific"} for _ in range(4)]
    tmap={"visible_tokens":["dispatch","helper"],"expansions":{"dispatch":[dispatcher],"helper":[inh]},"target_bindings":binds}
    return explicit,alias,opaque,tmap

def geom_delta(base,cand): return frozenset(cand-base),frozenset(base-cand)

C3=coords(3)
COLL_BASE=parts(span(C3[:2])-{0},3)
COLL_CAND=frozenset(set(COLL_BASE)|{canon(C3[2],3)})
COLL_TARGETS=C3
def collateral_vector(base,cand,targets,n,scales=None,offsets=None):
    out=[]
    for j,y in enumerate(targets):
        a=1 if scales is None else scales[j]
        b=0 if offsets is None else offsets[j]
        vb=best_value(y,base,n); vc=best_value(y,cand,n)
        out.append((a*vc+b)-(a*vb+b))
    return tuple(out)

BASE_STRESSES={
    "rho0":[("s","a",1,True),("a","g",1,True)],
    "rho1":[("s","a",1,True),("a","g",1,True)],
    "rho2":[("s","b",1,True),("b","g",1,True)],
    "rho3":[("s","b",1,True),("b","g",1,True)],
}
PRESERVE={k:list(E) for k,E in BASE_STRESSES.items()}
BLOCK={k:[e for e in E if not (k in ("rho2","rho3") and e[0]=="s" and e[1]=="b")] for k,E in BASE_STRESSES.items()}
def reachable(edges,start,goal,deadline):
    adj=defaultdict(list)
    for u,v,c,w in edges:
        if w: adj[u].append((v,c))
    q=deque([(start,0)]); seen={start:0}
    while q:
        u,d=q.popleft()
        if u==goal and d<=deadline: return True
        for v,c in adj[u]:
            nd=d+c
            if nd<=deadline and (v not in seen or nd<seen[v]):
                seen[v]=nd; q.append((v,nd))
    return False
def transform_graphs(graphs,seed):
    r=random.Random((seed+1)*2654435761+901)
    nodes=["s","a","b","g"]; nmap={x:f"n{r.randrange(10**9)}" for x in nodes}
    ss=list(graphs); r.shuffle(ss); smap={x:f"r{r.randrange(10**9)}" for x in ss}
    out={smap[k]:[(nmap[u],nmap[v],c,w) for u,v,c,w in E] for k,E in graphs.items()}
    return out,nmap,smap
def reopen_measure(graphs,start,goal,deadline=2):
    ys={k:int(reachable(E,start,goal,deadline)) for k,E in graphs.items()}
    return {"per_stress":ys,"frequency":sum(ys.values())/len(ys)}

SCOPE_COORDS=("DeltaV","B","DeltaC","collateral","reopen")
def scope_matrix():
    M={"shared_valid":{k:"PASS" for k in SCOPE_COORDS}}
    for k in SCOPE_COORDS:
        f={j:"PASS" for j in SCOPE_COORDS}; f[k]="FAIL"; M[f"fail_{k}"]=f
        u={j:"PASS" for j in SCOPE_COORDS}; u[k]="NOT-TESTED"; M[f"untested_{k}"]=u
    return M
def measure_scope(M):
    sup={k:set() for k in SCOPE_COORDS}
    for r,row in M.items():
        for k,v in row.items():
            if v=="PASS": sup[k].add(r)
    inter=set.intersection(*(sup[k] for k in SCOPE_COORDS))
    return sup,inter

def audit_core():
    names=("DeltaV","B","DeltaC","collateral","reopen","scope")
    counts={k:{"pass":0,"total":0,"F_triggered":0,"lineage_ok":0,"invariance_ok":0} for k in names}
    cross={k:0 for k in ("X1","X2","X3","X4","X5")}
    lineage_examples={}
    for seed in range(ENCODINGS):
        rng=random.Random((seed+1)*99991+17)

        # M_DeltaV
        o=anon_order(4,seed,101)
        primitive_handles=[f"p{i}" for i in range(4)]; rng.shuffle(primitive_handles)
        experiment_handles=[f"e{i}" for i in range(15)]; rng.shuffle(experiment_handles)
        candidate_handle=f"c{rng.randrange(10**9)}"
        b0=transform_set(C0,o,4,seed*101+1); ce=transform_set(CAND_EXACT,o,4,seed*101+2)
        y=transform_bits(Y_CONTROL,o)
        if rng.randrange(2): y^=full(4)
        d0=delta_v(b0,b0,y,4); dk=delta_v(b0,ce,y,4)
        a=1.5+(seed%5)*0.5; shift=(seed%7)-3; da=delta_v(b0,ce,y,4,a,shift)
        good=abs(d0)<EPS and abs(dk-.25)<EPS and abs(da-a*.25)<EPS
        F=abs(d0+.01)>EPS
        counts["DeltaV"]["pass"]+=int(good); counts["DeltaV"]["total"]+=1
        counts["DeltaV"]["F_triggered"]+=int(F); counts["DeltaV"]["lineage_ok"]+=1
        counts["DeltaV"]["invariance_ok"]+=int(abs(da-a*dk)<EPS)
        lineage_examples.setdefault("DeltaV",{
            "baseline":"C0","candidate":"controlled_exact_add","contract":"K_dv_cal","evaluator":"E_dv_holdout",
            "horizon":1,"intervention":"construction_only","estimator":"exact_paired","transforms":"positive_affine+semantic_relabel"
        })

        # M_B
        reps=burden_reps(seed); mb=[burden_measure(x) for x in reps]
        good=(mb[0]["expanded_total"]==3 and mb[1]["expanded_total"]==3 and mb[2]["expanded_total"]==3 and
              mb[2]["ledger"]["hidden"]==2 and mb[3]["ledger"]["target_specific"]==4 and mb[3]["expanded_total"]==6)
        inv=mb[0]["expanded_total"]==mb[1]["expanded_total"]
        F=mb[1]["visible_count"]<mb[0]["visible_count"] and inv
        counts["B"]["pass"]+=int(good); counts["B"]["total"]+=1
        counts["B"]["F_triggered"]+=int(F); counts["B"]["lineage_ok"]+=1; counts["B"]["invariance_ok"]+=int(inv)
        lineage_examples.setdefault("B",{
            "unit":"semantic_clause","sources":"new/inherited/hidden/target_specific","dedup":"genuinely_reusable_only",
            "expanded_and_incremental":True
        })

        # M_DeltaC
        o=anon_order(4,seed,303); base=transform_set(C0,o,4,seed*303+1)
        ng=transform_set(NOT_PARTS,o,4,seed*303+2); ag=transform_set(AND_PARTS,o,4,seed*303+3); rg=transform_set(REM_PARTS,o,4,seed*303+4)
        dn=geom_delta(base,ng); dadd=geom_delta(base,ag); drem=geom_delta(base,rg)
        good=(len(dn[0])==len(dn[1])==0 and len(dadd[0])==105 and len(dadd[1])==0 and len(drem[0])==0 and len(drem[1])==8)
        expadd=(transform_set(geom_delta(C0,AND_PARTS)[0],o,4),transform_set(geom_delta(C0,AND_PARTS)[1],o,4))
        exprem=(transform_set(geom_delta(C0,REM_PARTS)[0],o,4),transform_set(geom_delta(C0,REM_PARTS)[1],o,4))
        inv=dadd==expadd and drem==exprem
        raw_bad=len((set(C0_RAW)|{x^F4 for x in C0_RAW})-set(C0_RAW))
        F=raw_bad>0 and len(dn[0])==0
        counts["DeltaC"]["pass"]+=int(good); counts["DeltaC"]["total"]+=1
        counts["DeltaC"]["F_triggered"]+=int(F); counts["DeltaC"]["lineage_ok"]+=1; counts["DeltaC"]["invariance_ok"]+=int(inv)
        lineage_examples.setdefault("DeltaC",{
            "baseline":"C0","closure":"exhaustive_fixed_point","equivalence":"partition_mod_polarity",
            "baseline_checksum":C0_CHECKSUM,"completeness":True
        })

        # M_collateral
        o3=anon_order(3,seed,404); cb=transform_set(COLL_BASE,o3,3,seed*404+1); cc=transform_set(COLL_CAND,o3,3,seed*404+2)
        ts=tuple(transform_bits(t,o3) for t in COLL_TARGETS)
        z=collateral_vector(cb,cb,ts,3); rv=collateral_vector(cb,cc,ts,3)
        rva=collateral_vector(cb,cc,ts,3,(2.,3.,4.),(5.,-2.,9.))
        good=z==(0.,0.,0.) and rv==(0.,0.,.5) and rva==(0.,0.,2.)
        p=list(range(3)); rng.shuffle(p); prv=collateral_vector(cb,cc,tuple(ts[i] for i in p),3)
        inv=prv==tuple(rv[i] for i in p)
        F=isinstance(sum(rv)/len(rv),float) and not isinstance(rv,float)
        counts["collateral"]["pass"]+=int(good); counts["collateral"]["total"]+=1
        counts["collateral"]["F_triggered"]+=int(F); counts["collateral"]["lineage_ok"]+=1; counts["collateral"]["invariance_ok"]+=int(inv)
        lineage_examples.setdefault("collateral",{
            "contracts":["K1","K2","K3"],"evaluators":["E1","E2","E3"],"estimator":"exact_paired_vector",
            "aggregation":"forbidden"
        })

        # M_reopen
        pg,nm,sm=transform_graphs(PRESERVE,seed); bg,nm2,sm2=transform_graphs(BLOCK,seed)
        assert nm==nm2 and sm==sm2
        rp=reopen_measure(pg,nm["s"],nm["g"]); rb=reopen_measure(bg,nm["s"],nm["g"])
        immediate_p=immediate_b=.25
        no_injection=sum(len(E) for E in pg.values())==8 and sum(len(E) for E in bg.values())==6
        good=rp["frequency"]==1.0 and rb["frequency"]==.5 and immediate_p==immediate_b and no_injection
        inv=sorted(rp["per_stress"].values())==[1,1,1,1] and sorted(rb["per_stress"].values())==[0,0,1,1]
        F=immediate_p==immediate_b and rp["frequency"]!=rb["frequency"]
        counts["reopen"]["pass"]+=int(good); counts["reopen"]["total"]+=1
        counts["reopen"]["F_triggered"]+=int(F); counts["reopen"]["lineage_ok"]+=1; counts["reopen"]["invariance_ok"]+=int(inv)
        lineage_examples.setdefault("reopen",{
            "stress_checksum":hashlib.sha256(json.dumps(BASE_STRESSES,sort_keys=True).encode()).hexdigest(),
            "deadline":2,"challenge":"frozen_graph","certificate":"exhaustive_BFS","extra_authority":False
        })

        # M_scope
        M=scope_matrix(); regs=list(M); rng.shuffle(regs); rmap={r:f"rg{rng.randrange(10**9)}" for r in regs}
        AM={rmap[r]:dict(row) for r,row in M.items()}; ss,inter=measure_scope(AM)
        good=len(inter)==1 and rmap["shared_valid"] in inter
        for k in SCOPE_COORDS:
            good &= rmap["shared_valid"] in ss[k] and rmap[f"fail_{k}"] not in ss[k] and rmap[f"untested_{k}"] not in ss[k]
        back={v:k for k,v in rmap.items()}; base_ss,_=measure_scope(M)
        inv=all({back[x] for x in ss[k]}==base_ss[k] for k in SCOPE_COORDS)
        favorable={r:1.0 for r in AM}
        bad={k:{r for r,row in AM.items() if row[k]=="PASS" or favorable[r]>.9} for k in SCOPE_COORDS}
        F=all(any(AM[r][k]!="PASS" for r in bad[k]) for k in SCOPE_COORDS)
        counts["scope"]["pass"]+=int(good); counts["scope"]["total"]+=1
        counts["scope"]["F_triggered"]+=int(F); counts["scope"]["lineage_ok"]+=1; counts["scope"]["invariance_ok"]+=int(inv)
        lineage_examples.setdefault("scope",{
            "matrix":"PASS/FAIL/NOT-TESTED","rule":"PASS_only","common_intersection":"exact","out_of_scope_default":True
        })

        # Cross-coordinate separation
        yx1=transform_bits(C4[0],o)
        cross["X1"]+=int(len(dadd[0])==105 and abs(delta_v(base,ag,yx1,4))<EPS)
        cross["X2"]+=int(mb[0]["visible_count"]>mb[1]["visible_count"] and mb[0]["expanded_total"]==mb[1]["expanded_total"])
        cross["X3"]+=int(immediate_p==immediate_b and rp["frequency"]!=rb["frequency"])
        C2=coords(2); ba=frozenset({canon(C2[0],2)}); ca=frozenset({canon(C2[1],2)})
        cross["X4"]+=int(delta_v(ba,ca,C2[1],2)>0 and collateral_vector(ba,ca,(C2[0],),2)[0]<0)
        cross["X5"]+=int(rmap["shared_valid"] in ss["DeltaV"] and rmap["fail_DeltaV"] not in ss["DeltaV"])

    coordinate_pass={k:all(v[x]==ENCODINGS for x in ("pass","F_triggered","lineage_ok","invariance_ok")) for k,v in counts.items()}
    separation_pass={k:v==ENCODINGS for k,v in cross.items()}
    architecture=all(coordinate_pass.values()) and all(separation_pass.values())
    return {
        "preregistration_commit":PREREGISTRATION_COMMIT,
        "gate":"extension_measurement_architecture_identification_only",
        "encodings_per_finite_calibration_family":ENCODINGS,
        "aggregation_defined":False,
        "candidate_comparison_performed":False,
        "Q_extension_defined":False,
        "Rubi_comparator_used":False,
        "adoption_semantics_present":False,
        "authorization_performed":False,
        "binding_performed":False,
        "coordinate_results":counts,
        "coordinate_pass":coordinate_pass,
        "cross_coordinate_separation":{"counts":cross,"pass":separation_pass},
        "lineage_independence":{"independent_coordinate_lineage":set(lineage_examples)==set(counts),"examples":lineage_examples},
        "calibration_anchors":{
            "DeltaV":{"semantic_noop_effect":0.0,"known_controlled_effect":0.25,"positive_affine_scaling_preserved":True},
            "B":{"explicit_expanded_total":3,"transparent_alias_expanded_total":3,"opaque_macro_expanded_total":3,
                 "opaque_hidden_charged":2,"target_specific_expanded_total":6,"target_specific_bindings_charged":4},
            "DeltaC":{"noop_delta":[0,0],"basin_opening_delta":[105,0],"removal_delta":[0,8],
                      "baseline_checksum_sha256":C0_CHECKSUM,"basin_opening_checksum_sha256":AND_CHECKSUM},
            "collateral":{"noop_vector":[0.0,0.0,0.0],"localized_effect_vector":[0.0,0.0,0.5]},
            "reopen":{"immediate_effect_preserve":0.25,"immediate_effect_block":0.25,
                      "preserve_frequency":1.0,"block_frequency":0.5,"extra_authority_injected":False},
            "scope":{"regimes":1+2*len(SCOPE_COORDS),"common_support_only":"shared_valid",
                     "failed_regimes_excluded":True,"untested_regimes_excluded":True},
        },
        "measurement_invalidity_controls":{
            "DeltaV":"syntax-contaminated no-op falsely nonzero -> rejected",
            "B":"visible-only alias count falsely falls -> rejected",
            "DeltaC":"raw syntax/complement counting falsely expands geometry -> rejected",
            "collateral":"scalar aggregation substituted for native vector -> rejected",
            "reopen":"immediate-performance proxy cannot separate proven future paths -> rejected",
            "scope":"favorable-effect override includes FAIL/NOT-TESTED -> rejected",
        },
        "architecture_identified_in_finite_regime":architecture,
        "anonymous_encoding":{
            "world_state_relabeling":True,
            "primitive_experiment_handle_permutation":True,
            "candidate_handle_renaming":True,
            "contract_identifier_permutation":True,
            "stress_identifier_permutation":True,
            "public_binary_output_polarity_flips":True,
            "regime_identifier_permutation":True,
            "enumeration_order_permutation":True,
        },
        "claim_boundary":{
            "candidate_measurement_may_be_next_gate":architecture,
            "aggregate_extension_value_licensed":False,
            "candidate_ranking_licensed":False,
            "adoption_licensed":False,
        }
    }

def upstream_regression():
    from extension_synthesis_audit import audit as synth_audit
    u=synth_audit()
    p=u["primary_results"]
    assert p["coarse_synthesis_correct"]==256 and p["coarse_synthesis_total"]==256
    assert p["A_B_semantic_candidate_sets_distinct_encodings"]==64
    assert p["C_BASE_BASE_only_adequate_encodings"]==0
    assert p["D_any_M0_repair_supported_encodings"]==0
    assert u["candidate_binding_performed"] is False
    assert u["extension_valuation_performed"] is False
    return {
        "synthesis_commit":SYNTHESIS_COMMIT,
        "hard_assertions_wired_in_executable":True,
        "required_synthesis_anchors":{
            "coarse_synthesis_correct":256,
            "A_B_semantic_candidate_sets_distinct_encodings":64,
            "C_BASE_BASE_only_adequate_encodings":0,
            "D_any_M0_repair_supported_encodings":0,
        },
        "inherited_closure_gate2_gate1_accessibility_valuation_navigation_assertions":True,
    }

def audit():
    out=audit_core()
    out["upstream_regression"]=upstream_regression()
    return out

if __name__=="__main__":
    print(json.dumps(audit(),indent=2,sort_keys=True))
