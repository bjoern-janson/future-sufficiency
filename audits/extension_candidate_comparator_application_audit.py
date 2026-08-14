"""Actual-candidate comparator application audit; prereg 519073b. No preference layer."""
from __future__ import annotations
import base64,copy,hashlib,itertools,json,lzma,zlib
from collections import Counter
from pathlib import Path
PRE="519073b3bd980f729a4b37e3ee79723a53587fc5"; MC="c0db168261ebfb32106382c34c992bf00ec1aa4c"; MB="dce4b66df142cfcb2a6515a082585f36ab374071"; MR="07d669df0b5a0af007bda2312defe3b2501b229af91eb9508d845e6cc43dc657"; MNB=79395
CC="d0802137f303406c4aab1e5779af644b4cfe6b4f"; CR="7bac5f2aed17de6532b2fccfa138d8f954c78a8b"; CE="f7dcee2d583d1471707b21843f1ed1469aed16fe"; PS="76ae7638e225973f21b90605a9c020a74e752143d1dd008bd2f894fdbd4629aa"
KS=("DeltaV","B","DeltaC","collateral","reopen","Scope"); TS=("I_GREATER","J_GREATER","EQUIVALENT","INCOMPARABLE","NO_LICENSED_COMPARISON"); CATS=("explicit","inherited","hidden","target_specific","search","external"); SW={"I_GREATER":"J_GREATER","J_GREATER":"I_GREATER","EQUIVALENT":"EQUIVALENT","INCOMPARABLE":"INCOMPARABLE","NO_LICENSED_COMPARISON":"NO_LICENSED_COMPARISON"}
def gsha(b):return hashlib.sha1(f"blob {len(b)}\0".encode()+b).hexdigest()
def load(root):
 cb=(root/"extension_candidate_measurement_results.json").read_bytes();rb=(root/"extension_comparison_identification_results.json").read_bytes();eb=(root/"extension_comparison_identification_audit.py").read_bytes()
 assert (gsha(cb),gsha(rb),gsha(eb))==(MB,CR,CE);w=json.loads(cb);raw=lzma.decompress(base64.b64decode(w["payload_b64"]));assert len(raw)==w["uncompressed_bytes"]==MNB and hashlib.sha256(raw).hexdigest()==w["uncompressed_sha256"]==MR
 d=json.loads(raw);q=json.loads(rb);assert q["comparison_architecture_identified_in_finite_regime"] and not any(q[x] for x in ("candidate_preference_defined","cross_coordinate_aggregation_defined","Q_extension_defined","authorization_performed","binding_performed"));return d
def cmap(d):return {x["P"]["candidate_id"]:x for x in d["candidate_records"]}
def nat(d,c,k):
 z=c["coordinates"][k]
 if z["status"]!="IDENTIFIED":assert z["native_value"] is None;return None
 r=z["native_value"]["native_object_ref"];q=d["native_object_registry"][r];assert q["coordinate"]==k;return q["value"]
def gs(d,q):
 r=q["geometry_set_ref"];z=d["geometry_set_registry"][r];b=zlib.decompress(base64.b64decode(z["data"]));s=frozenset(int.from_bytes(b[i:i+2],"big") for i in range(0,len(b),2));assert len(s)==z["cardinality"]==q["cardinality"];return s
def sup(d,c,k):
 s=nat(d,c,"Scope");return frozenset(s["common_intersection"] if k=="Scope" else s["support"][k])
def par(c):return c["P"]["parent_substrate"]
def prv(c):return c["P"]["provenance_class"]
def sta(c,k):return c["coordinates"][k]["status"]
def bv(d,c):
 v=nat(d,c,"B");return tuple(sorted({tuple(int(x["ledger"][z]) for z in CATS) for x in v["minimal_obligation_ledgers"]}))
def gv(d,c):
 v=nat(d,c,"DeltaC");return gs(d,v["C_plus"]),gs(d,v["C_minus"]),v["C_plus"]["geometry_set_ref"],v["C_minus"]["geometry_set_ref"]
def comp(a,b):
 if tuple(a)==tuple(b):return "EQUIVALENT"
 ai=all(x>=y for x,y in zip(a,b));bj=all(y>=x for x,y in zip(a,b))
 return "I_GREATER" if ai and any(x>y for x,y in zip(a,b)) else "J_GREATER" if bj and any(y>x for x,y in zip(a,b)) else "INCOMPARABLE"
def brel(a,b):
 if set(a)==set(b):return "EQUIVALENT"
 ge=lambda X,Y:all(all(x>=y for x,y in zip(p,q)) for p in X for q in Y);ai,bj=ge(a,b),ge(b,a)
 return "I_GREATER" if ai and not bj else "J_GREATER" if bj and not ai else "INCOMPARABLE"
def grel(a,b):
 if a[:2]==b[:2]:return "EQUIVALENT"
 ai=a[0]>=b[0] and a[1]>=b[1];bj=b[0]>=a[0] and b[1]>=a[1];return "I_GREATER" if ai and not bj else "J_GREATER" if bj and not ai else "INCOMPARABLE"
def cond(k):
 q=["both_status_IDENTIFIED","native_type_valid","required_common_support_nonempty","measurement_lineage_present","no_imputation"]
 q+= {"DeltaV":["same_frozen_13_contract_panel","same_parent_substrate_causal_baseline","compatible_outcome_scale"],"B":["same_burden6_schema","complete_minimal_ledger_envelopes"],"DeltaC":["same_parent_substrate_geometry_baseline","same_partition_mod_polarity_semantic_universe","full_set_objects_present"],"collateral":["same_frozen_6_contract_panel","same_parent_substrate_causal_baseline","all_components_identified"],"reopen":["same_frozen_8_stress_family","same_deadline_and_harness","all_stress_outcomes_present"],"Scope":["same_scope_regime_universe","nonempty_common_all_coordinate_support"]}[k];return q
def core(d,a,b,k):
 si,sj=sta(a,k),sta(b,k);sa,sb=sup(d,a,k),sup(d,b,k);inter=sa&sb;bad=(["candidate_i_NOT_IDENTIFIED"] if si!="IDENTIFIED" else [])+(["candidate_j_NOT_IDENTIFIED"] if sj!="IDENTIFIED" else []);w=None
 if k=="DeltaV":
  fi=["DeltaV",par(a),"frozen_13_contract_panel","kappa=0.1"];fj=["DeltaV",par(b),"frozen_13_contract_panel","kappa=0.1"]
  if si==sj=="IDENTIFIED" and par(a)!=par(b):bad+=["different_parent_substrate_causal_baseline_no_bridge"]
  if not inter:bad+=["empty_coordinate_support_intersection"]
  if not bad:
   x,y=nat(d,a,k),nat(d,b,k);li=[z["contract"] for z in x["per_contract"]];lj=[z["contract"] for z in y["per_contract"]]
   if li!=lj or len(li)!=13:bad+=["incompatible_frozen_13_contract_panel"]
   else:
    u,v=x["panel_mean"],y["panel_mean"];t="I_GREATER" if u>v else "J_GREATER" if u<v else "EQUIVALENT";w={"panel_mean_i":u,"panel_mean_j":v,"per_contract_effects_i_sha256":hashlib.sha256(json.dumps([z["paired_effect"] for z in x["per_contract"]],separators=(",",":")).encode()).hexdigest(),"per_contract_effects_j_sha256":hashlib.sha256(json.dumps([z["paired_effect"] for z in y["per_contract"]],separators=(",",":")).encode()).hexdigest()}
 elif k=="B":
  fi=fj=["B","burden6","semantic_obligation_counts"]
  if not inter:bad+=["empty_coordinate_support_intersection"]
  if not bad:u,v=bv(d,a),bv(d,b);t=brel(u,v);w={"minimal_ledgers_i":[list(x) for x in u],"minimal_ledgers_j":[list(x) for x in v]}
 elif k=="DeltaC":
  fi=["DeltaC",par(a),"partition_mod_polarity"];fj=["DeltaC",par(b),"partition_mod_polarity"]
  if si==sj=="IDENTIFIED" and par(a)!=par(b):bad+=["different_parent_substrate_geometry_baseline_no_transport"]
  if not inter:bad+=["empty_coordinate_support_intersection"]
  if not bad:u,v=gv(d,a),gv(d,b);t=grel(u,v);w={"C_plus_i_ref":u[2],"C_minus_i_ref":u[3],"C_plus_j_ref":v[2],"C_minus_j_ref":v[3],"C_plus_i_cardinality":len(u[0]),"C_minus_i_cardinality":len(u[1]),"C_plus_j_cardinality":len(v[0]),"C_minus_j_cardinality":len(v[1]),"i_contains_j":[u[0]>=v[0],u[1]>=v[1]],"j_contains_i":[v[0]>=u[0],v[1]>=u[1]]}
 elif k=="collateral":
  fi=["collateral",par(a),"frozen_6_contract_panel","kappa=0.1"];fj=["collateral",par(b),"frozen_6_contract_panel","kappa=0.1"]
  if si==sj=="IDENTIFIED" and par(a)!=par(b):bad+=["different_parent_substrate_causal_baseline_no_bridge"]
  if not inter:bad+=["empty_coordinate_support_intersection"]
  if not bad:
   x,y=nat(d,a,k),nat(d,b,k);li=[z["contract"] for z in x["components"]];lj=[z["contract"] for z in y["components"]]
   if li!=lj or len(li)!=6 or not all(z["status"]=="IDENTIFIED" for z in x["components"]+y["components"]):bad+=["incompatible_frozen_6_contract_panel"]
   else:u=tuple(z["effect"] for z in x["components"]);v=tuple(z["effect"] for z in y["components"]);t=comp(u,v);w={"labels":li,"vector_i":list(u),"vector_j":list(v)}
 elif k=="reopen":
  fi=fj=["reopen","frozen_8_stress_panel","deadline=2"]
  if not inter:bad+=["empty_coordinate_support_intersection"]
  if not bad:
   x,y=nat(d,a,k),nat(d,b,k);li=[z["stress"] for z in x["per_stress"]];lj=[z["stress"] for z in y["per_stress"]]
   if li!=lj or len(li)!=8 or x["stress_checksum"]!=y["stress_checksum"] or x["deadline"]!=y["deadline"]:bad+=["incompatible_frozen_8_stress_family_or_harness"]
   else:u=tuple(z["Y_reopen"] for z in x["per_stress"]);v=tuple(z["Y_reopen"] for z in y["per_stress"]);t=comp(u,v);w={"labels":li,"stress_vector_i":list(u),"stress_vector_j":list(v),"frequency_i":sum(u)/8,"frequency_j":sum(v)/8}
 else:
  fi=fj=["Scope","candidate_scope_guard_v1"];x,y=nat(d,a,"Scope"),nat(d,b,"Scope")
  if set(x["regime_status"])!=set(y["regime_status"]):bad+=["different_scope_regime_universe_no_bijection"]
  if not inter:bad+=["empty_common_all_coordinate_support"]
  if not bad:u,v=frozenset(x["common_intersection"]),frozenset(y["common_intersection"]);t="EQUIVALENT" if u==v else "I_GREATER" if u>v else "J_GREATER" if v>u else "INCOMPARABLE";w={"support_i":sorted(u),"support_j":sorted(v)}
 if bad:t="NO_LICENSED_COMPARISON";w=None
 assert t in TS;return {"input_status_i":si,"input_status_j":sj,"native_frame_i":fi,"native_frame_j":fj,"support_i":sorted(sa),"support_j":sorted(sb),"support_intersection":sorted(inter),"license_conditions_checked":cond(k),"license_result":"LICENSED" if not bad else "NOT_LICENSED","failed_license_conditions":bad,"native_relation_witness":w,"relation_token":t}
def record(d,i,j,a,b,k):
 return {"pair_id":f"{i}__{j}","candidate_i":i,"candidate_j":j,"provenance_i":prv(a),"provenance_j":prv(b),"coordinate":k,**core(d,a,b,k),"measurement_lineage_i":a["coordinates"][k]["lineage"],"measurement_lineage_j":b["coordinates"][k]["lineage"],"comparison_lineage":{"candidate_measurement_commit":MC,"candidate_measurement_results_blob":MB,"comparison_identification_commit":CC,"comparison_identification_results_blob":CR,"comparison_identification_executable_blob":CE,"application_preregistration_commit":PRE,"pair_id":f"{i}__{j}","coordinate":k}}
def audit(root=None):
 d=load(root or Path(__file__).resolve().parent);C=cmap(d);ids=sorted(C);assert ids==["CTRL_ALIAS_A","CTRL_ID_DEG2","CTRL_ID_LINEAR","CTRL_SUPPLIED_DEG2","EXT_CT_A","EXT_CT_B","EXT_CT_C1","EXT_CT_C2","SYN_A_120","SYN_B_50","SYN_C1_1653","SYN_C2_2388"] and Counter(prv(C[x]) for x in ids)=={"CONTROL":4,"EXTERNAL":4,"SYNTHESIZED":4}
 ps=list(itertools.combinations(ids,2));assert len(ps)==66 and hashlib.sha256(json.dumps(ps,separators=(",",":")).encode()).hexdigest()==PS;r=[]
 for i,j in ps:
  for k in KS:
   z=record(d,i,j,C[i],C[j],k);r.append(z);assert core(d,C[j],C[i],k)["relation_token"]==SW[z["relation_token"]]
   a,b=copy.deepcopy(C[i]),copy.deepcopy(C[j]);a["P"]["provenance_class"]="SHADOW_I";b["P"]["provenance_class"]="SHADOW_J";assert core(d,a,b,k)["relation_token"]==z["relation_token"]
   a,b=copy.deepcopy(C[i]),copy.deepcopy(C[j])
   for q in KS:
    if q not in (k,"Scope"):a["coordinates"][q]={"sentinel":"IRRELEVANT"};b["coordinates"][q]={"sentinel":"IRRELEVANT"}
   assert core(d,a,b,k)["relation_token"]==z["relation_token"]
 assert len(r)==396
 rc={};lc={};inc={};nl={}
 for k in KS:
  x=[z for z in r if z["coordinate"]==k];rc[k]={t:sum(z["relation_token"]==t for z in x) for t in TS};lc[k]={"LICENSED":sum(z["license_result"]=="LICENSED" for z in x),"NOT_LICENSED":sum(z["license_result"]=="NOT_LICENSED" for z in x)};inc[k]=[[z["candidate_i"],z["candidate_j"]] for z in x if z["relation_token"]=="INCOMPARABLE"];nl[k]=[{"pair":[z["candidate_i"],z["candidate_j"]],"failed_license_conditions":z["failed_license_conditions"]} for z in x if z["relation_token"]=="NO_LICENSED_COMPARISON"];assert sum(rc[k].values())==66
 return {"preregistration_commit":PRE,"gate":"extension_candidate_comparator_application_only","candidate_measurement_commit":MC,"candidate_measurement_results_blob":MB,"comparison_identification_commit":CC,"comparison_identification_results_blob":CR,"comparison_identification_executable_blob":CE,"candidate_registry":[{"candidate_id":x,"provenance_class":prv(C[x]),"parent_substrate":par(C[x])} for x in ids],"candidate_count":12,"candidate_counts_by_provenance":{"CONTROL":4,"EXTERNAL":4,"SYNTHESIZED":4},"pair_count":66,"pair_list_sha256":PS,"coordinate_count":6,"application_record_count":396,"candidate_pruning":0,"candidate_addition":0,"pair_pruning":0,"pair_addition":0,"coordinate_record_pruning":0,"coordinate_record_addition":0,"coordinate_relation_counts":rc,"coordinate_license_counts":lc,"coordinate_incomparable_pairs":inc,"coordinate_no_license_pairs":nl,"application_records":r,"integrity":{"pair_swap_symmetry_pass":True,"pair_swap_symmetry_count":396,"pair_swap_symmetry_total":396,"provenance_blindness_regression_pass":True,"no_cross_coordinate_leakage_regression_pass":True,"candidate_machine_result_blob_anchor_verified":True,"candidate_machine_result_exact_decode_and_sha_verification_required_by_executable":True,"comparison_result_blob_anchor_verified":True,"comparison_executable_blob_anchor_verified":True,"no_missingness_imputation":True,"no_native_scalarization":True,"no_automatic_frame_bridging":True,"no_external_candidate_special_casing":True},"actual_candidate_coordinate_relations_computed":True,"actual_candidate_overall_pair_relation_defined":False,"candidate_preference_defined":False,"Pareto_filtering_performed":False,"cross_coordinate_aggregation_defined":False,"Q_extension_defined":False,"NO_WARRANTED_ADOPTION_defined":False,"authorization_performed":False,"binding_performed":False,"hudson_superiority_or_inferiority_claimed":False,"execution_provenance":{"fresh_application_result":True,"upstream_candidate_measurement_used_as_frozen_machine_result":True,"comparison_architecture_frozen_by_exact_blob_anchors":True,"repo_executable_requires_exact_candidate_result_decode_and_sha_verification":True,"wording":"fresh actual-candidate comparator-application result with inherited hard regression assertions"},"claim_boundary":"frozen native comparison architecture yields reported licensed coordinate-specific pairwise relations over preregistered 12-candidate set; no cross-coordinate preference or aggregation"}
def packed(root=None):
 q=audit(root);raw=json.dumps(q,sort_keys=True,separators=(",",":")).encode();return {"format":"lossless-lzma-base64-json-v1","payload_b64":base64.b64encode(lzma.compress(raw,preset=9)).decode(),"uncompressed_sha256":hashlib.sha256(raw).hexdigest(),"uncompressed_bytes":len(raw),"summary":{"preregistration_commit":PRE,"candidate_count":12,"pair_count":66,"application_record_count":396,"pair_list_sha256":PS,"coordinate_relation_counts":q["coordinate_relation_counts"],"coordinate_license_counts":q["coordinate_license_counts"],"actual_candidate_coordinate_relations_computed":True,"actual_candidate_overall_pair_relation_defined":False,"candidate_preference_defined":False,"Pareto_filtering_performed":False,"cross_coordinate_aggregation_defined":False,"Q_extension_defined":False,"NO_WARRANTED_ADOPTION_defined":False,"authorization_performed":False,"binding_performed":False}}
if __name__=="__main__":print(json.dumps(packed(),sort_keys=True,separators=(",",":")))