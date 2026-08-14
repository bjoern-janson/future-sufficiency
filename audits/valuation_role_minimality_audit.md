# Valuation-Role Minimality Audit — Results

## Provenance

Preregistered before execution at:

```text
faba1f247359ef89d514f73a25f84ada1222a1ff
```

Parent dependency checkpoint:

```text
44db372d221b2616218c9dba8d1bf4b7fe461a56
```

Empirical anchors:

```text
9a32f94  multi-candidate acquisition-order audit
c97a5cf  valuation-role discriminant audit
4694382  STOP-substitution audit
```

The new valuation-role-minimality panels were executed in-session against the preregistered logic. The committed executable imports and hard-asserts the full upstream regression chain when run in-repo.

This connector session does **not** claim a fresh end-to-end replay of the old audits. The correct provenance description is:

\[
\boxed{
\textbf{fresh valuation-role-minimality result with inherited hard regression assertions}.
}
\]

No broader theory file is changed by this result.

---

## 1. Frozen question

The audit independently attacks the two explicit valuation ingredients that remained after `9a32f94`:

\[
\boxed{R_{\rm corr},\;\kappa.}
\]

Everything else is held fixed at the role level:

\[
\boxed{
\mathfrak R_E,\;S_{\rm refine},\;Q_{\rm acquire}^{\rm role},\;T_{\rm stop},\;A_{\rm probe}.
}
\]

The surviving acquisition role remains:

\[
\boxed{
\text{identify a currently maximal worthwhile refinement by on-demand compensated comparison}.
}
\]

---

# Cut R — explicit correction relevance

## 2. Remove explicit `R_corr`

The substitute controller receives no `R_corr` field and no evidence-family label.

Instead it receives the already-frozen:

- evidence outcome partition;
- current posterior world set;
- correction contract;
- `kappa` burden.

For candidate `i`, it derives the post-evidence achievable correction count on demand:

\[
C_i^+
=
\sum_o\max_a|\{w:E_i(w)=o,\;a^\star(w)=a\}|.
\]

Candidate comparison is performed directly as:

\[
\boxed{
\frac{C_i^+}{N}+\kappa_j
>
\frac{C_j^+}{N}+\kappa_i
}
\]

without materializing `R_corr` or a cardinal `q` vector.

Against COMMIT:

\[
\boxed{
\frac{C_i^+}{N}>A_0+\kappa_i.
}
\]

### Result on the frozen P1–P8 multi-candidate panel

Across:

```text
64 anonymous encodings
8 panel states
512 encoded state evaluations
```

the no-explicit-`R_corr` comparator achieved:

\[
\boxed{512/512}.
\]

Therefore:

\[
\boxed{
\textbf{explicit controller-side }R_{\rm corr}\textbf{ is not necessary for the observed acquisition choices.}
}
\]

The correction-relevance **role** has not disappeared; it is derived from lower-level evidence consequences under the correction contract.

---

## 3. Contract-dependence mirror control

The mirror panel uses the same three balanced one-bit evidence partitions in both contexts:

```text
E0 = t0
E1 = t1
EN = nuisance
```

with the fixed conditional correction contract:

\[
a^\star_c(W)=t_c.
\]

The local evidence partitions and burden pattern are unchanged across contexts, but the warranted choice flips:

```text
c=0 -> E0
c=1 -> E1
```

The contract-aware consequence comparator achieved:

\[
\boxed{128/128}
\]

across 64 anonymous encodings × 2 contract contexts.

By contrast, the contract-blind representation receives the same local evidence/burden signature in the two mirrored worlds while different actions are required. Exhaustive candidate permutations produce the preregistered ceiling:

\[
\boxed{
6/12=1/2.
}
\]

Thus:

\[
\boxed{
\textbf{correction relevance is not intrinsic to the local evidence pattern; it remains grounded in the correction contract.}
}
\]

This prevents the successful `-R_corr` substitution from being misread as “evidence determines relevance by itself.”

---

## 4. What actually contracted in Cut R

The distinction between controller representation and external specification matters here.

The previous implementation already computed `R_corr` from evidence consequences before exposing the scalar to the controller. Therefore:

\[
\boxed{B_{\rm controller}\downarrow}
\]

because the explicit `R_corr` controller field disappears, but:

\[
\boxed{B_{\rm external}\not\downarrow}
\]

because no designer-supplied `R_corr` table existed to remove.

So Cut R earns a **representation/interface contraction**, not a new external-substrate reduction.

---

# Cut K — explicit acquisition burden

## 5. Burden-isolation panel

Correction consequences are fixed in every burden state:

\[
R_H=.5,\qquad R_M=.25,\qquad R_L=.125.
\]

The only manipulated quantity is acquisition burden.

| State | `kappa_H` | `kappa_M` | `kappa_L` | warranted action |
|---|---:|---:|---:|---|
| K1 | .300 | .100 | .020 | H |
| K2 | .450 | .080 | .010 | M |
| K3 | .480 | .200 | .010 | L |
| K4 | .550 | .300 | .150 | COMMIT |
| K5 | .550 | .350 | .270 | COMMIT |

In K1–K4 the burden ordering is always:

\[
\boxed{\kappa_H>\kappa_M>\kappa_L}
\]

while the warranted action rotates:

\[
\boxed{H\rightarrow M\rightarrow L\rightarrow COMMIT.}
\]

K5 is a constant burden shift of K1: the pairwise burden differences are identical to K1, but the absolute acquisition level pushes every candidate below COMMIT.

---

## 6. No burden: exact collision ceiling

With `kappa` removed entirely, the correction-consequence representation is identical across K1–K4 while four different actions are required.

Exhaustive anonymous candidate permutations give:

\[
\boxed{
6/24=1/4.
}
\]

A natural relevance-only chooser performs even more visibly badly over K1–K5:

```text
64 / 320 exact choices = 0.20
```

It is wrong on every encoding of:

```text
K2
K3
K4
K5
```

In K4/K5 it purchases correction-relevant evidence even though COMMIT is warranted.

Thus the preregistered failure signature occurs:

\[
\boxed{
-\kappa
\rightarrow
\text{over-purchase of useful-but-not-worthwhile evidence}.
}
\]

---

## 7. Burden order only is still insufficient

Retaining only:

\[
\kappa_H>\kappa_M>\kappa_L
\]

does not resolve the K1–K4 collision.

The best deterministic ceiling remains:

\[
\boxed{1/4.}
\]

Therefore:

\[
\boxed{
\text{ordinal burden}
\neq
\text{sufficient acquisition-burden structure}.
}
\]

The relevant role depends on burden magnitude, not merely on which candidate is cheaper.

---

## 8. Relative burden differences still miss the stopping anchor

K1 and K5 have identical pairwise burden differences:

\[
(.20,.28,.08)
\]

but require:

```text
K1 -> H
K5 -> COMMIT
```

A representation containing correction consequences plus pairwise burden differences, but no absolute burden anchor, therefore collides on K1/K5.

Across K1–K5, its exact best deterministic ceiling is:

\[
\boxed{
24/30=4/5.
}
\]

This earns the narrower distinction:

\[
\boxed{
\text{relative burden among probes}
\neq
\text{burden anchored to the COMMIT boundary}.
}
\]

---

## 9. Full anchored burden reference

The existing quantitative `kappa` representation, used through the already-earned on-demand compensated comparator, achieves:

\[
\boxed{320/320}
\]

across:

```text
64 anonymous encodings
5 burden states
```

This establishes sufficiency, not unique necessity of the literal symbol `kappa`.

The strongest dependency statement earned is:

\[
\boxed{
\textbf{some quantitative acquisition-burden information anchored to COMMIT remains necessary in the tested language family and frozen substrate.}
}
\]

The audit does **not** establish that no alternative encoding of that burden could ever replace `kappa`.

---

## 10. Specification accounting

| Representation | explicit `R_corr` | explicit `kappa` | new target/rank fields | external reduction | result |
|---|---:|---:|---:|---|---|
| current reference | yes, derived | yes | 0 | reference | sufficient |
| contract-grounded consequence comparator | no | yes | 0 | external unchanged | **512/512** |
| contract-blind local consequence structure | no | yes | 0 | external unchanged | ceiling **1/2** on mirror |
| no burden | consequence-derived | no | 0 | yes | ceiling **1/4** |
| burden order only | consequence-derived | no magnitudes | 0 | reduced diagnostic | ceiling **1/4** |
| pairwise burden differences only | consequence-derived | no absolute level | 0 | removes absolute anchor | ceiling **4/5** |
| anchored quantitative `kappa` | consequence-derived | yes | 0 | current burden spec | **320/320** |
| winner/rank table | arbitrary | arbitrary | direct | oracle displacement | invalid |

The anti-scaffold result is therefore asymmetric:

- removing explicit `R_corr` shrinks the controller interface but does not reduce external designer specification;
- removing external burden information really would reduce external specification, but the tested reductions fail.

---

## 11. Earned contraction

Before this audit, the live valuation ingredients were represented as:

\[
(R_{\rm corr},\kappa).
\]

Cut R contracts the first term from an explicit scalar field to a derived relation grounded directly in evidence consequences plus the frozen correction contract:

\[
\boxed{
R_{\rm corr}^{\rm explicit}
\downarrow
}
\]

while preserving:

\[
\boxed{
\text{contract-grounded corrective consequence comparison}.
}
\]

Cut K does **not** eliminate acquisition burden. The surviving burden role is more specific than generic “cost”:

\[
\boxed{
\textbf{quantitative acquisition burden on a scale anchored to COMMIT.}
}
\]

So the current valuation role can be described operationally as:

\[
\boxed{
\textbf{identify the maximal worthwhile refinement by comparing contract-derived corrective consequence against anchored acquisition burden.}
}
\]

This is a role-level compression, not a new theory object.

---

## 12. Upstream regression boundary

The child executable imports `multi_candidate_acquisition_order_audit.audit()`, which recursively reasserts the earlier valuation and STOP/navigation certificates.

The hard contract remains:

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

Those old audits were not freshly process-executed in this connector session. The new Cut R/Cut K panels were freshly executed; upstream behavior is inherited under unchanged code and hard assertions.

---

## 13. Claim boundary

The audit does **not** establish:

\[
P_{\rm ep,min}.
\]

It does not establish that:

- the correction contract can be removed;
- evidence semantics can be removed;
- the literal `kappa` scalar is uniquely necessary;
- a lower-level resource-transition representation could not replace `kappa` in a future audit;
- `A_probe` has been minimized;
- experiment-space construction or basin opening has occurred.

The probe menu and refinement geometry remain frozen.

The next repository action authorized by the preregistered sequence is only to update `P_EP_DEPENDENCY_CONSOLIDATION.md` with these results.
