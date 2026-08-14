# Extension Measurement Architecture — Preregistration

## Status

This document freezes the next empirical object **before any extension-value aggregation is defined or executed**.

Parent dependency checkpoint:

```text
3483f4a  Update experiment-planning dependency consolidation after extension synthesis
```

Extension-synthesis empirical anchor:

```text
9a50f07  extension synthesis relative to supplied M0
```

Closure-diagnosis anchor:

```text
7e3871c  closure-insufficiency diagnosis
```

No extension-valuation result is recorded here.

No `Q_extension` function exists in this artifact. No candidate is ranked, preferred, adopted, authorized, or bound. No Rubi-style construction or other external comparator is used to define a measurement coordinate.

The governing boundary is:

\[
\boxed{
\text{measurement architecture}
\neq
\text{candidate comparison}
\neq
\text{value aggregation}
\neq
\text{authorization}
\neq
\text{binding}.
}
\]

The current object is only:

\[
\boxed{
\mathcal M_{\rm ext}
=
\{
M_{\Delta V},
M_B,
M_{\Delta C},
M_{\rm collateral},
M_{\rm reopen},
M_{\rm scope}
\}.
}
\]

Each coordinate is typed as:

\[
\boxed{
M_k=(O_k,do_k,m_k,\mathcal T_k,F_k,L_k),
}
\]

where:

- `O_k` is the identity of the scientific object;
- `do_k` is the intervention / causal contrast required to identify it;
- `m_k` is the observable measurement rule;
- `T_k` is the admissible transformation class under which the measurement claim must be preserved;
- `F_k` is a preregistered **measurement-invalidity signature**;
- `L_k` is the evidence lineage and identification scope supporting that coordinate.

The global methodological invariant is:

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

## 1. Global anti-aggregation contract

The six coordinates are measurement objects, not six automatically compensable terms in a utility function.

The preregistered anti-aggregation invariants are:

\[
\boxed{
\begin{aligned}
|\Delta\mathcal C|\uparrow
&\not\Rightarrow \text{better extension},\\
B_{\rm visible}\downarrow
&\not\Rightarrow B_{\rm extension}\downarrow,\\
R_{\rm reopen}\uparrow
&\not\Rightarrow \Delta V_{\rm corr}\uparrow,\\
\Delta V_{\rm corr}\uparrow
&\not\Rightarrow R_{\rm collateral}\text{ acceptable},\\
\text{within-scope effect}
&\not\Rightarrow \text{out-of-scope license}.
\end{aligned}
}
\]

The following are forbidden in this preregistration and in the subsequent measurement-identification execution:

- weights across measurement coordinates;
- a scalar aggregate extension score;
- lexicographic or Pareto extension ranking;
- an adoption threshold;
- `NO_WARRANTED_ADOPTION` as an operational outcome;
- authorization semantics;
- binding semantics;
- candidate-specific tuning of a measurement definition;
- using a preferred extension, synthesized candidate, Rubi-style comparator, or other named comparator to choose the coordinate system.

The meta-rule is:

\[
\boxed{
\textbf{No aggregate extension value exists until all six measurement objects have independently survived identification.}
}
\]

A positive result on one coordinate grants no measurement authority on another:

\[
\boxed{L_i\not\Rightarrow L_j\quad(i\neq j).}
\]

---

# 2. `M_DeltaV` — corrective consequence

## 2.1 `O_DeltaV`: object identity

The object is the **extension-attributable change in held-out corrective consequence** under a frozen correction contract.

For current construction substrate `S0`, candidate structural transformation `s`, frozen target contract `K*`, and frozen held-out consequence evaluator `E*`:

\[
\boxed{
\Delta V_{\rm corr}(s)
=
V_{\rm corr}(do(S_0\oplus s);K^\star,E^\star)
-
V_{\rm corr}(do(S_0);K^\star,E^\star).
}
\]

`V_corr` is not defined as candidate adequacy and is not identical to `CanRestore`. `CanRestore(s)=1` states only that at least one warranted continuation becomes reachable. `Delta V_corr(s)` measures the extension-attributable consequence under the held-out evaluator.

Thus:

\[
\boxed{
\operatorname{CanRestore}(s)=1
\not\Rightarrow
\Delta V_{\rm corr}(s)>0
}
\]

as a matter of measurement identity.

## 2.2 `do_DeltaV`: intervention contrast

The required contrast changes **only** the construction substrate:

```text
do(S = S0 + s)
vs
do(S = S0)
```

while holding fixed:

- latent world / environment realization;
- correction contract `K*`;
- downstream controller and acquisition policy;
- evaluator `E*`;
- commitment boundary;
- random seed or matched stochastic realization where applicable;
- measurement horizon.

The transformation may be instantiated in an isolated evaluator sandbox. Measurement does not authorize or bind the candidate into the live adaptive system.

An observational statement such as “the candidate run scored better” without this isolated contrast does not identify `Delta V_corr`.

## 2.3 `m_DeltaV`: measurement rule

For a finite deterministic panel, measure the exact paired difference in frozen `V_corr` over matched episodes.

For a stochastic panel, use paired/coupled realizations where possible and report:

```text
per-episode paired effects
mean paired effect
uncertainty interval defined before candidate evaluation
```

The child identification audit must use held-out consequence episodes that were not used to synthesize the candidate or define its semantic adequacy.

## 2.4 `T_DeltaV`: admissible transformations

`V_corr` is licensed only under positive affine transformations:

\[
V' = aV+b,\qquad a>0.
\]

Then:

\[
\Delta V'_{\rm corr}=a\Delta V_{\rm corr}.
\]

Therefore sign and additive causal ordering are preserved. Ratio claims about `Delta V_corr` are not licensed merely by this transformation class.

World-label, action-label, candidate-handle, and output-token relabelings that preserve episode semantics must also leave the measured causal contrast invariant up to the corresponding scale transformation.

## 2.5 `F_DeltaV`: measurement-invalidity signatures

`M_DeltaV` fails identification if any preregistered calibration case shows one or more of:

1. a semantic no-op / alias produces a nonzero causal effect;
2. changing a non-construction variable is required to obtain the reported effect;
3. matched intervention ordering changes under an admissible positive-affine transformation;
4. the effect disappears when synthesis data and held-out consequence data are separated;
5. candidate identity or syntax, rather than the intervention consequence, enters the instrument;
6. the estimator cannot recover a known controlled extension-attributable effect in the identification panel.

A candidate with `Delta V_corr <= 0` is **not** a measurement failure. That is a candidate result. `F_DeltaV` concerns whether the instrument identifies the causal object.

## 2.6 `L_DeltaV`: evidence lineage

The lineage must record at least:

```text
baseline substrate identifier
candidate semantic transformation fingerprint
frozen correction-contract identifier
held-out evaluator identifier
held-out episode / seed identifiers
measurement horizon
intervention implementation checksum
estimator / uncertainty rule
admissible transformation checks
calibration-control outcomes
```

`L_DeltaV` licenses claims only for the tested target/evaluator/horizon regime.

---

# 3. `M_B` — extension specification burden

## 3.1 `O_B`: object identity

The object is the **expanded semantic specification burden required to instantiate the candidate structural transformation**, with visible syntax separated from hidden or inherited obligations.

The primary burden object is a structured ledger:

\[
\boxed{
B_{\rm extension}(s)
=
\big(
B_{\rm explicit},
B_{\rm inherited},
B_{\rm hidden},
B_{\rm target\mbox{-}specific},
B_{\rm search},
B_{\rm external}
\big)_s.
}
\]

A declared clause-count total may also be reported:

\[
\boxed{
B^{\rm expanded}_{\rm extension}
=
B_{\rm explicit}
+B_{\rm inherited}
+B_{\rm hidden}
+B_{\rm target\mbox{-}specific}
+B_{\rm search}
+B_{\rm external}.
}
\]

This total is a specification-accounting count, **not** an information-theoretic complexity measure and not yet a value penalty.

For adoption-cost accounting, also report the incremental burden newly added relative to the already-supplied parent substrate:

\[
\boxed{
B^{\rm incremental}_{\rm extension}
=
B_{\rm explicit,new}
+B_{\rm hidden,new}
+B_{\rm target\mbox{-}specific,new}
+B_{\rm search,new}
+B_{\rm external,new}.
}
\]

Inherited dependencies remain visible in the expanded ledger even when they are not incrementally re-supplied.

## 3.2 `do_B`: causal/accounting contrast

The burden audit contrasts alternative representations or implementations of the **same extensional candidate transformation**.

The semantic obligation set is held fixed while visible representation is manipulated through:

- transparent aliases;
- macro packaging;
- handle renaming;
- clause reordering;
- explicit versus hidden mappings;
- inherited helper reuse;
- target-conditioned lookup or search hints.

The anti-scaffold question is mandatory:

\[
\boxed{\textbf{Where did the specification go?}}
\]

## 3.3 `m_B`: measurement rule

Expand each implementation to the smallest auditable set of semantic obligations required to reproduce the candidate transformation under the frozen execution environment.

Count and report separately:

```text
explicit new semantic clauses
required inherited semantic clauses
hidden macro / mapping obligations
target-specific semantic obligations
search / grammar constraints
external oracle or service obligations
```

Rules:

1. transparent aliases are charged their expanded semantics;
2. opaque macros are charged the semantics they hide, not the visible token count;
3. target-conditioned lookup tables are charged per target-specific binding;
4. inherited machinery is listed even when incremental cost is zero;
5. generic reusable rules are counted once at their actual semantic level;
6. semantic duplicates are deduplicated only when they are genuinely reusable obligations rather than repeated target-specific bindings.

## 3.4 `T_B`: admissible transformations

Licensed transformations are semantics-preserving representation rewrites:

- identifier renaming;
- clause reordering;
- transparent macro introduction/removal;
- equivalent parenthesization;
- replacement by a provably equivalent reusable generic rule.

`B_extension` must be invariant after semantic expansion under these transformations.

Arbitrary monotone rescaling of burden counts is **not** licensed. The clause ledger defines the measurement unit for this audit.

## 3.5 `F_B`: measurement-invalidity signatures

`M_B` fails if:

1. a transparent alias reduces expanded burden merely by shortening syntax;
2. an opaque macro hides semantic obligations that are not charged;
3. target-specific hints are treated as generic rules;
4. handle renaming or clause reordering changes expanded burden;
5. inherited dependencies disappear from the expanded ledger;
6. two extensionally identical implementations receive different burden solely because of superficial syntax;
7. the ledger cannot distinguish visible compression from genuine semantic specification reduction.

A high burden is not a measurement failure. Failure means the accounting instrument does not track the specified semantic obligation object.

## 3.6 `L_B`: evidence lineage

Record:

```text
candidate semantic fingerprint
implementation / macro expansion graph
source of every semantic obligation
new vs inherited status
visible vs hidden status
target-specific vs generic status
external dependency status
deduplication rationale
expanded and incremental totals
```

Burden evidence licenses only this declared specification unit and execution environment.

---

# 4. `M_DeltaC` — construction-space geometry

## 4.1 `O_DeltaC`: object identity

The native geometry object is **set-valued**, not scalar:

\[
\boxed{
\Delta\mathcal C(s)
=
\big(
\mathcal C_+(s),
\mathcal C_-(s)
\big),
}
\]

where:

\[
\mathcal C_+(s)
=
\mathcal C(S_0\oplus s)\setminus\mathcal C(S_0),
\]

and:

\[
\mathcal C_-(s)
=
\mathcal C(S_0)\setminus\mathcal C(S_0\oplus s).
\]

The objects are semantic experiment-partition equivalence classes under the frozen construction semantics.

Cardinalities may be reported descriptively:

```text
|C_plus|
|C_minus|
```

but no ordering of candidates follows from those cardinalities.

Thus:

\[
\boxed{
\text{larger space}
\neq
\text{different space}
\neq
\text{correction-relevant space}
\neq
\text{better extension}.
}
\]

## 4.2 `do_DeltaC`: intervention contrast

Recompute the semantic fixed-point experiment closure under:

```text
do(S = S0 + s)
vs
do(S = S0)
```

with world semantics, primitive evidence channels, deduplication rule, and output-partition equivalence held fixed.

No target value or candidate desirability enters the closure computation.

## 4.3 `m_DeltaC`: measurement rule

For each side of the contrast:

1. construct the complete admitted experiment family to its declared semantic fixed point;
2. canonicalize evidence partitions modulo the frozen output-token equivalence;
3. deduplicate semantically;
4. compute exact set differences;
5. report closure fingerprints and sizes;
6. retain the full set-valued delta, not merely cardinality.

When exhaustive closure is infeasible in a later domain, this measurement contract is not automatically licensed there; a separate identification regime is required.

## 4.4 `T_DeltaC`: admissible transformations

Geometry must be invariant up to semantic isomorphism under:

- world-state relabeling;
- primitive-handle renaming;
- candidate-handle renaming;
- action-label renaming;
- public binary output polarity flips;
- enumeration-order permutation.

A licensed transformation induces a bijection on partition classes. Under that bijection, `C_plus` and `C_minus` must be identical as semantic sets.

There is no licensed scalar monotone transformation that converts closure cardinality into value.

## 4.5 `F_DeltaC`: measurement-invalidity signatures

`M_DeltaC` fails if:

1. a syntax-only operator appears to expand geometry after semantic deduplication;
2. claimed new partitions vanish under the canonical equivalence relation;
3. handle or world relabeling changes the semantic delta beyond isomorphism;
4. incomplete closure enumeration is reported as complete;
5. target labels influence the geometry computation;
6. the instrument cannot recover a known add/remove partition intervention in the calibration panel.

A candidate with `C_plus = empty` is not by itself a measurement failure.

## 4.6 `L_DeltaC`: evidence lineage

Record:

```text
baseline construction-substrate identifier
candidate transformation fingerprint
closure rule / fixed-point algorithm
primitive evidence-channel identifiers
semantic equivalence rule
baseline closure size + checksum
candidate closure size + checksum
C_plus full fingerprint + cardinality
C_minus full fingerprint + cardinality
completeness certificate
anonymous-isomorphism checks
```

Geometry lineage supports only domains where closure completeness and semantic equivalence are identified.

---

# 5. `M_collateral` — collateral causal consequences

## 5.1 `O_collateral`: object identity

Collateral consequence is a **vector over frozen non-target contracts**, not a weighted penalty:

\[
\boxed{
R_{\rm collateral}(s)
=
(r_1(s),\ldots,r_m(s)),
}
\]

with:

\[
\boxed{
r_j(s)
=
V_j(do(S_0\oplus s);K_j,E_j)
-
V_j(do(S_0);K_j,E_j).
}
\]

The non-target contract family:

\[
\mathcal K_{\rm coll}=\{K_1,\ldots,K_m\}
\]

must be frozen **before** any candidate identity or external comparator is evaluated under this instrument.

The coordinate retains positive, zero, and negative collateral consequences separately by contract.

No mean, weighted sum, max-loss penalty, or scalar summary is a valid primary measurement object at this stage.

## 5.2 `do_collateral`: intervention contrast

For every frozen collateral contract `K_j`, compare:

```text
do(S = S0 + s)
vs
do(S = S0)
```

holding fixed the collateral world, evaluator, downstream policy, and horizon for that contract.

The active synthesis target is not permitted to redefine `K_coll` after candidate generation.

## 5.3 `m_collateral`: measurement rule

Measure a paired extension-attributable consequence for each frozen collateral contract separately.

Report:

```text
contract identifier
paired effect r_j
uncertainty / exactness statement
held-out episode identifiers
```

The native output remains the labeled vector.

## 5.4 `T_collateral`: admissible transformations

For each contract `j`, positive affine transformations of that contract's viability scale are licensed:

\[
V'_j=a_jV_j+b_j,\qquad a_j>0,
\]

so:

\[
r'_j=a_jr_j.
\]

Contract-index permutation is licensed only when the contract labels and their lineages are permuted consistently. Cross-contract averaging is not an admissible transformation.

## 5.5 `F_collateral`: measurement-invalidity signatures

`M_collateral` fails if:

1. a semantic no-op produces nonzero collateral effects;
2. an intervention known to affect one frozen contract contaminates unrelated vector coordinates through the measurement implementation;
3. candidate identity changes the collateral contract panel;
4. an aggregate scalar is substituted for the preregistered vector;
5. component ordering changes under an admissible positive-affine transformation within a contract;
6. held-out non-target contracts are not genuinely separated from synthesis/target data.

A negative collateral coordinate is a measured candidate consequence, not an instrument failure.

## 5.6 `L_collateral`: evidence lineage

Maintain independent lineage for every vector component:

```text
K_j identifier
E_j evaluator identifier
baseline substrate
candidate semantic fingerprint
held-out episode / seed set
horizon
paired effect estimate
uncertainty rule
admissible scale transformation
calibration outcome
```

No `L_j` may be generalized to another collateral contract without independent evidence.

---

# 6. `M_reopen` — future corrective reopenability

## 6.1 `O_reopen`: object identity

The object is the preservation of **later warranted corrective reachability** after the candidate transformation has been counterfactually instantiated.

Let the preregistered held-out stress family be:

\[
\mathcal R_{\rm stress}=\{\rho_1,\ldots,\rho_n\}.
\]

For stress episode `rho`, define:

\[
Y_{\rm reopen}(s,\rho)=1
\]

iff, after `do(S = S0 + s)` and the later stress is introduced, there exists an admissible evidence/refinement path that restores a strict-positive warranted corrective continuation before the frozen deadline under the frozen future challenge and refinement apparatus.

Otherwise:

\[
Y_{\rm reopen}(s,\rho)=0.
\]

The finite-panel reopenability measure is:

\[
\boxed{
R_{\rm reopen}(s)
=
\frac{1}{|\mathcal R_{\rm stress}|}
\sum_{\rho\in\mathcal R_{\rm stress}}
Y_{\rm reopen}(s,\rho).
}
\]

This is an empirical frequency over the frozen stress family, not a universal probability of corrigibility.

## 6.2 `do_reopen`: intervention contrast

The identification contrast applies the candidate in an isolated state, then introduces a **later** correction-requiring stress:

```text
do(S = S0 + s); then do(stress = rho)
vs
do(S = S0);     then do(stress = rho)
```

The later stress is held out from candidate synthesis and from immediate corrective-consequence evaluation.

Frozen across the comparison:

- future challenge channels;
- evidence access machinery;
- refinement controller;
- burden / continuation contract;
- authorization assumptions;
- deadline;
- stress realization.

No extra authority may be granted merely to make the candidate appear reopenable.

## 6.3 `m_reopen`: measurement rule

For finite audited regimes, recompute the future reachable-refinement graph exactly and determine `Y_reopen` from the existence of a warranted timely path.

Report:

```text
per-stress binary reachability
stress-family frequency R_reopen
baseline paired frequency
path / impossibility certificate where finite
```

Immediate task success is not a proxy for reopenability.

## 6.4 `T_reopen`: admissible transformations

Licensed transformations are semantic isomorphisms of the future stress episodes and repair graph:

- stress identifier permutation;
- world-state relabeling;
- action/experiment-handle renaming;
- public token-polarity relabeling preserving evidence partitions.

`Y_reopen` and the finite-panel frequency must remain invariant.

No monotone rescaling of `R_reopen` is licensed in this audit.

## 6.5 `F_reopen`: measurement-invalidity signatures

`M_reopen` fails if:

1. two interventions matched on immediate corrective consequence but known to differ in future path availability receive the same reopenability result when the finite graph proves otherwise;
2. a path-blocking transformation is scored as reopenable because the evaluator grants an extra challenge channel or authority not present in the frozen apparatus;
3. immediate `Delta V_corr` is substituted as a proxy for future reachability;
4. stress-label or world-label permutation changes the result;
5. a claimed reachable path violates the frozen burden, deadline, evidence, or authorization constraints;
6. a claimed impossibility result is made without exhaustive characterization in a domain where exhaustiveness is required.

A low `R_reopen` is a candidate result, not measurement invalidity.

## 6.6 `L_reopen`: evidence lineage

Record:

```text
candidate semantic fingerprint
stress-family definition + checksum
future challenge/evidence apparatus
refinement rules
deadline / commitment boundary
burden / continuation contract
per-stress reachability certificate
baseline paired reachability
anonymous-isomorphism checks
```

Reopenability evidence licenses only the frozen stress family and structurally validated transfer regimes.

---

# 7. `M_scope` — evidential support scope

## 7.1 `O_scope`: object identity

Scope is a **validity constraint**, never a compensable benefit.

For each causal/measurement coordinate `k`, define the coordinate-specific support set:

\[
\boxed{
\mathcal R_{s,k}
=
\{r:\text{the identification assumptions and validation checks for }M_k(s)\text{ hold in regime }r\}.
}
\]

The native scope object is the labeled tuple:

\[
\boxed{
\operatorname{Scope}(s)
=
(\mathcal R_{s,\Delta V},
\mathcal R_{s,B},
\mathcal R_{s,\Delta C},
\mathcal R_{s,\rm coll},
\mathcal R_{s,\rm reopen}).
}
\]

A conservative common support set may be reported descriptively:

\[
\boxed{
\mathcal R_s^{\cap}
=
\bigcap_k\mathcal R_{s,k}.
}
\]

This intersection is not a score. It is the largest regime set on which all required measurement coordinates are simultaneously supported under the frozen architecture.

Any future `Q_extension(s;r)` may be licensed no more broadly than the measurement lineage supporting the coordinates it uses. This statement constrains future validity; it does not define `Q_extension`.

## 7.2 `do_scope`: regime intervention

Identification of scope varies a preregistered regime descriptor while holding the candidate and measurement contract fixed.

Examples of regime dimensions that may be manipulated in the child identification audit include:

- world distribution;
- target family;
- deadline;
- evidence-access pattern;
- collateral-contract family;
- future stress family.

A regime enters `R_{s,k}` only when the coordinate-specific identification and invariance checks are actually satisfied there.

Untested regimes are not in scope by default.

## 7.3 `m_scope`: measurement rule

For every preregistered regime `r` and coordinate `k`:

```text
run M_k identification checks in r
record PASS / FAIL / NOT-TESTED
include r in R_{s,k} iff PASS
```

No interpolation, semantic similarity, or favorable candidate performance may substitute for an identification pass.

Report both coordinate-specific support sets and their conservative intersection.

## 7.4 `T_scope`: admissible transformations

Licensed transformations are bijective relabelings of regime identifiers that preserve all structural regime descriptors and measurement conditions.

Scope membership must be invariant under those relabelings.

There is no admissible numerical rescaling because scope is set-valued.

## 7.5 `F_scope`: measurement-invalidity signatures

`M_scope` fails if:

1. an untested regime is included as supported;
2. a regime remains in scope after its required coordinate identification check fails;
3. favorable effect magnitude is used to compensate for a failed validity condition;
4. regime relabeling changes support membership;
5. evidence from one coordinate silently enlarges another coordinate's scope;
6. out-of-scope extrapolation is presented as licensed measurement.

A narrow support set is not a measurement failure.

## 7.6 `L_scope`: evidence lineage

The scope lineage is the explicit matrix:

```text
(candidate semantic fingerprint, coordinate, regime)
    -> identification assumptions
    -> validation tests
    -> PASS / FAIL / NOT-TESTED
    -> source evidence
```

No support claim exists outside this matrix.

---

# 8. Cross-coordinate separation requirements

The child measurement-identification audit must include matched constructions demonstrating that the six objects are not silently proxies for one another.

At minimum, the calibration panel must contain the following qualitative crossings:

### X1 — geometry versus corrective consequence

Two transformations with different `DeltaC` but matched `Delta V_corr`, or one with larger geometry and zero corrective consequence.

Required conclusion:

\[
\boxed{|\Delta\mathcal C|\uparrow\not\Rightarrow\Delta V_{\rm corr}\uparrow.}
\]

### X2 — visible syntax versus expanded burden

Two extensionally identical transformations with different visible syntax / macro packaging but equal expanded semantic obligations.

Required conclusion:

\[
\boxed{B_{\rm visible}\downarrow\not\Rightarrow B_{\rm extension}\downarrow.}
\]

### X3 — immediate correction versus reopenability

Two transformations matched on held-out immediate `Delta V_corr` but differing in later warranted path preservation.

Required conclusion:

\[
\boxed{\Delta V_{\rm corr}\text{ matched}\not\Rightarrow R_{\rm reopen}\text{ matched}.}
\]

### X4 — corrective consequence versus collateral consequence

A transformation may improve the active correction contract while producing a negative effect on at least one frozen collateral contract.

Required conclusion:

\[
\boxed{\Delta V_{\rm corr}\uparrow\not\Rightarrow R_{\rm collateral}\text{ componentwise nonnegative}.}
\]

### X5 — effect magnitude versus scope

A strong measured effect in one validated regime and an invalid or untested measurement in another regime.

Required conclusion:

\[
\boxed{\text{effect magnitude inside }r_1\not\Rightarrow r_2\in\operatorname{Scope}.}
\]

These crossings are **measurement discriminants**, not extension rankings.

---

# 9. Measurement-identification audit obligations

The next execution artifact must test the instruments themselves before applying them to synthesized or external candidate comparisons.

## 9.1 Anonymous calibration encodings

Use at least 64 anonymous encodings for every finite calibration family where relabeling is meaningful.

At minimum randomize consistently:

- world-state labels;
- primitive / experiment handles;
- candidate handles;
- contract identifiers;
- stress identifiers;
- public binary output polarity;
- regime identifiers;
- enumeration order.

The measurement result must remain invariant under the licensed semantic transformations.

## 9.2 Required calibration controls

The child audit must contain at least:

```text
DeltaV:
  semantic no-op -> exact zero causal effect
  known controlled construction effect -> recovered exactly / within preregistered uncertainty

B_extension:
  transparent alias / reordering -> same expanded burden
  opaque hidden macro -> hidden semantics charged
  target-specific mapping -> target-specific burden charged

DeltaC:
  syntax-only no-geometry transformation -> empty semantic delta
  known basin-opening transformation -> exact known added partition set
  known removal transformation -> exact known removed partition set

R_collateral:
  semantic no-op -> zero vector
  contract-localized controlled effect -> only intended component changes

R_reopen:
  immediate-effect-matched path-preserving vs path-blocking pair -> separated correctly
  no extra evidence/authority injected by evaluator

Scope:
  validated within-scope regime -> included
  preregistered identification-failure regime -> excluded
  untested regime -> not included
```

The exact finite constructions implementing these controls must be encoded in the child executable and must not depend on the identity of any extension later evaluated for value.

## 9.3 Success criterion

The measurement architecture is identified in the audited finite regime only if **every** coordinate:

1. recovers its preregistered positive and negative calibration controls;
2. is invariant under its licensed transformation class;
3. triggers its `F_k` measurement-invalidity condition on deliberately broken controls;
4. preserves its independent `L_k` evidence lineage;
5. passes the cross-coordinate separation requirements;
6. introduces no aggregation or adoption semantics.

A partial pass does **not** license an aggregate extension value. Failed coordinates remain unresolved and must be repaired or scope-contracted before candidate measurement proceeds.

---

# 10. Provenance and anti-leakage

The coordinate system must be frozen independently of any extension that might later be compared.

The following objects are prohibited from defining, tuning, weighting, or selecting `M_k`:

- the synthesized A/B/C candidate identities from `9a50f07`;
- any future synthesized candidate that performs well or poorly;
- any Rubi-style corrigibility transformation;
- any other externally supplied preferred extension;
- any future authorization policy;
- any future adoption decision;
- leaderboard-like aggregate performance.

Future candidates may be **measured by** this architecture only after the architecture survives identification.

The provenance direction must remain:

\[
\boxed{
\mathcal M_{\rm ext}\text{ frozen}
\rightarrow
\{M_k(S_{\rm synth}),M_k(S_{\rm external}),M_k(S_{\rm controls})\}
}
\]

and never:

\[
\boxed{
S_{\rm preferred}
\rightarrow
\mathcal M_{\rm ext}.
}
\]

External comparator evidence is not synthesis evidence, and synthesis evidence is not measurement-identification evidence.

---

# 11. Failure interpretation

| Observation | Interpretation |
|---|---|
| `DeltaV` no-op is nonzero | corrective-consequence instrument invalid |
| burden falls under transparent alias after expansion | specification ledger invalid |
| geometry changes under semantic relabeling | geometry instrument invalid |
| collateral vector panel changes with candidate identity | collateral instrument contaminated |
| reopenability tracks immediate performance despite proven path difference | reopenability instrument invalid |
| untested/failed regime enters scope | scope instrument invalid |
| one coordinate fails while others pass | contract / scope revision for that coordinate only; no authority leakage |
| all six measurement contracts pass | finite-regime measurement architecture identified; candidate measurement may become the next gate |

No measurement-identification result, including a full pass, licenses candidate ranking or adoption.

---

# 12. Claim boundary if identification later succeeds

If the subsequent child audit passes all six contracts and all separation controls, the strongest permitted claim will be:

\[
\boxed{
\textbf{
In the audited finite regimes, the six extension-measurement objects are independently operationalized and identified under their preregistered intervention contrasts, invariance classes, failure signatures, and evidence lineages.
}
}
\]

That result would license **measurement of candidate transformations** under the validated coordinates.

It would not establish:

- an aggregate `Q_extension`;
- that any coordinate should receive positive or negative value weight;
- a ranking of synthesized candidates;
- a ranking of synthesized versus external candidates;
- Rubi superiority or inferiority;
- `NO_WARRANTED_ADOPTION`;
- authorization;
- binding;
- persistence;
- held-out post-adoption consequence;
- unrestricted research agency;
- self-modification.

---

# 13. Frozen next sequence

The empirical program is now parked at:

\[
\boxed{
\begin{aligned}
D_{\rm closure}&\checkmark\\
\widehat{\mathfrak S}_{\rm candidate}&\checkmark\\
\boxed{\mathcal M_{\rm ext}\text{ measurement architecture}}&\text{ [preregistered]}\\
\mathcal M_{\rm ext}\text{ identification audit}&\text{ next execution gate}\\
\mathcal V_{\rm ext}(s)&\text{ not yet instantiated on candidate comparisons}\\
Q_{\rm extension}&\text{ undefined}\\
Auth&\text{ undefined}\\
Bind&\text{ undefined}.
\end{aligned}
}
\]

The only authorized next repository action is execution of this measurement-identification preregistration.

No `P_ep` ledger update, candidate-comparison artifact, `Q_extension` artifact, Rubi-comparison artifact, adoption artifact, authorization artifact, or binding artifact is authorized before that execution result exists.
