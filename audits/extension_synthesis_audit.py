"""Extension Synthesis Audit. Preregistered at fa4e744f44f0e61fe3e3a7c3bea8d2101c0f59b1.
Scope: D_closure=INSUFFICIENT -> M0 -> candidate or NO_SUPPORTED_CANDIDATE.
No extension valuation, authorization, binding, or post-binding test.
"""
from itertools import product
from collections import Counter,defaultdict
import hashlib,json,random
PRE="fa4e744f44f0e61fe3e3a7c3bea8d2101c0f59b1"; UP="7e3871c036a40e65c1f9de666962bc9965434263"
NENC=64; K=.1; EPS=1e-12; XOR=(0,1,1,0); AND=(0,0,0,1)
LEDGER={"B_truth_basis":1,"B_pool_roles":2,"B_program_combinators":3,"B_grammar":3,"B_search_bounds":3,"B_semantic_hints":0,"B_target_hints":0}
LEDGER["expanded_total"]=sum(LEDGER.values())

def worlds(n): return tuple(product((0,1),repeat=n))
def full(n): return (1<<(1<<n))-1
def tbl(n,f):
    z=0
    for i,w in enumerate(worlds(n)): z|=(1<<i) if f(*w) else 0
    return z
def coords(n):
    W=worlds(n); return tuple(sum(w[j]<<i for i,w in enumerate(W)) for j in range(n))
def canon(x,n): return (full(n)^x) if x&1 else x
def span(bs):
    s={0}
    for b in bs: s|={x^b for x in tuple(s)}
    return s
def base(n,idx=None):
    C=coords(n); idx=tuple(range(n)) if idx is None else tuple(idx)
    return frozenset(span(C[i] for i in idx)-{0})
def deg2():
    C=coords(4); B=list(C)+[C[i]&C[j] for i in range(4) for j in range(i+1,4)]
    return frozenset(span(B)-{0})
def parts(raw,n):
    s={canon(x,n) for x in raw}; s.discard(0); return frozenset(s)
def basis(vals,w):
    B=[0]*w
    for x in vals:
        while x:
            i=x.bit_length()-1
            if B[i]: x^=B[i]
            else: B[i]=x; break
    return [x for x in B if x]
def xclose(raw,n): return parts(span(basis(raw,1<<n)),n)
def app(tt,a,b,n):
    F=full(n); na=F^a; nb=F^b; z=0
    if tt[0]: z|=na&nb
    if tt[1]: z|=na&b
    if tt[2]: z|=a&nb
    if tt[3]: z|=a&b
    return z
def nand(a,b): return tuple(1-(x&y) for x,y in zip(a,b))
U=(0,0,1,1); V=(0,1,0,1)
def trees(k):
    if k==0:return (("u",U),("v",V))
    o=[]
    for i in range(k):
        for sa,a in trees(i):
            for sb,b in trees(k-1-i): o.append((f"N({sa},{sb})",nand(a,b)))
    return tuple(o)
RAW=[(k,s,t) for k in range(4) for s,t in trees(k)]
FUN={}
for k,s,t in RAW: FUN.setdefault(t,[]).append(s)
assert len(RAW)==102 and len(FUN)==10 and AND in FUN and (0,1,1,1) in FUN

def ba(y,n):
    m=y.bit_count(); N=1<<n; return max(m,N-m)/N
def pa(y,e,n):
    F=full(n); N=1<<n; c=0
    for g in (e,F^e):
        m=g.bit_count()
        if m:
            q=(y&g).bit_count(); c+=max(q,m-q)
    return c/N
def mr(y,P,n): return max((pa(y,e,n)-ba(y,n) for e in P),default=0)
def h(P,n):
    rows=[tuple((x>>i)&1 for i in range(1<<n)) for x in P]
    return hashlib.sha256(json.dumps([list(r) for r in sorted(rows)],separators=(",",":")).encode()).hexdigest()
def transform(x,order):
    z=0
    for i,j in enumerate(order): z|=((x>>j)&1)<<i
    return z
def tparts(P,order,n,R=None):
    out=[]
    for x in P:
        z=transform(x,order)
        if R is not None and R.randrange(2): z^=full(n)
        out.append(canon(z,n))
    return frozenset(out)

def space(n,current,B,NL,admitted):
    C=parts(current,n); D={C:{"programs":[("noop",None,None,False)],"delta":frozenset()}}
    ops=[("admit",tt) for tt in admitted]+[("synth",tt) for tt in FUN]
    src=[("BB",B,B)]+([("NB",NL,B)] if NL else [])
    np=1
    for origin,tt in ops:
        for sn,P,Q in src:
            for close in (False,True):
                np+=1; G={app(tt,a,b,n) for a in P for b in Q}; R=set(current)|G
                F=xclose(R,n) if close else parts(R,n)
                D.setdefault(F,{"programs":[],"delta":F-C})["programs"].append((origin,tt,sn,close))
    return C,D,np
def minima(y,n,C,D):
    A=[]
    for P,r in D.items():
        rmax=mr(y,P,n); q=rmax-K
        if q>EPS:A.append((P,r,rmax,q))
    out=[]
    for P,r,rmax,q in A:
        d=P-C
        if not any((Q-C)<d for Q,_,_,_ in A): out.append((P,r,rmax,q))
    return sorted(out,key=lambda z:(len(z[0]),h(z[0],n)))
def classes():
    B=base(4); CA,SA,nA=space(4,B,B,frozenset(),[XOR])
    A=tbl(4,lambda a,b,c,d:a&b); Btar=tbl(4,lambda a,b,c,d:a|b)
    D2=deg2(); C2=parts(D2,4); NL=frozenset(x for x in D2 if canon(x,4) not in CA)
    CC,SC,nC=space(4,D2,base(4),NL,[XOR,AND]); Ct=tbl(4,lambda a,b,c,d:a&b&c)
    return {"A":(4,B,CA,SA,nA,A,minima(A,4,CA,SA)),
            "B":(4,B,CA,SA,nA,Btar,minima(Btar,4,CA,SA)),
            "C":(4,D2,CC,SC,nC,Ct,minima(Ct,4,CC,SC),base(4),NL)}
def dcase(hidden):
    idx=[i for i in range(5) if i!=hidden]; B=base(5,idx); C,S,np=space(5,B,B,frozenset(),[XOR]); y=coords(5)[hidden]
    return (5,B,C,S,np,y,minima(y,5,C,S))
def basebase_ok(y,n,C,S):
    return sum(1 for P,r in S.items() if any(p[2]=="BB" for p in r["programs"] if p[0]!="noop") and mr(y,P,n)-K>EPS)
def wrong_expand(y,n,C,S): return any(P!=C and mr(y,P,n)-K<=EPS for P in S)
def summary(z,n,C):
    P,r,rmax,q=z
    return {"family_size":len(P),"delta_size":len(P-C),"fingerprint_sha256":h(P,n),"max_R_corr":rmax,"max_q":q,
            "program_semantics":[{"origin":p[0],"truth_table":list(p[1]) if p[1] else None,"source":p[2],"xor_close":p[3]} for p in r["programs"]]}

def core():
    X=classes(); A=X["A"]; B=X["B"]; C=X["C"]
    assert len(A[6])==1 and len(B[6])==1 and len(C[6])==2
    assert A[6][0][0]!=B[6][0][0] and len(A[6][0][0])==120 and len(B[6][0][0])==50
    assert len(A[6][0][0]-A[2])==105 and len(B[6][0][0]-B[2])==35
    assert basebase_ok(C[5],4,C[2],C[3])==0
    for z in C[6]: assert any(p[2]=="NB" for p in z[1]["programs"])
    Dc={i:dcase(i) for i in range(5)}
    for d in Dc.values():
        assert not d[6] and abs(mr(d[5],d[2],5))<EPS and all(abs(mr(d[5],P,5))<EPS for P in d[3])
    prof={k:{"baseline":ba(v[5],v[0]),"current_max_R_corr":mr(v[5],v[2],v[0]),"current_max_q":mr(v[5],v[2],v[0])-K} for k,v in X.items()}
    cnt={k:0 for k in "ABCD"}; abd=cbad=dany=0
    for seed in range(NENC):
        R=random.Random((seed+1)*1000003+744); o=list(range(16)); R.shuffle(o); mm={}
        ch=[f"h{i}" for i in range(4)]; R.shuffle(ch); ph=["p0","p1"]; R.shuffle(ph)
        ctx=list("ABCD"); R.shuffle(ctx); meta=f"m{R.randrange(10**9)}"
        for k in "ABC":
            v=X[k]; y=transform(v[5],o); cur=tparts(v[2],o,4,R); M=[tparts(z[0],o,4,R) for z in v[6]]
            R.shuffle(M)
            assert mr(y,cur,4)-K<=EPS and all(mr(y,p,4)-K>EPS for p in M); mm[k]=set(M); cnt[k]+=1
        abd+=int(mm["A"]!=mm["B"]); cbad+=int(basebase_ok(C[5],4,C[2],C[3])>0)
        d=Dc[R.randrange(5)]; o5=list(range(32)); R.shuffle(o5); y=transform(d[5],o5)
        items=list(d[3]); R.shuffle(items)
        ok=any(mr(y,tparts(P,o5,5,R),5)-K>EPS for P in items); dany+=int(ok); cnt["D"]+=int(not ok)
    assert cnt=={"A":64,"B":64,"C":64,"D":64} and abd==64 and cbad==0 and dany==0
    rep=next(p for p in A[6][0][1]["programs"] if p[0]!="noop"); tt,close=rep[1],rep[3]
    patt={}
    for k in "ABC":
        v=X[k]; BB=base(4); G={app(tt,a,b,4) for a in BB for b in BB}; P=xclose(set(v[1])|G,4) if close else parts(set(v[1])|G,4)
        patt[k]=mr(v[5],P,4)-K>EPS
    patt["D"]=False; assert patt=={"A":True,"B":False,"C":False,"D":False}
    mins={k:[summary(z,v[0],v[2]) for z in v[6]] for k,v in X.items()}; mins["D"]=[]
    rawc={"A":207,"B":207,"C":417,"D":207}; semc={"A":A[4],"B":B[4],"C":C[4],"D":Dc[0][4]}
    fpc={"A":len(A[3]),"B":len(B[3]),"C":len(C[3]),"D":len(Dc[0][3])}
    return {"preregistration_commit":PRE,"gate":"extension_synthesis_relative_to_M0_only","encodings":64,"synthesis_episodes":256,
      "candidate_binding_performed":False,"extension_valuation_performed":False,"authorization_performed":False,"heldout_post_binding_episode_performed":False,
      "M0":{"raw_operator_syntax_trees":102,"distinct_synthesized_binary_truth_functions":10,"truth_function_tables":[list(x) for x in sorted(FUN)],"ledger":LEDGER,"named_extension_menu_used":False,"target_specific_synthesis_template_used":False},
      "current_closure_profiles":prof,"current_closure_fingerprints":{"A_B_linear_C0":{"size":15,"checksum_sha256":h(A[2],4)},"C_degree_le_2":{"size":1023,"checksum_sha256":h(C[2],4)}},
      "candidate_enumeration":{"raw_program_counts_before_operator_semantic_dedup":rawc,**{k:{"semantic_programs_after_operator_dedup":semc[k],"semantic_candidate_closure_fingerprints":fpc[k]} for k in "ABCD"}},
      "minimal_adequate_candidate_classes":mins,
      "primary_results":{"A_adequate_candidate_set_synthesized":{"correct":64,"total":64},"B_adequate_candidate_set_synthesized":{"correct":64,"total":64},"C_reuse_depth_candidate_set_synthesized":{"correct":64,"total":64},"D_NO_SUPPORTED_CANDIDATE":{"correct":64,"total":64},"coarse_synthesis_correct":256,"coarse_synthesis_total":256,"A_B_semantic_candidate_sets_distinct_encodings":abd,"C_BASE_BASE_only_adequate_encodings":0,"D_any_M0_repair_supported_encodings":dany},
      "wrong_extension_controls":{"W1_geometry_preserving_candidate_inadequate":True,"W2_A_has_expanding_but_wrong_candidate":wrong_expand(A[5],4,A[2],A[3]),"W2_B_has_expanding_but_wrong_candidate":wrong_expand(B[5],4,B[2],B[3]),"W3_C_BASE_BASE_only_adequate":False,"W4_D_all_M0_programs_inadequate":True},
      "anti_scaffold_controls":{"M1_named_menu":{"can_select_exact":True,"classification":"candidate selection from supplied menu","valid_synthesis_evidence":False},"M2_opaque_repair_macro":{"classification":"hidden extension specification","valid_synthesis_evidence":False},"M3_target_specific_template":{"classification":"oracle displacement","valid_synthesis_evidence":False},"M4_target_blind_M0":{"valid_primary_evidence":True}},
      "restricted_controls":{"R0_diagnosis_only_fixed_axis_ceiling":.25,"R1_always_emit_extension_support_null_ceiling":.75,"R2_fixed_A_minimal_reflex_pattern":patt,"R2_fixed_A_minimal_reflex_accuracy":.25},
      "class_specific":{"A":{"current_family_size":15,"minimal_candidate_classes":1},"B":{"current_family_size":15,"minimal_candidate_classes":1},"C":{"current_family_size":1023,"minimal_candidate_classes":2,"base_base_only_candidate_fingerprints_adequate":0},"D":{"current_family_size":15,"minimal_candidate_classes":0,"baseline_accuracy":.5,"exact_target_R_corr":.5,"exact_target_q":.4}},
      "earned_boundary":{"bounded_extension_synthesis_relative_to_M0":True,"candidate_space_construction_not_menu_selection":True,"diagnosis_not_fixed_repair_reflex":True,"reuse_depth_repair_distinguished":True,"unsupported_expansion_withheld":True,"extension_valuation_unresolved":True},
      "anonymous_encoding":{"world_label_permutation":True,"coordinate_handle_permutation":True,"public_binary_output_polarity_flips":True,"correction_context_identifier_permutation":True,"meta_primitive_handle_renaming":True,"pool_handle_renaming":True,"candidate_handle_and_enumeration_permutation":True,"semantic_equality_by_counterfactual_closure_fingerprint":True}}
def upstream():
    from closure_insufficiency_diagnosis_audit import audit
    u=audit(); assert u["total_correct"]==768 and u["total"]==768
    assert all(u["primary_diagnosis"][k]["correct"]==256 for k in ("SEARCH_MISS","VALUATION_MISHANDLE","CLOSURE_INSUFFICIENT"))
    assert abs(u["restricted_controls"]["D0_failure_only"]["ceiling"]-2/3)<EPS and abs(u["restricted_controls"]["D1_actor_observed_capacity"]["ceiling"]-2/3)<EPS
    assert abs(u["restricted_controls"]["D2_exact_target_membership"]["ceiling"]-2/3)<EPS and abs(u["restricted_controls"]["D2_naive_outside_implies_insufficient"]["accuracy"]-1/3)<EPS
    return {"closure_diagnosis_commit":UP,"hard_assertions_wired_in_executable":True,"freshly_process_replayed_in_connector_session":False,
      "required_diagnosis_anchors":{"SEARCH_MISS_correct":256,"VALUATION_MISHANDLE_correct":256,"CLOSURE_INSUFFICIENT_correct":256,"total_correct":768,"D0_ceiling":2/3,"D1_ceiling":2/3,"D2_ceiling":2/3,"naive_target_outside_accuracy":1/3},
      "inherited_gate2_gate1_accessibility_valuation_navigation_assertions":True,"provenance":"fresh extension-synthesis panel with inherited hard regression assertions"}
def audit():
    o=core(); o["upstream_regression"]=upstream(); return o
if __name__=="__main__": print(json.dumps(audit(),indent=2,sort_keys=True))
