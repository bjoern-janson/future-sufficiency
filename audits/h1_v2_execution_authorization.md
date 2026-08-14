# H1 v2 — Execution Authorization

## Status

```text
round_id
  H1_V2_R1

preregistration_commit
  de42e3422b55a962bd16ae9fdba87447f387daa1

implementation_construction_commit
  ddfbeea03d657de909fbd2f9a1d47232f56f1642

failed_speccomplete_audit_commit
  06d20b30597eb246c1616d6b51a032d518eb7d8d

minimal_implementation_repair_commit
  c4aa7689286a7111b5d6b899eba85823c7b941d8

speccomplete_valid_checkpoint
  73215b74ecfe7d063be9f5e93f1f314b068665ad

H1_V2_IMPLEMENTATION_CONSTRUCTED    = true
H1_V2_IMPLEMENTATION_REPAIRED       = true
H1_V2_SPECCOMPLETE                  = true
H1_V2_SPECIFICATION_STATE           = SPECIFICATION_VALID
H1_V2_EXECUTION_MANIFEST_FROZEN     = true
H1_V2_EXECUTION_AUTHORIZED          = true
H1_V2_RECONSTRUCTION_EVIDENCE_SEEN  = false
H1_V2_COLLISION_EVIDENCE_SEEN       = false
BACKWARD_DESIGN_AUTHORITY           = 0
```

This artifact performs **execution authorization only**.

It does not expose a primary packet, query any reconstructor, compute or inspect the primary L2 fiber surface, inspect any collision outcome, score any reconstruction, execute the README diagnostic, or repair framework documentation.

The governing separation remains:

\[
\boxed{
\text{SpecComplete}
\neq
\text{execution authorization}
\neq
\text{scientific evidence}.
}
\]

---

# 1. Authorization question

The only question answered here is:

\[
\boxed{
\text{May the specification-valid H1 implementation now execute the already-frozen L1/L2 protocols?}
}
\]

Answer:

```text
YES — EXECUTION_AUTHORIZED
```

subject to the exact pre-access execution manifest and operational preflight below.

Authorization grants no empirical conclusion.

---

# 2. Frozen scientific object

This authorization does not change the preregistered object:

\[
\mathcal R_{\rm H1}^{(2)}
=
(
X_{\rm framework},
O_{\rm framework},
T_A,
\mathcal G_A,
\mathcal K_{\rm conformance},
\Pi_{\rm reconstruction},
\Pi_{\rm collision},
B_{\rm H1},
\Sigma_{\rm H1}
).
\]

The following remain frozen exactly as preregistered:

```text
X_framework
O_framework
O_README
T_A
T_A^core
G_A
Pi_reconstruction
Pi_collision
B_H1
Sigma_H1
state universe S01..S10
packet membership and serialization
semantic canonicalization
gold targets
constraint profiles
fixed reconstruction task prompt
allowed-token schema
L1 output ontology
L2 collision criterion
README diagnostic status
claim authority
```

Thus:

\[
\boxed{
\text{execution authorization}
\neq
\text{scientific design revision}.
}
\]

---

# 3. Bound pre-access reconstructor panel

The preregistration requires at least three independently hosted general-purpose reconstructors and requires their identities to be bound before the first packet exposure.

The authorized panel is exactly:

| ID | provider / host | exact model identifier | access mode | documented context limit |
|---|---|---|---|---|
| `M01` | OpenAI | `gpt-5.6-sol` | first-party OpenAI Responses API | 1,050,000 tokens |
| `M02` | Anthropic | `claude-opus-5` | first-party Claude Messages API | 1,000,000 tokens |
| `M03` | Google | `gemini-3.6-flash` | first-party Gemini API | 1,000,000 tokens |

These three providers are operationally independent first-party hosts. No proxy, model router, aggregator, or common third-party inference gateway is authorized.

Model-identity provenance was checked against current official vendor documentation before this authorization on 2026-08-14:

```text
OpenAI
  https://developers.openai.com/api/docs/models/gpt-5.6-sol
  https://developers.openai.com/api/docs/models

Anthropic
  https://platform.claude.com/docs/en/about-claude/models/overview
  https://platform.claude.com/docs/en/build-with-claude/context-windows

Google
  https://ai.google.dev/gemini-api/docs/models
  https://ai.google.dev/gemini-api/docs/latest-model
```

No later alias substitution is permitted.

If a listed model becomes unavailable before first exposure, the execution must stop with:

```text
EXECUTION_PRECHECK_BLOCKED
```

A different model may not be substituted under this authorization.

---

# 4. Exact execution-manifest fields

The pre-access execution manifest is bound as follows.

## 4.1 `M01` — OpenAI

```text
provider
  OpenAI

exact_model_identifier_version
  gpt-5.6-sol

access_mode
  first-party OpenAI Responses API; stateless single request per state

system_prompt_visibility
  experiment-supplied system prompt: NONE
  provider-internal system/developer state: NOT_VISIBLE_TO_EXPERIMENTER

temperature_or_deterministic_setting
  reasoning.effort = none

sampling_parameters
  no tools
  no web search
  no file search
  no retrieval
  no conversation reuse
  no output-conditioned rerun
  truncation disabled / forbidden
  maximum requested text output = 4096 tokens

tool_availability
  NONE

context_limits
  documented model context window = 1,050,000 tokens
  no truncation, compaction, or context dropping permitted

execution_date
  2026-08-14
```

## 4.2 `M02` — Anthropic

```text
provider
  Anthropic

exact_model_identifier_version
  claude-opus-5

access_mode
  first-party Claude Messages API; stateless single request per state

system_prompt_visibility
  experiment-supplied system prompt: NONE
  provider-internal system state: NOT_VISIBLE_TO_EXPERIMENTER

temperature_or_deterministic_setting
  effort explicitly fixed at medium

sampling_parameters
  temperature = 0
  no tools
  no web search
  no retrieval
  no conversation reuse
  no output-conditioned rerun
  maximum requested text output = 4096 tokens

tool_availability
  NONE

context_limits
  documented model context window = 1,000,000 tokens
  no truncation, compaction, or context dropping permitted

execution_date
  2026-08-14
```

## 4.3 `M03` — Google

```text
provider
  Google

exact_model_identifier_version
  gemini-3.6-flash

access_mode
  first-party Gemini API; stateless single request per state

system_prompt_visibility
  experiment-supplied system prompt: NONE
  provider-internal system state: NOT_VISIBLE_TO_EXPERIMENTER

temperature_or_deterministic_setting
  documented default thinking level = medium

sampling_parameters
  provider sampling parameters otherwise left at the documented model defaults
  no tools
  no web grounding
  no retrieval
  no conversation reuse
  no output-conditioned rerun
  maximum requested text output = 4096 tokens

tool_availability
  NONE

context_limits
  documented model context window = 1,000,000 tokens
  no truncation, compaction, or context dropping permitted

execution_date
  2026-08-14
```

The fixed scientific reconstruction prompt and allowed-token schema remain exactly those frozen in the preregistration. This manifest does not alter them.

---

# 5. Session and exposure universe

The L1 execution universe is exactly:

\[
\boxed{
3\ \text{reconstructors}
\times
10\ \text{frozen states}
=
30\ \text{fresh isolated reconstruction sessions}.
}
\]

Authorized model order:

```text
M01 OpenAI gpt-5.6-sol
M02 Anthropic claude-opus-5
M03 Google gemini-3.6-flash
```

Authorized state order within each model:

```text
S01 S02 S03 S04 S05 S06 S07 S08 S09 S10
```

Every cell receives exactly one canonical primary `O_framework(S_k)` packet together with the already-frozen task prompt and allowed-token schema.

No cell receives:

```text
another state's packet
another model's answer
prior reconstruction output
gold target table
conversation history
assistant memory
web access
retrieval
repository access outside the supplied packet
follow-up correction
self-consistency dialogue
```

No output-conditioned change to model order, state order, panel membership, prompt, schema, packet, target, or scoring is permitted.

---

# 6. Pre-exposure operational preflight

Execution authorization does not convert infrastructure failure into scientific evidence.

Before the first packet is transmitted to any provider, the execution runner must check only:

```text
all three required credentials/endpoints are configured
all three exact model IDs are addressable
all ten frozen Git anchors resolve
the SpecComplete-valid implementation checkpoint is exactly bound
no execution-manifest field has changed
```

This preflight must not send any H1 framework packet or gold target to a model.

If any preflight check fails:

```text
EXECUTION_PRECHECK_BLOCKED
```

and stop before exposure.

Forbidden responses to a preflight failure:

```text
model substitution
model upgrade
model downgrade
provider substitution
panel reduction
packet truncation
packet summarization
state removal
claim imputation
NOT_REPRESENTABLE
framework defect
```

Thus:

\[
\boxed{
\text{operational unavailability}
\neq
\text{L1 failure}
\neq
\text{L2 defect}.
}
\]

---

# 7. Execution-date validity

The bound execution date is:

```text
2026-08-14
```

This authorization is valid for first packet exposure only on that date.

If no packet has been exposed by the end of 2026-08-14, this authorization expires operationally. A subsequent authorization may update only operational manifest fields whose availability is time-dependent; it may not change the H1 scientific object or use any empirical H1 output, because none will yet exist.

An expired authorization is not a scientific failure.

---

# 8. L1 / L2 separation during execution

The governing firewall remains:

\[
\boxed{
\text{L1 reconstruction failure}
\not\Rightarrow
\Delta_T^A(O_{\rm framework})\neq\varnothing.
}
\]

L1 output is scored only by the frozen coordinate-wise scorer.

L2 is computed only by exact equality of preregistered semantic observations and heterogeneity of `T_A^core` within those exact fibers.

No reconstruction output enters:

```text
O_framework^sem
fiber construction
T_A^core
collision evaluation
README diagnostic collision evaluation
```

No L2 result changes L1 scoring.

---

# 9. Evidence handling and no-look rule

The actual execution operation must preserve raw reconstruction responses before interpretation.

No human/model review of reconstruction correctness may be used to modify any remaining run parameter.

The execution implementation may mechanically validate transport success and serialize raw responses, but it may not use answer content to alter execution.

After the frozen 30-cell L1 exposure schedule is complete or terminally `NOT_EVALUATED` where transport failed, the frozen scorer may compute coordinate outcomes.

The deterministic L2 primary and README diagnostic surfaces are then computed under the already-frozen procedures.

This ordering is an anti-leakage execution rule, not a modification of the scientific target.

---

# 10. Evidence provenance after execution

If execution proceeds exactly under this authorization, the H1 characterization evidence class remains the preregistered:

```text
PREREGISTERED_RETROSPECTIVE_CHARACTERIZATION_EVIDENCE
```

It is not:

```text
HELD_OUT_CONFIRMATION
CALIBRATION_EVIDENCE
APPLICATION_EVIDENCE
DEVELOPMENT_DECISION
```

The historical ten-state panel remains the reason for the retrospective characterization label.

---

# 11. Non-claims of authorization

This artifact establishes none of the following:

```text
framework sufficiency
framework insufficiency
Delta_T^A(O_framework) = empty
Delta_T^A(O_framework) != empty
any L1 reconstruction success
any L1 reconstruction failure
any primary L2 fiber
any primary L2 collision
any README diagnostic collision
any model comparison
any model ranking
any framework repair
```

The type rule is:

\[
\boxed{
\text{execution authorization}
\neq
\text{scientific result}.
}
\]

---

# 12. Hard anti-mutation boundary

After this authorization and before terminal H1 classification, do not change:

```text
scientific state universe
packet allowlist
packet serialization
semantic canonicalization
target coordinates
target domains
gold targets
constraint profiles
reconstructor panel
model identities
model order
state order
fixed task prompt
allowed-token schema
L1 scorer
L2 collision evaluator
README diagnostic rule
claim authority
```

Any required scientific-design change terminates `H1_V2_R1`; it cannot be patched into the live round.

Operational credential repair is permitted only before first packet exposure and may not alter provider/model identity or any scientific object.

---

# 13. Authorized next operation

The next permissible operation is exactly:

\[
\boxed{
\textbf{execute the frozen H1 L1/L2 characterization}
}
\]

subject first to section 6 preflight.

The execution must emit at minimum:

```text
execution-manifest verification
provider/model preflight result
raw L1 response ledger for all 30 authorized cells
coordinate-level L1 scoring ledger
state-level L1 classifications
B_H1 exposure vectors
primary O_framework^sem fiber structure
primary Delta_T^A(O_framework) collision certificate or exact null certificate
README-only diagnostic fiber/collision surface
terminal Sigma_H1 classifications
provenance and anti-mutation flags
```

No repair or post-H1 design operation is authorized in the same execution artifact.

---

# 14. Stop condition

```text
STOP_H1_V2_EXECUTION_AUTHORIZATION
```

Terminal state of this operation:

```text
H1_V2_IMPLEMENTATION_CONSTRUCTED    = true
H1_V2_IMPLEMENTATION_REPAIRED       = true
H1_V2_SPECCOMPLETE                  = true
H1_V2_SPECIFICATION_STATE           = SPECIFICATION_VALID
H1_V2_EXECUTION_MANIFEST_FROZEN     = true
H1_V2_EXECUTION_AUTHORIZED          = true
H1_V2_RECONSTRUCTION_EVIDENCE_SEEN  = false
H1_V2_COLLISION_EVIDENCE_SEEN       = false
BACKWARD_DESIGN_AUTHORITY           = 0

STOP_H1_V2_EXECUTION_AUTHORIZATION
```
