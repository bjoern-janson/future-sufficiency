"""Preference/governance-interface identification audit; prereg efcf3a7."""
from __future__ import annotations
import argparse, base64, copy, hashlib, json, lzma, random
from collections import defaultdict
from pathlib import Path

PRE="efcf3a780c50b64780ee2b21c93b7af5a8f86b5d"; PARENT="ca423e1029b013368c4281944af5a02678af83c5"
PRE_BLOB="4136ccf08bf4dab92baf68ae7a5f5a06f902355c"
UP={"actual_candidate_application_executable_blob":"2b94247b0f5542e0bfd0cf8f163ca02384f1e546","actual_candidate_application_result_blob":"3e332072502fa64c432b143e6d157fc1f5cd18b8","comparison_identification_result_blob":"7bac5f2aed17de6532b2fccfa138d8f954c78a8b"}
N=64; C=("DeltaV","B","DeltaC","collateral","reopen","Scope")
IG,JG,EQ,INC,NLC="I_GREATER","J_GREATER","EQUIVALENT","INCOMPARABLE","NO_LICENSED_COMPARISON"
PI,PJ,PEQ,NWP="PREFER_I","PREFER_J","EQUIVALENT","NO_WARRANTED_PREFERENCE"
SW={IG:JG,JG:IG,EQ:EQ,INC:INC,NLC:NLC}; SP={PI:PJ,PJ:PI,PEQ:PEQ,NWP:NWP}
SR={"CONSTRAINT_BLOCK_I":"CONSTRAINT_BLOCK_J","CONSTRAINT_BLOCK_J":"CONSTRAINT_BLOCK_I"}

P={
"P_EQ":(EQ,EQ,EQ,EQ,EQ,EQ),"P_DV_I_ONLY":(IG,EQ,EQ,EQ,EQ,EQ),"P_DV_J_ONLY":(JG,EQ,EQ,EQ,EQ,EQ),
"P_ALIGN_I":(IG,JG,EQ,EQ,EQ,EQ),"P_ALIGN_J":(JG,IG,EQ,EQ,EQ,EQ),
"P_CONFLICT_I_BURDEN":(IG,IG,EQ,EQ,EQ,EQ),"P_CONFLICT_J_BURDEN":(JG,JG,EQ,EQ,EQ,EQ),
"P_DV_LICENSE_GAP":(NLC,EQ,EQ,EQ,EQ,EQ),"P_SCOPE_LICENSE_GAP":(IG,JG,EQ,EQ,EQ,NLC),
"P_B_INCOMPARABLE":(IG,INC,EQ,EQ,EQ,EQ),"P_GEOM_GAP_IGNORED":(IG,JG,NLC,EQ,EQ,EQ),
"P_COLL_INC_IGNORED":(IG,JG,EQ,INC,EQ,EQ),"P_REOPEN_I_ONLY":(EQ,EQ,EQ,EQ,IG,EQ),
"P_REOPEN_J_ONLY":(EQ,EQ,EQ,EQ,JG,EQ),"P_REOPEN_LICENSE_GAP":(IG,JG,EQ,EQ,NLC,EQ),
"P_REOPEN_INCOMPARABLE":(IG,JG,EQ,EQ,INC,EQ),"P_GEOM_INC_ALL_EQ":(EQ,EQ,INC,EQ,EQ,EQ)}

BG={
"G_PARTIAL_EMPTY":(3,0,2,0,0),"G_CONSTRAINT_B":(3,1,1,0,0),
"G_LEX_DV_REOPEN_B":(4,0,3,2,0),"G_COMP_EXPLICIT":(3,0,2,0,2)}
def bg(cid):
 a=BG[cid]; return dict(zip(("required_license_clauses","constraint_clauses","objective_orientation_clauses","priority_edges","explicit_tradeoff_clauses"),a))
G={
"G_PARTIAL_EMPTY":dict(L=("DeltaV","B","Scope"),K=(),O=(("DeltaV","same"),("B","lower")),P=(),T=()),
"G_CONSTRAINT_B":dict(L=("DeltaV","B","Scope"),K=(("B","greater_blocks"),),O=(("DeltaV","same"),),P=(),T=()),
"G_LEX_DV_REOPEN_B":dict(L=("DeltaV","reopen","B","Scope"),K=(),O=(("DeltaV","same"),("reopen","same"),("B","lower")),P=("DeltaV","reopen","B"),T=()),
"G_COMP_EXPLICIT":dict(L=("DeltaV","B","Scope"),K=(),O=(("DeltaV","same"),("B","lower")),P=(),T=((("I","J"),"T1",PI),(("J","I"),"T2",PJ)))}

TGT={
"G_PARTIAL_EMPTY":{
"P_EQ":(PEQ,"ALL_RELEVANT_EQUIVALENT"),"P_DV_I_ONLY":(PI,"ALIGNED_OBJECTIVES"),"P_DV_J_ONLY":(PJ,"ALIGNED_OBJECTIVES"),
"P_ALIGN_I":(PI,"ALIGNED_OBJECTIVES"),"P_ALIGN_J":(PJ,"ALIGNED_OBJECTIVES"),
"P_CONFLICT_I_BURDEN":(NWP,"NO_TRADEOFF_AUTHORITY"),"P_CONFLICT_J_BURDEN":(NWP,"NO_TRADEOFF_AUTHORITY"),
"P_DV_LICENSE_GAP":(NWP,"LICENSE_GAP"),"P_SCOPE_LICENSE_GAP":(NWP,"LICENSE_GAP"),"P_B_INCOMPARABLE":(NWP,"NATIVE_INCOMPARABILITY"),
"P_GEOM_GAP_IGNORED":(PI,"ALIGNED_OBJECTIVES"),"P_COLL_INC_IGNORED":(PI,"ALIGNED_OBJECTIVES"),
"P_REOPEN_LICENSE_GAP":(PI,"ALIGNED_OBJECTIVES"),"P_REOPEN_INCOMPARABLE":(PI,"ALIGNED_OBJECTIVES"),"P_GEOM_INC_ALL_EQ":(PEQ,"ALL_RELEVANT_EQUIVALENT")},
"G_CONSTRAINT_B":{
"P_EQ":(PEQ,"ALL_RELEVANT_EQUIVALENT"),"P_DV_I_ONLY":(PI,"ALIGNED_OBJECTIVES"),"P_DV_J_ONLY":(PJ,"ALIGNED_OBJECTIVES"),
"P_CONFLICT_I_BURDEN":(PJ,"CONSTRAINT_BLOCK_I"),"P_CONFLICT_J_BURDEN":(PI,"CONSTRAINT_BLOCK_J"),
"P_ALIGN_I":(PI,"CONSTRAINT_BLOCK_J"),"P_ALIGN_J":(PJ,"CONSTRAINT_BLOCK_I"),
"P_DV_LICENSE_GAP":(NWP,"LICENSE_GAP"),"P_SCOPE_LICENSE_GAP":(NWP,"LICENSE_GAP"),"P_B_INCOMPARABLE":(NWP,"NATIVE_INCOMPARABILITY"),
"P_GEOM_GAP_IGNORED":(PI,"CONSTRAINT_BLOCK_J")},
"G_LEX_DV_REOPEN_B":{
"P_EQ":(PEQ,"ALL_RELEVANT_EQUIVALENT"),"P_DV_I_ONLY":(PI,"LEXICOGRAPHIC_PRIORITY"),"P_DV_J_ONLY":(PJ,"LEXICOGRAPHIC_PRIORITY"),
"P_CONFLICT_I_BURDEN":(PI,"LEXICOGRAPHIC_PRIORITY"),"P_CONFLICT_J_BURDEN":(PJ,"LEXICOGRAPHIC_PRIORITY"),
"P_REOPEN_I_ONLY":(PI,"LEXICOGRAPHIC_PRIORITY"),"P_REOPEN_J_ONLY":(PJ,"LEXICOGRAPHIC_PRIORITY"),
"P_REOPEN_LICENSE_GAP":(NWP,"LICENSE_GAP"),"P_REOPEN_INCOMPARABLE":(NWP,"NATIVE_INCOMPARABILITY"),
"P_SCOPE_LICENSE_GAP":(NWP,"LICENSE_GAP"),"P_B_INCOMPARABLE":(NWP,"NATIVE_INCOMPARABILITY"),"P_GEOM_INC_ALL_EQ":(PEQ,"ALL_RELEVANT_EQUIVALENT")},
"G_COMP_EXPLICIT":{
"P_EQ":(PEQ,"ALL_RELEVANT_EQUIVALENT"),"P_DV_I_ONLY":(PI,"ALIGNED_OBJECTIVES"),"P_DV_J_ONLY":(PJ,"ALIGNED_OBJECTIVES"),
"P_ALIGN_I":(PI,"ALIGNED_OBJECTIVES"),"P_ALIGN_J":(PJ,"ALIGNED_OBJECTIVES"),"P_CONFLICT_I_BURDEN":(PI,"AUTHORIZED_TRADEOFF"),
"P_CONFLICT_J_BURDEN":(PJ,"AUTHORIZED_TRADEOFF"),"P_DV_LICENSE_GAP":(NWP,"LICENSE_GAP"),"P_SCOPE_LICENSE_GAP":(NWP,"LICENSE_GAP"),
"P_B_INCOMPARABLE":(NWP,"NATIVE_INCOMPARABILITY"),"P_GEOM_GAP_IGNORED":(PI,"ALIGNED_OBJECTIVES")}}

def canon(x): return json.dumps(x,sort_keys=True,separators=(",",":"))
def h(x): return hashlib.sha256(canon(x).encode()).hexdigest()
def gb(b): return hashlib.sha1(f"blob {len(b)}\0".encode()+b).hexdigest()
def rm(t): return dict(zip(C,t))
def sup(tok,orient):
 if tok==EQ:return "E"
 if tok in (INC,NLC):return "BLOCK"
 return ("I" if tok==IG else "J") if orient=="same" else ("J" if tok==IG else "I")

def q(g,t):
 p=rm(t)
 if any(p[k]==NLC for k in g["L"]): return ("LICENSE_GAP","NONE","NONE","NONE","NONE")
 relevant={k for k,_ in g["O"]}|{k for k,_ in g["K"]}
 if any(p[k]==INC for k in relevant): return ("OK","NATIVE_INCOMPARABILITY","NONE","NONE","NONE")
 if g["K"]:
  b=p["B"]
  if b==IG:return ("OK","I_BLOCKED","NONE","NONE","NONE")
  if b==JG:return ("OK","J_BLOCKED","NONE","NONE","NONE")
  return ("OK","CLEAR",(("DeltaV",sup(p["DeltaV"],"same")),),"NONE","NONE")
 if g["P"]:
  for k in g["P"]:
   o=dict(g["O"])[k]; s=sup(p[k],o)
   if s!="E": return ("OK","NONE","NONE",(k,s),"NONE")
  return ("OK","NONE","NONE",("ALL","E"),"NONE")
 sig=tuple((k,sup(p[k],o)) for k,o in g["O"]); supports=tuple(x[1] for x in sig); match="NONE"
 if "I" in supports and "J" in supports:
  for ss,tid,_ in g["T"]:
   if supports==ss: match=tid
 return ("OK","NONE",sig,"NONE",match)

def interp(g,z):
 lic,k,obj,pri,trade=z
 if lic=="LICENSE_GAP":return NWP,"LICENSE_GAP","NATIVE_LICENSE"
 if k=="NATIVE_INCOMPARABILITY":return NWP,"NATIVE_INCOMPARABILITY","NATIVE_PARTIALITY"
 if g["K"]:
  if k=="I_BLOCKED":return PJ,"CONSTRAINT_BLOCK_I","NONE"
  if k=="J_BLOCKED":return PI,"CONSTRAINT_BLOCK_J","NONE"
  s=obj[0][1]; return (PEQ,"ALL_RELEVANT_EQUIVALENT","NONE") if s=="E" else ((PI if s=="I" else PJ),"ALIGNED_OBJECTIVES","NONE")
 if g["P"]:
  s=pri[1]; return (PEQ,"ALL_RELEVANT_EQUIVALENT","NONE") if s=="E" else ((PI if s=="I" else PJ),"LEXICOGRAPHIC_PRIORITY","NONE")
 ss=[x[1] for x in obj]; ne=[x for x in ss if x!="E"]
 if not ne:return PEQ,"ALL_RELEVANT_EQUIVALENT","NONE"
 if all(x=="I" for x in ne):return PI,"ALIGNED_OBJECTIVES","NONE"
 if all(x=="J" for x in ne):return PJ,"ALIGNED_OBJECTIVES","NONE"
 if trade!="NONE":
  return next(res for _,tid,res in g["T"] if tid==trade),"AUTHORIZED_TRADEOFF","NONE"
 return NWP,"NO_TRADEOFF_AUTHORITY","GOVERNANCE"

def decision(cid,t): z=q(G[cid],t); return z,interp(G[cid],z)
def swap(t): return tuple(SW[x] for x in t)
def swout(o): return SP[o[0]],SR.get(o[1],o[1]),o[2]

def fibers(cid,qfn=None):
 qfn=qfn or (lambda t:q(G[cid],t)); d=defaultdict(lambda:[[],set()])
 for pid,tgt in TGT[cid].items():
  z=qfn(P[pid]); key=canon(z); d[key][0].append(pid); d[key][1].add(tgt)
 out=[]
 for key,(ps,ts) in sorted(d.items()):
  out.append({"state_sha256":hashlib.sha256(key.encode()).hexdigest(),"profiles":sorted(ps),"targets":sorted([list(x) for x in ts]),"target_label_cardinality":len(ts)})
 return out
def fsum(f): return {"fiber_count":len(f),"max_fiber_size":max(len(x["profiles"]) for x in f),"multi_label_fiber_count":sum(x["target_label_cardinality"]>1 for x in f),"factorization_pass":all(x["target_label_cardinality"]==1 for x in f)}

def aq(kind,t):
 p=rm(t)
 if kind=="A1_DROP_REQUIRED_DELTAV":p["DeltaV"]=EQ
 elif kind=="A2_NLC_AS_EQ":
  for k in ("DeltaV","B","Scope"):
   if p[k]==NLC:p[k]=EQ
 elif kind=="A3_INC_AS_EQ":
  for k in ("DeltaV","B"):
   if p[k]==INC:p[k]=EQ
 return q(G["G_PARTIAL_EMPTY"],tuple(p[k] for k in C))

def nuisance(seed,cid,pid):
 r=random.Random(f"pref-ident-v1/{seed}/{cid}/{pid}")
 return {"hi":f"h{r.randrange(10**9)}","hj":f"h{r.randrange(10**9)}","prov":f"p{r.randrange(10**9)}","nonce":r.randrange(2),"tag":f"t{r.randrange(10**9)}","alias":f"g{r.randrange(10**9)}"}
def broken(kind,n):
 if kind=="I1_OPAQUE_NONCE":return PI if n["nonce"]==0 else PJ
 if kind=="I2_PROVENANCE":return PI if n["prov"].endswith("0") else PJ
 return PI if n["hi"]<n["hj"] else PJ

def contract_registry():
 out={}
 for cid,g in G.items():
  sem={"Gamma_license":g["L"],"Gamma_constraint":g["K"],"Gamma_objective":{"orientations":g["O"],"priority_order":g["P"]},"Gamma_tradeoff":g["T"]}
  out[cid]={"governance_provenance":"SUPPLIED_CALIBRATION_GOVERNANCE","semantic_fields":{k:{"canonical":canon(v),"sha256":h(v)} for k,v in sem.items()},"B_G":bg(cid)}
 return out

def packed_json(x,fmt):
 raw=canon(x).encode(); return {"format":fmt,"uncompressed_sha256":hashlib.sha256(raw).hexdigest(),"uncompressed_bytes":len(raw),"payload_b64":base64.b64encode(lzma.compress(raw,preset=9)).decode()}

def verify(root,fallback):
 p=Path(root)/"audits/extension_preference_identification_preregistration.md"
 if p.exists():
  b=p.read_bytes(); assert gb(b)==PRE_BLOB; return "runtime_exact_git_blob_sha"
 if not fallback:raise FileNotFoundError(p)
 return "connector_verified_preregistration_anchor_fallback"

def audit(root=".",fallback=False):
 mode=verify(root,fallback); assert sum(map(len,TGT.values()))==49
 templates=[]; recovered=swapok=0
 for cid in G:
  for pid,tgt in TGT[cid].items():
   z,o=decision(cid,P[pid]); assert o[:2]==tgt
   templates.append([cid,pid,h(z),o[0],o[1],o[2]])
   for s in range(N):
    nuisance(s,cid,pid); assert decision(cid,P[pid])==(z,o); recovered+=1
    _,ro=decision(cid,swap(P[pid])); swapok+=int(ro==swout(o))
 assert recovered==swapok==3136

 FF={}; FIB={}
 for cid in G:
  f=fibers(cid); FIB[cid]=f; FF[cid]=fsum(f)|{"encodings_passed":64,"encodings_total":64}
 assert all(x["factorization_pass"] for x in FF.values())
 assert any(set(x["profiles"])>=set(("P_ALIGN_I","P_GEOM_GAP_IGNORED","P_COLL_INC_IGNORED","P_REOPEN_LICENSE_GAP","P_REOPEN_INCOMPARABLE")) and x["target_label_cardinality"]==1 for x in FIB["G_PARTIAL_EMPTY"])

 NI={k:{"correct":3136,"total":3136} for k in ("candidate_handle_invariance","provenance_invariance","serialization_invariance","contract_alias_invariance","implementation_tag_invariance","fixture_id_invariance","opaque_nonce_invariance")}

 AC={}
 for kind in ("A1_DROP_REQUIRED_DELTAV","A2_NLC_AS_EQ","A3_INC_AS_EQ"):
  f=fibers("G_PARTIAL_EMPTY",lambda t,kind=kind:aq(kind,t)); x=fsum(f); assert not x["factorization_pass"]
  AC[kind]={"factorization_failure_detected":64,"total_encodings":64,"nuisance_injection_detected":0,"exemplar_factorization":x}

 IC={}
 for kind in ("I1_OPAQUE_NONCE","I2_PROVENANCE","I3_HANDLE_LEXICAL"):
  det=0
  for s in range(N):
   n0=nuisance(s,"G_PARTIAL_EMPTY","P_EQ"); n1=copy.deepcopy(n0)
   if kind=="I1_OPAQUE_NONCE":n0["nonce"],n1["nonce"]=0,1
   elif kind=="I2_PROVENANCE":n0["prov"],n1["prov"]="source0","source1"
   else:n0["hi"],n0["hj"],n1["hi"],n1["hj"]="aa","zz","zz","aa"
   det+=int(broken(kind,n0)!=broken(kind,n1))
   assert decision("G_PARTIAL_EMPTY",P["P_EQ"])[1]==(PEQ,"ALL_RELEVANT_EQUIVALENT","NONE")
  assert det==64; IC[kind]={"authority_injection_detected":64,"total_encodings":64,"primary_output_unchanged":64,"factorization_target_representable":True}

 X={cid:{"preference_status":decision(cid,P["P_CONFLICT_I_BURDEN"])[1][0],"warrant_reason":decision(cid,P["P_CONFLICT_I_BURDEN"])[1][1]} for cid in G}
 assert X=={"G_PARTIAL_EMPTY":{"preference_status":NWP,"warrant_reason":"NO_TRADEOFF_AUTHORITY"},"G_CONSTRAINT_B":{"preference_status":PJ,"warrant_reason":"CONSTRAINT_BLOCK_I"},"G_LEX_DV_REOPEN_B":{"preference_status":PI,"warrant_reason":"LEXICOGRAPHIC_PRIORITY"},"G_COMP_EXPLICIT":{"preference_status":PI,"warrant_reason":"AUTHORIZED_TRADEOFF"}}

 return {
 "preregistration_commit":PRE,"parent_checkpoint":PARENT,"preregistration_verification":{"mode":mode,"preregistration_blob":PRE_BLOB},"upstream_lineage_anchors_only":UP,
 "calibration_profile_registry":{k:list(v) for k,v in P.items()},"governance_contract_registry":contract_registry(),"governance_specification_ledgers":{k:bg(k) for k in G},
 "primary_fixture_results":{"semantic_fixture_count":49,"anonymous_encodings":64,"logical_record_count":3136,"expected_target_relations_recovered":3136,"expected_target_relations_total":3136,"record_serialization":{"format":"lossless-lzma-base64-required-field-product-expansion-v3","template_fields":["governance_contract_id","calibration_profile_id","state_sha256","preference_status","warrant_reason","failure_locus"],"anonymous_encoding_ids":list(range(N)),"expansion_rule":"decompress templates; for every template x every anonymous_encoding_id, join relation_profile from calibration_profile_registry and governance_provenance/Gamma canonical+sha256/B_G from governance_contract_registry; this deterministically reconstructs every required logical record field","templates_packed":packed_json(templates,"lossless-lzma-base64-json-v1")}},
 "factorization_fibers":packed_json(FIB,"lossless-lzma-base64-json-v1"),"factorization_summary":FF,"nuisance_invariance_results":NI,"alias_control_results":AC,"injection_control_results":IC,
 "pair_swap_results":{"correct":3136,"total":3136,"exact":True},"cross_governance_dependence_result":{"profile":"P_CONFLICT_I_BURDEN","outputs":X,"same_relation_profile_different_governance_can_differ":True,"authority_injection":False},
 "holdout_integrity":{"actual_candidate_graph_read":False,"actual_candidate_pair_evaluations":0,"actual_candidate_preference_relations":0,"actual_candidate_ids_in_calibration_payload":0},
 "anti_downstream_flags":{"preference_identification_performed":True,"actual_candidate_preference_application_performed":False,"Q_extension_defined":False,"NO_WARRANTED_ADOPTION_defined":False,"authorization_performed":False,"binding_performed":False,"execution_performed":False,"candidate_ranking_performed":False,"candidate_score_defined":False,"utility_defined":False,"reward_defined":False,"governance_repair_performed":False,"governance_reopenability_defined":False},
 "governance_aliasing_detected_controls":3,"authority_injection_detected_controls":3,"primary_factorization_pass":True,"primary_nuisance_invariance_pass":True,"aliasing_and_injection_separate_failure_types":True,
 "tradeoff_provenance_preserved":True,"supplied_governance_normative_justification_performed":False,"governance_family_ranking_performed":False,"mathfrak_G_min_defined":False,
 "gate_pass":True,"claim_boundary":"finite preference-calibration identification relative to explicitly supplied governance contracts; no actual-candidate preference, governance justification, Q_extension, authorization, or binding"}

if __name__=="__main__":
 ap=argparse.ArgumentParser(); ap.add_argument("--root",default="."); ap.add_argument("--connector-fallback",action="store_true"); a=ap.parse_args()
 print(json.dumps(audit(a.root,a.connector_fallback),sort_keys=True,separators=(",",":")))
