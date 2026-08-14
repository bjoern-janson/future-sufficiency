# Multi-Candidate Acquisition-Order Discriminant Audit — Preregistration

## Status

This document freezes the next `Q_acquire` minimality audit **before execution**.

Current repository parent at preregistration time:

```text
27e5520  Add three correction pressure cases note
```

Empirical valuation anchor:

```text
c97a5cf  Add valuation-role discriminant audit
```

No empirical results are recorded here.

The previous audit established only a candidate-vs-commit comparison:

\[
\boxed{
Q_{\rm acquire}^{\bot}(e)
:\;
e\succ COMMIT\;?
}
\]

It did **not** establish the minimum structure required when several worthwhile refinements are simultaneously admissible.

The present audit asks:

\[
\boxed{
\textbf{What is the weakest non-oracular comparison structure sufficient to choose which worthwhile refinement should come next?}
}
\]

This is a valuation-order audit, not an experiment-accessibility audit and not an experiment-space-construction audit.

---

## 1. Frozen empirical boundary

Hold fixed across all compared acquisition controllers:

\[
\boxed{
\mathfrak R_E,\;S_{\rm refine},\;T_{\rm stop},\;\Pi_{\mathcal P},\;\tau.
}
\]

Operationally:

- the world set is fixed;
- the candidate evidence partitions are fixed;
- all candidates are simultaneously admissible;
- the correction contract is fixed;
- the normalized burden representation `kappa` earned at `c97a5cf` is fixed;
- candidate identities and evidence-output tokens are anonymous/permuted;
- only the **comparison structure used to select among candidates** changes.

The valuation panel itself allows one evidence acquisition before commitment. This isolates multi-candidate ordering from sequential planning. The already-earned `S_refine` and `T_stop` roles are protected by regression against the prior controller/STOP audits rather than redefined here.

No new probe generation, geometry repair, authorization change, or stronger planning horizon is permitted.

---

## 2. Existing result being extended

The preceding valuation audit established:

\[
\boxed{
I(e)\neq R_{\rm corr}(e)\neq Q_{\rm acquire}(e)
}
\]

and showed that the separate cardinal representation `(V,C)` could be replaced by:

\[
\boxed{
\kappa(e)=C(e)/V
}
\]

with exact candidate-vs-commit behavior preserved.

Under the scale-free representation, define the evaluator-side acquisition margin:

\[
q(e)=R_{\rm corr}(e)-\kappa(e).
\]

The previous audit needed only:

\[
q(e)>0\;?
\]

The present audit requires simultaneous comparison among:

\[
\boxed{
\{e_1,e_2,e_3,COMMIT\}.
}
\]

The cardinal `q` value is the reference implementation only. Its necessity is precisely what is under test.

---

## 3. Finite world and correction contract

Use a uniform finite world:

\[
W=(t,g_1,g_2,g_3,n)\in\{0,1\}^5.
\]

The warranted terminal correction is:

\[
a^\star(W)=t.
\]

Before evidence acquisition:

\[
\operatorname{BayesAcc}(a^\star)=0.5.
\]

Define three balanced one-bit evidence families with different correction relevance but identical raw world information.

### High-relevance probe `H`

\[
E_H=t.
\]

Therefore:

\[
I(W;E_H)=1\text{ bit},
\qquad
R_{\rm corr}(H)=0.5.
\]

### Medium-relevance probe `M`

Let `g=(g_1,g_2,g_3)` be uniform over eight states and define a deterministic noise indicator that is one on exactly two of those eight states. Then:

\[
E_M=t\oplus z_{2/8}.
\]

The observation is correct about `t` with probability `3/4`, while remaining balanced. Hence:

\[
I(W;E_M)=1\text{ bit},
\qquad
R_{\rm corr}(M)=0.25.
\]

### Low-relevance probe `L`

Define a deterministic noise indicator that is one on exactly three of the eight gate states:

\[
E_L=t\oplus z_{3/8}.
\]

The observation is correct about `t` with probability `5/8`, while remaining balanced. Hence:

\[
I(W;E_L)=1\text{ bit},
\qquad
R_{\rm corr}(L)=0.125.
\]

Thus throughout the main panel:

\[
\boxed{
I(H)=I(M)=I(L)=1
}
\]

while:

\[
\boxed{
R_H>R_M>R_L.
}
\]

Raw information therefore cannot rank the candidates.

For same-relevance controls, multiple anonymous copies of the same evidence partition may be assigned different `kappa` burdens. Candidate identity carries no semantic authority.

---

## 4. Reference acquisition contract

The reference cardinal implementation assigns:

\[
q_i=R_i-\kappa_i
\]

and treats commitment as:

\[
q_{COMMIT}=0.
\]

The warranted next action is the `argmax` set over:

\[
\{q_1,q_2,q_3,0\}.
\]

If every candidate has `q_i <= 0`, commit.

If multiple candidates share the maximal positive margin, every tied maximizer is acceptable; the audit must compare optimal-action sets rather than impose an arbitrary semantic tie-break.

This reference is not assumed minimal.

---

## 5. Frozen multi-candidate panel

Each state presents exactly three simultaneously admissible candidates plus `COMMIT`.

All main H/M/L candidates have one bit of raw information. Only correction relevance and normalized burden vary.

### P1 — same burden, different correction relevance

```text
candidate   R_corr   kappa   q
H           0.500    0.100   0.400
M           0.250    0.100   0.150
L           0.125    0.100   0.025
```

All three are worth acquiring. The unique optimal next refinement is:

\[
\boxed{H}.
\]

This is the matched control:

\[
\boxed{
I_H=I_M=I_L,
\quad
\kappa_H=\kappa_M=\kappa_L,
\quad
R_H\neq R_M\neq R_L.
}
\]

### P2 — same correction relevance, different burden

Use three anonymous copies of the medium-relevance evidence partition:

```text
candidate   R_corr   kappa   q
M_a         0.250    0.050   0.200
M_b         0.250    0.100   0.150
M_c         0.250    0.200   0.050
```

All three are worth acquiring. The unique optimal next refinement is the lowest-burden copy:

\[
\boxed{M_a}.
\]

This isolates burden under matched information and correction relevance.

### P3 — crossing tradeoff, high relevance wins

```text
candidate   R_corr   kappa   q
H           0.500    0.300   0.200
M           0.250    0.100   0.150
L           0.125    0.020   0.105
```

Every candidate is worthwhile.

Higher correction relevance comes with higher burden, so no candidate Pareto-dominates the others in `(R_corr, -kappa)`.

Unique optimum:

\[
\boxed{H}.
\]

### P4 — crossing tradeoff, medium relevance wins

```text
candidate   R_corr   kappa   q
H           0.500    0.450   0.050
M           0.250    0.080   0.170
L           0.125    0.010   0.115
```

Again all three are worthwhile and mutually Pareto-incomparable.

Unique optimum:

\[
\boxed{M}.
\]

### P5 — crossing tradeoff, low relevance wins

```text
candidate   R_corr   kappa   q
H           0.500    0.480   0.020
M           0.250    0.200   0.050
L           0.125    0.010   0.115
```

Again all three are worthwhile and mutually Pareto-incomparable.

Unique optimum:

\[
\boxed{L}.
\]

The P3/P4/P5 triplet prevents a fixed shortcut such as:

```text
always choose highest correction relevance
always choose lowest burden
always choose a fixed candidate identity
```

from reproducing the target policy.

### P6 — equal acquisition worth under different decompositions

```text
candidate   R_corr   kappa   q
H           0.500    0.300   0.200
M           0.250    0.050   0.200
L           0.125    0.010   0.115
```

The warranted optimal set is:

\[
\boxed{\{H,M\}}.
\]

The audit must preserve the equivalence rather than invent an unearned ordering between equal-margin candidates.

### P7 — exact commit boundary

```text
candidate   R_corr   kappa   q
H           0.500    0.500   0.000
M           0.250    0.250   0.000
L           0.125    0.125   0.000
```

The previously frozen strict acquisition rule is:

\[
q>0.
\]

Therefore:

\[
\boxed{COMMIT}.
\]

This protects the termination boundary against an accidental `>=` change.

### P8 — sign-only positive control

```text
candidate   R_corr   kappa   q
H           0.500    0.550  -0.050
M           0.250    0.100   0.150
L           0.125    0.200  -0.075
```

Exactly one candidate is worthwhile.

Unique optimum:

\[
\boxed{M}.
\]

This shows that candidate-vs-commit sign information remains sufficient when there is no within-positive ordering problem.

---

## 6. Core preregistered choice signature

Canonical optimal-action sets:

```text
P1  {H}
P2  {M_a}
P3  {H}
P4  {M}
P5  {L}
P6  {H, M}
P7  {COMMIT}
P8  {M}
```

The core discriminant is not raw performance. It is which representation classes can identify these action sets under anonymous candidate permutations.

---

## 7. Representation ladder under test

The audit compares the following structures while holding the environment fixed.

### R0 — candidate-vs-commit sign only

For each candidate, expose only:

\[
\boxed{
\sigma_i=\mathbf 1[q_i>0].
}
\]

This is the `Q_acquire^bot` role already earned by the preceding valuation audit.

It contains no information for ranking multiple positive candidates.

Preregistered expectation:

- succeeds on P7/P8;
- is insufficient on states with multiple anonymous positive candidates and a unique optimum.

### R1 — sign plus Pareto partial order

Retain the candidate-vs-commit sign and add only uncompensated dominance:

\[
e_i\succ_P e_j
\iff
R_i\ge R_j
\land
\kappa_i\le\kappa_j
\]

with at least one strict inequality.

This representation can resolve P1 and P2, where one candidate is better without a relevance/burden tradeoff.

It cannot order the crossing tradeoffs P3/P4/P5, where the candidates are pairwise incomparable.

Preregistered expectation:

\[
\boxed{
\text{Pareto partial order is insufficient for the complete panel.}
}
\]

### R2 — derived compensated ordinal comparator

Do **not** store numeric `q_i` values and do **not** supply a rank table.

Generate only pairwise comparison outcomes at decision time:

\[
\boxed{
e_i\succ_Q e_j
\iff
R_i-\kappa_i>R_j-\kappa_j.
}
\]

Equivalently, implementations may compare:

\[
R_i+\kappa_j
\quad\text{vs}\quad
R_j+\kappa_i
\]

without materializing a persistent cardinal `q` representation.

Commit is included through the already-earned strict comparison:

\[
R_i>\kappa_i.
\]

The pairwise relation must be generated from evidence consequences and burden, never supplied as a semantic ranking table.

Preregistered expectation:

\[
\boxed{
\text{derived ordinal comparison is sufficient for the panel.}
}
\]

If so, the result concerns the representation of acquisition value, not removal of the underlying relevance/burden quantities.

### R3 — max-only tournament using the same comparator

A stronger minimality probe asks whether a **full ordinal ranking** must ever be represented.

Use the same derived pairwise comparator as R2, but maintain only a current candidate champion. Compare candidates sequentially and retain the winner; after the tournament, compare the winner against `COMMIT`.

The controller must not materialize or store the total order among losing candidates.

Preregistered expectation:

\[
\boxed{
\text{full ranking storage is not necessary if max-only comparison preserves the same optimal-action set.}
}
\]

A pass would support only a representational contraction toward choice-maximality. It would not establish that the compensated comparator itself is minimal.

### R4 — cardinal reference

Reference implementation:

\[
q_i=R_i-\kappa_i
\]

with explicit numeric margins and `argmax` over candidates plus `COMMIT`.

This is the behavioral baseline, not a presumed minimum.

---

## 8. Anonymous-candidate identifiability control

Run at least 64 anonymous encodings.

For each encoding:

- permute the three candidate identifiers;
- permute presentation order;
- independently flip the binary evidence-output tokens;
- permute gate-state labels used to realize the same evidence partitions;
- preserve only the actual evidence partition and burden field.

No controller may access semantic labels such as `H`, `M`, `L`, `best`, `cheap`, or `relevant`.

For same-relevance P2 candidates, the evidence partitions may be structurally identical; only burden differs.

This makes candidate identity an invalid shortcut.

---

## 9. Evaluator-side impossibility / ceiling certificate

The audit must compute the best achievable action-selection accuracy for restricted representations under anonymous candidate permutations, rather than evaluating one arbitrary tie-break rule.

Preregistered structural expectations:

### Sign-only ceiling

On P1–P5, all three candidates have positive sign but only one is optimal. A sign-only anonymous policy cannot distinguish the unique winner.

On P6, all three are positive but two are acceptable maximizers.

P7 and P8 are sign-resolvable.

Under uniform candidate permutations and uniform weighting of the eight panel states, the expected best sign-only ceiling is:

\[
\boxed{
13/24\approx0.5417.
}
\]

The implementation must verify this from orbit/signature collisions rather than hard-code the number.

### Sign + Pareto ceiling

P1 and P2 are Pareto-resolvable.

P3–P5 contain three positive pairwise-incomparable candidates with one unique optimum.

P6 contains three positive pairwise-incomparable candidates with two acceptable maximizers.

P7/P8 are resolvable by the sign gate.

Under the same symmetry/weighting contract, the preregistered expected ceiling is:

\[
\boxed{
17/24\approx0.7083.
}
\]

Again, the implementation must derive this from representation collisions.

### Ordinal/cardinal target

The derived compensated ordinal relation and cardinal reference are expected to identify the complete optimal-action correspondence:

\[
\boxed{1.0}.
\]

If the evaluator-side ceilings differ from these preregistered values because of an implementation detail, stop and diagnose the panel rather than silently changing the interpretation.

---

## 10. Negative controls and localization

The panel must make the following failures distinguishable.

### N1 — sign-only

Failure on P1–P6 with multiple positive candidates localizes:

\[
\boxed{
\text{candidate-vs-commit sufficiency}
\neq
\text{multi-candidate choice sufficiency}.
}
\]

### N2 — correction-relevance lexicographic rule

Always choosing maximal `R_corr` among positive candidates must fail P4/P5.

### N3 — burden lexicographic rule

Always choosing minimal `kappa` among positive candidates must fail P3 and, depending on ties, other matched cases.

### N4 — Pareto-only

Failure on P3/P4/P5 localizes the need for a compensated tradeoff relation among candidates that are each better on a different dimension.

### N5 — supplied order table

A precomputed per-state ranking or winner table may reproduce behavior but is classified as:

\[
\boxed{\text{oracle displacement}.}
\]

It cannot support a substrate-reduction claim.

---

## 11. Anti-oracle and specification-burden rule

The governing rule is:

\[
\boxed{
\text{behavioral substitution}
\neq
\text{substrate reduction}.
}
\]

No valid substitution may receive:

- the target winner;
- a precomputed candidate ranking;
- semantic candidate type labels;
- a per-state policy table.

Valid comparison relations must be **generated from the frozen evidence consequences and burden representation**.

The implementation must report a finite specification ledger including at least:

| Representation | Supplied target decisions | Supplied rank entries | Persistent cardinal `q` values | Derived pairwise comparisons | Notes |
|---|---:|---:|---:|---:|---|
| sign only | 0 | 0 | 0 | 0 | candidate-vs-commit only |
| sign + Pareto | 0 | 0 | 0 | Pareto only | no compensated tradeoff |
| full ordinal | 0 | 0 | 0 | yes | derived online from `R_corr,kappa` |
| max-only tournament | 0 | 0 | 0 | yes, on demand | no total ranking stored |
| cardinal baseline | 0 | 0 | yes | optional | explicit numeric margins |
| order/winner table | direct or equivalent | direct | 0 | 0 | oracle displacement |

A successful ordinal or max-only substitution is at most a **representation contraction** unless the supplied external valuation burden also decreases.

The audit must explicitly ask:

\[
\boxed{\textbf{Where did the complexity go?}}
\]

---

## 12. Frozen regression requirements

The executable child audit must reassert the already-earned upstream certificates rather than modifying them.

At minimum:

1. valuation-role regression from `c97a5cf`:
   - 64 anonymous encodings;
   - 320 candidate-vs-commit valuation decisions;
   - zero baseline-vs-`kappa` mismatches;
2. STOP/navigation regression from `4694382`:
   - 64 anonymous encodings;
   - 3,584 visited decision points;
   - 1,536 derived terminations;
   - zero normalized primitive-vs-derived trajectory mismatches.

If either upstream regression changes, reject attribution to multi-candidate acquisition ordering.

---

## 13. Primary endpoints

A valid execution must report:

1. exact evaluator-generated `I`, `R_corr`, `kappa`, and reference `q` for every candidate/state;
2. exact optimal-action set for P1–P8;
3. action-set agreement for each representation across all anonymous encodings;
4. evaluator-side best-possible ceilings for sign-only and sign+Pareto representations;
5. whether the derived ordinal comparator matches the cardinal reference;
6. whether the max-only tournament matches without materializing a total order;
7. candidate-identity invariance;
8. upstream valuation/navigation/termination regression results;
9. specification-burden accounting.

Terminal accuracy alone is not an adequate endpoint.

---

## 14. Frozen interpretation rules

| Result | Interpretation |
|---|---|
| sign-only fails where multiple worthwhile candidates coexist | candidate-vs-commit role is insufficient for multi-candidate selection |
| Pareto succeeds on P1/P2 but fails P3/P4/P5 | uncompensated partial order is insufficient when relevance/burden trade off |
| derived ordinal comparator matches cardinal baseline | explicit cardinal `q` representation is not necessary for these choices; compensated ordering survives |
| max-only tournament matches ordinal/cardinal behavior | storing a full ordinal ranking is unnecessary; choice-maximality via pairwise comparison is sufficient in this panel |
| full ordinal succeeds but max-only fails | additional relational context beyond simple tournament maximality is required; diagnose before broader claim |
| cardinal succeeds but derived ordinal fails | cardinal magnitude is doing behavioral work under the declared contract |
| supplied rank/winner table succeeds | behavioral equivalence only; oracle displacement |
| candidate-ID permutation changes behavior | leakage / invalid audit |
| upstream regression changes | intervention leaked outside acquisition ordering; reject attribution |
| crossing cases fail inconsistently | comparison-role decomposition is underspecified; do not promote a dependency claim |

---

## 15. Candidate claims if preregistered predictions hold

If sign-only and Pareto controls fail as predicted while the derived ordinal comparator succeeds, the strongest candidate claim is:

\[
\boxed{
\textbf{In this finite audited panel, candidate-vs-commit worth and uncompensated Pareto dominance are insufficient to choose among multiple worthwhile refinements; a compensated acquisition ordering identifies the warranted next refinement.}
}
\]

If the max-only tournament also preserves the cardinal baseline, an additional candidate claim is:

\[
\boxed{
\textbf{A stored full ranking and explicit cardinal }q\textbf{ vector are not necessary for the observed choices; on-demand pairwise comparison sufficient to identify a maximal candidate preserves behavior.}
}
\]

The stronger claim is explicitly **not** earned by this preregistration:

\[
\boxed{
Q_{\rm acquire,min}\;?
}
\]

remains open.

In particular, a successful ordinal/max-only substitution would not establish that:

- cardinal `R_corr` itself is unnecessary;
- normalized burden `kappa` is unnecessary;
- the compensated comparison relation is globally minimal;
- the probe menu is generated rather than supplied;
- experiment accessibility has been minimized;
- experiment-space construction or basin opening has occurred.

No broader dependency-ledger update is authorized by this preregistration alone.

---

## 16. Research position after this preregistration

The empirical sequence remains:

\[
\boxed{
\text{geometry}
\rightarrow
\text{navigation}
\rightarrow
\text{valuation representation}
\rightarrow
\boxed{Q_{\rm acquire}\text{ multi-candidate minimality}}
\rightarrow
\text{experiment accessibility}.
}
\]

The next repository action after this preregistration is implementation/execution of this audit only. Results, if any, must be committed separately so the preregistration remains historically inspectable.
