# Extension Candidate Measurement — Preregistration

## Status

This document freezes the next empirical gate **before any candidate measurement is executed and before any candidate comparison or extension-value aggregation is defined**.

Parent checkpoint:

```text
607502a9434884ca9bb06d5ddd6ff6c17f2ef002
```

Measurement-identification preregistration:

```text
338981353778dd4efd6c5e0b0106a2d0828710c9
```

Measurement-identification execution:

```text
607502a9434884ca9bb06d5ddd6ff6c17f2ef002
```

Extension-synthesis anchor:

```text
9a50f07a1da3deee288366b47a0bd3a6a989e0a6
```

No `Q_extension` exists in this artifact. No candidate is ranked, preferred, selected, adopted, authorized, or bound. No Pareto filtering is permitted. No `NO_WARRANTED_ADOPTION` outcome exists.

The only object frozen here is:

\[
\boxed{
 s\longrightarrow\mathcal V_{\rm ext}(s)
}
\]

with:

\[
\boxed{
\mathcal V_{\rm ext}(s)=
\left(
\Delta V_{\rm corr}(s),
B_{\rm extension}(s),
\Delta\mathcal C(s),
R_{\rm collateral}(s),
R_{\rm reopen}(s),
\operatorname{Scope}(s)
\right).
}
\]

The governing methodological rule remains:

\[
\boxed{
\textbf{measure first}
\rightarrow
\textbf{compare second}
\rightarrow
\textbf{aggregate last}.
}
\]

---

# 1. Gate boundary

The present audit tests only whether a preregistered candidate set can be measured under the **already-identified** extension-measurement architecture.

The prohibited downstream chain is:

\[
\boxed{
\text{measurement}
\not\Rightarrow
\text{ranking}
\not\Rightarrow
Q_{\rm extension}
\not\Rightarrow
Auth
\not\Rightarrow
Bind.
}
\]

A measurement record may contain positive, zero, or negative coordinate values. Those values are measurements only.

The strongest claim permitted after a successful execution is:

\[
\boxed{
\textbf{
The preregistered candidate set was measured under the previously identified extension-measurement architecture, with provenance, native coordinate types, coordinate-specific lineage, and scope preserved.
}
}
\]

Nothing in this gate licenses a preference relation.

---

# 2. Immutable measurement architecture

The candidate-measurement execution must use the architecture identified at `607502a` without changing the scientific objects, intervention contracts, measurement rules, admissible transformations, invalidity signatures, or evidence-lineage requirements.

\[
\boxed{
\mathcal M_{\rm ext}^{\rm candidate}
=
\mathcal M_{\rm ext}^{\rm identified}.
}
\]

The six instruments remain:

\[
\boxed{
\mathcal M_{\rm ext}
=
\{M_{\Delta V},M_B,M_{\Delta C},M_{\rm collateral},M_{\rm reopen},M_{\rm scope}\}.
}
\]

The executable must import or otherwise checksum-verify the identified measurement implementation from:

```text
audits/extension_measurement_architecture_audit.py
commit: 607502a9434884ca9bb06d5ddd6ff6c17f2ef002
blob:   8ee0fa796f6eb40dd2b70f4f58ba51bec181238c
```

If a candidate cannot satisfy an instrument's already-identified intervention or scope conditions, the instrument must **not** be broadened or redesigned in this execution.

The result must instead be:

```text
Z_k(s) = NOT_IDENTIFIED
value  = null
```

with the failed identification/scope condition recorded in lineage.

Any change to an `O_k`, `do_k`, `m_k`, `T_k`, `F_k`, or `L_k` definition invalidates this preregistration and requires a new measurement-identification gate before candidate measurement resumes.

---

# 3. Canonical candidate record

For every candidate `s`, emit exactly one typed record:

\[
\boxed{
\left[
P(s),
\{(Z_k(s),M_k(s),L_k(s),\mathcal R_{s,k})\}_k
\right].
}
\]

`P(s)` is provenance metadata, not a value coordinate.

For each coordinate:

\[
\boxed{
Z_k(s)\in\{\texttt{IDENTIFIED},\texttt{NOT\_IDENTIFIED}\}.
}
\]

If `IDENTIFIED`, the native typed measurement is reported together with its lineage and support set.

If `NOT_IDENTIFIED`, no numerical or pseudo-numerical substitute may be emitted.

The missing-data discipline is absolute:

\[
\boxed{
\texttt{NOT\_IDENTIFIED}\neq0\neq\text{negative measured consequence}.
}
\]

and:

\[
\boxed{
\texttt{NOT\_IDENTIFIED}
\not\rightarrow
\text{imputation}.
}
\]

Forbidden substitutes include:

- zero filling;
- mean filling;
- worst-case filling;
- best-case filling;
- sentinel numbers that enter later arithmetic;
- candidate deletion because a coordinate is missing;
- treating missing scope as neutral scope;
- relabeling a negative value as `BAD`.

`BAD` is not a measurement status in this gate. A negative effect remains `IDENTIFIED` with its signed native value.

---

# 4. Candidate universe frozen before measurement

The full candidate universe is frozen here as a disjoint union of **candidate records by provenance**, not by extensional equivalence:

\[
\boxed{
\mathfrak S_{\rm measure}
=
\mathfrak S_{\rm synth}
\dot\cup
\mathfrak S_{\rm external}
\dot\cup
\mathfrak S_{\rm control}.
}
\]

No candidate may be added, removed, replaced, or pruned after any candidate-level coordinate measurement has been observed.

Candidates may be extensionally identical while remaining different provenance objects:

\[
\boxed{
\mathcal V_{\rm ext}(s_1)=\mathcal V_{\rm ext}(s_2)
\not\Rightarrow
P(s_1)=P(s_2).
}
\]

The execution must report all preregistered candidates, including candidates with partially or wholly `NOT_IDENTIFIED` coordinate records.

---

# 5. Parent substrate registry

Candidate measurement uses candidate-specific parent substrates already established upstream.

## 5.1 `LINEAR_C0`

```text
semantic family size: 15
checksum:
809abd918f17a77c779f76ce1b14ba4661e63b6834c4bec475fbe8a8f8eeed49
```

## 5.2 `DEG2_C`

Complete zero-constant Boolean polynomial experiment family of algebraic degree `<=2`:

```text
semantic family size: 1023
checksum:
c51cc447000204a4c32e205d4e8daab954a52b80939664bbab2968629299efb7
```

A candidate record must retain its parent-substrate identifier. Parent differences are provenance/scope facts and may not be hidden during later serialization.

---

# 6. `S_synth` — all earned minimal synthesized semantic classes

No synthesized candidate is selected based on later measurements. The set is the complete set of minimal adequate semantic candidate classes already earned at `9a50f07`.

## 6.1 `SYN_A_120`

```text
provenance class: SYNTHESIZED
source commit: 9a50f07a1da3deee288366b47a0bd3a6a989e0a6
parent: LINEAR_C0
semantic closure size: 120
semantic closure fingerprint:
8d3a5ecddbcf823c2ffca59f2490d2950caea216816b3c8e9af58bb2dfbb5dc1
```

The implementation envelope is the complete preregistered set of M0 programs from the synthesis result that map to this semantic closure fingerprint. `M_B` must expand their semantic obligations under its already-identified accounting rule; candidate measurement may not choose a representation after observing burden.

## 6.2 `SYN_B_50`

```text
provenance class: SYNTHESIZED
source commit: 9a50f07a1da3deee288366b47a0bd3a6a989e0a6
parent: LINEAR_C0
semantic closure size: 50
semantic closure fingerprint:
c5381b17c76e113f0927e55a929bc855b74b68f4a3a676bc4534944c1330d897
```

## 6.3 `SYN_C1_1653`

```text
provenance class: SYNTHESIZED
source commit: 9a50f07a1da3deee288366b47a0bd3a6a989e0a6
parent: DEG2_C
semantic closure size: 1653
semantic closure fingerprint:
f5fc3cdd75661c1bdccc1efe88382e1669b481136ee14de2396009abc9330ad4
```

## 6.4 `SYN_C2_2388`

```text
provenance class: SYNTHESIZED
source commit: 9a50f07a1da3deee288366b47a0bd3a6a989e0a6
parent: DEG2_C
semantic closure size: 2388
semantic closure fingerprint:
644e80b2a4e568b789dad11dbb2057c71d836bc52e1e0d68fb31e3aa1f62493f
```

No other synthesized candidate is admitted in this gate.

The synthesis result's `D` null case produced no candidate and therefore contributes no member to `S_synth`.

---

# 7. `S_external` — frozen Hudson/Rubi corrigibility wrappers

The external comparator family is fixed **before candidate measurement** and is explicitly not synthesis evidence.

Source:

```text
Rubi Hudson
"Corrigibility Transformation: Constructing Goals That Accept Updates"
arXiv:2510.15395v2
version date: 2026-08-05
source object: Algorithm 1 main corrigibility transformation
```

The source describes a transformation that extends the action space with an accept/reject update bit, sets the transformed goal to be myopic, and rewards an action using the original-goal counterfactual action value for the reject-update version of that base action plus a fixed bonus for accepting the update.

The frozen external wrapper used here is:

```text
EXT_CT_HUDSON_V2

action space:
  A_base x {0,1}
  0 = reject designated update
  1 = accept designated update

gamma_C:
  0

reward:
  R_C(state, a_i, state')
    = Q_G^{pi**}(state, a_0) + delta * I(i=1)

delta:
  1/64

alternate-policy convention:
  pi**_{G_C}  = pi*_G
  pi**_{-G_C} = pi*_{-G_C}

reward timing:
  issued after action selection and before action execution

designated update channel:
  only the frozen update-request bit in the candidate-measurement harness
```

The following variants are **not** part of this comparator:

- the paper's optional `max_i Q` variant;
- recursively corrigible secondary-agent extension;
- goal-tampering extension;
- LLM prompt-level implementation;
- candidate-specific delta tuning;
- any modification chosen after seeing measurements.

The external comparator is instantiated as a wrapper on each already-frozen synthesized structural candidate. The structural repair remains visible in provenance; the wrapper makes the complete candidate an `EXTERNAL` provenance object because the distinguishing added transformation is externally supplied.

The four external candidates are:

```text
EXT_CT_A
  parent: LINEAR_C0
  structural base: SYN_A_120
  composite fingerprint:
  6b6c0313231b9ae7b195a0581fa689f26440854f0357645a62393545b8c4c760

EXT_CT_B
  parent: LINEAR_C0
  structural base: SYN_B_50
  composite fingerprint:
  cc36ca78600cf7615ee194375f8a28b9167136331dd3abe1f9252d38a7cd6a99

EXT_CT_C1
  parent: DEG2_C
  structural base: SYN_C1_1653
  composite fingerprint:
  756d62cad8ec50f8edd401c227e5635f91a937b0623b12c8015e06e8d1a5517f

EXT_CT_C2
  parent: DEG2_C
  structural base: SYN_C2_2388
  composite fingerprint:
  cde45778b9241e1c5d8b887a91d535f9554974e4ac3a0434d08d94816ee3ff36
```

These SHA-256 composite fingerprints are over the frozen base semantic fingerprint plus the canonical wrapper specification above.

## 7.1 External-comparator scope discipline

The identified measurement architecture was calibrated primarily on construction-substrate interventions. The external wrapper changes additional goal/action semantics.

Therefore the execution must run the existing per-coordinate identification/scope guards **before** reporting a measurement for an external candidate.

If `do_k` does not license the composite intervention, then:

```text
Z_k(EXT_CT_*) = NOT_IDENTIFIED
M_k value      = null
```

The child executable is forbidden from widening `do_k` to make the Hudson comparator fit.

This is a positive test of the scope discipline, not a failure of the candidate.

---

# 8. `S_control` — frozen controls

## 8.1 `CTRL_ID_LINEAR`

```text
provenance class: CONTROL
parent: LINEAR_C0
transformation: semantic identity / no-op
```

## 8.2 `CTRL_ID_DEG2`

```text
provenance class: CONTROL
parent: DEG2_C
transformation: semantic identity / no-op
```

## 8.3 `CTRL_SUPPLIED_DEG2`

This is the already-established Gate-2 supplied construction-substrate expansion, included as a prior externally supplied structural control rather than synthesis evidence.

```text
provenance class: CONTROL
parent: LINEAR_C0
source anchor: ee1b9ac
construction: supplied target-blind conjunction-capable binary operation + post-extension XOR closure
resulting semantic closure size: 1023
resulting semantic closure fingerprint:
c51cc447000204a4c32e205d4e8daab954a52b80939664bbab2968629299efb7
```

## 8.4 `CTRL_ALIAS_A`

This control is extensionally identical at the construction-space level to `SYN_A_120` but has distinct provenance and packaging.

```text
provenance class: CONTROL
parent: LINEAR_C0
semantic closure fingerprint:
8d3a5ecddbcf823c2ffca59f2490d2950caea216816b3c8e9af58bb2dfbb5dc1
visible representation: one opaque macro handle
hidden semantics: complete semantic obligation set required to reproduce SYN_A_120
```

Its purpose is not to prove a preference. It ensures candidate records do not merge solely because measured vectors or extension semantics coincide, and that `M_B` continues to charge hidden obligations rather than visible token length.

---

# 9. Frozen candidate registry cardinality

The execution must contain exactly:

```text
S_synth     4 candidates
S_external  4 candidates
S_control   4 candidates
-----------------------
TOTAL       12 candidates
```

No post-measurement candidate inclusion or exclusion is permitted.

Candidate order must be randomized during execution and canonicalized only by candidate ID for final serialization. Final order must never be sorted by a measured coordinate.

---

# 10. Anonymous encodings

Use exactly 64 common anonymous encodings for every candidate whenever the instrument's finite semantics permit it.

The same encoding index must be paired across candidates.

For encoding `j`, randomize consistently:

- world-state labels;
- primitive / experiment handles;
- candidate handles;
- target-contract identifiers;
- collateral-contract identifiers;
- stress identifiers;
- regime identifiers;
- public binary output polarity;
- update-bit public labels;
- enumeration order.

The semantic candidate identity, parent substrate, and provenance record remain unchanged.

The candidate-measurement executable must use a fixed deterministic seed namespace:

```text
candidate-measurement-v1 / encoding 0..63
```

No seed may depend on a measured candidate value.

---

# 11. Frozen held-out corrective-consequence panel

`M_DeltaV` must use a target panel not used as the synthesis target formulas.

The globally excluded synthesis targets are:

```text
x1 AND x2
x1 OR  x2
x1 AND x2 AND x3
```

The frozen held-out panel `K_corr*` contains 13 target contracts.

## 11.1 Pair targets

For pairs:

```text
(x1,x3)
(x1,x4)
(x2,x3)
(x2,x4)
(x3,x4)
```

include both:

```text
xi AND xj
xi OR  xj
```

for 10 contracts.

## 11.2 Cubic targets

Include:

```text
x1 AND x2 AND x4
x1 AND x3 AND x4
x2 AND x3 AND x4
```

for 3 contracts.

Total:

```text
|K_corr*| = 13
```

## 11.3 Frozen consequence evaluator

For each target contract and candidate/parent intervention pair:

1. compute baseline Bayes accuracy;
2. enumerate currently accessible semantic experiments under the frozen candidate construction substrate;
3. compute `R_corr = post_accuracy - baseline_accuracy`;
4. use the already-established continuation burden `kappa=0.1`;
5. if no experiment has `q=R_corr-kappa>0`, retain the baseline consequence;
6. otherwise use the frozen object-level acquisition rule to take a maximal worthwhile experiment; tie-breaking may depend only on semantic fingerprint, never candidate provenance or syntax;
7. measure the resulting held-out consequence under the previously identified `M_DeltaV` intervention contract.

Report per-contract paired effects and the preregistered mean across the 13 contracts.

The mean is an internal definition of this one measurement coordinate over a frozen evaluator panel. It is **not** cross-coordinate value aggregation.

If the candidate intervention violates `M_DeltaV`'s identified construction-only causal contrast, emit `NOT_IDENTIFIED` rather than modifying the contrast.

---

# 12. Frozen collateral panel

The non-target collateral family is fixed independently of candidate identity:

\[
\mathcal K_{\rm coll}^{\star}
=
\{x_1,x_2,x_3,x_4,x_1\oplus x_2,x_3\oplus x_4\}.
\]

Thus:

```text
m = 6 collateral contracts
```

For each contract, run the already-identified paired causal instrument independently and retain the native labeled vector:

\[
\boxed{
R_{\rm collateral}(s)
=(r_1,r_2,r_3,r_4,r_5,r_6).
}
\]

No sum, mean, maximum loss, weighted penalty, or sign count may replace the vector.

If any component is not identified under the candidate intervention, preserve component-level status rather than treating that component as zero.

---

# 13. Frozen future-reopenability stress family

The reopenability stress family is disjoint from both the synthesis targets and the immediate corrective-consequence target panel.

Use the following eight later target contracts:

```text
rho1 = (x1 AND x3) XOR (x2 AND x4)
rho2 = (x1 AND x4) XOR (x2 AND x3)
rho3 = (x1 OR  x3) XOR (x2 OR  x4)
rho4 = (x1 OR  x4) XOR (x2 OR  x3)
rho5 = x1 AND (x2 OR x4)
rho6 = x2 AND (x1 OR x3)
rho7 = x3 OR (x1 AND x4)
rho8 = x4 OR (x1 AND x2)
```

The family checksum must be reported by the child executable from a canonical truth-table serialization.

## 13.1 Future-update harness

The future stress evaluator is a finite fully observable update harness.

Frozen structure:

```text
state includes:
  environment state
  active goal identifier
  candidate-installed construction substrate

action includes:
  frozen base acquisition/commit action
  update bit {reject, accept}

original goal G0:
  basic reward function
  non-myopic discount gamma = 1/2

update request:
  sent only through the designated frozen update channel
  changes the active goal to G_rho when accepted

transition dynamics:
  non-goal environment dynamics depend only on the base action
  active-goal identity does not alter non-goal transition dynamics

deadline:
  two post-request decision steps

continuation burden:
  kappa = 0.1
```

The harness is constructed so the goal component is fully observable and the original reward is basic in the sense that reward does not directly value the goal-identity component.

For the Hudson external comparator, exact finite `Q_G` and optimal-policy quantities required by the frozen wrapper must be computed exhaustively; no learned critic approximation is admitted in this finite audit.

## 13.2 Reopenability path rule

Use the already-identified `M_reopen` object.

For candidate `s` and stress `rho`:

```text
Y_reopen(s,rho) = 1
```

iff the exact post-candidate, post-stress reachable graph contains a timely warranted corrective path under the frozen controller/challenge/refinement apparatus and without adding evidence, authority, or construction rules not already present in the candidate plus frozen future apparatus.

Otherwise:

```text
Y_reopen(s,rho) = 0
```

Report the full eight-element binary stress vector plus the finite-panel frequency:

\[
R_{\rm reopen}(s)
=\frac{1}{8}\sum_{j=1}^{8}Y_{\rm reopen}(s,\rho_j).
\]

If a candidate changes system variables outside the identified `M_reopen` intervention scope, record `NOT_IDENTIFIED`. Do not redefine reopenability around the candidate.

---

# 14. `M_B` candidate implementation discipline

Candidate measurement must not choose implementation packaging after observing burden.

## 14.1 Synthesized semantic classes

For each `SYN_*` semantic candidate class:

1. retrieve all already-recorded M0 programs that instantiate the semantic closure fingerprint;
2. expand all semantic obligations under the identified burden ledger;
3. remove only genuine semantic duplicates;
4. retain the complete set of inclusion-minimal obligation ledgers if more than one remains;
5. report the structured ledger and any already-licensed expanded/incremental totals.

Do not pick the lowest visible syntax representation.

## 14.2 External wrappers

For each `EXT_CT_*`, the burden ledger must include both:

- the complete structural-base candidate obligations; and
- the externally supplied wrapper obligations.

The wrapper obligations include at least:

```text
update-bit action extension
myopic transformed discount
exact original-goal action-value computation
alternate-policy convention
counterfactual reject-update reward rule
fixed acceptance bonus delta=1/64
pre-execution reward timing
designated update-channel semantics
```

Any external theorem assumption used to execute or interpret the wrapper must be recorded as an inherited/external obligation rather than disappearing from the ledger.

## 14.3 Controls

`CTRL_ALIAS_A` must be charged the hidden A semantics despite its one-token visible macro.

---

# 15. `M_DeltaC` structural projection rule

The native geometry object remains:

\[
\Delta\mathcal C(s)=(\mathcal C_+(s),\mathcal C_-(s)).
\]

For a composite external candidate, geometry is measured only if the candidate declaration contains an unambiguous frozen **structural projection** and all non-structural components are proven geometry-inert under the identified closure semantics.

For `EXT_CT_A/B/C1/C2`, the declared structural projection is exactly the underlying `SYN_*` candidate.

The Hudson wrapper is declared geometry-inert because it changes goal/action-update semantics and does not add, remove, or modify experiment-construction rules.

If execution detects that the wrapper implementation changes accessible experiment construction, the structural projection is invalid and `M_DeltaC` must emit `NOT_IDENTIFIED` for that candidate rather than silently absorbing the change.

The full set-valued `C_plus` and `C_minus` objects and checksums must be preserved. Cardinality alone is not the candidate record.

---

# 16. Scope and status protocol

For every candidate-coordinate pair, run the frozen identification guard before emitting a measurement.

The output schema is:

```text
candidate_id
provenance
parent_substrate
coordinate
status: IDENTIFIED | NOT_IDENTIFIED
native_value: <typed value> | null
lineage
support_regimes
failed_identification_conditions: [] | [...]
```

A coordinate is `IDENTIFIED` only where all already-frozen identification assumptions and invariance conditions hold.

A coordinate is `NOT_IDENTIFIED` if any required identification condition fails or if the candidate intervention lies outside the instrument's validated causal contrast.

The scope record must distinguish:

```text
PASS
FAIL
NOT_TESTED
```

at the regime level exactly as in the measurement-identification audit.

No candidate-level positive effect may override a `FAIL` or `NOT_TESTED` status.

---

# 17. Provenance schema

`P(s)` must contain at least:

```text
candidate_id
provenance_class: SYNTHESIZED | EXTERNAL | CONTROL
source_commit_or_document
parent_substrate
semantic_or_composite_fingerprint
structural_base_fingerprint
wrapper_or_packaging_fingerprint if present
implementation-envelope identifier
candidate-registry version
```

For composite external candidates also record:

```text
base_provenance: SYNTHESIZED
wrapper_provenance: EXTERNAL
external_source: arXiv:2510.15395v2 Algorithm 1
```

Provenance is never included in a measurement value and never used as a tie-breaker or ranking feature.

---

# 18. Native coordinate types must be preserved

The child results must preserve:

```text
DeltaV_corr:
  per-contract paired effects + frozen-panel mean

B_extension:
  structured semantic-obligation ledger
  already-licensed expanded/incremental totals only as descriptive fields

DeltaC:
  full C_plus set/fingerprint
  full C_minus set/fingerprint
  cardinalities as descriptive fields

R_collateral:
  six labeled component effects with component-level status/lineage

R_reopen:
  eight labeled binary stress results
  finite-panel frequency

Scope:
  coordinate-specific PASS/FAIL/NOT_TESTED support sets
  conservative common intersection as a set, never as a score
```

No serialization step may convert these objects into a common scalar.

---

# 19. Anti-ranking / anti-aggregation contract

The execution and result note must not compute or report:

- `s1 > s2` or any candidate ordering;
- pairwise preference matrices;
- Pareto dominance or Pareto fronts;
- weighted sums across coordinates;
- lexicographic orderings;
- normalized common scales across coordinates;
- win counts;
- rank correlations across candidates;
- adoption thresholds;
- `Q_extension`;
- `NO_WARRANTED_ADOPTION`;
- authorization status;
- binding status;
- a "best" synthesized candidate;
- a "best" external candidate;
- Rubi/Hudson superiority or inferiority.

Raw candidate records may be displayed in canonical candidate-ID order. Mere co-display is not a comparison result.

No result prose may interpret one vector as preferable to another.

---

# 20. No candidate pruning after measurement

The child executable must assert:

```text
expected_candidate_count = 12
observed_candidate_count = 12
post_measurement_pruning  = 0
post_measurement_addition = 0
```

Candidates with all coordinates `NOT_IDENTIFIED` remain in the result set.

Candidates with negative measured effects remain in the result set.

Candidates extensionally identical to another provenance object remain distinct records.

---

# 21. Upstream hard regression requirements

The child executable must import and hard-assert the measurement-identification result at `607502a`.

At minimum assert:

```text
M_DeltaV     calibration/invariance/F_k/lineage = 64/64 each
M_B          calibration/invariance/F_k/lineage = 64/64 each
M_DeltaC     calibration/invariance/F_k/lineage = 64/64 each
M_collateral calibration/invariance/F_k/lineage = 64/64 each
M_reopen     calibration/invariance/F_k/lineage = 64/64 each
M_scope      calibration/invariance/F_k/lineage = 64/64 each

X1..X5 = 64/64 each
Q_extension_defined = false
aggregation_defined = false
authorization_performed = false
binding_performed = false
```

The measurement-identification executable recursively carries the inherited synthesis assertions. The candidate-measurement result should therefore use provenance wording:

\[
\boxed{
\textbf{fresh candidate-measurement result with inherited hard regression assertions}.
}
\]

unless the upstream chain is independently rerun in that execution session.

---

# 22. Candidate-measurement success criterion

The gate passes only if all of the following hold:

1. exactly the 12 preregistered candidate records are present;
2. candidate identities and provenance match this registry before any coordinate values are computed;
3. all six instruments are checksum-anchored to the identified architecture;
4. every candidate-coordinate pair emits either a valid native `IDENTIFIED` value or `NOT_IDENTIFIED` with `null` value and explicit failed identification condition;
5. no `NOT_IDENTIFIED` value is imputed;
6. all native coordinate types and lineages are preserved;
7. all licensed anonymity/invariance checks remain satisfied;
8. no candidate is added, removed, or pruned after measurement;
9. no cross-coordinate aggregate exists;
10. no candidate ordering, Pareto filter, adoption rule, authorization rule, or binding operation is computed;
11. the Hudson external comparator is evaluated only where existing instrument scope licenses it and otherwise produces `NOT_IDENTIFIED` without instrument redesign;
12. no synthesized/external/control provenance records are merged even when semantic transformations or measured vectors coincide.

A partial coordinate record does not fail the entire candidate-measurement gate if the missing coordinate is correctly labeled `NOT_IDENTIFIED` for a preregistered scope reason. It fails only if the system misrepresents that lack of identification as a value or alters the instrument to avoid it.

---

# 23. Failure interpretation

| Observation | Interpretation |
|---|---|
| candidate removed after a negative measurement | post-measurement selection leakage |
| candidate removed because a coordinate is missing | missingness-to-selection leakage |
| `NOT_IDENTIFIED` serialized as `0` | invalid measurement record |
| external wrapper forces change to `M_k` | instrument redesign; preregistration invalid |
| candidate provenance lost after semantic deduplication | provenance collapse |
| hidden macro appears cheaper because visible syntax is shorter | burden-instrument violation |
| geometry scalar replaces set-valued delta | native-type loss |
| collateral mean replaces vector | unauthorized aggregation |
| reopenability replaced by immediate performance | coordinate collapse |
| scope failure overridden by favorable consequence | authority leakage from magnitude to validity |
| ranking/Pareto/frontier emitted | candidate-comparison leakage |
| all records emitted under frozen instruments | candidate measurement gate may pass |

---

# 24. Claim boundary if execution succeeds

The strongest permitted claim is exactly:

\[
\boxed{
\textbf{
The preregistered synthesized, external, and control candidate records were measured under the previously identified extension-measurement architecture, with provenance, native coordinate types, coordinate-specific lineage, explicit identification status, and scope preserved.
}
}
\]

A pass does **not** establish:

- that one candidate is better than another;
- Pareto dominance;
- any coordinate priority;
- any tradeoff rate between coordinates;
- any extension-value function;
- Rubi/Hudson superiority or inferiority;
- `NO_WARRANTED_ADOPTION`;
- authorization;
- binding;
- persistence;
- post-adoption consequence;
- general self-modification;
- research agency.

---

# 25. Frozen next sequence

The empirical sequence is now:

\[
\boxed{
\mathcal M_{\rm ext}\text{ identification}\checkmark
\rightarrow
\boxed{s\rightarrow\mathcal V_{\rm ext}(s)\text{ [preregistered]}}
\rightarrow
\text{candidate-measurement execution}
\rightarrow
\text{candidate comparison [undefined]}
\rightarrow
Q_{\rm extension}\text{ [undefined]}
\rightarrow
Auth\text{ [undefined]}
\rightarrow
Bind\text{ [undefined]}.
}
\]

The only authorized next repository action is execution of this candidate-measurement preregistration.

No dependency-ledger update, candidate-comparison artifact, `Q_extension` artifact, adoption artifact, authorization artifact, or binding artifact is authorized before that execution result exists.
