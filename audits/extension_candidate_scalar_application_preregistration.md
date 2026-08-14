# Extension Candidate Scalar Application — Preregistration

## Status

This document freezes the **actual-candidate scalar application gate** after successful scalar-sufficiency / decision-substrate identification.

Parent checkpoint:

```text
f10ff41e292ba8d2df26c0468f785d4fb07c2de6
```

Scalar-sufficiency identification preregistration:

```text
d3319438a6c8784d6057ed72033f0dc82631c527
```

Scalar-sufficiency identification execution:

```text
f10ff41e292ba8d2df26c0468f785d4fb07c2de6
```

Exact scalar-sufficiency preregistration blob:

```text
4ebfd307e990710142bec0d732a0056d388e3c2d
```

Exact scalar-sufficiency executable blob:

```text
8548875bd88eb0c92a18c3cd4229486ea800816e
```

Exact scalar-sufficiency result blob:

```text
98a5db5311f18efa0f84e0fb1d99ef77574d8a91
```

Exact scalar-sufficiency result-note blob:

```text
e35f58ef45903ffba266a52627c59138f14881a6
```

Actual-candidate preference-application preregistration:

```text
f64dd1d3e222b9ca13903facc8fd1e727adb2fd7
```

Actual-candidate preference-application execution:

```text
97c0b092932b2931a74af47a7761a6aa93272c23
```

Exact actual-candidate preference-application executable blob:

```text
b568d90be09bcfa23b4a67ebbdeb90be64bce02f
```

Exact actual-candidate preference-application result blob:

```text
7efc07e54de9b7e4719caee632daecab32e56f1f
```

Exact actual-candidate preference-application result-note blob:

```text
26c5bebb205e320df8bb8c40f60a393ccf542455
```

The only new object frozen here is:

\[
\boxed{
(R_{\rm pref}^{G,\rm actual},D_j)
\longrightarrow
\left(
D_{\rm scalar}^{G,j},
B_{D_j},
F_{\rm scalar}^{G,j}
\right)
}
\]

for each of the four already-frozen supplied governance contracts `G` and each already-identified admissible scalar family

```text
D0
D1
D2
```

with `W_LOOKUP` retained as the preregistered representability/non-contraction control and `D3` retained as the native typed-relation baseline.

This gate is **application, not redesign**.

It introduces no new scalar family, no new threshold type, no new band policy, no new score precision, no pair-specific exception mechanism, no governance revision, and no downstream authorization semantics.

---

# 1. Scientific question

The preceding scalar-identification gate established that scalar sufficiency is relation- and decoder-family-dependent:

\[
\boxed{
\text{typed decision relation}
\not\Rightarrow
\text{scalar impossibility}
}
\]

and:

\[
\boxed{
\text{scalar representation}
\not\Rightarrow
\text{scalar sufficiency/contraction}.
}
\]

It also separated three diagnoses:

```text
FAITHFUL_CONTRACTION
REPRESENTABLE_NO_CONTRACTION
NOT_REPRESENTABLE
```

and demonstrated that unrestricted lookup can represent a finite typed relation while failing to contract it.

The present question is strictly:

\[
\boxed{
\textbf{
For each frozen actual governance-relative preference graph over the 12 frozen candidates, which of the already-identified scalar families D0-D2 faithfully represents the graph, which contracts it under the already-frozen burden ledger, and where does any failure occur?
}
}
\]

This gate does not ask whether a richer scalar family could work.

It does not ask which governance contract is normatively correct.

It does not ask which candidate should be adopted.

---

# 2. Former holdout becomes immutable application input

During scalar-sufficiency identification, the actual preference graph was a strict holdout and was not decoded or used to tune the scalar families.

That historical boundary remains fixed.

This gate is the first permitted scalar-stage application to:

```text
audits/extension_candidate_preference_application_results.json
```

with exact frozen blob:

```text
7efc07e54de9b7e4719caee632daecab32e56f1f
```

The child execution may decode that file only as the immutable target relation.

It may not use any observed graph topology to alter:

```text
D0 semantics
D1 semantics
D2 semantics
score domain
threshold/cutpoint domain
band-policy domain
burden formulas
outcome vocabulary
failure-locus vocabulary
canonical witness rule
search completeness requirement
broken controls
```

Thus:

\[
\boxed{
R_{\rm pref}^{G,\rm actual}
\longrightarrow
D_{\rm scalar}^{G,j}
}
\]

is permitted, while:

\[
\boxed{
R_{\rm pref}^{G,\rm actual}
\not\longrightarrow
\text{decoder redesign}.
}
\]

Any surprising result must be reported as-is.

---

# 3. Frozen candidate universe

The candidate universe remains exactly:

```text
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
```

No candidate may be added, deleted, merged, pruned, aliased, or deduplicated before scalar application.

Provenance remains lineage metadata only:

```text
CONTROL       4
EXTERNAL      4
SYNTHESIZED   4
TOTAL        12
```

Candidate provenance, display spelling, lexical position, and implementation handle have no scalar authority.

---

# 4. Frozen pair universe

Let `IDS` be the lexicographically sorted vector of the 12 candidate IDs above.

The unordered canonical pair universe remains:

```python
pairs = list(itertools.combinations(IDS, 2))
```

Therefore:

\[
\boxed{
|\mathfrak P_{\rm actual}|=\binom{12}{2}=66.
}
\]

The inherited compact-JSON canonical pair-list SHA-256 remains:

```text
76ae7638e225973f21b90605a9c020a74e752143d1dd008bd2f894fdbd4629aa
```

All 66 pair obligations are present under every governance contract.

No pair may be dropped because it is `NO_WARRANTED_PREFERENCE`, contains an external candidate, appears redundant, or conflicts with scalar structure.

---

# 5. Frozen governance-contract universe

Exactly four supplied governance contracts are application environments:

```text
G_PARTIAL_EMPTY
G_CONSTRAINT_B
G_LEX_DV_REOPEN_B
G_COMP_EXPLICIT
```

No fifth contract may be introduced and none may be omitted.

The scalar object remains governance-relative:

\[
\boxed{
Q_{\rm extension}^{G}
}
\]

not an unqualified governance-free scalar.

The child may find different representability or witness structure under different governance contracts.

It may not interpret lower scalar burden or greater scalarizability as evidence that one governance contract is better.

---

# 6. Frozen actual target relations

For each governance contract `G`, the target is the complete 66-edge typed candidate preference relation:

\[
\boxed{
R_{\rm pref}^{G,\rm actual}:\mathfrak P_{\rm actual}\rightarrow\Sigma_P
}
\]

with exact alphabet:

```text
PREFER_I
PREFER_J
EQUIVALENT
NO_WARRANTED_PREFERENCE
```

`NO_WARRANTED_PREFERENCE` remains an explicit typed decision state.

It is not missingness, zero, equivalence, or an invitation to force a direction.

The already-executed target-count integrity checks are frozen as:

| governance | PREFER_I | PREFER_J | EQUIVALENT | NO_WARRANTED_PREFERENCE | total |
|---|---:|---:|---:|---:|---:|
| `G_PARTIAL_EMPTY` | 0 | 0 | 1 | 65 | 66 |
| `G_CONSTRAINT_B` | 5 | 3 | 1 | 57 | 66 |
| `G_LEX_DV_REOPEN_B` | 3 | 5 | 1 | 57 | 66 |
| `G_COMP_EXPLICIT` | 3 | 5 | 1 | 57 | 66 |

These counts are integrity anchors, not sufficient statistics for scalarization.

The child must recover the full 66-edge relation for each `G` from the exact upstream result and verify the counts above before scalar search.

---

# 7. Scalar representation condition

For each governance contract `G` and scalar family `D_j`, a candidate scalar substrate has the already-frozen type:

\[
\boxed{
Q^{G,j}=(q_{G,j},g_j,a_{G,j}).
}
\]

Exact representation requires:

\[
\boxed{
\forall i\neq j:\quad
R_{\rm pref}^{G,\rm actual}(i,j)
=
g_j(q_{G,j}(i),q_{G,j}(j);a_{G,j}).
}
\]

Every one of the 66 canonical pair outputs must match exactly.

Directional edges alone are insufficient.

`EQUIVALENT` and `NO_WARRANTED_PREFERENCE` must be reproduced exactly where present.

---

# 8. Frozen score domain

For the actual 12-candidate universe, every admissible scalar family uses the inherited bounded integer domain:

\[
\boxed{
q(s)\in\{0,1,\ldots,13\}.
}
\]

Canonical translation normalization remains:

```text
min_s q(s) = 0
```

Forbidden:

```text
floating epsilon encoding
irrational encoding
arbitrary precision decimals
large integer codebooks
candidate-ID encoding
pair-index encoding
hash-derived scores
provenance-derived scores
serialization-position scores
```

A heuristic failure to find a scalar is not evidence of `NOT_REPRESENTABLE`.

---

# 9. Frozen admissible scalar families

No family semantics may change during execution.

## D0 — ordinary ordered scalar

```text
q_i > q_j  -> PREFER_I
q_i < q_j  -> PREFER_J
q_i = q_j  -> EQUIVALENT
```

`NO_WARRANTED_PREFERENCE` is unreachable.

No abstention parameter exists.

## D1 — scalar + one global abstention radius

For:

```text
tau in {0,...,13}
d = q_i - q_j
```

use exactly:

```text
d = 0                 -> EQUIVALENT
0 < |d| <= tau        -> NO_WARRANTED_PREFERENCE
d > tau               -> PREFER_I
d < -tau              -> PREFER_J
```

The threshold is global for the governance-conditioned graph.

No candidate-specific or pair-specific threshold is allowed.

## D2 — scalar + restricted two-cut typed decoder

Use exactly:

```text
0 <= tau_1 <= tau_2 <= 13
```

with nonzero magnitude bands:

```text
B1: 0 < |d| <= tau_1
B2: tau_1 < |d| <= tau_2
B3: |d| > tau_2
```

Each band receives exactly one global policy:

```text
DIRECTION
NO_WARRANTED_PREFERENCE
```

There are exactly eight band-policy triples.

Zero difference always maps to:

```text
EQUIVALENT
```

A `DIRECTION` band orients only by sign:

```text
d > 0 -> PREFER_I
d < 0 -> PREFER_J
```

No exception table, candidate identity, provenance field, governance display name, pair identity, or hidden branch is admissible.

## D3 — native typed-relation baseline

D3 remains:

```text
one typed relation token per canonical unordered pair
```

It is not a scalar family and may not be described as scalarization.

## W_LOOKUP — unrestricted pair lookup control

`W_LOOKUP` stores the pair relation directly:

```text
(candidate_i, candidate_j) -> target preference token
```

It must represent every actual governance graph exactly.

It is never eligible for contraction.

---

# 10. Frozen burden architecture

The inherited anti-scaffold question remains:

\[
\boxed{\textbf{Where did the decision complexity go?}}
\]

Common inherited structure is excluded symmetrically:

```text
candidate registry
canonical pair enumeration rule
four-token vocabulary
pair-swap semantics
governance-condition identity
```

Only representation-specific semantic obligations are counted.

For `n=12`:

\[
\boxed{
B_{R_{\rm pref}}=\binom{12}{2}=66.
}
\]

The scalar burdens are frozen before execution:

### D0

```text
B_q            = 12
B_g            = 3
B_auxiliary    = 0
B_D0           = 15
```

### D1

```text
B_q            = 12
B_g            = 4
B_auxiliary    = 1
B_D1           = 17
```

### D2

```text
B_q            = 12
B_g            = 5
B_auxiliary    = 2
B_D2           = 19
```

### D3

```text
B_D3           = 66
```

### W_LOOKUP

```text
B_q            = 0
B_g            = 1
B_auxiliary    = 66
B_LOOKUP       = 67
```

Therefore, under the frozen ledger:

\[
\boxed{
D_0,D_1,D_2\text{ exact representability}
\Rightarrow
\texttt{FAITHFUL\_CONTRACTION}
}
\]

for this 12-candidate application, because:

```text
15 < 66
17 < 66
19 < 66
```

`REPRESENTABLE_NO_CONTRACTION` remains part of the general outcome vocabulary, but for D0-D2 it can occur only if execution discovers admissible representation-specific burden that the preregistered ledger requires counting and that was not already included above. Such a discovery must be reported as an accounting failure or preregistration violation, not silently ignored.

`W_LOOKUP` is the positive control expected to occupy the representable/non-contracting regime:

```text
67 > 66
```

---

# 11. Frozen outcome vocabulary

For every `(G,D_j)` application emit exactly one:

```text
FAITHFUL_CONTRACTION
REPRESENTABLE_NO_CONTRACTION
NOT_REPRESENTABLE
```

Definitions remain:

### `FAITHFUL_CONTRACTION`

```text
exact typed relation recovered
zero unauthorized scalar-ordering mismatches
B_scalar < B_Rpref
```

### `REPRESENTABLE_NO_CONTRACTION`

```text
exact typed relation recovered
zero unauthorized scalar-ordering mismatches
B_scalar >= B_Rpref
```

### `NOT_REPRESENTABLE`

```text
no member of the complete preregistered finite family reproduces the full 66-edge target relation exactly
```

For each governance contract a descriptive summary may additionally emit:

```text
NO_SUPPORTED_CONTRACTION
```

iff all of D0, D1, and D2 are `NOT_REPRESENTABLE` or otherwise fail to qualify as faithful contractions.

This means only no supported contraction in the tested frozen families.

It does not establish global minimality of the native typed relation.

---

# 12. Required output tuple

For each governance contract `G` and each scalar family `D_j`, the primary output is exactly:

\[
\boxed{
\left(
\text{status},
B_{D_j},
\text{failure\_locus}
\right).
}
\]

`failure_locus` is **set-valued** to avoid forcing a false single-cause explanation when more than one obstruction is certified.

Allowed members are exactly:

```text
AUTHORIZED_DISTINCTION_LOSS
UNAUTHORIZED_SCALAR_ORDERING
DECODER_INSUFFICIENCY
BURDEN_NON_CONTRACTION
```

A successful faithful contraction has:

```text
failure_locus = []
```

A faithful but non-contracting representation has:

```text
failure_locus = [BURDEN_NON_CONTRACTION]
```

A `NOT_REPRESENTABLE` result must include:

```text
DECODER_INSUFFICIENCY
```

plus any independently certified unavoidable mismatch class described below.

No candidate-level, governance-level, or downstream authorization meaning attaches to `failure_locus`.

---

# 13. Preservation diagnostics

The child must preserve the reason for failure rather than reporting only a terminal label.

## 13.1 Authorized distinction loss

Count a target distinction loss whenever the scalar decoder fails to preserve an authorized target state without creating a directional scalar authority injection.

At minimum:

```text
PREFER_I/J -> EQUIVALENT
PREFER_I/J -> NO_WARRANTED_PREFERENCE
EQUIVALENT -> NO_WARRANTED_PREFERENCE
NO_WARRANTED_PREFERENCE -> EQUIVALENT
```

are distinction-loss mismatches.

Opposite-direction errors are handled under unauthorized scalar ordering and may also be recorded as loss of the target direction in the detailed mismatch ledger.

## 13.2 Unauthorized scalar ordering

Count scalar authority injection whenever decoded scalar structure creates or reverses directional authority not present in the target:

```text
NO_WARRANTED_PREFERENCE -> PREFER_I/J
EQUIVALENT              -> PREFER_I/J
PREFER_I                 -> PREFER_J
PREFER_J                 -> PREFER_I
```

## 13.3 Decoder insufficiency

`DECODER_INSUFFICIENCY` means exhaustive exact search proves that no member of the frozen scalar family reproduces all 66 target edges.

It does not mean all scalar families are impossible.

It does not license adding a threshold, changing the score domain, or redesigning a decoder inside this gate.

## 13.4 Burden non-contraction

`BURDEN_NON_CONTRACTION` applies only when an exact faithful representation exists but its full counted semantic burden is not strictly lower than 66.

The lookup control must instantiate this locus.

---

# 14. Unavoidable-failure certification

For a nonrepresentable `(G,D_j)` result, do not choose an arbitrary failed scalar witness and call its mismatch pattern the cause.

Across the complete finite family or an exactly equivalent complete constraint proof, compute the following descriptive certificates:

```text
exact_representation_exists
loss_free_member_exists
injection_free_member_exists
min_total_mismatches
min_authorized_distinction_loss_mismatches
min_unauthorized_scalar_ordering_mismatches
```

Then:

```text
AUTHORIZED_DISTINCTION_LOSS
```

is added to `failure_locus` only if:

```text
loss_free_member_exists = false
```

and:

```text
UNAUTHORIZED_SCALAR_ORDERING
```

is added only if:

```text
injection_free_member_exists = false
```

This permits a legitimate result such as:

```text
failure_locus = [DECODER_INSUFFICIENCY]
```

when loss-free and injection-free family members each exist separately but no single family member satisfies both simultaneously.

No arbitrary precedence among failure reasons is permitted.

---

# 15. Exact search / proof requirement

`NOT_REPRESENTABLE` requires complete finite-family adjudication.

Because the actual universe has 12 candidates, naive enumeration of all score vectors is not required if an exactly equivalent complete constraint procedure is used.

The execution must use either:

1. complete enumeration of the frozen finite family; or
2. exact finite-domain constraint/backtracking search with only sound pruning rules that preserve completeness.

For every branch pruned, the implementation must be able to state the violated frozen decoder constraint that makes all descendants impossible.

Heuristic optimization, stochastic search, local search, gradient fitting, or timeout-based failure may not support `NOT_REPRESENTABLE`.

The exact finite domains remain:

```text
q_i        in {0,...,13}
min(q)     = 0
D1 tau     in {0,...,13}
D2 tau_1   in {0,...,13}
D2 tau_2   in {tau_1,...,13}
D2 policy  in {DIRECTION,NWP}^3
```

For D0, an exact algebraic total-preorder test is permitted as an equivalent completeness proof if it verifies the same decoder semantics.

For D1/D2, exact finite-domain CSP/backtracking certificates are permitted.

---

# 16. Canonical witness rule

If a family is representable, witness choice is descriptive and must not affect status.

Choose the canonical witness by:

1. minimum counted `B_scalar` within the frozen family schema;
2. lexicographically smallest normalized `q` vector in canonical candidate order;
3. lexicographically smallest decoder-parameter tuple.

Because burden is fixed within each family, step 1 normally ties.

For D2, decoder-parameter lexicographic order is frozen as:

```text
(tau_1, tau_2, B1_policy, B2_policy, B3_policy)
```

with:

```text
DIRECTION < NO_WARRANTED_PREFERENCE
```

for canonical serialization only.

Canonical witness selection is not a preference over candidates or governance contracts.

---

# 17. Governance dependence is preserved

Each governance contract is adjudicated independently:

\[
\boxed{
D_j(G_a)
\text{ may differ from }
D_j(G_b).
}
\]

Likewise:

\[
\boxed{
q_{G_a,j}
\text{ may differ from }
q_{G_b,j}.
}
\]

No execution result may force:

```text
q_G_PARTIAL_EMPTY
=
q_G_CONSTRAINT_B
=
q_G_LEX_DV_REOPEN_B
=
q_G_COMP_EXPLICIT
```

or any analogous decoder-parameter equality.

The gate therefore tests scalarizability as a property of the governance-relative typed relation, not of the bare candidate set alone.

The allowed interpretation is:

\[
\boxed{
\text{scalarizability is assessed on }R_{\rm pref}^{G,\rm actual}.
}
\]

The execution must not simplify this to a governance-free candidate score.

---

# 18. Governance-free reuse broken control

Define broken control:

```text
W_GOVERNANCE_FREE_REUSE
```

which demands one identical complete scalar substrate:

```text
(q, g, a)
```

across all four governance contracts.

Because the target governance relations are not identical, this control must not be allowed to overwrite contract-specific targets.

If one shared substrate fails, classify only the control as a governance-typing failure.

If an implementation accidentally reports success by dropping contract identity or merging conflicting target edges, the gate fails.

This control does not test whether some lower-level candidate coordinate could be shared while decoders remain governance-specific; that is outside scope.

---

# 19. Known structural consequence versus open application result

The target integrity counts already contain `NO_WARRANTED_PREFERENCE` under all four governance contracts.

Since D0 cannot emit that token, the following is a direct logical consequence of the already-frozen D0 semantics and upstream target counts:

```text
D0 cannot exactly represent any of the four actual governance graphs.
```

This is not a new empirical discovery and must not be presented as one.

It is an input-level structural consequence.

The open application questions concern the richer frozen D1 and D2 families, their exact witnesses or impossibility certificates, and the full failure diagnostics.

No D1 or D2 outcome is preregistered here.

---

# 20. Nuisance invariance

The canonical application is performed on the frozen actual candidate IDs, but scalar authority must be invariant to non-authoritative nuisance relabeling.

Construct 64 deterministic anonymous encodings preserving:

```text
candidate role identity under a permutation map
governance semantic identity
full target edge relation
pair-swap semantics
```

while varying:

```text
candidate handles
governance display aliases
serialization order
opaque nonce
implementation tag
```

Required:

```text
status unchanged 64/64
burden unchanged 64/64
failure_locus unchanged 64/64
```

For successful representations, the canonical witness must transport exactly under the candidate permutation.

For nonrepresentable cases, full re-solving under every relabeling is not required: candidate relabeling is a bijection on the finite scalar family, so the canonical exact impossibility certificate may be transported, with spot-check execution permitted for regression testing.

No candidate spelling, provenance, nonce, or serialization position may alter scalar authority.

---

# 21. Pair-swap symmetry

For every governance graph and every successful scalar representation:

```text
PREFER_I                 <-> PREFER_J
PREFER_J                 <-> PREFER_I
EQUIVALENT                 -> EQUIVALENT
NO_WARRANTED_PREFERENCE    -> NO_WARRANTED_PREFERENCE
```

must hold under pair reversal.

The target and decoded relation must agree under both canonical and swapped orientation.

A scalar implementation that depends on canonical lexical order rather than scalar sign fails this gate.

---

# 22. Broken controls / forbidden shortcuts

The execution must explicitly reject or detect the following.

## W1 — redesign after seeing actual graph

Add a threshold, new band, pair exception, or wider score domain because D1/D2 fail.

Failure type:

```text
application-to-calibration leakage
```

## W2 — NWP collapsed to equivalence

Map target `NO_WARRANTED_PREFERENCE` to scalar equality.

Failure type:

```text
authorized distinction loss
```

## W3 — NWP forced directional

Use candidate ID, lexical order, provenance, or arbitrary tie-breaking to orient target abstention.

Failure type:

```text
unauthorized scalar ordering
```

## W4 — hidden pair exception table

Permit per-pair thresholds or exceptions while counting only the visible scalar.

Failure type:

```text
anti-scaffold burden violation
```

## W5 — lookup called contraction

Omit the 66 pair entries from `W_LOOKUP` burden.

Failure type:

```text
false contraction
```

## W6 — decoder burden omitted

Count only 12 candidate scores and omit thresholds, cutpoints, policies, or branch semantics.

Failure type:

```text
anti-scaffold accounting failure
```

## W7 — governance erased

Require one scalar substrate to stand in for conflicting governance-relative target relations without preserving `G`.

Failure type:

```text
governance typing collapse
```

## W8 — heuristic nonrepresentability

Stop a search after timeout or failure to find a witness and report `NOT_REPRESENTABLE`.

Failure type:

```text
incomplete adjudication
```

## W9 — nuisance encoded in q

Use candidate handles, provenance labels, nonce, hash order, or serialization position to construct scalar values.

Failure type:

```text
authority injection
```

## W10 — scalar status becomes governance quality

Infer that a governance contract is better because it scalarizes more easily or with a simpler family.

Failure type:

```text
normative authority leakage
```

## W11 — scalar preference becomes authorization

Use a faithful scalar witness to adopt, authorize, bind, execute, or reward a candidate.

Failure type:

```text
downstream authority leakage
```

## W12 — candidate ranking inferred from partial typed relation

Publish a total leaderboard or global ranking not licensed by the target graph and decoder semantics.

Failure type:

```text
unlicensed decision completion
```

---

# 23. Application success criteria

The gate passes only if all of the following hold:

1. exact upstream scalar-identification and preference-application blob anchors are verified;
2. the 12-candidate universe is unchanged;
3. the 66-pair canonical universe is unchanged;
4. all four governance contracts are present and separately typed;
5. each target graph contains exactly 66 typed pair records;
6. target token counts match the frozen integrity table;
7. D0/D1/D2 semantics match the scalar-identification preregistration exactly;
8. the score domain remains `0..13` with `min(q)=0` normalization;
9. no new decoder family or exception mechanism is introduced;
10. every successful representation reproduces all 66 target pair states exactly;
11. every `NOT_REPRESENTABLE` result is backed by complete exact finite-family adjudication or an exactly equivalent proof procedure;
12. `EQUIVALENT` and `NO_WARRANTED_PREFERENCE` remain distinct;
13. unauthorized scalar ordering is counted explicitly;
14. authorized distinction loss is counted explicitly;
15. burden is reported as `B_q + B_g + B_auxiliary` with the frozen formulas;
16. every D0-D2 exact representation satisfies the frozen contraction inequality before receiving `FAITHFUL_CONTRACTION`;
17. `W_LOOKUP` represents every governance graph and is never labeled a contraction;
18. `failure_locus` follows the set-valued rules above and is not chosen by arbitrary precedence;
19. pair-swap symmetry is exact;
20. nuisance invariance holds under all 64 encodings;
21. governance-free reuse does not overwrite contract-relative targets;
22. no governance contract is ranked or normatively selected;
23. no global candidate ranking is introduced beyond the exact decoder semantics;
24. no utility, reward, adoption, authorization, binding, or execution semantics are introduced.

A partial pass does not license authorization or binding.

---

# 24. Required result serialization

The result JSON must include at minimum:

```text
preregistration_commit
parent_checkpoint
upstream_blob_anchors
candidate_registry
pair_registry
governance_registry
target_relation_integrity
scalar_family_registry
score_domain
burden_schema
governance_x_family_diagnoses
successful_scalar_witnesses
nonrepresentability_certificates
failure_locus_certificates
pair_swap_results
nuisance_invariance_results
broken_control_results
anti_downstream_flags
gate_pass
```

For every `(G,D_j)` pair serialize at minimum:

```text
governance_id
scalar_family_id
status
failure_locus
exact_relation_match
B_q
B_g
B_auxiliary
B_scalar
B_Rpref
canonical_q
canonical_decoder_parameters
loss_free_member_exists
injection_free_member_exists
min_total_mismatches
min_authorized_distinction_loss_mismatches
min_unauthorized_scalar_ordering_mismatches
complete_family_adjudicated
adjudication_method
```

For `NOT_REPRESENTABLE`, canonical scalar fields may be null, but the exact proof/exhaustion certificate must be present.

For successful D0-D2 cases, the full target and decoded 66-edge relations must be retained losslessly in the machine payload.

---

# 25. Required execution artifacts

A later authorized execution must add exactly three scientific artifacts:

```text
audits/extension_candidate_scalar_application_audit.py
audits/extension_candidate_scalar_application_results.json
audits/extension_candidate_scalar_application_audit.md
```

No dependency ledger, evidence matrix, README, governance contract, candidate measurement, comparison graph, preference graph, or scalar-identification artifact may be modified in the same execution commit.

The execution commit should use provenance wording equivalent to:

\[
\boxed{\textbf{
fresh actual-candidate scalar-application result with frozen scalar-family semantics, frozen governance-relative preference targets, exact finite-family adjudication, and hard anti-scaffold regression assertions.
}}
\]

---

# 26. Anti-downstream flags

The child execution must hard-assert:

```text
scalar_sufficiency_identification_performed = true
actual_candidate_scalar_application_performed = true
actual_Q_extension_defined = false
governance_contract_selected = false
candidate_adoption_selected = false
candidate_ranking_performed = false
utility_defined = false
reward_defined = false
NO_WARRANTED_ADOPTION_defined = false
adoption_performed = false
authorization_performed = false
binding_performed = false
execution_performed = false
```

A successful scalar witness may be serialized as an **application-stage decision representation** for its governance contract.

It is not yet an authorized `Q_extension` with downstream action semantics.

---

# 27. Interpretation boundary

Allowed claims after successful execution include:

> Under supplied governance contract `G`, frozen scalar family `D_j` does or does not faithfully represent the complete actual 12-candidate typed preference relation under the preregistered decoder and finite score domain.

> Where exact representation exists, the frozen semantic-obligation ledger determines whether that representation is a contraction relative to the native 66-edge typed relation.

> Different supplied governance contracts may have different scalar-family sufficiency status or different scalar witnesses, so scalarization is governance-relative in this audited application.

Forbidden claims include:

```text
scalarization is universally possible
scalarization is universally impossible
the native typed relation is globally minimal
a scalar witness is a reward
a scalar witness is a utility function
a scalar witness selects the correct governance contract
lower scalar burden makes governance normatively better
scalar representability authorizes adoption
scalar nonrepresentability rejects a candidate
```

---

# 28. Strongest permitted earned endpoint

If the gate passes, the strongest admissible project-level statement is:

\[
\boxed{\textbf{
For the frozen 12-candidate extension set and four supplied governance-relative preference relations, the already-identified D0-D2 scalar families have been applied without redesign and adjudicated exactly for faithful representation and semantic-obligation contraction; failures retain typed distinction-loss, authority-injection, decoder-insufficiency, and burden loci, while governance provenance and downstream authorization boundaries remain preserved.
}}
\]

This is an actual finite application result.

It is not a universal theorem about scalar decision substrates.

---

# 29. Stop condition

After producing the exact `(status, burden, failure_locus)` matrix and all required controls, stop.

Do **not** in the same execution:

```text
define a richer D4 family
choose the least-complex successful family as authoritative
merge governance contracts
construct a universal governance-free scalar
promote a scalar to reward or utility
select a candidate
rank the 12 candidates globally
adopt an extension
authorize an extension
bind an extension
execute an extension
update the dependency ledger
```

Any such step is a new scientific object and requires a new preregistration.
