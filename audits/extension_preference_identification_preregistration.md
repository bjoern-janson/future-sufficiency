# Extension Preference / Governance-Interface Identification — Preregistration

## Status

This document freezes the next empirical gate **before any preference relation is applied to the actual 12-candidate extension graph and before any `Q_extension` is defined**.

Parent checkpoint:

```text
ca423e1029b013368c4281944af5a02678af83c5
```

Actual-candidate comparator-application preregistration:

```text
519073b3bd980f729a4b37e3ee79723a53587fc5
```

Actual-candidate comparator-application execution:

```text
ca423e1029b013368c4281944af5a02678af83c5
```

Frozen application executable blob:

```text
2b94247b0f5542e0bfd0cf8f163ca02384f1e546
```

Frozen application result blob:

```text
3e332072502fa64c432b143e6d157fc1f5cd18b8
```

Comparison-identification execution:

```text
d0802137f303406c4aab1e5779af644b4cfe6b4f
```

Comparison-identification result blob:

```text
7bac5f2aed17de6532b2fccfa138d8f954c78a8b
```

The only object frozen here is:

\[
\boxed{
(\mathcal R^{\rm cal},G_{\rm pref})
\longrightarrow
R_{\rm pref}.
}
\]

The actual 12-candidate native comparison graph is **held out completely** from preference calibration.

This artifact does not define or apply `Q_extension`.

It does not rank or choose among the actual extension candidates.

It does not justify any supplied governance contract.

It does not authorize, adopt, bind, or execute any extension.

---

# 1. Scientific boundary

The preceding branch has established, in finite audited regimes:

\[
\boxed{
\mathcal M_{\rm ext}\checkmark
\rightarrow
s\mapsto\mathcal V_{\rm ext}(s)\checkmark
\rightarrow
\mathcal R_{\rm compare}\checkmark
\rightarrow
\text{actual native candidate graph}\checkmark.
}
\]

The present question is narrower and new:

> Given independently constructed native-relation profiles and an explicitly supplied governance contract, can a preference mechanism preserve every distinction that the supplied contract requires for warranted preference while introducing no distinction that lacks preference authority?

The governing separation is:

\[
\boxed{
\text{native comparison}
\neq
\text{preference}
\neq
\text{tradeoff authority}
\neq
\text{authorization}.
}
\]

The strongest claim permitted after a successful execution is:

\[
\boxed{
\textbf{
In the audited finite preference-calibration regimes, candidate-level preference relations are identifiable relative to explicitly supplied governance contracts while native license gaps, native incomparability, non-compensable contract structure, governance provenance, and nuisance invariance are preserved.
}
}
\]

A successful audit does **not** establish that any supplied `G_pref` is normatively correct.

---

# 2. Actual candidate graph is a strict holdout

The 12-candidate graph at `ca423e1` motivated the existence of the present scientific question, but it is not a calibration dataset.

The child execution must not deserialize, inspect, enumerate, summarize, query, or condition on any actual candidate-pair relation from:

```text
audits/extension_candidate_comparator_application_results.json
```

It must not import the actual-candidate comparator-application executable to obtain graph values.

It must not contain actual candidate IDs in its calibration fixture registry.

It must not use observed coordinate counts, observed candidate-pair patterns, Hudson-specific pair patterns, or any other feature of the actual graph to choose:

```text
Gamma_license
Gamma_constraint
Gamma_objective
Gamma_tradeoff
fixture profiles
preference outputs
reason codes
thresholds
priorities
tradeoff clauses
```

The upstream commit and blob anchors may be recorded as lineage only.

The execution must emit:

```text
actual_candidate_graph_read = false
actual_candidate_pair_evaluations = 0
actual_candidate_preference_relations = 0
```

Thus:

\[
\boxed{
\text{actual 12-candidate graph}
\not\rightarrow
G_{\rm pref}.
}
\]

---

# 3. Frozen native relation alphabet

Every synthetic calibration profile uses only the already-identified native relation vocabulary:

\[
\Sigma_R=
\{
\texttt{I_GREATER},
\texttt{J_GREATER},
\texttt{EQUIVALENT},
\texttt{INCOMPARABLE},
\texttt{NO_LICENSED_COMPARISON}
\}.
\]

The coordinate order is frozen as:

```text
DeltaV
B
DeltaC
collateral
reopen
Scope
```

A relation profile is therefore:

\[
\boxed{
\mathcal R
=
(R_{\Delta V},R_B,R_{\Delta C},R_{\rm collateral},R_{\rm reopen},R_{\rm scope}).
}
\]

No synthetic profile contains a scalar score, candidate utility, reward, adoption value, or hidden magnitude.

The native semantics remain unchanged:

- `DeltaV:I_GREATER` means greater identified corrective consequence for candidate `i` under the relevant native relation.
- `B:I_GREATER` means greater structured burden for candidate `i`.
- `DeltaC:I_GREATER` means set-theoretically greater semantic geometry delta for candidate `i`, not better geometry.
- `collateral:I_GREATER` means componentwise greater signed collateral consequence under its native comparison.
- `reopen:I_GREATER` means stresswise greater reachable-correction profile for candidate `i`.
- `Scope` is descriptive support topology and may never become a compensable objective in this audit.

There is no generic rule:

```text
I_GREATER = good
J_GREATER = bad
```

Coordinate orientation enters preference only where an explicit supplied governance contract grants it authority.

---

# 4. Preference output type

The candidate-level preference output vocabulary is frozen as:

\[
\boxed{
\Sigma_P=
\{
\texttt{PREFER_I},
\texttt{PREFER_J},
\texttt{EQUIVALENT},
\texttt{NO_WARRANTED_PREFERENCE}
\}.
}
\]

`EQUIVALENT` here is a candidate-level preference relation **relative to the supplied governance contract and calibration profile**. It is not native-coordinate equivalence and does not imply equality of all measurements.

`NO_WARRANTED_PREFERENCE` means:

> the supplied governance contract and available native relation profile do not authorize a candidate-level direction or equivalence conclusion beyond the typed reason recorded.

It is distinct from both native null-like states:

\[
\boxed{
\texttt{NO_LICENSED_COMPARISON}
\neq
\texttt{INCOMPARABLE}
\neq
\texttt{NO_WARRANTED_PREFERENCE}.
}
\]

The first two are inputs from the native comparison layer.

The third is an output of the preference/governance layer.

---

# 5. Preference warrant / reason codes

Every preference output must carry exactly one primary warrant code from:

```text
ALIGNED_OBJECTIVES
ALL_RELEVANT_EQUIVALENT
LICENSE_GAP
NATIVE_INCOMPARABILITY
NO_TRADEOFF_AUTHORITY
CONSTRAINT_BLOCK_I
CONSTRAINT_BLOCK_J
LEXICOGRAPHIC_PRIORITY
AUTHORIZED_TRADEOFF
```

The code is lineage, not a second score.

For `NO_WARRANTED_PREFERENCE`, the allowed primary reasons are:

```text
LICENSE_GAP
NATIVE_INCOMPARABILITY
NO_TRADEOFF_AUTHORITY
```

For `PREFER_I` / `PREFER_J`, the allowed primary reasons are contract-dependent and must be one of:

```text
ALIGNED_OBJECTIVES
CONSTRAINT_BLOCK_I
CONSTRAINT_BLOCK_J
LEXICOGRAPHIC_PRIORITY
AUTHORIZED_TRADEOFF
```

For candidate-level `EQUIVALENT`:

```text
ALL_RELEVANT_EQUIVALENT
```

No output may use a generic `UNCERTAIN` reason.

---

# 6. Supplied governance contract

The governance object is frozen as:

\[
\boxed{
G_{\rm pref}
=
(\Gamma_{\rm license},
 \Gamma_{\rm constraint},
 \Gamma_{\rm objective},
 \Gamma_{\rm tradeoff},
 P_G,
 B_G).
}
\]

where:

- `Gamma_license` specifies which native relations must be licensed before the contract can form a preference;
- `Gamma_constraint` specifies non-compensable candidate-level restrictions, if any;
- `Gamma_objective` specifies which native coordinates have directional preference authority and their orientation;
- `Gamma_tradeoff` specifies any explicit conflict-resolution authority;
- `P_G` is governance provenance;
- `B_G` is a descriptive governance-specification ledger.

Every primary contract has:

```text
P_G = SUPPLIED_CALIBRATION_GOVERNANCE
```

No primary contract is inferred, fitted, optimized, selected, or tuned from data.

The audit identifies preference behavior **relative to** these supplied contracts.

It does not identify the contracts themselves as warranted.

Thus:

\[
\boxed{
\text{preference mechanism identified relative to }G_{\rm pref}
\neq
G_{\rm pref}\text{ justified}.
}
\]

---

# 7. Governance specification ledger `B_G`

The audit preserves a structured descriptive ledger:

```text
required_license_clauses
constraint_clauses
objective_orientation_clauses
priority_edges
explicit_tradeoff_clauses
```

No scalar `B_G` ranking is computed.

No governance minimality conclusion is permitted in this gate.

The four primary contracts have frozen ledgers:

| contract | license | constraint | objective | priority edges | tradeoff clauses |
|---|---:|---:|---:|---:|---:|
| `G_PARTIAL_EMPTY` | 3 | 0 | 2 | 0 | 0 |
| `G_CONSTRAINT_B` | 3 | 1 | 1 | 0 | 0 |
| `G_LEX_DV_REOPEN_B` | 4 | 0 | 3 | 2 | 0 |
| `G_COMP_EXPLICIT` | 3 | 0 | 2 | 0 | 2 |

These numbers are specification provenance only.

The audit must not claim:

```text
smaller B_G = better governance
larger B_G = more correct governance
more complete preference = better governance
```

`mathfrak G_min` remains a future object.

---

# 8. Contract `G_PARTIAL_EMPTY`

This is the primary partial-order-preserving, non-compensatory contract.

## 8.1 `Gamma_license`

Required native coordinates:

```text
DeltaV
B
Scope
```

A required `NO_LICENSED_COMPARISON` yields:

```text
NO_WARRANTED_PREFERENCE / LICENSE_GAP
```

A required `INCOMPARABLE` on an objective coordinate yields:

```text
NO_WARRANTED_PREFERENCE / NATIVE_INCOMPARABILITY
```

`Scope` is a license requirement only. Any licensed Scope token is sufficient for this synthetic gate; it never supplies objective direction.

## 8.2 `Gamma_constraint`

```text
none
```

## 8.3 `Gamma_objective`

Two objectives have preference authority:

```text
DeltaV  : greater native corrective consequence supports the same candidate
B       : lower native burden supports the candidate with lower burden
```

Therefore orientation is:

| native relation | `DeltaV` support | `B` support |
|---|---|---|
| `I_GREATER` | I | J |
| `J_GREATER` | J | I |
| `EQUIVALENT` | E | E |
| `INCOMPARABLE` | BLOCK | BLOCK |
| `NO_LICENSED_COMPARISON` | BLOCK | BLOCK |

Coordinates `DeltaC`, `collateral`, and `reopen` have no preference authority under this contract.

Their relation tokens may vary without affecting preference.

## 8.4 `Gamma_tradeoff`

\[
\boxed{\Gamma_{\rm tradeoff}=\varnothing.}
\]

Decision rule after license/incomparability checks:

```text
all relevant objectives E                 -> EQUIVALENT
all non-E objective support is I          -> PREFER_I
all non-E objective support is J          -> PREFER_J
both I and J support occur                 -> NO_WARRANTED_PREFERENCE
```

A conflict emits:

```text
NO_WARRANTED_PREFERENCE / NO_TRADEOFF_AUTHORITY
```

No compensation rate is invented.

---

# 9. Contract `G_CONSTRAINT_B`

This is a supplied constraint-first calibration contract.

## 9.1 `Gamma_license`

Required:

```text
DeltaV
B
Scope
```

Required license gaps and burden incomparability block preference as above.

## 9.2 `Gamma_constraint`

Structured burden is non-compensable in this synthetic contract.

Pair-relative constraint semantics are frozen as:

```text
B:I_GREATER -> candidate I is constraint-blocked
B:J_GREATER -> candidate J is constraint-blocked
B:EQUIVALENT -> neither candidate is blocked
B:INCOMPARABLE -> NO_WARRANTED_PREFERENCE / NATIVE_INCOMPARABILITY
B:NO_LICENSED_COMPARISON -> NO_WARRANTED_PREFERENCE / LICENSE_GAP
```

If exactly one candidate is blocked, the other receives the candidate-level preference relation regardless of `DeltaV` direction:

```text
I blocked -> PREFER_J / CONSTRAINT_BLOCK_I
J blocked -> PREFER_I / CONSTRAINT_BLOCK_J
```

This is a supplied governance rule, not a claim that burden should generally have this authority.

## 9.3 `Gamma_objective`

If neither candidate is burden-blocked, `DeltaV` is the only objective:

```text
DeltaV:I_GREATER -> PREFER_I
DeltaV:J_GREATER -> PREFER_J
DeltaV:EQUIVALENT -> EQUIVALENT
```

## 9.4 `Gamma_tradeoff`

```text
none
```

Constraint authority is not represented as a tradeoff weight.

---

# 10. Contract `G_LEX_DV_REOPEN_B`

This is a supplied lexicographic calibration contract.

It is a hypothesis/control family, not a preferred governance design.

## 10.1 `Gamma_license`

Required:

```text
DeltaV
reopen
B
Scope
```

Before lexicographic evaluation, every required objective must be licensed and non-`INCOMPARABLE`.

Thus lower-priority missingness cannot be ignored merely because a higher-priority objective already differs.

## 10.2 `Gamma_constraint`

```text
none
```

## 10.3 `Gamma_objective`

Priority order:

```text
DeltaV > reopen > B
```

Orientations:

```text
DeltaV : greater supports same candidate
reopen : greater supports same candidate
B      : lower supports candidate with lower burden
```

After all required license checks pass, evaluate the first non-equivalent objective in that order.

The result carries:

```text
LEXICOGRAPHIC_PRIORITY
```

If all three are equivalent:

```text
EQUIVALENT / ALL_RELEVANT_EQUIVALENT
```

## 10.4 `Gamma_tradeoff`

There is no numeric compensation table.

The priority order itself is supplied governance structure and is provenance-tracked in `B_G`.

---

# 11. Contract `G_COMP_EXPLICIT`

This is a supplied finite compensatory lookup contract.

It is included to test whether an explicitly authorized tradeoff can be applied without being misrepresented as empirically justified.

## 11.1 `Gamma_license`

Required:

```text
DeltaV
B
Scope
```

## 11.2 `Gamma_constraint`

```text
none
```

## 11.3 `Gamma_objective`

Same orientation as `G_PARTIAL_EMPTY`:

```text
DeltaV : greater supports same candidate
B      : lower supports candidate with lower burden
```

## 11.4 `Gamma_tradeoff`

Exactly two symmetric finite clauses are supplied:

```text
T1: DeltaV supports I AND B supports J -> PREFER_I
T2: DeltaV supports J AND B supports I -> PREFER_J
```

These clauses are fixed before execution.

They may not be generalized into numeric weights.

They may not be tuned after calibration.

An output using either clause carries:

```text
AUTHORIZED_TRADEOFF
```

The allowed claim is only:

> the mechanism correctly applied the supplied tradeoff clause.

Forbidden inference:

> the tradeoff clause is normatively justified because it produced the preregistered output.

---

# 12. Governance interface representation

For each fixed primary contract, define the governance-interface state:

\[
\boxed{
q_G(\mathcal R)=G_{\rm pref}(\mathcal R).
}
\]

The canonical state contains only contract-authorized decision features:

```text
license_state
constraint_state
objective_support_signature
priority_state
matched_tradeoff_clause
```

Fields irrelevant to a contract are omitted or set to a single canonical `NONE` token.

The governance interface must not preserve candidate names, provenance labels, fixture IDs, serialization order, random nonces, implementation branch labels, or actual-candidate metadata.

The candidate-level target relation for calibration is denoted:

\[
L_G(\mathcal R).
\]

The audit tests whether the target relation factors through the governance interface:

\[
\boxed{
\exists h_G:\quad
L_G=h_G\circ G_{\rm pref}
}
\]

over each preregistered finite contract-specific calibration domain.

---

# 13. Factorization criterion — no governance aliasing

For fixed contract `G`, group all calibration profiles by their canonical governance-interface state `q_G`.

Factorization passes iff every fiber has exactly one target relation:

\[
\boxed{
G(\mathcal R_a)=G(\mathcal R_b)
\Rightarrow
L_G(\mathcal R_a)=L_G(\mathcal R_b).
}
\]

If one governance-interface state contains more than one target label, the contract representation is decision-insufficient on the calibration domain.

That failure is named:

\[
\boxed{\textbf{governance aliasing}.}
\]

The execution must serialize the fibers and their target-label cardinalities.

No post-hoc feature may be added to split a failed fiber.

A failed factorization means the gate fails for that architecture.

---

# 14. Nuisance invariance criterion — no authority injection

Let `N` contain all non-authoritative variables:

```text
anonymous candidate handles
synthetic provenance labels
fixture identifiers
serialization order
mapping insertion order
opaque nonce
implementation branch/tag label
human-readable aliases
```

For fixed licensed inputs and fixed governance semantics:

\[
\boxed{
(\mathcal R,G)_a\equiv(\mathcal R,G)_b
\Rightarrow
R_{\rm pref}(a)=R_{\rm pref}(b)
}
\]

under admissible changes in `N`.

A preference difference caused only by `N` is named:

\[
\boxed{\textbf{authority injection}.}
\]

The primary interpreter must never read `N` on the decision path.

---

# 15. The two decisive failure modes

The preference-identification gate is explicitly two-sided:

| failure | defect |
|---|---|
| governance aliasing | an authoritative distinction required by `L_G` is lost |
| authority injection | a non-authoritative distinction is added to preference |

The core principle tested is:

\[
\boxed{
\textbf{preserve every authorized distinction; introduce none that is unauthorized.}
}
\]

This is an empirical calibration claim only within the finite supplied governance tasks below.

---

# 16. Independent synthetic calibration profiles

The calibration profiles below are synthetic symbolic objects constructed before execution.

They are not sampled from the actual 12-candidate graph.

Abbreviations:

```text
IG  = I_GREATER
JG  = J_GREATER
EQ  = EQUIVALENT
INC = INCOMPARABLE
NLC = NO_LICENSED_COMPARISON
```

Coordinate order:

```text
(DeltaV, B, DeltaC, collateral, reopen, Scope)
```

Frozen base profile registry:

```text
P_EQ                  = (EQ,  EQ,  EQ,  EQ,  EQ,  EQ)
P_DV_I_ONLY           = (IG,  EQ,  EQ,  EQ,  EQ,  EQ)
P_DV_J_ONLY           = (JG,  EQ,  EQ,  EQ,  EQ,  EQ)
P_ALIGN_I             = (IG,  JG,  EQ,  EQ,  EQ,  EQ)
P_ALIGN_J             = (JG,  IG,  EQ,  EQ,  EQ,  EQ)
P_CONFLICT_I_BURDEN   = (IG,  IG,  EQ,  EQ,  EQ,  EQ)
P_CONFLICT_J_BURDEN   = (JG,  JG,  EQ,  EQ,  EQ,  EQ)
P_DV_LICENSE_GAP      = (NLC, EQ,  EQ,  EQ,  EQ,  EQ)
P_SCOPE_LICENSE_GAP   = (IG,  JG,  EQ,  EQ,  EQ,  NLC)
P_B_INCOMPARABLE      = (IG,  INC, EQ,  EQ,  EQ,  EQ)
P_GEOM_GAP_IGNORED    = (IG,  JG,  NLC, EQ,  EQ,  EQ)
P_COLL_INC_IGNORED    = (IG,  JG,  EQ,  INC, EQ,  EQ)
P_REOPEN_I_ONLY       = (EQ,  EQ,  EQ,  EQ,  IG,  EQ)
P_REOPEN_J_ONLY       = (EQ,  EQ,  EQ,  EQ,  JG,  EQ)
P_REOPEN_LICENSE_GAP  = (IG,  JG,  EQ,  EQ,  NLC, EQ)
P_REOPEN_INCOMPARABLE = (IG,  JG,  EQ,  EQ,  INC, EQ)
P_GEOM_INC_ALL_EQ     = (EQ,  EQ,  INC, EQ,  EQ,  EQ)
```

No profile contains actual candidate provenance or measured magnitudes.

---

# 17. Frozen target relations for `G_PARTIAL_EMPTY`

The child execution must reproduce exactly:

| profile | expected `R_pref` | expected reason |
|---|---|---|
| `P_EQ` | `EQUIVALENT` | `ALL_RELEVANT_EQUIVALENT` |
| `P_DV_I_ONLY` | `PREFER_I` | `ALIGNED_OBJECTIVES` |
| `P_DV_J_ONLY` | `PREFER_J` | `ALIGNED_OBJECTIVES` |
| `P_ALIGN_I` | `PREFER_I` | `ALIGNED_OBJECTIVES` |
| `P_ALIGN_J` | `PREFER_J` | `ALIGNED_OBJECTIVES` |
| `P_CONFLICT_I_BURDEN` | `NO_WARRANTED_PREFERENCE` | `NO_TRADEOFF_AUTHORITY` |
| `P_CONFLICT_J_BURDEN` | `NO_WARRANTED_PREFERENCE` | `NO_TRADEOFF_AUTHORITY` |
| `P_DV_LICENSE_GAP` | `NO_WARRANTED_PREFERENCE` | `LICENSE_GAP` |
| `P_SCOPE_LICENSE_GAP` | `NO_WARRANTED_PREFERENCE` | `LICENSE_GAP` |
| `P_B_INCOMPARABLE` | `NO_WARRANTED_PREFERENCE` | `NATIVE_INCOMPARABILITY` |
| `P_GEOM_GAP_IGNORED` | `PREFER_I` | `ALIGNED_OBJECTIVES` |
| `P_COLL_INC_IGNORED` | `PREFER_I` | `ALIGNED_OBJECTIVES` |
| `P_REOPEN_LICENSE_GAP` | `PREFER_I` | `ALIGNED_OBJECTIVES` |
| `P_REOPEN_INCOMPARABLE` | `PREFER_I` | `ALIGNED_OBJECTIVES` |
| `P_GEOM_INC_ALL_EQ` | `EQUIVALENT` | `ALL_RELEVANT_EQUIVALENT` |

This contract therefore demonstrates lawful quotienting of coordinates it does not authorize.

For example:

```text
P_ALIGN_I
P_GEOM_GAP_IGNORED
P_COLL_INC_IGNORED
P_REOPEN_LICENSE_GAP
P_REOPEN_INCOMPARABLE
```

must map to the same governance-interface decision state and the same target preference under `G_PARTIAL_EMPTY`.

---

# 18. Frozen target relations for `G_CONSTRAINT_B`

Mandatory cases:

| profile | expected `R_pref` | expected reason |
|---|---|---|
| `P_EQ` | `EQUIVALENT` | `ALL_RELEVANT_EQUIVALENT` |
| `P_DV_I_ONLY` | `PREFER_I` | `ALIGNED_OBJECTIVES` |
| `P_DV_J_ONLY` | `PREFER_J` | `ALIGNED_OBJECTIVES` |
| `P_CONFLICT_I_BURDEN` | `PREFER_J` | `CONSTRAINT_BLOCK_I` |
| `P_CONFLICT_J_BURDEN` | `PREFER_I` | `CONSTRAINT_BLOCK_J` |
| `P_ALIGN_I` | `PREFER_I` | `CONSTRAINT_BLOCK_J` |
| `P_ALIGN_J` | `PREFER_J` | `CONSTRAINT_BLOCK_I` |
| `P_DV_LICENSE_GAP` | `NO_WARRANTED_PREFERENCE` | `LICENSE_GAP` |
| `P_SCOPE_LICENSE_GAP` | `NO_WARRANTED_PREFERENCE` | `LICENSE_GAP` |
| `P_B_INCOMPARABLE` | `NO_WARRANTED_PREFERENCE` | `NATIVE_INCOMPARABILITY` |
| `P_GEOM_GAP_IGNORED` | `PREFER_I` | `CONSTRAINT_BLOCK_J` |

The apparent disagreement between this contract and another contract on the same profile is not an error if the supplied governance semantics differ.

---

# 19. Frozen target relations for `G_LEX_DV_REOPEN_B`

Mandatory cases:

| profile | expected `R_pref` | expected reason |
|---|---|---|
| `P_EQ` | `EQUIVALENT` | `ALL_RELEVANT_EQUIVALENT` |
| `P_DV_I_ONLY` | `PREFER_I` | `LEXICOGRAPHIC_PRIORITY` |
| `P_DV_J_ONLY` | `PREFER_J` | `LEXICOGRAPHIC_PRIORITY` |
| `P_CONFLICT_I_BURDEN` | `PREFER_I` | `LEXICOGRAPHIC_PRIORITY` |
| `P_CONFLICT_J_BURDEN` | `PREFER_J` | `LEXICOGRAPHIC_PRIORITY` |
| `P_REOPEN_I_ONLY` | `PREFER_I` | `LEXICOGRAPHIC_PRIORITY` |
| `P_REOPEN_J_ONLY` | `PREFER_J` | `LEXICOGRAPHIC_PRIORITY` |
| `P_REOPEN_LICENSE_GAP` | `NO_WARRANTED_PREFERENCE` | `LICENSE_GAP` |
| `P_REOPEN_INCOMPARABLE` | `NO_WARRANTED_PREFERENCE` | `NATIVE_INCOMPARABILITY` |
| `P_SCOPE_LICENSE_GAP` | `NO_WARRANTED_PREFERENCE` | `LICENSE_GAP` |
| `P_B_INCOMPARABLE` | `NO_WARRANTED_PREFERENCE` | `NATIVE_INCOMPARABILITY` |
| `P_GEOM_INC_ALL_EQ` | `EQUIVALENT` | `ALL_RELEVANT_EQUIVALENT` |

`DeltaC` and `collateral` remain ignored by this supplied lexicographic contract.

---

# 20. Frozen target relations for `G_COMP_EXPLICIT`

Mandatory cases:

| profile | expected `R_pref` | expected reason |
|---|---|---|
| `P_EQ` | `EQUIVALENT` | `ALL_RELEVANT_EQUIVALENT` |
| `P_DV_I_ONLY` | `PREFER_I` | `ALIGNED_OBJECTIVES` |
| `P_DV_J_ONLY` | `PREFER_J` | `ALIGNED_OBJECTIVES` |
| `P_ALIGN_I` | `PREFER_I` | `ALIGNED_OBJECTIVES` |
| `P_ALIGN_J` | `PREFER_J` | `ALIGNED_OBJECTIVES` |
| `P_CONFLICT_I_BURDEN` | `PREFER_I` | `AUTHORIZED_TRADEOFF` |
| `P_CONFLICT_J_BURDEN` | `PREFER_J` | `AUTHORIZED_TRADEOFF` |
| `P_DV_LICENSE_GAP` | `NO_WARRANTED_PREFERENCE` | `LICENSE_GAP` |
| `P_SCOPE_LICENSE_GAP` | `NO_WARRANTED_PREFERENCE` | `LICENSE_GAP` |
| `P_B_INCOMPARABLE` | `NO_WARRANTED_PREFERENCE` | `NATIVE_INCOMPARABILITY` |
| `P_GEOM_GAP_IGNORED` | `PREFER_I` | `ALIGNED_OBJECTIVES` |

The audit must state explicitly that `AUTHORIZED_TRADEOFF` means only “authorized by the supplied calibration contract.”

It does not mean “normatively justified by empirical evidence.”

---

# 21. Cross-governance dependence control

The same relation profile may legitimately yield different candidate-level relations under different supplied governance contracts.

The frozen discriminant is:

```text
profile = P_CONFLICT_I_BURDEN
```

Required outputs:

```text
G_PARTIAL_EMPTY      -> NO_WARRANTED_PREFERENCE / NO_TRADEOFF_AUTHORITY
G_CONSTRAINT_B       -> PREFER_J / CONSTRAINT_BLOCK_I
G_LEX_DV_REOPEN_B    -> PREFER_I / LEXICOGRAPHIC_PRIORITY
G_COMP_EXPLICIT      -> PREFER_I / AUTHORIZED_TRADEOFF
```

This control demonstrates:

\[
\boxed{
\mathcal R\text{ alone does not determine }R_{\rm pref}.
}
\]

Different output under different `G_pref` is not authority injection because the authoritative input changed.

---

# 22. Positive factorization fibers

The primary architecture must deliberately collapse nuisance or non-authoritative distinctions when target preference is unchanged.

At minimum, under `G_PARTIAL_EMPTY`, the following profiles must share one governance-interface fiber:

```text
P_ALIGN_I
P_GEOM_GAP_IGNORED
P_COLL_INC_IGNORED
P_REOPEN_LICENSE_GAP
P_REOPEN_INCOMPARABLE
```

with unique target label:

```text
PREFER_I / ALIGNED_OBJECTIVES
```

Likewise:

```text
P_EQ
P_GEOM_INC_ALL_EQ
```

must share one fiber with:

```text
EQUIVALENT / ALL_RELEVANT_EQUIVALENT
```

Equivalent lawful quotient fibers must exist for the other contracts wherever ignored coordinates vary.

This prevents the positive architecture from passing factorization merely by copying the entire raw relation profile through unchanged.

---

# 23. Deliberate governance-aliasing controls

Three lossy governance interfaces are frozen as negative controls.

They are not candidate governance proposals.

## A1 — drop required `DeltaV`

`G_alias_drop_DeltaV` removes the `DeltaV` distinction from the governance state under `G_PARTIAL_EMPTY`.

It therefore maps:

```text
P_EQ
P_DV_I_ONLY
```

to the same governance state despite target labels:

```text
EQUIVALENT
PREFER_I
```

Required result:

```text
factorization failure detected
```

## A2 — collapse `NO_LICENSED_COMPARISON` to equality

`G_alias_NLC_as_EQ` maps a required native `NO_LICENSED_COMPARISON` to the same governance state as `EQUIVALENT`.

It therefore aliases:

```text
P_DV_LICENSE_GAP
P_EQ
```

while target labels differ:

```text
NO_WARRANTED_PREFERENCE
EQUIVALENT
```

Required result:

```text
factorization failure detected
```

## A3 — collapse `INCOMPARABLE` to equality

`G_alias_INC_as_EQ` maps required native `INCOMPARABLE` to the same governance state as `EQUIVALENT`.

It aliases:

```text
P_B_INCOMPARABLE
P_DV_I_ONLY
```

after preserving the shared `DeltaV:I_GREATER` and neutralizing only burden state.

Target labels differ:

```text
NO_WARRANTED_PREFERENCE
PREFER_I
```

Required result:

```text
factorization failure detected
```

All three alias controls must fail in every anonymous encoding.

No failed alias control may be repaired during execution.

---

# 24. Deliberate authority-injection controls

The primary interpreter must be nuisance-invariant.

Three broken interpreters are frozen only as falsifiers.

## I1 — opaque nonce tie-break

For identical:

```text
R = P_EQ
G = G_PARTIAL_EMPTY
```

construct two nuisance copies with different opaque nonce values.

Broken interpreter:

```text
nonce bit 0 -> PREFER_I
nonce bit 1 -> PREFER_J
```

Required:

```text
authority injection detected
```

The primary interpreter must emit:

```text
EQUIVALENT
```

for both.

## I2 — provenance-sensitive preference

Hold `R` and governance semantics fixed while changing only a synthetic provenance label.

Broken interpreter changes candidate-level preference based on provenance.

Required:

```text
authority injection detected
```

## I3 — candidate-handle lexical tie-break

Hold relation orientation and governance semantics fixed while replacing anonymous candidate handles.

Broken interpreter prefers the lexicographically smaller handle.

Required:

```text
authority injection detected
```

The primary interpreter must not read candidate handles.

---

# 25. Anonymous encodings

Every base calibration assertion, factorization control, and injection control is run over:

```text
64 anonymous encodings
```

Each encoding may permute or rename only nuisance structure:

```text
candidate handles
synthetic provenance labels
fixture IDs
contract display IDs while preserving contract semantics
serialization order
mapping insertion order
opaque nonce labels where nonce is not authoritative
implementation branch tags
```

It must not change:

```text
native relation semantics
coordinate identity
Gamma_license
Gamma_constraint
Gamma_objective
Gamma_tradeoff
expected L_G
```

The positive output must be invariant under every licensed nuisance transformation.

---

# 26. Pair-swap law

For each calibration profile, construct the swapped relation profile by:

```text
I_GREATER <-> J_GREATER
EQUIVALENT -> EQUIVALENT
INCOMPARABLE -> INCOMPARABLE
NO_LICENSED_COMPARISON -> NO_LICENSED_COMPARISON
```

Governance semantics are swapped only in candidate role, not changed substantively.

Candidate-level outputs must obey:

```text
PREFER_I <-> PREFER_J
EQUIVALENT -> EQUIVALENT
NO_WARRANTED_PREFERENCE -> NO_WARRANTED_PREFERENCE
```

Reason-code swap law:

```text
CONSTRAINT_BLOCK_I <-> CONSTRAINT_BLOCK_J
all other reason codes remain semantically identical
```

Pair-swap is a hard regression control.

---

# 27. Contract-semantic invariance

A semantically identical governance contract with:

```text
different contract ID
different field serialization order
different human-readable aliases
```

must produce the same governance-interface states and preference outputs.

Only the semantic content of:

```text
Gamma_license
Gamma_constraint
Gamma_objective
Gamma_tradeoff
```

has preference authority.

This is distinct from comparing different governance contracts, which may legitimately yield different outputs.

---

# 28. Typed abstention as failure-locus preservation

The child result must preserve the following layer distinction:

| observed native/governance condition | candidate-level result | failure locus |
|---|---|---|
| required `NO_LICENSED_COMPARISON` | `NO_WARRANTED_PREFERENCE / LICENSE_GAP` | native evidence/license |
| required `INCOMPARABLE` | `NO_WARRANTED_PREFERENCE / NATIVE_INCOMPARABILITY` | native relational partiality |
| licensed conflicting objectives with no tradeoff clause | `NO_WARRANTED_PREFERENCE / NO_TRADEOFF_AUTHORITY` | governance |

The execution may serialize a descriptive `failure_locus` field from:

```text
NONE
NATIVE_LICENSE
NATIVE_PARTIALITY
GOVERNANCE
```

It must not execute a repair.

It must not acquire evidence.

It must not modify `G_pref`.

Thus this gate tests typed diagnosis only.

---

# 29. Repair authority follows failure locus — non-execution assertion

The result note may state the following architectural rule as a frozen diagnostic boundary:

\[
\boxed{
\textbf{repair authority follows failure locus.}
}
\]

But no repair is executed.

Forbidden cross-layer reactions include:

```text
LICENSE_GAP -> invent tradeoff weights
NATIVE_INCOMPARABILITY -> rewrite measurement values
NO_TRADEOFF_AUTHORITY -> impute missing native relations
GOVERNANCE failure -> widen measurement scope
```

This rule is tested only as absence of illegal repair behavior in the child executable.

---

# 30. Competing aggregation families are controls, not winners

The four primary supplied governance families intentionally represent different mechanisms:

```text
partial-order preserving
constraint-first
lexicographic
explicit finite compensatory lookup
```

The execution may report their calibration results separately.

It must not rank governance families.

It must not compute:

```text
best governance contract
accuracy-based governance winner
Pareto frontier over G_pref
B_G-normalized preference quality
contract leaderboard
```

All primary contracts are calibration environments.

No observed success grants one family normative priority over another.

---

# 31. Wrong-control panel

The following shortcuts are explicitly forbidden in the primary path and must be represented as negative controls or hard type assertions.

## W1 — native no-license neutralization

Forbidden:

```text
NO_LICENSED_COMPARISON -> EQUIVALENT
NO_LICENSED_COMPARISON -> neutral support
```

## W2 — native incomparability tie

Forbidden:

```text
INCOMPARABLE -> EQUIVALENT
```

on a required objective.

## W3 — missing relation penalty

Forbidden:

```text
NO_LICENSED_COMPARISON -> numeric penalty
```

## W4 — Scope compensation

Forbidden:

```text
Scope relation -> positive/negative utility contribution
```

Scope may license or fail to license only according to the supplied contract.

## W5 — one favorable objective implies global preference

Forbidden when another authorized objective conflicts and no tradeoff authority exists.

## W6 — post-hoc weights

No weight, priority edge, or tradeoff clause may be added after calibration outcomes are observed.

## W7 — actual graph tuning

Forbidden:

```text
actual 12-candidate graph -> G_pref
```

## W8 — provenance preference

Candidate or fixture provenance cannot supply direction unless explicitly part of `G_pref`; no primary contract grants it authority.

## W9 — tradeoff success implies tradeoff justification

Forbidden inference:

```text
supplied tradeoff produced expected preference
-> supplied tradeoff is normatively warranted
```

## W10 — hidden nuisance tie-break

Any dependence on candidate handle, nonce, serialization, implementation path, or alias is authority injection.

---

# 32. Reference target and implementation separation

The expected `L_G` labels in Sections 17–20 are frozen data.

The child executable must implement the primary governance interface and candidate-level interpreter separately from that expected-label registry.

The implementation must not call the expected-label table to produce its outputs.

The expected-label table may only be used after output generation for verification.

This prevents the calibration from reducing to direct answer lookup.

---

# 33. Factorization implementation requirement

For each primary contract:

1. compute `q_G(R)` from the primary governance interface for every profile in that contract's frozen domain;
2. group profiles by canonical `q_G`;
3. inspect only the preregistered target labels after grouping;
4. verify every fiber contains exactly one target preference status and compatible warrant semantics;
5. construct the induced `h_G` mapping from governance state to target status only after uniqueness is established;
6. hard-fail if any fiber contains multiple target statuses.

The result must include:

```text
fiber_count
max_fiber_size
multi_label_fiber_count
factorization_pass
```

for each primary governance contract.

The alias controls must produce:

```text
multi_label_fiber_count >= 1
factorization_pass = false
```

in every encoding.

---

# 34. Nuisance-invariance implementation requirement

For every primary fixture and governance contract:

1. generate two or more nuisance variants with identical authorized semantic inputs;
2. compute `q_G` and `R_pref` independently;
3. verify exact equality of governance state and preference output;
4. repeat under all 64 anonymous encodings.

The result must include exact counts for:

```text
candidate_handle_invariance
provenance_invariance
serialization_invariance
contract_alias_invariance
implementation_tag_invariance
```

The deliberately nuisance-sensitive broken interpreters must disagree in every targeted encoding.

---

# 35. No scalarization

The preference-identification gate consumes native relation tokens plus supplied governance semantics.

It does not reconstruct measurement magnitudes.

It does not assign numeric values to:

```text
I_GREATER
J_GREATER
EQUIVALENT
INCOMPARABLE
NO_LICENSED_COMPARISON
PREFER_I
PREFER_J
NO_WARRANTED_PREFERENCE
```

No weighted sum exists.

No common scale exists.

No utility function exists.

No `Q_extension` exists.

---

# 36. `Q_extension` remains undefined

The branch after this preregistration remains:

\[
\boxed{
\mathcal V
\rightarrow
\mathcal R_{\rm compare}
\rightarrow
G_{\rm pref}
\rightarrow
R_{\rm pref}
\rightarrow
Q_{\rm extension}
\rightarrow
Auth
\rightarrow
Bind.
}
\]

Only the `G_pref -> R_pref` identification relation is under test here.

The audit must not define:

```text
Q_extension(s)
Q_extension(i,j)
reward
utility
candidate score
ranking
selection policy
```

Even if preference identification succeeds, scalar sufficiency remains a separate future question.

---

# 37. Preference is not authorization

A calibrated result:

```text
PREFER_I
```

means only that the supplied governance contract identifies a candidate-level preference relation for the synthetic calibration profile.

It does not imply:

```text
AUTHORIZE_I
ADOPT_I
BIND_I
EXECUTE_I
```

The child result must hard-assert:

```text
preference_identification_performed = true
actual_candidate_preference_application_performed = false
Q_extension_defined = false
NO_WARRANTED_ADOPTION_defined = false
authorization_performed = false
binding_performed = false
execution_performed = false
```

---

# 38. Governance provenance is retained

Every result record must carry:

```text
governance_contract_id
governance_provenance = SUPPLIED_CALIBRATION_GOVERNANCE
Gamma_license checksum/canonical representation
Gamma_constraint checksum/canonical representation
Gamma_objective checksum/canonical representation
Gamma_tradeoff checksum/canonical representation
B_G structured ledger
calibration_profile_id
anonymous_encoding_id
```

Preference status alone is insufficient serialization.

A supplied tradeoff clause may never lose its supplied provenance after producing a preference.

Thus:

\[
\boxed{
\text{preference output identity}
\not\Rightarrow
\text{governance provenance identity}.
}
\]

---

# 39. Authority-conservation check

The primary mechanism is allowed to depend only on:

```text
native relation profile fields authorized by G_pref
semantic G_pref contract fields
```

Everything else is nuisance.

The child executable must instrument the decision path or use shadow perturbation to establish that changing an unauthorized field cannot change preference.

The audit therefore tests the finite-regime analogue of:

\[
\boxed{
\text{preference authority cannot outrun licensed relation + supplied governance}.
}
\]

This is not promoted as a universal law by this gate.

---

# 40. Governance aliasing and authority injection are independent

The audit must include cases showing that one defect can occur without the other.

Required:

```text
alias control:
  factorization fails
  nuisance sensitivity need not be present

injection control:
  factorization target can remain representable
  output changes under nuisance perturbation
```

The result may not collapse both under one generic failure flag.

Required top-level fields:

```text
governance_aliasing_detected_controls
authority_injection_detected_controls
primary_factorization_pass
primary_nuisance_invariance_pass
```

---

# 41. Calibration success criteria

The preference-identification gate passes only if all of the following hold:

1. the actual 12-candidate graph is not read, deserialized, or used during calibration;
2. all synthetic calibration profiles exactly match this preregistration;
3. all four supplied governance contracts exactly match this preregistration;
4. the output vocabulary is exactly the frozen four-token preference vocabulary;
5. typed reason codes are preserved;
6. every required native `NO_LICENSED_COMPARISON` produces `NO_WARRANTED_PREFERENCE / LICENSE_GAP`;
7. every required native `INCOMPARABLE` produces `NO_WARRANTED_PREFERENCE / NATIVE_INCOMPARABILITY` unless that coordinate is explicitly ignored by the supplied contract;
8. `Gamma_tradeoff = empty` is supported and unresolved conflicts remain `NO_WARRANTED_PREFERENCE`;
9. explicit supplied tradeoff clauses are applied exactly and retain supplied provenance;
10. success of a tradeoff clause is never serialized as justification of the clause;
11. all preregistered expected target relations are recovered in all 64 anonymous encodings;
12. pair-swap symmetry is exact;
13. semantic governance-contract aliasing/renaming leaves outputs invariant;
14. nuisance perturbations leave primary governance states and preferences invariant;
15. all three governance-aliasing controls fail factorization in all encodings;
16. all three authority-injection controls are detected in all encodings;
17. aliasing and injection remain separate failure types;
18. lawful quotient fibers over ignored coordinates are present and single-label;
19. no numeric scalarization, weights, candidate scores, or hidden tie-breaks enter the primary path;
20. no governance family is ranked or selected;
21. no actual candidate preference is computed;
22. no `Q_extension`, adoption, authorization, binding, or execution object is introduced.

A partial pass does not license actual-candidate preference application.

---

# 42. Failure interpretation

| observation | interpretation |
|---|---|
| actual graph is inspected | holdout contamination |
| required NLC treated as neutral | native-license collapse |
| required INC treated as tie | native-partiality collapse |
| conflict resolved under empty tradeoff authority | authority injection / hidden governance |
| same `q_G` contains multiple target labels | governance aliasing |
| identical authorized input changes under nuisance | authority injection |
| candidate provenance changes preference | provenance authority leakage |
| ignored coordinate changes preference | governance projection leakage |
| supplied tradeoff success presented as justification | authority provenance leakage |
| Scope contributes utility | type violation |
| preference becomes authorization | governance-type violation |
| all primary contracts factor and remain nuisance-invariant | preference architecture may pass in audited finite regimes |

---

# 43. Anti-scaffold boundary

This gate does not answer:

> what is the smallest governance contract?

It does preserve enough structured specification data to ask that later.

The anti-scaffold question is frozen for future work as:

\[
\boxed{\textbf{Where did the preference complexity go?}}
\]

But the child execution must not optimize or compare `B_G`.

No `mathfrak G_min` result is permitted here.

---

# 44. Recursive-governance hypothesis remains unearned

The present preregistration is motivated by the hypothesis that preference aggregation can behave as an interface over relational structure.

A successful execution may provide finite-regime evidence for two predicted failure modes:

```text
governance aliasing
authority injection
```

It does not establish a universal recursive-closure theory.

It does not establish governance reopenability.

It does not establish meta-governance repair.

It does not add a new theory layer to the repository.

---

# 45. Result serialization requirements

The later execution commit must contain exactly three new scientific artifacts:

```text
audits/extension_preference_identification_audit.py
audits/extension_preference_identification_results.json
audits/extension_preference_identification_audit.md
```

The result JSON must contain:

```text
preregistration_commit
parent_checkpoint
calibration_profile_registry
governance_contract_registry
governance_specification_ledgers
primary_fixture_results
factorization_fibers
factorization_summary
nuisance_invariance_results
alias_control_results
injection_control_results
pair_swap_results
cross_governance_dependence_result
holdout_integrity
anti_downstream_flags
```

No actual candidate graph records may appear in the result.

No actual candidate IDs may appear in the calibration payload.

---

# 46. Anti-downstream contract

The execution and result note must not compute, emit, or imply:

- preference over any of the actual 12 extension candidates;
- a best synthesized, control, or external candidate;
- Hudson/Rubi superiority or inferiority;
- Pareto dominance;
- a candidate ranking;
- a candidate score;
- a governance-family ranking;
- normative correctness of a supplied `G_pref`;
- `mathfrak G_min`;
- `Q_extension`;
- `NO_WARRANTED_ADOPTION`;
- adoption;
- authorization;
- binding;
- execution;
- post-adoption consequence;
- governance repair;
- governance reopenability.

---

# 47. Strongest permitted claim after success

If and only if all success criteria pass, the strongest permitted claim is:

\[
\boxed{
\textbf{
In the audited finite preference-calibration regimes, candidate-level preference relations are identifiable relative to explicitly supplied governance contracts: the primary governance interfaces preserve the decision distinctions required by their preregistered target relations, remain invariant to non-authoritative nuisance variables, preserve typed no-preference boundaries, and retain the provenance of supplied constraint, priority, and tradeoff structure.
}
}
\]

A successful control result may additionally state:

> Deliberately lossy governance interfaces produce preregistered governance-aliasing failures, and deliberately nuisance-sensitive interpreters produce preregistered authority-injection failures in the audited finite calibration regimes.

No broader generality claim is licensed.

---

# 48. Frozen next sequence

The empirical sequence is now:

\[
\boxed{
\begin{aligned}
\mathcal M_{\rm ext}\text{ identification}&\checkmark\\
s\mapsto\mathcal V_{\rm ext}(s)&\checkmark\\
\mathcal R_{\rm compare}\text{ identification}&\checkmark\\
\text{actual native comparison graph}&\checkmark\\
(\mathcal R^{\rm cal},G_{\rm pref})\rightarrow R_{\rm pref}
&\text{ [preregistered here]}\\
\text{preference-identification execution}
&\leftarrow\textbf{next}\\
\text{actual-candidate preference application}
&\text{ undefined}\\
Q_{\rm extension}&\text{ undefined}\\
Auth&\text{ undefined}\\
Bind&\text{ undefined}.
\end{aligned}
}
\]

The **only authorized next repository action** after this preregistration is execution of this preference-identification audit.

No dependency-ledger mutation occurs before that execution.

No actual-candidate preference application occurs before that execution.

No `Q_extension` artifact occurs before that execution.
