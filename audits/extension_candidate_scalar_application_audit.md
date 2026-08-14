# Extension Candidate Scalar Application Audit — Results

## Provenance

Preregistered before execution at:

```text
9f1ab6488e155b95b0d60896df3ab65b1ff5cd5d
```

Parent checkpoint:

```text
f10ff41e292ba8d2df26c0468f785d4fb07c2de6
```

Frozen scalar-family anchors:

```text
scalar-sufficiency preregistration
  4ebfd307e990710142bec0d732a0056d388e3c2d

scalar-sufficiency executable
  8548875bd88eb0c92a18c3cd4229486ea800816e

scalar-sufficiency result
  98a5db5311f18efa0f84e0fb1d99ef77574d8a91

scalar-sufficiency result note
  e35f58ef45903ffba266a52627c59138f14881a6
```

Frozen actual-preference anchors:

```text
preference-application executable
  b568d90be09bcfa23b4a67ebbdeb90be64bce02f

preference-application result
  7efc07e54de9b7e4719caee632daecab32e56f1f

preference-application result note
  26c5bebb205e320df8bb8c40f60a393ccf542455
```

Correct provenance:

\[
\boxed{\textbf{
fresh actual-candidate scalar-application result with frozen scalar-family semantics,
frozen governance-relative preference targets, exact finite-family adjudication,
and hard anti-scaffold regression assertions.
}}
\]

No scalar-family redesign, governance selection, candidate ranking, adoption, authorization, binding, or execution is introduced.

---

## 1. Frozen endpoint

The audit executes only:

\[
\boxed{
(R_{\rm pref}^{G,\rm actual},D_j)
\rightarrow
(D_{\rm scalar}^{G,j},B_{D_j},F_{\rm scalar}^{G,j})
}
\]

for:

```text
candidates                         12
unordered pairs                    66
governance contracts                4
admissible scalar families          3
primary G x D diagnoses            12
```

The candidate universe, pair universe, governance contracts, score domain, decoder semantics, burden formulas, and failure-locus vocabulary are unchanged from preregistration.

---

## 2. Primary result matrix

| governance contract | D0 | D1 | D2 |
|---|---|---|---|
| `G_PARTIAL_EMPTY` | `NOT_REPRESENTABLE` | `FAITHFUL_CONTRACTION` | `FAITHFUL_CONTRACTION` |
| `G_CONSTRAINT_B` | `NOT_REPRESENTABLE` | `NOT_REPRESENTABLE` | `NOT_REPRESENTABLE` |
| `G_LEX_DV_REOPEN_B` | `NOT_REPRESENTABLE` | `NOT_REPRESENTABLE` | `NOT_REPRESENTABLE` |
| `G_COMP_EXPLICIT` | `NOT_REPRESENTABLE` | `NOT_REPRESENTABLE` | `NOT_REPRESENTABLE` |

Across the 12 admissible family applications:

```text
FAITHFUL_CONTRACTION   2
NOT_REPRESENTABLE     10
```

The unrestricted lookup control is:

```text
REPRESENTABLE_NO_CONTRACTION  4/4
```

with:

```text
B_LOOKUP = 67 > 66 = B_Rpref
```

Therefore the lookup control again separates finite representability from genuine contraction.

---

## 3. D0 is predetermined, not experimental

Every actual governance-relative target graph contains `NO_WARRANTED_PREFERENCE`.

Observed target topology:

| governance | PREFER_I | PREFER_J | EQUIVALENT | NWP |
|---|---:|---:|---:|---:|
| `G_PARTIAL_EMPTY` | 0 | 0 | 1 | 65 |
| `G_CONSTRAINT_B` | 5 | 3 | 1 | 57 |
| `G_LEX_DV_REOPEN_B` | 3 | 5 | 1 | 57 |
| `G_COMP_EXPLICIT` | 3 | 5 | 1 | 57 |

Since D0 cannot emit NWP:

\[
\boxed{
D_0(G)=\texttt{NOT_REPRESENTABLE}
\quad\forall G.
}
\]

This is an input-level structural consequence, not a newly discovered empirical pattern.

The exact minimum total mismatches under D0 are therefore the target NWP counts:

```text
G_PARTIAL_EMPTY       65
each decisive graph   57
```

Loss-free and injection-free D0 members each exist separately, so the unavoidable failure locus remains only:

```text
DECODER_INSUFFICIENCY
```

---

## 4. The sparse partial-governance graph contracts

For `G_PARTIAL_EMPTY`, the complete target relation is:

```text
65 NO_WARRANTED_PREFERENCE
 1 EQUIVALENT
 0 directional edges
```

D1 has the canonical witness:

```text
candidate order:
CTRL_ALIAS_A
CTRL_ID_DEG2
CTRL_ID_LINEAR
CTRL_SUPPLIED_DEG2
EXT_CT_A
EXT_CT_B
EXT_CT_C1
EXT_CT_C2
SYN_A_120
SYN_B_50
SYN_C1_1653
SYN_C2_2388

q = [0,1,2,3,4,5,6,7,8,8,9,10]
tau = 10
```

Every nonzero difference lies inside the global abstention radius and the sole equality is exactly:

```text
SYN_A_120 = SYN_B_50
```

Thus:

```text
B_D1    = 17
B_Rpref = 66
```

and D1 earns `FAITHFUL_CONTRACTION`.

D2 has the same canonical q with:

```text
tau_1 = 0
tau_2 = 0
B1 = DIRECTION
B2 = DIRECTION
B3 = NO_WARRANTED_PREFERENCE
```

The first two bands are empty at these cutpoints; every nonzero observed difference uses B3.

Thus:

```text
B_D2    = 19
B_Rpref = 66
```

and D2 also earns `FAITHFUL_CONTRACTION`.

No family ranking follows from the fact that both contract this graph.

---

## 5. The three decisive governance graphs defeat D1

The three decisive graphs share the same undirected directional topology; the lexicographic and explicit-compensation graphs globally reverse the directional orientation relative to `G_CONSTRAINT_B`.

For D1, exact finite adjudication used:

```text
tau states                              14
normalized score subsets               286
semantic graph instances              4004
label-to-score bijections              exact, via directed graph isomorphism
```

No exact representation exists.

The minimum total mismatch count is exactly:

```text
4
```

For `G_CONSTRAINT_B`, an explicit four-mismatch family member is:

```text
q = [1,2,10,0,3,4,5,6,9,9,7,8]
tau = 8
```

Its only mismatches are:

```text
CTRL_ID_DEG2   vs SYN_C1_1653
CTRL_ID_DEG2   vs SYN_C2_2388
CTRL_ID_LINEAR vs SYN_A_120
CTRL_ID_LINEAR vs SYN_B_50
```

all four being target directional distinctions decoded as NWP.

The lower bound is exact: every target relation at Hamming distance 1, 2, or 3 from the actual decisive target was exhaustively adjudicated:

```text
radius 1    198 relations
radius 2  19305 relations
radius 3 1235520 relations
```

and none is D1-representable.

Therefore:

\[
\boxed{
\min \text{ total D1 mismatches}=4.
}
\]

---

## 6. D2 gets closer, but still fails the decisive graphs

D2 exhausts:

```text
raw parameter states                    840
unique semantic decoders                158
normalized score subsets                286
semantic graph instances              45188
label-to-score bijections              exact, via directed graph isomorphism
```

No exact decisive-graph representation exists.

The exact minimum total mismatch count is:

```text
2
```

For `G_CONSTRAINT_B`, an explicit two-mismatch family member is:

```text
q = [1,11,9,0,4,5,6,7,8,8,2,3]

tau_1 = 7
tau_2 = 9

B1 = NO_WARRANTED_PREFERENCE
B2 = DIRECTION
B3 = NO_WARRANTED_PREFERENCE
```

Its only mismatches are:

```text
CTRL_ID_LINEAR vs SYN_A_120
CTRL_ID_LINEAR vs SYN_B_50
```

both target directions decoded as NWP.

All 198 relations at Hamming distance one from the actual decisive target were exhaustively adjudicated and none is D2-representable. The two-mismatch witness therefore proves:

\[
\boxed{
\min \text{ total D2 mismatches}=2.
}
\]

D2 is strictly closer to the decisive actual topology than D1 under this descriptive mismatch count, but this does not authorize a decoder redesign or a preference for D2.

---

## 7. Failure locus remains set-valued and non-causal

For every nonrepresentable D0-D2 application:

```text
loss_free_member_exists       true
injection_free_member_exists  true
```

separately.

A loss-free member can preserve every target direction/equivalence while injecting directional order into target NWP edges.

An injection-free member can preserve every target NWP/equivalence while losing target directional distinctions.

Therefore neither mismatch class is individually unavoidable across the whole family.

The exact unavoidable locus is:

```text
[DECODER_INSUFFICIENCY]
```

for all ten nonrepresentable D0-D2 cases.

This is precisely why the preregistered set-valued failure locus matters: no arbitrary failed witness is promoted into a causal diagnosis.

`BURDEN_NON_CONTRACTION` occurs only for `W_LOOKUP`.

---

## 8. Governance determines scalarizability in this audited application

The same frozen 12-candidate universe gives different scalar status under different supplied governance relations:

\[
\boxed{
D_{1,2}(G_{\rm PARTIAL\_EMPTY})
=
\texttt{FAITHFUL\_CONTRACTION}
}
\]

while:

\[
\boxed{
D_{1,2}(G_{\rm CONSTRAINT\_B})
=
D_{1,2}(G_{\rm LEX\_DV\_REOPEN\_B})
=
D_{1,2}(G_{\rm COMP\_EXPLICIT})
=
\texttt{NOT\_REPRESENTABLE}.
}
\]

Thus the actual application supports the narrower statement:

\[
\boxed{
\text{scalarizability is a property of }R_{\rm pref}^{G,\rm actual},
\text{ not of the bare candidate set alone.}
}
\]

It does not establish that a more scalarizable governance contract is better.

The two reversed decisive status topologies have the same D1/D2 scalar-sufficiency status because global score reflection preserves absolute-distance decoder geometry while reversing directional sign.

---

## 9. Contract-level supported-contraction status

Exactly one governance graph has a supported scalar contraction in the frozen family:

```text
G_PARTIAL_EMPTY
```

The contract-level `NO_SUPPORTED_CONTRACTION` set is:

```text
G_CONSTRAINT_B
G_LEX_DV_REOPEN_B
G_COMP_EXPLICIT
```

This means only:

> no D0-D2 member faithfully contracts the corresponding actual typed preference relation.

It does not establish global minimality of the native typed relation.

---

## 10. Symmetry, nuisance, and broken controls

Pair-swap integrity remains exact:

```text
target relations                  264 / 264
successful scalar relations       132 / 132
```

Across 64 nuisance encodings:

```text
status                            768 / 768
burden                            768 / 768
failure_locus                     768 / 768
successful witness transport      128 / 128
```

The preregistered broken controls are detected or structurally rejected:

```text
W1  redesign after graph             absent
W2  NWP -> EQUIVALENT                detected
W3  NWP -> arbitrary direction       detected
W4  hidden pair exceptions           rejected
W5  lookup called contraction        detected
W6  decoder burden omitted           detected
W7  governance erased                rejected
W8  heuristic nonrepresentability    absent
W9  nuisance encoded in q            absent
W10 scalar status -> governance rank absent
W11 scalar -> authorization          absent
W12 global candidate ranking         absent
```

---

## 11. Anti-downstream status

```text
scalar sufficiency identification       true
actual candidate scalar application     true
actual Q_extension defined              false
governance contract selected            false
candidate adoption selected             false
candidate ranking performed             false
utility defined                         false
reward defined                          false
NO_WARRANTED_ADOPTION defined           false
adoption performed                      false
authorization performed                 false
binding performed                       false
execution performed                     false
```

A successful scalar witness remains an application-stage decision representation only.

---

## 12. Earned claim

\[
\boxed{\textbf{
For the frozen 12-candidate extension set and four supplied governance-relative
preference relations, the already-identified D0-D2 scalar families have been
applied without redesign and adjudicated exactly for faithful representation
and semantic-obligation contraction. The sparse partial-governance relation
admits D1 and D2 faithful contractions, while the three decisive governance
relations defeat all tested D0-D2 families; their nonrepresentability has
decoder insufficiency as the only unavoidable family-level failure locus.
Governance provenance, anti-scaffold burden accounting, and downstream
authorization boundaries remain preserved.
}}
\]

This is a finite actual application result.

It is not a universal theorem about scalar decision substrates.

---

## 13. Stop condition

The execution stops here.

It does not:

```text
define D4
redesign D1 or D2
choose a scalar family as authoritative
merge governance contracts
define Q_extension
define reward or utility
rank candidates
select a candidate
adopt
authorize
bind
execute
update the dependency ledger
```
