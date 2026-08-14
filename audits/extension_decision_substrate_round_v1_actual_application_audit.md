# Decision-Substrate Language Identification — Round v1 Actual Application Audit

## Status

```text
POST_SPECIFICATION_APPLICATION_EVIDENCE
STOP_DSLI_R1
```

Preregistered at `f8a76956ecfbf4848b62659e6db23c3918311679`.

The execution passed the frozen 24,576-cell n=4 semantic conformance gate before reading the actual target blob.

## Primary 4 x 6 application surface

| governance | L_ORD1 | L_RADIUS1 | L_BANDS1 | L_INTERSECT2 | L_POSET | L_SPARSE_LINEAR |
|---|---|---|---|---|---|---|
| `G_PARTIAL_EMPTY` | `NOT_REPRESENTABLE` | `FAITHFUL_CONTRACTION` (B*=17) | `FAITHFUL_CONTRACTION` (B*=19) | `FAITHFUL_CONTRACTION` (B*=28) | `FAITHFUL_CONTRACTION` (B*=6) | `FAITHFUL_CONTRACTION` (B*=6) |
| `G_CONSTRAINT_B` | `NOT_REPRESENTABLE` | `NOT_REPRESENTABLE` | `NOT_REPRESENTABLE` | `FAITHFUL_CONTRACTION` (B*=28) | `FAITHFUL_CONTRACTION` (B*=11) | `FAITHFUL_CONTRACTION` (B*=12) |
| `G_LEX_DV_REOPEN_B` | `NOT_REPRESENTABLE` | `NOT_REPRESENTABLE` | `NOT_REPRESENTABLE` | `FAITHFUL_CONTRACTION` (B*=28) | `FAITHFUL_CONTRACTION` (B*=11) | `FAITHFUL_CONTRACTION` (B*=12) |
| `G_COMP_EXPLICIT` | `NOT_REPRESENTABLE` | `NOT_REPRESENTABLE` | `NOT_REPRESENTABLE` | `FAITHFUL_CONTRACTION` (B*=28) | `FAITHFUL_CONTRACTION` (B*=11) | `FAITHFUL_CONTRACTION` (B*=12) |

Aggregate terminal counts:

```text
FAITHFUL_CONTRACTION                           14
NOT_REPRESENTABLE                              10
```

These are descriptive application outcomes only. They do not rank or select languages or governance contracts.

## Conformance and invariance

- semantic conformance: `24576 / 24576`; mismatches `0`
- nuisance target inverse transport: `256 / 256`
- representable-witness nuisance transport: `896 / 896`
- target pair swap: `264 / 264`
- representable-witness pair swap: `924 / 924`

## Provenance and claim boundary

Evidence role: `POST_SPECIFICATION_APPLICATION_EVIDENCE`.

The actual target relations historically predate DSLI_R1; this is not pristine held-out confirmation.

No output defines a cross-language winner, language weighting/ranking, governance winner, candidate selection, `Q_extension`, authorization, binding, or execution.

## Anti-downstream state

```text
actual_target_application_performed = true
application_evidence_role = POST_SPECIFICATION_APPLICATION_EVIDENCE
application_set_modified = false
language_family_modified = false
language_semantics_modified = false
characterization_dependent_filtering = false
characterization_dependent_weighting = false
application_priority_assigned = false
cross_language_ranking_performed = false
cross_language_winner_selected = false
governance_contract_selected = false
governance_family_ranked = false
Q_extension_defined = false
candidate_ranking_performed = false
candidate_selected = false
authorization_performed = false
binding_performed = false
execution_performed = false
v2_design_update_performed = false
```

## Stop

```text
STOP_DSLI_R1
```

No v2 design update is performed in this execution.
