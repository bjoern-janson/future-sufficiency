# Decision-Substrate Language Identification — Round v1 Actual-Application Preregistration

## Status

```text
ACTUAL_APPLICATION_PREREGISTERED
```

This is the final design artifact of `DSLI_R1`.

It freezes only the application of the already-carried-forward round-v1 treatment family to the already-existing four actual governance-relative preference relations. It does not alter any treatment language, governance contract, authority rule, burden rule, closure rule, target relation, or application-set membership.

After this preregistration the only licensed v1 scientific transition is:

\[
\boxed{
\text{execute actual application}
\rightarrow
\texttt{POST_SPECIFICATION_APPLICATION_EVIDENCE}
\rightarrow
\textbf{STOP v1}.
}
\]

No further v1 architecture/design revision is licensed.

---

# 1. Scientific lineage

```text
characterization_anchor
  ddffe4b976352b3fec4efc3300a0dcc0097ca217

application_set_freeze
  f0c594bc9ed70856ec980a06926275584db79086

round_v1_construction
  6482667d3b48c2e0c47bfea2fb44da92187b0511

round_v1_speccomplete
  0f2e2e9cf38258b583dc3d7f9bbbf2cd047fcf53
```

The Git parent of this preregistration is repository history. The scientific anchors above define the experimental lineage.

The application-set freeze is binding:

\[
\boxed{
\mathfrak L_{\rm app}^{(1)}
=
\mathfrak L_{\rm DS}^{(1)}.
}
\]

Characterization output has no path to application membership, weighting, priority, semantics, or ranking.

---

# 2. Exact application endpoint

For every frozen actual governance-relative target relation and every carried-forward treatment language, execute exactly:

\[
\boxed{
R_{\rm actual}^{G}
\longrightarrow
S(R_{\rm actual}^{G},L;A_{\rm DS}^{(1)},B_{\rm DS}^{(1)}).
}
\]

The primary application universe is the Cartesian product:

```text
4 governance-relative actual relations
x
6 treatment languages
=
24 primary application cells
```

No cell may be pruned, skipped, weighted, prioritized, or duplicated because of characterization or application outcomes.

---

# 3. Frozen actual-target source and graph anchors

The actual targets are the already-existing candidate-level preference relations produced by the frozen preference-application execution:

```text
actual_preference_application_commit
  97c0b092932b2931a74af47a7761a6aa93272c23

actual_preference_application_executable_blob
  b568d90be09bcfa23b4a67ebbdeb90be64bce02f

actual_preference_application_result_blob
  7efc07e54de9b7e4719caee632daecab32e56f1f

actual_preference_application_audit_blob
  26c5bebb205e320df8bb8c40f60a393ccf542455
```

The upstream graph/governance anchors used by that frozen application remain:

```text
actual_candidate_native_comparison_result_blob
  3e332072502fa64c432b143e6d157fc1f5cd18b8

preference_identification_executable_blob
  b47c0884dcb7769a2ca9b934e8a9b64dad218399

preference_identification_result_blob
  4fab22d2a7be25b001b679fe92e67187098ce696

canonical_pair_list_sha256
  76ae7638e225973f21b90605a9c020a74e752143d1dd008bd2f894fdbd4629aa
```

No target graph is regenerated from candidate measurements or comparison logic in this application. The exact preference-application result blob is the source of truth.

## 3.1 Target extraction contract

Execution must:

1. verify the exact Git blob SHA of `audits/extension_candidate_preference_application_results.json`;
2. losslessly decode its packed `application_records` using the already-frozen `lossless-lzma-base64-json-v1` format;
3. verify 12 candidates, 66 canonical unordered pairs, four governance contracts, and 264 preference-application records;
4. verify the canonical pair-list SHA-256 above;
5. for each governance contract, select exactly its 66 records and use only `preference_status` as the target decision token;
6. map the frozen candidate registry to anonymous handles `0..11` in the frozen registry order;
7. serialize each resulting 66-token anonymous target relation canonically and record its SHA-256 in the application result.

Candidate ID, provenance, display alias, governance display name, warrant text, and failure-locus metadata are ingestion/provenance fields only. They are not decoder-visible language inputs.

---

# 4. Frozen governance-relative target set

The four target relations are identified only by the exact frozen governance-contract machine IDs:

```text
G_PARTIAL_EMPTY
G_CONSTRAINT_B
G_LEX_DV_REOPEN_B
G_COMP_EXPLICIT
```

All four are application targets.

No governance contract is selected, ranked, averaged, merged, voted over, or treated as authoritative over the others by this application.

Cross-governance disagreement is preserved as provenance, not resolved.

---

# 5. Exact six-language application set

The treatment family is exactly:

```text
L_ORD1
L_RADIUS1
L_BANDS1
L_INTERSECT2
L_POSET
L_SPARSE_LINEAR
```

Equivalently:

\[
\forall L:\quad
L\in\mathfrak L_{\rm app}^{(1)}
\iff
L\in\mathfrak L_{\rm DS}^{(1)}.
\]

No control language is a primary treatment cell.

No treatment may be added, removed, widened, narrowed, repaired, retuned, or conditionally activated after this preregistration.

---

# 6. Frozen round-v1 semantic bundle

The application uses the already-frozen DSLI_R1 semantics without modification.

Binding bundle anchors:

```text
specification.md blob
  9f3ab86278d8ed9e2c15f2ee24fe3f05a8def556
  sha256 d3913e6082ace84e8b6f7f511d35012a5e80ad554e1bc5f9a2575d1c7c7f1148

specification.json blob
  fadf2241923ba6ae2e14d3c2bb5c42b8276f31f6
  sha256 8793022b6aab79f754153631dacb99b9ce9655285e63a101613540b35a802bf2

reference.py blob
  a0938d91fb13fccc7d3865e8ee98e8ed449f91d5
  sha256 d3d1a85a4ba614931b2194549e94187d09368799940e148a702c9b960a57fe24

construction_bundle_map_sha256
  b6f7e9c42db1ee9f607e56ce9a47ab866090219f9c2b562911c81826976ffde8
```

The application executor may optimize implementation strategy only by exact semantics-preserving constraint pruning or lazy enumeration. It may not alter the witness domain, decoder, authority regime, burden formula, closure predicate, minimum criterion, or terminal classifier.

---

# 7. Frozen authority regime `A_DS^(1)`

Licensed common infrastructure remains exactly:

```text
anonymous candidate handles
canonical unordered-pair addressing
```

Licensed-and-counted state remains only the language-declared fields:

```text
scalar scores
thresholds/cutpoints
band policies
partition merges
order ranks
cover edges
sparse direct edges
```

Forbidden decoder-visible channels remain:

```text
semantic candidate identity
candidate provenance
display aliases
candidate hashes/nonces
serialization position
implementation tags
actual-target lookup
actual-target mismatch features
```

Not available to treatment decoders:

```text
upstream measurement state
upstream comparison state
upstream preference artifacts
network state
current time
learned/adaptive state
```

The application evaluator necessarily reads the target relation to adjudicate closure. The treatment witness/decoder may not use target lookup as representational state.

Every legal round-v1 treatment witness remains authority-admissible. A primary treatment cell that would require authority-invalid state is a specification/conformance failure and must not be silently converted into an empirical success.

---

# 8. Frozen burden regime `B_DS^(1)`

For the actual application:

```text
n   = 12
B_R = C(12,2) = 66
```

The burden decomposition remains:

\[
B(h)=B_{\rm state}+B_{\rm decoder}+B_{\rm auxiliary}+B_{\rm selector}+B_{\rm exception}.
\]

Language-specific formulas are unchanged:

```text
L_ORD1          B = n + 3
L_RADIUS1       B = n + 5
L_BANDS1        B = n + 7
L_INTERSECT2    B = n + c + 5
L_POSET         B = (n-c) + |E_cover| + 5
L_SPARSE_LINEAR B = (n-c) + |E_direct| + 5
```

where `c` is the exact lawful equivalence-block count for the target relation after quotienting.

Common infrastructure remains excluded exactly as in the frozen specification. File compression, byte packing, implementation sharing, runtime layout, or caching never reduce semantic burden.

No burden term may be added or removed after application outcomes are observed.

---

# 9. Exact closure/minimum procedures

The scientific procedure remains the frozen tripartite certification:

\[
\Pi_{\mathcal L}
=
(\Pi^{unrestricted}_{\mathcal L},\Pi^{admissible}_{\mathcal L},\Pi^{minimum}_{\mathcal L}).
\]

A negative result may arise only from an exact closure certificate.

The following are forbidden as `NOT_REPRESENTABLE` evidence:

```text
timeout
search interruption
optimizer failure
best mismatch
near miss
failure to find
stochastic search failure
resource exhaustion
```

## 9.1 `L_ORD1`

Use the frozen algebraic closure procedure:

```text
lawful EQ partition
cross-block homogeneity
no NWP on quotient
complete acyclic directional quotient
```

Membership yields fixed minimum burden `n+3`.

## 9.2 `L_RADIUS1`

Use an exactly exhaustive constraint procedure over the frozen witness domain:

```text
distinct equivalence-block scores in 0..n-1
min used score = 0
tau in 0..n-1
```

Execution order is frozen:

```text
tau ascending
block roots ascending anonymous handle
available scores ascending
```

Depth-first search may prune a partial score assignment only when a pair whose two endpoint scores are already assigned decodes to a token different from the frozen target. Such pruning removes only impossible completions and is therefore exactly equivalent to exhaustive injection enumeration.

An exact witness ends unrestricted search because all exact `L_RADIUS1` witnesses have the same burden `n+5`. `NOT_REPRESENTABLE` requires exhaustive completion of all parameter/assignment branches.

## 9.3 `L_BANDS1`

Use the same exact block-score DFS over:

```text
distinct equivalence-block scores in 0..n-1
min used score = 0
0 <= tau_1 <= tau_2 <= n-1
(p1,p2,p3) in {DIRECTION,NWP}^3
```

Parameter order is frozen lexicographically:

```text
tau_1 ascending
tau_2 ascending
policy tuple over (DIRECTION,NWP)^3 in product order
block roots ascending
available scores ascending
```

The only permitted branch pruning is exact pair-decoder inconsistency after both endpoint scores are assigned.

An exact witness ends unrestricted search because every exact `L_BANDS1` witness has fixed burden `n+7`. `NOT_REPRESENTABLE` requires exhaustive completion of all branches.

## 9.4 `L_INTERSECT2`

Use the frozen algebraic preconditions:

```text
lawful homogeneous quotient
directional quotient acyclic
directional quotient transitively closed
```

If they pass, enumerate linear extensions of `order1` lazily in deterministic lexicographic topological order rather than materializing the full extension set.

For each `order1`, construct the frozen `order2` constraints: preserve every target direction and reverse every target-NWP pair relative to `order1`. Exact acyclicity of those constraints decides whether an `order2` exists.

Lazy enumeration changes no witness semantics and is complete because every exact witness contains an `order1` linear extension of all target directions.

Membership yields fixed burden `n+c+5`.

## 9.5 `L_POSET`

Use the frozen algebraic closure procedure:

```text
lawful homogeneous quotient
directions acyclic
directions equal their transitive closure
unique transitive reduction
```

The unique transitive reduction supplies the exact minimum witness and burden.

## 9.6 `L_SPARSE_LINEAR`

Use the frozen algebraic closure procedure:

```text
lawful homogeneous quotient
unique direct directional set
no reciprocal pair
|E_direct| <= n-1
```

No transitive completion is applied. The unique explicit direct-edge state supplies the exact minimum witness and burden.

---

# 10. Pre-application executor-conformance gate

Any application executable introduced in the execution commit must first demonstrate that its exact semantics match the frozen round-v1 semantics before reading the actual target blob.

Required gate:

```text
all 4096 complete four-token relations at n=4
x 6 treatment languages
= 24576 conformance cells
```

For every cell, the application executable must agree with the frozen reference semantics on:

```text
unrestricted closure membership
admissible closure membership
B_star when defined
terminal Sigma_outcome
```

The executor may use its optimized exact DFS/lazy enumeration implementation, but conformance must be exact.

If any mismatch occurs:

```text
STOP_APPLICATION_CONFORMANCE_FAILURE
```

and no actual application result is scientifically reachable.

This gate is specification-conformance evidence, not application evidence.

---

# 11. Terminal outcome map

The frozen classifier remains:

```text
Rep = 0
  -> NOT_REPRESENTABLE

Rep = 1 and Rep^A = 0
  -> REPRESENTABLE_AUTHORITY_INVALID

Rep^A = 1 and B_star >= B_R
  -> ADMISSIBLE_REPRESENTATION_NO_CONTRACTION

Rep^A = 1 and B_star < B_R
  -> FAITHFUL_CONTRACTION
```

For the six treatment languages, legal exact witness state is authority-admissible by the frozen authority regime. Any contradiction of that invariant must be surfaced as a conformance failure rather than repaired after target access.

---

# 12. Per-`(G,L)` output schema

Every one of the 24 primary cells must emit exactly one record with at least:

```text
governance_contract_id
language_id
target_relation_sha256
anonymous_candidate_count = 12
pair_count                = 66
B_R                       = 66
Rep
RepA
B_star
Sigma_outcome
closure_certificate_type
minimum_certificate
```

Typed field semantics:

```text
Rep
  boolean

RepA
  boolean when Rep=true
  NOT_EVALUATED when Rep=false

B_star
  nonnegative integer when RepA=true
  NOT_DEFINED otherwise

Sigma_outcome
  NOT_REPRESENTABLE
  REPRESENTABLE_AUTHORITY_INVALID
  ADMISSIBLE_REPRESENTATION_NO_CONTRACTION
  FAITHFUL_CONTRACTION

closure_certificate_type
  exact algebraic
  exact exhaustive constraint
  exact lazy finite enumeration

minimum_certificate
  canonical witness / exact burden certificate when defined
  NOT_DEFINED otherwise
```

Binding missingness semantics:

\[
\boxed{
\texttt{NOT_DEFINED}
\neq 0
\neq \infty.
}
\]

and:

\[
\boxed{
\texttt{NOT_EVALUATED}
\not\rightarrow
\text{imputation}.
}
\]

No missing value, timeout, or absent witness may be converted into zero burden, infinite burden, a negative result, or a terminal status by imputation.

---

# 13. Nuisance, anonymity, and permutation checks

The primary scientific object is the anonymous typed relation, not candidate naming or serialization.

## 13.1 Candidate permutation / nuisance transport

For each governance target and each encoding index `e=0..63`, derive the nuisance encoding from the frozen round-v1 deterministic nuisance function using:

```text
case_id = "ACTUAL_APPLICATION__" + governance_contract_id
n       = 12
```

The encoding supplies the already-frozen nuisance dimensions:

```text
candidate permutation
pair-record serialization order
display aliases
opaque nonce
implementation tag
```

Additionally, provenance display labels must be shadow-rewritten deterministically and excluded before the treatment interface.

For all 256 target encodings:

```text
inverse-transport(target_permuted) == canonical_target
```

must hold exactly.

For every representable primary cell, transport the exact witness under each candidate permutation and verify:

```text
exact target decode
same B_star
same Sigma_outcome
```

For nonrepresentable cells, permutation invariance is certified by the already-SpecComplete-validated candidate-permutation equivariance of the frozen language semantics plus exact bijective target transport; nonmembership is not re-decided by an outcome-dependent alternative search.

Report the full numerator/denominator counts. Any mismatch is a conformance failure, not a new scientific outcome.

## 13.2 Pair swap

For each of the 4 x 66 target pairs, verify exact typed swap:

```text
PREFER_I                 <-> PREFER_J
PREFER_J                 <-> PREFER_I
EQUIVALENT                 -> EQUIVALENT
NO_WARRANTED_PREFERENCE    -> NO_WARRANTED_PREFERENCE
```

Every representable-cell witness must also decode consistently under both pair orientations for every pair.

No tolerance is permitted.

---

# 14. Evidence provenance

The execution output provenance is frozen as:

```text
POST_SPECIFICATION_APPLICATION_EVIDENCE
```

This label is intentional.

The actual target relations existed historically before the DSLI_R1 language architecture. Therefore this execution is not labeled pristine held-out confirmation and must not be described as such.

The application asks only how the already-frozen language family behaves on the already-existing actual governance-relative relations.

---

# 15. No cross-language or cross-governance decision layer

Application outputs remain a 4 x 6 response surface.

They do not define:

```text
cross-language winner
cross-language ranking
language score
language weighting
application priority
best language
minimum-B_star language selection
governance winner
governance ranking
governance vote
governance aggregation
candidate ranking
candidate selection
```

In particular:

\[
\boxed{
\Sigma(R_{\rm actual}^{G},L)
\not\rightarrow
\text{SELECTED}(L).
}
\]

and:

\[
\boxed{
\texttt{FAITHFUL_CONTRACTION}
\not\rightarrow
Q_{\rm extension}.
}
\]

No `argmin_L B_star`, Pareto filter, majority rule, tie-break, or implicit preference over languages is licensed.

---

# 16. Anti-downstream flags

The execution result must bind at least:

```text
actual_target_application_performed      = true
application_evidence_role                = POST_SPECIFICATION_APPLICATION_EVIDENCE

application_set_modified                 = false
language_family_modified                 = false
language_semantics_modified              = false
characterization_dependent_filtering     = false
characterization_dependent_weighting     = false
application_priority_assigned            = false
cross_language_ranking_performed         = false
cross_language_winner_selected           = false
governance_contract_selected             = false
governance_family_ranked                  = false
Q_extension_defined                      = false
candidate_ranking_performed              = false
candidate_selected                       = false
authorization_performed                  = false
binding_performed                        = false
execution_performed                      = false
v2_design_update_performed               = false
```

Application results cannot change any of these downstream flags in the same execution commit.

---

# 17. Hard stop

After all 24 primary cells, conformance checks, nuisance checks, pair-swap checks, result serialization, and application audit are complete, emit:

```text
STOP_DSLI_R1
```

The execution commit must not in the same scientific operation:

```text
add or modify a treatment language
define a new decoder
repair a failed language
select a language
rank languages
select governance
resolve governance disagreement
define Q_extension
rank or select candidates
authorize
bind
execute
construct K'
define Delta_T^A
define P_keep
construct a repair/replacement language
begin a v2 calibration/application round
```

Any post-v1 architecture or v2 development begins only after the completed v1 application has been committed and `STOP_DSLI_R1` recorded.

---

# 18. Binding preregistration statement

The only licensed v1 execution is now:

\[
\boxed{
\forall G\in
\{G_{\rm PARTIAL\_EMPTY},G_{\rm CONSTRAINT\_B},G_{\rm LEX\_DV\_REOPEN\_B},G_{\rm COMP\_EXPLICIT}\},
\quad
\forall L\in\mathfrak L_{\rm app}^{(1)}:
\quad
R_{\rm actual}^{G}
\mapsto
S(R_{\rm actual}^{G},L;A_{\rm DS}^{(1)},B_{\rm DS}^{(1)}).
}
\]

The application records representability, authority-valid representability, exact minimum burden when defined, and the frozen terminal outcome for every cell.

It grants no language-selection authority, no governance-selection authority, no candidate-selection authority, no `Q_extension`, no authorization, and no binding.

After execution, v1 stops.
