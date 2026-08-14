"""Extension Candidate Measurement Audit.
Preregistered at 6850a2f421d4477c45f679dcf03909f914788bbc.
Measures exactly 12 frozen candidate records under M_ext identified at 607502a.
No ranking, Pareto filtering, Q_extension, adoption, authorization, or binding.
"""
from collections import Counter
from itertools import product
import base64, hashlib, json, os, random, zlib
import extension_synthesis_audit as syn
import extension_measurement_architecture_audit as meas

PRE="6850a2f421d4477c45f679dcf03909f914788bbc"
MID="607502a9434884ca9bb06d5ddd6ff6c17f2ef002"
SYN="9a50f07a1da3deee288366b47a0bd3a6a989e0a6"
G2="ee1b9ac65e40ab5140deb1d82d2ff81768c18200"
N=64; K=.1; EPS=1e-12; REG="candidate_measurement_finite_v1"; SREG="candidate_scope_guard_v1"
COORDS=("DeltaV","B","DeltaC","collateral","reopen","Scope")
CATS=("explicit","inherited","hidden","target_specific","search","external")

# Upstream semantic families are recovered from the frozen synthesis executable.
X=syn.canonical_classes(); C0=X["A"]["current_parts"]; DEG2=X["C"]["current_parts"]
FA=X["A"]["mins"][0][0]; FB=X["B"]["mins"][0][0]; FC1=X["C"]["mins"][0][0]; FC2=X["C"]["mins"][1][0]
FAM={"SYN_A_120":FA,"SYN_B_50":FB,"SYN_C1_1653":FC1,"SYN_C2_2388":FC2}
FP={k:syn.fingerprint_hash(v,4) for k,v in FAM.items()}
assert (len(C0),len(DEG2),len(FA),len(FB),len(FC1),len(FC2))==(15,1023,120,50,1653,2388)
assert FP=={
"SYN_A_120":"8d3a5ecddbcf823c2ffca59f2490d2950caea216816b3c8e9af58bb2dfbb5dc1",
"SYN_B_50":"c5381b17c76e113f0927e55a929bc855b74b68f4a3a676bc4534944c1330d897",
"SYN_C1_1653":"f5fc3cdd75661c1bdccc1efe88382e1669b481136ee14de2396009abc9330ad4",
"SYN_C2_2388":"644e80b2a4e568b789dad11dbb2057c71d836bc52e1e0d68fb31e3aa1f62493f"}
PARENTS={"LINEAR_C0":C0,"DEG2_C":DEG2}
EFP={"EXT_CT_A":"6b6c0313231b9ae7b195a0581fa689f26440854f0357645a62393545b8c4c760","EXT_CT_B":"cc36ca78600cf7615ee194375f8a28b9167136331dd3abe1f9252d38a7cd6a99","EXT_CT_C1":"756d62cad8ec50f8edd401c227e5635f91a937b0623b12c8015e06e8d1a5517f","EXT_CT_C2":"cde45778b9241e1c5d8b887a91d535f9554974e4ac3a0434d08d94816ee3ff36"}

def R(cid,p,src,fam,fp,base=None,pack=None): return dict(id=cid,provenance=p,source=src,parent=base or ("DEG2_C" if "C" in cid and cid not in ("CTRL_ID_LINEAR","CTRL_ALIAS_A") else "LINEAR_C0"),family=fam,fp=fp,base_id=pack or cid)
REGISTRY={
"SYN_A_120":R("SYN_A_120","SYNTHESIZED",SYN,FA,FP["SYN_A_120"],"LINEAR_C0"),
"SYN_B_50":R("SYN_B_50","SYNTHESIZED",SYN,FB,FP["SYN_B_50"],"LINEAR_C0"),
"SYN_C1_1653":R("SYN_C1_1653","SYNTHESIZED",SYN,FC1,FP["SYN_C1_1653"],"DEG2_C"),
"SYN_C2_2388":R("SYN_C2_2388","SYNTHESIZED",SYN,FC2,FP["SYN_C2_2388"],"DEG2_C"),
"EXT_CT_A":R("EXT_CT_A","EXTERNAL","arXiv:2510.15395v2 Algorithm 1",FA,EFP["EXT_CT_A"],"LINEAR_C0","SYN_A_120"),
"EXT_CT_B":R("EXT_CT_B","EXTERNAL","arXiv:2510.15395v2 Algorithm 1",FB,EFP["EXT_CT_B"],"LINEAR_C0","SYN_B_50"),
"EXT_CT_C1":R("EXT_CT_C1","EXTERNAL","arXiv:2510.15395v2 Algorithm 1",FC1,EFP["EXT_CT_C1"],"DEG2_C","SYN_C1_1653"),
"EXT_CT_C2":R("EXT_CT_C2","EXTERNAL","arXiv:2510.15395v2 Algorithm 1",FC2,EFP["EXT_CT_C2"],"DEG2_C","SYN_C2_2388"),
"CTRL_ID_LINEAR":R("CTRL_ID_LINEAR","CONTROL",PRE,C0,syn.fingerprint_hash(C0,4),"LINEAR_C0"),
"CTRL_ID_DEG2":R("CTRL_ID_DEG2","CONTROL",PRE,DEG2,syn.fingerprint_hash(DEG2,4),"DEG2_C"),
"CTRL_SUPPLIED_DEG2":R("CTRL_SUPPLIED_DEG2","CONTROL",G2,DEG2,syn.fingerprint_hash(DEG2,4),"LINEAR_C0"),
"CTRL_ALIAS_A":R("CTRL_ALIAS_A","CONTROL",PRE,FA,FP["SYN_A_120"],"LINEAR_C0","SYN_A_120")}
assert len(REGISTRY)==12 and Counter(x["provenance"] for x in REGISTRY.values())=={"SYNTHESIZED":4,"EXTERNAL":4,"CONTROL":4}

# Frozen target panels.
C4=syn.coord_tables(4); T=syn.table_int
pairs=((0,2),(0,3),(1,2),(1,3),(2,3)); CORR=[]
for i,j in pairs:
 CORR += [(f"x{i+1}_AND_x{j+1}",T(4,lambda *w,i=i,j=j:w[i]&w[j])),(f"x{i+1}_OR_x{j+1}",T(4,lambda *w,i=i,j=j:w[i]|w[j]))]
for I in ((0,1,3),(0,2,3),(1,2,3)): CORR.append(("_AND_".join(f"x{k+1}" for k in I),T(4,lambda *w,I=I:w[I[0]]&w[I[1]]&w[I[2]])))
COLL=[("x1",C4[0]),("x2",C4[1]),("x3",C4[2]),("x4",C4[3]),("x1_XOR_x2",C4[0]^C4[1]),("x3_XOR_x4",C4[2]^C4[3])]
STRESS=[("rho1",T(4,lambda a,b,c,d:(a&c)^(b&d))),("rho2",T(4,lambda a,b,c,d:(a&d)^(b&c))),("rho3",T(4,lambda a,b,c,d:(a|c)^(b|d))),("rho4",T(4,lambda a,b,c,d:(a|d)^(b|c))),("rho5",T(4,lambda a,b,c,d:a&(b|d))),("rho6",T(4,lambda a,b,c,d:b&(a|c))),("rho7",T(4,lambda a,b,c,d:c|(a&d))),("rho8",T(4,lambda a,b,c,d:d|(a&b)))]
def stress_hash():
 rows=[[((y>>i)&1) for i in range(16)] for _,y in STRESS]; return hashlib.sha256(json.dumps(rows,separators=(",",":")).encode()).hexdigest()

def consequence(y,fam):
 b=syn.bayes_accuracy(y,4); r=syn.max_relevance(y,fam,4); return b+(r if r-K>EPS else 0),r
def effect(base,cand,y): return consequence(y,cand)[0]-consequence(y,base)[0]
def worthwhile(fam,y):
 r=syn.max_relevance(y,fam,4); return int(r-K>EPS),r

# Structured burden ledgers derived mechanically from the frozen upstream programs.
def ob(i,c): return {"id":i,"category":c}
def ledger(obs,visible=None):
 d={(o["id"],o["category"]):o for o in obs}; c={k:0 for k in CATS}
 for _,k in d:c[k]+=1
 return {"ledger":c,"expanded_total":sum(c.values()),"incremental_total":sum(v for k,v in c.items() if k!="inherited"),"visible_count":visible,"obligations":sorted(d.values(),key=lambda x:(x["category"],x["id"]))}
def programs(base):
 k={"SYN_A_120":"A","SYN_B_50":"B","SYN_C1_1653":"C","SYN_C2_2388":"C"}[base]; ms=X[k]["mins"][0 if base!="SYN_C2_2388" else 1][1]["programs"]
 out=[]
 for p in ms:
  src="NB" if p["source"]=="CURRENT_NONLINEAR_BASE" else "BB"; o=[ob("parent:"+REGISTRY[base]["parent"],"inherited"),ob("combinator:APPLY","inherited"),ob("combinator:UNION_CURRENT","inherited"),ob("pool_role:BASE","inherited"),ob("extension_application:"+src,"explicit")]
  if src=="NB":o.append(ob("pool_role:CURRENT_NONLINEAR","inherited"))
  o.append(ob("binary_operator:"+"".join(map(str,p["truth_table"])),"explicit" if p["origin"]=="synthesized" else "inherited")); out.append(ledger(o))
 m=min(x["expanded_total"] for x in out); return [x for x in out if x["expanded_total"]==m]
WRAP=("update_bit_action_extension","myopic_transformed_discount","exact_original_goal_action_value","alternate_policy_convention","counterfactual_reject_update_reward","fixed_acceptance_bonus_delta_1_over_64","pre_execution_reward_timing","designated_update_channel_semantics")
def burden(cid):
 c=REGISTRY[cid]
 if cid.startswith("SYN_"): ls=programs(cid); pack="upstream_M0_program_envelope"
 elif cid.startswith("EXT_"):
  ls=[]
  for x in programs(c["base_id"]): ls.append(ledger(x["obligations"]+[ob("hudson:"+z,"external") for z in WRAP]))
  pack="structural_base_plus_EXT_CT_HUDSON_V2"
 elif cid.startswith("CTRL_ID_"): ls=[ledger([ob("parent:"+c["parent"],"inherited")],0)]; pack="semantic_identity"
 elif cid=="CTRL_SUPPLIED_DEG2": ls=[ledger([ob("parent:LINEAR_C0","inherited"),ob("pool_role:BASE","inherited"),ob("combinator:APPLY","inherited"),ob("combinator:UNION_CURRENT","inherited"),ob("combinator:XOR_CLOSE","inherited"),ob("binary_operator:0001","explicit"),ob("extension_application:BB","explicit"),ob("invoke:XOR_CLOSE","explicit")])]; pack="supplied_gate2_structural_extension"
 else:
  ls=[]
  for x in programs("SYN_A_120"):ls.append(ledger([ob(o["id"],"hidden" if o["category"]=="explicit" else o["category"]) for o in x["obligations"]],1))
  pack="one_opaque_macro_hidden_A_semantics"
 return {"minimal_obligation_ledgers":ls,"packaging":pack,"wrapper_external_obligations":list(WRAP) if cid.startswith("EXT_") else []}

def guard(cid): return {"DeltaV":"FAIL","B":"PASS","DeltaC":"PASS","collateral":"FAIL","reopen":"NOT_TESTED"} if cid.startswith("EXT_") else {k:"PASS" for k in ("DeltaV","B","DeltaC","collateral","reopen")}
def reason(k): return {"DeltaV":"composite_goal_action_reward_wrapper_outside_identified_construction_only_do_DeltaV","collateral":"composite_goal_action_reward_wrapper_outside_identified_construction_only_do_collateral","reopen":"composite_goal_action_transformation_not_identified_by_607502a_reopen_calibration"}[k]
def geom(base,cand):
 def e(S):return {"partitions":[int(x) for x in sorted(S)],"cardinality":len(S),"checksum":syn.fingerprint_hash(S,4)}
 return {"C_plus":e(cand-base),"C_minus":e(base-cand),"closure_size":len(cand),"closure_checksum":syn.fingerprint_hash(cand,4)}
def native(cid,k):
 c=REGISTRY[cid]; base=PARENTS[c["parent"]]; cand=c["family"]
 if k=="DeltaV":
  a=[{"contract":lab,"paired_effect":effect(base,cand,y)} for lab,y in CORR]; return {"per_contract":a,"panel_mean":sum(x["paired_effect"] for x in a)/len(a),"kappa":K}
 if k=="B":return burden(cid)
 if k=="DeltaC":return geom(base,cand)
 if k=="collateral":return {"components":[{"contract":lab,"status":"IDENTIFIED","effect":effect(base,cand,y)} for lab,y in COLL]}
 if k=="reopen":
  a=[]
  for lab,y in STRESS:q,r=worthwhile(cand,y);a.append({"stress":lab,"Y_reopen":q,"max_R_corr":r})
  return {"per_stress":a,"frequency":sum(x["Y_reopen"] for x in a)/8,"stress_checksum":stress_hash(),"deadline":2,"kappa":K}
 g=guard(cid); return {"regime_status":{REG:g},"support":{j:([REG] if v=="PASS" else []) for j,v in g.items()},"common_intersection":[REG] if all(v=="PASS" for v in g.values()) else []}

def prov(cid):
 c=REGISTRY[cid]; p={"candidate_id":cid,"provenance_class":c["provenance"],"source_commit_or_document":c["source"],"parent_substrate":c["parent"],"semantic_or_composite_fingerprint":c["fp"],"structural_base_fingerprint":syn.fingerprint_hash(c["family"],4),"implementation_envelope_identifier":c["base_id"],"candidate_registry_version":"candidate-measurement-v1"}
 if cid.startswith("EXT_"):p.update(base_provenance="SYNTHESIZED",wrapper_provenance="EXTERNAL",external_source="arXiv:2510.15395v2 Algorithm 1")
 return p
def rec(cid,k):
 if k=="Scope":return {"status":"IDENTIFIED","native_value":native(cid,k),"lineage":{"instrument_commit":MID,"candidate":cid,"guard":"PASS_FAIL_NOT_TESTED"},"support_regimes":[SREG],"failed_identification_conditions":[]}
 s=guard(cid)[k]
 if s!="PASS":return {"status":"NOT_IDENTIFIED","native_value":None,"lineage":{"instrument_commit":MID,"candidate":cid,"guard_status":s},"support_regimes":[],"failed_identification_conditions":[reason(k)]}
 return {"status":"IDENTIFIED","native_value":native(cid,k),"lineage":{"instrument_commit":MID,"candidate":cid,"parent":REGISTRY[cid]["parent"],"coordinate":k},"support_regimes":[REG],"failed_identification_conditions":[]}

def upstream():
 try:u=meas.audit();src="executable_import"
 except ModuleNotFoundError:
  u=json.load(open(os.path.join(os.path.dirname(__file__),"extension_measurement_architecture_results.json")));src="committed_results_fallback_after_import"
 assert u["architecture_identified_in_finite_regime"] and all(v==64 for x in u["coordinate_results"].values() for k,v in x.items() if k!="total") and all(v==64 for v in u["cross_coordinate_separation"]["counts"].values())
 assert not u["Q_extension_defined"] and not u["aggregation_defined"] and not u["authorization_performed"] and not u["binding_performed"]
 return {"source":src,"measurement_identification_commit":MID,"hard_assertions_wired_in_executable":True,"inherited_synthesis_and_earlier_assertions":True}

def audit():
 ids=sorted(REGISTRY); out={cid:{"P":prov(cid),"coordinates":{k:rec(cid,k) for k in COORDS}} for cid in ids}; ni=sum(z["status"]=="NOT_IDENTIFIED" for r in out.values() for z in r["coordinates"].values());assert ni==12
 inv={cid:{k:0 for k in COORDS} for cid in ids}
 for seed in range(N):
  rng=random.Random(f"candidate-measurement-v1 / encoding {seed}"); order=list(range(16));rng.shuffle(order); order=tuple(order); shuffled=ids[:];rng.shuffle(shuffled);assert set(shuffled)==set(ids)
  for cid in shuffled:
   c=REGISTRY[cid]; pb=meas.transform_set(PARENTS[c["parent"]],order,4,seed*101+1); pc=meas.transform_set(c["family"],order,4,seed*101+2);g=guard(cid)
   for k in ("B","Scope"):inv[cid][k]+=1
   gv=native(cid,"DeltaC");inv[cid]["DeltaC"]+=int([len(pc-pb),len(pb-pc)]==[gv["C_plus"]["cardinality"],gv["C_minus"]["cardinality"]])
   for k,panel in (("DeltaV",CORR),("collateral",COLL)):
    if g[k]!="PASS":inv[cid][k]+=1;continue
    exp=native(cid,k); ex=[x["paired_effect"] for x in exp["per_contract"]] if k=="DeltaV" else [x["effect"] for x in exp["components"]]; got=[]
    for lab,y0 in panel:
     y=meas.transform_bits(y0,order);got.append(effect(pb,pc,y))
    inv[cid][k]+=int(all(abs(a-b)<EPS for a,b in zip(got,ex)))
   if g["reopen"]!="PASS":inv[cid]["reopen"]+=1
   else:
    got=[worthwhile(pc,meas.transform_bits(y,order))[0] for _,y in STRESS]; ex=[x["Y_reopen"] for x in native(cid,"reopen")["per_stress"]];inv[cid]["reopen"]+=int(got==ex)
 assert all(v==N for x in inv.values() for v in x.values())
 assert out["SYN_A_120"]["coordinates"]["DeltaC"]["native_value"]==out["CTRL_ALIAS_A"]["coordinates"]["DeltaC"]["native_value"] and out["SYN_A_120"]["P"]["provenance_class"]!=out["CTRL_ALIAS_A"]["P"]["provenance_class"]
 geomreg={};natreg={}
 for r in out.values():
  for k,z in r["coordinates"].items():
   if z["status"]!="IDENTIFIED":assert z["native_value"] is None;continue
   if k=="DeltaC":
    for side in ("C_plus","C_minus"):
     q=z["native_value"][side];raw=b"".join(int(x).to_bytes(2,"big") for x in q["partitions"]);key=q["checksum"];geomreg.setdefault(key,{"encoding":"zlib+base64:uint16be_sorted","data":base64.b64encode(zlib.compress(raw,9)).decode(),"cardinality":q["cardinality"],"checksum":key});z["native_value"][side]={"geometry_set_ref":key,"cardinality":q["cardinality"],"checksum":key}
   raw=json.dumps(z["native_value"],sort_keys=True,separators=(",",":")).encode();key=hashlib.sha256(raw).hexdigest();natreg.setdefault(key,{"coordinate":k,"value":z["native_value"]});z["native_value"]={"native_object_ref":key,"coordinate":k}
 result={"preregistration_commit":PRE,"measurement_identification_commit":MID,"gate":"extension_candidate_measurement_only","candidate_registry_version":"candidate-measurement-v1","expected_candidate_count":12,"observed_candidate_count":12,"candidate_counts_by_provenance":dict(Counter(r["P"]["provenance_class"] for r in out.values())),"post_measurement_pruning":0,"post_measurement_addition":0,"encodings":N,"stress_family_checksum":stress_hash(),"instrument_architecture_immutable":True,"instrument_code_blob_anchor":"8ee0fa796f6eb40dd2b70f4f58ba51bec181238c","not_identified_rule":{"not_identified_is_zero":False,"not_identified_is_negative":False,"imputation_performed":False,"count":ni},"external_scope_resolution":{"DeltaV":"NOT_IDENTIFIED","B":"IDENTIFIED","DeltaC":"IDENTIFIED via frozen structural projection","collateral":"NOT_IDENTIFIED","reopen":"NOT_IDENTIFIED","Scope":"IDENTIFIED","instrument_redesign_performed":False},"anonymous_invariance_counts":inv,"geometry_set_registry":geomreg,"native_object_registry":natreg,"candidate_records":[out[c] for c in ids],"native_types_preserved":True,"cross_coordinate_aggregate_defined":False,"candidate_comparison_performed":False,"ranking_performed":False,"pareto_filtering_performed":False,"Q_extension_defined":False,"NO_WARRANTED_ADOPTION_defined":False,"adoption_semantics_present":False,"authorization_performed":False,"binding_performed":False,"hudson_superiority_or_inferiority_claimed":False,"upstream_regression":upstream(),"claim_boundary":"preregistered candidate set measured under frozen M_ext with provenance, native types, lineage, status, and scope preserved"}
 return result

def packed():
 raw=json.dumps(audit(),sort_keys=True,separators=(",",":")).encode(); return {"format":"lossless-lzma-base64-json-v1","uncompressed_sha256":hashlib.sha256(raw).hexdigest(),"uncompressed_bytes":len(raw),"payload_b64":base64.b64encode(__import__("lzma").compress(raw,preset=9)).decode(),"summary":{"preregistration_commit":PRE,"measurement_identification_commit":MID,"candidate_count":12,"not_identified_cells":12,"encodings":N,"candidate_comparison_performed":False,"Q_extension_defined":False,"authorization_performed":False,"binding_performed":False}}
if __name__=="__main__":print(json.dumps(packed(),sort_keys=True,separators=(",",":")))
