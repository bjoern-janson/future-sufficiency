# Experiment-Planning Dependency Consolidation

## Status

This document consolidates the experiment-planning dependency picture after the reachable-refinement, controller-substitution, STOP-substitution, valuation-role, multi-candidate acquisition-order, valuation-role-minimality, accessibility-contraction, and latent-registry-minimality audits.

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
```

The current phase is:

\[
\boxed{
\text{geometry}
\rightarrow
\text{navigation}
\rightarrow
\text{valuation}
\rightarrow
\text{accessibility}
\rightarrow
\text{registry specification minimality}
\rightarrow
\boxed{\text{experiment-space construction}}.
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

and now:

\[
\boxed{\text{registry compression}\neq\text{registry expansion}.}
\]

---

## 1. Empirical contraction history

### 1.1 Reachable refinement geometry

At `fadf503`, matched static evidence resources but different contingent refinement geometry produced different timely correction possibility.

Earned:

\[
\boxed{\text{eventual identifiability}\neq\text{future-sufficient identifiability}.}
\]

The surviving role is that correction-relevant contingent refinement paths must remain reachable before the applicable commitment boundary.

### 1.2 Dynamic programming

At `68f2338`, Bellman dynamic programming was replaced by a reachability-preserving controller with zero actions outside the DP-optimal set across 3,584 visited decisions.

Therefore:

\[
\boxed{\Pi_{\rm DP}\notin N_{P_{\rm ep}}}
\]

for the observed navigation behavior.

The surviving role is:

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

The audit simultaneously preserved:

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

An on-demand compensated comparator:

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

The surviving acquisition role is:

\[
\boxed{Q_{\rm acquire}^{\rm role}=\text{identify a currently maximal worthwhile refinement}.}
\]

### 1.7 Explicit `R_corr`

At `b7c068b`, explicit controller-side `R_corr` was removed. Corrective consequence was derived directly from the evidence partition and frozen correction contract, preserving 512/512 multi-candidate choices.

The contract-dependence mirror gave:

```text
contract-aware: 128/128
contract-blind ceiling: 1/2
```

Therefore:

\[
\boxed{R_{\rm corr}^{\rm explicit}\text{ is representation-contingent}}
\]

while correction relevance remains contract-grounded.

This is controller-interface contraction, not external-specification reduction.

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

The surviving role is:

\[
\boxed{\textbf{quantitative acquisition burden anchored to the COMMIT boundary}.}
\]

The literal symbol `kappa` is not claimed uniquely necessary.

### 1.9 Explicit probe menu

At `6355333`, the fixed 15-probe latent registry was held constant while the access interface changed.

The access ledger contracted:

\[
\boxed{B_{\rm access}:15\rightarrow1}
\]

from 15 explicit menu clauses to one target-blind `ALL_REGISTRY` rule, while preserving:

```text
target reachability 960/960
downstream choice   960/960
```

Therefore:

\[
\boxed{\text{explicit per-probe access enumeration}\notin N_{P_{\rm ep}}}
\]

for this fixed finite registry.

The no-access control gave 0/960. The target-blind first-7 control gave exactly 448/960 = 7/15. The context-to-target lookup gave 960/960 but required 15 semantic hints and was oracle displacement.

Earned:

\[
\boxed{\text{latent experiment existence}\neq\text{experiment accessibility}.}
\]

### 1.10 Explicit latent registry

At `c661e58`, Gate 1 attacked the remaining registry specification while holding the useful experiment family extensionally fixed.

Reference R0 supplied 15 explicit experiment-semantic bindings:

\[
\boxed{B_{\mathcal E^\star}^{R0}=15.}
\]

Primary R1 supplied only:

```text
4 coordinate evidence primitives
1 reusable XOR operator
1 target-blind recursive closure rule
2 generic generation constraints
```

with no target hints or family labels:

\[
\boxed{B_{\mathcal E^\star}^{R1}=8.}
\]

Across 64 anonymous encodings:

```text
R1 target partitions recovered   15/15 per encoding
R1 precision / recall            1.0 / 1.0
R1 exact extensional equality    64/64
R1 extra partitions              0
R1 downstream choices            960/960
```

Therefore:

\[
\boxed{B_{\mathcal E^\star}:15\rightarrow8}
\]

while:

\[
\boxed{\Pi(\mathcal E^\star_{R1})=\Pi(\mathcal E^\star_{R0}).}
\]

The explicit 15-entry latent registry is therefore not a necessary representation for this fixed family.

This is **registry compression**, not registry expansion.

### 1.11 Registry controls

R2, primitives only, recovered exactly:

\[
\boxed{4/15}
\]

and produced:

\[
\boxed{256/960=4/15}
\]

downstream agreement.

R3, one XOR layer without recursive closure, recovered:

\[
\boxed{10/15}
\]

and produced:

\[
\boxed{640/960=10/15.}
\]

Neither exceeded its extensional coverage ceiling.

Thus:

\[
\boxed{\text{primitive availability}\neq\text{adequate compositional closure}.}
\]

R4, the opaque `ALL_PARITIES_4` macro, was behaviorally exact but had:

```text
visible burden  = 1
expanded burden = 15 semantic obligations
```

and therefore counted as hidden specification / notation compression.

R5, a context-to-target experiment generator, could produce 960/960 behavior but required 15 target hints and did not recover a context-independent registry. It was oracle displacement.

---

## 2. Current surviving role / supplied-substrate inventory

The branch should now be described at the role level rather than by its original implementation list.

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
\text{registry-generating substrate}
\}.
}
\]

These are bookkeeping labels, not new theoretical primitives.

Operationally:

- `S_refine`: preserve correction-relevant contingent refinement paths;
- `T_stop`: terminate when no continuation remains warranted;
- `Q_acquire^role`: identify a currently maximal worthwhile accessible refinement;
- `R_contract`: derive corrective consequence under the frozen correction contract;
- `B_anchored`: quantitative acquisition burden anchored to COMMIT;
- `A_registry`: generic target-blind access to the currently admitted registry;
- registry-generating substrate: enough primitive semantics, composition, and closure to recover the admitted experiment family.

The audited R1 implementation is one sufficient registry-generating substrate. It is **not** established as globally minimal, and its four-coordinate basis or XOR operator is not claimed universally necessary.

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
| primitives only | **coverage-limited**, `4/15`, 256/960 | composition required for this family |
| one XOR layer | **coverage-limited**, `10/15`, 640/960 | adequate closure required |
| opaque family macro | behaviorally exact but expanded burden `15` | notation compression only |
| context-target experiment generator | behaviorally exact but **oracle displacement** | not a context-independent registry |
| R1 basis + XOR closure | **sufficient**, exact 15/15 and 960/960 | current Gate-1 contraction endpoint; not global minimum |
| experiment-space expansion mechanism | **untested** | Gate 2 frontier |

---

## 4. Current role-level compression

The audited experiment-planning branch can now be summarized operationally as:

\[
\boxed{
\text{derive an admitted experiment registry from a compact supplied substrate}
\rightarrow
\text{generic access}
\rightarrow
\text{contract-derived corrective consequence}
+
\text{COMMIT-anchored burden}
\rightarrow
\text{maximal worthwhile refinement}
}
\]

embedded inside:

\[
\boxed{S_{\rm refine}+T_{\rm stop}.}
\]

Removed implementation / representation mass now includes:

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
\text{explicit 15-entry experiment registry}&\downarrow.
\end{aligned}
}
\]

What has **not** disappeared is the functional need for:

\[
\boxed{
\text{correction contract}
+
\text{anchored burden}
+
\text{access path}
+
\text{some admitted-registry-generating substrate}.
}
\]

---

## 5. Specification accounting

The accessibility phase separated:

\[
B_{\rm total}=B_{\mathcal E^\star}+B_{\rm access}.
\]

At `6355333`:

\[
\boxed{B_{\rm access}:15\rightarrow1}
\]

while the registry specification was frozen.

At `c661e58`, the access rule remained frozen and Gate 1 changed only the registry specification:

\[
\boxed{B_{\mathcal E^\star}:15\rightarrow8.}
\]

The Gate-1 ledger is:

| Representation | Visible burden | Expanded burden | Recovery | Downstream | Status |
|---|---:|---:|---:|---:|---|
| R0 explicit registry | 15 | 15 | 15/15 | 960/960 | reference |
| R1 basis + XOR closure | 8 | 8 | 15/15 | 960/960 | **valid contraction** |
| R2 primitives only | 4 | 4 | 4/15 | 256/960 | insufficient |
| R3 one XOR layer | 7 | 7 | 10/15 | 640/960 | insufficient |
| R4 opaque macro | 1 | 15 | 15/15 | 960/960 | hidden specification |
| R5 context-target generator | 16 | 16 | no context-independent registry | 960/960 | oracle displacement |

The governing anti-scaffold rule remains:

\[
\boxed{\textbf{Where did the complexity go?}}
\]

and, specifically:

\[
\boxed{\text{compressed syntax}\not\Rightarrow\text{compressed specification}.}
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
=
1/4,
\]

\[
\operatorname{Ceiling}(\text{relative burden without COMMIT anchor})=4/5,
\]

\[
\operatorname{Ceiling}(A3)=7/15,
\]

and now:

\[
\boxed{\operatorname{Coverage}(R2)=4/15}
\]

\[
\boxed{\operatorname{Coverage}(R3)=10/15.}
\]

The R2/R3 downstream scores match those coverage limits exactly. These are substrate-expression failures, not optimizer failures.

---

## 7. Provenance and regression status

### Fresh Gate-1 evidence at `c661e58`

```text
64 anonymous encodings
15 correction contexts
960 downstream evaluations

R0 explicit:
  15/15 partitions
  64/64 exact extensional recovery
  960/960 choices

R1 basis + XOR closure:
  15/15 partitions
  precision/recall 1/1
  0 extras
  64/64 exact extensional recovery
  960/960 choices
  expanded B_E* = 8

R2 primitives:
  4/15 partitions
  256/960 choices

R3 one layer:
  10/15 partitions
  640/960 choices

R4 opaque macro:
  960/960 behavior
  expanded burden 15
  invalid contraction

R5 target generator:
  960/960 behavior
  15 target hints
  oracle displacement
```

The accessibility-source semantic checksum remains:

```text
54b7375f6ff283a3dff9f06bdaf67cced806411c9277021b0f9579c50cf45e59
```

The canonical target partition-set checksum is:

```text
809abd918f17a77c779f76ce1b14ba4661e63b6834c4bec475fbe8a8f8eeed49
```

### Inherited hard regressions

The `c661e58` executable imports the accessibility audit, which recursively wires the valuation/navigation assertions.

The Gate-1 panel was freshly executed in the connector session. Older audits were not freshly process-reexecuted there.

Correct provenance:

\[
\boxed{\textbf{fresh latent-registry-minimality result with inherited hard regression assertions}.}
\]

---

## 8. Current empirical boundary

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
\boxed{G_2:\text{ experiment-space construction}}.
}
\]

Gate 1 earns:

\[
\boxed{
B_{\mathcal E^\star}\downarrow
\land
\mathcal E^\star\text{ unchanged extensionally}.
}
\]

It does **not** earn:

\[
\boxed{\mathcal E_t^\star\subsetneq\mathcal E_{t+1}^\star.}
\]

No useful experiment outside the old recoverable family became available at `c661e58`.

Therefore this ledger does not claim:

- experiment invention;
- experiment-space expansion;
- ontology construction;
- \(\mathfrak R_{E,t}\to\mathfrak R_{E,t+1}\);
- basin opening;
- unrestricted experiment generation.

The next scientific frontier is Gate 2: a useful refinement must be unavailable under the old admitted experiment substrate and become available only after that substrate changes, with specification burden and oracle displacement audited separately.

No Gate-2 artifact is created by this consolidation.

`P_ep,min` remains explicitly unresolved.
