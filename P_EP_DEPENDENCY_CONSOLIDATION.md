# Experiment-Planning Dependency Consolidation

## Status

This document consolidates the experiment-planning dependency picture after the reachable-refinement, controller-substitution, STOP-substitution, valuation-role, multi-candidate acquisition-order, and valuation-role-minimality audits.

It is a **dependency ledger**, not a new theory layer and not a `P_ep,min` certificate.

Relevant empirical reference points:

```text
fadf503  reachable-refinement discriminant audit
68f2338  refinement-controller substitution audit
4694382  STOP-substitution audit
c97a5cf  valuation-role discriminant audit
9a32f94  multi-candidate acquisition-order audit
b7c068b  valuation-role minimality audit
```

The current phase is now:

\[
\boxed{
\text{validated geometry}
\rightarrow
\text{navigation minimality}
\rightarrow
\text{valuation minimality}
\rightarrow
\boxed{\text{experiment accessibility}}
\rightarrow
\text{later experiment-space construction}.
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

and:

\[
\boxed{
\text{behavioral substitution}
\neq
\text{substrate reduction}.
}
\]

A representation that merely relocates target decisions, rankings, relevance labels, or affordability labels is **oracle displacement**, not minimality evidence.

---

## 1. What has actually been removed or ruled out

The original active-evidence implementation supplied, among other things:

\[
P_{\rm ep}
\supseteq
\{A_{\rm probe},C,V,\Pi_{\rm DP},STOP_{\rm primitive}\}.
\]

Successive interventions have removed implementation-specific machinery and localized the functional roles that survive.

### 1.1 Dynamic programming

At `68f2338`, finite Bellman dynamic programming was replaced by a reachability-preserving controller.

Across all 64 anonymous encodings and all A/B/C geometries, the replacement matched DP on terminal accuracy, probe cost, probe count and utility, with zero actions outside the DP-optimal set over 3,584 visited decision points.

Therefore, in the declared finite deterministic regime:

\[
\boxed{
\Pi_{\rm DP}\notin N_{P_{\rm ep}}
}
\]

for the observed navigation behavior.

The surviving role is sequential/compositional preservation of correction-relevant refinement structure.

### 1.2 Primitive `STOP`

At `4694382`, primitive `STOP` was removed from the epistemic action set.

Termination was derived as the absence of a justified continuation.

Across all 64 anonymous encodings:

```text
1,536 primitive STOP decisions
1,536 corresponding derived terminations
0 normalized trajectory mismatches
```

The exhaustion-only negative control continued probing unnecessarily, preserving accuracy but increasing cost.

Therefore:

\[
\boxed{
STOP_{\rm primitive}\notin N_{P_{\rm ep}}
}
\]

while:

\[
\boxed{
\text{termination token}
\neq
\text{termination discipline}.
}
\]

### 1.3 Separate cardinal `V,C`

At `c97a5cf`, the valuation-role audit separated:

\[
\boxed{
I(e)
\neq
R_{\rm corr}(e)
\neq
Q_{\rm acquire}(e).
}
\]

The baseline:

\[
M_{VC}(e)=V R_{\rm corr}(e)-C(e)
\]

was replaced by:

\[
\boxed{
\kappa(e)=C(e)/V
}
\]

with exact preservation across:

```text
64 anonymous encodings
320 valuation decisions
0 baseline-vs-kappa mismatches
```

Thus:

\[
\boxed{
(V,C)\text{ as separately represented cardinal scales}
\notin N_{P_{\rm ep}}
}
\]

for the audited behavior.

The negative controls simultaneously established:

\[
\boxed{
\text{raw information}
\neq
\text{correction relevance}
\neq
\text{acquisition worth}.
}
\]

### 1.4 Candidate-vs-COMMIT sign only

The `c97a5cf` result established only:

\[
\boxed{
e\succ_Q COMMIT\;?}
\]

At `9a32f94`, multiple worthwhile refinements were simultaneously admissible.

Under exhaustive anonymous candidate permutations:

\[
\boxed{
\operatorname{Ceiling}(Q^\bot)=13/24\approx0.5417.
}
\]

Therefore:

\[
\boxed{
\text{candidate-vs-COMMIT sufficiency}
\neq
\text{multi-candidate choice sufficiency}.
}
\]

This is a representation-language insufficiency result, not a learner failure.

### 1.5 Uncompensated Pareto dominance

Adding uncompensated dominance in `(R_corr,-kappa)` raises the best possible ceiling only to:

\[
\boxed{
\operatorname{Ceiling}(Q^\bot+Pareto)=17/24\approx0.7083.
}
\]

The crossing tradeoff states remain unresolved.

Thus:

\[
\boxed{
\text{uncompensated dominance is insufficient under relevance/burden tradeoffs}.
}
\]

### 1.6 Explicit cardinal `q` vector

The multi-candidate cardinal reference used:

\[
q_i=R_i-\kappa_i.
\]

A derived comparator used:

\[
\boxed{
e_i\succ_Q e_j
\iff
R_i+\kappa_j>R_j+\kappa_i
}
\]

without storing `q_i`.

It matched the cardinal reference:

\[
\boxed{512/512}.
\]

Therefore:

\[
\boxed{
\text{explicit cardinal }q\text{ vector}
\notin N_{P_{\rm ep}}.
}
\]

### 1.7 Stored full ordinal ranking

A max-only implementation retained only the current co-maximal class and discarded losing relations.

It also matched:

\[
\boxed{512/512}.
\]

Therefore:

\[
\boxed{
\text{stored full candidate ranking}
\notin N_{P_{\rm ep}}.
}
\]

The surviving acquisition role contracted to:

\[
\boxed{
\textbf{identify a currently maximal worthwhile refinement by on-demand compensated comparison.}
}
\]

### 1.8 Explicit controller-side `R_corr`

At `b7c068b`, the valuation-role-minimality audit removed the explicit `R_corr` scalar from the acquisition-controller interface.

The replacement receives only the already-frozen:

- evidence outcome partition;
- current posterior world set;
- correction contract;
- acquisition burden.

It derives post-evidence achievable correction directly from consequences and compares candidates without materializing `R_corr` or `q`.

On the frozen P1–P8 multi-candidate panel:

\[
\boxed{512/512}
\]

choices were preserved.

Therefore:

\[
\boxed{
R_{\rm corr}^{\rm explicit/controller}
\notin N_{P_{\rm ep}}
}
\]

for the observed acquisition choices.

But this is a **controller-interface / representation contraction**, not an external-specification reduction: the previous implementation already derived `R_corr` from evidence consequences rather than receiving a designer-supplied relevance table.

The surviving role is:

\[
\boxed{
\text{correction relevance derived from evidence consequences under the frozen correction contract}.
}
\]

### 1.9 Correction relevance remains contract-grounded

The same audit included a mirror control with identical local evidence partitions and burden pattern but a conditional correction contract:

\[
a^\star_c(W)=t_c.
\]

The warranted choice flips with the contract context.

The contract-aware consequence comparator achieved:

\[
\boxed{128/128}.
\]

A contract-blind local-evidence representation has an exact collision ceiling:

\[
\boxed{1/2}.
\]

Therefore:

\[
\boxed{
\text{local evidence structure alone}
\neq
\text{correction relevance}.
}
\]

The explicit `R_corr` scalar is contingent, but the correction contract is still doing genuine normative/decision-defining work.

### 1.10 Acquisition burden cannot be reduced to absence, order, or relative differences

The second independent cut at `b7c068b` held correction consequences fixed:

\[
R_H=.5,\quad R_M=.25,\quad R_L=.125
\]

while varying only acquisition burden.

Across K1–K4, the burden ordering was always:

\[
\kappa_H>\kappa_M>\kappa_L
\]

but the warranted next action rotated:

\[
\boxed{H\rightarrow M\rightarrow L\rightarrow COMMIT.}
\]

The exact representation ceilings were:

\[
\boxed{
\operatorname{Ceiling}(\text{no burden})=1/4
}
\]

and:

\[
\boxed{
\operatorname{Ceiling}(\text{burden order only})=1/4.
}
\]

A relevance-only natural control achieved only:

```text
64 / 320 exact choices = 0.20
```

and over-purchased correction-relevant evidence in K4/K5 where COMMIT was warranted.

Thus:

\[
\boxed{
\text{correction relevance alone}
\neq
\text{acquisition worth}.
}
\]

### 1.11 Relative burden still needs an absolute stopping anchor

K5 is a constant burden shift of K1.

K1 and K5 have identical pairwise burden differences, but require:

```text
K1 -> H
K5 -> COMMIT
```

A representation containing correction consequences plus pairwise burden differences but no absolute burden level therefore has ceiling:

\[
\boxed{4/5}.
\]

The full anchored burden representation remains exact:

\[
\boxed{320/320}.
\]

The strongest current dependency statement is not that the literal symbol `kappa` is uniquely necessary. It is:

\[
\boxed{
\textbf{some quantitative acquisition-burden information anchored to the COMMIT boundary remains necessary in the tested language family and frozen substrate.}
}
\]

---

## 2. Current surviving role inventory

The original flat implementation list has now contracted substantially.

A provisional role/supplied-ingredient inventory is:

\[
\boxed{
P_{\rm ep}^{\rm surviving}
=
\{
A_{\rm probe},
S_{\rm refine},
\text{contract-grounded correction consequence},
\text{anchored quantitative acquisition burden},
Q_{\rm acquire}^{\rm role},
T_{\rm stop}
\}.
}
\]

where:

\[
\boxed{
Q_{\rm acquire}^{\rm role}
=
\text{identify a currently maximal worthwhile refinement by on-demand compensated comparison}.
}
\]

This is **not** a minimal set.

It means only that:

- `A_probe` remains a supplied finite menu of accessible refinements;
- `S_refine` remains the sequential/compositional navigation role;
- explicit `R_corr` has been removed from the controller interface, but correction relevance remains derivable only relative to the frozen correction contract;
- acquisition burden remains quantitatively specified and must be anchored to the stopping boundary in the tested family;
- `Q_acquire^role` remains maximal-class selection by on-demand compensation;
- `T_stop` remains the discipline of terminating when no candidate is worth continuing with.

Do not infer:

\[
P_{\rm ep,min}=P_{\rm ep}^{\rm surviving}.
\]

---

## 3. Dependency table

| Component / representation | Tested implementation or language | Surviving functional role | Evidence status | Lowest-blast-radius unresolved question |
|---|---|---|---|---|
| `Pi_DP` | Bellman recursion | preserve correction-relevant contingent refinement structure | **implementation removed** at `68f2338` | none unless later task breaks role abstraction |
| `STOP_primitive` | first-class STOP action | terminate when continuation is unwarranted | **implementation removed** at `4694382` | do not reintroduce token |
| separate `V,C` | separate cardinal value/cost scales | compare corrective improvement with burden | **representation removed** at `c97a5cf` | none as separate scales |
| `Q^bot` | candidate-vs-COMMIT sign | decide whether one candidate is worthwhile | **insufficient for multi-candidate selection**; ceiling `13/24` | none as complete multi-candidate language |
| Pareto partial order | uncompensated `(relevance,-burden)` dominance | eliminate strictly dominated candidates | **insufficient**; ceiling `17/24` | none as complete comparison |
| cardinal `q` vector | explicit `R-kappa` margins | identify best worthwhile refinement | **representation removed** at `9a32f94` | none as stored vector |
| stored full ranking | total order over candidates | identify maximal class | **representation removed** at `9a32f94` | none as persistent ranking |
| explicit `R_corr` | derived scalar passed to controller | correction relevance | **controller representation removed** at `b7c068b`; consequence-derived comparator `512/512` | correction contract itself remains constitutive/frozen |
| contract-blind evidence relation | local evidence partitions without correction contract | none sufficient for relevance | **insufficient**; mirror ceiling `1/2` | none as relevance substitute |
| no burden | correction consequence only | none sufficient for acquisition worth | **insufficient**; ceiling `1/4` | none as burden substitute |
| burden order only | cheap/expensive ordering | coarse burden comparison | **insufficient**; ceiling `1/4` | none as complete burden language |
| pairwise burden differences only | relative cardinal burden, no absolute anchor | rank probes relative to each other | **insufficient for COMMIT boundary**; ceiling `4/5` | none as complete burden language |
| anchored quantitative burden | current `kappa` representation | price acquisition relative to COMMIT | **role survives**; literal encoding not proven unique | revisit only if a genuinely lower-level burden consequence exists without added scaffold |
| `Q_acquire^role` | on-demand compensated max-only choice | identify a currently maximal worthwhile refinement | **role survives** | currently stable enough to move to accessibility |
| `S_refine` | reachability-preserving controller logic | preserve contingent corrective paths | **role survives** | later cross-check under accessibility interventions |
| `T_stop` | absence of justified continuation | stop when no worthwhile refinement remains | **role survives** | later cross-check under accessibility interventions |
| `A_probe` | supplied finite probe menu and semantics | make candidate refinements accessible | **supplied / unresolved** | next frontier: reduce/generate accessibility without relocating experiment specification complexity |

---

## 4. Current valuation contraction

The valuation-side sequence is now:

\[
\boxed{
(V,C)
\rightarrow
\kappa
\rightarrow
Q^\bot
\rightarrow
\text{compensated pairwise comparison}
\rightarrow
\text{maximal-class identification}
\rightarrow
\text{contract-derived corrective consequence + anchored burden}.
}
\]

This is an empirical intervention history, not a stack of new theoretical primitives.

The current role-level statement is:

\[
\boxed{
\textbf{
identify the maximal worthwhile refinement by comparing contract-derived corrective consequence against quantitative acquisition burden anchored to COMMIT.
}
}
\]

The major contractions are now:

```text
DP                         removed as necessary implementation
primitive STOP             removed as necessary implementation
separate V,C               removed as necessary representation
candidate-vs-COMMIT only   ruled out as complete multi-candidate language
Pareto-only                ruled out under crossing tradeoffs
cardinal q vector          removed as necessary representation
stored full ranking        removed as necessary representation
explicit controller R_corr removed as necessary representation
```

What has **not** disappeared is the functional distinction between:

```text
what the correction contract makes consequential
what evidence changes the warranted correction
what acquisition burden makes worth paying
which currently accessible refinement is maximal
when continuation should terminate
```

---

## 5. Representation ceilings versus learner failure

The current valuation branch contains four independent impossibility-style certificates:

\[
\boxed{
\operatorname{Ceiling}(Q^\bot)=13/24
}
\]

\[
\boxed{
\operatorname{Ceiling}(Q^\bot+Pareto)=17/24
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

and:

\[
\boxed{
\operatorname{Ceiling}(\text{relative burden differences without COMMIT anchor})=4/5.
}
\]

These failures arise from representation collisions, not weak optimization.

The relevant methodological rule remains:

\[
\boxed{
\text{epistemic/representational impossibility}
\neq
\text{inference failure}.
}
\]

---

## 6. Specification-burden accounting

The anti-scaffold question remains:

\[
\boxed{
\textbf{Where did the complexity go?}
}
\]

### Explicit `R_corr` removal

The previous implementation already derived `R_corr` from evidence consequences, then exposed the scalar to the controller.

The `b7c068b` replacement computes the correction comparison directly from the frozen evidence partition and correction contract.

Therefore:

\[
\boxed{B_{\rm controller}\downarrow}
\]

but:

\[
\boxed{B_{\rm external}\not\downarrow}.
\]

This is a real controller-interface contraction but not an external-substrate reduction.

### Acquisition burden ablation

`kappa` is genuinely supplied per candidate in the current valuation panel.

Removing it would reduce external specification, but the no-burden representation fails at ceiling `1/4`.

Reducing it to ordinal burden also fails at `1/4`.

Retaining only relative burden differences improves the ceiling to `4/5` but loses the absolute COMMIT boundary.

Thus no successful external-specification reduction of acquisition burden has yet been demonstrated.

A future substitute counts only if:

\[
\boxed{
B_{\rm external}\downarrow
\land
R_{\rm functional}\text{ preserved}.
}
\]

Supplying winners, affordability labels, compensated answers, or rank tables remains oracle displacement.

---

## 7. Provenance and regression status

Provenance remains layered rather than collapsed.

### Fresh valuation-role-minimality evidence at `b7c068b`

Cut R:

```text
64 anonymous encodings
512 prior multi-candidate states
512/512 no-explicit-R_corr choices
128/128 contract-aware mirror choices
contract-blind mirror ceiling 1/2
```

Cut K:

```text
64 anonymous encodings
5 burden states
320/320 anchored-kappa reference choices
relevance-only natural control 64/320
no-burden ceiling 1/4
burden-order ceiling 1/4
relative-difference ceiling 4/5
```

### Inherited hard regression assertions

The older multi-candidate / valuation / STOP-navigation audits were not freshly process-reexecuted in the connector session used for `b7c068b`.

The committed executable imports the full upstream audit chain and hard-asserts:

```text
multi-candidate:
  512 encoded states
  max-only 512/512
  sign-only ceiling 13/24
  Pareto ceiling 17/24

candidate-vs-COMMIT:
  320 decisions
  baseline-vs-kappa mismatches 0

STOP/navigation:
  3584 visited decision points
  1536 derived terminations
  trace mismatches 0
```

The correct description is:

\[
\boxed{
\textbf{fresh valuation-role-minimality result with inherited hard regression assertions}.
}
\]

Do not describe `b7c068b` as a fresh end-to-end replay of all earlier audits.

---

## 8. Current evidence-status summary

\[
\boxed{
\begin{aligned}
\Pi_{\rm DP}&:\;\text{implementation contingent / removed},\\
STOP_{\rm primitive}&:\;\text{implementation contingent / removed},\\
(V,C)_{\rm separate}&:\;\text{representation contingent / removed},\\
Q^\bot&:\;\text{locally sufficient vs COMMIT, insufficient for multi-candidate choice},\\
Pareto&:\;\text{insufficient under relevance/burden tradeoffs},\\
q_{\rm cardinal}&:\;\text{representation contingent / removed},\\
\text{full ranking}&:\;\text{representation contingent / removed},\\
R_{\rm corr}^{\rm explicit}&:\;\text{controller representation contingent / removed},\\
\text{correction contract grounding}&:\;\text{functional dependency survives},\\
\text{burden absent / ordinal}&:\;\text{insufficient},\\
\text{relative burden only}&:\;\text{insufficient for COMMIT anchor},\\
\text{anchored quantitative burden}&:\;\text{functional dependency survives; encoding not uniquely identified},\\
Q_{\rm acquire}^{\rm role}&:\;\text{maximal-class identification survives},\\
S_{\rm refine}&:\;\text{functional role survives},\\
T_{\rm stop}&:\;\text{functional role survives},\\
A_{\rm probe}&:\;\text{supplied, necessity unresolved}.
\end{aligned}
}
\]

`P_ep,min` remains unresolved.

---

## 9. Research order

The dependency order can now advance one step:

\[
\boxed{
\text{geometry}
\rightarrow
\text{navigation}
\rightarrow
\text{valuation representation}
\rightarrow
\text{valuation role minimality}
\rightarrow
\boxed{\text{experiment accessibility}}
\rightarrow
\text{experiment-space construction}.
}
\]

Valuation minimality is not globally solved, but the current frozen substrate has reached a useful boundary:

- explicit relevance scalar removed;
- correction-contract grounding localized;
- burden-free, ordinal-burden, and relative-burden-only reductions ruled out;
- anchored quantitative burden remains live.

Further burden reduction would require a genuinely lower-level acquisition/resource consequence representation. Introducing such a representation now would change the probe/action substrate and therefore belongs with the accessibility-side question rather than another renamed valuation scalar.

The next frontier is therefore `A_probe`.

The anti-scaffold question becomes:

\[
\boxed{
\textbf{where did experiment specification complexity go?}
}
\]

Experiment-space construction / geometry repair remains later:

\[
\boxed{
\mathfrak R_{E,t}
\rightarrow
\mathfrak R_{E,t+1}.
}
\]

No basin-opening claim follows from this consolidation.

---

## 10. Current open question

The next narrow dependency question is now:

\[
\boxed{
\textbf{Can }A_{\rm probe}\textbf{ be reduced, derived, or generated while preserving the already-earned correction behavior without relocating experiment-specification complexity?}
}
\]

This question is **not yet an implemented audit**.

The current freeze point is:

\[
\boxed{
\text{contract-derived corrective consequence}
+
\text{anchored quantitative acquisition burden}
+
\text{maximal-class choice}
}
\]

inside the already-frozen navigation and termination roles.

No experiment-accessibility intervention, experiment-space-construction claim, or next capability rung is introduced by this consolidation.
