# Experiment-Planning Dependency Consolidation

## Status

This document consolidates the experiment-planning dependency picture after the reachable-refinement, controller-substitution, STOP-substitution, valuation-role, multi-candidate acquisition-order, valuation-role-minimality, and accessibility-contraction audits.

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
```

The current phase is:

\[
\boxed{
\text{validated geometry}
\rightarrow
\text{navigation minimality}
\rightarrow
\text{valuation minimality}
\rightarrow
\text{accessibility contraction}
\rightarrow
\boxed{\text{experiment-space construction}}.
}
\]

The governing distinctions remain:

\[
\boxed{
\text{removed implementation}
\neq
\text{removed functional role}
}
\]

\[
\boxed{
\text{behavioral substitution}
\neq
\text{substrate reduction}
}
\]

and now:

\[
\boxed{
\text{accessibility contraction}
\neq
\text{experiment construction}.
}
\]

---

## 1. Empirical contraction history

### 1.1 Reachable refinement geometry

At `fadf503`, matched static evidence resources but different contingent refinement geometry produced different correction possibility.

The earned finite-deterministic distinction was:

\[
\boxed{
\text{eventual identifiability}
\neq
\text{future-sufficient identifiability}.
}
\]

The role-level dependency is that correction can require a contingent refinement path to remain reachable before the relevant commitment boundary.

### 1.2 Dynamic programming

At `68f2338`, finite Bellman dynamic programming was replaced by a reachability-preserving controller.

Across all 64 anonymous encodings and A/B/C geometries, the replacement matched DP on terminal accuracy, probe count, probe cost, and utility, with zero actions outside the DP-optimal action set over 3,584 visited decisions.

Therefore:

\[
\boxed{
\Pi_{\rm DP}\notin N_{P_{\rm ep}}
}
\]

for the observed navigation behavior.

The surviving role is:

\[
\boxed{
S_{\rm refine}
=
\text{preserve correction-relevant contingent refinement structure across steps}.
}
\]

### 1.3 Primitive STOP

At `4694382`, primitive `STOP` was removed from the epistemic action set.

Derived termination matched all 1,536 primitive STOP decisions with zero normalized trajectory mismatches.

The exhaustion-only control continued probing unnecessarily and reduced utility.

Therefore:

\[
\boxed{
STOP_{\rm primitive}\notin N_{P_{\rm ep}}
}
\]

while:

\[
\boxed{
T_{\rm stop}
=
\text{terminate when no warranted continuation remains}
}
\]

survives.

### 1.4 Separate cardinal `V,C`

At `c97a5cf`, the valuation-role audit established:

\[
\boxed{
I(e)\neq R_{\rm corr}(e)\neq Q_{\rm acquire}(e).
}
\]

The separate cardinal representation:

\[
(V,C)
\]

was replaced by:

\[
\kappa=C/V
\]

with:

```text
64 anonymous encodings
320 valuation decisions
0 baseline-vs-kappa mismatches
```

Therefore:

\[
\boxed{
(V,C)_{\rm separate}\notin N_{P_{\rm ep}}
}
\]

for the audited behavior.

This removed a representation scale, not the acquisition-burden role.

### 1.5 Candidate-vs-COMMIT is not enough

At `9a32f94`, multiple worthwhile refinements were simultaneously admissible.

The best possible deterministic choice accuracy from candidate-vs-COMMIT sign information was:

\[
\boxed{
\operatorname{Ceiling}(Q^\bot)=13/24.
}
\]

Thus:

\[
\boxed{
e\succ_Q COMMIT
\not\Rightarrow
e_i\succ_Q e_j.
}
\]

### 1.6 Pareto dominance is not enough

Adding uncompensated dominance in `(R_corr,-kappa)` produced only:

\[
\boxed{
\operatorname{Ceiling}(Q^\bot+\mathrm{Pareto})=17/24.
}
\]

The crossing tradeoff cases require compensated comparison.

### 1.7 Cardinal `q` vector

The explicit reference:

\[
q_i=R_i-\kappa_i
\]

was replaced by an on-demand compensated comparator:

\[
\boxed{
e_i\succ_Q e_j
\iff
R_i+\kappa_j>R_j+\kappa_i.
}
\]

It matched the cardinal reference on all 512 encoded states.

Therefore:

\[
\boxed{
q_{\rm cardinal}\notin N_{P_{\rm ep}}
}
\]

for the observed choices.

### 1.8 Stored full ranking

A max-only co-maximal tournament also matched:

\[
\boxed{512/512}
\]

without materializing a total candidate ordering.

Therefore:

\[
\boxed{
\text{stored full ranking}\notin N_{P_{\rm ep}}.
}
\]

The surviving acquisition role contracted to:

\[
\boxed{
Q_{\rm acquire}^{\rm role}
=
\text{identify a currently maximal worthwhile refinement}.
}
\]

### 1.9 Explicit `R_corr`

At `b7c068b`, the controller-side `R_corr` scalar was removed.

The replacement derived corrective consequence directly from the frozen evidence partition and correction contract, with:

\[
\boxed{512/512}
\]

multi-candidate choices preserved.

A contract-dependence mirror achieved:

```text
contract-aware choices: 128/128
contract-blind ceiling: 1/2
```

Therefore:

\[
\boxed{
R_{\rm corr}^{\rm explicit}
\text{ is implementation-contingent}
}
\]

while correction relevance remains grounded in the correction contract.

This is:

\[
\boxed{
B_{\rm controller}\downarrow
}
\]

but not:

\[
\boxed{
B_{\rm external}\downarrow,
}
\]

because the earlier implementation already derived `R_corr` rather than receiving a designer-supplied relevance table.

### 1.10 Acquisition burden

The burden ablation at `b7c068b` found:

\[
\boxed{
\operatorname{Ceiling}(-\kappa)=1/4
}
\]

\[
\boxed{
\operatorname{Ceiling}(\text{burden order only})=1/4
}
\]

and:

\[
\boxed{
\operatorname{Ceiling}(\text{relative burden differences without COMMIT anchor})=4/5.
}
\]

The anchored quantitative burden reference remained exact on:

\[
\boxed{320/320}.
\]

The earned role is therefore not “a scalar named `kappa` is uniquely necessary.” It is:

\[
\boxed{
\textbf{quantitative acquisition burden anchored to the COMMIT boundary}.
}
\]

### 1.11 Explicit probe menu

At `6355333`, the accessibility-contraction audit froze the latent probe universe:

\[
\boxed{
\mathcal E^\star
=
\{e_m:m\neq0000\},
\qquad
|\mathcal E^\star|=15
}
\]

and held all probe semantics, correction contracts, burdens, valuation, navigation, and stopping machinery fixed.

The explicit access reference used:

```text
B_access(A0) = 15
```

for 15 per-probe menu clauses.

The target-blind `ALL_REGISTRY` rule used:

```text
B_access(A1) = 1
```

and preserved:

```text
target reachability: 960/960
downstream choice:    960/960
```

with:

\[
\boxed{
B_{\mathcal E^\star}=\text{fixed}.
}
\]

Therefore:

\[
\boxed{
\text{explicit per-probe menu enumeration}
\notin N_{P_{\rm ep}}
}
\]

for complete accessibility in this fixed finite latent registry.

The surviving access role is narrower:

\[
\boxed{
A_{\rm registry}
=
\text{generic access to members of the already-defined latent registry}.
}
\]

Accessibility itself has **not** disappeared.

The no-access control produced:

\[
\boxed{0/960}
\]

despite every probe still existing latently.

The target-blind partial-access control produced exactly:

\[
\boxed{
448/960=7/15
}
\]

and never exceeded its coverage ceiling.

Thus:

\[
\boxed{
\text{latent existence}
\neq
\text{accessibility}.
}
\]

The context-to-target lookup achieved 960/960 but required 15 target-specific semantic hints and was classified as:

\[
\boxed{\text{oracle displacement}.}
\]

---

## 2. Current surviving role / supplied-substrate inventory

The experiment-planning branch should now be represented at the role level, not as the original implementation list.

A provisional current inventory is:

\[
\boxed{
P_{\rm ep}^{\rm surviving}
=
\{
S_{\rm refine},
T_{\rm stop},
Q_{\rm acquire}^{\rm role},
A_{\rm registry},
R_{\rm contract},
B_{\rm anchored},
\mathcal E^\star_{\rm supplied}
\}.
}
\]

These symbols are bookkeeping labels for surviving functional roles and supplied substrate, not newly asserted theoretical primitives.

Operationally:

- `S_refine`: preserve correction-relevant contingent refinement paths;
- `T_stop`: terminate when no continuation remains warranted;
- `Q_acquire^role`: identify a currently maximal worthwhile accessible refinement;
- `R_contract`: derive corrective consequence from evidence under the frozen correction contract;
- `B_anchored`: quantitative acquisition burden anchored to COMMIT;
- `A_registry`: generic access to the already-defined latent probe registry;
- `E*_supplied`: latent experiment membership and semantics remain externally specified.

Do **not** infer:

\[
P_{\rm ep,min}
=
P_{\rm ep}^{\rm surviving}.
\]

That remains unresolved.

---

## 3. Dependency table

| Component / representation | Tested implementation or language | Surviving role | Evidence status | Current boundary |
|---|---|---|---|---|
| `Pi_DP` | Bellman recursion | preserve contingent corrective structure | **removed** at `68f2338` | implementation contingent |
| `STOP_primitive` | explicit STOP action | warranted termination | **removed** at `4694382` | token contingent |
| separate `V,C` | cardinal value and cost scales | acquisition tradeoff | **removed** at `c97a5cf` | separate scale contingent |
| `Q^bot` | candidate-vs-COMMIT sign | single-candidate worth | **insufficient**; ceiling `13/24` | not a complete multi-candidate language |
| Pareto only | uncompensated relevance/burden dominance | remove dominated candidates | **insufficient**; ceiling `17/24` | compensated tradeoff survives |
| cardinal `q` vector | explicit `R-kappa` margins | choose maximal worthwhile candidate | **removed** at `9a32f94` | cardinal vector contingent |
| stored full ranking | total candidate ordering | identify maximal class | **removed** at `9a32f94` | persistent ranking contingent |
| explicit `R_corr` | derived scalar passed to controller | correction relevance | **removed** at `b7c068b` | contract-grounded consequence survives |
| contract-blind relevance | local evidence without correction contract | — | **insufficient**; ceiling `1/2` | contract remains constitutive |
| no burden | corrective consequence only | — | **insufficient**; ceiling `1/4` | burden role survives |
| burden order only | ordinal cheap/expensive relation | coarse burden | **insufficient**; ceiling `1/4` | quantitative magnitude needed |
| relative burden differences | probe-relative burden only | relative probe ordering | **insufficient**; ceiling `4/5` | COMMIT anchor needed |
| anchored quantitative burden | current `kappa` encoding | price acquisition relative to COMMIT | **role survives** | literal encoding not proven unique |
| explicit probe menu | 15 target-blind opaque menu entries | expose latent probes | **removed** at `6355333`; `B_access 15→1`, 960/960 preserved | enumeration contingent |
| no access | latent registry exists but no exposure path | — | **insufficient**; 0/960 | access path causally relevant |
| partial registry access | target-blind first 7 of 15 | partial exposure | **coverage-limited**; 448/960 = `7/15` | accessibility localized |
| target lookup | context→target probe semantic hints | expose target directly | 960/960 but **oracle displacement** | invalid minimality evidence |
| generic registry access | one `ALL_REGISTRY` rule | expose all already-defined latent probes | **role survives** | current access contraction endpoint |
| latent registry `E*` | 15 supplied parity probes and semantics | define what experiments exist | **supplied / untouched** | next frontier |

---

## 4. Current role-level compression

The current experiment-planning machinery can be summarized operationally as:

\[
\boxed{
\text{generic access to a supplied latent experiment registry}
\rightarrow
\text{contract-derived corrective consequence}
+
\text{COMMIT-anchored burden}
\rightarrow
\text{maximal worthwhile accessible refinement}
}
\]

embedded inside:

\[
\boxed{
S_{\rm refine}
+
T_{\rm stop}.
}
\]

The major removed implementation mass is:

\[
\boxed{
\begin{aligned}
\Pi_{\rm DP}&\downarrow\\
STOP_{\rm primitive}&\downarrow\\
(V,C)_{\rm separate}&\downarrow\\
R_{\rm corr}^{\rm explicit}&\downarrow\\
q_{\rm cardinal}&\downarrow\\
\text{full ranking}&\downarrow\\
\text{explicit 15-item access menu}&\downarrow.
\end{aligned}
}
\]

What has **not** disappeared is:

\[
\boxed{
\text{correction contract}
+
\text{anchored burden}
+
\text{access path}
+
\text{latent experiment specification}.
}
\]

---

## 5. Accessibility-specific specification accounting

The accessibility audit explicitly separates:

\[
\boxed{
B_{\rm total}
=
B_{\mathcal E^\star}
+
B_{\rm access}.
}
\]

The valid primary substitution changed only:

\[
\boxed{
B_{\rm access}:15\rightarrow1
}
\]

while:

\[
\boxed{
B_{\mathcal E^\star}=\text{constant}.
}
\]

The full access ledger was:

| Interface | menu | generator | grammar | semantic hints | search constraints | total |
|---|---:|---:|---:|---:|---:|---:|
| A0 explicit menu | 15 | 0 | 0 | 0 | 0 | 15 |
| A1 all registry | 0 | 1 | 0 | 0 | 0 | **1** |
| A2 no access | 0 | 0 | 0 | 0 | 0 | 0 |
| A3 first 7 | 0 | 1 | 0 | 0 | 1 | 2 |
| A4 target lookup | 0 | 1 | 0 | 15 | 0 | 16 |

Therefore the valid success is a genuine **access-interface contraction**:

\[
\boxed{
B_{\rm access}\downarrow
\land
R_{\rm functional}\text{ preserved}.
}
\]

But it is not yet a reduction of experiment ontology or probe semantics.

---

## 6. Representation / accessibility ceilings versus learner failure

The branch now contains multiple structural impossibility certificates:

\[
\boxed{
\operatorname{Ceiling}(Q^\bot)=13/24
}
\]

\[
\boxed{
\operatorname{Ceiling}(Q^\bot+\mathrm{Pareto})=17/24
}
\]

\[
\boxed{
\operatorname{Ceiling}(\text{contract-blind relevance})=1/2
}
\]

\[
\boxed{
\operatorname{Ceiling}(\text{no burden})
=
\operatorname{Ceiling}(\text{burden order})
=1/4
}
\]

\[
\boxed{
\operatorname{Ceiling}(\text{relative burden without COMMIT anchor})=4/5
}
\]

and now the exact accessibility-coverage certificate:

\[
\boxed{
\operatorname{Ceiling}(A3)=7/15.
}
\]

The accessibility failure is not a learner failure. In the missing A3 contexts:

\[
\boxed{
e^\star\in\mathcal E^\star
\land
Q_{\rm acquire}\text{ would select }e^\star
\land
e^\star\notin A.
}
\]

Thus:

\[
\boxed{
\text{epistemic / representational / accessibility impossibility}
\neq
\text{inference failure}.
}
\]

---

## 7. Provenance and regression status

Provenance remains layered rather than collapsed.

### Fresh accessibility evidence at `6355333`

```text
64 anonymous encodings
15 contexts per encoding
960 context-encoding evaluations

A0 explicit menu:
  reachability 960/960
  choice agreement 960/960
  B_access 15

A1 ALL_REGISTRY:
  reachability 960/960
  choice agreement 960/960
  B_access 1

A2 no access:
  reachability 0/960
  choice agreement 0/960

A3 first 7:
  reachability 448/960
  choice agreement 448/960
  exact coverage ceiling 7/15

A4 target lookup:
  choice agreement 960/960
  B_access 16
  oracle displacement
```

The latent semantic checksum was frozen across every access interface:

```text
54b7375f6ff283a3dff9f06bdaf67cced806411c9277021b0f9579c50cf45e59
```

### Inherited hard regression assertions

The committed child executable imports the valuation-role-minimality audit and recursively hard-asserts the earlier multi-candidate, candidate-vs-COMMIT, and STOP/navigation certificates.

Those older audits were not freshly process-reexecuted in the connector session used for `6355333`.

The correct provenance statement is:

\[
\boxed{
\textbf{fresh accessibility result with inherited hard regression assertions}.
}
\]

Do not describe `6355333` as a fresh end-to-end replay of all earlier audits.

---

## 8. Current empirical boundary

The empirical spine is now:

\[
\boxed{
\text{geometry}
\checkmark
\rightarrow
\text{navigation}
\checkmark
\rightarrow
\text{valuation}
\checkmark
\rightarrow
\text{accessibility contraction}
\checkmark
\rightarrow
\boxed{\text{experiment-space construction}}.
}
\]

The current accessibility result earns:

\[
\boxed{
\text{explicit access enumeration}
\rightarrow
\text{generic access to a fixed latent registry}.
}
\]

It does **not** earn:

\[
\boxed{
\mathcal E^\star
\rightarrow
\mathcal E^{\star\star}.
}
\]

It does not establish:

- experiment invention;
- probe-semantics generation;
- registry construction;
- experiment-ontology compression;
- basin opening;
- unrestricted experiment generation.

The remaining specification bottleneck is now concentrated in:

\[
\boxed{
B_{\mathcal E^\star}.
}
\]

The next scientific question, if pursued, is:

\[
\boxed{
\textbf{
Where does the latent experiment specification come from, and can that specification itself be reduced or constructed without relocating the experiment designer into a hidden grammar or oracle?
}
\]

That is an **experiment-space-construction** question, not another accessibility audit.

`P_ep,min` remains explicitly unresolved.
