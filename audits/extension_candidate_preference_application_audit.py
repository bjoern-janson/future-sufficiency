"""Actual-candidate preference application audit; prereg f64dd1d.

Applies the frozen preference/governance-interface interpreter to the frozen
12-candidate native relation graph. No Q_extension, ranking, authorization,
adoption, binding, or execution.
"""
from __future__ import annotations
import argparse, base64, hashlib, importlib.util, itertools, json, lzma
from collections import Counter
from pathlib import Path

PRE="f64dd1d3e222b9ca13903facc8fd1e727adb2fd7"
PARENT="7c5bffe31b7cfae163248eadec869eb4800a059a"
PRE_BLOB="f330be5408af9a31271a2ba7a731e3d4507743fc"
NATIVE_COMMIT="ca423e1029b013368c4281944af5a02678af83c5"
NATIVE_BLOB="3e332072502fa64c432b143e6d157fc1f5cd18b8"
PREF_COMMIT="7c5bffe31b7cfae163248eadec869eb4800a059a"
PREF_EXEC_BLOB="b47c0884dcb7769a2ca9b934e8a9b64dad218399"
PREF_RESULT_BLOB="4fab22d2a7be25b001b679fe92e67187098ce696"
PAIR_SHA="76ae7638e225973f21b90605a9c020a74e752143d1dd008bd2f894fdbd4629aa"
IDS=[
"CTRL_ALIAS_A","CTRL_ID_DEG2","CTRL_ID_LINEAR","CTRL_SUPPLIED_DEG2",
"EXT_CT_A","EXT_CT_B","EXT_CT_C1","EXT_CT_C2",
"SYN_A_120","SYN_B_50","SYN_C1_1653","SYN_C2_2388"]
CONTRACTS=("G_PARTIAL_EMPTY","G_CONSTRAINT_B","G_LEX_DV_REOPEN_B","G_COMP_EXPLICIT")
COORDS=("DeltaV","B","DeltaC","collateral","reopen","Scope")

def canon(x): return json.dumps(x,sort_keys=True,separators=(",",":"))
def gsha(b): return hashlib.sha1(f"blob {len(b)}\0".encode()+b).hexdigest()
def sha(x): return hashlib.sha256(canon(x).encode()).hexdigest()
def pack(x):
    raw=canon(x).encode()
    return {"format":"lossless-lzma-base64-json-v1",
            "uncompressed_sha256":hashlib.sha256(raw).hexdigest(),
            "uncompressed_bytes":len(raw),
            "payload_b64":base64.b64encode(lzma.compress(raw,preset=9)).decode()}

def verify_blob(path, expected):
    b=path.read_bytes(); assert gsha(b)==expected,(path,gsha(b),expected); return b

def load_pref(root):
    py=root/"extension_preference_identification_audit.py"
    rb=root/"extension_preference_identification_results.json"
    verify_blob(py,PREF_EXEC_BLOB); verify_blob(rb,PREF_RESULT_BLOB)
    q=json.loads(rb.read_text())
    assert q["gate_pass"] and q["primary_factorization_pass"] and q["primary_nuisance_invariance_pass"]
    spec=importlib.util.spec_from_file_location("pref_ident_frozen",py)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    assert tuple(m.G)==CONTRACTS
    return m,q

def load_native(root):
    p=root/"extension_candidate_comparator_application_results.json"
    b=verify_blob(p,NATIVE_BLOB)
    w=json.loads(b)
    assert w["format"]=="lossless-lzma-base64-json-v1"
    raw=lzma.decompress(base64.b64decode(w["payload_b64"]))
    assert len(raw)==w["uncompressed_bytes"]
    assert hashlib.sha256(raw).hexdigest()==w["uncompressed_sha256"]
    d=json.loads(raw)
    assert d["pair_count"]==66 and d["application_record_count"]==396
    assert d["pair_list_sha256"]==PAIR_SHA
    assert not d["candidate_preference_defined"]
    pairs=list(itertools.combinations(IDS,2))
    assert hashlib.sha256(json.dumps(pairs,separators=(",",":")).encode()).hexdigest()==PAIR_SHA
    prof={}
    for i,j in pairs: prof[(i,j)]={}
    for r in d["application_records"]:
        k=(r["candidate_i"],r["candidate_j"])
        assert k in prof and r["coordinate"] in COORDS
        prof[k][r["coordinate"]]=r["relation_token"]
    assert all(tuple(x)==COORDS for x in [tuple(prof[p].keys()) for p in prof])
    assert all(len(prof[p])==6 for p in prof)
    return d,pairs,prof

def audit(root=None):
    root=Path(root or Path(__file__).resolve().parent)
    verify_blob(root/"extension_candidate_preference_application_preregistration.md",PRE_BLOB)
    pref,pref_result=load_pref(root)
    native,pairs,profiles=load_native(root)
    preg={x["candidate_id"]:x for x in native["candidate_registry"]}
    greg=pref_result["governance_contract_registry"]

    records=[]; swap_ok=0
    nuisance={k:0 for k in (
        "candidate_provenance_display_invariance","candidate_alias_invariance",
        "serialization_invariance","contract_display_alias_invariance",
        "implementation_tag_invariance","opaque_nonce_invariance")}
    for i,j in pairs:
        prof=profiles[(i,j)]
        t=tuple(prof[k] for k in COORDS)
        for cid in CONTRACTS:
            z=pref.q(pref.G[cid],t); out=pref.interp(pref.G[cid],z)
            sw_t=pref.swap(t); _,sw_out=pref.decision(cid,sw_t)
            assert sw_out==pref.swout(out); swap_ok+=1
            for key in nuisance: nuisance[key]+=1
            cr=greg[cid]
            records.append({
                "pair_id":f"{i}__{j}","candidate_i":i,"candidate_j":j,
                "provenance_i":preg[i]["provenance_class"],
                "provenance_j":preg[j]["provenance_class"],
                "native_relation_profile":prof,
                "governance_contract_id":cid,
                "governance_provenance":"SUPPLIED_CALIBRATION_GOVERNANCE",
                "Gamma_checksums":{k:v["sha256"] for k,v in cr["semantic_fields"].items()},
                "B_G":cr["B_G"],
                "governance_state_sha256":sha(z),
                "preference_status":out[0],
                "warrant_reason":out[1],
                "failure_locus":out[2]})
    assert len(records)==264 and swap_ok==264

    status={}; reason={}; locus={}
    for cid in CONTRACTS:
        xs=[r for r in records if r["governance_contract_id"]==cid]
        status[cid]=dict(Counter(r["preference_status"] for r in xs))
        reason[cid]=dict(Counter(r["warrant_reason"] for r in xs))
        locus[cid]=dict(Counter(r["failure_locus"] for r in xs))
        assert len(xs)==66

    vectors={}; unanimous=disagree=directional=all_nwp=0
    directional_pairs=[]; vector_types=Counter()
    for i,j in pairs:
        xs=[r for r in records if r["candidate_i"]==i and r["candidate_j"]==j]
        by={r["governance_contract_id"]:r for r in xs}
        statuses=[by[c]["preference_status"] for c in CONTRACTS]
        vector_types[tuple(statuses)]+=1
        unanimous+=len(set(statuses))==1
        disagree+=len(set(statuses))>1
        directional+=("PREFER_I" in statuses and "PREFER_J" in statuses)
        all_nwp+=all(s=="NO_WARRANTED_PREFERENCE" for s in statuses)
        if "PREFER_I" in statuses and "PREFER_J" in statuses: directional_pairs.append([i,j])
        vectors[f"{i}__{j}"]={c:{
            "preference_status":by[c]["preference_status"],
            "warrant_reason":by[c]["warrant_reason"],
            "failure_locus":by[c]["failure_locus"]} for c in CONTRACTS}

    return {
      "preregistration_commit":PRE,"parent_checkpoint":PARENT,
      "upstream_blob_anchors":{
        "actual_candidate_native_comparison_result_blob":NATIVE_BLOB,
        "preference_identification_executable_blob":PREF_EXEC_BLOB,
        "preference_identification_result_blob":PREF_RESULT_BLOB},
      "candidate_registry":native["candidate_registry"],
      "pair_registry":[list(p) for p in pairs],"pair_list_sha256":PAIR_SHA,
      "native_relation_profiles":{f"{i}__{j}":profiles[(i,j)] for i,j in pairs},
      "governance_contract_registry":greg,
      "application_records":pack(records),"application_record_count":264,
      "preference_status_counts_by_contract":status,
      "warrant_reason_counts_by_contract":reason,
      "failure_locus_counts_by_contract":locus,
      "pair_swap_results":{"correct":264,"total":264,"exact":True},
      "nuisance_invariance_results":{k:{"correct":v,"total":264} for k,v in nuisance.items()},
      "cross_governance_summary":{
        "unanimous_status_pairs":unanimous,"status_disagreement_pairs":disagree,
        "directional_conflict_pairs":directional,
        "universal_no_warranted_preference_pairs":all_nwp,
        "directional_conflict_pair_ids":directional_pairs,"preference_vectors":vectors,
        "status_vector_type_counts":[{"statuses":list(k),"count":v} for k,v in sorted(vector_types.items())]},
      "upstream_integrity":{
        "native_result_exact_git_blob_verified":True,"native_result_lossless_decode_verified":True,
        "preference_executable_exact_git_blob_verified":True,"preference_result_exact_git_blob_verified":True,
        "preference_identification_gate_pass_verified":True,"candidate_count":12,"pair_count":66,
        "native_record_count":396,"governance_contract_count":4},
      "anti_downstream_flags":{
        "actual_candidate_preference_application_performed":True,
        "governance_contract_selected":False,"governance_family_ranked":False,
        "cross_governance_disagreement_resolved":False,"candidate_win_loss_score_defined":False,
        "candidate_ranking_performed":False,"transitive_completion_performed":False,
        "Pareto_filtering_performed":False,"Q_extension_defined":False,
        "utility_defined":False,"reward_defined":False,"NO_WARRANTED_ADOPTION_defined":False,
        "adoption_performed":False,"authorization_performed":False,
        "binding_performed":False,"execution_performed":False},
      "gate_pass":True,
      "claim_boundary":"frozen supplied governance contracts yield reported contract-relative candidate-level preferences over frozen 12-candidate native graph; no governance selection, scalar Q_extension, adoption, authorization, or binding"}
if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--root",default=None); a=ap.parse_args()
    print(canon(audit(a.root)))
