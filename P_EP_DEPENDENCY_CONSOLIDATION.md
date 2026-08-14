# Experiment-Planning Dependency Consolidation

## Status

This document consolidates the experiment-planning dependency picture after the reachable-refinement, controller-substitution, STOP-substitution, valuation-role, and multi-candidate acquisition-order audits.

It is a **dependency ledger**, not a new theory layer and not a `P_ep,min` certificate.

The relevant empirical reference points are:

```text
fadf503  reachable-refinement discriminant audit
68f2338  refinement-controller substitution audit
4694382  STOP-substitution audit
c97a5cf  valuation-role discriminant audit
9a32f94  multi-candidate acquisition-order audit
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
\text{later experiment accessibility}.
}
\]

The immediate purpose of this ledger remains:

\[
\boxed{
\text{removed implementation}
\neq
\text{removed functional role}.
}
\]

The valuation audits add a second distinction that is now equally important:

\[
\boxed{
\text{behavioral substitution}
\neq
\text{substrate reduction}.
}
\]

A representation may preserve behavior while merely relocating specification burden. Direct rank or winner tables are therefore treated as **oracle displacement**, not as evidence of minimal substrate.

---

## 1. What has actually been removed or ruled out

The original active-evidence implementation supplied, among other things:

\[
P_{\rm ep}
\supseteq
\{A_{\rm probe},C,V,\Pi_{\rm DP},STOP_{\rm primitive}\}.
\]

Successive interventions have now removed several implementation-specific pieces and ruled out several weaker comparison languages.

### 1.1 Dynamic programming

At `68f2338`, finite Bellman dynamic programming was replaced by a controller that preserves correction-relevant contingent refinement structure and otherwise uses the frozen local acquisition comparison.

Across all 64 anonymous encodings and all A/B/C geometries, the replacement matched DP on terminal accuracy, probe cost, probe count and utility, with zero actions outside the DP-optimal set over 3,584 visited decision points.

Therefore, in the declared finite deterministic regime:

\[
\boxed{
\Pi_{\rm DP}\notin N_{P_{\rm ep}}
}
\]

for the observed navigation behavior.

The surviving role is not dynamic programming itself. It is the preservation of correction-relevant contingent refinement structure across steps.

### 1.2 Primitive `STOP`

At `4694382`, primitive `STOP` was removed from the epistemic action set.

Termination was derived instead as the absence of a justified continuation under the frozen refinement and acquisition contract.

Across all 64 anonymous encodings:

```text
1,536 primitive STOP decisions
1,536 corresponding derived terminations
0 normalized trajectory mismatches
```

The exhaustion-only negative control continued probing unnecessarily in B/C, increasing mean probe count from 1 to 2 while leaving accuracy at 0.75 and reducing utility from 6.5 to 5.5.

Therefore:

\[
\boxed{
STOP_{\rm primitive}\notin N_{P_{\rm ep}}
}
\]

for the observed behavior, while:

\[
\boxed{
\text{termination token}
\neq
\text{termination discipline}.
}
\]

### 1.3 Separate cardinal `V,C` representation

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

The baseline representation:

\[
M_{VC}(e)=V R_{\rm corr}(e)-C(e)
\]

was replaced by the normalized burden representation:

\[
\boxed{
\kappa(e)=\frac{C(e)}{V}
}
\]

with the decision rule:

\[
R_{\rm corr}(e)>\kappa(e).
\]

Across 64 anonymous encodings and 320 valuation decisions:

```text
baseline vs kappa mismatches: 0
```

Therefore, for the audited behavior:

\[
\boxed{
(V,C)\text{ as separately represented cardinal scales}
\notin N_{P_{\rm ep}}.
}
\]

This is a **representation contraction**, not evidence that valuation or acquisition burden disappeared.

The negative controls establish the surviving functional separation:

\[
\boxed{
I\text{-only}
\Rightarrow
\text{purchases correction-irrelevant information}
}
\]

and:

\[
\boxed{
R_{\rm corr}\text{-only}
\Rightarrow
\text{purchases correction-relevant evidence that is not worth its burden}.
}
\]

### 1.4 Candidate-vs-COMMIT threshold alone

The result at `c97a5cf` established only:

\[
\boxed{
e\succ_Q COMMIT\;?}
\]

for one candidate at a time.

At `9a32f94`, multiple worthwhile refinements were simultaneously admissible. Under anonymous candidate permutations, the best possible deterministic single-action accuracy from candidate-vs-COMMIT sign information was:

\[
\boxed{
\operatorname{Ceiling}(Q^\bot)=\frac{13}{24}\approx0.5417.
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

This is not an implementation removal in the same sense as DP or primitive `STOP`; it is an **insufficiency result for a weaker comparison language**.

### 1.5 Uncompensated Pareto dominance

Adding the partial order:

\[
e_i\succ_P e_j
\iff
R_i\ge R_j
\land
\kappa_i\le\kappa_j
\]

with at least one strict inequality raises the permutation-derived ceiling only to:

\[
\boxed{
\operatorname{Ceiling}(Q^\bot+Pareto)=\frac{17}{24}\approx0.7083.
}
\]

The crossing tradeoff states remain unresolved because correction relevance and acquisition burden move in opposite directions.

Thus:

\[
\boxed{
\text{uncompensated dominance is insufficient for the audited multi-candidate policy}.
}
\]

Again, this is an insufficiency result, not a claim that Pareto structure is useless in every regime.

### 1.6 Explicit cardinal `q` vector

The cardinal multi-candidate reference at `9a32f94` used:

\[
q_i=R_i-\kappa_i.
\]

A derived pairwise comparator instead used:

\[
\boxed{
e_i\succ_Q e_j
\iff
R_i+\kappa_j>R_j+\kappa_i
}
\]

without storing numeric `q_i` values.

Across 64 anonymous encodings and 512 encoded state evaluations, the derived comparator matched the cardinal reference exactly:

\[
\boxed{512/512}.
\]

Therefore:

\[
\boxed{
\text{explicit cardinal }q\text{ vector}
\notin N_{P_{\rm ep}}
}
\]

for the observed multi-candidate choice behavior.

### 1.7 Stored full ordinal ranking

A stronger substitution at `9a32f94` retained only the current **co-maximal candidate class** during sequential pairwise comparison. Losing relations were discarded; no total ranking was materialized.

This max-only implementation also matched the complete optimal-action correspondence:

\[
\boxed{512/512}.
\]

Therefore, for this panel:

\[
\boxed{
\text{stored full candidate ranking}
\notin N_{P_{\rm ep}}.
}
\]

The surviving role is narrower:

\[
\boxed{
\textbf{identify a currently maximal worthwhile refinement by on-demand compensated comparison.}
}
\]

---

## 2. Current surviving role inventory

The experiment-planning substrate should no longer be represented as the original flat implementation list.

The current provisional role/supplied-ingredient inventory is:

\[
\boxed{
P_{\rm ep}^{\rm surviving}
=
\{
A_{\rm probe},
S_{\rm refine},
R_{\rm corr},
\kappa,
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
- `S_refine` remains the surviving sequential/compositional navigation role;
- `R_corr` remains explicitly represented from correction consequences;
- `kappa` remains an explicitly supplied normalized acquisition-burden representation;
- the acquisition role has contracted from cardinal valuation / full ranking to on-demand maximal-class identification;
- `T_stop` remains the discipline of terminating when no candidate is worth continuing with.

Do not infer:

\[
P_{\rm ep,min}=P_{\rm ep}^{\rm surviving}.
\]

That remains open.

---

## 3. Dependency table

| Component / representation | Supplied implementation or tested language | Surviving functional role | Evidence status | Lowest-blast-radius unresolved question |
|---|---|---|---|---|
| `Pi_DP` | finite Bellman recursion over remaining probes | preserve correction-relevant contingent refinement structure across steps | **implementation removed** at `68f2338` | none unless a later task breaks the role-level abstraction |
| `STOP_primitive` | explicit first-class epistemic action | terminate when no refinement continuation is warranted | **implementation removed** at `4694382` | do not reintroduce token; test only the dependencies supporting termination discipline |
| separate `V,C` | global correctness scale plus absolute acquisition costs | compare corrective improvement with acquisition burden | **representation removed** at `c97a5cf`; `kappa=C/V` preserved 320/320 decisions | whether even explicit normalized burden can be weakened or derived |
| `Q^bot` | candidate-vs-COMMIT sign only | decide whether one candidate is worth acquiring | **sufficient locally, insufficient for multi-candidate selection**; ceiling `13/24` at `9a32f94` | none as a complete multi-candidate representation |
| Pareto partial order | uncompensated dominance in `(R_corr,-kappa)` | eliminate candidates that are strictly worse on both dimensions | **insufficient under crossing tradeoffs**; ceiling `17/24` at `9a32f94` | none as the complete acquisition comparison |
| cardinal `q` vector | explicit `q_i=R_i-kappa_i` for all candidates | identify best worthwhile refinement | **representation removed** at `9a32f94`; derived ordinal comparator matched 512/512 | whether compensated comparison itself can be weakened |
| stored full ordinal ranking | materialized order over all candidates | identify maximal worthwhile candidate/class | **representation removed** at `9a32f94`; max-only co-maximal tournament matched 512/512 | whether even co-maximal pairwise comparison can be represented more minimally |
| `Q_acquire^role` | on-demand compensated pairwise comparison, retaining only current co-maximal class | identify a currently maximal worthwhile refinement | **role survives**; stronger minimality unresolved | can the compensated relation be weakened without oracle displacement? |
| `R_corr` | explicit evaluator/controller-side correction-relevance quantity derived from correction consequences | represent how much a candidate can improve warranted correction | **supplied / unresolved** | can maximal-choice behavior be preserved without explicitly representing cardinal `R_corr`? |
| `kappa` | normalized acquisition burden `C/V` | represent acquisition burden on the same comparison scale | **supplied / unresolved** | can maximal-choice behavior be preserved without explicitly supplying `kappa`? |
| `S_refine` | reachability-preserving controller logic | retain refinement branches that can still change warranted correction before commitment | **role survives** | revisit only after valuation ingredients are better localized |
| `T_stop` | absence of any justified continuation | terminate when no worthwhile refinement remains | **role survives** | determine which reduced valuation ingredients are actually necessary for the boundary |
| `A_probe` | finite supplied probe menu with fixed admissibility/semantics | make candidate refinements accessible for selection | **supplied / unresolved** | defer until valuation minimality is stabilized; then ask where experiment specification burden goes |

---

## 4. Current valuation contraction

The valuation-side empirical sequence is now:

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
\text{maximal-class identification}.
}
\]

This sequence should not be read as five equally fundamental theoretical objects.

It records successive interventions:

1. `V,C` as separate cardinal scales were unnecessary for the observed candidate-vs-COMMIT behavior;
2. candidate-vs-COMMIT sign information was insufficient when several worthwhile refinements competed;
3. uncompensated Pareto structure remained insufficient under crossing relevance/burden tradeoffs;
4. compensated pairwise comparison recovered the complete choice correspondence without storing cardinal `q`;
5. a max-only co-maximal tournament recovered the same choices without storing a full ranking.

The current surviving valuation role is therefore not a generic scalar “utility function.” It is:

\[
\boxed{
\textbf{choice-maximality under a compensated correction-relevance / acquisition-burden comparison.}
}
\]

This is a role-level statement inside the audited finite deterministic regime.

---

## 5. Representation ceilings versus learner failure

The multi-candidate audit strengthens the minimality program because the weak-language failures are not merely observed controller errors.

Under exhaustive anonymous candidate permutations:

\[
\boxed{
\operatorname{Ceiling}(Q^\bot)=13/24
}
\]

and:

\[
\boxed{
\operatorname{Ceiling}(Q^\bot+Pareto)=17/24.
}
\]

These ceilings arise from representation collisions: distinct target choices map to the same impoverished representation.

Therefore:

\[
\boxed{
\text{epistemically/representationally insufficient comparison language}
\neq
\text{poor learner or optimizer}.
}
\]

The successful compensated ordinal and max-only substitutions both reach exact agreement with the cardinal reference over all 512 encoded state evaluations.

The resulting boundary is:

\[
\boxed{
\text{threshold information}
<
\text{uncompensated partial dominance}
<
\text{compensated choice relation}
}
\]

for the declared task family.

---

## 6. Specification-burden accounting

The anti-scaffold rule remains mandatory:

\[
\boxed{
\textbf{Where did the complexity go?}
}
\]

The valuation audits distinguish genuine representation contraction from answer relocation.

### Candidate-vs-COMMIT audit

The finite supplied-field ledger contracts:

```text
baseline V,C:  one global value scalar + per-case absolute costs
kappa:         no separate global V + per-case normalized thresholds
order table:   direct target decisions -> oracle displacement
```

### Multi-candidate audit

The successful max-only controller supplies no winner table and no rank table. It derives comparisons online from `R_corr` and `kappa`, stores no cardinal `q` vector, and retains only the current co-maximal class.

Therefore the audit supports a **representation contraction**:

\[
\boxed{
\text{cardinal vector / full ranking}
\downarrow
}
\]

while preserving:

\[
\boxed{
\text{maximal-choice behavior}.
}
\]

But external valuation information has not disappeared:

\[
\boxed{
R_{\rm corr}
\text{ and }
\kappa
\text{ remain supplied}. 
}
\]

A future representation that directly stores winners, pairwise answers, or per-state rankings would therefore count as oracle displacement unless independent specification accounting shows a genuine reduction.

---

## 7. Provenance and regression status

The provenance status must remain explicit.

The `c97a5cf` valuation-role audit was executed on its new valuation panel with:

```text
64 anonymous encodings
320 candidate-vs-COMMIT decisions
0 baseline-vs-kappa mismatches
```

The `9a32f94` multi-candidate audit was freshly executed on its new panel with:

```text
64 anonymous encodings
8 panel states
512 encoded state evaluations
512/512 compensated-ordinal matches
512/512 max-only matches
512/512 cardinal-reference matches
```

The older valuation / STOP / navigation regressions were **not freshly process-reexecuted in the connector environment during the `9a32f94` run**.

Instead:

- the relevant upstream source blobs were verified unchanged;
- the new executable imports the prior valuation audit;
- that audit imports the STOP audit;
- hard assertions re-check the frozen upstream certificates whenever the child audit is executed in-repo.

Therefore the correct description is:

\[
\boxed{
\textbf{fresh multi-candidate result with inherited hard regression assertions}. 
}
\]

Do not describe `9a32f94` as a fresh end-to-end replay of all earlier audits.

---

## 8. Current evidence-status summary

The current experiment-planning picture is:

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
Q_{\rm acquire}^{\rm role}&:\;\text{maximal-class identification by compensated comparison survives},\\
R_{\rm corr}&:\;\text{supplied, necessity unresolved},\\
\kappa&:\;\text{supplied, necessity unresolved},\\
S_{\rm refine}&:\;\text{functional role survives},\\
T_{\rm stop}&:\;\text{functional role survives},\\
A_{\rm probe}&:\;\text{supplied, necessity unresolved}.
\end{aligned}
}
\]

The governing interpretation remains:

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

## 9. Research order

The dependency order remains deliberately conservative:

\[
\boxed{
\text{geometry}
\rightarrow
\text{navigation}
\rightarrow
\text{valuation representation}
\rightarrow
\text{valuation ingredient minimality}
\rightarrow
\text{experiment accessibility}
\rightarrow
\text{experiment-space construction}.
}
\]

The first three stages have now established:

- reachable refinement geometry matters under matched static resources;
- DP and primitive `STOP` are not necessary implementations for the audited navigation behavior;
- separate `V,C`, explicit cardinal `q`, and stored full rankings are not necessary valuation representations;
- candidate-vs-COMMIT sign and uncompensated Pareto structure are too weak for the audited multi-candidate problem;
- on-demand compensated maximal-class identification preserves the observed acquisition choices.

The program should **not** attack `A_probe` yet.

Removing a supplied probe menu introduces the stronger specification-accounting question:

\[
\boxed{
\textbf{where did experiment specification complexity go?}
}
\]

Experiment accessibility therefore remains downstream of the still-unresolved valuation ingredients.

Experiment-space construction / geometry repair remains later:

\[
\boxed{
\mathfrak R_{E,t}
\rightarrow
\mathfrak R_{E,t+1}.
}
\]

No basin-opening claim follows from the current consolidation.

---

## 10. Current open question

The next narrow dependency question is now:

\[
\boxed{
\textbf{Can the explicit }R_{\rm corr}\textbf{ and }\kappa\textbf{ representations be weakened or removed while preserving maximal-choice behavior without oracle displacement?}
}
\]

This question is **not yet an implemented audit**.

The current freeze point is:

\[
\boxed{
Q_{\rm acquire}^{\rm role}
=
\text{identify a currently maximal worthwhile refinement by on-demand compensated comparison}
}
\]

with:

\[
\boxed{
R_{\rm corr},\;\kappa
\text{ still supplied and necessity-unresolved}. 
}
\]

`P_ep,min` remains explicitly unresolved.

No experiment-accessibility intervention, experiment-space construction claim, or next capability rung is introduced by this consolidation.
