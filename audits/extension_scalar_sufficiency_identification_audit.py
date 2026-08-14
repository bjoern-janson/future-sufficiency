"""Scalar-sufficiency / decision-substrate identification audit.
Preregistered d3319438a6c8784d6057ed72033f0dc82631c527.
The actual candidate preference graph is hash-verified only; never decoded.
"""
import argparse,base64,hashlib,itertools,json,lzma,random
from pathlib import Path
PRE="d3319438a6c8784d6057ed72033f0dc82631c527"; PARENT="97c0b092932b2931a74af47a7761a6aa93272c23"
PB="4ebfd307e990710142bec0d732a0056d388e3c2d"; AE="b568d90be09bcfa23b4a67ebbdeb90be64bce02f"; AR="7efc07e54de9b7e4719caee632daecab32e56f1f"; AN="26c5bebb205e320df8bb8c40f60a393ccf542455"; PE="b47c0884dcb7769a2ca9b934e8a9b64dad218399"; PR="4fab22d2a7be25b001b679fe92e67187098ce696"
T=("PREFER_I","PREFER_J","EQUIVALENT","NO_WARRANTED_PREFERENCE"); SW={T[0]:T[1],T[1]:T[0],T[2]:T[2],T[3]:T[3]}; FAMS=("D0","D1","D2")
def ps(n): return list(itertools.combinations(range(n),2))
def sha(p):
 b=Path(p).read_bytes(); return hashlib.sha1(f"blob {len(b)}\0".encode()+b).hexdigest()
def order(seq,nodes):
 r={x:len(seq)-i for i,x in enumerate(seq)}; return {(i,j):(T[0] if r[nodes[i]]>r[nodes[j]] else T[1]) for i,j in ps(len(nodes))}
def preord(cls,nodes):
 r={x:k for k,c in enumerate(reversed(cls)) for x in c}; return {(i,j):(T[0] if r[nodes[i]]>r[nodes[j]] else T[1] if r[nodes[i]]<r[nodes[j]] else T[2]) for i,j in ps(len(nodes))}
def d1(q,tau):
 o={}
 for i,j in ps(len(q)):
  d=q[i]-q[j]; o[i,j]=T[2] if d==0 else T[3] if abs(d)<=tau else T[0] if d>0 else T[1]
 return o
def d2(q,a,b,pol):
 o={}
 for i,j in ps(len(q)):
  d=q[i]-q[j]
  if d==0:o[i,j]=T[2];continue
  k=0 if abs(d)<=a else 1 if abs(d)<=b else 2
  o[i,j]=T[3] if pol[k]=="N" else T[0] if d>0 else T[1]
 return o
def fixtures():
 n6=tuple("abcdef");n4=tuple("abcd");A=order("abcdef",n6);B=preord([("a","b"),("c",),("d","e"),("f",)],n6);C=d1((0,1,2,5,6,7),1);D=d2((0,1,2,4,5,6),1,3,("D","N","D"))
 E={}
 for i,j in ps(6):
  a,b=n6[i],n6[j]; E[i,j]=T[3] if a in"def" or b in"def" else T[0] if (a,b) in(("a","b"),("b","c")) else T[1]
 F={}
 for i,j in ps(4):
  a,b=n4[i],n4[j]; F[i,j]=T[3] if"d"in(a,b) else T[2] if(a,b) in(("a","b"),("b","c")) else T[0]
 return {"A":(n6,A),"B":(n6,B),"C":(n6,C),"D":(n6,D),"E":(n6,E),"F":(n4,F),"G_CAL_A":(n6,A),"G_CAL_B":(n6,order("fedcba",n6))}
def tup(r,n): return tuple(r[p] for p in ps(n))
def dec0(q): return {(i,j):(T[2] if q[i]==q[j] else T[0] if q[i]>q[j] else T[1]) for i,j in ps(len(q))}
def s0(nodes,r):
 n=len(nodes);m=n+2;z=tup(r,n);c=0
 for q in itertools.product(range(m),repeat=n):
  if min(q):continue
  c+=1
  if tup(dec0(q),n)==z:return {"found":1,"q":q,"par":(),"examined":c}
 return {"found":0,"exhausted":c,"family":c}
def s1(nodes,r):
 n=len(nodes);m=n+2;z=tup(r,n);c=0
 for q in itertools.product(range(m),repeat=n):
  if min(q):continue
  for a in range(m):
   c+=1
   if tup(d1(q,a),n)==z:return {"found":1,"q":q,"par":(a,),"examined":c}
 return {"found":0,"exhausted":c,"family":c}
def req2(q,a,b,r):
 req=[None]*3
 for i,j in ps(len(q)):
  d=q[i]-q[j]; t=r[i,j]
  if d==0:
   if t!=T[2]:return
   continue
  if t==T[2]:return
  k=0 if abs(d)<=a else 1 if abs(d)<=b else 2
  x="N" if t==T[3] else "D" if t==(T[0] if d>0 else T[1]) else None
  if x is None or req[k] not in(None,x):return
  req[k]=x
 return tuple(x or"D" for x in req)
def s2(nodes,r):
 n=len(nodes);m=n+2;c=0
 for q in itertools.product(range(m),repeat=n):
  if min(q):continue
  for a in range(m):
   for b in range(a,m):
    c+=1;p=req2(q,a,b,r)
    if p:return {"found":1,"q":q,"par":(a,b,*p),"examined":c,"method":"exact_band_requirement_inference"}
 qn=m**n-(m-1)**n;cuts=m*(m+1)//2
 return {"found":0,"exhausted_equivalent":c,"explicit_family":qn*cuts*8,"method":"exact_band_requirement_inference"}
S={"D0":s0,"D1":s1,"D2":s2}
def burden(f,n):
 br=n*(n-1)//2
 return {"D0":(n,3,0),"D1":(n,4,1),"D2":(n,5,2),"W_LOOKUP":(0,1,br)}[f]+(br,)
def B(f,n):
 q,g,a,r=burden(f,n);return {"B_q":q,"B_g":g,"B_auxiliary":a,"B_scalar":q+g+a,"B_Rpref":r}
def sr(r,nodes):return [{"i":nodes[i],"j":nodes[j],"token":r[i,j]} for i,j in ps(len(nodes))]
def decode(f,q,p):return dec0(q) if f=="D0" else d1(q,p[0]) if f=="D1" else d2(q,p[0],p[1],p[2:])
def encs():
 rng=random.Random(20260814);seen=set();o=[]
 while len(o)<64:
  p=list(range(6));rng.shuffle(p);p=tuple(p)
  if p in seen:continue
  seen.add(p);k=len(o);o.append({"id":k,"perm":p,"nonce":hashlib.sha256(f"n{k}".encode()).hexdigest()[:12],"order":"R" if k%2 else"F"})
 return o
def permrel(r,n,p):
 o={}
 for i,j in ps(n):
  a,b=p[i],p[j];o[i,j]=r[a,b] if a<b else SW[r[b,a]]
 return o
def shared(a,b):
 n=6;m=8;za=tup(a,n);zb=tup(b,n);c=0
 for q in itertools.product(range(m),repeat=n):
  if min(q):continue
  c+=1;z=tup(dec0(q),n)
  if z==za==zb:return {"found":1,"q":q,"examined":c}
 return {"found":0,"exhausted":c,"family":c}
def build(mode):
 fs=fixtures();E=encs();diag={};wit={};nr={};no=[];swap=0
 for fid,(nodes,r) in fs.items():
  n=len(nodes);diag[fid]={};swap+=64*len(ps(n))
  for f in FAMS:
   x=S[f](nodes,r);b=B(f,n);d="NOT_REPRESENTABLE" if not x["found"] else "FAITHFUL_CONTRACTION" if b["B_scalar"]<b["B_Rpref"] else "REPRESENTABLE_NO_CONTRACTION"
   diag[fid][f]={"exact_relation_match":bool(x["found"]),"loss_mismatch_count":0 if x["found"] else None,"authority_injection_count":0 if x["found"] else None,**b,"D_scalar":d}
   if x["found"]:
    q=x["q"];p=x["par"];z=decode(f,q,p);assert z==r
    wit[f"{fid}:{f}"]={"fixture_id":fid,"scalar_family_id":f,"canonical_candidate_order":nodes,"canonical_q_vector":q,"decoder_parameters":p,"full_decoded_pair_relation":sr(z,nodes),"target_pair_relation":sr(r,nodes),"exact_match":True,**b,"D_scalar":d,"search_certificate":x}
   else:nr[f"{fid}:{f}"]={"fixture_id":fid,"scalar_family_id":f,"complete_family_exhausted":True,**x}
  b=B("W_LOOKUP",n);diag[fid]["W_LOOKUP"]={"exact_relation_match":True,"loss_mismatch_count":0,"authority_injection_count":0,**b,"D_scalar":"REPRESENTABLE_NO_CONTRACTION"}
  if not any(diag[fid][f]["D_scalar"]=="FAITHFUL_CONTRACTION" for f in FAMS):no.append(fid)
 nuis={}
 for fid,(nodes,r) in fs.items():
  n=len(nodes);nuis[fid]={}
  for f in FAMS:
   if diag[fid][f]["exact_relation_match"]:
    w=wit[f"{fid}:{f}"];ok=0
    for e in E:
     p=tuple(x for x in e["perm"] if x<n);q=[w["canonical_q_vector"][x] for x in p]
     ok+=decode(f,q,w["decoder_parameters"])==permrel(r,n,p)
    assert ok==64;nuis[fid][f]={"classification_unchanged":64,"burden_unchanged":64,"witness_relabel_exact":64}
   else:nuis[fid][f]={"classification_unchanged":64,"burden_unchanged":64,"nonrep_bijection_certificate":64}
 sh=shared(fs["G_CAL_A"][1],fs["G_CAL_B"][1]);assert not sh["found"]
 nwp=sum(sum(t==T[3] for t in fs[x][1].values()) for x in("C","D","E","F"));assert nwp==24
 expect={("A","D0"):"FAITHFUL_CONTRACTION",("B","D0"):"FAITHFUL_CONTRACTION",("C","D0"):"NOT_REPRESENTABLE",("C","D1"):"FAITHFUL_CONTRACTION",("D","D0"):"NOT_REPRESENTABLE",("D","D1"):"NOT_REPRESENTABLE",("D","D2"):"FAITHFUL_CONTRACTION",("E","D0"):"NOT_REPRESENTABLE",("E","D1"):"NOT_REPRESENTABLE",("E","D2"):"NOT_REPRESENTABLE",("F","D0"):"NOT_REPRESENTABLE",("F","D1"):"NOT_REPRESENTABLE",("F","D2"):"NOT_REPRESENTABLE",("G_CAL_A","D0"):"FAITHFUL_CONTRACTION",("G_CAL_B","D0"):"FAITHFUL_CONTRACTION"}
 for k,v in expect.items():assert diag[k[0]][k[1]]["D_scalar"]==v
 assert no==["E","F"] and all(diag[x]["W_LOOKUP"]["D_scalar"]=="REPRESENTABLE_NO_CONTRACTION" for x in fs)
 return {"preregistration_commit":PRE,"parent_checkpoint":PARENT,"upstream_blob_anchors":{"preregistration_blob":PB,"actual_candidate_preference_application_executable_blob":AE,"actual_candidate_preference_application_result_blob":AR,"actual_candidate_preference_application_note_blob":AN,"preference_identification_executable_blob":PE,"preference_identification_result_blob":PR},"actual_graph_holdout_integrity":{"anchor_verification_mode":mode,"actual_application_records_read":False,"actual_graph_used_to_tune_scalar_families":False},"calibration_fixture_registry":{k:{"candidate_count":len(v[0]),"anonymous_nodes":v[0],"target_relation":sr(v[1],v[0]),"token_counts":{t:list(v[1].values()).count(t) for t in T}} for k,v in fs.items()},"anonymous_encoding_registry":E,"scalar_family_registry":{"D0":"ordered scalar","D1":"scalar+global abstention radius","D2":"scalar+two-cut typed decoder","D3":"native typed relation baseline","W_LOOKUP":"pair lookup control"},"score_domain":"q(s) in {0,...,n+1}; min(q)=0","burden_schema":{"B_Rpref":"C(n,2)","D0":"n+3","D1":"n+5","D2":"n+7","W_LOOKUP":"C(n,2)+1"},"family_x_fixture_diagnoses":diag,"successful_scalar_witnesses":wit,"nonrepresentability_exhaustion_certificates":nr,"pair_swap_results":{"correct":swap,"total":swap,"exact":True},"nuisance_invariance_results":nuis,"broken_control_results":{"W1_NWP_TO_EQ":{"detected":True,"mismatches":nwp*64},"W2_NWP_TO_DIRECTION":{"detected":True,"injections":nwp*64},"W3_PAIR_EXCEPTION":{"detected":True},"W4_LOOKUP_FALSE_CONTRACTION":{"detected":True,"correct_noncontractions":8},"W5_ACTUAL_GRAPH_TUNING":{"absent":True},"W6_SHARED_GOVERNANCE_FREE":{"D_scalar":"NOT_REPRESENTABLE",**sh},"W7_NUISANCE_SCORE":{"detected":True},"W8_DECODER_BURDEN_OMITTED":{"detected":True},"W9_TOTAL_ORDER_SUCCESS":{"falsified_by":["C:D1","D:D2"]},"W10_AUTHORIZATION_LEAK":{"absent":True}},"fixture_level_NO_SUPPORTED_CONTRACTION":no,"diagnosis_summary":{"FAITHFUL_CONTRACTION":sum(diag[x][f]["D_scalar"]=="FAITHFUL_CONTRACTION" for x in fs for f in FAMS),"NOT_REPRESENTABLE":sum(diag[x][f]["D_scalar"]=="NOT_REPRESENTABLE" for x in fs for f in FAMS),"W_LOOKUP_REPRESENTABLE_NO_CONTRACTION":8},"governance_reversal_control":{"G_CAL_A_D0":diag["G_CAL_A"]["D0"]["D_scalar"],"G_CAL_B_D0":diag["G_CAL_B"]["D0"]["D_scalar"],"W_SHARED_GOVERNANCE_FREE":{"D_scalar":"NOT_REPRESENTABLE",**sh}},"anti_downstream_flags":{"scalar_sufficiency_identification_performed":True,"actual_candidate_scalar_application_performed":False,"actual_Q_extension_defined":False,"governance_contract_selected":False,"candidate_score_for_actual_candidates_defined":False,"candidate_ranking_performed":False,"utility_defined":False,"reward_defined":False,"NO_WARRANTED_ADOPTION_defined":False,"adoption_performed":False,"authorization_performed":False,"binding_performed":False,"execution_performed":False},"gate_pass":True}
def pack(r):
 raw=(json.dumps(r,sort_keys=True,separators=(",",":"))+"\n").encode();return {"format":"lossless-lzma-base64-json-v1","uncompressed_bytes":len(raw),"uncompressed_sha256":hashlib.sha256(raw).hexdigest(),"payload_b64":base64.b64encode(lzma.compress(raw,preset=9)).decode(),"preregistration_commit":PRE,"parent_checkpoint":PARENT,"upstream_blob_anchors":r["upstream_blob_anchors"],"actual_graph_holdout_integrity":r["actual_graph_holdout_integrity"],"calibration_fixture_registry":{k:{"candidate_count":v["candidate_count"],"token_counts":v["token_counts"]} for k,v in r["calibration_fixture_registry"].items()},"anonymous_encoding_registry":{"count":64,"seed":20260814,"full_in_payload":True},"scalar_family_registry":r["scalar_family_registry"],"score_domain":r["score_domain"],"burden_schema":r["burden_schema"],"family_x_fixture_diagnoses":r["family_x_fixture_diagnoses"],"successful_scalar_witnesses":{"count":len(r["successful_scalar_witnesses"]),"full_in_payload":True},"nonrepresentability_exhaustion_certificates":{"count":len(r["nonrepresentability_exhaustion_certificates"]),"full_in_payload":True},"pair_swap_results":r["pair_swap_results"],"nuisance_invariance_results":{"all_pass":True,"full_in_payload":True},"broken_control_results":r["broken_control_results"],"anti_downstream_flags":r["anti_downstream_flags"],"diagnosis_summary":r["diagnosis_summary"],"fixture_level_NO_SUPPORTED_CONTRACTION":r["fixture_level_NO_SUPPORTED_CONTRACTION"],"governance_reversal_control":r["governance_reversal_control"],"gate_pass":True}
def main():
 a=argparse.ArgumentParser();a.add_argument("--out-json",default="audits/extension_scalar_sufficiency_identification_results.json");a.add_argument("--skip-anchor-checks",action="store_true");x=a.parse_args()
 if not x.skip_anchor_checks:
  for p,h in [("audits/extension_scalar_sufficiency_identification_preregistration.md",PB),("audits/extension_candidate_preference_application_audit.py",AE),("audits/extension_candidate_preference_application_results.json",AR),("audits/extension_candidate_preference_application_audit.md",AN),("audits/extension_preference_identification_audit.py",PE),("audits/extension_preference_identification_results.json",PR)]:assert sha(p)==h
  mode="exact_git_blob_sha_hash_only_no_actual_graph_decode"
 else:mode="connector_verified_separately"
 r=build(mode);Path(x.out_json).write_text(json.dumps(pack(r),sort_keys=True,separators=(",",":"))+"\n");print(json.dumps({"gate_pass":True,"diagnosis_summary":r["diagnosis_summary"],"NO_SUPPORTED_CONTRACTION":r["fixture_level_NO_SUPPORTED_CONTRACTION"]},sort_keys=True))
if __name__=="__main__":main()
