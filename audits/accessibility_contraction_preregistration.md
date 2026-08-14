# Accessibility Contraction Audit — Preregistration

## Status

This document freezes the next experiment-planning dependency cut **before execution**.

Parent dependency checkpoint:

```text
309f7dd  Update experiment-planning dependency consolidation after valuation-role minimality
```

Empirical anchors remain:

```text
b7c068b  valuation-role minimality audit
9a32f94  multi-candidate acquisition-order audit
4694382  STOP-substitution audit
```

No empirical results are recorded here.

The valuation phase is treated as parked. The present audit targets only the accessibility component that has remained supplied:

\[
\boxed{A_{\rm probe}.}
\]

The scientific question is:

\[
\boxed{
\textbf{How little designer-supplied access structure is required to make already-defined decision-relevant refinements reachable?}
}
\]

This is **not** an experiment-space-construction audit. No new evidence operator may be invented, composed, repaired, or added to the latent experiment universe.

---

## 1. Frozen causal boundary

Freeze the latent refinement universe:

\[
\boxed{\mathcal E^\star=\{e_1,\ldots,e_n\}}
\]

and hold fixed across every compared access interface:

\[
\boxed{
\mathfrak R_E,\;S_{\rm refine},\;Q_{\rm acquire}^{\rm role},\;T_{\rm stop},\;\Pi_{\mathcal P},\;\tau.
}
\]

Also freeze:

- every probe's evidence partition / semantics;
- every probe's acquisition burden;
- the correction contract;
- the valuation comparator earned in the valuation branch;
- the commitment rule;
- the latent registry itself.

The only intervention is:

\[
\boxed{A_{\rm explicit}\rightarrow A_{\rm reduced}.}
\]

A valid accessibility contraction must preserve the same latent probes. Changing \(\mathcal E^\star\) invalidates attribution.

---

## 2. Separate latent experiment specification from access specification

The audit distinguishes two externally supplied burdens:

\[
\boxed{
B_{\rm total}
=
B_{\mathcal E^\star}
+
B_{\rm access}.
}
\]

Here:

- \(B_{\mathcal E^\star}\) is the fixed specification of the latent probe universe and its semantics;
- \(B_{\rm access}\) is the additional structure required to make members of that already-defined universe available to the chooser.

This audit freezes:

\[
\boxed{B_{\mathcal E^\star}=\text{constant}.}
\]

Therefore any success can establish only an **accessibility contraction**. It cannot establish experiment-space construction or reduction of the latent experiment ontology itself.

---

## 3. Access-burden ledger

Use the following finite supplied-structure ledger:

\[
\boxed{
B_{\rm access}
=
B_{\rm menu}
+B_{\rm generator}
+B_{\rm grammar}
+B_{\rm semantic\ hints}
+B_{\rm search\ constraints}.
}
\]

These are counts of designer-supplied structural clauses for this finite audit, **not** universal bits, MDL, or Kolmogorov complexity.

Every execution must report the full vector:

```text
(menu, generator, grammar, semantic_hints, search_constraints)
```

as well as the finite clause sum.

A claimed contraction requires:

1. lower total supplied clause count than the explicit-menu reference;
2. no target-specific winner/rank entries;
3. no semantic hints identifying which latent probe is correction-relevant;
4. no new grammar that changes or enlarges \(\mathcal E^\star\);
5. preserved reachability and downstream choice for the same relevant probes.

A lower visible menu count alone is insufficient.

---

## 4. Frozen latent universe

Use four independent latent bits:

\[
X=(x_1,x_2,x_3,x_4)\in\{0,1\}^4
\]

under the uniform world distribution.

Define one latent probe for every nonzero mask:

\[
m\in\{0,1\}^4\setminus\{0000\}.
\]

The fixed latent experiment universe is:

\[
\boxed{
\mathcal E^\star
=\{e_m:m\neq0000\},
\qquad
|\mathcal E^\star|=15.
}
\]

Each probe is the one-bit parity experiment:

\[
\boxed{
e_m(X)=m\cdot X\pmod 2.}
\]

The 15 probes and these semantics exist identically under every access condition. No controller may add a mask, combine masks, alter the parity operator, or synthesize a new probe.

All probe identities presented to the controller are opaque.

---

## 5. Frozen correction contexts

Use 15 anonymous correction contexts, one for each nonzero mask.

For context \(c_m\), the warranted terminal correction is:

\[
\boxed{a^\star_{c_m}(X)=m\cdot X\pmod 2.}
\]

Before evidence acquisition:

\[
\operatorname{BayesAcc}(a^\star)=0.5.
\]

Under the uniform four-bit world:

- probe \(e_m\) reveals the target exactly in context \(c_m\);
- every distinct nonzero parity \(e_{m'}\), \(m'\neq m\), is independent of the target parity.

Therefore, in context \(c_m\):

\[
\boxed{
R_{\rm corr}(e_m)=0.5,
\qquad
R_{\rm corr}(e_{m'})=0\quad(m'\neq m).
}
\]

Every latent probe carries exactly one raw information bit:

\[
\boxed{I(e_m)=1\text{ bit for all }m.}
\]

Assign the same fixed anchored acquisition burden to every probe:

\[
\boxed{\kappa(e_m)=0.1.}
\]

Thus, if the target probe is accessible, the already-frozen valuation role has a unique warranted choice:

\[
\boxed{e_m.}
\]

If the target probe is inaccessible, every accessible alternative has zero correction consequence and positive burden, so the frozen valuation/termination machinery correctly returns:

\[
\boxed{COMMIT.}
\]

This creates the desired localization:

\[
\boxed{
\text{target refinement exists}
\land
\text{valuation would select it if exposed}
\land
\text{access may fail to expose it}.
}
\]

---

## 6. Reference access interface A0 — explicit menu

The explicit reference exposes all 15 opaque probe handles simultaneously.

No semantic labels, mask labels, or target hints are supplied.

Finite access ledger:

```text
B_menu               = 15
B_generator          = 0
B_grammar            = 0
B_semantic_hints     = 0
B_search_constraints = 0
--------------------------------
B_access clauses     = 15
```

Preregistered target:

\[
\boxed{
\operatorname{Reach}_{A0}(e_m\mid c_m)=1
\quad\forall m
}
\]

and exact downstream selection in all contexts / encodings.

This is a behavioral reference, not a presumed minimum.

---

## 7. Primary substitution A1 — target-blind latent-registry wildcard

Replace the 15 explicit exposure clauses with one generic access rule:

```text
ALL_REGISTRY:
    expose every handle already present in the frozen latent experiment registry
```

The rule receives no correction context, no target mask, no semantic labels, and no winner information.

It does not generate new probes. It only enumerates members of the already-fixed \(\mathcal E^\star\).

Finite access ledger:

```text
B_menu               = 0
B_generator          = 1    # generic ALL_REGISTRY exposure rule
B_grammar            = 0
B_semantic_hints     = 0
B_search_constraints = 0
--------------------------------
B_access clauses     = 1
```

The candidate stream order must be anonymous/permuted. The frozen max-only valuation role processes candidates without storing a full ranking.

### Preregistered success condition

Across 64 anonymous encodings × 15 correction contexts:

\[
\boxed{960\text{ context-encoding evaluations}.}
\]

A1 should satisfy:

\[
\boxed{
\operatorname{Reach}_{A1}(e_m\mid c_m)=1
\quad\forall m
}
\]

and:

\[
\boxed{
\operatorname{Choice}_{A1}
=
\operatorname{Choice}_{A0}
\quad 960/960.
}
\]

If so, the finite access ledger contracts from 15 explicit exposure clauses to one generic target-blind access clause while the latent experiment specification is unchanged.

The strongest permitted claim is:

\[
\boxed{
\textbf{An explicit per-probe menu is not necessary for complete accessibility of this fixed finite latent experiment universe; a generic target-blind registry-access rule preserves reachability and downstream choice.}
}
\]

This does **not** establish that generic registry access is globally minimal.

---

## 8. Negative control A2 — no access path

Remove every access rule.

```text
B_access = 0
```

No latent probe can be exposed.

Preregistered target:

\[
\boxed{
\operatorname{Reach}_{A2}(e_m\mid c_m)=0
\quad\forall m.
}
\]

Since every context requires acquiring its unique target probe under A0, exact downstream agreement should be:

\[
\boxed{0/960.}
\]

This control establishes that access machinery has not disappeared merely because the latent probes exist.

---

## 9. Negative control A3 — target-blind partial registry exposure

Use the same generic registry mechanism but constrain it to the first seven opaque handles in the anonymous registry order:

```text
FIRST_7_REGISTRY
```

The access rule remains target-blind.

Finite ledger:

```text
B_menu               = 0
B_generator          = 1
B_grammar            = 0
B_semantic_hints     = 0
B_search_constraints = 1    # stop after seven handles
--------------------------------
B_access clauses     = 2
```

For each encoding, exactly seven of the 15 latent probes are reachable.

Because all 15 correction contexts are evaluated uniformly, the accessibility ceiling is determined by coverage rather than learner quality:

\[
\boxed{
\operatorname{ReachRate}(A3)=\frac7{15}.
}
\]

The preregistered exact-choice ceiling is therefore:

\[
\boxed{
\frac7{15}
=
\frac{448}{960}.
}
\]

In the remaining contexts, the correct target probe exists in \(\mathcal E^\star\) and would be selected if exposed, but the access interface cannot present it.

This is the primary failure localization:

\[
\boxed{
\text{exists}
\land
\text{valuable/selectable}
\land
\text{inaccessible}.
}
\]

---

## 10. Anti-scaffold control A4 — contract-to-probe hint lookup

Construct a superficially tiny visible menu by exposing only the target probe for each correction context.

Operationally:

```text
TARGET_LOOKUP(context) -> opaque target handle
```

This can reproduce 960/960 choices, but it requires a context-to-target mapping with one target-specific semantic entry per correction context.

Finite ledger:

```text
B_menu               = 0
B_generator          = 1
B_grammar            = 0
B_semantic_hints     = 15   # context -> target handle
B_search_constraints = 0
--------------------------------
B_access clauses     = 16
```

This is preregistered as:

\[
\boxed{\text{oracle displacement}.}
\]

Its behavioral success cannot support an accessibility-contraction claim because the experiment designer has simply moved into the access rule.

Any equivalent target/winner/rank lookup is invalid for minimality.

---

## 11. Why no richer grammar is introduced

The present audit intentionally does **not** replace the menu with a compositional experiment grammar.

A grammar that can form parity probes would risk changing the scientific question from:

\[
\text{access existing probe}
\]

to:

\[
\text{construct probe description}.
\]

That belongs to the later experiment-space-construction branch.

For this audit:

\[
\boxed{B_{\rm grammar}=0}
\]

for all primary interfaces.

The only valid generator in A1/A3 is a generic enumerator over the already-frozen registry.

---

## 12. Anonymous encoding requirements

Run at least 64 anonymous encodings.

For each encoding:

- randomly permute the mapping from the 15 latent parity probes to opaque handles;
- randomly permute registry iteration order;
- independently flip each probe's binary output token;
- permute the 15 correction-context identifiers;
- preserve only the underlying probe partition, correction contract, and burden;
- never expose mask names, parity descriptions, `target`, `relevant`, `best`, or equivalent semantic labels.

A successful access interface must remain invariant to these renamings.

---

## 13. Frozen downstream valuation contract

Accessibility is evaluated upstream of the already-earned valuation role.

Once a candidate is exposed, downstream selection is frozen as:

\[
\boxed{
\text{contract-derived corrective consequence}
+
\text{COMMIT-anchored quantitative burden}
\rightarrow
\text{current maximal worthwhile refinement}.
}
\]

No new valuation field, ranking table, stronger planner, or target-specific heuristic may be introduced.

The access audit must report both:

1. target-probe reachability;
2. downstream action agreement conditional on the accessible candidate set.

Terminal action alone is not an adequate accessibility endpoint.

---

## 14. Upstream regression boundary

The executable child audit must reassert the frozen upstream certificates through hard assertions.

At minimum:

### Valuation-role minimality

```text
Cut R:
  512/512 no-explicit-R_corr choices
  contract-blind mirror ceiling 1/2

Cut K:
  anchored burden 320/320
  no-burden ceiling 1/4
  burden-order ceiling 1/4
  relative-difference ceiling 4/5
```

### Multi-candidate valuation

```text
512 encoded states
max-only 512/512
sign-only ceiling 13/24
Pareto ceiling 17/24
```

### STOP/navigation

```text
3584 visited decision points
1536 derived terminations
0 normalized trajectory mismatches
```

If any upstream assertion changes, reject attribution to accessibility.

As in the recent connector executions, a new accessibility-panel run may be fresh while older audits remain inherited hard assertions unless a true repository-process replay is performed.

---

## 15. Primary endpoints

A valid execution must report:

1. exact latent universe size and semantics checksum / invariant;
2. proof that \(\mathcal E^\star\) is identical across A0–A4;
3. per-context target-probe reachability;
4. exact downstream choice agreement;
5. candidate-identity invariance;
6. the full access-burden vector for every interface;
7. finite structural-clause sum for every interface;
8. no-access failure rate;
9. partial-access coverage ceiling and observed agreement;
10. oracle-displacement classification for A4;
11. upstream hard-regression status.

---

## 16. Frozen interpretation rules

| Result | Interpretation |
|---|---|
| A1 reaches all 15 target probes and matches A0 while `B_access` falls 15 -> 1 | explicit per-probe menu is contingent; generic registry access preserves accessibility in this fixed universe |
| A2 fails despite all probes existing latently | existence of experiments does not imply accessibility |
| A3 matches exactly `7/15` reachability/choice ceiling | failure localizes to inaccessible target probes, not valuation/inference |
| A4 reproduces behavior but uses 15 context-to-target hints | oracle displacement; no minimality claim |
| A1 changes probe semantics or latent universe | invalid; experiment construction leaked into accessibility intervention |
| A1 requires a richer experiment grammar | invalid for this audit; move to later construction branch |
| upstream regression changes | intervention leaked downstream; reject attribution |
| access ledger decreases only by hiding structure in another component | no contraction claim |

---

## 17. Candidate claim if preregistered prediction holds

If A1 preserves reachability and choice while A2/A3 fail as predicted and A4 is correctly rejected as oracle displacement, the strongest candidate claim is:

\[
\boxed{
\textbf{In this finite audited regime, explicit enumeration of a fixed latent probe menu is not necessary for complete experiment accessibility; a single target-blind access rule over the unchanged latent registry preserves reachability of every decision-relevant refinement and downstream choice.}
}
\]

The complementary dependency claim is:

\[
\boxed{
\textbf{Latent existence of a decision-relevant refinement is insufficient when the access interface cannot expose it.}
}
\]

The audit does **not** establish:

- that the generic registry-access primitive is minimal;
- that the latent probe registry is unnecessary;
- that probe semantics are generated rather than supplied;
- that the experiment ontology has been compressed;
- that novel experiments can be constructed;
- that \(\mathfrak R_{E,t}\to\mathfrak R_{E,t+1}\) has occurred;
- any basin-opening result.

---

## 18. Research position after this preregistration

The empirical sequence remains:

\[
\boxed{
\text{geometry}
\rightarrow
\text{navigation}
\rightarrow
\text{valuation}
\rightarrow
\boxed{\text{accessibility contraction}}
\rightarrow
\text{experiment-space construction}.
}
\]

The next repository action after this preregistration is implementation/execution of this audit only.

No `P_ep` ledger update is authorized until the accessibility results exist.