"""Closure-Insufficiency Diagnosis Audit.

Preregistered at 133ab57111d57afe2897df84e9202e73b1099b28.

Scope:
    E_failure -> D_closure in {SUFFICIENT, INSUFFICIENT}

No construction change, extension proposal, extension valuation, authorization, or
binding is admitted in this audit.
"""
from collections import Counter, defaultdict
from itertools import product
import hashlib, json, random

PREREGISTRATION_COMMIT = "133ab57111d57afe2897df84e9202e73b1099b28"
GATE2_COMMIT = "ee1b9ac65e40ab5140deb1d82d2ff81768c18200"
ENCODINGS = 64
KAPPA = 0.1
ACTOR_BAD_KAPPA = 0.30
EPS = 1e-12
WORLDS = tuple(product((0,1), repeat=4))

def canon(table):
    t = tuple(table)
    c = tuple(1-x for x in t)
    return min(t,c)

def xor_table(a,b):
    return tuple(x^y for x,y in zip(a,b))

def primitive_tables():
    return tuple(tuple(w[i] for w in WORLDS) for i in range(4))

def closure_xor(primitives):
    raw = list(primitives)
    out = {canon(t) for t in raw}
    changed = True
    while changed:
        changed = False
        snap = tuple(raw)
        for i in range(len(snap)):
            for j in range(i+1,len(snap)):
                t = xor_table(snap[i], snap[j])
                if len(set(t)) == 1:
                    continue
                p = canon(t)
                if p not in out:
                    out.add(p); raw.append(t); changed = True
    return frozenset(out)

C0_CANON = closure_xor(primitive_tables())
assert len(C0_CANON) == 15
C0_CHECKSUM = hashlib.sha256(
    json.dumps([list(x) for x in sorted(C0_CANON)], separators=(",",":")).encode()
).hexdigest()
assert C0_CHECKSUM == "809abd918f17a77c779f76ce1b14ba4661e63b6834c4bec475fbe8a8f8eeed49"

def H_targets():
    fs = (
        lambda x1,x2,x3,x4: x1 & (x2|x3),
        lambda x1,x2,x3,x4: x2 & (x3|x4),
        lambda x1,x2,x3,x4: x3 & (x4|x1),
        lambda x1,x2,x3,x4: x4 & (x1|x2),
    )
    return tuple(tuple(f(*w) for w in WORLDS) for f in fs)

def G_targets():
    fs = (
        lambda x1,x2,x3,x4: (x1&x2) ^ (x3&x4),
        lambda x1,x2,x3,x4: ((1-x1)&x2) ^ (x3&x4),
        lambda x1,x2,x3,x4: (x1&(1-x2)) ^ (x3&x4),
        lambda x1,x2,x3,x4: ((1-x1)&(1-x2)) ^ (x3&x4),
    )
    return tuple(tuple(f(*w) for w in WORLDS) for f in fs)

H = H_targets()
G = G_targets()

def bayes_accuracy(target):
    c = Counter(target)
    return max(c.values())/len(target)

def post_accuracy(target, evidence):
    groups = defaultdict(list)
    for y,e in zip(target,evidence):
        groups[e].append(y)
    correct = 0
    for ys in groups.values():
        c = Counter(ys)
        correct += max(c.values())
    return correct/len(target)

def relevance(target, evidence):
    return post_accuracy(target,evidence) - bayes_accuracy(target)

def profile(target, closure, kappa=KAPPA):
    rows = [(relevance(target,e), e) for e in closure]
    max_r = max(r for r,_ in rows)
    qmax = max_r-kappa
    maxima = [e for r,e in rows if abs(r-max_r)<EPS]
    return {
        "baseline": bayes_accuracy(target),
        "exact_target_in_closure": canon(target) in closure,
        "exact_target_R_corr": 1.0-bayes_accuracy(target),
        "max_R_corr": max_r,
        "max_q": qmax,
        "qmax_count": len(maxima),
        "max_partitions": tuple(maxima),
    }

def encode_table(table, order, flip):
    t = tuple(table[i] for i in order)
    return tuple(x^flip for x in t)

def make_encoding(seed):
    rng = random.Random((seed+1)*1000003 + 133571)
    order = list(range(16)); rng.shuffle(order)
    primitive_order = list(range(4)); rng.shuffle(primitive_order)
    primitive_flips = [rng.randrange(2) for _ in range(4)]
    target_flips = [rng.randrange(2) for _ in range(8)]
    primitives = []
    canonical_prims = primitive_tables()
    for j,i in enumerate(primitive_order):
        primitives.append((f"p{j}", encode_table(canonical_prims[i], order, primitive_flips[j]), i))
    Henc = tuple(encode_table(t,order,target_flips[i]) for i,t in enumerate(H))
    Genc = tuple(encode_table(t,order,target_flips[4+i]) for i,t in enumerate(G))
    ctx = list(range(12)); rng.shuffle(ctx)
    return {"primitives":tuple(primitives),"H":Henc,"G":Genc,"context_order":tuple(ctx),"world_order":tuple(order)}

def recompute_closure(encoded):
    prim_tables = tuple(t for _,t,_ in encoded["primitives"])
    return closure_xor(prim_tables)

def closure_diagnosis(target, closure):
    p = profile(target, closure, KAPPA)
    return ("SUFFICIENT" if p["max_q"] > EPS else "INSUFFICIENT"), p

def actor_search_miss(target, encoded, closure):
    primitive_parts = {canon(t) for _,t,_ in encoded["primitives"]}
    observed = tuple(e for e in closure if e not in primitive_parts)
    p = profile(target, observed, KAPPA)
    return "COMMIT" if p["max_q"] <= EPS else "ACQUIRE", p

def actor_valuation_mishandle(target, closure):
    p = profile(target, closure, ACTOR_BAD_KAPPA)
    return "COMMIT" if p["max_q"] <= EPS else "ACQUIRE", p

def actor_closure_insufficient(target, closure):
    p = profile(target, closure, KAPPA)
    return "COMMIT" if p["max_q"] <= EPS else "ACQUIRE", p

def representation_ceiling(groups):
    bucket = defaultdict(Counter)
    for k,y in groups:
        bucket[k][y] += 1
    correct = sum(max(c.values()) for c in bucket.values())
    return correct/len(groups), correct, len(groups)

def audit_core():
    counts = {
        "SEARCH_MISS":{"correct":0,"total":0,"actor_commit":0},
        "VALUATION_MISHANDLE":{"correct":0,"total":0,"actor_commit":0},
        "CLOSURE_INSUFFICIENT":{"correct":0,"total":0,"actor_commit":0},
    }
    d0=[]; d1=[]; d2=[]; naive_d2_correct=0
    closure_checksums=set()
    exact_outside=0
    total=0

    for seed in range(ENCODINGS):
        enc = make_encoding(seed)
        closure = recompute_closure(enc)
        assert len(closure)==15
        checksum=hashlib.sha256(json.dumps([list(x) for x in sorted(closure)],separators=(",",":")).encode()).hexdigest()
        closure_checksums.add(checksum)

        for target in enc["H"]:
            actor, ap = actor_search_miss(target, enc, closure)
            diag, dp = closure_diagnosis(target, closure)
            assert actor=="COMMIT" and diag=="SUFFICIENT"
            assert abs(dp["baseline"]-0.625)<EPS
            assert dp["exact_target_in_closure"] is False
            assert abs(dp["exact_target_R_corr"]-0.375)<EPS
            assert abs(dp["max_R_corr"]-0.25)<EPS
            assert abs(dp["max_q"]-0.15)<EPS
            assert dp["qmax_count"]==1
            assert abs(ap["max_q"]+0.1)<EPS
            counts["SEARCH_MISS"]["correct"]+=1
            counts["SEARCH_MISS"]["total"]+=1
            counts["SEARCH_MISS"]["actor_commit"]+=1
            exact_outside+=1; total+=1
            d0.append((("unresolved","COMMIT"),"SUFFICIENT"))
            d1.append((round(ap["max_q"],6),"SUFFICIENT"))
            d2.append((False,"SUFFICIENT"))

        for target in enc["H"]:
            actor, ap = actor_valuation_mishandle(target, closure)
            diag, dp = closure_diagnosis(target, closure)
            assert actor=="COMMIT" and diag=="SUFFICIENT"
            assert abs(dp["max_q"]-0.15)<EPS
            assert abs(ap["max_q"]+0.05)<EPS
            counts["VALUATION_MISHANDLE"]["correct"]+=1
            counts["VALUATION_MISHANDLE"]["total"]+=1
            counts["VALUATION_MISHANDLE"]["actor_commit"]+=1
            exact_outside+=1; total+=1
            d0.append((("unresolved","COMMIT"),"SUFFICIENT"))
            d1.append((round(dp["max_q"],6),"SUFFICIENT"))
            d2.append((False,"SUFFICIENT"))

        for target in enc["G"]:
            actor, ap = actor_closure_insufficient(target, closure)
            diag, dp = closure_diagnosis(target, closure)
            assert actor=="COMMIT" and diag=="INSUFFICIENT"
            assert abs(dp["baseline"]-0.625)<EPS
            assert dp["exact_target_in_closure"] is False
            assert abs(dp["exact_target_R_corr"]-0.375)<EPS
            assert abs(dp["max_R_corr"]-0.0)<EPS
            assert abs(dp["max_q"]+0.1)<EPS
            counts["CLOSURE_INSUFFICIENT"]["correct"]+=1
            counts["CLOSURE_INSUFFICIENT"]["total"]+=1
            counts["CLOSURE_INSUFFICIENT"]["actor_commit"]+=1
            exact_outside+=1; total+=1
            d0.append((("unresolved","COMMIT"),"INSUFFICIENT"))
            d1.append((round(dp["max_q"],6),"INSUFFICIENT"))
            d2.append((False,"INSUFFICIENT"))
            naive_d2_correct += 1

    assert total==768 and exact_outside==768
    for name in counts:
        assert counts[name]["correct"]==256
        assert counts[name]["actor_commit"]==256
    c0=representation_ceiling(d0); c1=representation_ceiling(d1); c2=representation_ceiling(d2)
    assert abs(c0[0]-2/3)<EPS and abs(c1[0]-2/3)<EPS and abs(c2[0]-2/3)<EPS
    assert naive_d2_correct==256 and abs(naive_d2_correct/768-1/3)<EPS

    return {
        "preregistration_commit":PREREGISTRATION_COMMIT,
        "gate":"closure_insufficiency_diagnosis_only",
        "construction_changed":False,
        "extension_proposal_present":False,
        "encodings":ENCODINGS,
        "contexts_per_encoding":12,
        "diagnostic_episodes":total,
        "old_closure":{
            "canonical_source_size":len(C0_CANON),
            "canonical_source_checksum_sha256":C0_CHECKSUM,
            "encoded_fixed_point_size_all_encodings":True,
            "distinct_encoded_checksums_due_world_relabeling":len(closure_checksums),
        },
        "matched_panel":{
            "all_exact_targets_outside_current_closure":True,
            "exact_targets_outside_count":exact_outside,
            "baseline_accuracy_all":0.625,
            "exact_target_R_corr_all":0.375,
            "exact_target_q_all":0.275,
            "all_failed_runs_unresolved":True,
            "all_failed_runs_commit":True,
        },
        "target_profiles":{
            "H_closure_sufficient":{"max_R_corr":0.25,"max_q":0.15,"qmax_count":1,"all_other_C0_R_corr":0.0},
            "G_closure_insufficient":{"max_R_corr":0.0,"max_q":-0.1},
        },
        "primary_diagnosis":counts,
        "total_correct":sum(v["correct"] for v in counts.values()),
        "total":total,
        "restricted_controls":{
            "D0_failure_only":{"ceiling":c0[0],"best_correct":c0[1],"total":c0[2]},
            "D1_actor_observed_capacity":{"ceiling":c1[0],"best_correct":c1[1],"total":c1[2]},
            "D2_exact_target_membership":{"ceiling":c2[0],"best_correct":c2[1],"total":c2[2]},
            "D2_naive_outside_implies_insufficient":{"accuracy":naive_d2_correct/total,"correct":naive_d2_correct,"total":total},
            "D3_supplied_qmax_oracle":{"can_be_exact":True,"valid_primary_evidence":False,"classification":"oracle displacement"},
        },
        "earned_boundary":{
            "failure_not_closure_insufficiency":True,
            "exact_target_absence_not_closure_insufficiency":True,
            "diagnosis_not_extension_discovery":True,
        }
    }

def run_upstream_regression():
    from experiment_space_construction_audit import audit as gate2_audit
    u = gate2_audit()
    assert u["old_closure"]["size"] == 15
    assert u["condition_results"]["G20_old_S0"]["target_reachable"] == 0
    assert u["condition_results"]["G20_old_S0"]["commit_decisions"] == 256
    assert u["condition_results"]["G21_AND_plus_post_extension_closure"]["target_reachable"] == 256
    assert u["condition_results"]["G21_AND_plus_post_extension_closure"]["exact_target_chosen"] == 256
    assert u["condition_results"]["G22_NOT_no_new_geometry"]["target_reachable"] == 0
    assert u["condition_results"]["G23_AND_one_layer_only"]["target_reachable"] == 192
    assert u["condition_results"]["G23_AND_one_layer_only"]["exact_target_chosen"] == 192
    return {
        "gate2_commit":GATE2_COMMIT,
        "old_closure_size":15,
        "G20_reachability":0,
        "G20_commit":256,
        "G21_reachability":256,
        "G21_exact_choice":256,
        "G22_reachability":0,
        "G23_reachability":192,
        "G23_exact_choice":192,
        "inherited_gate1_accessibility_valuation_navigation_assertions":True,
    }

def audit():
    out = audit_core()
    out["upstream_regression"] = run_upstream_regression()
    return out

if __name__=="__main__":
    print(json.dumps(audit(),indent=2,sort_keys=True))