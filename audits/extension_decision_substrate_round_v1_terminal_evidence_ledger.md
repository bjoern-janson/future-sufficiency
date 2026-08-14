# Decision-Substrate Language Identification — Round v1 Terminal Evidence Ledger

## Status

```text
DSLI_R1_SCIENTIFIC_STATE = CLOSED
TERMINAL_V1_LEDGER       = COMMITTED
STOP_DSLI_R1             = true
```

This artifact is the terminal retrospective classification ledger for `DSLI_R1`.

It records what the completed round established, what it did not establish, and which questions remain open after the round. It does not construct, select, preregister, or authorize any `v=2` object.

The governing termination firewall is:

\[
\boxed{
\texttt{TERMINAL\_V1\_LEDGER}
\not\rightarrow
\texttt{V2\_DESIGN}
}
\]

inside this scientific operation.

No new treatment language, decoder, authority regime, burden regime, calibration world, target relation, repair operator, representation, candidate selection rule, governance rule, or experimental design is introduced here.

---

# 1. Scientific lineage

The terminal scientific lineage is:

```text
round-v1 construction
  6482667d3b48c2e0c47bfea2fb44da92187b0511

round-v1 SpecComplete
  0f2e2e9cf38258b583dc3d7f9bbbf2cd047fcf53

characterization
  ddffe4b976352b3fec4efc3300a0dcc0097ca217

identity application-set carry-forward
  f0c594bc9ed70856ec980a06926275584db79086

actual-application preregistration
  f8a76956ecfbf4848b62659e6db23c3918311679

actual application / terminal execution
  a4eac05b9387e46bebf2008b3cfb57f3e375577f
```

The scientific state graph is therefore:

\[
\boxed{
\text{frozen design}
\rightarrow
\text{characterization}
\rightarrow
\text{identity carry-forward}
\rightarrow
\text{preregistered application}
\rightarrow
\text{application evidence}
\rightarrow
\text{terminal classification}
\rightarrow
\mathbf{STOP}.
}
\]

Git ancestry may contain repository-administration history that does not define additional scientific versions. Scientific state is determined by the explicit checkpoints above.

---

# 2. Evidence classes remain distinct

The terminal ledger contains two completed empirical evidence classes:

```text
CALIBRATION_EVIDENCE
POST_SPECIFICATION_APPLICATION_EVIDENCE
```

They are not interchangeable:

\[
\boxed{
\texttt{CALIBRATION\_EVIDENCE}
\neq
\texttt{POST\_SPECIFICATION\_APPLICATION\_EVIDENCE}.
}
\]

The calibration world was frozen as part of `DSLI_R1` construction and used to characterize the six fixed treatment languages.

The actual application used already-existing governance-relative preference relations. Those target relations historically predate the `DSLI_R1` language architecture. Therefore the application is not labeled pristine held-out confirmation.

No terminal claim may silently promote the application evidence to a stronger provenance class.

---

# 3. Frozen treatment family

The complete round-v1 treatment family remained unchanged through characterization, application-set carry-forward, preregistration, and application:

```text
L_ORD1
L_RADIUS1
L_BANDS1
L_INTERSECT2
L_POSET
L_SPARSE_LINEAR
```

Equivalently:

\[
\boxed{
\mathfrak L_{\rm app}^{(1)}
=
\mathfrak L_{\rm DS}^{(1)}.
}
\]

Characterization output did not filter, weight, rank, prioritize, add, remove, widen, narrow, repair, or retune any treatment before application.

---

# 4. Calibration evidence ledger

The frozen characterization world contains:

```text
26 anonymous calibration relations
x
6 treatment languages
=
156 treatment cells
```

Terminal calibration counts:

```text
NOT_REPRESENTABLE                         102
REPRESENTABLE_AUTHORITY_INVALID            0
ADMISSIBLE_REPRESENTATION_NO_CONTRACTION   8
FAITHFUL_CONTRACTION                       46
```

Per-language calibration outcomes:

| Language | Representable | FC | ARNC | NR |
|---|---:|---:|---:|---:|
| `L_ORD1` | 2/26 | 2 | 0 | 24 |
| `L_RADIUS1` | 10/26 | 10 | 0 | 16 |
| `L_BANDS1` | 11/26 | 11 | 0 | 15 |
| `L_INTERSECT2` | 13/26 | 5 | 8 | 13 |
| `L_POSET` | 14/26 | 14 | 0 | 12 |
| `L_SPARSE_LINEAR` | 4/26 | 4 | 0 | 22 |

Controls separately instantiated the authority-invalid and admissible-no-contraction states:

```text
W_DIRECT_LOOKUP
  representable and authority-valid
  B_star = B_R + 1
  -> ADMISSIBLE_REPRESENTATION_NO_CONTRACTION

W_IDENTITY_ORACLE
  extensionally representable
  authority-invalid by UNLICENSED_CANDIDATE_IDENTITY
  -> REPRESENTABLE_AUTHORITY_INVALID
```

Thus the round maintained the separation:

\[
\boxed{
\text{expressivity}
\neq
\text{authority validity}
\neq
\text{contraction}.
}
\]

## 4.1 Calibration findings retained at terminal classification

Within the frozen matched calibration support:

- directional cyclicity changed closure for the five order/partial-order-derived languages tested on the preregistered matched cases;
- lawful versus nontransitive equivalence separated the five languages that admit equivalence under their frozen semantics;
- transitivity requirements were distinguished from bounded explicit direct relational storage;
- abstention topology changed closure in preregistered local contrasts, with `L_BANDS1` showing a candidate-count-specific exception;
- greater raw resolved-edge cardinality was not a monotone proxy for representational difficulty on the matched cardinality-stress cases;
- connectivity was a null discriminant on its tested matched support;
- product-geometry terminal states did not support a one-factor causal attribution;
- exact representability and contraction were empirically separated by eight `L_INTERSECT2` ARNC cells.

These remain finite, frozen-support characterizations rather than universal representation theorems.

---

# 5. Post-specification application evidence ledger

The actual application universe contains:

```text
4 frozen governance-relative actual relations
x
6 carried-forward treatment languages
=
24 primary application cells
```

The four frozen governance contracts are:

```text
G_PARTIAL_EMPTY
G_CONSTRAINT_B
G_LEX_DV_REOPEN_B
G_COMP_EXPLICIT
```

The terminal application surface is:

| governance | L_ORD1 | L_RADIUS1 | L_BANDS1 | L_INTERSECT2 | L_POSET | L_SPARSE_LINEAR |
|---|---|---|---|---|---|---|
| `G_PARTIAL_EMPTY` | `NR` | `FC` (B*=17) | `FC` (B*=19) | `FC` (B*=28) | `FC` (B*=6) | `FC` (B*=6) |
| `G_CONSTRAINT_B` | `NR` | `NR` | `NR` | `FC` (B*=28) | `FC` (B*=11) | `FC` (B*=12) |
| `G_LEX_DV_REOPEN_B` | `NR` | `NR` | `NR` | `FC` (B*=28) | `FC` (B*=11) | `FC` (B*=12) |
| `G_COMP_EXPLICIT` | `NR` | `NR` | `NR` | `FC` (B*=28) | `FC` (B*=11) | `FC` (B*=12) |

Aggregate terminal application counts:

```text
FAITHFUL_CONTRACTION                       14
NOT_REPRESENTABLE                          10
ADMISSIBLE_REPRESENTATION_NO_CONTRACTION    0
REPRESENTABLE_AUTHORITY_INVALID             0
```

These are descriptive application outcomes only.

The repeated application phenotype:

```text
(NR, NR, NR, FC, FC, FC)
```

for `G_CONSTRAINT_B`, `G_LEX_DV_REOPEN_B`, and `G_COMP_EXPLICIT` is recorded as repeated behavior of three frozen target relations under the six frozen languages.

It is not promoted to three independent confirmations of one generating mechanism.

---

# 6. Application execution integrity

The application executor was required to demonstrate semantic conformance before actual-target access.

The terminal execution passed:

```text
n=4 complete four-token conformance cells   24576 / 24576
semantic mismatches                              0
```

Application nuisance and symmetry checks passed:

```text
nuisance target inverse transport          256 / 256
representable-witness nuisance transport   896 / 896
target pair swap                           264 / 264
representable-witness pair swap            924 / 924
```

The authoritative application execution used the frozen CPython 3.12.11 runtime and is bound to the committed execution provenance at the terminal application checkpoint.

Computational inconvenience did not generate scientific negatives:

\[
\boxed{
\text{timeout / failure-to-find / resource inconvenience}
\not\rightarrow
\texttt{NOT\_REPRESENTABLE}.
}
\]

Missingness semantics remained:

\[
\boxed{
\texttt{NOT\_DEFINED}
\neq 0
\neq \infty
}
\]

and:

\[
\boxed{
\texttt{NOT\_EVALUATED}
\not\rightarrow
\text{imputation}.
}
\]

---

# 7. Claims earned by v1

The strongest terminal v1 claim is:

> **Within the frozen finite regimes, decision-substrate closure and contraction vary with the target relation presented under the frozen governance-relative interfaces; exact representability, authority validity, and contraction remain distinct objects.**

The completed evidence further supports the following scoped statements:

1. The six preregistered treatment languages exhibit distinct exact closure and contraction behavior on the frozen calibration support.
2. Matched calibration contrasts identify local finite sensitivities to directional topology, lawful equivalence, transitivity, and abstention topology under the frozen language semantics.
3. Raw relation cardinality is not a monotone proxy for representational difficulty on the preregistered matched cardinality-stress support.
4. Exact representability does not imply semantic contraction under the frozen burden regime.
5. The same fixed 12-candidate universe, when represented by different frozen governance-relative preference relations, yields different decision-substrate application outcomes while language semantics remain unchanged.
6. The actual application contains both exact faithful contractions and exact nonrepresentability across the fixed 4 x 6 response surface.
7. The application implementation reproduced the frozen semantic regime on the complete preregistered n=4 conformance universe before actual-target access.

These claims are finite and relative to the frozen treatment family, authority regime, burden regime, target relations, and execution procedures.

---

# 8. Claims not earned by v1

The round does not establish any of the following:

```text
universal closure theorem for any treatment language
universal ordering of treatment-language expressivity
preferred treatment language
best language
cross-language winner
cross-language ranking
cross-language utility
language adoption rule
causal effect of governance as the generating cause of application heterogeneity
three independent mechanism confirmations from the repeated application phenotype
pristine held-out confirmation on the actual target relations
actual Q_extension
candidate ranking
candidate selection
governance selection
governance winner
governance aggregation
authorization
binding
execution of any extension
unrestricted interface invention
v2 treatment family
v2 calibration world
v2 preregistration
```

In particular:

\[
\boxed{
\text{governance-relative application heterogeneity}
\neq
\text{identified causal effect of governance}.
}
\]

and:

\[
\boxed{
(\mathrm{NR},\mathrm{NR},\mathrm{NR},\mathrm{FC},\mathrm{FC},\mathrm{FC})
\text{ repeated}
\neq
\text{three independent mechanism confirmations}.
}
\]

The terminal downstream firewall remains:

\[
\boxed{
\mathrm{FC}
\not\Rightarrow
\text{preferred language}
\not\Rightarrow
Q_{\rm extension}
\not\Rightarrow
\text{authorization}.
}
\]

No `argmin B_star`, frequency of FC, calibration count, application count, or repeated phenotype is licensed as an implicit selection criterion.

---

# 9. Open post-v1 hypotheses

The following questions remain open after v1 and are recorded only as post-v1 development candidates:

```text
licensed interface-sufficiency / fiber-defect operators
oracle distinction lower bounds
preservation authority and future-relevant retention
repair versus replacement
fiber challenges for interface invention
future-horizon / reopenability structure
legibility and communication-interface questions
external critiques of the current representation program
```

Their presence in this terminal ledger means only:

```text
OPEN_AFTER_V1
```

not:

```text
V1_FAILURE
V2_REQUIREMENT
V2_SELECTED_HYPOTHESIS
V2_DESIGN
V2_AUTHORIZATION
```

The governing invariant is:

\[
\boxed{
\text{open hypothesis}
\neq
\text{v1 failure}.
}
\]

No open hypothesis receives design priority, representation choice, measurement definition, calibration case, success criterion, or implementation route in this ledger.

---

# 10. Provenance transition after closure

Only after this ledger is closed may subsequent work separately reclassify relevant terminal observations, critiques, and post-v1 conceptual developments as:

```text
DEVELOPMENT_EVIDENCE
```

for a separately designed future round.

The permitted temporal sequence is:

\[
\boxed{
\text{v1 result}
\rightarrow
\text{terminal evidence ledger}
\rightarrow
\texttt{DEVELOPMENT\_EVIDENCE}
\rightarrow
\text{separately designed v2}.
}
\]

The following edge is prohibited inside this artifact:

\[
\boxed{
\text{terminal classification}
\not\rightarrow
\text{v2 design decision}.
}
\]

Thus this ledger may become provenance for later development discussion, but it does not itself exercise future design authority.

---

# 11. Terminal authority state

The terminal round state is:

```text
DSLI_R1_SCIENTIFIC_STATE         = CLOSED
APPLICATION_EVIDENCE             = POST_SPECIFICATION_APPLICATION_EVIDENCE
Q_EXTENSION_DEFINED              = false
LANGUAGE_SELECTED                = false
GOVERNANCE_SELECTED              = false
CANDIDATE_SELECTED               = false
AUTHORIZATION                    = false
BINDING                          = false
EXTENSION_EXECUTION              = false
V2_DESIGN_AUTHORITY              = not_yet_exercised
TERMINAL_LEDGER_TO_V2_DESIGN     = prohibited
```

The v1 application result does not modify any of these downstream states.

---

# 12. Archive statement

`DSLI_R1` is archived as a completed finite scientific round.

Its terminal evidential objects are the frozen characterization evidence and the frozen post-specification application evidence, interpreted only through the claim boundaries recorded above.

No unresolved post-v1 question reopens `DSLI_R1`.

No later development hypothesis may retroactively modify the v1 language family, calibration world, application set, actual target relations, execution procedure, result surface, evidence provenance, or earned/non-earned claim boundary.

The archival invariant is:

\[
\boxed{
\textbf{v1 is history, not a live design surface.}
}
\]

Final state:

```text
STOP_DSLI_R1
DSLI_R1_SCIENTIFIC_STATE = CLOSED
```
