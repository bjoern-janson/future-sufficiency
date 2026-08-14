# Decision-Substrate Language Identification — Specification-Completeness Gate

## Status

This document freezes the **specification-completeness gate** that must be satisfied before any decision-substrate identification round may enter characterization.

Parent round-firewall checkpoint:

```text
7e4e97aa9c5fe54b449f2ad82a7b1528f448106c
```

Parent architecture checkpoint:

```text
fe21bbe2cd48bd71011674edd16488b5a492f291
```

Non-semantic serialization erratum:

```text
9ee1fd5f49f2dc43889894b9617ea9333077dd05
```

This gate is frozen **before any concrete decision-substrate language family or calibration world is instantiated**.

The governing distinction is:

\[
\boxed{\textbf{
Specified does not imply specification-complete.
}}
\]

A round may contain text for every required object and still be underdetermined. Characterization is authorized only when the complete round specification closes every scientific degree of freedom required to determine the scientific outputs.

No concrete language, grammar, primitive, dimensionality, parameter domain, calibration relation, calibration generator, actual-target application, candidate ranking, governance selection, authorization, binding, or execution is introduced here.

---

# 1. Scientific purpose of this gate

The parent architecture and firewall already require that a round freeze:

\[
\mathcal R^{(v)}
=
\left(
\mathfrak L_{\rm DS}^{(v)},
\mathfrak K_{\rm cal}^{(v)},
A_{\rm DS}^{(v)},
B_{\rm DS}^{(v)},
\Pi_{\rm closure}^{(v)},
\Sigma_{\rm outcome}^{(v)}
\right)
\]

before calibration outcomes exist.

This gate asks a distinct question:

\[
\boxed{
\text{Does the frozen tuple determine one scientific experiment rather than a family of reasonable interpretations?}
}
\]

The operational criterion is:

> Could two competent, conforming, independent implementers produce materially different witness spaces or scientific outcomes while claiming to follow the same frozen round specification?

If **yes**, the round is not specification-complete and characterization is forbidden.

If **no**, up to explicitly licensed nuisance-equivalent encodings, the round may enter characterization.

The gate therefore separates:

\[
\boxed{
\text{specification failure}
\neq
\text{empirical representational failure}
\neq
\text{contraction failure}.
}
\]

A specification failure must never emit `NOT_REPRESENTABLE`, `REPRESENTABLE_AUTHORITY_INVALID`, `ADMISSIBLE_REPRESENTATION_NO_CONTRACTION`, or `FAITHFUL_CONTRACTION`.

---

# 2. Frozen specification-completeness object

Define:

\[
\boxed{
\operatorname{SpecComplete}(\mathcal R^{(v)})
=
C_L
\land C_A
\land C_B
\land C_\Pi
\land C_K
\land C_\Sigma
\land C_{\rm env}.
}
\]

where:

```text
C_L      language and witness-domain completeness
C_A      authority/admissibility completeness
C_B      witness-burden completeness
C_Pi     closure/admissible-closure/minimum completeness
C_K      calibration-world completeness
C_Sigma  outcome-classifier completeness
C_env    execution-environment semantic reproducibility completeness
```

Characterization is authorized iff:

\[
\boxed{
\operatorname{SpecComplete}(\mathcal R^{(v)})=1.
}
\]

The resulting authorization token is purely procedural:

```text
CHARACTERIZATION_AUTHORIZED
```

It is not a scientific result about any language.

If:

\[
\operatorname{SpecComplete}(\mathcal R^{(v)})=0,
\]

then the only permitted terminal action for this gate is:

```text
STOP_SPECIFICATION_REPAIR_REQUIRED
```

The round must return to design/specification work. No characterization result exists.

---

# 3. Gate precedence

This gate operates **after** a round specification has been frozen but **before** characterization execution.

The binding sequence is:

\[
\boxed{
\text{architecture}
\rightarrow
\text{round language/world specification}
\rightarrow
\text{specification-completeness certification}
\rightarrow
\text{characterization, iff certified}.
}
\]

The parent firewall remains binding:

\[
\mathcal Y_{\rm cal}^{(v)}
\not\longrightarrow
\mathcal R^{(v)}.
\]

Specification-completeness review may discover an underdetermination **before calibration outcomes exist**. Repairing that underdetermination before characterization is specification completion, not evidence-driven language adaptation.

Once characterization begins, this gate is immutable for the round. Any later scientific modification requires a new round/version under the parent firewall.

---

# 4. `C_L` — language and witness-domain completeness

For every language:

\[
\mathcal L_i
=
(\Sigma_i,
\mathcal G_i,
\llbracket\cdot\rrbracket_i,
A_i,
B_i,
\Pi_i),
\]

`C_L = 1` only if the round specification uniquely determines, up to explicitly licensed semantic equivalence:

\[
\boxed{
\Sigma_i,
\mathcal G_i,
\mathcal H_i(S),
\llbracket\cdot\rrbracket_i
}
\]

for every candidate-universe size `S` used in the frozen calibration world.

At minimum, the specification must determine:

```text
language identifier and version
finite/bounded alphabet or parameter domains
all primitive symbols/operators
operator arity and typing
composition rules
grammar depth/size bounds where applicable
normalization rules
witness validity predicate
candidate-index domain
pair-index domain where applicable
all latent-state domains
dimensionality domains
threshold/cutpoint domains
precision policy
matrix/graph/partition domains where applicable
exception syntax, if any
selector/module syntax, if any
canonical or equivalence-preserving witness serialization
deterministic decoder semantics for every legal witness
behavior for every boundary condition
behavior for duplicate/equal latent states
behavior under candidate permutation
behavior under pair swap
behavior under empty or degenerate substructures
complete definition of the witness universe H_L(S)
```

The following phrases are not specification-complete unless expanded into exact rules:

```text
reasonable range
standard representation
appropriate threshold
low dimensional
small graph
bounded complexity
usual normalization
natural ordering
sufficient precision
equivalent implementation
as needed
if helpful
etc.
```

A conforming implementation may choose different internal data structures only when those choices are proven nuisance-equivalent under the frozen confluence relation.

`C_L = 0` if any conforming implementer must exercise substantive judgment to determine whether a witness is legal or how it decodes.

---

# 5. Language-family membership completeness

The complete treatment family:

\[
\boxed{
\mathfrak L_{\rm DS}^{(v)}
=
\{\mathcal L_1,\ldots,\mathcal L_m\}
}
\]

must itself be frozen.

Language-family membership is part of the treatment definition.

`C_L = 1` therefore also requires:

```text
complete language registry
exact member count
exact language-version identifiers
hash of each language specification
no wildcard future members
no optional language activation based on performance
no post-characterization additions
no post-characterization deletions
no performance-based language filtering inside the round
```

Adding or removing a language after calibration exposure changes the round and requires `v -> v+1`.

---

# 6. `C_A` — authority/admissibility completeness

The parent architecture requires witness-level authority.

For every legal witness `h` in every frozen language, the admissibility predicate must be total:

\[
\boxed{
\operatorname{Adm}_{A_{\rm DS}^{(v)}}(h)\in\{0,1\}.
}
\]

`C_A = 1` only if no legal witness can reach an undefined authority case.

The round specification must provide exact rules for at least:

```text
candidate-handle use
anonymous candidate state
pair-addressed state
candidate identity
candidate provenance
candidate aliases/display names
candidate hashes/nonces
serialization positions
implementation tags
governance identifiers
external/inherited state
target-edge lookup
target-derived features
pair exceptions
selectors and module choice
latent labels
metadata channels
cached state
learned state
solver-generated auxiliary state
precomputed tables
random seeds
canonicalization artifacts
```

Every information channel available to decoding must be classified as one of:

```text
LICENSED_AND_COUNTED
LICENSED_COMMON_INFRASTRUCTURE
FORBIDDEN
NOT_AVAILABLE
```

No channel may remain implicitly available.

The authority predicate must specify transport requirements under candidate permutation, pair swap, serialization permutation, alias changes, nonce changes, provenance relabeling, and implementation-tag changes.

`C_A = 0` if an implementer can reasonably ask:

> Is this state licensed?

and the frozen specification does not mechanically answer.

---

# 7. Authority completeness is not language-level blacklisting

Authority remains witness-level.

A language may contain both admissible and inadmissible witnesses.

Therefore `C_A` does **not** require that every legal witness be admissible.

It requires that every legal witness have a determinate admissibility status.

Thus:

\[
\boxed{
\text{authority predicate totality}
\neq
\text{universal witness admissibility}.
}
\]

The empirical object remains:

\[
\mathcal H_{\mathcal L}^{A}(R)
=
\{h:\ R_h=R,\ \operatorname{Adm}(h)=1\}.
\]

---

# 8. `C_B` — witness-specific burden completeness

For every legal witness relevant to exact or minimum-burden adjudication, burden must be a total deterministic function:

\[
\boxed{
B_i:\mathcal H_i\rightarrow\mathbb N.
}
\]

The inherited burden decomposition is:

\[
B(h)
=
B_{\rm state}(h)
+
B_{\rm decoder}(h)
+
B_{\rm auxiliary}(h)
+
B_{\rm selector}(h)
+
B_{\rm exception}(h).
\]

`C_B = 1` only if the specification determines exactly how every possible witness obligation maps into these ledgers.

At minimum, burden rules must settle:

```text
per-candidate state
per-pair state
per-component state
latent dimensions
thresholds/cutpoints
matrices
partitions
graph edges/nodes where semantically stored
operator instances
operator types
branch semantics
decoder branches
module selectors
exception state
precision obligations
symbolic constants
macros and their expanded semantic burden
common infrastructure exclusions
inherited/external state
cached/precomputed state
compressed encodings
shared subexpressions
reused parameters
symmetry reductions
canonicalization machinery
```

Burden cannot depend on implementation byte size, accidental compression, variable names, file format, compiler optimization, or runtime memory layout unless a future separately frozen scientific object explicitly changes the burden semantics.

The gate requires semantic-obligation accounting, not storage optimization.

`C_B = 0` if two conforming implementers can assign materially different burden to the same semantic witness.

---

# 9. `B*_L(R)` remains downstream of admissibility

This gate preserves the parent ordering.

For a target relation `R`:

\[
B^*_{\mathcal L}(R)
=
\min_{h\in\mathcal H^A_{\mathcal L}(R)}B(h)
\]

is defined only when:

\[
\mathcal H^A_{\mathcal L}(R)\neq\varnothing.
\]

If no admissible exact witness exists:

```text
B_star = NOT_DEFINED
```

A complete burden function does not authorize burden comparison for authority-invalid exact witnesses.

---

# 10. `C_Pi` — certification-procedure completeness

The closure/minimum procedure is explicitly tripartite:

\[
\boxed{
\Pi_{\mathcal L}
=
\left(
\Pi^{\rm unrestricted}_{\mathcal L},
\Pi^{\rm admissible}_{\mathcal L},
\Pi^{\rm minimum}_{\mathcal L}
\right).
}
\]

These are three different certification claims.

`C_Pi = 1` requires each component to have:

```text
exact input type
exact output type
complete algorithm/decision procedure
soundness argument
completeness argument
termination argument on the frozen domain
all pruning rules stated
all equivalence reductions stated
all normalization reductions stated
certificate serialization defined
failure behavior defined
```

A search executable without a completeness argument is not sufficient.

---

# 11. `Pi_unrestricted` completeness

`Pi_unrestricted_L` decides:

\[
\boxed{
R\in\mathrm{Cl}_{\mathcal L}
\quad\text{or}\quad
R\notin\mathrm{Cl}_{\mathcal L}.
}
\]

A negative result is licensed only if the procedure exhausts or exactly decides the complete frozen witness theory.

Permitted complete methods include, where formally justified:

```text
complete finite enumeration
exact CSP
exact SAT/SMT over a bounded finite domain
exact graph-isomorphism reduction
exact dynamic programming
algebraic decision procedure
exhaustive canonical-form enumeration
other exactly equivalent complete finite proof procedure
```

Forbidden substitutions include:

```text
search timeout
optimizer failure
no witness found yet
best mismatch > 0
local-search failure
random-search failure
beam-search failure
solver UNKNOWN
resource exhaustion
```

If the procedure cannot decide the required membership exactly, the specification-completeness gate fails for this round; characterization is not permitted to manufacture `NOT_REPRESENTABLE`.

---

# 12. `Pi_admissible` completeness

If unrestricted closure membership is positive, `Pi_admissible_L` independently decides:

\[
\boxed{
R\in\mathrm{Cl}^{A}_{\mathcal L}
\quad\text{or}\quad
R\notin\mathrm{Cl}^{A}_{\mathcal L}.
}
\]

It must account for all unrestricted exact witnesses or use an exactly equivalent complete decision reduction.

Finding one authority-invalid exact witness does not prove absence of an admissible exact witness.

Likewise, finding one admissible exact witness settles positive membership but does not by itself establish minimum burden.

`Pi_admissible_L` must serialize either:

```text
ADMISSIBLE_CLOSURE_MEMBER + exact admissible witness/certificate
```

or:

```text
ADMISSIBLE_CLOSURE_NONMEMBER + exact completeness certificate
```

No heuristic authority-negative state exists.

---

# 13. `Pi_minimum` completeness

If admissible closure membership is positive, `Pi_minimum_L` certifies:

\[
\boxed{
B^*_{\mathcal L}(R)
=
\min_{h\in\mathcal H^A_{\mathcal L}(R)} B(h).
}
\]

The procedure must prove both:

```text
existence: at least one admissible exact witness of burden b exists
lower bound: no admissible exact witness of burden < b exists
```

Finding a witness of burden `b` proves only the first statement.

A complete minimum certificate may use:

```text
complete enumeration
exact branch-and-bound with sound lower bounds
exact dynamic programming
exact finite optimization with completeness proof
other exactly equivalent exhaustive/decision procedure
```

The minimizer object is set-valued.

Where multiple minimum witnesses exist, retain:

\[
\mathcal H^*_{\mathcal L}(R)
=
\arg\min_{h\in\mathcal H^A_{\mathcal L}(R)}B(h)
\]

or a lossless frozen equivalence-class certificate.

No arbitrary canonical witness may substitute for proof of minimum completeness.

---

# 14. Separation of the three certification claims

The following implications are explicitly invalid:

\[
\boxed{
\text{no cheap witness found}
\not\Rightarrow
R\notin\mathrm{Cl}^{A}_{\mathcal L}
}
\]

\[
\boxed{
\text{no admissible witness found by one search}
\not\Rightarrow
R\notin\mathrm{Cl}^{A}_{\mathcal L}
}
\]

\[
\boxed{
\exists h:\ B(h)=b
\not\Rightarrow
B^*_{\mathcal L}(R)=b.
}
\]

The three serialized certificates must remain distinct:

```text
unrestricted_closure_certificate
admissible_closure_certificate
minimum_burden_certificate
```

---

# 15. `C_K` — calibration-world completeness

The frozen calibration world:

\[
\boxed{
\mathfrak K_{\rm cal}^{(v)}
}
\]

is part of the treatment definition, not a sampling convenience.

`C_K = 1` only if the round specification completely determines the calibration relations or the exact procedure that generates them before any characterization outcome exists.

The specification must freeze at minimum:

```text
structural-axis registry
allowed value set for every axis
generator family for every structural cell
generator parameter domains
candidate-count domains
relation-count/cardinality rules
matched-discriminant construction
which axes are held fixed in each contrast
which axis is manipulated in each contrast
target-token count matching rules
equivalence-class size matching rules
resolved/abstaining edge matching rules
connectivity matching rules
latent-generator certificates
finite enumeration versus sampling status
sampling weights/frequencies
random/deterministic seeds
sample count or exact stopping rule
duplicate handling
isomorphism/canonicalization handling
control-relation generators
nuisance-encoding construction
nuisance-encoding count
pair-swap construction
serialization order
artifact naming and hashing
```

The calibration generator must not choose relations conditionally on observed language performance.

`C_K = 0` if an implementer must decide which calibration cases are “representative,” “interesting,” “sufficient,” or “necessary” after the round specification freeze.

---

# 16. Calibration-world determinacy versus universal closure

A specification-complete calibration world may still be a finite sample from a larger structural class.

Therefore:

\[
\boxed{
C_K=1
\not\Rightarrow
\text{universal structural-class closure is identified}.
}
\]

The parent rule remains binding: universal class claims require exhaustive enumeration of the frozen class or an exact proof/decision reduction covering every class member.

Specification completeness concerns **what experiment is being run**, not the scope of claims beyond that experiment.

---

# 17. `C_Sigma` — outcome-classifier completeness

The scientific outcome classifier must contain no substantive discretion.

For each target-language pair, it is the deterministic function:

\[
\boxed{
\Sigma_{\rm outcome}
=
f\!\left(
\operatorname{Rep}_{\mathcal L}(R),
\operatorname{Rep}^{A}_{\mathcal L}(R),
B^*_{\mathcal L}(R),
B_R
\right).
}
\]

The frozen mapping remains:

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

`C_Sigma = 1` only if every logically reachable certified input state maps to exactly one terminal scientific state.

No implementation may substitute qualitative judgment such as:

```text
close enough
nearly representable
small burden difference
practically contracting
approximately admissible
mostly exact
```

Approximation diagnostics may be descriptive only if separately frozen; they cannot alter the four-state classifier.

---

# 18. Gate failure is outside `Sigma_outcome`

Specification-completeness failure is a **pre-characterization procedural failure**, not a fifth language outcome.

Thus:

```text
STOP_SPECIFICATION_REPAIR_REQUIRED
```

is not an element of:

\[
\Sigma_{\rm outcome}.
\]

This preserves the ontology:

\[
\boxed{
\text{experiment not well-defined}
\neq
\text{well-defined experiment returns nonrepresentability}.
}
\]

---

# 19. `C_env` — semantic execution reproducibility envelope

The environment is not a seventh scientific object.

Its sole purpose is to enforce:

\[
\boxed{
\text{same frozen scientific specification}
\Rightarrow
\text{same semantic execution}.
}
\]

`C_env = 1` requires enough computational state to be pinned that runtime variation cannot change the effective witness universe, authority result, burden, closure result, minimum result, or terminal status.

At minimum freeze/hash as applicable:

```text
source code implementing the round specification
language specification artifacts
calibration generator artifacts
closure/minimum executables
runtime language version
material dependency versions
solver name/version when solver semantics matter
solver options that affect semantics or completeness
random seeds
canonical serialization rules
canonical ordering rules
integer/finite precision policy
floating-point use, if any
numerical tolerance, if any
locale-sensitive behavior, if any
hash algorithm
artifact hashes
input artifact hashes
output schema version
```

Where the scientific object is purely discrete, exact arithmetic is preferred. If floating point is unavoidable, all tolerance and rounding semantics must be frozen before characterization.

---

# 20. No post-freeze mutable semantic state

`C_env = 1` additionally requires:

```text
no_post_freeze_mutable_state = true
```

with respect to any state capable of changing scientific outputs.

Forbidden output-affecting mutable state includes, unless explicitly frozen as part of the round:

```text
learned lookup tables
adaptive caches
persistent solver hints that alter completeness
online-fitted parameters
model checkpoints updated during characterization
self-modifying grammar state
auto-generated exception tables
outcome-dependent memoization used as semantic state
network-fetched state
current-time dependent state
machine-specific nondeterministic ordering that changes semantics
unseeded randomness
```

Ordinary performance caches are permitted only if proven semantics-preserving and not exposed as scientific state.

The relevant distinction is:

\[
\boxed{
\text{mutable implementation optimization}
\neq
\text{mutable scientific semantics}.
}
\]

---

# 21. All scientific degrees of freedom must be closed

The certificate manifest must contain:

```text
all_scientific_degrees_of_freedom_closed = true
```

This field is `true` only if the six scientific round objects and their reproducibility envelope leave no unresolved scientific choice to characterization execution.

Examples of unresolved scientific degrees of freedom include:

```text
choosing a threshold range after seeing a case
selecting among decoder variants at runtime
choosing which burden interpretation is favorable
choosing whether a metadata field counts as authorized
choosing a calibration cell because it is informative
choosing how many relations to generate after inspecting results
selecting a closure search depth adaptively
choosing a numerical tolerance post hoc
adding a fallback pair exception
removing a poorly performing language
```

Any such possibility forces this field to `false`.

---

# 22. Implementation confluence

The independent-implementer criterion is formalized as an implementation-confluence requirement.

Let `I_1` and `I_2` be two conforming independent implementations of the same frozen round specification.

Require:

\[
\boxed{
I_1(\mathcal R^{(v)})
\simeq
I_2(\mathcal R^{(v)}).
}
\]

Here `\simeq` does not require byte-identical intermediate data structures.

It identifies only explicitly licensed nuisance-equivalent implementation differences.

The following scientific objects must agree exactly, up to frozen witness equivalence where appropriate:

\[
\boxed{
\mathrm{Cl}_{\mathcal L},
\mathrm{Cl}^{A}_{\mathcal L},
B^*_{\mathcal L}(R),
\mathcal H^*_{\mathcal L}(R),
\Sigma_{\rm outcome}.
}
\]

Calibration-relation generation must also agree exactly or agree under the frozen generator distribution/seed semantics.

---

# 23. Licensed nuisance differences under confluence

Examples of differences that may be declared nuisance-equivalent include:

```text
0-based versus 1-based anonymous candidate handles
different internal object layouts
different hash-map implementations
different traversal order when canonicalized before semantics
different variable names
different source-code formatting
different but proven equivalent exact CSP encodings
different witness serialization that maps bijectively to the same frozen semantic equivalence classes
```

They are licensed only if they cannot change any scientific output or burden obligation.

A difference is **not** nuisance-equivalent merely because two implementers both call it “equivalent.” The equivalence relation itself must be frozen or derivable from the frozen semantics.

---

# 24. Confluence certification

A later concrete round specification must include a confluence plan capable of detecting underspecification before characterization.

Permitted evidence includes:

```text
independent reference implementation
independent executable implementation
cross-implementation golden cases derived from the frozen language only
formal equivalence proof
exhaustive comparison on a bounded specification test domain
property-based equivalence tests with an exact finite support
independent serialization/deserialization implementation
```

A single implementation agreeing with itself is not confluence evidence.

The specification-completeness gate may use deliberately synthetic specification-test cases that are not calibration evidence, provided they are generated solely to test interpretation of the frozen specification and do not characterize language performance over `K_cal`.

Such cases must be labeled:

```text
SPECIFICATION_CONFORMANCE_EVIDENCE
```

They may not be reused as confirmatory calibration evidence without separate preregistration.

---

# 25. Specification conformance is not calibration

The gate distinguishes:

```text
SPECIFICATION_CONFORMANCE_EVIDENCE
CALIBRATION_EVIDENCE
```

Conformance evidence asks:

> Do independent implementations agree on what the frozen experiment means?

Calibration evidence asks:

> What closure, admissibility, burden, and outcome properties does the frozen language exhibit over the frozen calibration world?

Conformance cases must not be selected to establish favorable representational properties.

Passing conformance does not count toward language characterization.

---

# 26. Required completeness manifest

The later round specification must emit a machine-readable specification-completeness manifest containing at minimum:

```text
round_id
round_version
round_specification_commit
round_specification_hash
parent_architecture_commit
parent_firewall_commit

language_registry_complete
language_membership_frozen
language_specification_hashes
witness_domains_complete
witness_validity_total
decoder_semantics_total
boundary_semantics_total
language_equivalence_relation_frozen

authority_predicates_total
authority_channel_registry_complete
authority_transport_rules_complete

burden_functions_total
burden_common_infrastructure_frozen
burden_expansion_rules_complete

unrestricted_closure_procedures_complete
unrestricted_completeness_arguments_present
admissible_closure_procedures_complete
admissible_completeness_arguments_present
minimum_burden_procedures_complete
minimum_completeness_arguments_present

calibration_world_complete
calibration_axis_registry_complete
calibration_generator_complete
matched_discriminants_complete
calibration_cardinality_or_stopping_rule_frozen
calibration_seeds_frozen
control_generators_complete
nuisance_world_frozen
pair_swap_world_frozen

classification_function_total
classification_mapping_frozen

runtime_versions_pinned
material_dependencies_pinned
solver_semantics_pinned
canonical_serialization_frozen
precision_policy_frozen
artifact_hashes_complete
no_post_freeze_mutable_state

implementation_confluence_relation_frozen
implementation_confluence_plan_complete
all_scientific_degrees_of_freedom_closed
actual_target_access_prohibited
within_round_mutability_zero

C_L
C_A
C_B
C_Pi
C_K
C_Sigma
C_env
SpecComplete
characterization_authorized
```

The corrected inherited serialization spelling is always:

```text
anonymous_candidate_count
```

where candidate counts are later serialized for calibration cases.

---

# 27. Hard Boolean consistency rules

The manifest must satisfy:

\[
\boxed{
\texttt{SpecComplete}
=
C_L\land C_A\land C_B\land C_\Pi\land C_K\land C_\Sigma\land C_{\rm env}.
}
\]

and:

```text
characterization_authorized = SpecComplete
```

The following must be true whenever `SpecComplete = true`:

```text
all_scientific_degrees_of_freedom_closed = true
no_post_freeze_mutable_state              = true
actual_target_access_prohibited           = true
within_round_mutability_zero              = true
```

No human override field exists.

There is no:

```text
force_characterization
accept_minor_ambiguity
proceed_with_caveat
best_effort_specification
```

switch.

---

# 28. Gate output vocabulary

This gate has exactly two procedural outputs:

```text
CHARACTERIZATION_AUTHORIZED
STOP_SPECIFICATION_REPAIR_REQUIRED
```

These are not elements of `Sigma_outcome`.

The mapping is:

```text
SpecComplete = true
  -> CHARACTERIZATION_AUTHORIZED

SpecComplete = false
  -> STOP_SPECIFICATION_REPAIR_REQUIRED
```

If stopped, the failed completeness coordinates must be retained explicitly.

Example:

```text
C_L     true
C_A     true
C_B     false
C_Pi    true
C_K     true
C_Sigma true
C_env   true

SpecComplete false
failed_coordinates [C_B]
```

No attempt may reinterpret a failed coordinate as an empirical language result.

---

# 29. Specification repair semantics

If this gate fails **before calibration execution**, the round may be repaired by completing the underspecified object, provided:

```text
no calibration outcomes have been generated or inspected;
no actual target artifacts are used;
the repaired specification receives a new immutable commit/hash;
the completeness certificate is rerun from scratch;
the old failed specification remains in provenance.
```

This is not evidence-driven within-round adaptation because no characterization evidence exists.

If calibration evidence has already been exposed, any semantic repair follows the parent firewall and requires a new version/round.

---

# 30. Classification must contain no substantive discretion

Once:

```text
CHARACTERIZATION_AUTHORIZED
```

is emitted, the later classification layer is required to be a deterministic consequence of certified upstream objects.

Any scientific disagreement during execution must be localizable to one of:

\[
\boxed{
\mathcal L_i,
A_i,
B_i,
\Pi_i,
\mathfrak K_{\rm cal}^{(v)},
\Sigma_{\rm outcome},
\text{or the reproducibility envelope}.
}
\]

The classification layer cannot resolve disagreements by interpretation.

---

# 31. Treatment-set interpretation

The language family is frozen as a treatment set:

\[
\boxed{
\mathfrak L_{\rm DS}^{(v)}
\text{ is a treatment set, not a candidate pool.}
}
\]

The calibration world is likewise part of the treatment definition:

\[
\boxed{
\mathfrak K_{\rm cal}^{(v)}
\text{ is part of the experimental world, not a sampling convenience.}
}
\]

Therefore, characterization may not:

```text
add a language
remove a language
modify a language
add a calibration regime
remove a calibration regime
rebalance calibration frequencies
regenerate unfavorable cases
change matched controls
change nuisance encodings
change stopping rules
```

without leaving the round.

---

# 32. Reproducible-from-commit requirement

A specification-complete round must be reconstructible from immutable repository state and explicitly retained external runtime anchors, if any.

The intended invariant is:

\[
\boxed{
\texttt{round_v specification commit}
\Rightarrow
\begin{array}{l}
\text{language family}\\
\text{witness domains}\\
\text{authority rules}\\
\text{burden rules}\\
\text{closure/minimum procedures}\\
\text{completeness arguments}\\
\text{calibration world}\\
\text{environment envelope}
\end{array}
}
\]

A reader should not need an undocumented conversation, notebook state, local cache, private convention, or implementer memory to determine the scientific experiment.

---

# 33. Environment does not become a hidden scientific variable

`C_env` is a reproducibility envelope, not a new representational treatment dimension.

The environment may be varied in robustness checks only if the scientific semantics are proven invariant.

If changing the environment changes:

```text
legal witness domain
decoder outputs
authority status
burden
closure membership
minimum burden
terminal status
```

then the supposedly irrelevant environment was carrying scientific semantics and the specification was not complete.

---

# 34. Broken controls / forbidden shortcuts

The later gate implementation must explicitly reject the following.

## S1 — headings-present fallacy

All six round objects have text, so call the round complete.

```text
failure: SPECIFIED_NOT_SPECIFICATION_COMPLETE
```

## S2 — unresolved witness legality

A runtime implementation decides whether a borderline witness is permitted.

```text
failure: WITNESS_DOMAIN_UNDERSPECIFIED
```

## S3 — unresolved decoder semantics

A runtime implementation chooses a reasonable boundary or tie behavior.

```text
failure: DECODER_SEMANTICS_UNDERSPECIFIED
```

## S4 — authority judgment at runtime

An implementation manually decides whether a data channel is licensed.

```text
failure: AUTHORITY_PREDICATE_UNDERSPECIFIED
```

## S5 — burden interpretation at runtime

An implementation decides whether an operation/state/selector counts.

```text
failure: BURDEN_FUNCTION_UNDERSPECIFIED
```

## S6 — search absence called closure certificate

No witness is found and the implementation emits nonrepresentability without complete adjudication.

```text
failure: UNRESTRICTED_COMPLETENESS_MISSING
```

## S7 — authority-negative from one cheating witness

One authority-invalid exact witness is found and the implementation concludes no admissible witness exists.

```text
failure: ADMISSIBLE_COMPLETENESS_MISSING
```

## S8 — found burden called minimum burden

A burden-`b` witness is found and `B_star=b` is reported without lower-bound proof.

```text
failure: MINIMUM_COMPLETENESS_MISSING
```

## S9 — adaptive calibration generator

Calibration cases are generated or reweighted after observing language outcomes.

```text
failure: CALIBRATION_WORLD_UNDERSPECIFIED_OR_ADAPTIVE
```

## S10 — outcome discretion

A near miss is manually promoted to a more favorable terminal state.

```text
failure: CLASSIFIER_DISCRETION
```

## S11 — mutable learned semantic state

A cache/table/model/solver state changes the effective scientific output after freeze.

```text
failure: POST_FREEZE_MUTABLE_SEMANTICS
```

## S12 — one implementation certifies its own interpretation

One executable agrees with itself and calls that implementation confluence.

```text
failure: CONFLUENCE_NOT_INDEPENDENT
```

## S13 — implementation differences called nuisance without proof

Two implementations disagree scientifically and the difference is hand-waved as equivalent.

```text
failure: NUISANCE_EQUIVALENCE_UNFROZEN
```

## S14 — specification failure emitted as `NOT_REPRESENTABLE`

The experiment is underdetermined, but a scientific closure state is emitted anyway.

```text
failure: SPECIFICATION_TO_EMPIRICAL_STATUS_LEAKAGE
```

## S15 — forced characterization override

A human or executable bypasses `SpecComplete = 0`.

```text
failure: SPECIFICATION_GATE_BYPASS
```

## S16 — actual target used to close ambiguity

An underspecified choice is resolved by selecting the interpretation that behaves best on an actual target.

```text
failure: ACTUAL_TARGET_SPECIFICATION_LEAKAGE
```

---

# 35. Required specification-test controls

A later concrete round should include conformance tests sufficient to expose at least:

```text
witness-domain ambiguity
decoder-boundary ambiguity
authority-channel ambiguity
burden-accounting ambiguity
closure-pruning unsoundness
minimum-burden lower-bound failure
serialization-order dependence
candidate-handle dependence
pair-swap dependence
unseeded nondeterminism
mutable semantic cache dependence
solver-option semantic dependence
```

These are specification/conformance controls, not calibration fixtures.

Their purpose is to test whether the frozen round has one interpretation.

---

# 36. Success criteria

The specification-completeness gate passes only if all of the following hold:

1. the language treatment family is complete and immutable;
2. every language has a total legal-witness definition;
3. every legal witness has total deterministic decoder semantics;
4. every legal witness has a determinate authority status;
5. every relevant witness has a determinate semantic burden;
6. unrestricted closure has a complete exact decision/certification procedure;
7. admissible closure has a separate complete exact decision/certification procedure;
8. minimum burden has a separate complete exact optimization certificate;
9. the calibration world/generator is fully frozen and reproducible;
10. matched discriminants and nuisance worlds are completely specified;
11. the four-state classifier is total and deterministic;
12. the runtime/dependency/solver/precision envelope cannot change scientific semantics;
13. no output-affecting post-freeze mutable state exists;
14. implementation nuisance equivalence is frozen;
15. an implementation-confluence plan exists;
16. all scientific degrees of freedom are closed;
17. actual-target access remains prohibited for specification completion;
18. within-round mutability remains zero;
19. all seven completeness coordinates are true;
20. `SpecComplete = true` is mechanically derived from those coordinates.

---

# 37. Anti-downstream flags

At this checkpoint:

```text
specification_completeness_gate_frozen        = true
round_firewall_architecture_frozen            = true
concrete_language_universe_instantiated       = false
calibration_world_instantiated                = false
calibration_generator_instantiated            = false
round_specification_complete                  = false
characterization_authorized                   = false
characterization_executed                     = false
application_set_frozen                        = false
actual_target_application_preregistered       = false
actual_target_application_performed           = false
actual_Q_extension_defined                    = false
governance_contract_selected                  = false
candidate_ranking_performed                   = false
candidate_adoption_selected                   = false
authorization_performed                       = false
binding_performed                             = false
execution_performed                           = false
```

`round_specification_complete = false` here means simply that no concrete round has yet been instantiated and certified. It is not a failed future round.

No dependency-ledger update is implied.

---

# 38. Strongest permitted claim

The strongest claim licensed by this artifact alone is:

\[
\boxed{\textbf{
Decision-substrate characterization now requires a separate specification-completeness certification after round specification and before empirical characterization. A round is characterization-authorized only when its language/witness domain, authority predicate, witness burden, unrestricted/admissible/minimum certification procedures, calibration world, outcome classifier, and semantic execution environment jointly close all scientific degrees of freedom and support implementation-confluent scientific outputs.
}}
\]

This artifact does not establish:

```text
that any concrete round is specification-complete
that any concrete language exists
that any language is representable or nonrepresentable on any calibration relation
that any language has an admissible witness
that any burden minimum has been computed
that any language contracts
that any structural regime is closed
that any actual target can be represented or contracted
that any language should enter the application set
that any governance contract is better
that Q_extension exists
```

---

# 39. Frozen state machine

The pre-application decision-substrate program now follows:

\[
\boxed{
\begin{array}{c}
\text{architecture}\\
\downarrow\\
\text{round language/world specification}\\
\downarrow\\
\operatorname{SpecComplete}(\mathcal R^{(v)})?\\
\begin{array}{cc}
\swarrow\ 0 & 1\ \searrow\\
\text{STOP: specification repair} & \text{characterization authorized}
\end{array}\\
\qquad\qquad\downarrow\\
\qquad\Phi_{\mathfrak L^{(v)}}(K)\\
\qquad\qquad\downarrow\\
\qquad\text{application-set freeze}\\
\qquad\qquad\downarrow\\
\qquad\text{actual application preregistration}\\
\qquad\qquad\downarrow\\
\qquad\text{actual application}
\end{array}
}
\]

The scientific classifier is unreachable when `SpecComplete = 0`.

---

# 40. Governing invariants added by this gate

Freeze the following:

\[
\boxed{\textbf{
Specified does not imply specification-complete.
}}
\]

\[
\boxed{\textbf{
No empirical representational status may be emitted by an underdetermined experiment.
}}
\]

\[
\boxed{\textbf{
Closure certification, admissible-closure certification, and minimum-burden certification are three distinct completeness claims.
}}
\]

\[
\boxed{\textbf{
Two conforming implementations may differ in nuisance encoding but not in scientific semantics.
}}
\]

\[
\boxed{\textbf{
Once specification completeness passes, execution may compute consequences but may not invent scientific rules.
}}
\]

---

# 41. Stop condition

Stop after freezing this specification-completeness gate.

Do not in this commit:

```text
instantiate a concrete language family
choose language primitives
choose language dimensionality
choose language parameter ranges
instantiate a calibration structural domain
construct calibration relations
choose calibration frequencies
choose calibration seeds for a concrete round
write a concrete round executable
run specification conformance
run implementation confluence tests
certify a concrete round as SpecComplete
execute characterization
freeze an application set
read actual target artifacts for design
apply any language to actual targets
define Q_extension
rank candidates
select governance
adopt
authorize
bind
execute
update the dependency ledger
```

The next scientific artifact is a **concrete round language-family + calibration-world specification** that must subsequently pass this gate before characterization.