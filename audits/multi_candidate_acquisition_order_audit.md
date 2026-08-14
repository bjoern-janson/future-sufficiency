# Multi-Candidate Acquisition-Order Discriminant Audit — Results

## Provenance

Preregistered before execution at:

```text
c3816400ef6ffd61d02b3a5fceec2712de064357
```

Empirical valuation anchor:

```text
c97a5cfde0dba0052f63ab5636f574cd4c4d1f2e
```

No broader dependency ledger is updated by this result.

The new multi-candidate panel was executed in-session against the preregistered logic. The executable child audit imports the existing valuation-role audit, which in turn reruns the STOP/navigation regression when executed in-repo.

This connector session cannot launch a repository process, so the upstream regression is not claimed as freshly re-executed here. Instead, the previously audited result is inherited under unchanged source blobs and the child executable contains hard assertions for the full upstream certificate.

---

## 1. Frozen question

The preceding audit established only:

\[
\boxed{
e \succ_Q COMMIT\;?
}
\]

This audit asks whether that sign/threshold relation is sufficient when three worthwhile refinements are simultaneously admissible:

\[
\boxed{
\{e_1,e_2,e_3,COMMIT\}.
}
\]

The compared ladder is:

\[
\boxed{
Q^\bot
\rightarrow
Q^\bot+\text{Pareto}
\rightarrow
\text{compensated ordinal}
\rightarrow
\text{max-only tournament}
\rightarrow
q\text{-cardinal}.
}
\]

The environment, correction contract, candidate evidence partitions, normalized burden representation, and one-step commitment boundary are frozen.

---

## 2. Evaluator-side panel

The three evidence families have matched raw information:

\[
\boxed{
I(H)=I(M)=I(L)=1\text{ bit}
}
\]

while their correction relevance is:

\[
\boxed{
R_H=0.5,\qquad R_M=0.25,\qquad R_L=0.125.
}
\]

The reference margin is used only by the cardinal baseline:

\[
q_i=R_i-\kappa_i.
\]

The eight preregistered states evaluate to:

| State | Candidates `(R_corr, kappa, q)` | Optimal action set |
|---|---|---|
| P1 | H `(.500,.100,.400)`; M `(.250,.100,.150)`; L `(.125,.100,.025)` | `{H}` |
| P2 | M_a `(.250,.050,.200)`; M_b `(.250,.100,.150)`; M_c `(.250,.200,.050)` | `{M_a}` |
| P3 | H `(.500,.300,.200)`; M `(.250,.100,.150)`; L `(.125,.020,.105)` | `{H}` |
| P4 | H `(.500,.450,.050)`; M `(.250,.080,.170)`; L `(.125,.010,.115)` | `{M}` |
| P5 | H `(.500,.480,.020)`; M `(.250,.200,.050)`; L `(.125,.010,.115)` | `{L}` |
| P6 | H `(.500,.300,.200)`; M `(.250,.050,.200)`; L `(.125,.010,.115)` | `{H,M}` |
| P7 | H `(.500,.500,.000)`; M `(.250,.250,.000)`; L `(.125,.125,.000)` | `{COMMIT}` |
| P8 | H `(.500,.550,-.050)`; M `(.250,.100,.150)`; L `(.125,.200,-.075)` | `{M}` |

The P3/P4/P5 triplet rotates the winner across high-, medium-, and low-relevance probes while every candidate remains worthwhile and pairwise Pareto-incomparable.

---

## 3. Collision-derived ceilings

The impoverished representations were evaluated by exhaustive anonymous candidate permutations, not by selecting an arbitrary tie-break rule.

There are:

```text
8 panel states × 6 candidate permutations = 48 presentations
```

### Candidate-vs-COMMIT sign only

The best possible deterministic single-action accuracy from the sign signature is:

\[
\boxed{
26/48=13/24\approx0.5417.
}
\]

This reproduces the preregistered ceiling exactly.

Therefore:

\[
\boxed{
Q^\bot\text{ is insufficient for multi-candidate selection.}
}
\]

### Sign + Pareto partial order

Adding uncompensated dominance raises the best possible ceiling to:

\[
\boxed{
34/48=17/24\approx0.7083.
}
\]

Again this exactly matches the preregistration.

P1 and P2 become resolvable, but the crossing tradeoffs P3/P4/P5 remain structurally ambiguous.

Therefore:

\[
\boxed{
Q^\bot+\text{Pareto is still insufficient.}
}
\]

These are representation ceilings, not learner failures.

---

## 4. Action-set agreement across anonymous encodings

Across:

```text
64 anonymous encodings
8 panel states
512 encoded state evaluations
```

the exact optimal-action-set agreement is:

| Representation | Exact matches | Accuracy |
|---|---:|---:|
| sign only | 128 / 512 | 0.25 |
| sign + Pareto | 256 / 512 | 0.50 |
| derived compensated ordinal | 512 / 512 | **1.00** |
| max-only tournament | 512 / 512 | **1.00** |
| explicit cardinal `q` | 512 / 512 | **1.00** |

The lower exact-set figures for sign/Pareto are expected because those representations often expose a set of indistinguishable candidates rather than the true maximal set. Their best achievable single-action ceilings are the collision values above.

---

## 5. Compensated ordinal substitution

The derived comparator never stores numeric `q_i`.

It compares candidates through:

\[
R_i+\kappa_j
\quad\text{vs}\quad
R_j+\kappa_i,
\]

which is equivalent to testing:

\[
R_i-\kappa_i
\quad\text{vs}\quad
R_j-\kappa_j
\]

without materializing the cardinal margin vector.

It matches the explicit-cardinal reference on all 512 encoded states:

\[
\boxed{
0\text{ action-set mismatches}.
}
\]

Thus the explicit cardinal acquisition-margin representation is not necessary for these observed choices.

What survives is the compensated comparison relation.

---

## 6. Max-only tournament substitution

The stronger substitution does not retain a total ordering of candidates.

It processes candidates sequentially and keeps only the current co-maximal equivalence class. Losing relations are discarded.

The P6 tie requires retaining co-maximal candidates rather than imposing a semantic tie-break:

\[
\boxed{
Q(H)=Q(M)>Q(L).
}
\]

This is the minimal implementation clarification consistent with the preregistered requirement to compare optimal-action **sets**.

The tournament performs two candidate comparisons for each three-candidate state, then compares the surviving champion class against `COMMIT`.

It also achieves:

\[
\boxed{
512/512
}
\]

exact action-set matches.

Therefore, in this panel:

\[
\boxed{
\text{stored full ranking is not necessary}
}
\]

and:

\[
\boxed{
\text{explicit cardinal }q\text{ vector is not necessary}.
}
\]

The surviving role is narrower:

\[
\boxed{
\textbf{identify a currently maximal worthwhile refinement by on-demand compensated comparison.}
}
\]

---

## 7. Negative controls

A correction-relevance lexicographic rule fails:

```text
P2, P4, P5, P6
```

including the preregistered P4/P5 crossing cases.

A lowest-burden lexicographic rule fails:

```text
P1, P3, P4, P6
```

including P3.

So neither:

\[
\max R_{\rm corr}
\]

nor:

\[
\min\kappa
\]

can substitute for the compensated relation.

The crossing states are doing the intended causal work.

---

## 8. Candidate-identity invariance

For the three successful representations:

```text
derived compensated ordinal
max-only tournament
cardinal q reference
```

there are:

```text
0 anonymous-encoding mismatches
0 mismatches across all 48 exhaustive candidate permutations
```

Candidate identity therefore carries no decision authority in the successful result.

Raw output tokens and gate-state realizations are also permuted while preserving the evidence partitions and evaluator-derived relevance.

---

## 9. Specification-burden accounting

The anti-oracle rule remains:

\[
\boxed{
\text{behavioral substitution}\neq\text{substrate reduction}.
}
\]

| Representation | Target decisions supplied | Rank entries supplied | Persistent cardinal `q` | Comparison structure |
|---|---:|---:|---:|---|
| sign only | 0 | 0 | 0 | commit threshold only |
| sign + Pareto | 0 | 0 | 0 | uncompensated dominance |
| compensated ordinal | 0 | 0 | 0 | pairwise tradeoff relation derived from `R_corr,kappa` |
| max-only tournament | 0 | 0 | 0 | same comparator, on demand; only co-maximal class retained |
| cardinal baseline | 0 | 0 | 3 per state | explicit margins |
| order/winner table | direct/equivalent | direct | 0 | **oracle displacement** |

The tournament removes cardinal `q` storage and total-rank storage, but it does **not** reduce the externally supplied `R_corr` or `kappa` information.

Therefore this is a representation contraction, not a complete substrate-minimality certificate.

---

## 10. Upstream regression boundary

The child executable imports the valuation-role audit at `c97a5cf`, which itself imports and reruns the STOP-substitution audit.

The frozen contract remains:

```text
valuation encodings:                  64
candidate-vs-COMMIT decisions:       320
baseline vs kappa mismatches:          0

STOP encodings:                       64
visited navigation decisions:       3584
derived terminations:               1536
normalized trace mismatches:           0
```

At the current parent, the relevant source blobs remain unchanged:

```text
valuation_role_discriminant_audit.py  0afe6d1275975a5cbc6e85c07f0419c7b2c8d70e
stop_substitution_audit.py             cdb70de4d9bdc6c84f4d718c147612adfd49225b
```

This session executed the new multi-candidate core panel. It does not claim a fresh repository-process execution of the old upstream regressions; the committed executable reasserts them on every in-repo run.

---

## 11. Earned result

Within this finite deterministic panel:

\[
\boxed{
\textbf{
candidate-vs-COMMIT worth is insufficient when multiple worthwhile refinements compete.
}
}
\]

and:

\[
\boxed{
\textbf{
uncompensated Pareto dominance is insufficient when correction relevance and burden trade off.
}
}
\]

A compensated pairwise acquisition relation is sufficient:

\[
\boxed{
e_i\succ_Q e_j
\iff
R_i+\kappa_j>R_j+\kappa_i.
}
\]

But neither a stored full ranking nor explicit cardinal acquisition margins are required for the observed policy:

\[
\boxed{
\textbf{
on-demand max-only compensated comparison preserves the complete optimal-action correspondence.
}
}
\]

This contracts the live role from a generic multi-candidate “value ranking” to:

\[
\boxed{
\textbf{
choice-maximality under a compensated correction-relevance / burden comparison.
}
}
\]

---

## 12. Claim boundary

The audit does **not** establish:

\[
\boxed{
Q_{\rm acquire,min}.
}
\]

In particular, it does not establish that:

- cardinal `R_corr` is unnecessary;
- normalized burden `kappa` is unnecessary;
- the compensated comparator is globally minimal;
- the probe menu is generated rather than supplied;
- experiment accessibility has been minimized;
- experiment-space construction or basin opening has occurred.

The next dependency question, if pursued, is whether the compensated comparison itself can be weakened without oracle displacement.

No experiment-accessibility claim follows from this result.
