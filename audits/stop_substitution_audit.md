# STOP Substitution Audit

## Status

Navigation-minimality continuation from `68f2338b5a903efdd77555dea372620655aec201`.

Primary intervention only:

\[
\boxed{do(STOP_{\rm primitive}\leftarrow STOP_{\rm derived}).}
\]

The following remain frozen:

\[
\boxed{\mathfrak R_E,\Pi_{\mathcal P},C,V,\tau,A_{\rm probe},\text{budget},\Pi_{\rm prune}.}
\]

No geometry repair, probe-space change, new evidence channel, or new theory is introduced here.

---

## Scientific question

Can termination be recovered from the already-frozen refinement geometry and value/cost contract without supplying `STOP` as an epistemic action?

The intended distinction is:

\[
\boxed{\text{termination token}\neq\text{termination discipline}.}
\]

The audit does **not** ask whether termination can be learned from scratch, nor whether termination discipline itself can be removed.

---

## Baseline

The baseline is the reachability-pruning controller from `68f2338b5a903efdd77555dea372620655aec201`.

That controller already replaced Bellman dynamic programming with the narrower role:

\[
\boxed{\text{preserve correction-relevant contingent refinement structure across steps}.}
\]

But its fallback action set still contains primitive `STOP`.

---

## Substitution

The derived controller's epistemic action set contains **probes only**.

There is no `STOP` candidate.

At each state, first compute the same reachability-preserving probes as the frozen controller. If any exist, retain the same sequential role and choose one of them.

If no exact timely correction path remains, define the immediate commit utility from the frozen correction/value contract:

\[
U_{\rm commit}(s)=V\,\operatorname{BayesAcc}(a^\star\mid s).
\]

For each currently timely probe \(r\), define the same one-step acquisition utility used by the baseline fallback:

\[
Q_1(r\mid s)
=
-C(r)
+
\mathbb E_o\left[U_{\rm commit}(s_{r,o})\right].
\]

The continuation set is then determined by the frozen contract:

- if a reachability-preserving probe exists, continue on that refinement path;
- otherwise continue only if some probe satisfies

\[
Q_1(r\mid s)>U_{\rm commit}(s);
\]

- if no such probe exists, no continuation is returned and commitment occurs.

Thus termination is represented as:

\[
\boxed{\text{absence of a justified continuation}.}
\]

It is not represented as a supplied epistemic action.

---

## Why this is not a claim that termination machinery disappeared

The specification-accounting rule remains mandatory:

\[
\boxed{\text{removed from view}\neq\text{removed from substrate}.}
\]

The explicit `STOP` token is removed, but the termination judgment is still encoded by the frozen value/cost and refinement contract.

So the strongest possible earned result is only:

\[
\boxed{STOP_{\rm primitive}\text{ is unnecessary for this audited behavior}.}
\]

It would **not** imply that termination discipline is unnecessary.

---

## Negative control: exhaustion-only continuation

To test whether the derived boundary is doing causal work, the audit includes a controller with:

- no primitive `STOP` action;
- the same reachability-preserving rule;
- **no value-derived termination condition**.

When exact correction reachability is absent, this controller continues probing whenever any timely probe remains, even when the best remaining probe cannot improve utility over immediate commitment.

This isolates:

\[
\boxed{\text{remove STOP token}\neq\text{recover termination discipline}.}
\]

---

## Results

The audit runs all 64 anonymous probe permutations/polarity flips from the frozen geometry.

| Geometry | Controller | Accuracy | Mean probes/cost | Utility |
|---|---|---:|---:|---:|
| A timely | primitive `STOP` | 1.00 | 2.00 | 8.00 |
| A timely | derived termination | 1.00 | 2.00 | 8.00 |
| A timely | exhaustion-only | 1.00 | 2.00 | 8.00 |
| B late | primitive `STOP` | 0.75 | 1.00 | 6.50 |
| B late | derived termination | 0.75 | 1.00 | 6.50 |
| B late | exhaustion-only | 0.75 | 2.00 | 5.50 |
| C unreachable | primitive `STOP` | 0.75 | 1.00 | 6.50 |
| C unreachable | derived termination | 0.75 | 1.00 | 6.50 |
| C unreachable | exhaustion-only | 0.75 | 2.00 | 5.50 |

The derived controller exactly preserves baseline behavior.

Across:

\[
\boxed{3584\text{ visited decision points}}
\]

there are:

\[
\boxed{1536\text{ primitive STOP decisions}}
\]

and:

\[
\boxed{1536\text{ corresponding derived terminations}.}
\]

After mapping primitive `STOP` to an empty continuation, normalized trajectories have:

\[
\boxed{0\text{ mismatches}.}
\]

The derived termination reasons are:

- `no_timely_refinement`: 512 cases;
- `no_positive_continuation_value`: 1024 cases.

The latter are exactly the B/C cases where additional probing remains physically possible but is not justified by the frozen value/cost contract.

---

## Localization from the negative control

The exhaustion-only controller is diagnostic.

In B and C it keeps probing after the primitive/derived controller would commit:

\[
\boxed{1\rightarrow2\text{ mean probes}.}
\]

Accuracy does not improve:

\[
\boxed{0.75\rightarrow0.75,}
\]

so utility falls:

\[
\boxed{6.5\rightarrow5.5.}
\]

Therefore simply deleting the `STOP` token is insufficient.

The causal role that survives is the termination boundary supplied by the frozen refinement and value/cost contract.

---

## Earned result

Within this finite deterministic audited regime:

\[
\boxed{\textbf{primitive STOP is not necessary for the observed navigation behavior}.}
\]

The same behavior is recovered when termination is derived as the absence of a refinement continuation justified by the already-frozen reachability and value/cost contract.

The corresponding implementation-independent distinction is:

\[
\boxed{\textbf{termination token}\neq\textbf{termination discipline}.}
\]

The negative control shows that termination discipline still matters: removing the token without preserving the stopping role produces needless acquisition cost in B/C.

---

## Boundaries

This audit does not establish that:

- termination discipline is unnecessary;
- the derived rule is globally minimal;
- stopping can be learned without a supplied value/cost contract;
- the value function or cost model is itself necessary in its current form;
- Boolean reachability plus one-step fallback generalizes to stochastic or deeper systems;
- probe-space construction, geometry repair, basin opening, or research agency has occurred.

The result is restricted to the declared finite deterministic regime.

---

## Dependency update implied by this audit

The navigation substrate can now distinguish implementation from role more sharply:

\[
\boxed{\Pi_{\rm DP}\text{ removed}}
\]

and:

\[
\boxed{STOP_{\rm primitive}\text{ removed}}
\]

while the surviving functional requirements include:

\[
\boxed{\text{sequential correction-relevant refinement preservation}}
\]

and:

\[
\boxed{\text{termination discipline from the value/refinement contract}.}
\]

This audit does not yet claim a complete \(P_{\rm ep,min}\) certificate. The next repository step is to update the dependency map and then attack the remaining supplied experiment-selection substrate one component at a time.
