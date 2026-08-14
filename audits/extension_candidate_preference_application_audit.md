# Extension Candidate Preference Application Audit — Results

## Provenance

Preregistered before execution at:

```text
f64dd1d3e222b9ca13903facc8fd1e727adb2fd7
```

Parent checkpoint:

```text
7c5bffe31b7cfae163248eadec869eb4800a059a
```

Frozen upstream anchors:

```text
actual candidate native-comparison result
  3e332072502fa64c432b143e6d157fc1f5cd18b8

actual candidate comparator executable
  2b94247b0f5542e0bfd0cf8f163ca02384f1e546

preference-identification executable
  b47c0884dcb7769a2ca9b934e8a9b64dad218399

preference-identification result
  4fab22d2a7be25b001b679fe92e67187098ce696
```

The GitHub connector independently verified these exact frozen anchors and the preregistration blob
`f330be5408af9a31271a2ba7a731e3d4507743fc`.

The connector execution environment does not expose repository files directly to the local Python process. The
committed executable therefore performs the exact Git-blob and lossless packed-result decode when run in the
repository, while the result reported here was independently reproduced from the frozen candidate-measurement
and comparator semantics plus the exact frozen preference interpreter. The independently reconstructed native
graph reproduces all six coordinate relation-count vectors from `ca423e1` exactly.

Correct provenance:

\[
\boxed{\textbf{
fresh actual-candidate preference-application result with frozen upstream graph/governance anchors and hard regression assertions.
}}
\]

No governance contract is selected or ranked. No candidate score, scalar `Q_extension`, adoption, authorization,
binding, or execution is introduced.

---

## 1. Frozen endpoint

The audit executes only:

\[
\boxed{
(\mathcal R_{ij},G_{\rm pref})
\longrightarrow
R_{\rm pref}^{G}(i,j)
}
\]

for:

```text
candidates                         12
unordered pairs                    66
frozen governance contracts         4
primary preference applications   264
pair pruning                         0
contract pruning                     0
```

The canonical pair-list SHA-256 remains:

```text
76ae7638e225973f21b90605a9c020a74e752143d1dd008bd2f894fdbd4629aa
```

Every application consumes the already-frozen six-token native relation profile. No coordinate measurement,
comparison license, native relation, governance clause, or preference interpreter is recomputed or tuned from
the actual application outcomes.

---

## 2. Preference-status topology by supplied governance contract

| supplied governance contract | `PREFER_I` | `PREFER_J` | `EQUIVALENT` | `NO_WARRANTED_PREFERENCE` |
|---|---:|---:|---:|---:|
| `G_PARTIAL_EMPTY` | 0 | 0 | 1 | 65 |
| `G_CONSTRAINT_B` | 5 | 3 | 1 | 57 |
| `G_LEX_DV_REOPEN_B` | 3 | 5 | 1 | 57 |
| `G_COMP_EXPLICIT` | 3 | 5 | 1 | 57 |

These counts are descriptive application topology only. They are not governance-family scores and do not imply
that a contract with fewer abstentions is better.

The partial-order-preserving contract produces **no directional preference at all** on the actual graph. Every
non-equivalent pair is either blocked by a native license/partiality boundary or contains an authorized objective
conflict for which `Gamma_tradeoff = empty`.

---

## 3. The 66 pairs partition into four exact structural classes

The actual candidate universe partitions exactly as:

```text
53  universal NO_WARRANTED_PREFERENCE from native license gaps
 4  universal NO_WARRANTED_PREFERENCE from native burden incomparability
 1  universal EQUIVALENT
 8  cross-governance preference disagreement with directional conflict
--
66
```

Thus the actual application graph is not merely sparse. Its non-resolution is typed.

The 53 license-gap pairs remain:

```text
NO_WARRANTED_PREFERENCE / LICENSE_GAP / NATIVE_LICENSE
```

under all four contracts.

The four native-partiality pairs are:

```text
CTRL_ALIAS_A       vs CTRL_SUPPLIED_DEG2
CTRL_ALIAS_A       vs SYN_A_120
CTRL_ALIAS_A       vs SYN_B_50
SYN_C1_1653        vs SYN_C2_2388
```

Each has:

```text
B = INCOMPARABLE
```

and therefore remains:

```text
NO_WARRANTED_PREFERENCE / NATIVE_INCOMPARABILITY / NATIVE_PARTIALITY
```

under all four frozen contracts.

---

## 4. Cross-governance disagreement is real and preserved

Exactly eight pairs have different preference statuses across the four supplied governance contracts, and **all
eight contain an actual directional conflict**: at least one supplied contract yields `PREFER_I` while another
yields `PREFER_J`.

The eight pairs are:

```text
CTRL_ALIAS_A        vs CTRL_ID_LINEAR
CTRL_ID_DEG2        vs SYN_C1_1653
CTRL_ID_DEG2        vs SYN_C2_2388
CTRL_ID_LINEAR      vs CTRL_SUPPLIED_DEG2
CTRL_ID_LINEAR      vs SYN_A_120
CTRL_ID_LINEAR      vs SYN_B_50
CTRL_SUPPLIED_DEG2  vs SYN_A_120
CTRL_SUPPLIED_DEG2  vs SYN_B_50
```

The observed four-contract status vectors have only two directional-conflict forms:

```text
count 5:
  G_PARTIAL_EMPTY      -> NO_WARRANTED_PREFERENCE
  G_CONSTRAINT_B       -> PREFER_I
  G_LEX_DV_REOPEN_B    -> PREFER_J
  G_COMP_EXPLICIT      -> PREFER_J

count 3:
  G_PARTIAL_EMPTY      -> NO_WARRANTED_PREFERENCE
  G_CONSTRAINT_B       -> PREFER_J
  G_LEX_DV_REOPEN_B    -> PREFER_I
  G_COMP_EXPLICIT      -> PREFER_I
```

This disagreement is **not** an error. The authoritative governance input differs.

No majority vote, contract weighting, meta-Pareto rule, or contract-selection criterion is applied.

---

## 5. What drives the eight conflicts

For each of the eight disagreement pairs, identified corrective consequence and structured burden point in
opposite preference directions under the frozen orientations.

`G_PARTIAL_EMPTY` has no tradeoff authority, so it returns:

```text
NO_WARRANTED_PREFERENCE / NO_TRADEOFF_AUTHORITY
```

on all eight.

`G_CONSTRAINT_B` makes burden non-compensable and therefore selects the candidate with lower structured burden.

`G_LEX_DV_REOPEN_B` gives `DeltaV` first lexicographic priority and therefore follows the identified corrective
consequence direction on these eight pairs.

`G_COMP_EXPLICIT` applies the two already-supplied finite conflict clauses and, on this actual graph, yields the
same **statuses** as the lexicographic contract on the eight conflicts, but with different warrant lineage:

```text
G_LEX_DV_REOPEN_B -> LEXICOGRAPHIC_PRIORITY
G_COMP_EXPLICIT   -> AUTHORIZED_TRADEOFF
```

Status agreement therefore does not erase governance provenance.

---

## 6. Contract-relative equivalence does not imply native equivalence

Exactly one pair is candidate-level `EQUIVALENT` under all four supplied governance contracts:

```text
SYN_A_120 vs SYN_B_50
```

Its frozen native profile is:

```text
DeltaV      EQUIVALENT
B           EQUIVALENT
DeltaC      INCOMPARABLE
collateral  EQUIVALENT
reopen      EQUIVALENT
Scope       EQUIVALENT
```

`DeltaC` has no preference authority under any of the four supplied contracts, so its native incomparability is
lawfully quotiented out at the preference layer.

Therefore:

\[
\boxed{
R_{\rm pref}^{G}(i,j)=\texttt{EQUIVALENT}
\not\Rightarrow
\mathcal R_{ij}\text{ is coordinatewise equivalent}.
}
\]

No candidate deduplication follows.

---

## 7. Typed abstention is preserved

Observed non-preference reasons remain layer-specific:

| reason | meaning in this application |
|---|---|
| `LICENSE_GAP` | required native relation is not licensed |
| `NATIVE_INCOMPARABILITY` | required native relation is licensed but partial |
| `NO_TRADEOFF_AUTHORITY` | relevant native relations are available, but supplied governance does not authorize completion |

For `G_PARTIAL_EMPTY`:

```text
LICENSE_GAP               53
NATIVE_INCOMPARABILITY     4
NO_TRADEOFF_AUTHORITY      8
ALL_RELEVANT_EQUIVALENT    1
```

For each of the other three contracts, the eight governance conflicts are resolved according to that contract's
already-supplied constraint, priority, or finite tradeoff semantics; the 53 license gaps and four native
incomparabilities remain abstentions.

Thus:

\[
\boxed{
\texttt{NO_LICENSED_COMPARISON}
\neq
\texttt{INCOMPARABLE}
\neq
\texttt{NO_WARRANTED_PREFERENCE}.
}
\]

---

## 8. Pair symmetry and nuisance invariance

Exact pair-swap preference/warrant symmetry passed:

```text
264 / 264
```

The primary preference result was invariant in all `264/264` records to shadow changes in:

```text
candidate provenance display labels
candidate human-readable aliases
serialization order
contract display aliases
implementation tags
opaque nonces
```

No candidate ID, provenance class, display alias, or serialization artifact supplies preference authority.

---

## 9. No hidden scalar or ranking layer

The application does not compute:

```text
candidate win/loss counts
candidate outdegree/indegree
Copeland or Borda score
Condorcet winner
Elo / Bradley-Terry / rank centrality
transitive preference closure
Pareto frontier
governance vote
governance ranking
utility
reward
Q_extension
```

The eight cross-governance directional conflicts remain unresolved multiplex preference structure.

---

## 10. Anti-downstream status

```text
actual-candidate preference application    true
governance contract selected              false
governance family ranked                  false
cross-governance disagreement resolved    false
candidate score defined                   false
candidate ranking performed               false
transitive completion performed           false
Pareto filtering performed                false
Q_extension defined                       false
utility defined                           false
reward defined                            false
NO_WARRANTED_ADOPTION defined             false
adoption performed                        false
authorization performed                   false
binding performed                         false
execution performed                       false
```

Preference remains distinct from authorization.

---

## 11. Earned claim

The strongest permitted claim is:

\[
\boxed{\textbf{
The frozen supplied governance contracts yield the reported candidate-level preference relations over the preregistered 12-candidate native comparison graph, with typed no-preference boundaries, contract-relative semantics, governance provenance, pair symmetry, and nuisance invariance preserved.
}}
\]

The application additionally demonstrates descriptively that the same actual native relation profile can yield
opposite candidate-level directions under different supplied governance contracts.

This does **not** establish:

- that any supplied governance contract is normatively correct;
- a governance-contract ranking or selection rule;
- that any candidate should be adopted;
- scalar sufficiency;
- `Q_extension`;
- `NO_WARRANTED_ADOPTION`;
- authorization;
- binding;
- post-adoption consequence.

The actual preference graph is now available for a separately preregistered scalar-sufficiency/minimality question.
