# Valuation-Role Minimality Audit — Preregistration

## Status

This document freezes the next experiment-planning dependency cut **before execution**.

Parent dependency checkpoint:

```text
44db372  Update experiment-planning dependency consolidation
```

Empirical valuation anchors:

```text
c97a5cf  valuation-role discriminant audit
9a32f94  multi-candidate acquisition-order audit
```

No empirical results are recorded here.

The current surviving acquisition role is:

\[
\boxed{
Q_{\rm acquire}^{\rm role}
=
\text{identify a currently maximal worthwhile refinement by on-demand compensated comparison}.
}
\]

The two remaining supplied valuation ingredients are:

\[
\boxed{R_{\rm corr},\;\kappa.}
\]

The audit asks whether either explicit representation can be weakened or removed without moving the same information into an oracle.

---

## 1. Scientific question

The audit targets:

\[
\boxed{(R_{\rm corr},\kappa)\rightarrow Q'}
\]

while holding fixed:

\[
\boxed{
\mathfrak R_E,\;S_{\rm refine},\;Q_{\rm acquire}^{\rm role},\;T_{\rm stop},\;A_{\rm probe},\;\Pi_{\mathcal P},\;\tau.
}
\]

The two valuation factors are ablated **independently**.

### Cut R — explicit correction relevance

Remove the explicit controller-side scalar `R_corr` while leaving acquisition burden available.

Question:

> Can the required compensated comparison be derived on demand from the already-frozen evidence partitions plus the frozen correction contract, without materializing or supplying `R_corr`?

### Cut K — explicit acquisition burden

Remove explicit `kappa` while leaving correction consequences available.

Question:

> Can maximal-choice behavior survive with weaker burden information, or does the policy require quantitative acquisition burden anchored to the COMMIT boundary?

A joint failure is not sufficient evidence for either dependency; the cuts must remain separable.

---

## 2. Anti-oracle / specification rule

The governing rule is:

\[
\boxed{
\text{behavioral substitution}\neq\text{substrate reduction}.
}
\]

Invalid substitutes include:

```text
candidate -> relevant
candidate -> worth it
candidate -> winner
per-state rank table
precomputed pairwise Q table
```

A successful substitute must be generated from less explicitly represented valuation structure.

The audit reports two burdens separately:

1. **controller-interface burden** — explicit valuation fields presented to the acquisition controller;
2. **external specification burden** — designer-supplied information beyond the already-frozen evidence semantics, correction contract, and action topology.

This distinction matters because the current code already *derives* `R_corr` from evidence consequences before passing it to the controller. Removing that scalar can therefore be a real representation/interface contraction without necessarily reducing external designer specification.

No result may claim:

\[
B_{\rm external}\downarrow
\]

unless external supplied information actually decreases.

---

# Part I — Cut R: remove explicit `R_corr`

## 3. Frozen reference behavior

Reuse the eight-state multi-candidate panel from `9a32f94` unchanged.

For each candidate, the reference implementation currently exposes:

```text
correction_relevance = post-evidence Bayes accuracy - current Bayes accuracy
kappa               = normalized acquisition burden
```

and the successful max-only comparison uses the equivalent relation:

\[
e_i\succ_Q e_j
\iff
R_i+\kappa_j>R_j+\kappa_i.
\]

The target optimal-action correspondence P1–P8 remains exactly the one frozen at `9a32f94`.

---

## 4. R0 — explicit-`R_corr` reference

Reference only.

Each candidate carries explicit:

\[
(R_i,\kappa_i).
\]

No necessity claim follows from reference success.

---

## 5. R1 — contract-grounded consequence comparator

Remove the explicit `R_corr` field from the controller interface.

The replacement receives only:

- the candidate's actual evidence partition / outcome mapping;
- the current posterior world set;
- the frozen correction contract `a*(w)`;
- the candidate's `kappa` burden.

For candidate `i`, compute on demand the post-evidence achievable correction count:

\[
C_i^+
=
\sum_o \max_a |\{w:E_i(w)=o,\;a^\star(w)=a\}|.
\]

Let `N` be the current world count. Then pairwise comparison can be performed without materializing `R_corr`:

\[
\boxed{
\frac{C_i^+}{N}+\kappa_j
>
\frac{C_j^+}{N}+\kappa_i.
}
\]

The current Bayes accuracy cancels from candidate-vs-candidate comparison.

For comparison with COMMIT, use:

\[
\boxed{
\frac{C_i^+}{N}
>
A_0+\kappa_i,
}
\]

where `A0` is derived from the same frozen correction contract and current posterior.

The controller must not:

- materialize persistent `R_corr` values;
- receive evidence-family labels such as `H`, `M`, `L`;
- receive target winners or ranks.

### Preregistered prediction

The consequence comparator should reproduce the `9a32f94` maximal action set on all anonymous encodings:

\[
\boxed{512/512.}
\]

If it does, the strongest allowed claim is:

\[
\boxed{
\text{explicit controller-side }R_{\rm corr}\text{ is implementation-contingent for this behavior.}
}
\]

This does **not** establish that correction relevance as a functional relation has disappeared.

---

## 6. Contract-dependence mirror control

The audit must also show that correction relevance is not an intrinsic property of a local evidence pattern.

Use a fixed conditional correction contract over worlds:

\[
W=(t_0,t_1,n)\in\{0,1\}^3,
\]

with observed contract context `c in {0,1}` and:

\[
\boxed{a^\star_c(W)=t_c.}
\]

Present the same three balanced one-bit evidence partitions in both contexts:

```text
E0 = t0
E1 = t1
EN = n
```

with matched burdens:

```text
kappa(E0) = 0.10
kappa(E1) = 0.10
kappa(EN) = 0.01
```

All three carry one raw bit. The evidence partitions and burden pattern are identical across the two contexts.

But the warranted choice flips only because of the frozen correction contract:

```text
context c=0 -> choose E0
context c=1 -> choose E1
```

### R-negative control: contract-blind local consequence structure

A representation that sees the evidence partitions and burdens but not the correction contract/context-to-target mapping receives an identical valuation signature in the two mirror states while the target choice differs.

Under uniform mirror contexts and anonymous candidate permutations, its best deterministic choice ceiling is preregistered as:

\[
\boxed{1/2.}
\]

The implementation must derive this from representation collisions, not hard-code the number.

### Interpretation

If the contract-grounded comparator succeeds while the contract-blind representation hits the ceiling, the earned result is:

\[
\boxed{
\text{explicit }R_{\rm corr}\text{ scalar is unnecessary, but correction relevance remains contract-grounded.}
}
\]

Do **not** infer that evidence alone determines relevance.

---

# Part II — Cut K: remove explicit `kappa`

## 7. Burden-isolation panel

Hold correction consequences fixed across the burden states.

Use three candidates with the same correction-relevance vector in every state:

\[
\boxed{
R_H=0.5,\quad R_M=0.25,\quad R_L=0.125.
}
\]

Use the following burden states:

### K1 — high-relevance candidate wins

```text
candidate   R_corr   kappa   q
H           .500     .300    .200
M           .250     .100    .150
L           .125     .020    .105
```

Target: `{H}`.

### K2 — medium-relevance candidate wins

```text
H           .500     .450    .050
M           .250     .080    .170
L           .125     .010    .115
```

Target: `{M}`.

### K3 — low-relevance candidate wins

```text
H           .500     .480    .020
M           .250     .200    .050
L           .125     .010    .115
```

Target: `{L}`.

### K4 — all useful evidence is too expensive

```text
H           .500     .550   -.050
M           .250     .300   -.050
L           .125     .150   -.025
```

Target: `{COMMIT}`.

Across K1–K4:

- correction relevance is identical;
- raw evidence semantics are identical;
- burden order is identical:

\[
\boxed{\kappa_H>\kappa_M>\kappa_L;}
\]

- but the warranted next action rotates:

\[
\boxed{H\rightarrow M\rightarrow L\rightarrow COMMIT.}
\]

This is the primary burden-magnitude discriminant.

---

## 8. K0 — no burden representation

Remove `kappa` entirely while preserving the correction consequences.

Any deterministic anonymous policy based only on the fixed correction-relevance pattern receives the same representation in K1–K4 while four different choices are required.

Preregistered best-choice ceiling:

\[
\boxed{1/4.}
\]

Failure is expected to include over-purchase in K4:

\[
\boxed{
-\kappa
\rightarrow
\text{acquire correction-relevant evidence even when COMMIT is warranted}.
}
\]

---

## 9. K1-language — burden order only

Retain only the ordinal burden relation:

\[
\kappa_H>\kappa_M>\kappa_L
\]

without magnitudes.

Because this ordering is identical in K1–K4, the same collision remains.

Preregistered ceiling:

\[
\boxed{1/4.}
\]

Thus a failure would localize the need for more than `cheap < expensive` ordering.

A supplied per-state burden rank table is not a valid reduction if it simply relocates the original `kappa` values; this representation is evaluated only as an impoverished-language diagnostic.

---

## 10. K2-language — relative burden differences without absolute anchor

Add a fifth state:

### K5 — constant burden shift of K1

```text
candidate   R_corr   kappa   q
H           .500     .550   -.050
M           .250     .350   -.100
L           .125     .270   -.145
```

Target: `{COMMIT}`.

K1 and K5 have exactly the same pairwise burden differences:

\[
\boxed{
\kappa_H-\kappa_M=.20,\quad
\kappa_H-\kappa_L=.28,\quad
\kappa_M-\kappa_L=.08.
}
\]

Yet their required actions differ:

```text
K1 -> H
K5 -> COMMIT
```

Therefore a representation containing only relative burden differences cannot determine the absolute acquisition boundary against COMMIT.

Across K1–K5, the preregistered best deterministic ceiling for `(R_corr + pairwise kappa differences)` is:

\[
\boxed{4/5.}
\]

The implementation must derive this from collisions.

This distinguishes:

\[
\boxed{
\text{relative burden among probes}
\neq
\text{burden anchored to the stopping boundary}.
}
\]

---

## 11. K3 — quantitative anchored burden reference

The existing `kappa` representation remains the behavioral reference:

\[
q_i=R_i-\kappa_i,
\]

or its previously earned on-demand compensated equivalent.

Preregistered target:

\[
\boxed{1.0}
\]

on K1–K5.

The audit does **not** preregister the literal symbol `kappa` as uniquely necessary. The strongest result available from failure of K0/K1/K2 is narrower:

\[
\boxed{
\text{some quantitative acquisition-burden information anchored to COMMIT remains necessary in the tested language family and frozen substrate.}
}
\]

A future alternative encoding could still replace `kappa` if it carries less external specification and preserves behavior.

---

## 12. Why raw `C` or a hidden table is not an accepted substitute

Replacing `kappa=C/V` with separate `(C,V)` merely reverses the contraction already earned at `c97a5cf` and does not reduce external specification.

Likewise, supplying:

- exact pairwise compensated answers;
- candidate affordability labels;
- target winners;
- per-state policy tables;

counts as oracle displacement.

If a lower-level action/resource consequence representation is introduced in the future, its specification burden must be counted. This audit does not modify `A_probe` or the refinement transition dynamics merely to manufacture a new source for burden values.

---

## 13. Anonymous encoding / invariance requirements

Run at least 64 anonymous encodings.

Across both cuts:

- permute candidate identifiers and presentation order;
- flip binary evidence-output tokens;
- permute latent gate/state labels where applicable;
- expose no `H/M/L`, `t0/t1`, `relevant`, `cheap`, or winner labels to controllers;
- compare optimal-action **sets**, preserving ties.

Successful behavior must be invariant to these encodings.

---

## 14. Upstream regression boundary

The executable child audit must import and reassert the complete `9a32f94` audit, which itself imports the earlier valuation and STOP/navigation certificates.

Required inherited assertions include:

```text
multi-candidate:
  64 anonymous encodings
  512 encoded state evaluations
  compensated ordinal 512/512
  max-only tournament  512/512
  cardinal reference   512/512
  sign-only ceiling     13/24
  Pareto ceiling        17/24

candidate-vs-COMMIT:
  64 anonymous encodings
  320 decisions
  baseline vs kappa mismatches 0

STOP/navigation:
  64 anonymous encodings
  3584 visited decision points
  1536 derived terminations
  0 normalized trace mismatches
```

If any inherited assertion changes, reject valuation-role-minimality attribution.

In a connector-only execution session, distinguish freshly executed new panels from inherited hard assertions exactly as in the prior provenance discipline.

---

## 15. Specification ledger required in results

At minimum report:

| Representation | Explicit `R_corr` fields | Explicit `kappa` fields | Added target/rank fields | External new valuation specification | Interpretation |
|---|---:|---:|---:|---:|---|
| current reference | yes | yes | 0 | `kappa` supplied; `R_corr` derived | reference |
| contract-grounded consequence comparator | 0 | yes | 0 | none beyond frozen partitions + contract | representation/interface contraction if successful |
| contract-blind consequence structure | 0 | yes | 0 | none | diagnostic; expected insufficient |
| no burden | derived or explicit correction consequence | 0 | 0 | lower | valid ablation; expected insufficient |
| burden order only | correction consequence | no magnitudes | 0 | reduced/diagnostic | expected insufficient |
| pairwise burden differences only | correction consequence | no absolute levels | 0 | relative burden magnitudes only | expected insufficient at COMMIT shift |
| full `kappa` reference | correction consequence | yes | 0 | current burden specification | behavioral reference |
| winner/rank table | arbitrary | arbitrary | direct | oracle displacement | invalid minimality evidence |

The results must state separately whether `B_controller` and `B_external` decrease.

---

## 16. Frozen interpretation rules

| Result | Allowed interpretation |
|---|---|
| consequence comparator matches all prior choices | explicit `R_corr` scalar is not necessary as a controller representation |
| contract-blind mirror ceiling = 1/2 | relevance is not recoverable from local evidence structure without the correction contract |
| no-burden ceiling = 1/4 on K1–K4 | correction relevance alone cannot determine acquisition choice |
| burden-order ceiling = 1/4 | ordinal burden alone is insufficient |
| relative-difference ceiling = 4/5 on K1–K5 | relative probe burden is insufficient without an absolute COMMIT anchor |
| full `kappa` reference = 1.0 | quantitative anchored burden remains sufficient, not uniquely necessary |
| supplied winner/rank table succeeds | oracle displacement; no substrate claim |
| upstream regression changes | reject attribution |
| candidate identity affects results | leakage / invalid audit |

If Cut R succeeds and Cut K fails as preregistered, the candidate contraction is:

\[
\boxed{
\text{explicit }R_{\rm corr}
\downarrow
\quad\land\quad
\text{contract-grounded correction consequence survives}
}
\]

while:

\[
\boxed{
\text{quantitative acquisition burden anchored to COMMIT remains a live dependency.}
}
\]

Do not rewrite that as `kappa` being universally or uniquely necessary.

---

## 17. Claim boundary

A successful Cut R does **not** remove the correction contract, evidence semantics, or consequence computation.

A failed Cut K does **not** prove that the literal `kappa` scalar is the only valid burden representation.

Neither result establishes:

- `P_ep,min`;
- experiment-accessibility minimality;
- experiment-space construction;
- basin opening;
- unrestricted ontology or value invention.

The probe menu remains frozen throughout.

No broader theory note is authorized by this audit.

---

## 18. Repository sequence

The authorized sequence is:

\[
\boxed{
\text{preregister}
\rightarrow
\text{execute}
\rightarrow
\text{update only the }P_{\rm ep}\text{ consolidation ledger}.
}
\]

The ledger update must occur only after results exist.
