# Experiment-Planning Dependency Consolidation

## Status

This document consolidates the experiment-planning dependency picture after the reachable-refinement, controller-substitution, STOP-substitution, valuation-role, multi-candidate acquisition-order, valuation-role-minimality, accessibility-contraction, latent-registry-minimality, experiment-space-construction, and closure-insufficiency-diagnosis audits.

It is a **dependency ledger**, not a new theory layer and not a `P_ep,min` certificate.

Relevant empirical reference points:

```text
fadf503  reachable-refinement discriminant audit
68f2338  refinement-controller substitution audit
4694382  STOP-substitution audit
c97a5cf  valuation-role discriminant audit
9a32f94  multi-candidate acquisition-order audit
b7c068b  valuation-role minimality audit
6355333  accessibility contraction audit
c661e58  latent-registry minimality audit
ee1b9ac  experiment-space construction discriminant
7e3871c  closure-insufficiency diagnosis audit
```

The current empirical spine is:

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
\boxed{\text{extension discovery: unresolved}}.
}
\]

The governing distinctions now include:

\[
\boxed{\text{failure}\neq\text{closure insufficiency}}
\]

\[
\boxed{\text{closure diagnosis}\neq\text{extension discovery}}
\]

\[
\boxed{\text{basin opening under a supplied extension}\neq\text{discovery of the opening}.}
\]

---

## 1. Empirical dependency history

### 1.1 Navigation / termination

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
\boxed{STOP_{\rm primitive}\notin N_{P_{\rm ep}}.}
\]

The surviving role is:

\[
\boxed{T_{\rm stop}=\text{terminate when no warranted continuation remains}.}
\]

### 1.2 Valuation

At `c97a5cf`, separate cardinal `(V,C)` was replaced by `kappa=C/V` with zero mismatches over 320 decisions:

\[
\boxed{(V,C)_{\rm separate}\notin N_{P_{\rm ep}}.}
\]

At `9a32f94`:

\[
\operatorname{Ceiling}(Q^\bot)=13/24,
\qquad
\operatorname{Ceiling}(Q^\bot+\mathrm{Pareto})=17/24.
\]

An on-demand compensated comparator and max-only co-maximal tournament matched the cardinal reference on all 512 encoded states:

\[
\boxed{q_{\rm cardinal}\notin N_{P_{\rm ep}}},
\qquad
\boxed{\text{stored full ranking}\notin N_{P_{\rm ep}}.}
\]

At `b7c068b`, explicit controller-side `R_corr` was removed while preserving 512/512 choices. Contract-aware mirror choices were 128/128; the contract-blind ceiling was `1/2`.

The acquisition-burden ablations established:

\[
\operatorname{Ceiling}(\text{no burden})
=
\operatorname{Ceiling}(\text{burden order})
=
1/4
\]

and:

\[
\operatorname{Ceiling}(\text{relative burden without COMMIT anchor})=4/5.
\]

The surviving valuation role is:

\[
\boxed{
\text{derive corrective consequence under the correction contract}
+
\text{quantitative acquisition burden anchored to COMMIT}
\rightarrow
\text{maximal worthwhile refinement}.
}
\]

### 1.3 Accessibility

At `6355333`:

\[
\boxed{B_{\rm access}:15\rightarrow1}
\]

while preserving:

```text
target reachability 960/960
downstream choice   960/960
```

Therefore explicit per-probe access enumeration is not necessary for the audited fixed registry.

Controls:

```text
no access      0/960
first 7/15   448/960 = 7/15
target lookup 960/960 but 15 semantic hints -> oracle displacement
```

Earned:

\[
\boxed{\text{latent experiment existence}\neq\text{experiment accessibility}.}
\]

### 1.4 Registry compression

At `c661e58`, Gate 1 replaced 15 explicit experiment-semantic bindings with:

```text
4 coordinate evidence primitives
1 reusable XOR operator
1 target-blind recursive closure rule
2 generic generation constraints
```

so:

\[
\boxed{B_{\mathcal E^\star}:15\rightarrow8}
\]

while preserving:

```text
15/15 target partitions per encoding
precision / recall       1.0 / 1.0
exact extensional match  64/64
extra partitions         0
downstream choices       960/960
```

Controls:

\[
\operatorname{Coverage}(R2)=4/15,
\qquad
\operatorname{Coverage}(R3)=10/15.
\]

The opaque family macro was behaviorally exact but expanded to 15 hidden semantic obligations; the context-target generator was oracle displacement.

Earned:

\[
\boxed{\text{registry compression}\neq\text{registry expansion}.}
\]

### 1.5 Supplied-extension basin opening

At `ee1b9ac`, the complete old closure was recomputed:

```text
|C0| = 15
checksum =
809abd918f17a77c779f76ce1b14ba4661e63b6834c4bec475fbe8a8f8eeed49
```

Four nonlinear targets were outside `C0` in all 64 encodings and every old parity experiment had `R_corr=0` for those contexts.

Baseline `G20`:

```text
novel target reachability 0/256
exact target choice       0/256
COMMIT                   256/256
```

Primary `S0 -> S1` intervention added target-blind `AND` plus post-extension XOR closure:

\[
\boxed{B_{\rm construction}:8\rightarrow10}
\]

and produced:

```text
|C1| = 1023
C0 strict subset C1 = true
novel target reachability 256/256
exact novel-target choice 256/256
```

Thus:

\[
\boxed{
do(S_{\rm construct}:S_0\rightarrow S_1)
\Rightarrow
\mathcal C_0\subsetneq\mathcal C_1.
}
\]

Controls:

```text
NOT extension:               |C|=15, 0/256
AND without recombination:   |C|=120, 192/256 = 3/4
direct targets:              256/256 but target-specific displacement
opaque degree-2 macro:       hidden/aliased specification
```

Earned:

\[
\boxed{\textbf{local causal basin opening relative to }S_0.}
\]

This did not establish discovery or authorization of `S1`.

### 1.6 Closure-insufficiency diagnosis

At `7e3871c`, the construction substrate remained fixed at `S0`; no extension, candidate operator, or alternative grammar was admitted.

The diagnostic object was:

\[
\boxed{
D_{\rm closure}
\in
\{\texttt{SUFFICIENT},\texttt{INSUFFICIENT}\}.
}
\]

All 768 failed episodes were matched on:

```text
Bayes baseline accuracy    0.625
exact-target R_corr        0.375
exact-target q             0.275
exact target outside C0    yes
correction unresolved      yes
actor terminal action      COMMIT
```

The only relevant difference was complete-closure normative capacity.

For the closure-sufficient `H` family:

```text
max C0 R_corr = 0.250
max C0 q      = +0.150
q-max count   = 1
```

For the closure-insufficient `G` family:

```text
max C0 R_corr = 0.000
max C0 q      = -0.100
```

Primary result across 64 anonymous encodings:

```text
SEARCH_MISS:
  SUFFICIENT          256/256

VALUATION_MISHANDLE:
  SUFFICIENT          256/256

CLOSURE_INSUFFICIENT:
  INSUFFICIENT        256/256

TOTAL:
  correct             768/768
```

Restricted-information ceilings:

\[
\boxed{\operatorname{Ceiling}(D0_{\rm failure-only})=2/3}
\]

\[
\boxed{\operatorname{Ceiling}(D1_{\rm actor-observed-capacity})=2/3}
\]

\[
\boxed{\operatorname{Ceiling}(D2_{\rm exact-target-membership})=2/3}
\]

while the naïve rule:

```text
exact target outside C0 -> INSUFFICIENT
```

achieved only:

\[
\boxed{1/3.}
\]

A directly supplied `q_max` can be exact but is oracle displacement.

Earned:

\[
\boxed{
\text{current closure failed to produce correction}
\neq
\text{current closure cannot produce correction}.
}
\]

and:

\[
\boxed{
\Pi(y)\notin\mathcal C_0
\not\Rightarrow
D_{\rm closure}=\texttt{INSUFFICIENT}.
}
\]

The valid result is **closure-insufficiency diagnosis relative to an exhaustively enumerable supplied construction substrate and frozen correction contract, without being supplied the missing extension**.

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
D_{\rm closure}
\}.
}
\]

These are bookkeeping labels, not newly asserted theoretical primitives.

Operationally:

- `S_refine`: preserve correction-relevant contingent refinement paths;
- `T_stop`: terminate when no continuation remains warranted;
- `Q_acquire^role`: identify a maximal worthwhile accessible refinement;
- `R_contract`: derive corrective consequence under the frozen correction contract;
- `B_anchored`: quantitative acquisition burden anchored to COMMIT;
- `A_registry`: generic access to the currently admitted registry;
- `S_construct`: primitive/operator/closure structure determining which experiment partitions can exist;
- `D_closure`: diagnose whether the complete current closure still contains a warranted corrective continuation.

Do not infer:

\[
P_{\rm ep,min}=P_{\rm ep}^{\rm surviving}.
\]

---

## 3. Dependency table

| Component / representation | Evidence status | Surviving role / boundary |
|---|---|---|
| `Pi_DP` | **removed** at `68f2338` | sequential correction-relevant refinement survives |
| `STOP_primitive` | **removed** at `4694382` | warranted termination survives |
| separate `V,C` | **removed** at `c97a5cf` | acquisition tradeoff survives |
| `Q^bot` | **insufficient**, ceiling `13/24` | multi-candidate comparison required |
| Pareto only | **insufficient**, ceiling `17/24` | compensated tradeoff required |
| cardinal `q` vector | **removed** at `9a32f94` | maximal-choice comparison survives |
| stored full ranking | **removed** at `9a32f94` | on-demand co-maximal choice survives |
| explicit `R_corr` | **removed** at `b7c068b` | contract-grounded consequence survives |
| no / ordinal burden | **insufficient**, ceiling `1/4` | quantitative burden survives |
| relative burden only | **insufficient**, ceiling `4/5` | COMMIT anchor survives |
| explicit access menu | **removed** at `6355333`; `15→1` | generic registry access survives |
| no access | **insufficient**, `0/960` | access path causally relevant |
| partial access | **coverage-limited**, `7/15` | inaccessible probes cannot be chosen |
| explicit 15-partition registry | **removed as necessary representation** at `c661e58`; `15→8` | registry-generating substrate survives |
| primitives only | **coverage-limited**, `4/15` | composition needed for that family |
| one XOR layer | **coverage-limited**, `10/15` | adequate closure needed |
| old closure `C0` | **causally insufficient** for Gate-2 nonlinear panel | closure boundary is real |
| `NOT` extension | syntax changed; geometry unchanged | new syntax is not basin opening |
| direct `AND` layer | **partial expansion**, `3/4` | operator availability alone insufficient |
| `S1` AND + post-closure | **sufficient supplied expansion**, `256/256` | local basin opening |
| failure-only diagnosis | **insufficient**, ceiling `2/3` | failure is non-diagnostic |
| actor-observed-capacity diagnosis | **insufficient**, ceiling `2/3` | exhaustive closure characterization matters |
| exact-target-membership diagnosis | **insufficient**, ceiling `2/3` | target absence is not closure insufficiency |
| supplied `q_max` | exact but **oracle displacement** | invalid primary diagnostic evidence |
| exhaustive closure-capacity diagnosis | **sufficient**, `768/768` | closure diagnosis earned in certified domain |
| extension discovery | **untested** | current frontier |
| extension valuation | **untested** | later frontier |
| authorization / binding | **untested** | later frontier |

---

## 4. Structural ceilings versus competence failure

The branch now includes structural / representational ceilings at multiple layers:

\[
13/24,\quad 17/24,\quad 1/2,\quad 1/4,\quad 4/5,\quad 7/15,\quad 4/15,\quad 10/15,\quad 3/4,\quad 2/3.
\]

The newest diagnostic controls make the construction-space analogue explicit:

\[
\boxed{
\text{closure impossibility}
\neq
\text{search failure}
\neq
\text{valuation failure}.
}
\]

This is not inferred from actor behavior; the successful diagnostic independently recomputes the complete current closure and its normative acquisition capacity.

---

## 5. Provenance

### Fresh closure-diagnosis evidence at `7e3871c`

```text
64 anonymous encodings
12 contexts per encoding
768 diagnostic episodes

SEARCH_MISS             256/256 SUFFICIENT
VALUATION_MISHANDLE     256/256 SUFFICIENT
CLOSURE_INSUFFICIENT    256/256 INSUFFICIENT

D0 failure-only ceiling               2/3
D1 actor-observed-capacity ceiling    2/3
D2 exact-target-membership ceiling    2/3
naive target-outside rule             1/3
```

The child executable imports `ee1b9ac`, which recursively wires Gate-1 / accessibility / valuation / navigation assertions.

Older audits were not freshly process-replayed in this connector session.

Correct provenance:

\[
\boxed{\textbf{fresh closure-insufficiency-diagnosis result with inherited hard regression assertions}.}
\]

---

## 6. Current empirical boundary

The program has now empirically separated:

\[
\boxed{
\text{supplied basin opening}
\neq
\text{diagnosis that opening is needed}
\neq
\text{discovery of the opening}.
}
\]

Gate 2 established that changing `S_construct` can open a useful new basin.

`7e3871c` now establishes, in the finite certified regime, that the system can distinguish:

\[
\boxed{
\exists e\in\mathcal C_0:q(e)>0
}
\]

from:

\[
\boxed{
\forall e\in\mathcal C_0:q(e)\le0
}
\]

even when both observed actors fail and commit, and even when the exact target lies outside `C0` in both cases.

The next scientific frontier is therefore:

\[
\boxed{
D_{\rm closure}
\rightarrow
\widehat S_{\rm candidate}
}
\]

with **extension discovery** isolated from:

\[
\text{extension valuation}
\rightarrow
\text{authorization}
\rightarrow
\text{binding}
\rightarrow
\text{held-out correction}.
\]

No extension-discovery result is claimed here.

`P_ep,min` remains explicitly unresolved.
