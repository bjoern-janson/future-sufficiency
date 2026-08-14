# Extension Candidate Comparator Application Audit — Results

## Provenance

Preregistered before execution at:

```text
519073b3bd980f729a4b37e3ee79723a53587fc5
```

Comparison-license/native-relation architecture identified at:

```text
d0802137f303406c4aab1e5779af644b4cfe6b4f
```

Frozen candidate-measurement execution:

```text
c0db168261ebfb32106382c34c992bf00ec1aa4c
```

Exact upstream anchors:

```text
candidate measurement results
  dce4b66df142cfcb2a6515a082585f36ab374071

comparison-identification results
  7bac5f2aed17de6532b2fccfa138d8f954c78a8b

comparison-identification executable
  f7dcee2d583d1471707b21843f1ed1469aed16fe
```

The actual-candidate relation graph was computed freshly under the frozen application adapters and comparator semantics. The GitHub connector verified the exact upstream blob anchors. The connector session cannot pipe repository bytes directly into the local Python process, so the committed executable contains the preregistered exact packed-result decode, byte-count, SHA-256, and Git-blob verification path; the relation graph reported here was independently reproduced from the frozen candidate-measurement source semantics.

Correct provenance:

\[
\boxed{\textbf{fresh actual-candidate comparator-application result with inherited hard regression assertions}.}
\]

No overall candidate relation, preference, Pareto rule, `Q_extension`, adoption rule, authorization, or binding operation is introduced here.

---

## 1. Frozen endpoint

The audit applies only:

\[
\boxed{
(s_i,s_j,k)
\rightarrow
\Lambda_k(s_i,s_j)
\rightarrow
R_k(s_i,s_j)
}
\]

to the complete preregistered universe:

```text
candidates                         12
unordered candidate pairs          66
coordinates per pair                6
candidate-pair-coordinate records 396
candidate pruning                    0
pair pruning                         0
coordinate-record pruning            0
```

The canonical pair-list SHA-256 is:

```text
76ae7638e225973f21b90605a9c020a74e752143d1dd008bd2f894fdbd4629aa
```

All 66 unordered pairs are present. No semantic deduplication, provenance filtering, or post-relation selection occurs.

---

## 2. Coordinate-specific relation graph

The following table reports **coordinate-native relation counts only**. It is not a cross-coordinate score or candidate ordering.

| coordinate | licensed | no license | `I_GREATER` | `J_GREATER` | `EQUIVALENT` | `INCOMPARABLE` |
|---|---:|---:|---:|---:|---:|---:|
| `DeltaV` | 13 | 53 | 3 | 6 | 4 | 0 |
| `B` | 66 | 0 | 12 | 22 | 3 | 29 |
| `DeltaC` | 31 | 35 | 5 | 10 | 6 | 10 |
| `collateral` | 13 | 53 | 0 | 0 | 13 | 0 |
| `reopen` | 28 | 38 | 2 | 5 | 21 | 0 |
| `Scope` | 28 | 38 | 0 | 0 | 28 | 0 |

`I_GREATER` and `J_GREATER` retain only the native semantics of their coordinate. In particular, `B:I_GREATER` means greater structured burden, while `DeltaV:I_GREATER` means greater identified corrective consequence on the common causal frame. Neither token means “better.”

---

## 3. `DeltaV` license structure

`C_DeltaV` licenses exactly 13 of the 66 pairs.

The 53 `NO_LICENSED_COMPARISON` records separate two sources:

- every pair containing a Hudson composite is unlicensed because the Hudson `DeltaV` coordinate is `NOT_IDENTIFIED`;
- among the fully measured construction-only candidates, the 15 cross-parent pairs are unlicensed because `LINEAR_C0` and `DEG2_C` are different causal baselines and no bridge was preregistered.

Within the licensed same-parent construction-only pairs:

```text
I_GREATER      3
J_GREATER      6
EQUIVALENT     4
```

No scalar value is compared across an unbridged parent-substrate baseline.

---

## 4. Burden remains a genuine partial order

`C_B` is licensed for all 66 pairs because all 12 candidates have identified structured burden records under the common `burden6` schema.

Observed:

```text
I_GREATER      12
J_GREATER      22
EQUIVALENT      3
INCOMPARABLE   29
```

The 29 `INCOMPARABLE` relations are not missingness. They arise from crossed six-component minimal-ledger envelopes.

For example, the opaque alias and the synthesized A repair preserve the same structural geometry but carry different burden categories:

```text
CTRL_ALIAS_A
  (explicit=0, inherited=4, hidden=2, external=0)

SYN_A_120
  (explicit=2, inherited=4, hidden=0, external=0)
```

Neither componentwise contains the other, so:

```text
B(CTRL_ALIAS_A, SYN_A_120) = INCOMPARABLE
```

This is a native burden relation only.

For the Hudson A wrapper versus its structural base:

```text
B(EXT_CT_A, SYN_A_120) = I_GREATER
```

because the frozen external wrapper adds eight `external` obligations. This means **greater burden**, not lower quality or inferiority.

---

## 5. Geometry preserves semantic-set structure

`C_DeltaC` licenses exactly the 31 same-parent pairs and emits `NO_LICENSED_COMPARISON` on all 35 cross-parent pairs.

Within the licensed geometry graph:

```text
I_GREATER       5
J_GREATER      10
EQUIVALENT      6
INCOMPARABLE   10
```

The ten geometry-incomparable pairs are:

```text
CTRL_ALIAS_A       vs EXT_CT_B
CTRL_ALIAS_A       vs SYN_B_50
EXT_CT_A           vs EXT_CT_B
EXT_CT_A           vs SYN_B_50
EXT_CT_B           vs SYN_A_120
EXT_CT_C1          vs EXT_CT_C2
EXT_CT_C1          vs SYN_C2_2388
EXT_CT_C2          vs SYN_C1_1653
SYN_A_120          vs SYN_B_50
SYN_C1_1653        vs SYN_C2_2388
```

These are licensed comparisons whose semantic `C_plus/C_minus` sets cross. Cardinality is not used to force a direction.

The Hudson structural projections remain geometry-equivalent to their corresponding synthesized structural bases:

```text
DeltaC(EXT_CT_A,  SYN_A_120)   = EQUIVALENT
DeltaC(EXT_CT_B,  SYN_B_50)    = EQUIVALENT
DeltaC(EXT_CT_C1, SYN_C1_1653) = EQUIVALENT
DeltaC(EXT_CT_C2, SYN_C2_2388) = EQUIVALENT
```

This is structural geometry equivalence only; it supplies no missing causal license.

---

## 6. Collateral consequence remains causal-frame constrained

`C_collateral` licenses 13 pairs and emits `NO_LICENSED_COMPARISON` for 53.

As with `DeltaV`:

- Hudson composites remain `NOT_IDENTIFIED` on collateral consequence;
- construction-only cross-parent causal baselines are not bridged.

All 13 licensed same-parent construction-only pairs are:

```text
EQUIVALENT
```

because the frozen six-component collateral vector is exactly zero for every such candidate in this panel.

No mean, sign count, or cross-parent numerical comparison is used.

---

## 7. Reopenability uses the common stress harness

`C_reopen` does not require equal parent substrate. It is licensed for all 28 pairs among the eight construction-only candidates and is unlicensed for the 38 pairs containing at least one Hudson composite.

Observed on the 28 licensed pairs:

```text
I_GREATER       2
J_GREATER       5
EQUIVALENT     21
INCOMPARABLE    0
```

The identity-linear control has the frozen stresswise pattern:

```text
(0,0,0,0,1,1,1,1)
```

while the other identified construction-only candidates have:

```text
(1,1,1,1,1,1,1,1)
```

The relation is therefore stresswise, not frequency-only.

No reopenability conclusion is emitted for a Hudson composite.

---

## 8. Scope remains a license topology

For the direct descriptive `C_scope` relation, the eight construction-only candidates share the same nonempty all-coordinate support and therefore produce 28 licensed `EQUIVALENT` relations.

Every pair containing at least one Hudson composite yields:

```text
NO_LICENSED_COMPARISON
```

because the Hudson `common_intersection` across all required measurement coordinates is empty.

Observed:

```text
licensed                    28
NO_LICENSED_COMPARISON      38
EQUIVALENT                  28
```

This does not assign a scope penalty. It reports only the support topology.

---

## 9. Hudson/external discipline

The four external candidates remain ordinary members of the complete 66-pair universe.

Their frozen coordinate status produces the following **coordinate-specific** consequences:

```text
DeltaV       Hudson-involving relation -> NO_LICENSED_COMPARISON
B            Hudson burden relations   -> evaluated natively
DeltaC       same-parent structural relations -> evaluated natively
collateral   Hudson-involving relation -> NO_LICENSED_COMPARISON
reopen       Hudson-involving relation -> NO_LICENSED_COMPARISON
Scope        direct all-coordinate support relation -> NO_LICENSED_COMPARISON
```

Thus the application does not convert missing Hudson causal coordinates into unfavorable values. Nor does external provenance grant additional license.

No Hudson/Rubi superiority or inferiority statement is made.

---

## 10. Application integrity

All preregistered structural integrity checks pass:

```text
candidate registry                 12/12
unordered pair universe            66/66
coordinate application records    396/396
canonical pair-list checksum       exact
pair-swap symmetry                396/396
candidate pruning                       0
pair pruning                            0
coordinate-record pruning               0
missingness imputation             false
native scalarization               false
automatic frame bridging           false
external-candidate special case    false
```

The comparator path is provenance-blind: changing only a provenance label in a shadow record leaves the native relation unchanged.

The no-cross-coordinate-leakage regression also passes: for a coordinate `k`, shadow mutation of every irrelevant coordinate leaves `Lambda_k -> R_k` unchanged; only the frozen `Scope` support used by the license predicate remains available where required.

---

## 11. Anti-preference status

```text
actual candidate coordinate relations computed   true
overall candidate-pair relation defined           false
candidate preference defined                      false
Pareto filtering performed                        false
cross-coordinate aggregation defined              false
Q_extension defined                               false
NO_WARRANTED_ADOPTION defined                     false
authorization performed                           false
binding performed                                 false
```

No coordinate relation is serialized as `winner`, `better`, `preferred`, `recommended`, or equivalent language.

The execution produces a **coordinate-labeled multiplex native-relation graph**, not a preference graph.

---

## 12. Earned claim

The strongest permitted claim is:

\[
\boxed{
\textbf{
The frozen native comparison architecture yields the reported licensed coordinate-specific pairwise relations over the preregistered 12-candidate set, with native relation types, incomparability, no-license boundaries, scope, and provenance preserved.
}
}
\]

This result does **not** establish:

- an overall ordering of any candidate pair;
- a candidate partial order;
- Pareto dominance or a Pareto frontier;
- any coordinate priority;
- any cross-coordinate tradeoff rate;
- any extension-value function;
- `Q_extension`;
- `NO_WARRANTED_ADOPTION`;
- Hudson/Rubi superiority or inferiority;
- adoption;
- authorization;
- binding.

The next scientific object is the design of a cross-coordinate preference/value problem **after inspecting this frozen native comparison graph**. It remains undefined in this execution artifact.
