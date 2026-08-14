# Refinement Controller Substitution Audit

## Status

Navigation-minimality audit over the validated reachable-refinement geometry at `fadf50368d13d80ed06c5da1ff7fd0cc628b2690`.

Primary intervention only:

\[
\boxed{do(\Pi_{\rm DP}\leftarrow\Pi_{\rm prune}).}
\]

The following remain frozen:

\[
\boxed{\mathfrak R_E,\Pi_{\mathcal P},C,V,\tau,A_{\rm probe},\text{budget},STOP.}
\]

`STOP` is still primitive and is **not** tested here.

---

## Scientific question

The geometry audit established that timely compositional refinement reachability matters beyond static evidence inventory. This audit asks only:

> Is finite dynamic programming itself necessary to navigate that fixed geometry, or can a weaker decision-preserving sequential controller reproduce its behavior?

The intended distinction is:

\[
\boxed{\text{DP implementation necessity}\neq\text{sequential refinement-role necessity}.}
\]

---

## Frozen environment

The audit reuses the exact 8-world selector/left/right task and A/B/C geometry from the reachable-refinement discriminant audit:

- warranted correction: `left` if selector=0, else `right`;
- three binary probes: selector, left, right;
- probe cost \(C=1\);
- terminal correctness value \(V=10\);
- two-probe budget;
- commitment deadline \(\tau=2\);
- A: correct branch probe remains available on time after selector;
- B: correct branch probe remains available but too late;
- C: wrong branch probe remains available on time;
- 64 anonymous probe permutations/polarity flips.

No geometry or evidence semantics change between controllers.

---

## Baseline: DP

The baseline uses finite Bellman recursion:

\[
V_{\rm DP}(s)=\max\left\{V_{STOP}(s),\max_r[-C(r)+\mathbb E_oV_{\rm DP}(s_{r,o})]\right\}.
\]

---

## Substitution: reachability-preserving pruning

The replacement does **not** recursively propagate expected continuation value.

It uses only the fixed refinement geometry to evaluate a Boolean predicate:

\[
\operatorname{CanCorrect}^{\tau}(s),
\]

meaning that some contingent admissible refinement policy still guarantees the warranted correction for every compatible world before commitment.

At each state:

1. test which timely probes preserve \(\operatorname{CanCorrect}^{\tau}=1\) on every outcome branch;
2. if any exist, keep those and reject probes that destroy the exact timely correction path;
3. if no exact timely path remains, use only the frozen one-step \(V-C\) rule over currently available probes plus primitive `STOP`.

This is a finite operationalization of the preregistered role:

\[
\boxed{\text{preserve correction-relevant contingent refinement structure before commitment}.}
\]

It is **not** claimed to be a universal minimal controller.

---

## Negative control: myopic one-step navigation

A controller that repeatedly optimizes only immediate \(V-C\) is included as a localization control.

At the A root:

\[
\boxed{
V_1(STOP)=5.0,\quad
V_1(selector)=4.0,\quad
V_1(left)=V_1(right)=6.5.
}
\]

Thus the selector is unattractive myopically even though selector-first is the unique route to perfect timely correction.

---

## Results

Across all 64 anonymous encodings:

| Geometry | Controller | Accuracy | Mean probes/cost | Utility |
|---|---|---:|---:|---:|
| A timely | DP | 1.00 | 2.00 | 8.00 |
| A timely | refinement prune | 1.00 | 2.00 | 8.00 |
| A timely | myopic control | 0.75 | 1.00 | 6.50 |
| B late | DP | 0.75 | 1.00 | 6.50 |
| B late | refinement prune | 0.75 | 1.00 | 6.50 |
| B late | myopic control | 0.75 | 1.00 | 6.50 |
| C unreachable | DP | 0.75 | 1.00 | 6.50 |
| C unreachable | refinement prune | 0.75 | 1.00 | 6.50 |
| C unreachable | myopic control | 0.75 | 1.00 | 6.50 |

The pruning controller therefore matches DP on terminal accuracy, acquisition cost, probe count, and total utility in every condition and encoding.

A stronger action-level check evaluates every decision selected by the pruning controller against the DP-optimal action set.

Observed:

\[
\boxed{3584\text{ visited decision points}}
\]

and:

\[
\boxed{0\text{ pruning actions outside the DP-optimal set}.}
\]

The A myopic failure is the key localization control:

\[
\boxed{0.75\rightarrow1.00\text{ accuracy}}
\]

and

\[
\boxed{6.5\rightarrow8.0\text{ utility}}
\]

when moving from one-step navigation to reachability-preserving sequential navigation.

---

## Earned result

Within this finite deterministic audited geometry:

\[
\boxed{\Pi_{\rm DP}\text{ is not necessary for the observed navigation behavior}.}
\]

The result does **not** support eliminating sequential/compositional dependence. The myopic controller fails precisely where the selector has poor immediate value but positive two-step correction value.

The narrow surviving role is:

\[
\boxed{\textbf{navigation must preserve correction-relevant contingent refinement structure across steps when immediate value is insufficient}.}
\]

So the earned distinction is:

\[
\boxed{\text{dynamic-programming implementation}\neq\text{decision-preserving sequential refinement role}.}
\]

---

## Boundaries

This audit does not establish that:

- the pruning controller is globally minimal;
- Boolean reachability suffices in deeper or stochastic systems;
- expected-value planning is generally unnecessary;
- primitive `STOP` is unnecessary;
- termination discipline is derived;
- geometry repair, basin opening, or research agency has occurred.

The result is restricted to the declared finite deterministic regime.

---

## Next dependency

`STOP` was deliberately frozen. The next independent intervention is therefore:

\[
\boxed{do(STOP_{\rm primitive}\leftarrow STOP_{\rm derived}).}
\]

Only that audit can test:

\[
\boxed{\text{termination token}\neq\text{termination discipline}.}
\]

The phase order remains:

\[
\boxed{\text{validated geometry}\rightarrow\text{navigation minimality}\rightarrow\text{geometry repair}.}
\]
