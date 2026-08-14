# Valuation-Role Discriminant Audit — Preregistration

## Status

This document freezes the valuation-role audit **before execution**.

Parent dependency checkpoint:

```text
cb9afb6  Consolidate experiment-planning dependencies
```

No empirical results are recorded here.

The audit targets the comparison structure currently implemented by `V` and `C`; it does **not** ask whether the symbols `V` and `C` themselves are necessary.

The frozen conceptual target is:

\[
\boxed{
I(e)\neq R_{\rm corr}(e)\neq Q_{\rm acquire}(e).
}
\]

The intended research move is:

\[
\boxed{
\text{separate functional quantities}
\rightarrow
\text{substitute representation}
\rightarrow
\text{trace specification burden}
\rightarrow
\text{retain only necessary role}.
}
\]

---

## 1. Scientific question

What minimum valuation comparison structure is required to distinguish:

1. evidence that is informative about the world;
2. evidence that can improve the warranted correction;
3. evidence whose corrective improvement is worth its acquisition burden?

The audit must not collapse these into one quantity.

---

## 2. Frozen structures

Across valuation-controller interventions, hold fixed:

\[
\boxed{
\mathfrak R_E,\;S_{\rm refine},\;T_{\rm stop},\;\Pi_{\mathcal P},\;\tau.
}
\]

Operationally:

- every controller sees the same finite world set;
- every controller sees the same evidence partitions and outcome alphabets;
- every controller sees the same probe availability and one-step commitment boundary;
- every controller uses the same warranted terminal correction contract;
- only the **valuation representation / comparison rule** changes.

Because the valuation panel introduces nuisance variables to separate information from correction relevance, its fixed geometry is a dedicated matched test geometry. The already-earned navigation and termination roles are protected by a regression certificate against the previous STOP audit rather than redefined here.

No experiment-space construction, geometry repair, new evidence channel, authorization change, or stronger planner is permitted.

---

## 3. Evaluator-side quantities

For candidate evidence action `e`:

\[
I(e)=I(W;E_e)
\]

is raw world information.

Let the current terminal correction accuracy be:

\[
A_0=\operatorname{BayesAcc}(a^\star).
\]

Define correction relevance:

\[
R_{\rm corr}(e)
=
\mathbb E\left[\operatorname{BayesAcc}(a^\star\mid E_e)\right]-A_0.
\]

The current scalar baseline represents acquisition margin as:

\[
M_{VC}(e)=V R_{\rm corr}(e)-C(e).
\]

Acquire iff:

\[
M_{VC}(e)>0.
\]

These definitions are evaluator-side bookkeeping. Their role is to expose non-substitutability; they are not assumed to be universal primitives.

---

## 4. Finite world and correction contract

Use uniform worlds:

\[
W=(s,x,y,n_1,n_2,n_3,n_4)\in\{0,1\}^7.
\]

The nuisance bits never affect the warranted terminal correction.

The correction contract remains the selector task:

\[
a^\star(W)=
\begin{cases}
x,&s=0,\\
y,&s=1.
\end{cases}
\]

Before the valuation action:

\[
A_0=0.5.
\]

Observing either branch value `x` or `y` raises expected correction accuracy to `0.75`, hence:

\[
R_{\rm corr}=0.25
\]

for a single branch-relevant observation under the uniform prior.

The panel allows exactly one evidence acquisition before commitment. This prevents the sequential-reachability role from deciding the valuation contrast for the panel itself.

Baseline scalar value:

\[
V=10.
\]

---

## 5. Frozen valuation panel

### A — high information, high correction relevance, worth acquiring

Evidence:

```text
(x, n1, n2)
```

Cost:

\[
C_A=1.
\]

Preregistered quantities:

\[
I(A)=3,\qquad R_{\rm corr}(A)=0.25,
\]

\[
M_{VC}(A)=10(0.25)-1=+1.5.
\]

Prediction:

\[
\boxed{A:\;ACQUIRE}.
\]

### B — high information, correction-irrelevant

Evidence:

```text
(n1, n2, n3)
```

Cost:

\[
C_B=1.
\]

Preregistered quantities:

\[
I(B)=3,\qquad R_{\rm corr}(B)=0,
\]

\[
M_{VC}(B)=-1.
\]

Prediction:

\[
\boxed{B:\;COMMIT}.
\]

This gives the exact matched control:

\[
\boxed{I(A)=I(B),\quad C(A)=C(B),\quad R_{\rm corr}(A)\neq R_{\rm corr}(B).}
\]

### C — lower information, high correction relevance, worth acquiring

Evidence:

```text
x
```

Cost:

\[
C_C=1.
\]

Preregistered quantities:

\[
I(C)=1,\qquad R_{\rm corr}(C)=0.25,
\]

\[
M_{VC}(C)=+1.5.
\]

Prediction:

\[
\boxed{C:\;ACQUIRE}.
\]

Thus:

\[
\boxed{I(C)<I(A)\quad\land\quad Q_{\rm acquire}(C)=Q_{\rm acquire}(A).}
\]

### D — high information, high correction relevance, too costly

Evidence partition is identical to A:

```text
(x, n1, n2)
```

Cost:

\[
C_D=3.
\]

Preregistered quantities:

\[
I(D)=3,\qquad R_{\rm corr}(D)=0.25,
\]

\[
M_{VC}(D)=10(0.25)-3=-0.5.
\]

Prediction:

\[
\boxed{D:\;COMMIT}.
\]

This gives the second exact matched control:

\[
\boxed{I(A)=I(D),\quad R_{\rm corr}(A)=R_{\rm corr}(D),\quad C(A)\neq C(D).}
\]

### B+ — anti-information-maximization control

Evidence:

```text
(n1, n2, n3, n4)
```

Cost:

\[
C_{B+}=1.
\]

Preregistered quantities:

\[
I(B+)=4,\qquad R_{\rm corr}(B+)=0,
\]

\[
M_{VC}(B+)=-1.
\]

Prediction:

\[
\boxed{B+:\;COMMIT}.
\]

This deliberately makes raw information misleading:

\[
\boxed{I(B+)>I(A)>I(C)}
\]

while:

\[
\boxed{Q(B+)<0,\quad Q(A)>0,\quad Q(C)>0.}
\]

---

## 6. Core preregistered signature

The required acquisition pattern is:

\[
\boxed{(A,B,C,D,B+)=(1,0,1,0,0)}
\]

where `1 = ACQUIRE` and `0 = COMMIT`.

The decisive pairwise controls are:

| Contrast | Isolated question |
|---|---|
| A vs B | information vs correction relevance |
| A vs C | information magnitude vs correction relevance |
| A vs D | correction relevance vs acquisition worth |
| B+ | anti-information-maximization |

---

## 7. Baseline valuation representation

Baseline:

\[
M_{VC}(e)=V R_{\rm corr}(e)-C(e).
\]

Acquire iff `M_VC > 0`.

This is the reference behavior only. Success of this baseline does not establish necessity of separate `V` and `C` representations.

---

## 8. Primary substitution: scale-free threshold

Define:

\[
\kappa(e)=\frac{C(e)}{V}.
\]

Then:

\[
M_{VC}(e)>0
\iff
R_{\rm corr}(e)>\kappa(e).
\]

Replace the separate valuation inputs:

\[
\boxed{(V,C)\rightarrow\kappa.}
\]

The substituted controller receives `R_corr` and the normalized acquisition threshold `kappa`; it does not receive a separate global `V` or absolute `C` inside its decision rule.

Preregistered thresholds:

```text
A  0.1
B  0.1
C  0.1
D  0.3
B+ 0.1
```

A successful substitution supports only:

\[
\boxed{\text{separate literal }V,C\text{ representation is contingent for this behavior}.}
\]

It does not support eliminating the acquisition-worth comparison.

---

## 9. Secondary behavioral substitution: order table

A direct ordinal table over `{probe, COMMIT}` may be evaluated as a behavioral equivalence control.

However:

\[
\boxed{\text{behavioral substitution}\neq\text{substrate reduction}.}
\]

If an order table simply stores the baseline decisions, it relocates the valuation information into an oracle. Such a result must be reported as behavioral equivalence only.

It may not support a minimality claim unless specification accounting independently shows reduced external burden.

---

## 10. Negative controls

### N1 — information-only

Acquire whenever `I(e) > 0`.

Preregistered failures:

- B is incorrectly acquired;
- B+ is incorrectly acquired;
- D is incorrectly acquired.

The key failure signature is systematic purchase of high-information, correction-irrelevant evidence.

### N2 — correction-relevance-only

Acquire whenever:

\[
R_{\rm corr}(e)>0.
\]

Preregistered failure:

- D is incorrectly acquired.

This isolates the difference between correction relevance and acquisition worth.

### N3 — information-per-cost shortcut

Any controller whose decision is a function only of `I(e)/C(e)` must confront exact collisions:

\[
\frac{I(A)}{C(A)}=\frac{I(B)}{C(B)}=3
\]

with opposite required decisions.

Additionally:

\[
\frac{I(B+)}{C(B+)}=4>3=\frac{I(A)}{C(A)}
\]

while B+ must be rejected.

The audit will report the evaluator-side classification ceiling for feature subsets rather than selecting a favorable arbitrary threshold.

---

## 11. Feature-sufficiency / collision certificate

Before testing controllers, compute the maximum deterministic classification accuracy over the five valuation cases for signatures formed from subsets of:

```text
I
R_corr
C
I/C
```

This is an evaluator-side identifiability certificate.

Preregistered expectations:

- `I` alone cannot perfectly recover acquisition worth;
- `R_corr` alone cannot perfectly recover acquisition worth;
- `(I,C)` cannot separate A from B;
- `(I,R_corr)` cannot separate A from D;
- `I/C` cannot separate the required decisions;
- `(R_corr,C)` is sufficient for this panel;
- raw `I` is therefore not required once correction relevance is already represented.

These are panel-local statements only.

---

## 12. Anonymous encoding control

Run 64 anonymous encodings.

For each encoding:

- permute probe/case identifiers;
- permute output-coordinate order within multibit evidence;
- independently flip binary output tokens.

The evaluator computes `I` and `R_corr` from the resulting partitions, not from semantic names.

All preregistered quantities and decisions must remain invariant up to exact finite arithmetic / numerical tolerance.

---

## 13. Regression certificate for frozen navigation and termination roles

The implementation must invoke the existing STOP-substitution audit and require its previously earned behavior to remain intact.

Required regression conditions include:

```text
64 anonymous encodings
3584 visited decision points
1536 derived terminations
0 normalized primitive-vs-derived trajectory mismatches
```

The valuation audit may not alter the previous A/B/C geometry, sequential refinement preservation, or derived termination implementation.

If the regression changes, reject valuation-only attribution.

---

## 14. Specification-burden ledger

The audit must explicitly report designer-supplied valuation structure before and after substitution.

Use a finite operational ledger, not a claim about Kolmogorov complexity.

At minimum report:

- number of separate global valuation scalars;
- number of per-case/per-probe valuation fields;
- whether the replacement directly stores the target acquisition decision;
- whether any information removed from the controller has merely been moved into an oracle/table.

Preregistered interpretation:

- baseline `V,C`: one global value scalar plus per-case absolute cost fields;
- `kappa`: no separate global `V` in the decision rule and one normalized threshold field per case;
- order table: direct decision storage, therefore **oracle displacement**, not accepted as substrate reduction.

The anti-scaffold rule is mandatory:

\[
\boxed{\text{Where did the complexity go?}}
\]

---

## 15. Primary endpoints

A role-preserving scale-free substitution must satisfy all of:

1. exact A/B/C/D/B+ acquisition signature under all 64 encodings;
2. exact agreement with the baseline `V,C` decision on every valuation case;
3. preserved pairwise controls A/B, A/C and A/D;
4. STOP-audit regression remains unchanged;
5. no direct storage of target decisions in the scale-free controller;
6. specification ledger reports the representation change explicitly.

---

## 16. Frozen interpretation rules

| Result | Interpretation |
|---|---|
| `kappa` preserves all behavior and regression | separate literal `V,C` representation is contingent; acquisition-worth comparison survives |
| order table preserves behavior but stores target decisions | behavioral equivalence only; no substrate reduction |
| information-only buys B/B+ | raw information cannot substitute for correction relevance |
| relevance-only buys D | correction relevance cannot substitute for acquisition worth |
| substitution fails only on D | proposed reduction lost the acquisition-burden tradeoff |
| substitution fails on B/B+ | proposed reduction lost correction relevance |
| substitution fails on C | proposed reduction incorrectly equates information magnitude with usefulness |
| STOP/navigation regression changes | intervention leaked outside valuation; reject attribution |
| broader unexplained failure | valuation-role decomposition is underspecified |

---

## 17. Claim boundary

If the preregistered predictions hold, the strongest candidate claim is:

\[
\boxed{\textbf{In this finite audited panel, raw information, correction relevance, and acquisition worth are behaviorally non-substitutable.}}
\]

If the scale-free substitution also preserves behavior, the additional candidate claim is:

\[
\boxed{\textbf{The separate cardinal }V,C\textbf{ implementation is not necessary for the observed valuation decisions; a normalized acquisition-threshold representation preserves them.}}
\]

Neither result establishes that the surviving normalized tradeoff is minimal.

`Q_acquire,min` remains open.

No broader dependency-ledger update is authorized by this preregistration alone.
