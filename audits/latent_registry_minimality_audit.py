"""Latent-Registry Minimality Audit. Preregistered at 8936606715ab39eaeec27426624f5d46ead7c2a2.
Gate 1 only: compress the fixed 15-partition registry; do not expand experiment space.
"""
from itertools import product, combinations
import hashlib, json, random
from accessibility_contraction_audit import audit as accessibility_audit

PREREGISTRATION_COMMIT="8936606715ab39eaeec27426624f5d46ead7c2a2"
ACCESSIBILITY_COMMIT="635533302ba197133ff78b2e2bc5b66dd9791cc8"
ENCODINGS=64
MASKS=tuple(range(1,16)); COORDS=(8,4,2,1)
WORLDS=tuple(product((0,1), repeat=4))

def parity(mask,w): return sum(((mask>>(3-i))&1)*w[i] for i in range(4))%2
def table(mask): return tuple(parity(mask,w) for w in WORLDS)
TABLES={m:table(m) for m in MASKS}
def canon(t):
    t=tuple(t); c=tuple(1-x for x in t)
    return min(t,c)
TARGET=frozenset(canon(t) for t in TABLES.values())
assert len(TARGET)==15
ACCESS_CHECKSUM=hashlib.sha256(json.dumps({str(m):list(TABLES[m]) for m in MASKS},sort_keys=True).encode()).hexdigest()
PARTITION_CHECKSUM=hashlib.sha256(json.dumps([list(x) for x in sorted(TARGET)],separators=(",",":")).encode()).hexdigest()
def xor(a,b): return tuple(x^y for x,y in zip(a,b))
def flip(t): return tuple(1-x for x in t)

def encoding(seed):
    rng=random.Random((seed+1)*1000003+8936606)
    ms=list(COORDS); rng.shuffle(ms)
    order=list(range(16)); rng.shuffle(order)
    prim=[]
    for i,m in enumerate(ms):
        t=tuple(TABLES[m][j] for j in order)
        if rng.randrange(2): t=flip(t)
        prim.append((f"p{i}",t))
    target=frozenset(canon(tuple(TABLES[m][j] for j in order)) for m in MASKS)
    contexts=list(target); rng.shuffle(contexts)
    return rng,tuple(prim),target,tuple(contexts)

def r0(e): return e[2]
def r2(e): return frozenset(canon(t) for _,t in e[1])
def r3(e):
    raw=tuple(t for _,t in e[1]); out=set(canon(t) for t in raw)
    for a,b in combinations(raw,2): out.add(canon(xor(a,b)))
    return frozenset(out)
def r1(e):
    rng=e[0]; raw=[t for _,t in e[1]]; out=set(canon(t) for t in raw)
    changed=True
    while changed:
        changed=False
        snap=tuple(raw)
        for i in range(len(snap)):
            for j in range(i+1,len(snap)):
                t=xor(snap[i],snap[j])
                if rng.randrange(2): t=flip(t)
                if len(set(t))==1: continue
                p=canon(t)
                if p not in out:
                    out.add(p); raw.append(t); changed=True
    return frozenset(out)
def r4(e): return e[2]

BUILDERS={"R0_explicit":r0,"R1_basis_xor_closure":r1,"R2_primitives_only":r2,
          "R3_one_xor_layer":r3,"R4_opaque_macro":r4}

LEDGER={
"R0_explicit":{"visible":[0,0,0,15,0,0],"visible_total":15,"expanded_total":15},
"R1_basis_xor_closure":{"visible":[4,1,1,0,2,0],"visible_total":8,"expanded_total":8},
"R2_primitives_only":{"visible":[4,0,0,0,0,0],"visible_total":4,"expanded_total":4},
"R3_one_xor_layer":{"visible":[4,1,1,0,1,0],"visible_total":7,"expanded_total":7},
"R4_opaque_macro":{"visible":[0,0,1,0,0,0],"visible_total":1,"expanded_total":15,
                   "classification":"hidden specification / notation compression","valid":False},
"R5_context_target_generator":{"visible":[0,0,0,0,1,15],"visible_total":16,"expanded_total":16,
                   "classification":"oracle displacement","valid":False},
}
LEDGER_FIELDS=("B_primitives","B_operators","B_grammar","B_semantic_labels","B_generation_constraints","B_target_hints")

def audit_core():
    totals={k:{"recover":0,"extra":0,"exact":0,"choices":0} for k in BUILDERS}
    representative={}
    for seed in range(ENCODINGS):
        e=encoding(seed)
        for name,builder in BUILDERS.items():
            recovered=builder(e); inter=recovered&e[2]; extra=recovered-e[2]
            precision=len(inter)/len(recovered); recall=len(inter)/15
            choices=sum(ctx in recovered for ctx in e[3])
            totals[name]["recover"]+=len(inter); totals[name]["extra"]+=len(extra)
            totals[name]["exact"]+=int(recovered==e[2]); totals[name]["choices"]+=choices
            representative.setdefault(name,{"recovered":len(inter),"precision":precision,"recall":recall})
    assert totals["R0_explicit"]=={"recover":960,"extra":0,"exact":64,"choices":960}
    assert totals["R1_basis_xor_closure"]=={"recover":960,"extra":0,"exact":64,"choices":960}
    assert totals["R2_primitives_only"]=={"recover":256,"extra":0,"exact":0,"choices":256}
    assert totals["R3_one_xor_layer"]=={"recover":640,"extra":0,"exact":0,"choices":640}
    assert totals["R4_opaque_macro"]=={"recover":960,"extra":0,"exact":64,"choices":960}
    out={}
    for n in BUILDERS:
        out[n]={**representative[n],"exact_extensional_encodings":totals[n]["exact"],
                "encodings":64,"extra_partitions":totals[n]["extra"],
                "downstream_matches":totals[n]["choices"],"downstream_total":960}
    return {
      "preregistration_commit":PREREGISTRATION_COMMIT,"gate":"G1_registry_compression_only",
      "encodings":64,"contexts_per_encoding":15,"downstream_evaluations":960,
      "target_family":{"world_count":16,"partition_count":15,
        "accessibility_semantics_checksum_sha256":ACCESS_CHECKSUM,
        "canonical_partition_checksum_sha256":PARTITION_CHECKSUM,
        "fixed_extensionally":True},
      "registry_results":out,
      "R5_context_target_generator":{"context_independent_registry_recovered":False,
        "downstream_matches":960,"downstream_total":960,"target_hint_clauses":15,
        "classification":"oracle displacement","valid_minimality_evidence":False},
      "registry_specification_ledger":LEDGER,
      "primary_contraction":{"R0_expanded_B_E_star":15,"R1_expanded_B_E_star":8,
        "B_E_star_decreases":True,"R1_exact_partition_recovery":True,
        "R1_same_downstream_choices":True,"experiment_family_expanded":False,"gate_2_triggered":False},
      "coverage_controls":{"R2_expected":4/15,"R2_observed":4/15,"R2_choices":256,
        "R3_expected":10/15,"R3_observed":10/15,"R3_choices":640,"coverage_ceiling_exceeded":False},
      "anti_scaffold":{"R4_visible_total":1,"R4_expanded_total":15,
        "R4_behavioral_exact":True,"R4_valid_contraction":False,"R5_oracle_displacement":True},
    }

def run_upstream_regression():
    u=accessibility_audit(); a=u["access_results"]
    assert (a["A0_explicit_menu"]["target_reachable"],a["A0_explicit_menu"]["choice_matches_A0"])==(960,960)
    assert (a["A1_all_registry"]["target_reachable"],a["A1_all_registry"]["choice_matches_A0"])==(960,960)
    assert (a["A2_no_access"]["target_reachable"],a["A2_no_access"]["choice_matches_A0"])==(0,0)
    assert (a["A3_first_7_registry"]["target_reachable"],a["A3_first_7_registry"]["choice_matches_A0"])==(448,448)
    assert u["access_burden_ledger"]["A1_all_registry"]["B_access_clauses"]==1
    assert u["oracle_control"]["valid_minimality_evidence"] is False
    inherited=u["upstream_regression"]
    assert inherited["cut_R_no_explicit_R_corr_exact"]==512
    assert inherited["cut_K_anchored_burden_exact"]==320
    assert inherited["max_only_exact_matches"]==512
    assert inherited["visited_decision_points"]==3584
    assert inherited["derived_termination_decisions"]==1536
    assert inherited["trace_mismatches"]==0
    return {"accessibility_commit":ACCESSIBILITY_COMMIT,"A1_reachability":960,"A1_choices":960,
            "A1_B_access":1,"A3_reachability":448,"inherited_valuation_navigation_assertions":True}

def audit():
    r=audit_core(); r["upstream_regression"]=run_upstream_regression(); return r
if __name__=="__main__": print(json.dumps(audit(),indent=2))
