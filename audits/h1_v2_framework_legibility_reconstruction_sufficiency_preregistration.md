# H1 v2 — Framework-Legibility Reconstruction Sufficiency Preregistration

## Status

```text
v1_terminal_ledger
  81efea2405e3b0269c9bad3bf417d4ab73ea080b

development_inventory
  a72f5a8df8f69d33e79304a9dafd540d1d82f601

target_selection_protocol
  5f1282d76894716ed329a762eca8de5bfe0dc64b

target_selection_result
  80caa03109a105fd6c70d58f7d6663d957fc20ff

SELECTED_V2_TARGET                  = H1
H1_V2_PREREGISTRATION               = FROZEN
H1_V2_EXECUTION_AUTHORIZED          = false
H1_V2_RECONSTRUCTION_EVIDENCE_SEEN  = false
H1_V2_COLLISION_EVIDENCE_SEEN       = false
BACKWARD_DESIGN_AUTHORITY           = 0
```

This artifact freezes the first confirmatory design for the selected post-v1 target:

\[
\boxed{
\operatorname{Suff}^{A}
\left(
O_{\rm framework};
T_{\rm reconstruct}
\right)?
}
\]

It does not execute the experiment, query a reconstructor, inspect reconstruction output, search for favorable collisions, repair the framework, or modify v1.

The governing separation is:

\[
\boxed{
\text{L1 reconstruction utilization}
\neq
\text{L2 interface sufficiency}.
}
\]

A reconstruction error is not an interface-defect certificate.

---

# 1. Scientific object

The round identifier is:

```text
H1_V2_R1
```

The frozen experimental object is:

\[
\boxed{
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
}
\]

The scientific question is not whether a reader or model reports that it “understood the framework.”

The question is whether the frozen exposed representation preserves the licensed scientific-state distinctions required by the frozen reconstruction target, and separately whether independent reconstructors can use the information that is present.

---

# 2. Evidence provenance

The scientific state checkpoints used in this round all predate this preregistration. Therefore the primary state panel is historical and cannot be labeled pristine held-out confirmation.

If executed exactly as preregistered, its evidence role is:

```text
PREREGISTERED_RETROSPECTIVE_CHARACTERIZATION_EVIDENCE
```

This means:

- the reconstruction/collision procedures are frozen before reconstruction outputs exist;
- the state universe and source representation are historical and known in principle before preregistration;
- no result from this round may be relabeled `HELD_OUT_CONFIRMATION`;
- a later fresh confirmation would require a separately sealed state panel not used to motivate or tune this design.

The motivating independent reconstruction concern remains only:

```text
DEVELOPMENT_MOTIVATION
```

and is not included as a primary scientific observation in this round.

---

# 3. Frozen framework-state universe `X_framework`

The primary state universe contains only real scientific checkpoints from the existing repository lineage.

No synthetic target-toggled state enters the primary result.

The universe is exactly:

| state | commit | frontier token |
|---|---|---|
| `S01` | `6482667d3b48c2e0c47bfea2fb44da92187b0511` | `DSLI_R1_CONSTRUCTION` |
| `S02` | `0f2e2e9cf38258b583dc3d7f9bbbf2cd047fcf53` | `DSLI_R1_SPECCOMPLETE` |
| `S03` | `ddffe4b976352b3fec4efc3300a0dcc0097ca217` | `DSLI_R1_CHARACTERIZATION` |
| `S04` | `f0c594bc9ed70856ec980a06926275584db79086` | `APPLICATION_SET_IDENTITY_CARRY_FORWARD` |
| `S05` | `f8a76956ecfbf4848b62659e6db23c3918311679` | `ACTUAL_APPLICATION_PREREGISTRATION` |
| `S06` | `a4eac05b9387e46bebf2008b3cfb57f3e375577f` | `ACTUAL_APPLICATION_EXECUTION` |
| `S07` | `81efea2405e3b0269c9bad3bf417d4ab73ea080b` | `DSLI_R1_TERMINAL_LEDGER` |
| `S08` | `a72f5a8df8f69d33e79304a9dafd540d1d82f601` | `DEVELOPMENT_EVIDENCE_INVENTORY` |
| `S09` | `5f1282d76894716ed329a762eca8de5bfe0dc64b` | `V2_TARGET_SELECTION_PROTOCOL` |
| `S10` | `80caa03109a105fd6c70d58f7d6663d957fc20ff` | `H1_TARGET_SELECTED` |

The set is closed before any reconstruction run.

A primary scientific state may not be added, removed, substituted, duplicated, or edited after reconstruction evidence exists.

## 3.1 Anti-gotcha rule

Primary scientific evidence may arise only from the ten authentic repository checkpoints above.

Forbidden as primary evidence:

```text
synthetic status flips
synthetic provenance flips
synthetic frontier flips
target-only mutations
handwritten adversarial mini-cases
cases created by editing T_A while holding O fixed by construction
cases generated after observing reconstruction errors
```

Synthetic cases are allowed only inside the conformance suite and are permanently typed:

```text
CONFORMANCE_FIXTURE
```

They never enter `X_framework`, L1 performance summaries, L2 defect counts, or scientific claims.

---

# 4. Frozen exposed information boundary `O_framework`

The primary exposed representation for state `S_k` is constructed from the exact repository snapshot at the corresponding commit.

It contains only:

```text
README.md
all tracked UTF-8 Markdown files matching audits/*.md
```

that exist at that exact commit.

The packet serialization is:

1. enumerate eligible paths;
2. sort paths by raw Unicode code-point order;
3. for each path, emit the exact path followed by the exact file bytes decoded as UTF-8;
4. separate files with the fixed delimiter `\n<<<H1_FILE_BOUNDARY>>>\n`;
5. use LF line endings in the packet wrapper while preserving file text otherwise.

The packet does **not** contain:

```text
Git commit messages
branch names
Git tags
GitHub issue/PR text
workflow metadata not already written in an included Markdown file
JSON result payloads
Python source
conversation history
assistant memory
hidden system context
web search
external documentation
repository files outside the allowlist
```

Thus:

\[
\boxed{
O_{\rm framework}
\neq
\text{whatever context a model happens to receive}.
}
\]

It is a frozen information channel.

## 4.1 Diagnostic README-only projection

A secondary, non-primary diagnostic projection is also frozen:

```text
O_README(S_k) = exact README.md at S_k
```

It uses the same wrapper and canonicalization rules.

`O_README` is an ablation diagnostic only. It cannot replace the primary `O_framework` result or be used to claim that the full framework representation is sufficient/insufficient.

---

# 5. Licensed reconstruction target `T_A`

The reconstruction target is typed and non-scalar.

For every state `S_k`, the required target is:

\[
\boxed{
T_A(S_k)
=
(
F_k,
E_k,
P_k,
C_k,
N_k,
A_k,
H_k
)
}
\]

with coordinates:

```text
F_k  frontier_id
E_k  epistemic_status
P_k  provenance_class
C_k  closure_state
N_k  next_authorized_operation
A_k  constraint_profile
H_k  checkpoint_anchor
```

No aggregate “understanding” or “legibility” score is a primary target.

## 5.1 Exact coordinate domains

### `frontier_id`

Exactly the ten frontier tokens in the state table in section 3.

### `epistemic_status`

Allowed tokens:

```text
DESIGN_FROZEN
SPECIFICATION_VALID
CALIBRATION_CHARACTERIZED
IDENTITY_CARRY_FORWARD_FROZEN
ACTUAL_APPLICATION_PREREGISTERED
POST_SPECIFICATION_APPLICATION_EVIDENCE
SCIENTIFIC_STATE_CLOSED
DEVELOPMENT_INVENTORY_FROZEN
TARGET_SELECTION_RULE_FROZEN
TARGET_SELECTED
```

### `provenance_class`

Allowed tokens:

```text
DESIGN_ARTIFACT
SPECIFICATION_CONFORMANCE
CALIBRATION_EVIDENCE
DESIGN_CARRY_FORWARD
PREREGISTERED_DESIGN
POST_SPECIFICATION_APPLICATION_EVIDENCE
TERMINAL_CLASSIFICATION
DEVELOPMENT_EVIDENCE
DEVELOPMENT_DECISION_PROTOCOL
DEVELOPMENT_DECISION
```

### `closure_state`

Allowed tokens:

```text
LIVE_DESIGN_SURFACE
STOP_REQUIRED
CLOSED_ARCHIVE
POST_V1_DEVELOPMENT
```

### `next_authorized_operation`

Allowed tokens:

```text
RUN_SPECCOMPLETE
RUN_CHARACTERIZATION
FREEZE_APPLICATION_SET
PREREGISTER_ACTUAL_APPLICATION
EXECUTE_ACTUAL_APPLICATION
ARCHIVE_TERMINAL_LEDGER
CREATE_DEVELOPMENT_INVENTORY
FREEZE_TARGET_SELECTION_RULE
APPLY_TARGET_SELECTION_RULE
PREREGISTER_H1_V2
```

### `constraint_profile`

Allowed profile IDs are `CP01` through `CP10`, defined in section 5.3.

### `checkpoint_anchor`

Exact full 40-character Git commit SHA from section 3.

`checkpoint_anchor` is a provenance-reconstruction coordinate for L1. It is excluded from the L2 core target because exact commit identity is an unauthorized shortcut for semantic sufficiency.

## 5.2 Frozen gold target table

| state | epistemic status | provenance | closure | next operation | profile |
|---|---|---|---|---|---|
| `S01` | `DESIGN_FROZEN` | `DESIGN_ARTIFACT` | `LIVE_DESIGN_SURFACE` | `RUN_SPECCOMPLETE` | `CP01` |
| `S02` | `SPECIFICATION_VALID` | `SPECIFICATION_CONFORMANCE` | `LIVE_DESIGN_SURFACE` | `RUN_CHARACTERIZATION` | `CP02` |
| `S03` | `CALIBRATION_CHARACTERIZED` | `CALIBRATION_EVIDENCE` | `LIVE_DESIGN_SURFACE` | `FREEZE_APPLICATION_SET` | `CP03` |
| `S04` | `IDENTITY_CARRY_FORWARD_FROZEN` | `DESIGN_CARRY_FORWARD` | `LIVE_DESIGN_SURFACE` | `PREREGISTER_ACTUAL_APPLICATION` | `CP04` |
| `S05` | `ACTUAL_APPLICATION_PREREGISTERED` | `PREREGISTERED_DESIGN` | `LIVE_DESIGN_SURFACE` | `EXECUTE_ACTUAL_APPLICATION` | `CP05` |
| `S06` | `POST_SPECIFICATION_APPLICATION_EVIDENCE` | `POST_SPECIFICATION_APPLICATION_EVIDENCE` | `STOP_REQUIRED` | `ARCHIVE_TERMINAL_LEDGER` | `CP06` |
| `S07` | `SCIENTIFIC_STATE_CLOSED` | `TERMINAL_CLASSIFICATION` | `CLOSED_ARCHIVE` | `CREATE_DEVELOPMENT_INVENTORY` | `CP07` |
| `S08` | `DEVELOPMENT_INVENTORY_FROZEN` | `DEVELOPMENT_EVIDENCE` | `POST_V1_DEVELOPMENT` | `FREEZE_TARGET_SELECTION_RULE` | `CP08` |
| `S09` | `TARGET_SELECTION_RULE_FROZEN` | `DEVELOPMENT_DECISION_PROTOCOL` | `POST_V1_DEVELOPMENT` | `APPLY_TARGET_SELECTION_RULE` | `CP09` |
| `S10` | `TARGET_SELECTED` | `DEVELOPMENT_DECISION` | `POST_V1_DEVELOPMENT` | `PREREGISTER_H1_V2` | `CP10` |

The `frontier_id` and `checkpoint_anchor` are taken directly from section 3.

The gold table is frozen before any reconstruction output exists.

## 5.3 Constraint profiles

The constraint target is a profile token rather than an open-ended prose summary.

```text
CP01
  SpecComplete before characterization;
  no actual-target application;
  no downstream selection/authorization.

CP02
  characterization only after specification validity;
  no actual-target application;
  no downstream selection/authorization.

CP03
  calibration evidence cannot select/rank languages;
  no actual-target access in characterization;
  no Q_extension/authorization/binding.

CP04
  application-set carry-forward is identity only;
  no target access;
  no application mechanics;
  no Q_extension/authorization.

CP05
  conformance before target access;
  timeout/failure-to-find cannot imply NOT_REPRESENTABLE;
  NOT_DEFINED != 0 != infinity;
  no language winner/Q_extension/authorization.

CP06
  application outputs are descriptive only;
  no language/governance winner;
  no Q_extension/authorization/v2 mutation;
  STOP_DSLI_R1.

CP07
  DSLI_R1 immutable and closed;
  terminal ledger is retrospective only;
  terminal ledger cannot design v2.

CP08
  development inventory is descriptive only;
  no candidate ranking or selection;
  v1 remains immutable.

CP09
  selection rule may be frozen;
  protocol cannot name a winner;
  selection rule != v2 experimental design;
  v1 remains immutable.

CP10
  H1 receives design focus only;
  H1 selection != validation;
  no v2 execution authorization;
  v1 remains immutable.
```

A reconstructor must return the profile ID, not regenerate prose.

---

# 6. Core target for L2

The L2 sufficiency target excludes exact checkpoint identity:

\[
\boxed{
T_A^{\rm core}(S_k)
=
(F_k,E_k,P_k,C_k,N_k,A_k).
}
\]

This prevents a unique commit SHA from converting an otherwise semantically insufficient interface into an apparent sufficiency result.

The scientific question for L2 is therefore:

\[
\boxed{
\operatorname{Suff}^{A}
(O_{\rm framework}^{\rm sem};T_A^{\rm core})?
}
\]

on the frozen ten-state support.

---

# 7. Authority regime `G_A`

## 7.1 L1 allowed information

A reconstruction session may use only the literal packet supplied for one state.

The reconstructor may quote or copy information present in the packet, including commit hashes, because provenance reconstruction is itself an L1 target coordinate.

Forbidden L1 channels:

```text
web search
GitHub browsing
repository access outside the packet
conversation history
persistent memory of earlier cases
external notes
cross-case comparison
hidden state IDs
answer keys
follow-up questions
human correction during the run
```

If a model/provider injects unavoidable system context, it must be recorded in execution provenance. No claim may treat unavailable control over provider internals as proof of reader independence.

## 7.2 L2 noninterference rule

L2 may not use exact state identity as a scientific distinction channel.

The following are nuisance/identity fields for L2 canonicalization:

```text
Git commit hashes
SHA-256 digests
workflow run IDs
job IDs
artifact IDs
ISO date/time stamps
purely serial file-order differences
line-ending differences
trailing whitespace
```

The following remain licensed semantic content and are never masked merely because they distinguish states:

```text
file paths
headings
status tokens
provenance-class names
frontier descriptions
STOP/CLOSED/FROZEN/OPEN language
named scientific artifacts
language/governance IDs
reported empirical counts
burden values
explicit authority prohibitions
next-step statements
```

The authority principle is:

\[
\boxed{
\text{unique repository identity}
\neq
\text{scientific-state sufficiency}.
}
\]

---

# 8. L2 semantic canonicalization `O_framework^sem`

For every primary packet, canonicalization is deterministic and frozen:

1. normalize CRLF and CR to LF;
2. strip trailing horizontal whitespace on every line;
3. keep file paths and file boundaries;
4. mask standalone hexadecimal tokens of length 7 through 64 characters as `<HEX_ID>`;
5. mask decimal numeric tokens immediately associated with case-insensitive labels `workflow run`, `run id`, `job`, `job id`, `artifact`, or `artifact id` as `<RUN_ID>`;
6. mask ISO-8601 date/time strings of forms `YYYY-MM-DD`, `YYYY-MM-DDTHH:MM[:SS][Z|±HH:MM]` as `<TIME_ID>`;
7. do not otherwise alter words, numbers, equations, tables, headings, filenames, or status labels;
8. serialize files in the same lexicographic path order as section 4.

The exact canonical byte string is the L2 observation.

Two states are L2 observation-equivalent iff their canonical byte strings are exactly equal.

\[
\boxed{
S_a\sim_O S_b
\iff
O_{\rm framework}^{\rm sem}(S_a)
=
O_{\rm framework}^{\rm sem}(S_b).
}
\]

No embedding similarity, semantic-similarity model, fuzzy threshold, or human judgment defines an L2 fiber.

---

# 9. Reconstruction protocol `Pi_reconstruction` — L1

L1 is a utilization test only.

Each reconstruction is performed in a fresh isolated session with exactly one state packet.

The fixed task prompt is:

```text
You are reconstructing the scientific state represented by the supplied framework packet.
Use only the packet. Do not use external knowledge, browsing, memory from other cases, or inferred chronology.

Return exactly one JSON object with these keys:
frontier_id
epistemic_status
provenance_class
closure_state
next_authorized_operation
constraint_profile
checkpoint_anchor

Use only the allowed tokens defined in the accompanying schema.
If a coordinate cannot be identified from the packet, return the exact string NOT_IDENTIFIED for that coordinate.
Do not guess and do not replace NOT_IDENTIFIED with a default value.
```

The allowed-token schema is supplied with the prompt; the gold state table is not.

No follow-up, correction, self-consistency rerun, chain-of-thought request, retrieval tool, or adjudication dialogue is permitted.

## 9.1 Reconstructor panel

The L1 reconstructor panel is a nuisance/replication layer, not the basis of the L2 interface-defect claim.

Before the first state packet is shown to any reconstructor, an execution manifest must bind:

```text
provider
exact model identifier/version
access mode
system-prompt visibility if available
temperature or deterministic-setting value
sampling parameters
tool availability
context limits
execution date
```

A minimum of three independently hosted general-purpose reconstructor models is required for descriptive L1 replication.

The exact model identities may be frozen only in that pre-access execution manifest because model availability is operational rather than a property of `T_A`; however, once the first packet is exposed, no model may be added, removed, substituted, upgraded, or rerun because of observed performance.

No pooled “model-independent legibility” estimate is licensed.

Per-model results remain separate.

## 9.2 L1 output semantics

For each reconstructor × state × target coordinate, the terminal value is exactly one of:

```text
CORRECT
INCORRECT
NOT_IDENTIFIED
UNPARSEABLE
NOT_EVALUATED
```

Rules:

```text
NOT_IDENTIFIED != INCORRECT
NOT_IDENTIFIED != CORRECT
UNPARSEABLE != NOT_IDENTIFIED
NOT_EVALUATED != any empirical outcome
```

No missing value is imputed.

No partial-credit string similarity is allowed.

A state-level reconstruction is `EXACT_RECONSTRUCTION` iff all seven coordinates are `CORRECT`.

Otherwise it remains coordinate-wise; no scalar threshold converts it into an L2 diagnosis.

---

# 10. Collision protocol `Pi_collision` — L2

L2 is independent of reconstructor success or failure.

Procedure:

1. construct all ten primary `O_framework` packets from the frozen commits;
2. canonicalize each packet exactly as section 8;
3. group states by exact canonical observation equality;
4. enumerate every unordered state pair within every multi-state fiber;
5. compare only `T_A^core`;
6. record the exact target coordinates that differ.

The authority-qualified defect set is:

\[
\boxed{
\Delta_{T}^{A}(O_{\rm framework})
=
\{(S_a,S_b):
O_{\rm framework}^{\rm sem}(S_a)=O_{\rm framework}^{\rm sem}(S_b),
\;T_A^{\rm core}(S_a)\neq T_A^{\rm core}(S_b)
\}.
}
\]

A defect is therefore a literal observation-equivalent, target-heterogeneous pair under the preregistered canonicalization.

A reconstruction error never creates a member of this set.

## 10.1 Diagnostic README collision surface

The same collision procedure is run separately on `O_README`.

Its result is named:

```text
DELTA_README_DIAGNOSTIC
```

and cannot be substituted for the primary `Delta_T^A(O_framework)` result.

This diagnostic answers whether the top-level README projection collapses state distinctions that the full frozen Markdown framework surface preserves.

---

# 11. Conformance gate `K_conformance`

No reconstruction packet may be shown to any model until every conformance item below passes.

Required checks:

```text
K1  all ten commit anchors resolve exactly
K2  packet membership matches README.md + audits/*.md exactly at every anchor
K3  every included file is valid UTF-8
K4  primary packet serialization is deterministic
K5  README-only packet serialization is deterministic
K6  gold target manifest exactly matches the frozen table in section 5
K7  every target token belongs to its frozen domain
K8  L2 canonicalization masks every declared identity fixture
K9  L2 canonicalization preserves every declared semantic-content fixture
K10 exact-equality fiber grouping matches an independent reference implementation
K11 heterogeneous-target fixture is detected as a collision defect
K12 homogeneous-target fixture is not misclassified as a defect
K13 checkpoint identity alone cannot create an L2 target distinction
K14 reconstruction scorer preserves NOT_IDENTIFIED / INCORRECT / UNPARSEABLE / NOT_EVALUATED distinctions
K15 no synthetic conformance fixture is present in the primary state universe
```

All checks must be:

```text
PASS
```

before L1 access or L2 scientific execution.

Otherwise:

```text
SPECIFICATION_INVALID
```

and stop.

Synthetic fixtures used in K8–K14 are permanently excluded from scientific results.

---

# 12. Exposure burden `B_H1`

Burden is descriptive and is not part of the sufficiency criterion in this round.

For each state packet record:

\[
\boxed{
B_{\rm H1}(S_k)
=
(
N_{\rm documents},
N_{\rm UTF8\ bytes},
N_{\rm Unicode\ codepoints}
).
}
\]

For `O_README`, record the same vector separately.

Do not convert these vectors into a scalar cost, penalty, ranking, or correction criterion.

This round does not claim that a larger packet is less legible or that a smaller packet is better.

\[
\boxed{
\text{sufficiency}
\neq
\text{communication economy}.
}
\]

---

# 13. Terminal result ontology `Sigma_H1`

The result is typed, not scalar.

## 13.1 Specification layer

```text
SPECIFICATION_INVALID
CONFORMANCE_PASSED
```

No scientific characterization is authorized unless conformance passes.

## 13.2 L1 utilization layer

Per reconstructor and state:

```text
EXACT_RECONSTRUCTION
COORDINATE_ERRORS_PRESENT
NOT_EVALUATED
```

with the complete coordinate-level outcome vector retained.

There is no aggregate `UNDERSTOOD` token.

## 13.3 L2 primary interface layer

Exactly one of:

```text
FRAMEWORK_INTERFACE_DEFECT_DETECTED_ON_TESTED_SUPPORT
NO_FRAMEWORK_INTERFACE_DEFECT_DETECTED_ON_TESTED_SUPPORT
```

where:

```text
FRAMEWORK_INTERFACE_DEFECT_DETECTED_ON_TESTED_SUPPORT
iff
Delta_T^A(O_framework) is nonempty.
```

The negative state means only that no authority-qualified collision was found on the ten frozen states under the frozen semantic canonicalization.

It does **not** mean universal framework sufficiency.

## 13.4 README diagnostic layer

Exactly one of:

```text
README_DIAGNOSTIC_DEFECT_DETECTED
README_DIAGNOSTIC_NO_DEFECT_DETECTED
```

This is not a primary H1 terminal claim.

---

# 14. Claim authority

## 14.1 What an L1 result may establish

A particular reconstructor can or cannot recover particular target coordinates from particular frozen packets under the frozen utilization protocol.

It may not establish interface sufficiency or insufficiency.

\[
\boxed{
\text{L1 failure}
\not\Rightarrow
\Delta_T^A(O_{\rm framework})\neq\varnothing.
}
\]

Likewise, L1 success does not prove universal sufficiency.

## 14.2 What an L2 defect may establish

If:

\[
\Delta_T^A(O_{\rm framework})\neq\varnothing,
\]

then the full frozen Markdown framework interface is insufficient for `T_A^core` on the tested state support under the frozen canonicalization.

Nothing stronger follows automatically.

In particular, a defect does not identify:

```text
cause of the omission
best repair
preferred representation
communication mechanism
reader psychology
framework truth
future value of a repair
authorization to rewrite the framework
```

## 14.3 What a null L2 result may establish

If:

\[
\Delta_T^A(O_{\rm framework})=\varnothing,
\]

then:

```text
NO_FRAMEWORK_INTERFACE_DEFECT_DETECTED_ON_TESTED_SUPPORT
```

only.

Do not state universal sufficiency.

---

# 15. Primary interpretation matrix

The L1 and L2 layers must remain separate in interpretation.

| L1 utilization | L2 interface | licensed interpretation |
|---|---|---|
| strong | no defect detected | tested interface preserved distinctions and tested reconstructors often used them |
| weak | no defect detected | information may be present while utilization is poor; no interface defect identified |
| strong | defect detected | reconstructors may succeed on many cases while at least one tested interface collision exists |
| weak | defect detected | both utilization failures and at least one representation-level collision are present; causes remain separate |

No cell licenses a repair, rewrite, or v2 continuation by itself.

---

# 16. Nuisance and invariance checks

For L1 implementation validation, every packet must also be tested under deterministic nuisance transports that preserve literal scientific content:

```text
LF vs CRLF wrapper normalization
lexicographic file-order reconstruction from an intentionally permuted source list
presence/absence of trailing spaces before canonical serialization
```

These checks validate the packet builder, not model invariance.

The scientific L1 reconstructor receives only the canonical packet once per state.

For L2, canonical observations must be invariant under all declared nuisance transports and sensitive to declared semantic fixtures.

---

# 17. Anti-leakage rules

Before execution is closed, the following are forbidden:

```text
observing any L1 reconstruction and then changing target coordinates
observing any L1 reconstruction and then changing packet membership
observing any L1 reconstruction and then changing canonicalization
adding states because they expose an observed failure
removing states because they are difficult
adding reconstructors because prior reconstructors failed
removing reconstructors because prior reconstructors failed
changing gold targets after any model sees a packet
using model disagreement to define T_A
using README diagnostic output to redefine the primary interface
using exact commit identity to certify semantic L2 sufficiency
creating synthetic primary collisions
repairing O_framework before terminal classification
```

The anti-oracle firewall is:

\[
\boxed{
\text{reconstruction outcomes}
\not\rightarrow
(O_{\rm framework},T_A,\mathcal G_A,\Pi_{\rm collision})
}
\]

within `H1_V2_R1`.

---

# 18. Implementation / construction boundary

This preregistration authorizes only a subsequent implementation-construction step that materializes:

```text
state manifest
packet builder
gold target manifest
semantic canonicalizer
collision evaluator
reconstruction scorer
conformance fixtures
execution-manifest schema
```

That construction step must not query any reconstructor.

It must then pass the full `K_conformance` gate before execution can be separately authorized.

The execution order is therefore:

\[
\boxed{
\text{preregistration}
\rightarrow
\text{implementation construction}
\rightarrow
\text{SpecComplete / conformance}
\rightarrow
\text{separate execution authorization}
\rightarrow
\text{L1/L2 execution}.
}
\]

No reconstruction evidence exists at preregistration time.

---

# 19. Fresh-confirmation boundary

Because this round uses historical framework states, it is characterization rather than pristine confirmation.

A later fresh confirmation, if pursued, must use a state panel that is sealed after this preregistration and is not used to alter:

```text
O_framework
T_A
canonicalization
constraint profiles
reconstruction prompt
collision rule
```

No future state becomes confirmatory merely because it occurs later in Git history. Its generation and sealing procedure would require separate preregistration.

---

# 20. Non-claims

`H1_V2_R1` does not test or establish:

```text
truth of the research framework
quality of the scientific theories themselves
human-reader legibility in general
model-independent comprehension
best documentation structure
best summary length
best repair
framework adoption
framework authorization
interface invention
P_keep
repair vs replacement
horizon-cost effects
active-identifiability interventions
v1 reinterpretation
```

The selected target is H1 only.

No result from H1 may be used to claim that H2, H3, or H4 was rejected.

---

# 21. Frozen scientific question

The primary v2-r1 question is:

\[
\boxed{
\exists S_a,S_b\in X_{\rm framework}:
O_{\rm framework}^{\rm sem}(S_a)
=
O_{\rm framework}^{\rm sem}(S_b)
\land
T_A^{\rm core}(S_a)
\neq
T_A^{\rm core}(S_b)
?
}
\]

Separately, L1 asks:

\[
\boxed{
O_{\rm framework}(S_k)
\rightarrow
\widehat T_A(S_k)
}
\]

for independent reconstruction sessions.

These questions are not collapsed.

---

# 22. Stop condition

After this preregistration is committed:

```text
STOP_H1_V2_PREREGISTRATION
```

Do not in this operation:

```text
build the executor
query a model
run Kimi again
run ChatGPT reconstruction
run any external reconstructor
compute primary L2 fibers
inspect collision outcomes
score reconstruction outputs
repair documentation
change README
add a new framework summary
select H2/H3/H4
reopen v1
authorize v2 execution
```

Terminal state:

```text
SELECTED_V2_TARGET                 = H1
H1_V2_PREREGISTRATION              = FROZEN
H1_V2_IMPLEMENTATION_CONSTRUCTED   = false
H1_V2_SPECCOMPLETE                 = false
H1_V2_EXECUTION_AUTHORIZED         = false
H1_V2_RECONSTRUCTION_EVIDENCE_SEEN = false
H1_V2_COLLISION_EVIDENCE_SEEN      = false
BACKWARD_DESIGN_AUTHORITY          = 0

STOP_H1_V2_PREREGISTRATION
```
