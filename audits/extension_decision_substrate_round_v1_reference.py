"""DSLI_R1 frozen reference semantics. Construction only; no calibration characterization."""
from itertools import combinations,permutations,product
from collections import defaultdict,deque
from hashlib import sha256
import json
PI,PJ,EQ,NWP="PREFER_I","PREFER_J","EQUIVALENT","NO_WARRANTED_PREFERENCE"
TOK=(PI,PJ,EQ,NWP); LANG=("L_ORD1","L_RADIUS1","L_BANDS1","L_INTERSECT2","L_POSET","L_SPARSE_LINEAR")
def pairs(n): return list(combinations(range(n),2))
def canon(x): return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False)
def H(s): return sha256(s.encode()).hexdigest()
def blank(n,t=NWP): return {p:t for p in pairs(n)}
def setp(r,a,b,w):
 i,j=sorted((a,b)); r[i,j]=PI if w==i else PJ
def counts(r): return {t:list(r.values()).count(t) for t in TOK}
def records(r): return [{"i":i,"j":j,"token":r[i,j]} for i,j in sorted(r)]
def from_records(a,n):
 r={(x["i"],x["j"]):x["token"] for x in a}; assert set(r)==set(pairs(n)); return r
def total(order):
 n=len(order); q={x:k for k,x in enumerate(order)}
 return {(i,j):(PI if q[i]<q[j] else PJ) for i,j in pairs(n)}
def cyc(n):
 r={}
 for i,j in pairs(n):
  d=j-i
  r[i,j]=PI if d<=n/2 else PJ
 return r
def cycle(groups,n):
 r=blank(n)
 for g in groups:
  for a,b in zip(g,g[1:]+g[:1]): setp(r,a,b,a)
 return r
def world():
 out=[]
 def add(cid,n,r,K): out.append({"relation_id":cid,"anonymous_candidate_count":n,"candidate_handles":list(range(n)),"structural_descriptor_K":K|{"N":n,"C_Sigma":counts(r)},"target_token_counts":counts(r),"records":records(r),"evidence_role":"CALIBRATION_EVIDENCE_WHEN_EXECUTED"})
 for n in (6,7):
  cr=cyc(n); order={6:[0,1,2,5,4,3],7:[0,1,2,6,5,4,3]}[n]; tr=total(order)
  common={"T_abst":"NONE","T_eq":"TRIVIAL","T_comp":"PAIRWISE_GLOBAL","T_conn":"CONNECTED","T_dim":"NA","matched_block_id":f"DIR_TOPOLOGY_N{n}","manipulated_axes":["T_dir"],"held_fixed_axes":["T_abst","T_eq","T_comp","T_conn","T_dim","N","C_Sigma"]}
  add(f"DIR_TOPOLOGY_N{n}_A_TOTAL",n,tr,common|{"T_dir":"TOTAL_ORDER","case_role":"A"})
  add(f"DIR_TOPOLOGY_N{n}_B_CYCLE",n,cr,common|{"T_dir":"CYCLIC_TOURNAMENT","case_role":"B"})
  a=total(list(range(n))); b=dict(a)
  for i in range(n-1): a[i,i+1]=NWP
  for p in sorted(pairs(n),key=lambda p:(-abs(p[1]-p[0]),p[0],p[1]))[:n-1]: b[p]=NWP
  common={"T_dir":"ORDER_CONSISTENT_ACYCLIC","T_eq":"TRIVIAL","T_comp":"SINGLE_AXIS","T_conn":"CONNECTED","T_dim":"ONE_DIMENSIONAL","matched_block_id":f"ABST_TOPOLOGY_N{n}","manipulated_axes":["T_abst"],"held_fixed_axes":["T_dir","T_eq","T_comp","T_conn","T_dim","N","C_Sigma"]}
  add(f"ABST_TOPOLOGY_N{n}_A_MONOTONE",n,a,common|{"T_abst":"MONOTONE_LOCAL","case_role":"A"})
  add(f"ABST_TOPOLOGY_N{n}_B_CROSSCUT",n,b,common|{"T_abst":"CROSS_CUT","case_role":"B"})
  a=blank(n); b=blank(n); a[0,1]=a[2,3]=EQ; b[0,1]=b[1,2]=EQ
  common={"T_dir":"NONE","T_abst":"DEFAULT_COMPLEMENT","T_comp":"NONE","T_conn":"DISCONNECTED","T_dim":"NA","matched_block_id":f"EQ_LAWFULNESS_N{n}","manipulated_axes":["T_eq"],"held_fixed_axes":["T_dir","T_abst","T_comp","T_conn","T_dim","N","C_Sigma"]}
  add(f"EQ_LAWFULNESS_N{n}_A_PARTITION",n,a,common|{"T_eq":"LAWFUL_PARTITION","case_role":"A"})
  add(f"EQ_LAWFULNESS_N{n}_B_NONTRANSITIVE",n,b,common|{"T_eq":"NONTRANSITIVE_TOKEN","case_role":"B"})
  ga={6:[[0,1,2,5,3,4]],7:[[0,1,2,6,3,4,5]]}[n]; gb={6:[[0,1,2],[3,4,5]],7:[[0,1,2],[3,4,5,6]]}[n]
  a=cycle(ga,n); b=cycle(gb,n)
  common={"T_dir":"CYCLIC_SPARSE","T_abst":"DEFAULT_COMPLEMENT","T_eq":"TRIVIAL","T_comp":"RELATIONAL","T_dim":"NA","matched_block_id":f"CONNECTIVITY_N{n}","manipulated_axes":["T_conn"],"held_fixed_axes":["T_dir","T_abst","T_eq","T_comp","T_dim","N","C_Sigma"]}
  add(f"CONNECTIVITY_N{n}_A_CONNECTED",n,a,common|{"T_conn":"CONNECTED","case_role":"A"})
  add(f"CONNECTIVITY_N{n}_B_DISCONNECTED",n,b,common|{"T_conn":"DISCONNECTED","case_role":"B"})
  a=blank(n); b=blank(n)
  for i,j in combinations(range(4),2): a[i,j]=PI
  for i,j in [(0,1),(1,2),(2,3),(3,4),(0,4),(1,4)]: b[i,j]=PI
  common={"T_abst":"DEFAULT_COMPLEMENT","T_eq":"TRIVIAL","T_comp":"RELATIONAL","T_conn":"DISCONNECTED","T_dim":"NA","matched_block_id":f"TRANSITIVITY_N{n}","manipulated_axes":["T_dir"],"held_fixed_axes":["T_abst","T_eq","T_comp","T_conn","T_dim","N","C_Sigma"]}
  add(f"TRANSITIVITY_N{n}_A_PARTIAL_ORDER",n,a,common|{"T_dir":"PARTIAL_ORDER","case_role":"A"})
  add(f"TRANSITIVITY_N{n}_B_NONTRANSITIVE",n,b,common|{"T_dir":"ACYCLIC_NONTRANSITIVE","case_role":"B"})
  a=blank(n); b=blank(n)
  for i,j in pairs(n):
   if j-i>=3:a[i,j]=PI
   if j-i>=2:b[i,j]=PI
  common={"T_dir":"ORDER_CONSISTENT_ACYCLIC","T_abst":"MONOTONE_LOCAL","T_eq":"TRIVIAL","T_comp":"SINGLE_AXIS","T_conn":"CONNECTED","T_dim":"ONE_DIMENSIONAL","matched_block_id":f"CARDINALITY_STRESS_N{n}","manipulated_axes":["C_Sigma"],"held_fixed_axes":["T_dir","T_abst","T_eq","T_comp","T_conn","T_dim","N"]}
  add(f"CARDINALITY_STRESS_N{n}_A_SPARSE",n,a,common|{"case_role":"A"})
  add(f"CARDINALITY_STRESS_N{n}_B_DENSE",n,b,common|{"case_role":"B"})
 c=[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2)]; a=blank(6)
 for i,j in pairs(6):
  x,y=c[i],c[j]
  if x[0]>=y[0] and x[1]>=y[1]:a[i,j]=PI
  elif y[0]>=x[0] and y[1]>=x[1]:a[i,j]=PJ
 b=total([5,4,3,2,1,0])
 for p in [(0,1),(2,3),(4,5)]:b[p]=NWP
 common={"T_eq":"TRIVIAL","T_conn":"CONNECTED","matched_block_id":"PRODUCT_GEOMETRY_N6","manipulated_axes":["T_dir","T_abst","T_comp","T_dim"],"held_fixed_axes":["T_eq","T_conn","N","C_Sigma"]}
 add("PRODUCT_GEOMETRY_N6_A_PRODUCT",6,a,common|{"T_dir":"PRODUCT_ORDER","T_abst":"PRODUCT_INCOMPARABILITY","T_comp":"PRODUCT","T_dim":"TWO_DIMENSIONAL","case_role":"A"})
 add("PRODUCT_GEOMETRY_N6_B_SINGLE_AXIS",6,b,common|{"T_dir":"ORDER_CONSISTENT_ACYCLIC","T_abst":"DISCONNECTED_LOCAL","T_comp":"SINGLE_AXIS","T_dim":"ONE_DIMENSIONAL","case_role":"B"})
 assert len(out)==26
 return out
def blocks_from_eq(r,n):
 par=list(range(n))
 def f(x):
  while par[x]!=x:par[x]=par[par[x]];x=par[x]
  return x
 def u(a,b):
  a,b=f(a),f(b)
  if a!=b:par[b]=a
 for i,j in pairs(n):
  if r[i,j]==EQ:u(i,j)
 d=defaultdict(list)
 for i in range(n):d[f(i)].append(i)
 bs=sorted((tuple(sorted(v)) for v in d.values()),key=lambda z:z[0])
 for B in bs:
  for i,j in combinations(B,2):
   if r[i,j]!=EQ:return None
 roots={x:B[0] for B in bs for x in B}; qr={}
 for A,B in combinations(bs,2):
  ra,rb=A[0],B[0]; vals=set()
  for x in A:
   for y in B:
    i,j=sorted((x,y));t=r[i,j]
    if t==EQ:return None
    if t==NWP: vals.add(NWP)
    else:
     w=i if t==PI else j; vals.add("A" if roots[w]==ra else "B")
  if len(vals)!=1:return None
  qr[ra,rb]=next(iter(vals))
 return bs,roots,qr
def merges(bs): return [[B[0],x] for B in bs for x in B[1:]]
def edges(qr):
 e=set()
 for (a,b),t in qr.items():
  if t=="A":e.add((a,b))
  elif t=="B":e.add((b,a))
 return e
def acyclic(nodes,E):
 indeg={x:0 for x in nodes}; adj={x:[] for x in nodes}
 for a,b in E:adj[a].append(b);indeg[b]+=1
 q=deque(sorted(x for x in nodes if indeg[x]==0));k=0
 while q:
  a=q.popleft();k+=1
  for b in adj[a]:
   indeg[b]-=1
   if indeg[b]==0:q.append(b)
 return k==len(nodes)
def reach(nodes,E,a,b):
 adj={x:[] for x in nodes}
 for x,y in E:adj[x].append(y)
 q=[a];seen={a}
 while q:
  x=q.pop()
  for y in adj[x]:
   if y==b:return True
   if y not in seen:seen.add(y);q.append(y)
 return False
def closure(nodes,E): return {(a,b) for a in nodes for b in nodes if a!=b and reach(nodes,E,a,b)}
def topo(nodes,E):
 out=[];nodes=tuple(sorted(nodes))
 for p in permutations(nodes):
  rank={x:i for i,x in enumerate(p)}
  if all(rank[a]<rank[b] for a,b in E):out.append(p)
 return out
def qdecode(s,roots,kind,param):
 o={}
 for a,b in combinations(roots,2):
  d=s[a]-s[b]
  if kind=="R":o[a,b]=NWP if abs(d)<=param else ("A" if d>0 else "B")
  else:
   t1,t2,pol=param;k=0 if abs(d)<=t1 else 1 if abs(d)<=t2 else 2;o[a,b]=NWP if pol[k]=="N" else ("A" if d>0 else "B")
 return o
def pi(language,r,n):
 q=blocks_from_eq(r,n)
 if q is None:return False,None
 bs,root,qr=q;roots=[B[0] for B in bs];c=len(bs);E=edges(qr)
 if language=="L_ORD1":
  return (False,None) if any(v==NWP for v in qr.values()) or not acyclic(roots,E) else (True,n+3)
 if language in ("L_RADIUS1","L_BANDS1"):
  for vals in permutations(range(n),c):
   if min(vals)!=0:continue
   s=dict(zip(roots,vals))
   if language=="L_RADIUS1":
    for t in range(n):
     if qdecode(s,roots,"R",t)==qr:return True,n+5
   else:
    for t1 in range(n):
     for t2 in range(t1,n):
      for pol in product(("D","N"),repeat=3):
       if qdecode(s,roots,"B",(t1,t2,pol))==qr:return True,n+7
  return False,None
 if language=="L_INTERSECT2":
  if not acyclic(roots,E) or closure(roots,E)!=E:return False,None
  for o1 in topo(roots,E):
   rank={x:i for i,x in enumerate(o1)};C=set(E)
   for a,b in combinations(roots,2):
    if qr[a,b]==NWP:C.add((b,a) if rank[a]<rank[b] else (a,b))
   if acyclic(roots,C):return True,n+c+5
  return False,None
 if language=="L_POSET":
  if not acyclic(roots,E) or closure(roots,E)!=E:return False,None
  cover={(a,b) for a,b in E if not any(x not in (a,b) and (a,x) in E and (x,b) in E for x in roots)}
  return True,(n-c)+len(cover)+5
 if language=="L_SPARSE_LINEAR": return (len(E)<=n-1,((n-c)+len(E)+5) if len(E)<=n-1 else None)
 raise KeyError(language)
def nuisance(case,n,e):
 return {"candidate_permutation":sorted(range(n),key=lambda i:H(f"{case}|perm|{e}|{i}")),"pair_record_order":sorted(pairs(n),key=lambda p:H(f"{case}|pair-order|{e}|{p[0]}|{p[1]}")),"aliases":{i:"A_"+H(f"{case}|alias|{e}|{i}")[:12] for i in range(n)},"nonce":H(f"{case}|nonce|{e}"),"implementation_tag":"TAG_"+H(f"{case}|impl|{e}")[:12]}
if __name__=="__main__":
 print(canon({"round_id":"DSLI_R1","round_version":1,"cases":world(),"characterization_results_present":False}))
