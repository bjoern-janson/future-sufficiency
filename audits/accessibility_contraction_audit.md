# Accessibility Contraction Audit — Results

## Provenance

Preregistered before execution at:

```text
6116603e0814f6fd7742cdb21ef312bd0cb15070
```

Parent dependency checkpoint:

```text
309f7dd0457c2d55ca08357c00b1c8aef539e1d9
```

Empirical anchors remain:

```text
b7c068b  valuation-role minimality audit
9a32f94  multi-candidate acquisition-order audit
4694382  STOP-substitution audit
```

The new accessibility panel was executed in-session against the preregistered logic.

The committed executable imports the valuation-role-minimality audit and hard-asserts the complete upstream regression chain when run in-repo. This connector session does **not** claim a fresh process replay of those older audits.

The correct provenance description is:

\[
\boxed{
\textbf{fresh accessibility result with inherited hard regression assertions}.
}
\]

No theory file is changed by this result.

---

## 1. Frozen causal question

The latent experiment universe remains:

\[
\boxed{
\mathcal E^\star
=
\{e_m:m\in\{0,1\}^4\setminus\{0000\}\},
\qquad
|\mathcal E^\star|=15.
}
\]

Each frozen probe is:

\[
e_m(X)=m\cdot X\pmod 2.
\]

The latent-universe semantic checksum is:

```text
sha256 54b7375f6ff283a3dff9f06bdaf67cced806411c9277021b0f9579c50cf45e59
```

The same 15 probe semantics are used under A0–A4.

Therefore:

\[
\boxed{
B_{\mathcal E^\star}=\text{fixed}.
}
\]

Only the access interface changes:

\[
\boxed{
A_{\rm explicit}\rightarrow A_{\rm reduced}.
}
\]

The frozen downstream valuation remains:

\[
\boxed{
\text{contract-derived corrective consequence}
+
\text{COMMIT-anchored quantitative burden}
\rightarrow
\text{maximal worthwhile accessible refinement}.
}
\]

No probe is generated, composed, altered, or added.

---

## 2. Evaluator invariants

The finite world contains 16 four-bit states.

For each of 15 correction contexts \(c_m\):

- the matching parity probe \(e_m\) reveals the warranted correction exactly;
- every other nonzero parity is independent of that target;
- every probe carries one raw information bit;
- every probe has the same anchored burden \(\kappa=0.1\).

Thus:

\[
\boxed{
R_{\rm corr}(e_m\mid c_m)=0.5
}
\]

and:

\[
\boxed{
R_{\rm corr}(e_{m'}\mid c_m)=0
\quad(m'\neq m).
}
\]

If the matching probe is accessible, the frozen valuation selects it uniquely. If it is inaccessible, all exposed alternatives have zero corrective consequence and positive burden, so the frozen termination role returns `COMMIT`.

This preserves the preregistered localization:

\[
\boxed{
\text{exists}
\land
\text{valuable/selectable}
\land
\text{accessible?}
}
\]

---

## 3. Primary A0 → A1 accessibility contraction

Across:

```text
64 anonymous encodings
15 correction contexts per encoding
960 context-encoding evaluations
```

the explicit-menu reference A0 achieved:

```text
target probe reachable: 960 / 960
choice matches reference: 960 / 960
```

The target-blind `ALL_REGISTRY` access rule A1 also achieved:

```text
target probe reachable: 960 / 960
choice matches A0:       960 / 960
```

The access ledger changes from:

```text
A0 explicit menu
(menu, generator, grammar, semantic_hints, search_constraints)
(15,   0,         0,       0,              0)
B_access = 15
```

to:

```text
A1 ALL_REGISTRY
(menu, generator, grammar, semantic_hints, search_constraints)
(0,    1,         0,       0,              0)
B_access = 1
```

Therefore:

\[
\boxed{
B_{\rm access}:15\rightarrow1
}
\]

while:

\[
\boxed{
\operatorname{Reach}_{A1}
=
\operatorname{Reach}_{A0}
=
1
}
\]

for every decision-relevant target probe.

This earns the narrow contraction:

\[
\boxed{
\textbf{
explicit per-probe enumeration is not necessary for complete accessibility of this fixed finite latent registry.
}
}
\]

A single target-blind rule exposing all members of the already-specified registry preserves the same reachability and downstream choices.

This result does **not** reduce \(B_{\mathcal E^\star}\).

---

## 4. A2 no-access control

A2 removes every access path:

```text
(menu, generator, grammar, semantic_hints, search_constraints)
(0,    0,         0,       0,              0)
B_access = 0
```

Result:

```text
target probe reachable: 0 / 960
choice matches A0:      0 / 960
```

The 15 probes still exist in \(\mathcal E^\star\).

Therefore:

\[
\boxed{
\textbf{latent existence of a useful refinement does not imply accessibility.}
}
\]

---

## 5. A3 partial-access coverage certificate

A3 exposes only the first seven opaque handles in each anonymously permuted registry:

```text
(menu, generator, grammar, semantic_hints, search_constraints)
(0,    1,         0,       0,              1)
B_access = 2
```

Each encoding exposes exactly:

\[
\boxed{7/15}
\]

latent probes.

Across all 64 encodings:

```text
target probe reachable: 448 / 960
choice matches A0:      448 / 960
```

Hence:

\[
\boxed{
\frac{448}{960}
=
\frac7{15}
\approx0.4667.
}
\]

A3 does **not** exceed the preregistered accessibility ceiling.

For every failure context:

\[
\boxed{
e^\star\in\mathcal E^\star
\land
Q_{\rm acquire}\text{ would select }e^\star\text{ if exposed}
\land
e^\star\notin A3.
}
\]

The missing performance therefore localizes to unavailable refinement coverage, not to valuation, inference, or navigation.

---

## 6. A4 oracle-displacement control

A4 exposes only the target probe through:

```text
TARGET_LOOKUP(context) -> opaque target handle
```

It achieves:

```text
target probe reachable: 960 / 960
choice matches A0:      960 / 960
```

but its access ledger is:

```text
(menu, generator, grammar, semantic_hints, search_constraints)
(0,    1,         0,       15,             0)
B_access = 16
```

The 15 context-to-target semantic hints directly relocate the experiment designer into the access rule.

Therefore A4 is classified as:

\[
\boxed{\text{oracle displacement}.}
\]

Its behavioral success is invalid as accessibility-minimality evidence.

---

## 7. Anonymous-identity invariance

For every one of the 64 encodings, the audit independently:

- permutes the mapping between parity probes and opaque handles;
- permutes registry iteration order;
- flips every probe's output token independently;
- permutes correction-context identifiers.

A1 remains exact on all 960 evaluations.

A3 reaches exactly seven target probes per encoding and exactly its aggregate \(7/15\) ceiling.

Thus the successful accessibility result does not depend on stable probe names, context names, registry position, or output polarity.

---

## 8. Access specification ledger

| Interface | `B_menu` | `B_generator` | `B_grammar` | `B_semantic_hints` | `B_search_constraints` | `B_access` | Result |
|---|---:|---:|---:|---:|---:|---:|---|
| A0 explicit menu | 15 | 0 | 0 | 0 | 0 | 15 | 960/960 |
| A1 `ALL_REGISTRY` | 0 | 1 | 0 | 0 | 0 | **1** | **960/960** |
| A2 no access | 0 | 0 | 0 | 0 | 0 | 0 | 0/960 |
| A3 first 7 | 0 | 1 | 0 | 0 | 1 | 2 | 448/960 |
| A4 target lookup | 0 | 1 | 0 | 15 | 0 | 16 | 960/960; oracle |

For the primary valid substitution:

\[
\boxed{
B_{\rm access}\downarrow
\land
R_{\rm functional}\text{ preserved}.
}
\]

Specifically:

\[
\boxed{15\rightarrow1}
\]

with no new grammar, semantic hint, or target-specific search constraint.

---

## 9. What the audit earns

Within this finite deterministic regime:

\[
\boxed{
\textbf{explicit enumeration of every latent probe is contingent.}
}
\]

A generic target-blind access rule over the unchanged latent registry preserves complete target-probe reachability and complete downstream choice correspondence.

At the same time:

\[
\boxed{
\textbf{some access path remains causally necessary: latent existence alone is insufficient.}
}
\]

The role-level accessibility dependency has therefore contracted from 15 explicit menu entries to:

\[
\boxed{
\text{generic access to the already-defined latent registry}.
}
\]

This is an accessibility result, not an experiment-generation result.

---

## 10. What remains supplied

The largest remaining experiment-specification burden is deliberately untouched:

\[
\boxed{B_{\mathcal E^\star}.}
\]

The audit still assumes:

- the 15-member latent registry exists;
- every parity-probe semantic is supplied;
- the registry membership is fixed;
- a generic primitive can iterate that registry;
- the correction contract is fixed;
- the downstream valuation/navigation machinery is inherited.

Thus the result does **not** establish:

- that the registry-access primitive is globally minimal;
- that the latent registry is unnecessary;
- that probe semantics can be generated;
- that the experiment ontology has been compressed;
- that a system can construct a previously unavailable experiment;
- that \(\mathfrak R_{E,t}\rightarrow\mathfrak R_{E,t+1}\);
- basin opening.

The next scientific question is therefore exactly:

\[
\boxed{
\textbf{Where does the remaining latent experiment specification live, and can that specification itself be constructed or reduced without oracle displacement?}
}
\]

That question belongs to the later experiment-space-construction branch.

---

## 11. Upstream regression boundary

The committed executable imports `valuation_role_minimality_audit.audit()` and hard-asserts the frozen upstream chain:

```text
valuation-role minimality:
  Cut R no-explicit-R_corr: 512
  contract-blind mirror ceiling: 1/2
  anchored burden: 320
  no-burden ceiling: 1/4
  burden-order ceiling: 1/4
  relative-difference ceiling: 4/5

multi-candidate:
  encoded states: 512
  max-only exact: 512
  sign-only ceiling: 13/24
  Pareto ceiling: 17/24

STOP/navigation:
  visited decision points: 3584
  derived terminations: 1536
  trace mismatches: 0
```

Those older audits were not freshly process-reexecuted in this connector session.

Therefore the provenance statement remains:

\[
\boxed{
\textbf{fresh accessibility result with inherited hard regression assertions}.
}
\]

---

## 12. Current boundary

The empirical spine is now:

\[
\boxed{
\text{geometry}\checkmark
\rightarrow
\text{navigation}\checkmark
\rightarrow
\text{valuation}\checkmark
\rightarrow
\text{accessibility contraction}\checkmark
\rightarrow
\boxed{\text{experiment-space construction}}
}
\]

with the strict attribution boundary:

\[
\boxed{
\text{accessibility contraction}
\neq
\text{experiment invention}
\neq
\text{ontology construction}.
}
\]