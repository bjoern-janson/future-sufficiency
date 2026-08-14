# Decision-Substrate Language Identification — Architecture Preregistration

## Status

This document freezes the **architecture** for the next decision-substrate stage before any new concrete representational language is instantiated.

Parent checkpoint:

```text
3c43eb835dcd445845a471d25929284f659e69df
```

Frozen parent execution:

```text
extension candidate scalar application executable
  e93049f55f4c7b2b5bf04a301c46a86358c5e43b

extension candidate scalar application result
  3ad027f5f2b4a7c322674637b6020ecb3a30986f

extension candidate scalar application audit note
  968b694cf3675d26693f1468d5720c9e412e06c3

extension candidate scalar application preregistration
  d90d41fd9f2596b3234dca174eca388a42f2859d
```

The parent result established, on the frozen 12-candidate panel, that the same candidate universe can induce different scalar-family sufficiency statuses under different supplied governance-relative preference relations. It also preserved the separation among exact representability, faithful contraction, and unrestricted lookup representability.

This architecture is explicitly:

```text
POST_RESULT_CONCEIVED                 true
HISTORICAL_ACTUAL_TARGET_EXPOSURE     true
ACTUAL_TARGET_TUNING_ALLOWED          false
CONCRETE_LANGUAGE_UNIVERSE_DEFINED    false
CALIBRATION_RELATIONS_DEFINED         false
ACTUAL_LANGUAGE_APPLICATION_PERFORMED false
```

Therefore:

\[
\boxed{
\texttt{POST\_RESULT\_CONCEIVED}
\neq
\texttt{ACTUAL\_TARGET\_TUNED}.
}
\]

No claim of pristine historical independence is made. The safeguard is prospective: after this architecture freeze, the actual four governance-relative target graphs may not determine syntax, primitives, parameter domains, exceptions, burden rules, admissibility rules, calibration fixtures, or closure procedures for the new language program.

---

# 1. Scientific object

The next object is not another scalar family.

It is the representational closure of a bounded decision-substrate language under an explicit admissibility regime:

\[
\boxed{
X
\longrightarrow
(\mathcal L,A)
\longrightarrow
\mathrm{Cl}^{A}_{\mathcal L}
\longrightarrow
\text{boundary diagnosis}.
}
\]

For this stage:

\[
X = R_{\rm pref},
\]

where `R_pref` is a complete typed candidate-level decision relation over a finite candidate universe.

The governing methodological invariant is frozen as:

\[
\boxed{\textbf{
No representation-deficiency claim without a frozen representational language and admissibility regime.
}}
\]

Equivalently:

\[
\boxed{
\operatorname{Insufficient}
=
\operatorname{Insufficient}(X;\mathcal L,A).
}
\]

Failure of one actor, one search procedure, one decoder instance, or one low-burden witness does not establish representational insufficiency.

---

# 2. Six frozen architecture objects

This architecture freezes exactly six typed objects:

\[
\boxed{
\mathfrak L_{\rm DS},
A_{\rm DS},
B_{\rm DS},
\mathfrak K_{\rm cal},
\Pi_{\rm closure},
\Sigma_{\rm outcome}.
}
\]

At this checkpoint these are **architecture contracts**, not populated empirical results.

In particular, the concrete language registry inside `\mathfrak L_DS` is intentionally empty. A later language-specification stage must instantiate a bounded language universe under the admission rules frozen here.

No concrete new decoder, dimensionality, graph grammar, finite-band extension, relational primitive, exception mechanism, or actual-target repair is defined in this commit.

---

# 3. Frozen decision-relation type

The present architecture retains the already-established four-token decision alphabet:

```text
PREFER_I
PREFER_J
EQUIVALENT
NO_WARRANTED_PREFERENCE
```

For a finite candidate universe `S` of size `n`, let:

\[
\mathfrak P(S)=\{\{i,j\}:i,j\in S,\ i\neq j\}.
\]

A target decision relation is:

\[
\boxed{
R:\mathfrak P(S)\rightarrow\Sigma_P
}
\]

with pair-swap involution:

```text
PREFER_I                 <-> PREFER_J
EQUIVALENT                 -> EQUIVALENT
NO_WARRANTED_PREFERENCE    -> NO_WARRANTED_PREFERENCE
```

Candidate labels are addressing devices only. They do not supply decision authority.

Every concrete language later admitted to `\mathfrak L_DS` must decode to this exact target type unless a new architecture is separately preregistered.

---

# 4. Language schema `\mathfrak L_DS`

Each concrete decision-substrate language must instantiate the schema:

\[
\boxed{
\mathcal L
=
(\Sigma_{\mathcal L},
\mathcal G_{\mathcal L},
\llbracket\cdot\rrbracket_{\mathcal L},
A_{\mathcal L},
B_{\mathcal L},
\Pi_{\mathcal L}).
}
\]

The fields are:

```text
Sigma_L       finite/bounded witness alphabet and parameter domains
G_L           finite/bounded grammar or witness-construction syntax
[[.]]_L       deterministic typed decoder semantics
A_L           witness-level admissibility predicate inherited from A_DS
B_L           witness-specific semantic-obligation accounting map
Pi_L          exact closure / admissible-closure certification procedure
```

For every calibration universe size used later, the language must induce a finite witness set or a finitely decidable witness theory with an exact completeness proof.

A language is ineligible for this stage if `NOT_REPRESENTABLE` could be concluded only from:

```text
heuristic search
stochastic optimization
local search
timeout
failure to find a witness
failure to find a cheap witness
```

The concrete member set of `\mathfrak L_DS` remains **undefined here**.

---

# 5. Witness universe and two closures

For language `L` on a finite candidate universe `S`, define its full witness universe:

\[
\mathcal H_{\mathcal L}(S).
\]

Each witness `h` deterministically induces a complete typed relation:

\[
R_h=\llbracket h\rrbracket_{\mathcal L}.
\]

The unrestricted closure is:

\[
\boxed{
\mathrm{Cl}_{\mathcal L}(S)
=
\{R_h:h\in\mathcal H_{\mathcal L}(S)\}.
}
\]

Let the frozen authority regime induce a witness-level predicate:

\[
\operatorname{Adm}_{A_{\rm DS}}(h)\in\{0,1\}.
\]

Then the admissible closure is:

\[
\boxed{
\mathrm{Cl}^{A}_{\mathcal L}(S)
=
\{R_h:h\in\mathcal H_{\mathcal L}(S),\ \operatorname{Adm}_{A_{\rm DS}}(h)=1\}.
}
\]

Therefore, by construction:

\[
\boxed{
\mathrm{Cl}^{A}_{\mathcal L}(S)
\subseteq
\mathrm{Cl}_{\mathcal L}(S).
}
\]

This inclusion is a first-class audited object.

An unrestricted exact witness does not imply an admissible exact witness.

---

# 6. Exact representability and admissible representability

For target relation `R`:

\[
\boxed{
\operatorname{Rep}_{\mathcal L}(R)
=
\mathbf 1[R\in\mathrm{Cl}_{\mathcal L}].
}
\]

Admissible representability is:

\[
\boxed{
\operatorname{Rep}^{A}_{\mathcal L}(R)
=
\mathbf 1[R\in\mathrm{Cl}^{A}_{\mathcal L}].
}
\]

Equivalently, with exact-witness sets:

\[
\mathcal H_{\mathcal L}(R)
=
\{h\in\mathcal H_{\mathcal L}:R_h=R\},
\]

\[
\mathcal H^{A}_{\mathcal L}(R)
=
\{h\in\mathcal H_{\mathcal L}(R):\operatorname{Adm}_{A_{\rm DS}}(h)=1\}.
\]

Then:

\[
\operatorname{Rep}_{\mathcal L}(R)=1
\iff
\mathcal H_{\mathcal L}(R)\neq\varnothing,
\]

and:

\[
\operatorname{Rep}^{A}_{\mathcal L}(R)=1
\iff
\mathcal H^{A}_{\mathcal L}(R)\neq\varnothing.
\]

A language may contain inadmissible witnesses and still admit an admissible exact factorization. Authority validity is therefore assessed at the **witness path**, not by globally blacklisting a language that happens to contain forbidden productions.

---

# 7. Authority regime `A_DS`

The authority gate answers:

> Can the target relation be reproduced using only declared, counted, candidate-anonymous representational state and fixed language semantics, without importing unlicensed distinctions?

The default decision-substrate architecture is **self-contained**.

An admissible witness may use:

```text
1. explicit witness state declared by the concrete language;
2. fixed decoder semantics declared before target application;
3. anonymous candidate slots whose meaning transports exactly under permutation;
4. explicit pair-addressed state when that state is part of the declared witness syntax and is fully counted in burden;
5. governance identity only as an application-environment index selecting a separately typed target/witness, not as a hidden pair-decision branch;
6. canonical pair orientation only for serialization, with exact swap equivariance.
```

An admissible witness may not derive decision distinctions from:

```text
candidate semantic identity
candidate provenance class
candidate display name or lexical spelling
candidate hash
serialization position
opaque nonce
implementation tag
untracked pair identity
untracked pair exception tables
actual-target edge lookup hidden outside counted witness state
actual-target mismatch neighborhoods
raw upstream measurement/comparison/preference artifacts at decode time
external or inherited state whose semantic burden is omitted
post-application branches chosen after seeing the target
```

This gate does not forbid explicit direct relation storage. A canonical pair table is admissible if its pair-specific state is represented openly, transports under anonymous relabeling, and its full semantic burden is counted.

What is forbidden is using identity/provenance/hash/hidden lookup as an **uncounted external oracle** for pair decisions.

A later architecture revision would be required to study substrates that intentionally inherit external upstream state at decode time. That object is outside this self-contained gate.

---

# 8. Authority transport requirements

Admissibility requires all of the following invariances:

```text
candidate permutation equivariance
pair-swap equivariance
serialization-order invariance
provenance-label invariance
candidate-alias invariance
nonce invariance
implementation-tag invariance
```

For every candidate permutation `pi`, an admissible witness must transport to a witness `pi(h)` such that:

\[
\boxed{
R_{\pi(h)}(\pi(i),\pi(j))
=
\pi\big(R_h(i,j)\big)
}
\]

with `pi` acting only on candidate positions and pair orientation, not on preference semantics beyond the frozen pair-swap rule.

A representation that works only because the anonymous handles happen to coincide with semantic candidate identities is authority-invalid.

---

# 9. Witness-specific burden `B_DS`

Burden is attached to an exact witness, not merely to a language label.

For any admissible witness `h`, define:

\[
\boxed{
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
}
\]

The five ledgers mean:

```text
B_state       explicit candidate-, component-, pair-, or latent-state obligations
B_decoder     semantic branch/operation obligations needed to interpret the witness
B_auxiliary   thresholds, cutpoints, dimensions, matrices, partitions, graph parameters, etc.
B_selector    obligations required to select among non-equivalent grammar/module alternatives
B_exception   any declared exceptional state; pair-specific exceptions are never free
```

Common infrastructure may be excluded only when it is semantically identical and available symmetrically to every compared representation, such as:

```text
candidate registry
canonical unordered-pair enumeration
four-token target vocabulary
pair-swap convention
serialization format
```

The anti-scaffold rule is frozen:

\[
\boxed{\textbf{Where did the decision complexity go?}}
\]

Therefore:

```text
macros are charged at expanded semantic burden;
hidden obligations count;
fixed-before-target does not mean free;
uninstantiated grammar alternatives do not inflate a witness if they are not needed to interpret it;
selected non-common semantic machinery does count;
external state cannot be excluded merely because it is inherited;
per-pair state counts per pair;
per-candidate state counts per candidate;
no burden formula may be changed after actual application begins.
```

---

# 10. Native target burden

For the present typed decision relation, the direct native baseline remains one typed relation obligation per unordered pair:

\[
\boxed{
B_R=|\mathfrak P(S)|=\binom n2.
}
\]

This is not a claim that the relation is globally minimal.

It is the frozen comparison baseline for semantic-obligation contraction in this architecture.

Any future proposal to change the native baseline requires a separate preregistration before language application.

---

# 11. Minimum admissible witness burden

Only after admissible closure membership is certified may minimum burden be defined:

\[
\boxed{
B^{*}_{\mathcal L}(R)
=
\min_{h\in\mathcal H^{A}_{\mathcal L}(R)}B(h).
}
\]

If:

\[
\mathcal H^{A}_{\mathcal L}(R)=\varnothing,
\]

then `B*_L(R)` is serialized as:

```text
NOT_DEFINED
```

rather than silently set to a large number or used to blur authority failure into burden failure.

This is a hard gate ordering:

\[
\boxed{
\text{closure certification}
\rightarrow
\text{admissible closure certification}
\rightarrow
\text{minimum-burden search}
\rightarrow
\text{classification}.
}
\]

Failure to find a cheap witness never establishes failure of admissible closure.

---

# 12. Cross-language minimizer set

After a later concrete language universe is frozen, define the global minimum admissible witness set for `R` as:

\[
\boxed{
\mathcal H^{*}(R)
=
\arg\min_{\substack{
\mathcal L\in\mathfrak L_{\rm DS}\\
h\in\mathcal H^{A}_{\mathcal L}(R)
}}
B(h).
}
\]

This object is intentionally **set-valued**.

Multiple witnesses from different languages may tie at minimum burden.

No lexical, historical, aesthetic, or implementation-order tie-break is licensed.

A burden tie does not establish semantic equivalence between languages.

---

# 13. Admissible contraction

For a language with admissible exact witnesses:

\[
\boxed{
\operatorname{Contract}^{A}_{\mathcal L,B}(R)
=
\operatorname{Rep}^{A}_{\mathcal L}(R)
\land
[B^{*}_{\mathcal L}(R)<B_R].
}
\]

Thus the three gates remain distinct:

\[
\boxed{
\operatorname{Expressivity}
\rightarrow
\operatorname{Authority}
\rightarrow
\operatorname{Contraction}.
}
\]

Authority invalidity is not a burden failure.

An authority-invalid representation is not rehabilitated by being cheap.

---

# 14. Four-state outcome vocabulary `Sigma_outcome`

For every target-language pair `(R,L)`, emit exactly one terminal scientific state:

```text
NOT_REPRESENTABLE
REPRESENTABLE_AUTHORITY_INVALID
ADMISSIBLE_REPRESENTATION_NO_CONTRACTION
FAITHFUL_CONTRACTION
```

The decision rule is frozen as:

\[
\boxed{
\begin{aligned}
R\notin\mathrm{Cl}_{\mathcal L}
&\Rightarrow \texttt{NOT\_REPRESENTABLE},\\[1mm]
R\in\mathrm{Cl}_{\mathcal L}\setminus\mathrm{Cl}^{A}_{\mathcal L}
&\Rightarrow \texttt{REPRESENTABLE\_AUTHORITY\_INVALID},\\[1mm]
R\in\mathrm{Cl}^{A}_{\mathcal L},\ B^{*}_{\mathcal L}(R)\ge B_R
&\Rightarrow \texttt{ADMISSIBLE\_REPRESENTATION\_NO\_CONTRACTION},\\[1mm]
R\in\mathrm{Cl}^{A}_{\mathcal L},\ B^{*}_{\mathcal L}(R)<B_R
&\Rightarrow \texttt{FAITHFUL\_CONTRACTION}.
\end{aligned}
}
\]

No burden comparison is performed for the first two states.

A fifth per-language status is not introduced.

---

# 15. Aggregate `NO_SUPPORTED_CONTRACTION`

After a later concrete language universe is frozen, a target may receive the descriptive aggregate:

```text
NO_SUPPORTED_CONTRACTION
```

iff:

\[
\forall\mathcal L\in\mathfrak L_{\rm DS}^{\rm frozen},
\quad
\operatorname{Contract}^{A}_{\mathcal L,B}(R)=0.
\]

This means only:

> no admissible faithful contraction exists in the tested frozen language universe.

It does not establish:

```text
global minimality of the native relation
universal non-compressibility
intrinsic impossibility
impossibility in an untested language
normative inferiority of the target governance relation
```

---

# 16. Closure certification `Pi_closure`

Closure certification is independent of minimum-burden optimization.

For each concrete language later admitted, execution must proceed in this order:

```text
C0  validate exact language specification and finite/decidable witness domain
C1  certify unrestricted closure membership R in Cl_L or R not in Cl_L
C2  if C1 succeeds, certify admissible closure membership R in Cl^A_L or not
C3  only if C2 succeeds, certify minimum B(h) over all admissible exact witnesses
C4  classify using Sigma_outcome
```

`C1` and `C2` may use:

```text
complete finite enumeration
exact CSP
exact SAT/SMT with finite-domain completeness
exact graph-isomorphism reduction
exact dynamic programming
algebraic decision procedure
other exactly equivalent complete proof procedure
```

provided the concrete language specification states why pruning or reduction is sound and complete.

The following are forbidden bases for `NOT_REPRESENTABLE` or `REPRESENTABLE_AUTHORITY_INVALID`:

```text
heuristic absence
optimization failure
search timeout
best-so-far mismatch
minimum-distance witness
failure to find a low-burden witness
```

A closure certificate and a burden-minimum certificate are separate serialized objects.

---

# 17. Burden minimization certificate

For `R in Cl^A_L`, exact minimum burden may be certified by:

```text
complete enumeration of admissible exact witnesses
exact branch-and-bound with sound lower bounds
exact dynamic programming over witness syntax
exact equivalent optimization procedure with a completeness certificate
```

The implementation must prove that no admissible exact witness with burden below the reported minimum exists.

A canonical witness may be serialized for reproducibility, but canonicality is not the scientific minimization criterion.

If multiple minimum-burden witnesses exist, preserve the minimizer set or a lossless equivalence-class representation of it.

---

# 18. Structural calibration architecture `K_cal`

Calibration must be structural and anonymous rather than a named fixture zoo.

Every calibration relation receives a structural descriptor:

\[
\boxed{
K(R)
=
(T_{\rm dir},
T_{\rm abst},
T_{\rm eq},
T_{\rm comp},
T_{\rm conn},
T_{\rm dim},
N,
C_{\Sigma}).
}
\]

The architecture-level axes are:

```text
T_dir    directional topology
T_abst   abstention-region topology
T_eq     equivalence-token topology
T_comp   compositional/product/cross-cut structure
T_conn   connectivity/component structure
T_dim    latent generator dimension tag where applicable
N        candidate count
C_Sigma  target-token count vector, treated primarily as a matching/nuisance stratum
```

The later calibration-specification stage must instantiate finite values and generators for these axes before any calibration execution.

At architecture level, the intended structural regimes include at least the following kinds of variation, without yet defining concrete fixtures:

```text
directional:
  none / total or total-preorder / acyclic partial / cyclic / disconnected / product-like

abstention:
  none / monotone / nested / disconnected / cross-cutting

equivalence:
  trivial / lawful partition / deliberately nontransitive typed-token control

connectivity:
  connected / disconnected under the frozen resolved-edge support definition

composition:
  single-axis / product / cross-cut / mixed

latent generator dimension:
  one-dimensional / low-dimensional (>1) bounded tags when a generator supplies such structure
```

Some tags, especially abstention monotonicity and latent dimension, are generator-certified properties rather than properties inferred from the relation token table alone. The generator certificate must be retained.

---

# 19. Factorial matched-discriminant requirement

Calibration should not infer language boundaries from category names alone.

The later calibration panel must include matched relation pairs or small factorial blocks that differ along one preregistered structural axis while holding the remaining declared axes fixed as closely as construction permits.

For a matched contrast `(R_a,R_b)`:

\[
K(R_a)
\text{ and }
K(R_b)
\]

must record explicitly which structural coordinate differs.

Where feasible, matched contrasts must also hold fixed:

```text
candidate count n
target-token count vector
sizes of equivalence classes
number of resolved versus abstaining pairs
component count outside the manipulated axis
serialization and naming structure
```

This directly protects the inference:

\[
\boxed{
\text{relation cardinality}
\neq
\text{relation geometry}.
}
\]

A difference in scalar or language status cannot be attributed to a structural axis if other material axes were not controlled or recorded.

---

# 20. Structural-class closure claims

A calibration success on sampled fixtures does **not** automatically establish closure over an entire named structural class.

The statement:

\[
\boxed{
\mathcal L
\text{ is closed over structural class }K
}
\]

is licensed only if the later calibration protocol either:

```text
1. finitely enumerates every relation in the frozen class and certifies each; or
2. supplies an exact proof/decision reduction showing every class member lies in the relevant closure.
```

Otherwise the permitted wording is restricted to the finite calibration support actually tested.

This prevents sampled benchmark performance from being promoted into a closure theorem.

---

# 21. Calibration provenance and actual-target exclusion

The actual four governance-relative candidate preference graphs have already been inspected historically.

Therefore the next language stage is not called a pristine holdout study.

Instead, from this architecture checkpoint forward:

```text
actual candidate IDs are forbidden from language design and calibration;
actual pair IDs are forbidden from language design and calibration;
actual eight-edge disagreement structure may not be encoded into a primitive;
actual two-mismatch or four-mismatch neighborhoods may not define a primitive, threshold, dimension, exception, or generator;
actual target artifacts may not be loaded by language-specification or calibration executables;
actual governance names may not define calibration fixture semantics;
actual graph-specific parameter tuning is forbidden.
```

Language design rationales must be stated in abstract structural terms that apply independently of the observed actual target identities.

Anonymous calibration may legitimately inform language identification and later revisions **before final language freeze**, but all such revisions must be versioned and must remain blind to the actual target artifacts.

After final language freeze, actual application requires a separate preregistration.

---

# 22. Stage sequence

The program sequence is frozen as:

\[
\boxed{
\text{architecture}
\rightarrow
\text{language specification}
\rightarrow
\text{anonymous structural calibration/identification}
\rightarrow
\text{final language freeze}
\rightarrow
\text{actual application preregistration}
\rightarrow
\text{actual application execution}.
}
\]

The calibration/identification stage may revise candidate languages using anonymous calibration evidence, but may not use actual target artifacts.

Every revision changes provenance and must be explicit.

The final language freeze terminates language redesign before actual application begins.

---

# 23. Calibration controls for the four gates

The later language-calibration stage must include controls capable of making the four-state ontology empirically visible.

At minimum preserve these conceptual controls:

## `W_DIRECT_LOOKUP`

An explicit anonymous pair-table representation whose full pair state is counted.

Expected role:

```text
exact representability positive control
admissibility positive control
contraction negative control when burden >= B_R
```

For a direct four-token relation table with one decoder obligation, the inherited scalar-stage pattern suggests:

```text
B_direct_lookup = B_R + decoder overhead
```

but the exact later burden formula must be frozen in the concrete language specification before calibration.

## `W_IDENTITY_ORACLE`

A representation that reproduces target outputs by using forbidden semantic candidate identity, provenance, hash, or another non-transporting external oracle.

Expected role:

```text
Rep_L(R)   = 1
Rep^A_L(R) = 0
```

This control separates extensional reproducibility from authority-valid factorization.

The exact control construction must be anonymous with respect to actual project candidates and defined only on calibration data.

## expressivity-negative control

At least one calibration language/relation combination must be provably outside unrestricted closure.

## admissible-contraction positive control

At least one calibration language/relation combination must have a certified admissible exact witness with burden strictly below `B_R`.

No single language is required to occupy every state.

---

# 24. Nuisance invariance

Every later calibration relation and every admitted language must support deterministic anonymous nuisance testing.

Minimum nuisance transformations:

```text
candidate-handle permutation
serialization-order permutation
relation-record order permutation
display alias changes
opaque nonce changes
implementation-tag changes
```

The calibration protocol should inherit the project convention of 64 deterministic nuisance encodings unless a later preregistration justifies another frozen count before execution.

Required invariants:

```text
unrestricted closure status
admissible closure status
terminal Sigma_outcome state
minimum burden when defined
authority-violation diagnosis
```

For minimum witnesses, candidate permutation must transport the minimizer set or its equivalence-class certificate, not merely one arbitrary witness.

---

# 25. Pair-swap symmetry

Every decoded relation must satisfy exact pair-swap semantics.

A representation depending on canonical lexical pair order rather than its declared semantic state is authority-invalid or incorrect, depending on whether the output relation remains exact only because of the lexical scaffold.

Pair-swap tests are required for:

```text
calibration targets
unrestricted witnesses
admissible witnesses
minimum-burden witnesses
```

---

# 26. Failure diagnostics

The four terminal states are primary. Detailed failure reasons remain typed and may be set-valued inside the relevant gate.

For `REPRESENTABLE_AUTHORITY_INVALID`, retain an `authority_violation_set` drawn from a later concrete finite vocabulary including at least distinctions of the following form:

```text
UNLICENSED_CANDIDATE_IDENTITY
UNLICENSED_PROVENANCE
UNLICENSED_PAIR_IDENTITY_OR_EXCEPTION
UNLICENSED_TARGET_LOOKUP
UNCOUNTED_EXTERNAL_STATE
NON_EQUIVARIANT_SERIALIZATION_SCAFFOLD
OTHER_DECLARED_AUTHORITY_VIOLATION
```

The exact finite vocabulary must be finalized before calibration execution.

For `NOT_REPRESENTABLE`, the primary failure is unrestricted closure failure. Do not infer a causal reason from one near-miss witness.

For `ADMISSIBLE_REPRESENTATION_NO_CONTRACTION`, the failure locus is burden only.

For `FAITHFUL_CONTRACTION`, the failure locus is empty.

---

# 27. Broken controls / forbidden shortcuts

The later program must explicitly reject the following shortcuts.

## A1 — actual-target repair primitive

Define a language primitive because it fixes a known actual two- or four-mismatch pattern.

```text
failure: ACTUAL_TARGET_TUNING
```

## A2 — cheap-witness failure called closure failure

Fail to find a witness below a burden threshold and report `NOT_REPRESENTABLE`.

```text
failure: CLOSURE_OPTIMIZATION_COLLAPSE
```

## A3 — unrestricted representation called admissible

Find any exact witness and skip the authority gate.

```text
failure: AUTHORITY_GATE_BYPASS
```

## A4 — cheap cheating witness called contraction

Use candidate identity, provenance, hidden lookup, or external state to reduce visible burden.

```text
failure: AUTHORITY_INVALID_CONTRACTION
```

## A5 — burden evaluated before admissibility

Compare burden for an authority-invalid witness to `B_R`.

```text
failure: GATE_ORDER_VIOLATION
```

## A6 — one canonical witness used as minimum proof

Serialize one admissible witness and assume its burden is minimal.

```text
failure: INCOMPLETE_BURDEN_MINIMIZATION
```

## A7 — language semantics made free by preregistration

Exclude decoder/grammar obligations merely because they were frozen before target application.

```text
failure: ANTI_SCAFFOLD_ACCOUNTING_FAILURE
```

## A8 — hidden inherited substrate

Use upstream measurement, comparison, governance, or target state at decode time without charging and licensing it.

```text
failure: HIDDEN_EXTERNAL_STATE
```

## A9 — explicit pair table confused with identity oracle

Treat fully counted anonymous pair-addressed state as authority-invalid merely because it is pair-specific, or treat hidden semantic identity as legitimate pair addressing.

```text
failure: ADDRESSING_AUTHORITY_CONFUSION
```

## A10 — sampled calibration promoted to class closure

Pass selected examples and claim closure over all relations in a named structural class.

```text
failure: SAMPLED_TO_UNIVERSAL_LEAKAGE
```

## A11 — scalar/language status becomes governance quality

Infer that a governance contract is better because its induced relation contracts more easily.

```text
failure: NORMATIVE_AUTHORITY_LEAKAGE
```

## A12 — actual application before language freeze

Read or fit the actual target before completing anonymous calibration and final language freeze.

```text
failure: APPLICATION_TO_IDENTIFICATION_LEAKAGE
```

## A13 — fixture labels substitute for structural controls

Use named fixture categories without recording matched structural discriminants.

```text
failure: CALIBRATION_STRUCTURE_UNDERSPECIFIED
```

## A14 — arbitrary tie-breaking among minimizers

Collapse a set-valued minimum into one preferred language without an independently authorized rule.

```text
failure: UNAUTHORIZED_LANGUAGE_SELECTION
```

---

# 28. Required serialization for later identification/calibration

For every calibration target-language application, later machine results must include at minimum:

```text
relation_id
aonymous_candidate_count
structural_descriptor_K
target_token_counts
language_id
language_specification_hash
unrestricted_closure_member
unrestricted_closure_certificate
admissible_closure_member
admissible_closure_certificate
authority_violation_set
B_R
B_star
minimum_burden_certificate
minimum_witness_set_or_equivalence_certificate
terminal_status
pair_swap_result
nuisance_invariance_result
complete_closure_adjudicated
complete_admissible_closure_adjudicated
complete_burden_minimization
```

If `admissible_closure_member = false`, `B_star` must be `NOT_DEFINED`.

If any required exact certification is unavailable, the gate hard-fails rather than inventing a fifth scientific outcome.

---

# 29. Architecture-level success criteria

This architecture is considered correctly instantiated by later stages only if:

1. the concrete language universe is bounded and frozen before actual application;
2. every language has exact syntax, semantics, admissibility, burden, and closure procedures;
3. unrestricted and admissible closure are separately certified;
4. `Cl^A_L subseteq Cl_L` is enforced by construction;
5. closure certification precedes burden optimization;
6. minimum burden is searched only over admissible exact witnesses;
7. `B*_L(R)` remains undefined without an admissible exact witness;
8. authority-invalid witnesses cannot earn contraction regardless of cost;
9. pair-specific explicit state is counted rather than hidden;
10. candidate identity/provenance/hash cannot supply authority;
11. calibration is anonymous and structurally factorial/matched;
12. actual target artifacts are excluded from language calibration and tuning after this freeze;
13. sampled calibration is not promoted to universal closure without exhaustive/proof support;
14. minimizers remain set-valued under ties;
15. no language status is converted into governance ranking or candidate authorization.

---

# 30. Anti-downstream flags

At this architecture checkpoint:

```text
decision_substrate_language_architecture_frozen = true
concrete_language_universe_instantiated         = false
concrete_language_witness_defined               = false
anonymous_calibration_panel_instantiated        = false
closure_calibration_executed                    = false
final_language_freeze_performed                 = false
actual_target_application_preregistered         = false
actual_target_application_performed             = false
actual_Q_extension_defined                      = false
governance_contract_selected                    = false
candidate_ranking_performed                     = false
candidate_adoption_selected                     = false
utility_defined                                 = false
reward_defined                                  = false
NO_WARRANTED_ADOPTION_defined                   = false
adoption_performed                              = false
authorization_performed                         = false
binding_performed                               = false
execution_performed                             = false
```

No dependency ledger update is implied by this architecture freeze.

---

# 31. Strongest permitted claim from this commit

The strongest admissible claim from this architecture alone is:

\[
\boxed{\textbf{
The decision-substrate program now has a preregistered architecture that separates unrestricted representational closure, authority-valid representational closure, and witness-specific semantic-obligation contraction; requires exact closure certification before minimum-burden optimization; and constrains subsequent language identification to anonymous structural calibration before any new actual-target application.
}}
\]

This commit does **not** establish:

```text
that any new language exists
that any actual target is representable in a richer language
that any actual target is authority-invalid
that any actual target contracts
that any language is minimal
that any structural class is closed
that decision relations are scalar or non-scalar in general
that governance determines scalarizability in general
that any candidate should be selected
that Q_extension exists
```

---

# 32. Stop condition

Stop after freezing this architecture.

Do not in the same commit:

```text
instantiate a new concrete language
name a D3/D4-style repair as the next decoder
choose low-dimensional coordinates
choose graph primitives
choose actual language parameter domains
construct anonymous calibration relations
run closure certification
search minimum-burden witnesses
read actual target artifacts for decoder design
apply any new language to the actual four governance graphs
define Q_extension
rank candidates
select governance
adopt
authorize
bind
execute
update the dependency ledger
```

The next scientific artifact is a **separate concrete language-specification preregistration** governed by this architecture.