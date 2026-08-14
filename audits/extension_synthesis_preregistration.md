# Extension Synthesis Audit — Preregistration

## Status

This document freezes the next empirical gate **before execution**.

Parent dependency checkpoint:

```text
9fd30f1  Update experiment-planning dependency consolidation after closure diagnosis
```

Closure-diagnosis empirical anchor:

```text
7e3871c  closure-insufficiency diagnosis audit
```

Gate-2 basin-opening anchor:

```text
ee1b9ac  experiment-space construction discriminant
```

No empirical result is recorded here.

The governing boundary is:

\[
\boxed{
\text{candidate-space construction}
\neq
\text{candidate selection}
\neq
\text{extension valuation}
\neq
\text{authorization}
\neq
\text{binding}.
}
\]

The present audit tests only:

\[
\boxed{
D_{\rm closure}=\texttt{INSUFFICIENT}
\rightarrow
M_0
\rightarrow
\widehat S_{\rm candidate}
}
\]

or the warranted null output:

\[
\boxed{\texttt{NO\_SUPPORTED\_CANDIDATE}.}
\]

No candidate extension is bound into the live construction substrate.

---

## 1. Scientific question

The narrow question is:

\[
\boxed{
\textbf{Given a diagnosed construction-space insufficiency, can a system synthesize a non-oracular candidate substrate transformation from a supplied target-blind lower-level meta-substrate?}
}
\]

The strongest allowed interpretation is deliberately bounded:

\[
\boxed{
\textbf{extension synthesis relative to a supplied target-blind construction meta-substrate }M_0.
}
\]

This audit does **not** test unrestricted operator invention, unrestricted grammar invention, research agency, autonomous authorization, or self-modification.

---

## 2. Freeze the upstream diagnosis

Every primary synthesis episode must first satisfy the already-earned closure-diagnosis condition:

\[
\boxed{D_{\rm closure}=\texttt{INSUFFICIENT}.}
\]

The diagnosis must be recomputed from the currently admitted closure and frozen correction contract. It must not be supplied as a context label only.

The inherited diagnostic rule remains:

\[
D_{\rm closure}=\texttt{INSUFFICIENT}
\iff
\mathcal C(S)\text{ is exhaustively characterized}
\land
\max_{e\in\mathcal C(S)}q(e)\le0,
\]

with:

\[
q(e)=R_{\rm corr}(e)-\kappa,
\qquad
\boxed{\kappa=0.1}.
\]

All synthesis cases below are constructed so the current closure has no strict-positive warranted continuation.

The synthesis mechanism receives no `AND`, `OR`, `DEPTH`, `REUSE`, `MISSING_PRIMITIVE`, or equivalent repair label.

---

## 3. Candidate discovery is not extension valuation

The audit distinguishes **binary structural adequacy** from later extension valuation.

For a counterfactual candidate transformation `s`, define:

\[
\operatorname{CanRestore}(s)=1
\iff
\max_{e\in\mathcal C(S\oplus s)}q(e)>0.
\]

This is only a feasibility predicate: does the candidate make at least one warranted continuation reachable?

The synthesis stage must **not**:

- assign cardinal utility to candidate extensions;
- compare candidate acquisition or implementation costs;
- rank adequate candidates by expected future value;
- authorize any candidate;
- bind any candidate;
- execute a post-binding learning episode.

If several synthesized candidates are structurally adequate, retain the complete set of **minimal adequate semantic candidate classes**. Do not choose a winner.

Thus:

\[
\boxed{
\text{construct adequate candidate set}
\neq
\text{value candidates}.
}
\]

The endpoint `S_hat_candidate` may therefore be a semantic equivalence class or a co-minimal set of such classes rather than one privileged syntax tree.

---

## 4. Supplied target-blind meta-substrate `M0`

`M0` is an intensional construction language, not a named extension menu.

### 4.1 Low-level Boolean operator basis

Candidate binary experiment operators are synthesized from anonymous argument placeholders `u,v` using one target-blind Boolean primitive:

\[
N(u,v)=\neg(u\land v).
\]

The implementation must expose this primitive under an opaque handle; the downstream synthesizer must not receive the string `NAND` as a semantic hint.

Enumerate all syntax trees over `u,v,N` with at most:

\[
\boxed{3\text{ internal }N\text{ nodes}.}
\]

Deduplicate synthesized binary functions extensionally by their four-row truth tables before they are used in construction programs.

This bound is sufficient to make multiple nonlinear binary functions constructible, including functions extensionally equivalent to conjunction- and disjunction-like operators, without naming those operators in the candidate space.

### 4.2 Generic construction-program language

`M0` also supplies generic pool/program combinators:

```text
APPLY(f, P, Q)       # apply an admitted or synthesized binary operator f to all admissible pairs from pools P,Q
UNION(P, Q)          # merge experiment pools
XOR_CLOSE(P)         # use the already-admitted current XOR operator to fixed point over P
```

The available source-pool roles are:

```text
BASE                  # experiments in the current linear/parity base closure
CURRENT_NONLINEAR     # currently admitted experiments outside BASE, if any
```

Pool handles must be anonymized in public encodings. Their provenance relation may be used; their English names may not.

### 4.3 Candidate-program bound

A candidate transformation may contain:

1. zero or one synthesized binary-operator definition;
2. at most one `APPLY` instruction;
3. zero or one `XOR_CLOSE` instruction after the `APPLY`;
4. at most one union of newly generated experiments with the current registry.

The candidate grammar may apply an admitted/synthesized binary operator to:

```text
BASE x BASE
CURRENT_NONLINEAR x BASE
```

but **not**:

```text
NEW x NEW
```

and it may not introduce a new primitive evidence channel.

These are declared bounds on the claim. They are not hidden implementation accidents.

### 4.4 Candidate-space construction procedure

For each diagnosed-insufficient episode:

1. introspect the current construction substrate semantically;
2. enumerate all syntax-valid programs from `M0` within the frozen bounds;
3. execute each program only **counterfactually** to derive its resulting experiment-partition family;
4. deduplicate programs by the resulting closure fingerprint;
5. evaluate `CanRestore` from lower-level evidence partitions and the frozen correction contract;
6. remove semantically redundant supersets when a strictly smaller candidate delta yields the same restored continuation;
7. return all remaining minimal adequate semantic candidate classes;
8. if none exist, emit `NO_SUPPORTED_CANDIDATE`.

No externally supplied extension list participates in this procedure.

---

## 5. Specification-burden ledger for `M0`

The audit must report the entire meta-construction contract rather than visible syntax alone.

Track at least:

\[
\boxed{
B_{M_0}
=
B_{\rm truth\ basis}
+B_{\rm pool\ roles}
+B_{\rm program\ combinators}
+B_{\rm grammar}
+B_{\rm search\ bounds}
+B_{\rm semantic\ hints}
+B_{\rm target\ hints}.
}
\]

Preregistered supplied structure:

```text
B_truth_basis          = 1   # opaque two-input Boolean primitive N
B_pool_roles           = 2   # BASE, CURRENT_NONLINEAR provenance roles
B_program_combinators  = 3   # APPLY, UNION, XOR_CLOSE
B_grammar              = 3   # operator expression, apply expression, optional closure expression
B_search_bounds        = 3   # N-node cap, one APPLY, no NEWxNEW / no primitive invention
B_semantic_hints       = 0
B_target_hints         = 0
```

This is a clause ledger, not an information-theoretic bit count.

A successful audit therefore supports synthesis **relative to this supplied meta-substrate**. It does not imply that `M0` itself was discovered.

The governing anti-scaffold question remains:

\[
\boxed{\textbf{Where did the candidate-extension ontology go?}}
\]

---

## 6. Primary multi-extension panel

Use 64 anonymous encodings for each of four synthesis classes:

```text
A  OPERATOR-AND-LIKE
B  OPERATOR-OR-LIKE
C  REUSE/DEPTH
D  NO-SUPPORTED-CANDIDATE
```

Across the four classes:

\[
\boxed{64\times4=256\text{ synthesis episodes}.}
\]

All four classes must enter synthesis only after independently recomputed:

\[
\boxed{D_{\rm closure}=\texttt{INSUFFICIENT}.}
\]

The class label is evaluator-only and is never exposed to the synthesizer.

---

## 7. Class A — nonlinear operator synthesis, conjunction-like target

Use the familiar four-bit world:

\[
X=(x_1,x_2,x_3,x_4)\in\{0,1\}^4.
\]

Current construction substrate is the old linear Gate-1 substrate:

\[
S_A=S_0,
\qquad
|\mathcal C(S_A)|=15.
\]

Target correction contract:

\[
y_A=x_1\land x_2.
\]

Execution must derive:

```text
baseline Bayes accuracy       = 0.75
exact-target R_corr           = 0.25
current closure max R_corr    = 0.00
current closure max q         = -0.10
D_closure                     = INSUFFICIENT
```

No named conjunction operator is supplied.

`M0` must synthesize one or more binary-function/program candidates whose counterfactual closure makes a strict-positive corrective continuation reachable.

Because multiple syntactically different functions may generate the same repair-relevant partition family, evaluation is by semantic closure fingerprint, not by matching an `AND` token.

Primary requirement:

```text
at least one minimal adequate semantic candidate class synthesized: 64/64
NO_SUPPORTED_CANDIDATE emitted:                                    0/64
```

---

## 8. Class B — distinct operator-semantic synthesis, disjunction-like target

Use the **same current substrate**:

\[
S_B=S_0,
\qquad
|\mathcal C(S_B)|=15.
\]

Target:

\[
y_B=x_1\lor x_2.
\]

Execution must derive the matched closure diagnosis:

```text
baseline Bayes accuracy       = 0.75
exact-target R_corr           = 0.25
current closure max R_corr    = 0.00
current closure max q         = -0.10
D_closure                     = INSUFFICIENT
```

Again, no named disjunction operator is supplied.

Primary requirement:

```text
at least one minimal adequate semantic candidate class synthesized: 64/64
NO_SUPPORTED_CANDIDATE emitted:                                    0/64
```

The evaluator must additionally verify:

\[
\boxed{
\widehat{\mathfrak S}_A
\neq
\widehat{\mathfrak S}_B
}
\]

at the semantic candidate-family level.

This blocks the reflex:

\[
\boxed{
D_{\rm closure}=\texttt{INSUFFICIENT}
\rightarrow
\text{one fixed operator repair}.
}
\]

The exact count of adequate semantic classes must be derived exhaustively at execution and reported; it is not assumed from operator names.

---

## 9. Class C — structural reuse/depth repair rather than new operator name

Return to the four-bit world, but change the **current** construction substrate.

Let `S_C` be the complete zero-constant Boolean polynomial experiment family of algebraic degree `<=2`, generated by:

- the four coordinate primitives;
- the existing XOR mechanism;
- one already-admitted anonymous nonlinear binary operator sufficient to generate quadratic terms;
- the already-earned post-extension XOR closure.

Execution must derive:

\[
\boxed{|\mathcal C(S_C)|=1023.}
\]

Target:

\[
y_C=x_1x_2x_3.
\]

Execution must derive:

```text
baseline Bayes accuracy       = 0.875
exact-target R_corr           = 0.125
current degree<=2 max R_corr  = 0.000
current closure max q         = -0.100
D_closure                     = INSUFFICIENT
```

The target cannot be repaired by merely adding another one-layer binary operation over `BASE x BASE`; such operations remain degree `<=2`.

`M0` can, however, construct programs that reuse currently nonlinear experiments as one input to a further binary application:

```text
CURRENT_NONLINEAR x BASE
```

followed, if required, by the admitted XOR closure.

Primary structural requirement:

```text
at least one minimal adequate candidate uses nonlinear-result reuse/depth: 64/64
BASE x BASE only candidates adequate:                              0/64
NO_SUPPORTED_CANDIDATE emitted:                                    0/64
```

This class is intended to establish:

\[
\boxed{
\text{missing operator semantics}
\neq
\text{insufficient reuse/compositional depth}.
}
\]

No specific current nonlinear operator name is visible to the synthesizer; only its extensional semantics and provenance in the current substrate are available under opaque handles.

---

## 10. Class D — `NO_SUPPORTED_CANDIDATE`

Use a five-bit world:

\[
X=(x_1,x_2,x_3,x_4,x_5)\in\{0,1\}^5.
\]

For each anonymous encoding, choose one coordinate uniformly as the **inaccessible latent coordinate** `z` and expose the other four coordinates to the current construction substrate.

The current substrate and all `M0` programs may compose only functions of the four exposed coordinates. `M0` is explicitly not permitted to invent a new primitive evidence channel.

Target:

\[
y_D=z.
\]

Because `z` is independent of every function of the four exposed coordinates:

\[
\boxed{
R_{\rm corr}(e\mid y_D)=0
\quad
\forall e\text{ constructible from }S_D\oplus M_0.
}
\]

Yet an exact experiment on `z`, if such a primitive channel were available, would have:

```text
baseline Bayes accuracy = 0.50
exact-target R_corr     = 0.50
exact-target q          = 0.40
```

Thus the problem is not that correction would be worthless. The problem is that the admitted meta-substrate cannot construct access to the required primitive distinction.

Primary requirement:

```text
adequate semantic candidate classes: 0 / 64
NO_SUPPORTED_CANDIDATE:            64 / 64
```

This is the critical corrigibility control:

\[
\boxed{
D_{\rm closure}=\texttt{INSUFFICIENT}
\not\Rightarrow
\text{produce a repair anyway}.
}
\]

---

## 11. Wrong-extension controls

The generated candidate universe must contain structural alternatives that fail.

Execution must include and report at least the following derived negative cases:

### W1 — geometry-preserving operator syntax

A synthesized operator/program whose counterfactual experiment partitions remain inside the current closure must have:

\[
\operatorname{CanRestore}=0.
\]

New syntax alone is not a candidate repair.

### W2 — wrong nonlinear operator family

For Classes A and B, report synthesized nonlinear operator-family fingerprints that enlarge the registry but do **not** make the current target correction-relevant continuation reachable.

Thus:

\[
\boxed{
\text{space expansion}
\neq
\text{repair of this diagnosed defect}.
}
\]

### W3 — wrong structural axis for depth case

For Class C, every candidate restricted to one-layer `BASE x BASE` application must remain inadequate even if it adds a previously absent binary truth function.

The positive candidate must alter reuse/depth structure.

### W4 — unsupported primitive deficit

For Class D, **every** generated `M0` program must fail `CanRestore`. Any positive candidate is leakage or a benchmark defect.

---

## 12. Anti-scaffold controls

### M1 — supplied named extension menu

Construct a control in which the evaluator directly supplies a finite list of already-materialized candidate extensions corresponding to the semantic candidate classes available from `M0`.

A selector may achieve exact behavior from that menu.

Classification:

\[
\boxed{\text{candidate selection from supplied menu}.}
\]

This is **not** valid evidence for candidate-space construction.

### M2 — opaque repair macro

Allow one superficially compact command such as:

```text
MAKE_SUPPORTED_REPAIR
```

If the command internally stores a context-to-extension map or the generated candidate families, its expanded semantic burden must be counted.

Classification:

\[
\boxed{\text{hidden extension specification}.}
\]

### M3 — target-specific synthesis template

Supply a target-conditioned syntax skeleton, operator truth table, source-pool choice, or edit template that points directly to an adequate repair.

Classification:

\[
\boxed{\text{oracle displacement}.}
\]

### M4 — valid target-blind meta-substrate

Only the frozen lower-level `M0` grammar is valid primary evidence.

No context-to-repair table, extension name, target formula label, winner hint, or adequate-candidate label may enter `M0`.

---

## 13. Restricted-information / reflex controls

### R0 — closure diagnosis only

Expose only:

```text
D_closure = INSUFFICIENT
```

across the four balanced synthesis classes.

At the evaluator's coarse repair-axis level:

```text
operator-semantic A
operator-semantic B
reuse/depth
no-supported
```

are equally represented.

A deterministic reflex from `INSUFFICIENT` to one fixed repair axis therefore has ceiling:

\[
\boxed{\operatorname{Ceiling}(R0)=1/4.}
\]

This does not by itself define candidate-semantic exactness, which is evaluated separately.

### R1 — always produce some extension

Ignoring candidate semantics and asking only whether to emit a repair or `NO_SUPPORTED_CANDIDATE`, three of the four classes have support and one does not.

Thus the reflex:

```text
INSUFFICIENT -> always emit some extension
```

has support/null ceiling:

\[
\boxed{\operatorname{Ceiling}(R1)=3/4.}
\]

It fails the required unsupported case.

### R2 — fixed conjunction-like reflex

A fixed operator-family reflex adequate for Class A must fail semantic exactness on Class B, Class C, and Class D.

Preregistered coarse-axis ceiling:

\[
\boxed{\operatorname{Ceiling}(R2)\le1/4.}
\]

Execution must report the exact semantic adequacy pattern rather than assume it from names.

---

## 14. Anonymous encoding requirements

Run at least 64 anonymous encodings.

For each encoding:

- permute world-state labels consistently;
- permute exposed coordinate handles;
- independently flip public binary experiment output tokens;
- permute correction-context identifiers;
- rename the Boolean meta-primitive handle;
- rename pool handles;
- permute emitted experiment/candidate handles and candidate enumeration order;
- evaluate candidate equality only by counterfactual experiment-partition closure fingerprints;
- do not expose target formulas, target family names, repair-axis labels, operator names, `adequate`, `best`, or `supported` flags;
- in Class D, randomly choose which of five latent coordinates is inaccessible while exposing only the other four to `S_D` and `M0`.

The candidate-synthesis result must be invariant to naming and public output polarity.

---

## 15. Primary endpoints

Execution must report:

1. upstream closure-diagnosis hard-regression status;
2. recomputed current closure size/checksum for every substrate class;
3. current closure-wide `R_corr` and `q_max` proving `D_closure=INSUFFICIENT` before synthesis;
4. complete `M0` grammar ledger and expanded specification burden;
5. number of raw syntax programs generated;
6. number of distinct synthesized binary truth functions;
7. number of distinct semantic candidate closure fingerprints after deduplication;
8. number of minimal adequate candidate classes per episode;
9. all candidate `CanRestore` outcomes derived from lower-level partitions;
10. Class-A synthesis success;
11. Class-B synthesis success and semantic difference from Class A;
12. Class-C reuse/depth necessity and failure of `BASE x BASE`-only candidates;
13. Class-D zero-supported-candidate certificate and `NO_SUPPORTED_CANDIDATE` output;
14. R0/R1/R2 restricted-control ceilings;
15. M1/M2/M3 anti-scaffold classifications;
16. proof that no candidate was bound into the live substrate;
17. proof that no candidate ranking, extension cost, or authorization variable was used.

Terminal downstream task performance is **not** a primary endpoint because no candidate is bound.

---

## 16. Primary success conditions

Across 64 encodings × 4 synthesis classes:

```text
Class A: adequate candidate-set synthesis      64 / 64
Class B: adequate candidate-set synthesis      64 / 64
Class C: adequate reuse/depth candidate set     64 / 64
Class D: NO_SUPPORTED_CANDIDATE                 64 / 64
-------------------------------------------------------
coarse synthesis outcome correctness           256 / 256
```

Additionally:

```text
Class A/B semantic candidate sets differ       64 / 64
Class C BASE x BASE-only repair succeeds         0 / 64
Class D any M0 repair succeeds                   0 / 64
candidate bindings performed                     0
extension-valued winner selections               0
```

Exact semantic candidate-set equality must be evaluated against an exhaustive evaluator-side enumeration of the same frozen `M0`; the synthesizer is not given that enumeration as input.

---

## 17. Failure interpretation

| Result | Interpretation |
|---|---|
| positive classes have no adequate generated candidate | `M0` insufficient for the intended synthesis claim |
| Class A and B collapse to the same fixed repair despite different semantic requirements | fixed-repair reflex / insufficient discrimination |
| Class C solved by a `BASE x BASE`-only edit | benchmark defect or target not actually depth-sensitive |
| Class D produces any `CanRestore=1` candidate | leakage, hidden primitive access, or benchmark defect |
| named-menu control succeeds | selection only; not synthesis evidence |
| opaque macro succeeds via stored candidate semantics | hidden specification |
| target-specific template succeeds | oracle displacement |
| primary `M0` synthesis succeeds | bounded extension-synthesis evidence relative to supplied meta-substrate |

---

## 18. Candidate claim if the preregistered result holds

If the full `M0` synthesizer constructs semantically adequate candidate classes for the three supported defect types, distinguishes the two operator-semantic cases, requires a structurally different reuse/depth edit in Class C, emits `NO_SUPPORTED_CANDIDATE` in the inaccessible-primitive case, and the anti-scaffold controls behave as frozen, the strongest permitted claim is:

\[
\boxed{
\textbf{
In these finite audited regimes, after diagnosing that the current experiment closure is insufficient, a system can synthesize non-oracular candidate construction-substrate transformations from a supplied target-blind lower-level meta-language, while withholding repair when that meta-language contains no supported candidate.
}
}
\]

This is **extension synthesis relative to `M0`**.

It does **not** establish:

- unrestricted extension invention;
- discovery of the meta-language itself;
- that `M0` is minimal;
- that the generated candidate set contains the globally best extension;
- extension valuation;
- authorization;
- binding;
- autonomous inheritance;
- held-out post-binding correction;
- unrestricted research agency;
- general self-modification.

---

## 19. The next boundary remains extension valuation

A successful synthesis result would move the empirical chain to:

\[
\boxed{
\text{closure diagnosis}\checkmark
\rightarrow
\text{extension synthesis}\checkmark
\rightarrow
\boxed{\text{extension valuation}}
\rightarrow
\text{authorization}
\rightarrow
\text{binding}
\rightarrow
\text{held-out consequence}.
}
\]

The next stage would then ask how to compare multiple adequate candidate transformations by warranted expected consequence and burden.

This preregistration does not ask that question.

---

## 20. Upstream regression boundary

The child executable must import and hard-assert the closure-diagnosis certificate from `7e3871c`:

```text
SEARCH_MISS:          256/256 SUFFICIENT
VALUATION_MISHANDLE:  256/256 SUFFICIENT
CLOSURE_INSUFFICIENT: 256/256 INSUFFICIENT
TOTAL:                768/768
D0 ceiling:           2/3
D1 ceiling:           2/3
D2 ceiling:           2/3
naive target-outside: 1/3
```

That executable recursively imports Gate 2 / Gate 1 / accessibility / valuation / navigation hard assertions.

As in the recent connector workflow, the new extension-synthesis panel may be freshly executed while older panels remain inherited hard assertions unless a genuine repository-process replay is performed.

Correct future provenance, if executed that way:

\[
\boxed{
\textbf{fresh extension-synthesis result with inherited hard regression assertions}.
}
\]

---

## 21. Research position after this preregistration

The empirical spine is now:

\[
\boxed{
\text{geometry}\checkmark
\rightarrow
\text{navigation}\checkmark
\rightarrow
\text{valuation}\checkmark
\rightarrow
\text{accessibility}\checkmark
\rightarrow
G_1:\text{ registry compression}\checkmark
\rightarrow
G_2:\text{ supplied-extension basin opening}\checkmark
\rightarrow
\text{closure diagnosis}\checkmark
\rightarrow
\boxed{\text{extension synthesis [preregistered]}}
\rightarrow
\text{extension valuation}.
}
\]

No `P_ep` ledger update, extension valuation artifact, authorization artifact, or binding artifact is authorized until this synthesis result exists.
