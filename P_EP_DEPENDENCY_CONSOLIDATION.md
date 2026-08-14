# Experiment-Planning Dependency Consolidation

## Status

This document consolidates the experiment-planning dependency picture after the reachable-refinement, controller-substitution, and STOP-substitution audits.

It is a **dependency ledger**, not a new theory layer and not a `P_ep,min` certificate.

The relevant empirical reference points are:

```text
fadf503  reachable-refinement discriminant audit
68f2338  refinement-controller substitution audit
4694382  STOP-substitution audit
```

The current phase remains:

\[
\boxed{
\text{validated geometry}
\rightarrow
\text{navigation minimality}
\rightarrow
\text{later geometry repair}.
}
\]

The immediate purpose of this ledger is to distinguish:

\[
\boxed{
\text{removed implementation}
\neq
\text{removed functional role}.
}
\]

---

## 1. What has actually been removed

The original active-evidence implementation supplied, among other things:

\[
P_{\rm ep}
\supseteq
\{A_{\rm probe},C,V,\Pi_{\rm DP},STOP_{\rm primitive}\}.
\]

Two implementation-specific pieces have now survived direct substitution tests.

### Dynamic programming

At `68f2338`, finite Bellman dynamic programming was replaced by a controller that preserves correction-relevant contingent refinement structure and otherwise uses the frozen local value/cost fallback.

Across all 64 anonymous encodings and all A/B/C geometries, the replacement matched DP on terminal accuracy, probe cost, probe count and utility, with zero actions outside the DP-optimal set over 3,584 visited decision points.

Therefore, in the declared finite deterministic regime:

\[
\boxed{
\Pi_{\rm DP}\notin N_{P_{\rm ep}}
}
\]

for the observed navigation behavior.

This does **not** remove the sequential/compositional role.

The myopic control still fails in the complementary-refinement case.

### Primitive `STOP`

At `4694382`, primitive `STOP` was removed from the epistemic action set.

Termination was instead derived from the frozen refinement and value/cost contract as the absence of a justified continuation.

Across all 64 anonymous encodings:

```text
1,536 primitive STOP decisions
1,536 corresponding derived terminations
0 normalized trajectory mismatches
```

The exhaustion-only negative control continued probing unnecessarily in B/C, increasing mean probe count from 1 to 2 while leaving accuracy at 0.75 and reducing utility from 6.5 to 5.5.

Therefore, in the declared finite deterministic regime:

\[
\boxed{
STOP_{\rm primitive}\notin N_{P_{\rm ep}}
}
\]

for the observed navigation behavior.

But the negative control preserves the opposite conclusion about the functional role:

\[
\boxed{
\text{termination token}
\neq
\text{termination discipline}.
}
\]

---

## 2. Current surviving role inventory

The experiment-planning substrate should no longer be represented as the original flat implementation list.

A provisional role-level representation is:

\[
\boxed{
P_{\rm ep}^{\rm surviving}
=
\{A_{\rm probe},C,V,S_{\rm refine},T_{\rm stop}\}.
}
\]

This is **not** a minimal set.

It means only that:

- `A_probe`, `C`, and `V` are still supplied and have not yet been removed;
- the specific DP implementation has been removed while a sequential/compositional refinement role survives;
- the primitive `STOP` token has been removed while termination discipline survives.

Do not infer:

\[
P_{\rm ep,min}=P_{\rm ep}^{\rm surviving}.
\]

That remains open.

---

## 3. Dependency table

| Component | Supplied implementation | Surviving functional role | Evidence status | Lowest-blast-radius next intervention |
|---|---|---|---|---|
| `Pi_DP` | finite Bellman recursion over remaining probes | preserve correction-relevant contingent refinement structure across steps | **implementation removed** at `68f2338`; myopic negative control shows sequential/compositional dependence remains | none; do not re-litigate DP unless a later task breaks the role-level abstraction |
| `STOP_primitive` | explicit first-class epistemic action | terminate when no refinement continuation is warranted by the frozen contract | **implementation removed** at `4694382`; exhaustion-only negative control shows termination discipline remains | none; attack the valuation basis of the derived boundary rather than reintroducing a STOP token |
| `S_refine` | reachability-preserving controller logic | retain refinement branches that can still change warranted correction before commitment | **role survives**, but global necessity/minimal implementation is not established | after valuation is clarified, weaken or partially remove sequential reachability information under matched geometry |
| `T_stop` | derived comparison between immediate commitment and remaining acquisition value | stop when continuation is no longer warranted | **role survives**; token is contingent, discipline is not yet removed | attack the valuation structure from which the termination boundary is derived |
| `V` | scalar terminal correctness value (`V=10` in the current audit) | currently bundles correction relevance, decision usefulness and continuation comparison | **supplied / unresolved**; current audits use it but do not establish the scalar representation as necessary | decompose the valuation interface and test whether absolute scalar value can be replaced while preserving the relevant ordering/decision boundary |
| `C` | explicit scalar probe cost (`C=1`) | penalize acquisition and distinguish useful evidence from evidence worth acquiring | **supplied / unresolved**; STOP negative control shows acquisition burden matters, not that this scalar representation is uniquely necessary | separate cost representation from acquisition-worth ordering under matched evidence and correction relevance |
| `A_probe` | finite supplied probe menu with fixed admissibility/semantics | make candidate refinements accessible for selection | **supplied / unresolved**; reachable-refinement audits validate geometry conditional on this menu | defer until valuation is minimized; later remove or generate probe accessibility while auditing where experiment specification burden moves |

---

## 4. The valuation interface is now the lowest-blast-radius target

The current `(V,C)` pair should not be treated as two automatically primitive scalars.

Existing evidence already separates three ideas:

\[
\boxed{
\text{information gain}
\neq
\text{correction relevance}
\neq
\text{acquisition worth}.
}
\]

The first separation is supported by the Active Evidence Acquisition Audit: probes can carry equal raw outcome entropy while differing in decision value.

The second separation is sharpened by the STOP audit: an available refinement can remain physically executable while no longer being worth acquiring under the frozen value/cost contract.

A useful provisional decomposition is therefore:

```text
what matters for correction
        ->
what evidence would improve that correction
        ->
what improvement is worth its acquisition burden
```

This is a **decomposition target**, not a newly frozen ontology.

The current scalar implementation may be carrying several roles at once.

---

## 5. What the next valuation audit must not do

The next intervention should attack valuation scaffolding without changing:

\[
\boxed{
\mathfrak R_E,
\Pi_{\mathcal P},
A_{\rm probe},
\tau,
S_{\rm refine}.
}
\]

It should not change the probe menu, generate new experiments, repair the geometry, or add a stronger planner.

The causal question is narrower:

> **What minimum valuation structure is required to distinguish correction-relevant refinement from refinement worth acquiring?**

The first cut should target implementation rather than meaning.

In particular, the audit should test whether the current absolute scalar parameterization of `V` and `C` can be replaced by a weaker representation of the ordering / threshold that governs continuation, while preserving the same correction contract and refinement geometry.

If successful, the earned result would concern the scalar parameterization only.

It would **not** establish that valuation or acquisition cost is unnecessary.

The specification-accounting rule remains:

\[
\boxed{
\text{removed from view}
\neq
\text{removed from substrate}.
}
\]

A replacement that merely hides the same `V/C` decision boundary in a hand-coded oracle is not a substrate reduction.

---

## 6. Current evidence-status summary

The current navigation picture is:

\[
\boxed{
\begin{aligned}
\Pi_{\rm DP}&:\;\text{implementation contingent},\\
STOP_{\rm primitive}&:\;\text{implementation contingent},\\
S_{\rm refine}&:\;\text{functional role survives},\\
T_{\rm stop}&:\;\text{functional role survives},\\
V&:\;\text{supplied, necessity unresolved},\\
C&:\;\text{supplied, necessity unresolved},\\
A_{\rm probe}&:\;\text{supplied, necessity unresolved}.
\end{aligned}
}
\]

The correct interpretation is:

\[
\boxed{
\text{successful implementation}
\rightarrow
\text{substitution}
\rightarrow
\text{retain only the role that survives}.
}
\]

Not:

\[
\text{successful implementation}
\rightarrow
\text{declare every supplied component necessary}.
\]

---

## 7. Research order

The current dependency order is deliberately conservative:

\[
\boxed{
\text{controller scaffolding}
\rightarrow
\text{valuation scaffolding}
\rightarrow
\text{experiment accessibility}
\rightarrow
\text{experiment-space construction}.
}
\]

The first stage has now removed DP and primitive `STOP` as necessary implementations for the audited behavior.

The next stage is valuation.

Only after the valuation interface is decomposed should the program attack `A_probe`, because removing a supplied probe menu introduces the stronger specification-accounting question:

\[
\boxed{
\text{where did experiment specification complexity go?}
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

No basin-opening claim is made by this consolidation.

---

## 8. Current open question

The next narrow dependency question is:

\[
\boxed{
\textbf{What is the minimal valuation interface needed to preserve decision-directed acquisition and warranted termination over the already-frozen refinement geometry?}
}
\]

`P_ep,min` remains explicitly unresolved.

No next capability rung is introduced.
