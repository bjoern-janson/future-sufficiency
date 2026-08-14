# Extension Candidate Comparator Application — Preregistration

## Status

This document freezes the **application** of the already-identified extension comparison architecture to the already-measured, already-preregistered 12-candidate extension set.

Parent checkpoint:

```text
d0802137f303406c4aab1e5779af644b4cfe6b4f
```

Comparison-identification preregistration:

```text
844573923269a767027e6052068b57961a54381b
```

Comparison-identification execution:

```text
d0802137f303406c4aab1e5779af644b4cfe6b4f
```

Candidate-measurement preregistration:

```text
6850a2f421d4477c45f679dcf03909f914788bbc
```

Candidate-measurement execution:

```text
c0db168261ebfb32106382c34c992bf00ec1aa4c
```

Measurement-identification execution:

```text
607502a9434884ca9bb06d5ddd6ff6c17f2ef002
```

Exact upstream result blobs:

```text
candidate measurement results
  dce4b66df142cfcb2a6515a082585f36ab374071

comparison-identification results
  7bac5f2aed17de6532b2fccfa138d8f954c78a8b

comparison-identification executable
  f7dcee2d583d1471707b21843f1ed1469aed16fe
```

The only object frozen here is:

\[
\boxed{
(s_i,s_j,k)
\longrightarrow
\Lambda_k(s_i,s_j)
\longrightarrow
R_k(s_i,s_j)
}
\]

for every unordered pair of the frozen 12 candidates and every one of the six frozen comparison coordinates.

This artifact defines **no cross-coordinate candidate preference**.

It defines no `Q_extension`.

It defines no Pareto relation, winner, recommendation, adoption rule, authorization rule, or binding operation.

---

# 1. Scientific boundary

The preceding branch has earned, in finite audited regimes:

\[
\boxed{
\mathcal M_{\rm ext}\checkmark
\rightarrow
s\mapsto\mathcal V_{\rm ext}(s)\checkmark
\rightarrow
\mathcal R_{\rm compare}\checkmark.
}
\]

The present question is now deliberately mechanical:

> What native, coordinate-specific pairwise relations are produced when the frozen comparison-license/native-relation architecture is applied verbatim to the frozen measured candidate records?

The governing separation is:

\[
\boxed{
\text{candidate measurement}
\neq
\text{native coordinate relation}
\neq
\text{cross-coordinate preference}.
}
\]

The strongest result permitted after execution is:

\[
\boxed{
\textbf{
The frozen native comparison architecture yields the following licensed coordinate-specific pairwise relations over the preregistered candidate set, with incomparability and no-license boundaries preserved.
}
}
\]

No stronger claim is permitted.

---

# 2. Frozen candidate universe

The candidate universe is inherited without addition, deletion, replacement, deduplication, or post-measurement selection from `6850a2f` / `c0db168`.

Canonical candidate IDs, sorted lexicographically:

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

Frozen provenance counts:

```text
CONTROL       4
EXTERNAL      4
SYNTHESIZED   4
TOTAL        12
```

Provenance remains metadata and lineage only.

It may not alter `Lambda_k` or `R_k` when native records are otherwise identical.

Thus:

\[
\boxed{
P(s_i)\neq P(s_j)
\not\Rightarrow
R_k(s_i,s_j)\text{ changes}.
}
\]

---

# 3. Frozen pair universe

Every unordered pair of distinct candidates must be evaluated.

Let the sorted ID vector above be `IDS`.

The child executable must construct pairs exactly as:

```python
pairs = list(itertools.combinations(IDS, 2))
```

with `IDS` already lexicographically sorted.

Therefore:

\[
\boxed{
|\mathfrak P_{\rm actual}|=\binom{12}{2}=66.
}
\]

The canonical JSON encoding of the ordered pair list using compact separators has SHA-256:

```text
76ae7638e225973f21b90605a9c020a74e752143d1dd008bd2f894fdbd4629aa
```

No pair may be omitted because it appears uninteresting, redundant, obviously equivalent, externally sourced, incompletely measured, or likely unlicensed.

No pair may be added after inspecting relations.

No semantically equivalent candidates may be merged before comparison.

The alias and Hudson provenance objects remain separate candidate records even when one or more native coordinate measurements coincide with another candidate.

---

# 4. Frozen coordinate universe

For every one of the 66 pairs, evaluate exactly these six coordinates:

```text
DeltaV
B
DeltaC
collateral
reopen
Scope
```

Therefore the execution must produce exactly:

\[
\boxed{
66\times6=396
}
\]

candidate-pair-coordinate application records.

There is no pre-filter such as:

```text
compare only fully identified pairs
compare only synthesized pairs
compare only same-provenance pairs
compare only same-parent pairs
compare only pairs with apparent differences
```

If a coordinate is not licensed, the corresponding application record remains present and emits `NO_LICENSED_COMPARISON`.

---

# 5. Comparator architecture is immutable

The application must use the already-identified comparison architecture from `8445739` / `d080213` verbatim.

The comparator contracts remain:

\[
\boxed{
\mathcal R_{\rm compare}
=
\{C_{\Delta V},C_B,C_{\Delta C},C_{\rm collateral},C_{\rm reopen},C_{\rm scope}\}.
}
\]

Each remains typed as:

\[
\boxed{
C_k=(D_k,\Lambda_k,R_k,\mathcal T_k^{\rm cmp},F_k^{\rm cmp},L_k^{\rm cmp}).
}
\]

The only permitted evaluation chain is:

\[
\boxed{
D_k
\rightarrow
\Lambda_k
\rightarrow
R_k.
}
\]

The child executable must checksum-verify or import the frozen comparison-identification executable/result artifacts.

Any modification to a license condition, native relation, admissible transformation, native type, or relation vocabulary invalidates this preregistration rather than counting as an implementation adjustment.

In particular, application may not widen a comparator merely because an actual candidate pair would otherwise be unlicensed.

---

# 6. Frozen output vocabulary

Every candidate-pair-coordinate record must contain exactly one relation token from:

\[
\boxed{
\{
\texttt{I\_GREATER},
\texttt{J\_GREATER},
\texttt{EQUIVALENT},
\texttt{INCOMPARABLE},
\texttt{NO\_LICENSED\_COMPARISON}
\}.
}
\]

Candidate `i` and candidate `j` are defined by the canonical lexicographic pair order.

`I_GREATER` and `J_GREATER` retain only the coordinate-native semantics frozen at `8445739`.

They may not be rendered as:

```text
better
worse
winner
loser
preferred
dominated
recommended
should adopt
```

The child result must hard-assert:

\[
\boxed{
R_k(i,j)=\texttt{I\_GREATER}
\not\Rightarrow
i\succ j.
}
\]

---

# 7. Absolute separation of the two null-like relation outcomes

The application must preserve:

\[
\boxed{
\texttt{INCOMPARABLE}
\neq
\texttt{NO\_LICENSED\_COMPARISON}.
}
\]

`INCOMPARABLE` requires:

```text
both native coordinate records identified
native types valid
comparison frame licensed
required common support nonempty
native relation evaluated
no equality or direction follows
```

`NO_LICENSED_COMPARISON` means the application was stopped at `Lambda_k` because one or more required license conditions failed.

The execution may not translate either token into the other for convenience.

It may not turn `NOT_IDENTIFIED` into zero, an empty vector, an empty geometry set, an empty burden ledger, a neutral consequence, or a worst-case consequence.

---

# 8. Candidate record source and decoding

All actual coordinate inputs must come from the committed machine-readable candidate-measurement result blob:

```text
dce4b66df142cfcb2a6515a082585f36ab374071
```

The child executable must decode the lossless packed result produced at `c0db168` and verify its recorded uncompressed SHA-256 and byte count before constructing any `D_k` record.

The Markdown summary table is **not** an admissible substitute for the machine-readable native objects.

The application must preserve:

- all 13 `DeltaV` per-contract effects and the frozen panel mean;
- all inclusion-minimal burden ledgers;
- complete `C_plus` / `C_minus` semantic partition sets;
- all six labeled collateral components;
- all eight labeled reopenability stress outcomes;
- the complete coordinate-specific scope/support record;
- coordinate statuses and `NOT_IDENTIFIED` null values;
- provenance and measurement lineage.

No descriptive summary may replace a native object where the comparator requires the native object.

---

# 9. Canonical application record

For pair `(i,j)` and coordinate `k`, emit:

```text
pair_id
candidate_i
candidate_j
provenance_i
provenance_j
coordinate
input_status_i
input_status_j
D_k frame metadata
support_i
support_j
support_intersection
license_conditions_checked
license_result
native_relation_witness
relation_token
measurement_lineage_i
measurement_lineage_j
comparison_lineage
```

For `NO_LICENSED_COMPARISON`, also emit the explicit failed license condition(s).

No application record may contain an overall pair score, candidate preference label, utility value, rank, or adoption status.

---

# 10. `DeltaV` application adapter

The native candidate measurement contains the frozen 13-contract paired consequence record and `panel_mean`.

For `C_DeltaV`, construct the scalar native comparison value as:

```text
native_scalar = candidate.DeltaV.native_value.panel_mean
```

only when the coordinate status is `IDENTIFIED`.

The complete per-contract vector remains attached to lineage and must be checksum/panel verified; it is not discarded from provenance.

The causal comparison frame is frozen as:

```text
DeltaV / parent_substrate / frozen_13_contract_panel / kappa=0.1
```

Therefore two `DeltaV` records are in the same direct comparison frame only when:

1. both are `IDENTIFIED`;
2. both use the frozen 13-contract panel and outcome scale;
3. both use the same parent-substrate causal baseline;
4. their coordinate support intersection is nonempty and `PASS`;
5. no unregistered causal-frame bridge is required.

Different parent-substrate baselines are not automatically bridged merely because both outputs are scalar numbers.

If any condition fails:

```text
NO_LICENSED_COMPARISON
```

The scalar relation, when licensed, is exactly the identified signed-difference relation from `C_DeltaV`.

---

# 11. Burden application adapter

The candidate measurement retains the complete set of inclusion-minimal obligation ledgers.

For each minimal ledger, map the named category counts into exactly this frozen category order:

```text
explicit
inherited
hidden
target_specific
search
external
```

forming a six-component integer tuple.

The `D_B` native value is the complete deduplicated set of those six-tuples.

The burden schema is:

```text
burden6 / semantic obligation counts / expanded hidden-inherited-target-specific accounting
```

Visible token count, macro count, candidate source class, and `expanded_total` alone are not the native comparator input.

All candidates use the same frozen burden category schema; license still requires both statuses `IDENTIFIED` and nonempty coordinate-specific common support.

The robust minimal-ledger-envelope relation from `C_B` is then applied verbatim.

---

# 12. Geometry application adapter

The candidate measurement retains:

\[
\Delta\mathcal C(s)
=
(\mathcal C_+(s),\mathcal C_-(s)).
\]

Construct the native set objects from the full `partitions` fields, not from cardinalities or checksums alone.

The comparison frame is:

```text
DeltaC / parent_substrate baseline / partition_mod_polarity semantic universe
```

Direct comparison is licensed only if the two candidate geometry records use the same parent-substrate baseline frame or an already-preregistered bijective baseline transport exists.

This preregistration introduces **no new baseline transport**.

Therefore a cross-parent pair cannot be rescued by comparing only `|C_plus|`, `|C_minus|`, closure sizes, or checksums.

When licensed, the set-equality / componentwise-set-containment / crossing relation from `C_DeltaC` is applied verbatim.

Cardinality remains descriptive only.

---

# 13. Collateral application adapter

The candidate measurement retains six labeled collateral components:

```text
x1
x2
x3
x4
x1_XOR_x2
x3_XOR_x4
```

Construct the native signed vector in exactly that label order after verifying component labels.

The comparison architecture is the already-frozen componentwise vector relation parameterized by the common labeled collateral family.

The application uses the full six-component candidate panel; no mean, weighted mean, sign count, or maximum component substitutes for the vector.

The causal comparison frame is frozen as:

```text
collateral / parent_substrate / frozen_6_contract_panel / kappa=0.1
```

License requires:

1. both candidate collateral statuses `IDENTIFIED`;
2. all six components identified for both;
3. identical labeled collateral family;
4. compatible signed consequence scales;
5. the same parent-substrate causal baseline;
6. nonempty coordinate-specific common support.

No new cross-parent causal-frame bridge is introduced here.

When licensed, the componentwise partial order from `C_collateral` is applied verbatim.

---

# 14. Reopenability application adapter

The candidate measurement retains eight labeled binary stress outcomes and their descriptive frequency.

Construct the native vector in the frozen stress-label order:

```text
rho1
rho2
rho3
rho4
rho5
rho6
rho7
rho8
```

The stresswise vector—not frequency alone—is the comparator input.

License requires:

1. both statuses `IDENTIFIED`;
2. all eight stress outcomes present;
3. identical stress-family checksum;
4. compatible deadline, challenge/refinement apparatus, certificate semantics, and update harness;
5. nonempty coordinate-specific common support.

Parent-substrate identity is not itself a required equality condition for `C_reopen`, because this coordinate measures absolute future corrective reachability under the common frozen stress harness rather than an extension-attributable difference against a parent baseline.

No bridge is invented for Hudson composite records that were `NOT_IDENTIFIED` by the frozen reopenability measurement instrument.

When licensed, the stresswise componentwise partial order from `C_reopen` is applied verbatim.

Equal frequency with different stresswise outcomes remains non-equivalence.

---

# 15. Scope application adapter

The candidate Scope record contains the frozen regime-status map and per-coordinate support sets.

For the direct descriptive `C_scope` relation, use exactly:

```text
S_all(s) = candidate.Scope.native_value.common_intersection
```

where `common_intersection` is the already-measured support set on which all required extension-measurement coordinates are simultaneously `PASS`.

No union, imputation, or coordinate-specific rescue is introduced for the direct Scope relation.

Direct `C_scope` comparison uses the identified support-set relation and requires a nonempty common support intersection between the two `S_all` sets.

For every non-Scope coordinate `k`, `Lambda_k` uses instead the already-measured coordinate-specific support set:

```text
candidate.Scope.native_value.support[k]
```

Thus direct Scope description and coordinate-specific license remain distinct.

Effect magnitude may not expand either support set.

---

# 16. Hudson / external candidate discipline

The four external candidates remain ordinary members of the 12-candidate pair universe:

```text
EXT_CT_A
EXT_CT_B
EXT_CT_C1
EXT_CT_C2
```

They receive no special favorable or unfavorable comparator rule.

Their frozen candidate-measurement statuses remain authoritative.

In particular, the upstream measurement result established:

```text
DeltaV      NOT_IDENTIFIED
B           IDENTIFIED
DeltaC      IDENTIFIED
collateral  NOT_IDENTIFIED
reopen      NOT_IDENTIFIED
Scope       IDENTIFIED
```

for the Hudson composite class.

The application must therefore allow `Lambda_k` to emit `NO_LICENSED_COMPARISON` where required.

It must not reinterpret missing Hudson values as zero, neutral, bad, good, or conservative.

It must not widen `M_k` or `C_k` to obtain a more complete Hudson comparison.

No Hudson superiority or inferiority statement is permitted.

---

# 17. Canonical direction and pair-swap regression

Only the canonical lexicographic `(i,j)` pair orientation is serialized in the primary result.

The execution must additionally recompute every licensed/unlicensed relation after swapping the two input records and assert:

```text
I_GREATER                  <-> J_GREATER
EQUIVALENT                 ->  EQUIVALENT
INCOMPARABLE               ->  INCOMPARABLE
NO_LICENSED_COMPARISON     ->  NO_LICENSED_COMPARISON
```

The reverse computation is a regression assertion only and does not create a second graph edge in the canonical result.

---

# 18. Output structure: coordinate-labeled multiplex graph only

The result may serialize the 396 coordinate application records as a coordinate-labeled multiplex graph.

Allowed descriptive summaries include:

- relation-token counts **within each coordinate**;
- license / no-license counts **within each coordinate**;
- lists of coordinate-specific `INCOMPARABLE` pairs;
- lists of coordinate-specific `NO_LICENSED_COMPARISON` pairs and failed-license reasons;
- coordinate-specific equality or direction edges;
- provenance-stratified counts only if provenance is not used to determine any relation.

Forbidden summaries include:

- a single overall relation for a candidate pair;
- number of coordinates “won” by a candidate;
- cross-coordinate dominance counts;
- candidate win/loss records;
- candidate rankings;
- candidate scores;
- Pareto fronts;
- a global comparability rate used as a preference proxy;
- a best synthesized, external, or control candidate.

The multiplex graph must preserve coordinate labels all the way to serialization.

---

# 19. No cross-coordinate completion

The application must **not** construct a total or partial order over candidates by combining coordinate relations.

In particular, the following are forbidden even if mechanically tempting:

```text
if DeltaV is I_GREATER and burden is not J_GREATER -> prefer i
if i is never J_GREATER -> Pareto nondominated
count I_GREATER minus J_GREATER
majority vote across coordinates
lexicographic DeltaV then reopen then burden
normalize coordinates and sum
assign penalties to NO_LICENSED_COMPARISON
assign penalties to INCOMPARABLE
```

No relation token may be mapped to a common numerical scale.

There is no sign convention that turns `B:I_GREATER` into negative utility or `DeltaV:I_GREATER` into positive utility in this gate.

Coordinate orientation remains descriptive.

---

# 20. Missingness and no-license discipline

The execution must hard-assert:

\[
\boxed{
\texttt{NOT\_IDENTIFIED}\neq0\neq\text{negative consequence}.
}
\]

and:

\[
\boxed{
\texttt{NOT\_IDENTIFIED}\not\rightarrow\text{imputation}.
}
\]

Every `NO_LICENSED_COMPARISON` record must remain in the 396-record output.

No candidate may be dropped because it produces many no-license cells.

No pair may be dropped because all or most of its coordinate applications are unlicensed.

No later-stage placeholder preference is permitted.

---

# 21. Application integrity controls

The child executable must assert all of the following before accepting the result.

## A1 — candidate registry integrity

```text
candidate_count = 12
CONTROL = 4
EXTERNAL = 4
SYNTHESIZED = 4
```

Candidate IDs must match this preregistration exactly.

## A2 — pair universe integrity

```text
unordered_pair_count = 66
pair_list_sha256 = 76ae7638e225973f21b90605a9c020a74e752143d1dd008bd2f894fdbd4629aa
```

## A3 — coordinate completeness

Every pair has exactly six coordinate application records.

```text
application_record_count = 396
```

## A4 — no pruning / no addition

```text
candidate_pruning = 0
candidate_addition = 0
pair_pruning = 0
pair_addition = 0
coordinate_record_pruning = 0
coordinate_record_addition = 0
```

## A5 — frozen comparator verification

The child executable must verify the comparison-identification result and executable anchors from `d080213` before applying any relation.

## A6 — frozen candidate-measurement verification

The child executable must verify the packed candidate result blob and its internal uncompressed checksum before reading actual native records.

## A7 — pair-swap symmetry

All 396 canonical relation tokens must satisfy the frozen swap law under reversed inputs.

## A8 — provenance blindness

Changing only the provenance label in a copy of an otherwise identical application record must not alter `Lambda_k` or `R_k`.

This is a regression control only; it does not mutate the real candidate record.

## A9 — no cross-coordinate leakage

For each coordinate application, irrelevant coordinates must not be read by the comparator path except Scope support needed by `Lambda_k`.

## A10 — no preference output type

No output schema may contain:

```text
PREFER_I
PREFER_J
WINNER
LOSER
BETTER
WORSE
RANK
UTILITY
Q_extension
ADOPT
AUTHORIZE
BIND
```

---

# 22. Deliberately forbidden application shortcuts

The child executable should implement these only as hard assertions that the primary path does not contain them; it need not generate a new wrong-control score because their invalidity was already identified at `d080213`.

## W1 — missingness imputation

Forbidden:

```text
NOT_IDENTIFIED -> 0
```

## W2 — native scalarization

Forbidden:

```text
burden -> visible count or total only
geometry -> cardinality only
collateral -> mean
reopenability -> frequency only
Scope -> support cardinality only
```

## W3 — automatic frame bridging

Forbidden:

```text
same numerical type -> comparable
same cardinality -> comparable
same frequency -> comparable
same outcome scale -> comparable despite different causal baseline
```

## W4 — external-candidate special casing

Forbidden:

```text
Hudson missing -> pessimistic value
Hudson missing -> optimistic value
Hudson external provenance -> extra license
Hudson external provenance -> reduced license
```

## W5 — relation-to-preference leakage

Forbidden:

```text
I_GREATER -> PREFER_I
J_GREATER -> PREFER_J
```

for every coordinate.

---

# 23. No anonymous remeasurement and no comparator retuning

This is an **application** gate, not a new measurement-identification or comparator-identification gate.

The child executable must not regenerate candidate measurements under alternative panels, fit thresholds, tune tolerances, select candidate subsets, or alter comparator parameters after seeing actual relations.

The 64-anonymous-encoding identification evidence remains inherited from the upstream measurement and comparator audits.

The only fresh symmetry check required here is deterministic pair swapping and serialization-order independence on the fixed actual records.

If an actual candidate record exposes an unforeseen schema incompatibility, the execution must fail or emit `NO_LICENSED_COMPARISON` according to the frozen contract; it must not repair the comparator inside this run.

---

# 24. Relation lineage

Every coordinate relation must carry both measurement and comparison lineage.

At minimum:

```text
candidate_measurement_commit = c0db168261ebfb32106382c34c992bf00ec1aa4c
candidate_measurement_results_blob = dce4b66df142cfcb2a6515a082585f36ab374071
comparison_identification_commit = d0802137f303406c4aab1e5779af644b4cfe6b4f
comparison_identification_results_blob = 7bac5f2aed17de6532b2fccfa138d8f954c78a8b
comparison_identification_executable_blob = f7dcee2d583d1471707b21843f1ed1469aed16fe
pair_id
candidate_i
candidate_j
coordinate
input_status_i
input_status_j
native_frame_i
native_frame_j
support_intersection
license_result
failed_license_conditions
native_relation_witness
relation_token
```

No evidence lineage from one coordinate may license another coordinate's relation.

---

# 25. Result serialization requirements

The execution commit must contain exactly three new scientific artifacts:

```text
audits/extension_candidate_comparator_application_audit.py
audits/extension_candidate_comparator_application_results.json
audits/extension_candidate_comparator_application_audit.md
```

The JSON result must preserve all 396 application records losslessly.

If compression is required for repository size, the same lossless packed-wrapper discipline used by the candidate-measurement audit is permitted, provided the wrapper contains:

```text
format
payload
uncompressed_sha256
uncompressed_bytes
summary
```

The `summary` may contain only non-preference metadata and coordinate-specific relation counts.

The Markdown result note may co-display coordinate relations but must not collapse them into an overall candidate relation.

---

# 26. Anti-preference / anti-aggregation contract

The execution and result note must not compute, emit, or imply:

- `s_i \succ s_j`;
- “candidate i is better”;
- “candidate j wins”;
- any candidate recommendation;
- overall pairwise candidate dominance;
- Pareto dominance or Pareto frontiers;
- cross-coordinate win counts;
- coordinate priority;
- tradeoff rates;
- weights;
- normalized common scales;
- utility functions;
- lexicographic preference;
- `Q_extension`;
- `NO_WARRANTED_ADOPTION`;
- adoption thresholds;
- authorization;
- binding;
- Hudson/Rubi superiority or inferiority.

The execution must include hard flags:

```text
actual_candidate_coordinate_relations_computed = true
actual_candidate_overall_pair_relation_defined = false
candidate_preference_defined = false
Pareto_filtering_performed = false
cross_coordinate_aggregation_defined = false
Q_extension_defined = false
NO_WARRANTED_ADOPTION_defined = false
authorization_performed = false
binding_performed = false
```

The first flag is true because native coordinate relation application is exactly the object of this gate.

Every downstream preference-bearing flag must remain false.

---

# 27. Execution success criteria

The application gate passes only if all of the following hold:

1. the exact 12-candidate registry is recovered from the frozen machine result;
2. the exact 66 unordered-pair universe is constructed and checksum-verified;
3. exactly 396 pair-coordinate application records are emitted;
4. every application follows `D_k -> Lambda_k -> R_k` without bypass;
5. every relation token belongs to the frozen five-token vocabulary;
6. every `NOT_IDENTIFIED` input that prevents comparison yields `NO_LICENSED_COMPARISON` rather than imputation;
7. every unsupported/incompatible frame yields `NO_LICENSED_COMPARISON` rather than automatic bridging;
8. every licensed crossed native relation remains `INCOMPARABLE` rather than being forced into direction;
9. set-valued geometry is compared as sets, not cardinalities;
10. burden is compared using complete minimal-ledger envelopes, not visible syntax;
11. collateral is compared componentwise on the frozen six-contract panel, not by mean;
12. reopenability is compared stresswise on the frozen eight-stress family, not by frequency alone;
13. Scope acts as support topology/license and is never a compensable value;
14. canonical pair-swap symmetry holds;
15. provenance does not alter relation outputs;
16. no candidate, pair, or coordinate record is pruned after relations are seen;
17. no overall candidate-pair relation is emitted;
18. no cross-coordinate aggregation, preference, Pareto, `Q_extension`, adoption, authorization, or binding artifact is introduced.

A partial execution does not license downstream preference design.

---

# 28. Failure interpretation

| Observation | Interpretation |
|---|---|
| fewer than 12 candidates | candidate-universe leakage |
| fewer than 66 unordered pairs | pair-selection leakage |
| fewer than 396 coordinate records | coordinate pruning |
| `NOT_IDENTIFIED` converted to a number | missingness/imputation violation |
| cross-parent causal effects compared without bridge | causal-frame license failure |
| cross-baseline geometry compared by cardinality | geometry-frame / scalarization failure |
| Hudson causal coordinate receives fabricated value | measurement-ontology expansion |
| `INCOMPARABLE` replaced by a direction | partial-order collapse |
| `NO_LICENSED_COMPARISON` replaced by `INCOMPARABLE` | no-license/missingness collapse |
| candidate provenance changes relation | provenance leakage |
| coordinate relation converted to winner/preference | preference leakage |
| Pareto frontier appears | downstream aggregation leakage |
| all 396 records emitted under frozen contracts | application gate may pass |

---

# 29. Claim boundary if execution succeeds

The strongest permitted claim is exactly:

\[
\boxed{
\textbf{
The frozen native comparison architecture yields the reported licensed coordinate-specific pairwise relations over the preregistered 12-candidate set, with native relation types, incomparability, no-license boundaries, scope, and provenance preserved.
}
}
\]

A pass does **not** establish:

- that one candidate is better than another overall;
- an overall candidate partial order;
- Pareto dominance;
- a Pareto frontier;
- any coordinate priority;
- any cross-coordinate tradeoff rate;
- any extension-value function;
- `Q_extension`;
- `NO_WARRANTED_ADOPTION`;
- Hudson/Rubi superiority or inferiority;
- adoption;
- authorization;
- binding;
- persistence;
- post-adoption consequence;
- general self-modification;
- research agency.

The execution produces the **actual native comparison graph**, not a preference graph.

---

# 30. Frozen next sequence

The empirical sequence is now:

\[
\boxed{
\mathcal M_{\rm ext}\checkmark
\rightarrow
s\mapsto\mathcal V_{\rm ext}(s)\checkmark
\rightarrow
\mathcal R_{\rm compare}\checkmark
\rightarrow
\boxed{\text{actual-candidate comparator application [preregistered]}}
\rightarrow
\text{application execution}
\rightarrow
\text{inspection of native comparison graph}
\rightarrow
Q_{\rm extension}\text{ design [undefined]}
\rightarrow
Auth\text{ [undefined]}
\rightarrow
Bind\text{ [undefined]}.
}
\]

The only authorized next repository action is execution of this preregistration.

No dependency-ledger update, `Q_extension` artifact, Pareto artifact, preference artifact, adoption artifact, authorization artifact, or binding artifact is authorized before that execution result exists.
