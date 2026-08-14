# Experiment-Planning Dependency Consolidation

## Status

This document consolidates the experiment-planning dependency picture after the reachable-refinement, controller-substitution, STOP-substitution, valuation-role, multi-candidate acquisition-order, valuation-role-minimality, accessibility-contraction, latent-registry-minimality, and experiment-space-construction audits.

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
\boxed{\text{discovery / authorization of the opening: unresolved}}.
}
\]

The governing distinctions remain:

\[
\boxed{\text{removed implementation}\neq\text{removed functional role}}
\]

\[
\boxed{\text{behavioral substitution}\neq\text{substrate reduction}}
\]

\[
\boxed{\text{accessibility contraction}\neq\text{experiment construction}}
\]

\[
\boxed{\text{registry compression}\neq\text{registry expansion}}
\]

and now:

\[
\boxed{\text{basin opening under a supplied extension}\neq\text{discovery of the opening}.}
\]

---

## 1. Empirical contraction / dependency history

### 1.1 Reachable refinement geometry

At `fadf503`, matched static resources but different contingent refinement geometry produced different timely correction possibility.

Earned:

\[
\boxed{\text{eventual identifiability}\neq\text{future-sufficient identifiability}.}
\]

The role-level dependency is that correction-relevant contingent refinement paths must remain reachable before the applicable commitment boundary.

### 1.2 Dynamic programming

At `68f2338`, Bellman dynamic programming was replaced by a reachability-preserving controller with zero actions outside the DP-optimal set across 3,584 visited decisions.

Therefore:

\[
\boxed{\Pi_{\rm DP}\notin N_{P_{\rm ep}}}
\]

for the observed navigation behavior.

Surviving role:

\[
\boxed{S_{\rm refine}=\text{preserve correction-relevant contingent refinement structure}.}
\]

### 1.3 Primitive STOP

At `4694382`, primitive `STOP` was removed. Derived termination matched all 1,536 primitive STOP decisions with zero normalized trajectory mismatches.

Therefore:

\[
\boxed{STOP_{\rm primitive}\notin N_{P_{\rm ep}}}
\]

while:

\[
\boxed{T_{\rm stop}=\text{terminate when no warranted continuation remains}}
\]

survives.

### 1.4 Separate cardinal `V,C`

At `c97a5cf`, separate cardinal `V,C` was replaced by normalized burden `kappa=C/V` with zero mismatches across 320 valuation decisions.

Therefore:

\[
\boxed{(V,C)_{\rm separate}\notin N_{P_{\rm ep}}.}
\]

The audit also preserved:

\[
\boxed{I(e)\neq R_{\rm corr}(e)\neq Q_{\rm acquire}(e).}
\]

### 1.5 Candidate-vs-COMMIT and Pareto are insufficient

At `9a32f94`:

\[
\boxed{\operatorname{Ceiling}(Q^\bot)=13/24}
\]

and:

\[
\boxed{\operatorname{Ceiling}(Q^\bot+\mathrm{Pareto})=17/24.}
\]

Thus candidate-vs-COMMIT sign and uncompensated dominance are insufficient for the audited multi-candidate policy.

### 1.6 Cardinal `q` and stored total ranking

The on-demand compensated comparator:

\[
e_i\succ_Q e_j
\iff
R_i+\kappa_j>R_j+\kappa_i
\]

matched the cardinal reference on all 512 encoded states.

A max-only co-maximal tournament also matched 512/512 without storing a full ranking.

Therefore:

\[
\boxed{q_{\rm cardinal}\notin N_{P_{\rm ep}}}
\]

and:

\[
\boxed{\text{stored full ranking}\notin N_{P_{\rm ep}}}
\]

for the observed choices.

Surviving acquisition role:

\[
\boxed{Q_{\rm acquire}^{\rm role}=\text{identify a currently maximal worthwhile refinement}.}
\]

### 1.7 Explicit `R_corr`

At `b7c068b`, explicit controller-side `R_corr` was removed. Corrective consequence was derived directly from the evidence partition and frozen correction contract, preserving 512/512 multi-candidate choices.

Contract dependence:

```text
contract-aware:       128/128
contract-blind ceiling: 1/2
```

Therefore:

\[
\boxed{R_{\rm corr}^{\rm explicit}\text{ is representation-contingent}}
\]

while correction relevance remains contract-grounded.

### 1.8 Acquisition burden

The same audit found:

\[
\boxed{\operatorname{Ceiling}(-\kappa)=1/4}
\]

\[
\boxed{\operatorname{Ceiling}(\text{burden order only})=1/4}
\]

\[
\boxed{\operatorname{Ceiling}(\text{relative burden without COMMIT anchor})=4/5.}
\]

Anchored quantitative burden remained exact on 320/320.

Surviving role:

\[
\boxed{\textbf{quantitative acquisition burden anchored to the COMMIT boundary}.}
\]

The literal scalar encoding is not claimed uniquely necessary.

### 1.9 Explicit access menu

At `6355333`, the fixed 15-probe latent registry remained unchanged while the access interface contracted:

\[
\boxed{B_{\rm access}:15\rightarrow1}
\]

from 15 explicit menu clauses to one target-blind `ALL_REGISTRY` rule, preserving:

```text
target reachability 960/960
downstream choice   960/960
```

Therefore:

\[
\boxed{\text{explicit per-probe access enumeration}\notin N_{P_{\rm ep}}}
\]

for the audited fixed registry.

Controls:

```text
no access:             0/960
first 7 of 15:       448/960 = 7/15
target lookup:        960/960 but 15 semantic hints -> oracle displacement
```

Earned:

\[
\boxed{\text{latent experiment existence}\neq\text{experiment accessibility}.}
\]

### 1.10 Explicit latent registry

At `c661e58`, Gate 1 attacked registry specification while holding the useful experiment family extensionally fixed.

Reference:

\[
\boxed{B_{\mathcal E^\star}^{R0}=15}
\]

for 15 explicit semantic bindings.

Primary derived substrate:

```text
4 coordinate evidence primitives
1 reusable XOR operator
1 target-blind recursive closure rule
2 generic generation constraints
```

so:

\[
\boxed{B_{\mathcal E^\star}^{R1}=8.}
\]

Across 64 encodings:

```text
15/15 target partitions recovered per encoding
precision / recall       1.0 / 1.0
exact extensional match  64/64
extra partitions         0
downstream choices       960/960
```

Therefore:

\[
\boxed{B_{\mathcal E^\star}:15\rightarrow8}
\]

while:

\[
\boxed{\Pi(\mathcal E^\star_{R1})=\Pi(\mathcal E^\star_{R0}).}
\]

The explicit 15-entry registry is not a necessary representation for that family.

This is **registry compression**, not registry expansion.

### 1.11 Gate-1 controls

R2, primitives only:

\[
\boxed{4/15\text{ registry recall}\rightarrow256/960.}
\]

R3, one XOR layer:

\[
\boxed{10/15\text{ registry recall}\rightarrow640/960.}
\]

Neither exceeded its extensional coverage ceiling.

Thus:

\[
\boxed{\text{primitive availability}\neq\text{adequate compositional closure}.}
\]

R4, `ALL_PARITIES_4`, was behaviorally exact but expanded to 15 hidden semantic obligations. R5, context-to-target generation, achieved behavior only through 15 target hints and was oracle displacement.

### 1.12 Gate 2: old closure is genuinely insufficient

At `ee1b9ac`, the complete old Gate-1 construction substrate `S0` was recomputed rather than assumed.

Observed:

```text
|C0| = 15
C0 checksum = 809abd918f17a77c779f76ce1b14ba4661e63b6834c4bec475fbe8a8f8eeed49
```

Four nonlinear correction targets `n1...n4` were exhaustively checked against `C0`.

Across all 64 anonymous encodings:

```text
n1 outside C0: 64/64
n2 outside C0: 64/64
n3 outside C0: 64/64
n4 outside C0: 64/64
```

Every old parity experiment had:

\[
\boxed{R_{\rm corr}=0}
\]

for every nonlinear context.

With `kappa=0.1`, `S0` produced:

```text
novel target reachability 0/256
exact novel-target choice 0/256
COMMIT                  256/256
```

Therefore the Gate-2 baseline localizes a genuine closure limitation rather than a valuation or search failure:

\[
\boxed{
\text{useful target exists}
\land
\Pi(e_{\rm target})\notin\mathcal C_0
\land
\text{old admitted construction cannot expose it}.
}
\]

### 1.13 Gate 2: supplied target-blind basin opening

The primary intervention changed only the admitted experiment-construction substrate:

\[
\boxed{S_0\rightarrow S_1.}
\]

`S1` adds one generic target-blind `AND` operator and adequate post-extension XOR closure.

Construction burden changes:

\[
\boxed{B_{\rm construction}:8\rightarrow10.}
\]

No target-specific semantics, target formulas, context-to-target mappings, or winner hints are supplied.

Observed:

```text
|C1| = 1023
C1 checksum = c51cc447000204a4c32e205d4e8daab954a52b80939664bbab2968629299efb7
C0 strict subset C1 = true
novel target reachability 256/256
exact novel-target choice 256/256
```

All four target partitions are in:

\[
\boxed{\mathcal C_1\setminus\mathcal C_0.}
\]

Therefore the preregistered causal signature holds:

\[
\boxed{
B_{\rm construction}\uparrow
\land
\mathcal C_0\subsetneq\mathcal C_1
\land
\text{new correction-relevant partitions become reachable}.
}
\]

The earned claim is local and causal:

\[
\boxed{
\textbf{Changing the admitted experiment-composition substrate can open a strictly larger refinement space containing useful partitions that were unreachable under the complete prior closure.}
}
\]

This is a **local basin-opening result relative to `S0`**.

It does **not** establish autonomous discovery or authorization of the extension.

### 1.14 Gate-2 controls

`G22`, adding `NOT`, changes operator syntax but not experiment partition geometry:

```text
|C_NOT| = 15
C_NOT = C0
novel target reachability 0/256
exact target choice       0/256
COMMIT                   256/256
```

Thus:

\[
\boxed{\text{new operator syntax}\neq\text{experiment-space expansion}.}
\]

`G23`, adding `AND` without post-extension XOR recombination, produces:

```text
|C_G23| = 120
n1 reachable yes
n2 reachable yes
n3 reachable yes
n4 reachable no
exact target reachability / choice = 192/256 = 3/4
```

It does not exceed its preregistered coverage ceiling.

Important nuance: `n4` does not force COMMIT under `G23`. The partial family contains 18 tied refinements with:

```text
best partial R_corr = 0.125
best partial margin = 0.025
```

so the controller acquires a partial refinement while the exact `n4` partition remains unavailable.

This still establishes:

\[
\boxed{\text{nonlinear operator availability}\neq\text{adequate expanded compositional closure}.}
\]

`G24` directly supplies the four nonlinear targets and is classified as target-specific specification displacement.

`G25` behaves as follows:

- transparent macro alias: visible syntax 1, expanded burden 10 -> alias for `S1`, no independent evidence;
- direct opaque family macro: visible syntax 1, 1,023 hidden semantic bindings -> hidden specification.

---

## 2. Current surviving roles / supplied substrate

The experiment-planning branch should still be described at the role level, not by one implementation list.

A provisional inventory is:

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
S_{\rm construct}
\}.
}
\]

These are bookkeeping labels for surviving functional roles / supplied substrate, not newly asserted theoretical primitives.

Operationally:

- `S_refine`: preserve correction-relevant contingent refinement paths;
- `T_stop`: terminate when no continuation remains warranted;
- `Q_acquire^role`: identify a currently maximal worthwhile accessible refinement;
- `R_contract`: derive corrective consequence under the frozen correction contract;
- `B_anchored`: quantitative acquisition burden anchored to COMMIT;
- `A_registry`: generic target-blind access to the currently admitted registry;
- `S_construct`: admitted primitive / operator / closure structure determining which experiment partitions can exist.

Gate 1 showed one admitted registry can be generated compactly. Gate 2 showed changing `S_construct` can causally enlarge the reachable experiment space.

What remains **supplied** at Gate 2 is the extension itself: the new operator / closure contract is designer-provided and target-blind.

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
| contract-blind relevance | **insufficient**, ceiling `1/2` | correction contract remains constitutive |
| no burden | **insufficient**, ceiling `1/4` | burden role survives |
| burden order only | **insufficient**, ceiling `1/4` | burden magnitude matters |
| relative burden only | **insufficient**, ceiling `4/5` | COMMIT anchor matters |
| explicit 15-probe access menu | **removed** at `6355333`; `15→1`, 960/960 | generic registry access survives |
| no access | **insufficient**, 0/960 | access path causally relevant |
| partial access | **coverage-limited**, 448/960 = `7/15` | unavailable probes cannot be chosen |
| target access lookup | 960/960 but **oracle displacement** | invalid minimality evidence |
| explicit 15-partition registry | **removed as necessary representation** at `c661e58`; `15→8`, 960/960 | registry-generating substrate survives |
| Gate-1 primitives only | **coverage-limited**, `4/15`, 256/960 | composition required for that family |
| Gate-1 one XOR layer | **coverage-limited**, `10/15`, 640/960 | adequate closure required |
| Gate-1 opaque family macro | behaviorally exact but expanded burden `15` | notation compression only |
| old Gate-1 experiment closure `C0` | **causally insufficient** for nonlinear panel; 0/256 | closure boundary is real |
| `NOT` extension | syntax changes, geometry unchanged; 0/256 | new syntax is not basin opening |
| direct `AND` layer without recombination | **partial expansion**, 192/256 | new operator alone insufficient |
| `S1`: AND + post-extension closure | **sufficient Gate-2 expansion**, 256/256 | target-blind supplied basin opening |
| direct target registry | 256/256 but **target-specific displacement** | invalid construction evidence |
| opaque degree-2 macro | behaviorally exact but hidden/aliased burden | invalid independent construction evidence |
| discovery of `S1` | **untested** | next frontier |
| authorization / binding of `S1` | **untested** | next frontier |

---

## 4. Role-level compression and expansion

The branch has now separated three operations that were previously easy to conflate:

\[
\boxed{
\text{registry compression}
\neq
\text{registry accessibility}
\neq
\text{experiment-space expansion}.
}
\]

Operationally, the audited branch now supports:

\[
\boxed{
S_{\rm construct}
\rightarrow
\text{derived admitted registry}
\rightarrow
A_{\rm registry}
\rightarrow
R_{\rm contract}+B_{\rm anchored}
\rightarrow
Q_{\rm acquire}^{\rm role}
}
\]

inside:

\[
\boxed{S_{\rm refine}+T_{\rm stop}.}
\]

Gate 2 adds one more causal statement:

\[
\boxed{
do(S_{\rm construct}:S_0\rightarrow S_1)
\Rightarrow
\mathcal C_0\subsetneq\mathcal C_1.}
\]

Removed implementation / representation mass remains:

\[
\boxed{
\begin{aligned}
\Pi_{\rm DP}&\downarrow\\
STOP_{\rm primitive}&\downarrow\\
(V,C)_{\rm separate}&\downarrow\\
R_{\rm corr}^{\rm explicit}&\downarrow\\
q_{\rm cardinal}&\downarrow\\
\text{full ranking}&\downarrow\\
\text{explicit access menu}&\downarrow\\
\text{explicit 15-entry registry}&\downarrow.
\end{aligned}
}
\]

What has **not** disappeared is the need for some construction substrate adequate to generate the currently required experiment geometry.

---

## 5. Specification accounting

### Accessibility

At `6355333`:

\[
\boxed{B_{\rm access}:15\rightarrow1}
\]

while experiment semantics were frozen.

### Registry compression

At `c661e58`:

\[
\boxed{B_{\mathcal E^\star}:15\rightarrow8}
\]

while the useful experiment family remained extensionally identical.

### Basin opening

At `ee1b9ac`, Gate 2 is deliberately **not** a compression:

\[
\boxed{B_{\rm construction}:8\rightarrow10.}
\]

The relevant success criterion is not lower burden but changed reachable geometry under a target-blind supplied extension:

\[
\boxed{
B_{\rm construction}\uparrow
\land
\mathcal C_0\subsetneq\mathcal C_1
\land
\text{new useful partitions reachable}.
}
\]

Gate-2 ledger:

| Condition | Expanded construction burden | Family size | Exact target reachability / choice | Status |
|---|---:|---:|---:|---|
| G20 old `S0` | 8 | 15 | 0/256 | old closure insufficient |
| G21 `S1` = AND + post-extension closure | **10** | **1023** | **256/256** | valid supplied target-blind basin opening |
| G22 NOT | 10 | 15 | 0/256 | syntax only; no new geometry |
| G23 direct AND layer | 10 | 120 | 192/256 | partial expansion; inadequate closure |
| G24 direct nonlinear targets | 12 | 19 | 256/256 | target-specific displacement |
| G25 transparent macro | 10 expanded | 1023 | 256/256 | alias for G21 |
| G25 direct opaque macro | 1023 hidden bindings | 1023 | 256/256 | hidden specification |

The anti-scaffold rule remains:

\[
\boxed{\textbf{Where did the complexity go?}}
\]

and:

\[
\boxed{\text{compact syntax}\not\Rightarrow\text{compressed specification}.}
\]

---

## 6. Structural ceilings versus learner failure

The branch now contains structural insufficiency / coverage certificates at several layers:

\[
\operatorname{Ceiling}(Q^\bot)=13/24,
\qquad
\operatorname{Ceiling}(Q^\bot+\mathrm{Pareto})=17/24,
\]

\[
\operatorname{Ceiling}(\text{contract-blind relevance})=1/2,
\]

\[
\operatorname{Ceiling}(\text{no burden})
=
\operatorname{Ceiling}(\text{burden order})
=1/4,
\]

\[
\operatorname{Ceiling}(\text{relative burden without COMMIT anchor})=4/5,
\]

\[
\operatorname{Ceiling}(A3)=7/15,
\]

\[
\operatorname{Coverage}(R2)=4/15,
\qquad
\operatorname{Coverage}(R3)=10/15,
\]

and now:

\[
\boxed{\operatorname{Coverage}(G23)=3/4=192/256.}
\]

These are substrate-expression / reachability limits, not optimizer failures.

---

## 7. Provenance and regression status

### Fresh Gate-2 evidence at `ee1b9ac`

```text
64 anonymous encodings
4 nonlinear correction contexts
256 context-encoding evaluations

G20 old S0:
  |C0| 15
  nonlinear target reachability 0/256
  exact target choice 0/256
  COMMIT 256/256

G21 S1:
  |C1| 1023
  C0 strict subset C1
  nonlinear target reachability 256/256
  exact target choice 256/256

G22 NOT:
  family size 15
  geometry unchanged
  exact target choice 0/256

G23 direct AND layer:
  family size 120
  exact target choice 192/256
  ceiling 3/4 not exceeded

G24 direct targets:
  256/256 but target-specific displacement

G25 macro controls:
  transparent alias -> expanded burden 10
  opaque direct family -> 1023 hidden bindings
```

Old-closure checksum:

```text
809abd918f17a77c779f76ce1b14ba4661e63b6834c4bec475fbe8a8f8eeed49
```

Expanded-closure checksum:

```text
c51cc447000204a4c32e205d4e8daab954a52b80939664bbab2968629299efb7
```

### Inherited hard regressions

The `ee1b9ac` executable imports the Gate-1 audit, which recursively wires accessibility / valuation / navigation assertions.

The Gate-2 panel was freshly executed in the connector session. Older audits were not freshly process-reexecuted there.

Correct provenance:

\[
\boxed{\textbf{fresh Gate-2 experiment-space-construction result with inherited hard regression assertions}.}
\]

---

## 8. Current empirical boundary

Gate 1 earned:

\[
\boxed{B_{\mathcal E^\star}\downarrow\land\mathcal E^\star\text{ unchanged extensionally}.}
\]

Gate 2 now earns:

\[
\boxed{
S_0\rightarrow S_1
\Rightarrow
\mathcal C_0\subsetneq\mathcal C_1
}
\]

with useful partitions in `C1 \ C0` becoming reachable and choice-maximal under frozen downstream machinery.

The strongest permitted interpretation is:

\[
\boxed{\textbf{local causal basin opening relative to the audited Gate-1 substrate}.}
\]

This ledger does **not** claim:

- autonomous discovery of `AND`;
- diagnosis from failure evidence that `S0` is insufficient;
- warranted selection among candidate construction-substrate extensions;
- authorization to modify experiment machinery;
- autonomous binding / inheritance of the extension;
- unrestricted experiment invention;
- general ontology construction;
- self-modification;
- that `AND` is uniquely necessary;
- that the 1,023-partition family is minimal.

The next scientific frontier, if pursued, is therefore not another supplied basin-opening demonstration. It is the adaptive transformation chain:

\[
\boxed{
\text{failure evidence}
\rightarrow
\text{diagnosis of closure insufficiency}
\rightarrow
\text{candidate substrate transformation}
\rightarrow
\text{authorization}
\rightarrow
\text{expanded refinement space}.
}
\]

That chain remains untested.

`P_ep,min` remains explicitly unresolved.
