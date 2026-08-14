# Extension Candidate Preference Application — Preregistration

## Status

This document freezes the **mechanical application** of the already-identified preference/governance-interface architecture to the already-frozen 12-candidate native comparison graph.

Parent checkpoint:

```text
7c5bffe31b7cfae163248eadec869eb4800a059a
```

Preference/governance-interface identification preregistration:

```text
efcf3a780c50b64780ee2b21c93b7af5a8f86b5d
```

Preference/governance-interface identification execution:

```text
7c5bffe31b7cfae163248eadec869eb4800a059a
```

Exact preference-identification executable blob:

```text
b47c0884dcb7769a2ca9b934e8a9b64dad218399
```

Exact preference-identification result blob:

```text
4fab22d2a7be25b001b679fe92e67187098ce696
```

Actual-candidate native-comparator application preregistration:

```text
519073b3bd980f729a4b37e3ee79723a53587fc5
```

Actual-candidate native-comparator application execution:

```text
ca423e1029b013368c4281944af5a02678af83c5
```

Exact actual-candidate comparator executable blob:

```text
2b94247b0f5542e0bfd0cf8f163ca02384f1e546
```

Exact actual-candidate native-comparison result blob:

```text
3e332072502fa64c432b143e6d157fc1f5cd18b8
```

Comparison-identification execution:

```text
d0802137f303406c4aab1e5779af644b4cfe6b4f
```

The only object frozen here is:

\[
\boxed{
(\mathcal R_{ij},G_{\rm pref})
\longrightarrow
R_{\rm pref}^{G}(i,j)
}
\]

for every unordered pair in the already-frozen 12-candidate universe and every one of the four already-identified supplied governance contracts.

This artifact does **not** define `Q_extension`.

It does not select a governance contract.

It does not rank candidates.

It does not authorize, adopt, bind, or execute any extension.

---

# 1. Scientific boundary

The preceding branch has earned, in audited finite regimes:

\[
\boxed{
\mathcal M_{\rm ext}\checkmark
\rightarrow
s\mapsto\mathcal V_{\rm ext}(s)\checkmark
\rightarrow
\mathcal R_{\rm compare}\checkmark
\rightarrow
\text{actual native candidate graph}\checkmark
\rightarrow
(G_{\rm pref}\rightarrow R_{\rm pref})\checkmark
}
\]

where the final preference-identification result is explicitly **relative to supplied governance contracts**.

The present question is narrower and purely applicative:

> What candidate-level preference relations are produced when the frozen, already-identified preference interpreters are applied verbatim to the frozen actual native comparison profiles under each frozen supplied governance contract?

The governing separation remains:

\[
\boxed{
\text{native relation profile}
\neq
\text{candidate preference}
\neq
\text{governance-contract selection}
\neq
Q_{\rm extension}
\neq
\text{authorization}.
}
\]

The strongest permitted claim after a successful execution is:

\[
\boxed{
\textbf{
The frozen supplied governance contracts yield the reported candidate-level preference relations over the preregistered 12-candidate native comparison graph, with typed no-preference boundaries, contract-relative semantics, and governance provenance preserved.
}
}
\]

No broader claim is permitted.

---

# 2. The former holdout becomes application input, not calibration data

The actual 12-candidate graph was held out completely from the preference-identification calibration at `efcf3a7` / `7c5bffe`.

That calibration boundary remains historically fixed.

This application is the **first permitted preference-stage read** of the actual graph.

The child execution may read and decode:

```text
audits/extension_candidate_comparator_application_results.json
```

only as the frozen application input.

It may not use any actual pair result to alter, tune, fit, simplify, expand, prune, reinterpret, or select:

```text
Gamma_license
Gamma_constraint
Gamma_objective
Gamma_tradeoff
preference output vocabulary
warrant reason vocabulary
failure-locus mapping
preference interpreter logic
```

Thus the historical anti-leakage invariant remains:

\[
\boxed{
\text{actual candidate graph}
\not\rightarrow
G_{\rm pref}.
}
\]

The only allowed direction is now:

\[
\boxed{
(\text{frozen actual graph},\text{ frozen }G_{\rm pref})
\rightarrow
\text{application result}.
}
\]

If the actual graph exposes an undesirable or surprising consequence of a supplied governance contract, that consequence must be reported as-is.

It may not be repaired during this execution.

Any later governance revision would require a new, separately preregistered scientific object.

---

# 3. Frozen candidate universe

The 12 candidate IDs remain exactly:

```text
CTRL_ALIAS_A
CTRL_ID_DEG2
CTRL_ID_LINEAR
CTRL_SUPPLIED_DEG2
EXT_CT_A
EXT_CT_B
EXT_CT_C1
EXT_CT_C2
SYN_A_120
SYN_B_50
SYN_C1_1653
SYN_C2_2388
```

No candidate may be added, deleted, merged, aliased, deduplicated, or pruned before preference application.

Provenance remains lineage metadata only:

```text
CONTROL       4
EXTERNAL      4
SYNTHESIZED   4
TOTAL        12
```

No supplied governance contract grants candidate provenance preference authority.

Therefore provenance may not directly alter `R_pref` once the native relation profile and governance semantics are fixed.

---

# 4. Frozen pair universe

Let `IDS` be the lexicographically sorted candidate vector above.

The child execution must reconstruct the unordered pair universe exactly as:

```python
pairs = list(itertools.combinations(IDS, 2))
```

Therefore:

\[
\boxed{
|\mathfrak P_{\rm actual}|=\binom{12}{2}=66.
}
\]

The canonical compact-JSON pair-list SHA-256 remains:

```text
76ae7638e225973f21b90605a9c020a74e752143d1dd008bd2f894fdbd4629aa
```

Every one of the 66 pairs must remain present even if:

- all four governance contracts produce `NO_WARRANTED_PREFERENCE`;
- the pair contains an external/Hudson composite;
- several native coordinates are `NO_LICENSED_COMPARISON`;
- one or more native coordinates are `INCOMPARABLE`;
- the pair appears structurally redundant;
- another pair has the same native relation profile.

No pair-level pruning is permitted.

---

# 5. Frozen native relation-profile input

For each pair `(i,j)`, the child execution must read exactly the six already-computed native relations from the actual-candidate comparator application result at `ca423e1`.

Coordinate order remains:

```text
DeltaV
B
DeltaC
collateral
reopen
Scope
```

Thus:

\[
\boxed{
\mathcal R_{ij}
=
(R_{\Delta V},R_B,R_{\Delta C},R_{\rm collateral},R_{\rm reopen},R_{\rm scope}).
}
\]

Each coordinate token must belong to the already-frozen native alphabet:

\[
\boxed{
\Sigma_R=
\{
\texttt{I_GREATER},
\texttt{J_GREATER},
\texttt{EQUIVALENT},
\texttt{INCOMPARABLE},
\texttt{NO_LICENSED_COMPARISON}
\}.
}
\]

The preference-application child must **not** recompute candidate measurements, comparison licenses, native relations, causal contrasts, burden ledgers, geometry sets, collateral vectors, reopenability vectors, or scope relations.

The actual native graph is an immutable upstream object.

Any mismatch between the decoded graph and its frozen pair/coordinate integrity assertions is a hard failure.

---

# 6. Frozen governance-contract universe

Exactly four supplied governance contracts are applied:

```text
G_PARTIAL_EMPTY
G_CONSTRAINT_B
G_LEX_DV_REOPEN_B
G_COMP_EXPLICIT
```

No fifth contract may be introduced.

No contract may be omitted because it produces many abstentions, few directions, or counterintuitive actual-candidate relations.

No contract may be selected as the application default.

These contracts are **application environments**, not governance candidates being ranked.

Each retains:

```text
governance_provenance = SUPPLIED_CALIBRATION_GOVERNANCE
```

The child execution must verify the exact canonical semantic checksums from the preference-identification result before applying any contract.

## 6.1 `G_PARTIAL_EMPTY`

Frozen semantic checksums:

```text
Gamma_license
  2be736e8f664592d3a43f45b3a30799b73357629938874074376a78772a628ae
Gamma_constraint
  4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
Gamma_objective
  277c804789e20a50052a8033a75b1c6817e8eb99c487bd30839df554ba48c5ef
Gamma_tradeoff
  4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
```

Structured governance ledger:

```text
required_license_clauses       3
constraint_clauses             0
objective_orientation_clauses  2
priority_edges                 0
explicit_tradeoff_clauses      0
```

## 6.2 `G_CONSTRAINT_B`

Frozen semantic checksums:

```text
Gamma_license
  2be736e8f664592d3a43f45b3a30799b73357629938874074376a78772a628ae
Gamma_constraint
  9a2f7382a8a1fe8abad8e4ab2decbc8e3a42a26ca111573d4d511c3b3ba4f102
Gamma_objective
  c817327b78d60c26c4e8bb5b6739ef4c434eeaa0a1049b0ea3bf1736f99940e4
Gamma_tradeoff
  4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
```

Structured governance ledger:

```text
required_license_clauses       3
constraint_clauses             1
objective_orientation_clauses  1
priority_edges                 0
explicit_tradeoff_clauses      0
```

## 6.3 `G_LEX_DV_REOPEN_B`

Frozen semantic checksums:

```text
Gamma_license
  ca5ed7838919416845c2609fd390b8ebbee89f095fd1118625672119f315eda1
Gamma_constraint
  4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
Gamma_objective
  cded039bd3bb024e2ab0ffeddc4f5333b72ed80601571919852c1b81f69249ee
Gamma_tradeoff
  4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
```

Structured governance ledger:

```text
required_license_clauses       4
constraint_clauses             0
objective_orientation_clauses  3
priority_edges                 2
explicit_tradeoff_clauses      0
```

## 6.4 `G_COMP_EXPLICIT`

Frozen semantic checksums:

```text
Gamma_license
  2be736e8f664592d3a43f45b3a30799b73357629938874074376a78772a628ae
Gamma_constraint
  4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
Gamma_objective
  277c804789e20a50052a8033a75b1c6817e8eb99c487bd30839df554ba48c5ef
Gamma_tradeoff
  c2e284013bc09e194e33f796a877ee95bf533847e3163f33063b0d6e7109860c
```

Structured governance ledger:

```text
required_license_clauses       3
constraint_clauses             0
objective_orientation_clauses  2
priority_edges                 0
explicit_tradeoff_clauses      2
```

The successful preference-identification audit established only that these interpreters are identifiable **relative to their supplied semantics** in the audited calibration regimes.

Application success must not be presented as evidence that any one of these contracts is normatively correct.

---

# 7. Governance semantics are immutable during application

The preference-application child must use the already-identified governance-state construction and preference interpreter from `7c5bffe` verbatim in semantics.

For each contract `G` and actual relation profile `R_ij`, application is:

\[
\boxed{
\mathcal R_{ij}
\xrightarrow{G}
q_G(\mathcal R_{ij})
\xrightarrow{h_G}
R_{\rm pref}^{G}(i,j).
}
\]

The child executable may re-express the frozen logic locally for reproducibility, but it must hard-assert semantic identity using the frozen contract checksums and preference-identification executable/result anchors above.

It may not:

```text
add a license requirement
remove a license requirement
change an objective orientation
change burden from objective to constraint or vice versa
change lexicographic priority
add or delete a tradeoff clause
infer a new tradeoff clause from the actual graph
change how NLC is handled
change how INCOMPARABLE is handled
change how Scope is typed
change reason-code semantics
```

No actual-candidate outcome may trigger a governance edit inside this gate.

---

# 8. Application universe

Each of the 66 candidate pairs is evaluated under all four frozen governance contracts.

Therefore the child execution must produce exactly:

\[
\boxed{
66\times4=264
}
\]

candidate-pair-governance application records.

There is no prefilter such as:

```text
apply only contracts that can decide the pair
skip Hudson pairs
skip cross-parent pairs
skip pairs containing native NLC
skip pairs containing native INC
apply only one governance family
```

A `NO_WARRANTED_PREFERENCE` result remains an application record.

It is not missing data.

---

# 9. Frozen preference output vocabulary

Every one of the 264 application records must emit exactly one status from:

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

No application record may emit:

```text
WINNER
BETTER
BEST
ADOPT
REJECT
AUTHORIZE
SCORE
UTILITY
RANK
```

The token `PREFER_I` means only:

> under this particular supplied governance contract, the frozen native relation profile yields a candidate-level preference relation favoring the first member of the canonical pair.

It is not authorization.

The token `EQUIVALENT` is contract-relative candidate-level preference equivalence.

It does not imply equality of native measurements or global candidate identity.

---

# 10. Frozen warrant and failure-locus vocabulary

Every application output must retain exactly one primary warrant code from the already-identified set:

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

Every record may additionally carry the frozen descriptive failure locus:

```text
NONE
NATIVE_LICENSE
NATIVE_PARTIALITY
GOVERNANCE
```

The child may not introduce a generic `UNCERTAIN` or `FAILED` category that collapses these types.

The following distinctions remain structural:

\[
\boxed{
\texttt{NO_LICENSED_COMPARISON}
\neq
\texttt{INCOMPARABLE}
\neq
\texttt{NO_WARRANTED_PREFERENCE}.
}
\]

And at the preference layer:

```text
NO_WARRANTED_PREFERENCE / LICENSE_GAP
!=
NO_WARRANTED_PREFERENCE / NATIVE_INCOMPARABILITY
!=
NO_WARRANTED_PREFERENCE / NO_TRADEOFF_AUTHORITY
```

The child must preserve those reason/failure-locus differences even when the preference status token is identical.

---

# 11. Contract-specific application semantics remain exactly frozen

## 11.1 `G_PARTIAL_EMPTY`

Required native coordinates:

```text
DeltaV
B
Scope
```

Preference-authoritative objectives:

```text
DeltaV : greater supports same candidate
B      : lower supports lower-burden candidate
```

Tradeoff authority:

```text
empty
```

Therefore a licensed DeltaV/B conflict remains:

```text
NO_WARRANTED_PREFERENCE / NO_TRADEOFF_AUTHORITY
```

No actual-candidate conflict may cause a compensation rule to appear.

## 11.2 `G_CONSTRAINT_B`

Required native coordinates:

```text
DeltaV
B
Scope
```

Burden retains the frozen non-compensable pair-relative constraint semantics.

If exactly one candidate is burden-blocked **after all required license/partiality checks pass**, the other candidate receives the contract-relative preference.

This remains supplied governance, not an empirical claim that burden should generally be a hard constraint.

## 11.3 `G_LEX_DV_REOPEN_B`

Required native coordinates:

```text
DeltaV
reopen
B
Scope
```

All required coordinates must first be licensed and non-incomparable according to the frozen interpreter.

Only then is the frozen priority order applied:

```text
DeltaV > reopen > B
```

Lower-priority missingness or incomparability may not be ignored merely because a higher-priority direction exists.

## 11.4 `G_COMP_EXPLICIT`

Required native coordinates:

```text
DeltaV
B
Scope
```

Exactly the two previously supplied conflict clauses remain available:

```text
T1: DeltaV supports I AND B supports J -> PREFER_I
T2: DeltaV supports J AND B supports I -> PREFER_J
```

No numeric weights may be inferred.

No clause may be generalized beyond its frozen symbolic condition.

An `AUTHORIZED_TRADEOFF` warrant means only:

> the actual pair matched a tradeoff clause that had already been explicitly supplied before actual-candidate preference application.

It does not mean the tradeoff is empirically justified.

---

# 12. Cross-governance disagreement is an output, not a defect

For each actual candidate pair, the application produces a four-contract preference vector:

\[
\boxed{
\mathbf R^{\rm pref}_{ij}
=
(
R_{ij}^{G_{\rm PARTIAL\_EMPTY}},
R_{ij}^{G_{\rm CONSTRAINT\_B}},
R_{ij}^{G_{\rm LEX}},
R_{ij}^{G_{\rm COMP}}
).
}
\]

The four entries may differ.

Such disagreement is not authority injection because the authoritative governance input differs.

The child may report:

```text
per-pair four-contract preference vector
per-contract counts of preference statuses
per-contract counts of warrant reasons
per-contract counts of failure loci
number of pairs with unanimous four-contract status
number of pairs with cross-governance status disagreement
number of pairs with cross-governance directional disagreement
```

These are descriptive application-topology summaries only.

The child may **not** resolve disagreement by:

```text
majority vote over governance contracts
meta-Pareto over governance contracts
contract weighting
contract voting
contract ranking
selecting the most decisive contract
selecting the contract with fewest abstentions
selecting the contract that favors a particular candidate
```

There is no meta-governance layer in this gate.

---

# 13. No per-candidate score may be induced from pairwise preferences

The child must not compute or report:

```text
candidate win count
candidate loss count
candidate abstention-adjusted win rate
candidate outdegree
candidate indegree
Copeland score
Borda score
Condorcet winner
Elo-like score
Bradley-Terry score
rank centrality
transitive closure ranking
pairwise-victory leaderboard
```

The pairwise preference graphs remain typed relation objects.

They are not converted into candidate scores.

This prevents a scalar `Q_extension` surrogate from entering through graph summary statistics.

---

# 14. No transitive completion

The child may not infer a relation for `(i,k)` from relations on `(i,j)` and `(j,k)`.

Every actual candidate preference record must arise only from the directly frozen native profile for that pair under the directly frozen governance contract.

Thus:

\[
R_{\rm pref}^{G}(i,j)
\land
R_{\rm pref}^{G}(j,k)
\not\Rightarrow
R_{\rm pref}^{G}(i,k)
\]

unless the `(i,k)` relation is independently produced by its own application record.

No transitivity assumption is tested or imposed here.

---

# 15. Pair-swap law

For every one of the 264 primary records, the child must construct the candidate-role-swapped native profile and recompute the frozen preference interpreter.

Required preference swap law:

```text
PREFER_I  <-> PREFER_J
EQUIVALENT -> EQUIVALENT
NO_WARRANTED_PREFERENCE -> NO_WARRANTED_PREFERENCE
```

Required warrant swap law:

```text
CONSTRAINT_BLOCK_I <-> CONSTRAINT_BLOCK_J
all other warrant codes retain semantic identity
```

This must hold exactly for all 264 application records.

The swapped record is a regression control only; the canonical output universe remains the 66 lexicographically ordered pairs.

---

# 16. Provenance and nuisance invariance remain hard controls

Candidate provenance is retained in serialization for lineage but is not authorized by any frozen governance contract.

For each actual pair/contract record, the child must construct shadow copies that alter only non-authoritative application metadata such as:

```text
candidate provenance display label
candidate human-readable alias
serialization order
contract display alias
implementation tag
opaque nonce
```

while preserving:

```text
native six-token relation profile
semantic governance contract
canonical candidate role orientation
```

The primary preference status, warrant reason, and failure locus must remain unchanged.

Any nuisance-dependent difference is an authority-injection regression failure.

No actual candidate ID may be used as a hidden tie-break.

---

# 17. Upstream integrity checks

Before producing any application output, the child must verify:

1. current parent checkpoint is the preregistration child context;
2. actual native-comparison result is anchored to blob `3e332072502fa64c432b143e6d157fc1f5cd18b8`;
3. preference-identification result is anchored to blob `4fab22d2a7be25b001b679fe92e67187098ce696`;
4. preference-identification executable is anchored to blob `b47c0884dcb7769a2ca9b934e8a9b64dad218399`;
5. candidate registry is exactly 12 IDs;
6. pair universe is exactly 66 unordered pairs;
7. canonical pair-list checksum is exact;
8. every pair contains exactly six native relation tokens;
9. every native token belongs to `Sigma_R`;
10. the four governance contracts and their semantic SHA-256 checksums match this preregistration;
11. preference-identification upstream result reports `gate_pass = true`;
12. no contract semantic field is reconstructed from actual candidate outcomes.

Any failed upstream integrity assertion fails this gate.

---

# 18. Application success criteria

The actual-candidate preference-application gate passes only if all of the following hold:

1. exactly 12 frozen candidates are present;
2. exactly 66 unordered pairs are present;
3. pair-list SHA-256 matches the frozen checksum;
4. every pair reads exactly six frozen native relations from the upstream graph;
5. no native coordinate relation is recomputed or altered;
6. exactly four frozen governance contracts are applied;
7. governance semantic checksums match exactly;
8. exactly `66 * 4 = 264` primary application records are produced;
9. every record emits exactly one frozen preference status;
10. every record carries a frozen warrant reason;
11. typed failure-locus semantics are preserved;
12. `NO_LICENSED_COMPARISON` is never neutralized, penalized, or converted to equality;
13. required `INCOMPARABLE` is never converted to a tie;
14. `Gamma_tradeoff = empty` remains capable of returning `NO_WARRANTED_PREFERENCE`;
15. the finite supplied tradeoff clauses remain exactly unchanged;
16. every supplied tradeoff result retains supplied governance provenance;
17. pair-swap relation/warrant law holds for all 264 records;
18. nuisance perturbations do not alter preference outputs;
19. no governance contract is selected or ranked;
20. no cross-governance disagreement is resolved;
21. no candidate win/loss score or pairwise leaderboard is computed;
22. no transitive completion is performed;
23. no Pareto candidate relation is computed;
24. no scalarization, utility, reward, or `Q_extension` is defined;
25. no `NO_WARRANTED_ADOPTION` object is defined;
26. no adoption, authorization, binding, or execution operation is performed.

A partial pass does not license `Q_extension` design or authorization.

---

# 19. Failure interpretation

| observation | interpretation |
|---|---|
| actual native graph modified | upstream-object violation |
| governance checksum mismatch | governance-freeze violation |
| pair omitted because undecidable | application selection leakage |
| NLC treated as neutral | native-license collapse |
| INC treated as tie | native-partiality collapse |
| empty-tradeoff conflict forcibly resolved | hidden authority injection |
| candidate provenance changes preference | provenance authority leakage |
| candidate ID breaks a tie | nuisance authority injection |
| governance disagreement majority-voted | unpreregistered meta-governance |
| candidate preference win counts computed | hidden scalar/ranking layer |
| preference relation becomes authorization | governance-type violation |
| all 264 applications reproduce frozen semantics | application gate may pass |

---

# 20. Allowed result summaries

The result JSON and note may serialize:

```text
candidate_registry
pair_registry and checksum
native_relation_profile per pair
frozen governance contract registry and semantic checksums
264 pair x governance application records
preference-status counts by governance contract
warrant-reason counts by governance contract
failure-locus counts by governance contract
pair-swap results
nuisance-invariance results
cross-governance agreement/disagreement summaries
anti-downstream flags
```

The result may also identify specific candidate pairs as examples of:

```text
contract-relative directional preference
contract-relative equivalence
NO_WARRANTED_PREFERENCE / LICENSE_GAP
NO_WARRANTED_PREFERENCE / NATIVE_INCOMPARABILITY
NO_WARRANTED_PREFERENCE / NO_TRADEOFF_AUTHORITY
cross-governance disagreement
```

provided the wording remains descriptive and contract-relative.

---

# 21. Forbidden result summaries

The result must not compute, serialize, or imply:

```text
best candidate
worst candidate
winner
recommended candidate
candidate ranking
candidate score
candidate win rate
Pareto frontier
Condorcet winner
transitive preference closure
best governance contract
most rational governance contract
most decisive governance contract
normatively correct governance contract
meta-governance vote
Q_extension
reward
utility
NO_WARRANTED_ADOPTION
adoption
authorization
binding
execution
```

No Hudson/Rubi superiority or inferiority claim is licensed from a contract-relative application result.

No synthesized-candidate superiority claim is licensed merely because one supplied governance contract prefers it in one or more pairs.

---

# 22. Governance provenance remains part of every preference record

Every application record must retain at minimum:

```text
candidate_i
candidate_j
native_relation_profile
governance_contract_id
governance_provenance = SUPPLIED_CALIBRATION_GOVERNANCE
Gamma_license checksum
Gamma_constraint checksum
Gamma_objective checksum
Gamma_tradeoff checksum
B_G structured ledger
preference_status
warrant_reason
failure_locus
```

Preference status alone is insufficient serialization.

Thus:

\[
\boxed{
R_{\rm pref}^{G_1}(i,j)
=
R_{\rm pref}^{G_2}(i,j)
\not\Rightarrow
G_1=G_2.
}
\]

Identical output under different supplied governance contracts does not erase governance lineage.

---

# 23. Contract-relative equivalence is not global equivalence

If a pair yields:

```text
EQUIVALENT
```

under one contract, this means only that the pair is candidate-level preference-equivalent under that supplied governance interface.

It does not imply:

```text
all native coordinates equal
candidate implementations identical
candidate provenance identical
same preference under another governance contract
global candidate equivalence
```

No candidate deduplication may follow from a contract-relative equivalence result.

---

# 24. Universal abstention is not candidate rejection

If a pair yields:

```text
NO_WARRANTED_PREFERENCE
```

under all four supplied governance contracts, the allowed statement is only:

> none of the four frozen supplied governance contracts yields a warranted candidate-level preference for this pair on the frozen native relation profile.

Forbidden inference:

```text
both candidates are bad
both candidates should be rejected
there is no possible governance contract that could decide
no future evidence could help
NO_WARRANTED_ADOPTION
```

The application does not quantify over all possible governance structures.

---

# 25. Cross-governance directional conflict is not an error

If one contract yields `PREFER_I` and another yields `PREFER_J` for the same actual pair, the child must preserve both relations with their governance lineage.

It must not label one as inconsistent merely because the outputs differ.

The correct representation is:

\[
\boxed{
(\mathcal R_{ij},G_1)\rightarrow\texttt{PREFER_I},
\qquad
(\mathcal R_{ij},G_2)\rightarrow\texttt{PREFER_J}.
}
\]

The authoritative input changed because `G_1 != G_2`.

The application gate does not contain an authority source for choosing between `G_1` and `G_2`.

---

# 26. Anti-scaffold / future-Q boundary

The child must not answer:

> can these pairwise contract-relative preferences be compressed into a scalar `Q_extension`?

That is a separate future scientific object.

The present gate preserves enough structure to ask later whether:

\[
\boxed{
\exists g:\quad
R_{\rm pref}=g\circ Q_{\rm extension}
}
\]

for a declared downstream decision program.

But no such `Q_extension` is constructed, tested, or assumed here.

The future anti-scaffold question remains:

\[
\boxed{
\textbf{Does a scalar }Q\textbf{ add anything over the typed preference relation?}
}
\]

This preregistration does not answer it.

---

# 27. `Q_extension` remains undefined

The empirical chain after this preregistration is:

\[
\boxed{
\mathcal V
\rightarrow
\mathcal R_{\rm compare}
\rightarrow
G_{\rm pref}
\rightarrow
R_{\rm pref}^{\rm actual}
\rightarrow
Q_{\rm extension}\;?
\rightarrow
Auth
\rightarrow
Bind.
}
\]

Only the actual-candidate application of the frozen `G_pref -> R_pref` relation is under test here.

No application success can by itself establish scalar sufficiency.

---

# 28. Preference remains distinct from authorization

A result such as:

```text
G_PARTIAL_EMPTY:
  SYN_X vs SYN_Y -> PREFER_I
```

would mean only that the frozen native relation profile and that supplied governance contract yield a pairwise preference relation.

It would not imply:

```text
AUTHORIZE_I
ADOPT_I
BIND_I
EXECUTE_I
```

The child result must hard-assert:

```text
actual_candidate_preference_application_performed = true
Q_extension_defined = false
NO_WARRANTED_ADOPTION_defined = false
authorization_performed = false
binding_performed = false
execution_performed = false
```

---

# 29. No governance-family ranking

Application completeness or decisiveness may differ across the four supplied governance contracts.

The result may report descriptive counts, including the number of `NO_WARRANTED_PREFERENCE` outputs by contract.

It may not convert those counts into:

```text
more complete = better governance
fewer abstentions = better governance
more preferences = more rational governance
agreement with another contract = validation
```

The governance contracts remain supplied experimental conditions.

---

# 30. Result serialization requirements

The later execution commit must contain exactly three new scientific artifacts:

```text
audits/extension_candidate_preference_application_audit.py
audits/extension_candidate_preference_application_results.json
audits/extension_candidate_preference_application_audit.md
```

The result JSON must contain at minimum:

```text
preregistration_commit
parent_checkpoint
upstream_blob_anchors
candidate_registry
pair_registry
pair_list_sha256
native_relation_profiles
governance_contract_registry
application_records
preference_status_counts_by_contract
warrant_reason_counts_by_contract
failure_locus_counts_by_contract
pair_swap_results
nuisance_invariance_results
cross_governance_summary
upstream_integrity
anti_downstream_flags
```

No per-candidate aggregate preference score may appear.

---

# 31. Strongest permitted claim after success

If and only if every success criterion passes, the strongest permitted claim is:

\[
\boxed{
\textbf{
The frozen supplied governance contracts yield the reported candidate-level preference relations over the preregistered 12-candidate native comparison graph, with typed no-preference boundaries, contract-relative semantics, governance provenance, pair symmetry, and nuisance invariance preserved.
}
}
\]

The result may additionally state descriptively that the same actual native relation profile can yield different candidate-level relations under different supplied governance contracts where such differences occur.

It may not claim that any governance contract is normatively correct.

It may not claim that any candidate should be adopted.

---

# 32. Frozen next sequence

The empirical sequence is now:

\[
\boxed{
\begin{aligned}
\mathcal M_{\rm ext}\text{ identification}&\checkmark\\
s\mapsto\mathcal V_{\rm ext}(s)&\checkmark\\
\mathcal R_{\rm compare}\text{ identification}&\checkmark\\
\text{actual native comparison graph}&\checkmark\\
(G_{\rm pref}\rightarrow R_{\rm pref})\text{ identification}&\checkmark\\
\boxed{(\mathcal R_{ij},G_{\rm pref})\rightarrow R_{\rm pref}^{G}(i,j)}
&\text{ [preregistered here]}\\
\text{actual-candidate preference-application execution}
&\leftarrow\textbf{next}\\
Q_{\rm extension}\text{ design/minimality}&\text{ undefined}\\
Auth&\text{ undefined}\\
Bind&\text{ undefined}.
\end{aligned}
}
\]

The **only authorized next repository action** after this preregistration is execution of this actual-candidate preference-application audit.

No dependency-ledger mutation occurs before that execution.

No `Q_extension` artifact occurs before that execution.

No governance contract is revised before that execution.
