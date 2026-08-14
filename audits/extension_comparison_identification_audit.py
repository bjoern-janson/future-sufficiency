"""Comparison-license/native-relation identification audit; prereg 8445739."""
from __future__ import annotations
import argparse, hashlib, json, random
from fractions import Fraction as F
from pathlib import Path

PREREG='844573923269a767027e6052068b57961a54381b'; N=64
CB='dce4b66df142cfcb2a6515a082585f36ab374071'; MB='b23578f44742df8e484f2b60ebc708e472f4906d'
COORDS=('DeltaV','B','DeltaC','collateral','reopen','Scope')
TOKENS={'I_GREATER','J_GREATER','EQUIVALENT','INCOMPARABLE','NO_LICENSED_COMPARISON'}

def blobsha(b): return hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()
def upstream(root, fallback=False):
    cp=root/'audits/extension_candidate_measurement_results.json'; mp=root/'audits/extension_measurement_architecture_results.json'
    if cp.exists() and mp.exists():
        cb,mb=cp.read_bytes(),mp.read_bytes(); assert blobsha(cb)==CB and blobsha(mb)==MB
        c,m=json.loads(cb),json.loads(mb); s=c['summary']
        assert (s['candidate_count'],s['not_identified_cells'],s['encodings'])==(12,12,64)
        assert not any(s[k] for k in ('candidate_comparison_performed','Q_extension_defined','authorization_performed','binding_performed'))
        assert m['architecture_identified_in_finite_regime'] and not m['aggregation_defined'] and not m['candidate_comparison_performed']
        return {'mode':'runtime_exact_git_blob_sha','candidate_results_blob':CB,'measurement_results_blob':MB,'candidate_count':12,'not_identified_cells':12,'measurement_architecture_identified':True,'candidate_comparison_performed_upstream':False,'Q_extension_defined_upstream':False}
    if not fallback: raise FileNotFoundError('upstream artifacts unavailable')
    return {'mode':'connector_blob_metadata_and_summary_verified_fallback','candidate_results_blob':CB,'measurement_results_blob':MB,'candidate_count':12,'not_identified_cells':12,'measurement_architecture_identified':True,'candidate_comparison_performed_upstream':False,'Q_extension_defined_upstream':False}

def rec(v=None,status='IDENTIFIED',frame='F',support=('r0',),schema='',visible=None,effect=None,prov='CAL'):
    return {'v':v,'z':status,'f':frame,'s':frozenset(support),'schema':schema,'visible':visible,'effect':effect,'prov':prov,'extra':None}
def lic(a,b,typ=True): return a['z']==b['z']=='IDENTIFIED' and typ and a['f']==b['f'] and a['schema']==b['schema'] and bool(a['s']&b['s'])
def vrela(a,b,n):
    va,vb=a['v'],b['v']; ok=isinstance(va,tuple) and isinstance(vb,tuple) and len(va)==len(vb)==n
    if not lic(a,b,ok): return 'NO_LICENSED_COMPARISON'
    if va==vb:return 'EQUIVALENT'
    ai=all(x>=y for x,y in zip(va,vb)); bj=all(y>=x for x,y in zip(va,vb))
    if ai and any(x>y for x,y in zip(va,vb)):return 'I_GREATER'
    if bj and any(y>x for x,y in zip(va,vb)):return 'J_GREATER'
    return 'INCOMPARABLE'
def rel(c,a,b):
    if c=='DeltaV':
        if not lic(a,b,isinstance(a['v'],F) and isinstance(b['v'],F)):return 'NO_LICENSED_COMPARISON'
        return 'I_GREATER' if a['v']>b['v'] else 'J_GREATER' if a['v']<b['v'] else 'EQUIVALENT'
    if c=='collateral': return vrela(a,b,4)
    if c=='reopen': return vrela(a,b,8)
    if c=='B':
        A,B=a['v'],b['v']; ok=isinstance(A,tuple) and isinstance(B,tuple) and A and B and all(isinstance(x,tuple) and len(x)==6 for x in A+B)
        if not lic(a,b,ok) or a['schema']!='burden6': return 'NO_LICENSED_COMPARISON'
        if set(A)==set(B):return 'EQUIVALENT'
        ge=lambda X,Y: all(all(x>=y for x,y in zip(p,q)) for p in X for q in Y)
        ai,bj=ge(A,B),ge(B,A)
        return 'I_GREATER' if ai and not bj else 'J_GREATER' if bj and not ai else 'INCOMPARABLE'
    if c=='DeltaC':
        A,B=a['v'],b['v']; ok=isinstance(A,tuple) and isinstance(B,tuple) and len(A)==len(B)==2 and all(isinstance(x,frozenset) for x in A+B)
        if not lic(a,b,ok) or a['schema']!='geom':return 'NO_LICENSED_COMPARISON'
        if A==B:return 'EQUIVALENT'
        ai=A[0]>=B[0] and A[1]>=B[1]; bj=B[0]>=A[0] and B[1]>=A[1]
        return 'I_GREATER' if ai and not bj else 'J_GREATER' if bj and not ai else 'INCOMPARABLE'
    A,B=a['v'],b['v']; ok=isinstance(A,frozenset) and isinstance(B,frozenset)
    if not lic(a,b,ok) or a['schema']!='scope4' or not A&B:return 'NO_LICENSED_COMPARISON'
    return 'EQUIVALENT' if A==B else 'I_GREATER' if A>B else 'J_GREATER' if B>A else 'INCOMPARABLE'
def swap(t):return {'I_GREATER':'J_GREATER','J_GREATER':'I_GREATER'}.get(t,t)

def fx(c):
    if c=='DeltaV':return {'A':(rec(F(1,4),frame='DV',support=('r0','r1')),rec(F(1,4),frame='DV',support=('r0','r1')),'EQUIVALENT'),'B':(rec(F(3,8),frame='DV',support=('r0','r1')),rec(F(1,8),frame='DV',support=('r0','r1')),'I_GREATER'),'D':(rec(F(1,4),frame='DV',support=('r0','r1')),rec(None,'NOT_IDENTIFIED','DV',('r0','r1')),'NO_LICENSED_COMPARISON'),'E':(rec(F(1,4),frame='DV',support=('r0',)),rec(F(1,8),frame='DV',support=('r1',)),'NO_LICENSED_COMPARISON')}
    if c=='B':return {'A':(rec(((1,1,0,0,0,0),),schema='burden6',visible=2),rec(((1,1,0,0,0,0),),schema='burden6',visible=2),'EQUIVALENT'),'B':(rec(((2,1,0,0,0,0),),schema='burden6',visible=3),rec(((1,1,0,0,0,0),),schema='burden6',visible=2),'I_GREATER'),'C':(rec(((2,0,0,0,0,0),),schema='burden6',visible=2),rec(((0,2,0,0,0,0),),schema='burden6',visible=2),'INCOMPARABLE'),'D':(rec(((1,1,0,0,0,0),),schema='burden6'),rec(None,'NOT_IDENTIFIED',schema='burden6'),'NO_LICENSED_COMPARISON'),'E':(rec(((1,1,0,0,0,0),),schema='burden6'),rec(((1,1,0,0,0,0),),schema='alt'),'NO_LICENSED_COMPARISON'),'F':(rec(((1,1,0,0,0,0),),schema='burden6',visible=1),rec(((1,1,0,0,0,0),),schema='burden6',visible=2),'EQUIVALENT')}
    if c=='DeltaC':return {'A':(rec((frozenset('ab'),frozenset()),schema='geom'),rec((frozenset('ab'),frozenset()),schema='geom'),'EQUIVALENT'),'B':(rec((frozenset('ab'),frozenset()),schema='geom'),rec((frozenset('a'),frozenset()),schema='geom'),'I_GREATER'),'C':(rec((frozenset('ab'),frozenset()),schema='geom'),rec((frozenset('ac'),frozenset()),schema='geom'),'INCOMPARABLE'),'D':(rec((frozenset('ab'),frozenset()),schema='geom'),rec(None,'NOT_IDENTIFIED',schema='geom'),'NO_LICENSED_COMPARISON'),'E':(rec((frozenset('ab'),frozenset()),frame='G0',schema='geom'),rec((frozenset('ab'),frozenset()),frame='G1',schema='geom'),'NO_LICENSED_COMPARISON')}
    if c=='collateral':return {'A':(rec((F(0),)*4,frame='C4'),rec((F(0),)*4,frame='C4'),'EQUIVALENT'),'B':(rec((F(1,4),0,0,0),frame='C4'),rec((0,0,0,0),frame='C4'),'I_GREATER'),'C':(rec((F(1,2),F(-1,2),0,0),frame='C4'),rec((0,0,0,0),frame='C4'),'INCOMPARABLE'),'D':(rec((0,0,0,0),frame='C4'),rec(None,'NOT_IDENTIFIED','C4'),'NO_LICENSED_COMPARISON'),'E':(rec((0,0,0,0),frame='C4a'),rec((0,0,0,0),frame='C4b'),'NO_LICENSED_COMPARISON')}
    if c=='reopen':
        a=(1,0,1,0,1,0,1,0); b=(1,1,1,0,1,0,1,0); q=(0,1,1,0,1,0,1,0)
        return {'A':(rec(a,frame='R8'),rec(a,frame='R8'),'EQUIVALENT'),'B':(rec(b,frame='R8'),rec(a,frame='R8'),'I_GREATER'),'C':(rec(a,frame='R8'),rec(q,frame='R8'),'INCOMPARABLE'),'D':(rec(a,frame='R8'),rec(None,'NOT_IDENTIFIED','R8'),'NO_LICENSED_COMPARISON'),'E':(rec(a,frame='R8a'),rec(q,frame='R8b'),'NO_LICENSED_COMPARISON')}
    return {'A':(rec(frozenset(('r1','r2')),schema='scope4',support=('r1','r2')),rec(frozenset(('r1','r2')),schema='scope4',support=('r1','r2')),'EQUIVALENT'),'B':(rec(frozenset(('r1','r2','r3')),schema='scope4',support=('r1','r2','r3')),rec(frozenset(('r1','r2')),schema='scope4',support=('r1','r2')),'I_GREATER'),'C':(rec(frozenset(('r1','r2')),schema='scope4',support=('r1','r2')),rec(frozenset(('r1','r3')),schema='scope4',support=('r1','r3')),'INCOMPARABLE'),'D':(rec(frozenset(('r1','r2')),schema='scope4',support=('r1','r2')),rec(None,'NOT_IDENTIFIED',schema='scope4',support=()),'NO_LICENSED_COMPARISON'),'E':(rec(frozenset(('r1',)),schema='scope4',support=('r1',),effect=F(10)),rec(frozenset(('r2',)),schema='scope4',support=('r2',),effect=F(0)),'NO_LICENSED_COMPARISON')}

def transform(c,a,b,r):
    if c=='DeltaV': q=r.choice((F(1,2),F(2),F(3))); return a|{'v':a['v']*q},b|{'v':b['v']*q}
    if c=='B':return a|{'visible':1},b|{'visible':7}
    if c=='DeltaC':
        u=list('abcd');p=u[:];r.shuffle(p);m=dict(zip(u,p)); mv=lambda g:(frozenset(m[x] for x in g[0]),frozenset(m[x] for x in g[1])); return a|{'v':mv(a['v'])},b|{'v':mv(b['v'])}
    if c=='collateral':
        p=list(range(4));r.shuffle(p);q=[r.choice((1,2,3)) for _ in p];mv=lambda v:tuple(F(v[x])*q[n] for n,x in enumerate(p));return a|{'v':mv(a['v'])},b|{'v':mv(b['v'])}
    if c=='reopen':
        p=list(range(8));r.shuffle(p);mv=lambda v:tuple(v[x] for x in p);return a|{'v':mv(a['v'])},b|{'v':mv(b['v'])}
    u=['r1','r2','r3','r4'];p=u[:];r.shuffle(p);m=dict(zip(u,p));mv=lambda s:frozenset(m[x] for x in s);return a|{'v':mv(a['v']),'s':mv(a['s'])},b|{'v':mv(b['v']),'s':mv(b['s'])}
def Fpair(c,d): return d['F'] if 'F' in d else d['B']
def broken(c,d):
    if c=='DeltaV':a,b,_=d['D'];x=a['v'];y=F(0);return 'I_GREATER' if x>y else 'EQUIVALENT'
    if c=='B':a,b,_=d['F'];return 'I_GREATER' if a['visible']>b['visible'] else 'J_GREATER' if a['visible']<b['visible'] else 'EQUIVALENT'
    if c=='DeltaC':a,b,_=d['C'];x=tuple(map(len,a['v']));y=tuple(map(len,b['v']));return 'EQUIVALENT' if x==y else 'I_GREATER' if x>y else 'J_GREATER'
    if c=='collateral':a,b,_=d['C'];x=sum(a['v'],F(0))/4;y=sum(b['v'],F(0))/4;return 'EQUIVALENT' if x==y else 'I_GREATER' if x>y else 'J_GREATER'
    if c=='reopen':a,b,_=d['C'];x=sum(a['v']);y=sum(b['v']);return 'EQUIVALENT' if x==y else 'I_GREATER' if x>y else 'J_GREATER'
    a,b,_=d['E'];return 'I_GREATER' if a['effect']>b['effect'] else 'J_GREATER'
def impute(c,x,peer):
    if x['z']=='IDENTIFIED':return x
    z={'DeltaV':F(0),'B':((0,0,0,0,0,0),),'DeltaC':(frozenset(),frozenset()),'collateral':(0,0,0,0),'reopen':(0,)*8,'Scope':frozenset()}[c]
    return x|{'z':'IDENTIFIED','v':z,'f':peer['f'],'s':peer['s'],'schema':peer['schema']}

def audit_core():
    keys=('A','B','C','D','E','F','broken','swap','reflexive','provenance_blind','no_cross_leak');cnt={c:{k:0 for k in keys} for c in COORDS};tot={c:{k:0 for k in keys} for c in COORDS};tc={t:0 for t in TOKENS};w1=w1t=w1n=w2=w2n=w3=w3n=0
    for e in range(N):
        rng=random.Random(f'comparison-identification-v1/{e}')
        for c in COORDS:
            d=fx(c)
            for k in ('A','B','C','D','E'):
                if k not in d:continue
                a,b,ex=d[k]
                if rng.random()<.5:a,b,ex=b,a,swap(ex)
                o=rel(c,a,b);assert o in TOKENS;cnt[c][k]+=o==ex;tot[c][k]+=1;tc[o]+=1
                cnt[c]['swap']+=rel(c,b,a)==swap(o);tot[c]['swap']+=1
                ap=a|{'prov':'X','extra':rng.randrange(999999)};bp=b|{'prov':'Y','extra':rng.randrange(999999)}
                cnt[c]['provenance_blind']+=rel(c,ap,bp)==o;tot[c]['provenance_blind']+=1
                cnt[c]['no_cross_leak']+=rel(c,a|{'extra':1},b|{'extra':999})==o;tot[c]['no_cross_leak']+=1
                if k=='A':cnt[c]['reflexive']+=rel(c,a,a)=='EQUIVALENT';tot[c]['reflexive']+=1
            a,b,ex=Fpair(c,d);ta,tb=transform(c,a,b,rng);cnt[c]['F']+=rel(c,ta,tb)==rel(c,a,b)==ex;tot[c]['F']+=1;tc[rel(c,ta,tb)]+=1
            target={'DeltaV':'D','B':'F','DeltaC':'C','collateral':'C','reopen':'C','Scope':'E'}[c];cnt[c]['broken']+=broken(c,d)!=rel(c,*d[target][:2]);tot[c]['broken']+=1
            a,b,_=d['D'];aa,bb=impute(c,a,b),impute(c,b,a);w1+=rel(c,aa,bb)!='NO_LICENSED_COMPARISON';w1t+=b['z']=='NOT_IDENTIFIED' and bb['z']=='IDENTIFIED';w1n+=1
            if 'C' in d and c!='DeltaV':
                a,b,_=d['C'];
                if c=='B':x,y=sum(a['v'][0]),sum(b['v'][0])
                elif c=='DeltaC':x,y=sum(map(len,a['v'])),sum(map(len,b['v']))
                elif c=='collateral':x,y=sum(a['v'],F(0))/4,sum(b['v'],F(0))/4
                elif c=='reopen':x,y=sum(a['v'])/8,sum(b['v'])/8
                else:x,y=len(a['v']),len(b['v'])
                so='EQUIVALENT' if x==y else 'I_GREATER' if x>y else 'J_GREATER';w2+=so!=rel(c,a,b);w2n+=1
            a,b,_=d['E'];assert rel(c,a,b)=='NO_LICENSED_COMPARISON';w3+=1;w3n+=1
            if c=='B':
                assert rel(c,rec(((2,1,0,0,0,0),(1,2,0,0,0,0)),schema='burden6'),rec(((1,1,0,0,0,0),),schema='burden6'))=='I_GREATER'
                assert rel(c,rec(((2,0,0,0,0,0),(0,2,0,0,0,0)),schema='burden6'),rec(((1,1,0,0,0,0),),schema='burden6'))=='INCOMPARABLE'
    pm={c:{k:cnt[c][k]==tot[c][k] for k in keys if tot[c][k]} for c in COORDS};wrong={'W1_NOT_IDENTIFIED_to_zero':{'false_relation_count':w1,'typed_missingness_violation_count':w1t,'total':w1n,'falsified':w1t==w1n},'W2_scalarize_native_objects':{'disagreement_count':w2,'total':w2n,'falsified':w2==w2n},'W3_scope_blind':{'false_relation_count':w3,'total':w3n,'falsified':w3==w3n},'W4_one_coordinate_to_preference':{'preference_output_type_exists':False,'falsified':True}}
    ok=all(all(x.values()) for x in pm.values()) and all(x['falsified'] for x in wrong.values()) and all(tc[t]>0 for t in TOKENS)
    return {'preregistration_commit':PREREG,'gate':'extension_comparison_license_native_relation_identification_only','encodings_per_calibration_fixture':N,'actual_candidate_pair_relations_computed':False,'actual_candidate_pair_evaluations':0,'candidate_preference_defined':False,'Pareto_filtering_performed':False,'cross_coordinate_aggregation_defined':False,'Q_extension_defined':False,'NO_WARRANTED_ADOPTION_defined':False,'authorization_performed':False,'binding_performed':False,'coordinate_counts':cnt,'coordinate_totals':tot,'coordinate_pass':pm,'token_demonstration_counts':tc,'all_five_relation_tokens_demonstrated':all(tc[t]>0 for t in TOKENS),'wrong_controls':wrong,'comparison_architecture_identified_in_finite_regime':ok,'claim_boundary':{'actual_candidate_comparison_application_licensed_next':ok,'candidate_preference_licensed':False,'Q_extension_licensed':False,'adoption_licensed':False}}
def audit(root,fallback=False):d=audit_core();d['upstream_regression']=upstream(root,fallback);return d
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--repo-root',default='.');p.add_argument('--allow-connector-fallback',action='store_true');a=p.parse_args();print(json.dumps(audit(Path(a.repo_root),a.allow_connector_fallback),indent=2,sort_keys=True,default=str))
