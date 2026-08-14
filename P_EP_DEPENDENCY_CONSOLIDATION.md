# Experiment-Planning Dependency Consolidation

## Status

This document is the dependency ledger for the experiment-planning branch. It is not a new theory layer and it is not a `P_ep,min` certificate.

Relevant empirical anchors:

```text
fadf503  reachable-refinement discriminant
68f2338  refinement-controller substitution
4694382  STOP substitution
c97a5cf  valuation-role discriminant
9a32f94  multi-candidate acquisition-order discriminant
b7c068b  valuation-role minimality
6355333  accessibility contraction
c661e58  latent-registry minimality / Gate 1
 ee1b9ac experiment-space construction / Gate 2
7e3871c  closure-insufficiency diagnosis
9a50f07  extension synthesis relative to M0
```

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
\text{extension synthesis}\checkmark
\rightarrow
\boxed{\text{extension valuation: unresolved}}.
}
\]

The governing boundaries are:

\[
\boxed{
\text{failure}
\neq
\text{closure insufficiency}
\neq
\text{extension synthesis}
\neq
\text{extension valuation}
\neq
\text{authorization}
\neq
\text{binding}.
}
\]

and:

\[
\boxed{
\text{candidate-space construction}
\neq
\text{candidate selection from a supplied menu}.
}
\]

---

## 1. Empirical dependency history

### 1.1 Reachable refinement geometry

At `fadf503`, matched static resources but different contingent refinement geometry produced different timely correction possibility.

Earned:

\[
\boxed{\text{eventual identifiability}\neq\text{future-sufficient identifiability}.}
\]

The surviving role is preservation of correction-relevant contingent refinement paths before their commitment boundary.

### 1.2 Navigation implementation

At `68f2338`, Bellman dynamic programming was replaced by a reachability-preserving controller with zero actions outside the DP-optimal set across 3,584 visited decisions:

\[
\boxed{\Pi_{\rm DP}\notin N_{P_{\rm ep}}.}
\]

The surviving role is:

\[
\boxed{S_{\rm refine}=\text{preserve correction-relevant contingent refinement structure}.}
\]

At `4694382`, primitive `STOP` was removed. Derived termination matched all 1,536 primitive STOP decisions with zero normalized trajectory mismatches:

\[
\boxed{STOP_{\rm primitive}\notin N_{P_{\rm ep}}}
\]

while:

\[
\boxed{T_{\rm stop}=\text{terminate when no warranted continuation remains}}
\]

survives.

### 1.3 Valuation representation

At `c97a5cf`, separate cardinal `V,C` was replaced by normalized burden `kappa=C/V` with zero mismatches across 320 decisions:

\[
\boxed{(V,C)_{\rm separate}\notin N_{P_{\rm ep}}.}
\]

At `9a32f94`:

\[
\operatorname{Ceiling}(Q^\bot)=13/24,
\qquad
\operatorname{Ceiling}(Q^\bot+\mathrm{Pareto})=17/24.
\]

An on-demand compensated comparator and a max-only co-maximal tournament each matched the cardinal reference on 512/512 states. Therefore the cardinal `q` vector and stored full ranking are not necessary representations for the observed choices.

At `b7c068b`, explicit controller-side `R_corr` was removed while contract-derived consequence remained exact. The same audit established:

\[
\operatorname{Ceiling}(\text{no burden})=1/4,
\]

\[
\operatorname{Ceiling}(\text{burden order only})=1/4,
\]

\[
\operatorname{Ceiling}(\text{relative burden without COMMIT anchor})=4/5.
\]

The surviving valuation role is therefore:

\[
\boxed{
\text{contract-derived corrective consequence}
+
\text{quantitative acquisition burden anchored to COMMIT}.
}
\]

### 1.4 Accessibility contraction

At `6355333`, the latent 15-probe registry remained fixed while the access interface contracted:

\[
\boxed{B_{\rm access}:15\rightarrow1}
\]

with:

```text
reachability 960/960
choice       960/960
```

No access gave `0/960`; first-7 access gave exactly `448/960 = 7/15`; a context-target lookup was behaviorally perfect but required 15 semantic hints and was classified as oracle displacement.

Therefore:

\[
\boxed{\text{explicit per-probe access enumeration}\notin N_{P_{\rm ep}}}
\]

for the audited fixed registry.

### 1.5 Gate 1 — registry compression

At `c661e58`, the explicit 15-partition registry was replaced by a target-blind compositional substrate:

```text
4 coordinate primitives
1 reusable XOR operator
1 recursive closure rule
2 generic constraints
```

so:

\[
\boxed{B_{\mathcal E^\star}:15\rightarrow8}
\]

while preserving:

```text
15/15 target partitions
64/64 exact extensional recovery
0 extra partitions
960/960 downstream choices
```

R2 primitives-only recovered `4/15`; R3 one-XOR-layer recovered `10/15`. The opaque family macro retained expanded burden `15`; the context-target generator was oracle displacement.

Earned:

\[
\boxed{
\text{explicit experiment registry is not a necessary representation for this family}.
}
\]

This was registry compression, not experiment-space expansion.

### 1.6 Gate 2 — supplied-extension basin opening

At `ee1b9ac`, the complete old closure was recomputed:

```text
|C0| = 15
checksum = 809abd918f17a77c779f76ce1b14ba4661e63b6834c4bec475fbe8a8f8eeed49
```

Four nonlinear correction targets were outside `C0`, and every old parity experiment had zero correction relevance for them.

The intervention:

\[
\boxed{S_0\rightarrow S_1}
\]

added a target-blind nonlinear operator plus adequate post-extension composition, giving:

```text
|C1| = 1023
C0 strict subset C1
novel target reachability 256/256
exact novel-target choice 256/256
```

with:

\[
\boxed{B_{\rm construction}:8\rightarrow10.}
\]

Controls:

```text
NOT extension: geometry unchanged, 0/256
AND without post-extension recombination: 192/256 = 3/4
direct target registry: target-specific displacement
opaque family macro: hidden/aliased specification
```

Earned:

\[
\boxed{
\textbf{local causal basin opening relative to the audited }S_0.
}
\]

This did not establish discovery or authorization of the extension.

### 1.7 Closure-insufficiency diagnosis

At `7e3871c`, all observed actors failed and terminated at COMMIT, but the diagnostic independently recomputed the complete current closure and its normative acquisition capacity.

Across 64 anonymous encodings:

```text
SEARCH_MISS          256/256 -> SUFFICIENT
VALUATION_MISHANDLE  256/256 -> SUFFICIENT
CLOSURE_INSUFFICIENT 256/256 -> INSUFFICIENT
TOTAL                768/768
```

Restricted representations gave:

\[
\operatorname{Ceiling}(D0)=
\operatorname{Ceiling}(D1)=
\operatorname{Ceiling}(D2)=2/3,
\]

while the naive rule `target outside C0 -> INSUFFICIENT` scored only `1/3`.

Earned:

\[
\boxed{
\text{current closure failed to produce correction}
\neq
\text{current closure cannot support warranted continuation}.
}
\]

The result stopped at:

\[
\boxed{E_{\rm failure}\rightarrow D_{\rm closure}.}
\]

### 1.8 Extension synthesis relative to supplied `M0`

At `9a50f07`, the synthesis mechanism received no named extension menu. It constructed candidate transformations from a supplied target-blind meta-substrate `M0`.

`M0` contains:

```text
1 opaque two-input Boolean truth basis
2 provenance pool roles
3 generic program combinators
3 grammar clauses
3 search-bound clauses
0 semantic hints
0 target hints
--------------------------------
expanded B_M0 = 12
```

The Boolean basis generated:

```text
102 raw syntax trees
10 distinct binary truth functions
```

Candidate programs were executed only counterfactually, deduplicated by resulting experiment-closure fingerprint, and pruned to inclusion-minimal adequate semantic candidate classes.

No candidate was ranked by extension value, authorized, or bound.

#### A/B repair-axis discriminant

Classes A and B begin from the same `15`-partition closure with:

\[
\max_{e\in\mathcal C_0}q(e)=-0.1.
\]

Exhaustive semantic search produced distinct inclusion-minimal repair classes:

```text
A: 1 minimal class
   family size 120
   delta       105
   max R_corr  0.25
   max q       0.15

B: 1 different minimal class
   family size 50
   delta       35
   max R_corr  0.25
   max q       0.15
```

Across anonymous encodings:

\[
\boxed{
\widehat{\mathfrak S}_A\neq\widehat{\mathfrak S}_B
\quad 64/64.
}
\]

Therefore:

\[
\boxed{
D_{\rm closure}=\texttt{INSUFFICIENT}
\not\Rightarrow
\text{one fixed repair reflex}.
}
\]

#### C reuse/depth discriminant

Class C begins from the complete degree-`<=2` closure:

```text
|C| = 1023
checksum = c51cc447000204a4c32e205d4e8daab954a52b80939664bbab2968629299efb7
current max q = -0.1
```

Exhaustive one-layer `BASE x BASE` edits produced zero adequate candidate fingerprints.

Two inclusion-minimal adequate semantic candidate classes were synthesized only when nonlinear results could be reused as inputs:

```text
candidate 1: family 1653, delta 630,  max q 0.025
candidate 2: family 2388, delta 1365, max q 0.025
```

Across 64 encodings:

```text
reuse/depth candidate synthesis 64/64
BASE x BASE-only adequate        0/64
```

Thus:

\[
\boxed{
\text{missing operator semantics}
\neq
\text{insufficient compositional depth/reuse}.
}
\]

#### D warranted null synthesis

Class D withholds one primitive evidence coordinate from both the current substrate and `M0`.

Every current or synthesized experiment remains independent of the hidden coordinate:

\[
R_{\rm corr}=0
\]

for every generated candidate, while direct evidence about the hidden coordinate would have `q=0.4` if such access existed.

Observed:

```text
adequate M0 candidates       0
NO_SUPPORTED_CANDIDATE      64/64
any supported M0 repair      0/64
```

Therefore:

\[
\boxed{
D_{\rm closure}=\texttt{INSUFFICIENT}
\not\Rightarrow
\text{expand anyway}.
}
\]

This is a positive reopening-discipline result.

#### Aggregate extension-synthesis result

```text
A adequate candidate synthesis       64/64
B distinct candidate synthesis       64/64
C reuse/depth candidate synthesis    64/64
D NO_SUPPORTED_CANDIDATE             64/64
------------------------------------------
coarse synthesis outcome            256/256
```

Wrong-extension controls were present and inadequate. A diagnosis-only fixed-repair axis has ceiling `1/4`; an always-expand support/null reflex has ceiling `3/4`; instantiating an actual A-minimal repair as a fixed reflex produces the exact pattern `A=true, B=false, C=false, D=false`, again `1/4`.

The named-menu control can select correctly but is classified as selection only. The opaque repair macro is hidden specification. The target-specific synthesis template is oracle displacement.

Earned:

\[
\boxed{
\textbf{
In these finite audited regimes, after diagnosing construction-space insufficiency, a system can synthesize non-oracular candidate construction-substrate transformations from a supplied target-blind lower-level meta-language, while withholding repair when that meta-language contains no supported candidate.
}
}
\]

Scope:

\[
\boxed{\textbf{bounded extension synthesis relative to supplied }M_0.}
\]

This does not establish discovery of `M0`, global minimality of `M0`, extension valuation, authorization, binding, or unrestricted research agency.

---

## 2. Current surviving roles / supplied substrate

A provisional role-level inventory is:

\[
\boxed{
P_{\rm ep}^{\rm surviving}
=
\{
S_{\rm refine},
T_{\rm stop},
Q_{\rm acquire}^{\rm role},
R_{\rm contract},
B_{\rm anchored},
A_{\rm registry},
S_{\rm construct},
D_{\rm closure},
M_0\text{-relative synthesis}
\}.
}
\]

These are bookkeeping labels, not newly asserted theoretical primitives.

Operationally:

- `S_refine`: preserve correction-relevant contingent refinement paths;
- `T_stop`: terminate when no continuation remains warranted;
- `Q_acquire^role`: identify a currently maximal worthwhile accessible refinement;
- `R_contract`: derive corrective consequence under the frozen correction contract;
- `B_anchored`: quantitative acquisition burden anchored to COMMIT;
- `A_registry`: generic target-blind access to the admitted registry;
- `S_construct`: primitive/operator/closure structure determining which experiments can exist;
- `D_closure`: diagnose whether the complete current closure still contains a warranted continuation;
- `M0`-relative synthesis: construct minimal adequate candidate structural transformations or return `NO_SUPPORTED_CANDIDATE`.

`M0` itself remains externally supplied.

Do not infer:

\[
P_{\rm ep,min}=P_{\rm ep}^{\rm surviving}.
\]

---

## 3. Structural ceilings / impossibility certificates

Current branch certificates include:

\[
\operatorname{Ceiling}(Q^\bot)=13/24,
\qquad
\operatorname{Ceiling}(Q^\bot+\mathrm{Pareto})=17/24,
\]

\[
\operatorname{Ceiling}(\text{contract-blind relevance})=1/2,
\]

\[
\operatorname{Ceiling}(\text{no burden})=
\operatorname{Ceiling}(\text{burden order})=1/4,
\]

\[
\operatorname{Ceiling}(\text{relative burden without COMMIT anchor})=4/5,
\]

\[
\operatorname{Coverage}(A3)=7/15,
\qquad
\operatorname{Coverage}(R2)=4/15,
\qquad
\operatorname{Coverage}(R3)=10/15,
\]

\[
\operatorname{Coverage}(G23)=3/4,
\]

\[
\operatorname{Ceiling}(D0)=
\operatorname{Ceiling}(D1)=
\operatorname{Ceiling}(D2)=2/3,
\]

and now:

\[
\boxed{\operatorname{Ceiling}(\text{diagnosis-only fixed synthesis axis})=1/4,}
\]

\[
\boxed{\operatorname{Ceiling}(\text{always emit an extension})=3/4.}
\]

These are structural representation / reachability / synthesis limits, not optimizer-failure claims.

---

## 4. Specification accounting

The anti-scaffold rule remains:

\[
\boxed{\textbf{Where did the complexity go?}}
\]

Observed contractions / expansions:

\[
B_{\rm access}:15\rightarrow1,
\]

\[
B_{\mathcal E^\star}:15\rightarrow8,
\]

\[
B_{\rm construction}:8\rightarrow10
\quad\text{for supplied Gate-2 basin opening},
\]

and the synthesis stage introduces a supplied target-blind meta-substrate with:

\[
\boxed{B_{M_0}=12}
\]

under the finite clause ledger.

This is not a compression claim. It is the explicit specification burden relative to which bounded candidate synthesis is earned.

A named extension menu, opaque repair macro, or target-conditioned synthesis skeleton does not count as candidate-space construction.

---

## 5. Provenance

Fresh evidence at `9a50f07`:

```text
64 anonymous encodings
4 synthesis classes
256 synthesis episodes

A: minimal adequate set synthesized 64/64
B: distinct minimal adequate set    64/64
C: depth/reuse set synthesized      64/64
D: NO_SUPPORTED_CANDIDATE           64/64

A/B distinct                        64/64
C BASE x BASE adequate               0/64
D any M0 repair supported            0/64
bindings                              0
extension-valued winner selections    0
authorization decisions               0
```

The executable imports the closure-diagnosis audit and recursively wires the Gate-2 / Gate-1 / accessibility / valuation / navigation assertions. Those older panels were not freshly process-replayed in the connector session.

Correct provenance:

\[
\boxed{
\textbf{fresh extension-synthesis result with inherited hard regression assertions}.
}
\]

---

## 6. Current empirical boundary

The project has now earned:

\[
\boxed{
D_{\rm closure}
\rightarrow
M_0
\rightarrow
\widehat{\mathfrak S}_{\rm candidate}
\;\text{or}\;
\texttt{NO\_SUPPORTED\_CANDIDATE}
}
\]

in the audited finite regimes.

It has **not** earned:

- discovery of `M0` itself;
- unrestricted extension invention;
- a globally best candidate transformation;
- extension valuation;
- authority to modify `S_construct`;
- binding or inheritance of a candidate;
- held-out post-binding correction;
- unrestricted research agency;
- general self-modification.

The next causal boundary is therefore:

\[
\boxed{
\widehat S_{\rm candidate}
\rightarrow
Q_{\rm extension}.
}
\]

The next empirical question is which synthesized candidate extension is worth adopting under warranted consequence and burden. That question is **not** answered by this ledger update.

`P_ep,min` remains explicitly unresolved.
