# CUHK-X V7 — execution adjudication

## Status

```text
probe_id                         CUHKX_V7_STRONG_IR_DINOV2_B14
execution_state                  V7_EXECUTION_COMPLETE
primary_adjudication             MATERIAL_IR_REPRESENTATION_GAIN
secondary_adjudication           MATERIAL_STRONG_IR_SENSOR_GAIN
scientific_evidence_seen         true
raw_result_artifact              /CUHK-X/cuhkx_v7_strong_ir_dinov2_results.zip
raw_result_zip_sha256            af7687fad3c7a4d140707c09dd84edea79288abdd81f91e9755d21cb63aad088
execution_script_sha256          473d83342c680836badc0aa5232f32df5aecb7ae7d5755ec7986798eac13b544
```

This artifact adjudicates the single frozen V7 execution against the preregistered gates. It does not revise the FS core theory and does not authorize architecture search or post-result gate changes.

## Reproduction firewalls

All frozen historical reproduction checks passed before V7 scoring:

```text
V5 reproduction, all 809 HAU episodes   PASS
V5 reproduction, B5-matched support     PASS
B5 reproduction, matched support        PASS
```

Frozen provenance hashes reproduced:

```text
training outer ZIP
667a00cb03ec67e1eeb49a744cb4fc764878fadae0b35ea873e25c2f7b3868bc

pose cache
d7e609a5e8a9ebc4bbdda92f8fe601d8b0c6ccfd4a2757f9a632a1ac9211b89a

IMU cache
8c4656e2c76029783c18d0b76f92f58fa8165a786a7049c3be7bf90a28aa0234

V5 IR cache
265f27036b75afb3ae14eea9e3c1f03d091052f495deaf6c1ae903222eafea0e

subject folds
0ae2bd6a594152dd1af444566416410043ac11f153d20c8a517bb2a6d5052b73
```

DINOv2 execution bindings:

```text
source revision              7764ea0f912e53c92e82eb78a2a1631e92725fc8
source archive SHA-256       04276715cddb29d45d05bff3a6fc132224dc27749b279ac98ad2ce4620e20d48
checkpoint SHA-256           0b8b82f85de91b424aded121c7e1dcc2b7bc6d0adeea651bf73a13307fad8c73
V7 feature-cache SHA-256     e9699696af7d886896df7fa1e52d2b28ecfbb8abeef71a6b3b2ee04a68abb5db
```

The embedded execution script hash equals the frozen implementation hash exactly.

## Primary result — representation repair

Primary population:

```text
809 HAU multi episodes
3236 candidate-action decisions
5 frozen subject-held-out folds
```

Comparison:

```text
V5 cheap IR
BalAcc   0.6655735735643534
MacroF1  0.6643425341676923
ExactSet 0.22373300370828184

V7 DINOv2-B/14 IR
BalAcc   0.7509240663293679
MacroF1  0.7506302907618697
ExactSet 0.3522867737948084
```

Frozen contrasts:

\[
\boxed{\Delta BalAcc_{V7-V5}=+0.0853504928}
\]

\[
\boxed{\Delta ExactSet_{V7-V5}=+0.1285537701}
\]

Required thresholds were +0.020 BalAcc and +0.030 ExactSet.

Fold stability:

```text
V7 >= V5 BalAcc   5/5 folds   required >=4/5
V7 >= V5 ExactSet 5/5 folds   required >=3/5
```

Fold deltas:

| Fold | Delta BalAcc | Delta ExactSet |
|---|---:|---:|
| F0 | +0.091832 | +0.169118 |
| F1 | +0.082765 | +0.101695 |
| F2 | +0.080356 | +0.139706 |
| F3 | +0.096895 | +0.156977 |
| F4 | +0.074806 | +0.090426 |

Therefore:

\[
\boxed{D_{V7}^{primary}=\texttt{MATERIAL\_IR\_REPRESENTATION\_GAIN}}
\]

Paired candidate topology:

```text
V7-only correct   565
V5-only correct   284
net candidate gain +281
```

Exact-set topology:

```text
V7-only exact     163
V5-only exact      59
net exact episodes +104
```

Action-level balanced accuracy improved for 34/40 actions; 32/40 improved by at least +0.03. This is descriptive characterization only and is not a separate promotion gate.

## Secondary result — fixed joint exploitation

Secondary population:

```text
786 B5-matched episodes
3144 candidate-action decisions
same 5 subject-held-out folds
```

Comparison:

```text
B5 pose+IMU
BalAcc   0.7130640619614627
MacroF1  0.7120487083722378
ExactSet 0.3053435114503817

V7F pose+IMU+strong-IR
BalAcc   0.7594595605210277
MacroF1  0.7590965236694271
ExactSet 0.37404580152671757
```

Frozen contrasts:

\[
\boxed{\Delta BalAcc_{V7F-B5}=+0.0463954986}
\]

\[
\boxed{\Delta ExactSet_{V7F-B5}=+0.0687022901}
\]

Fold stability:

```text
V7F >= B5 BalAcc   5/5 folds   required >=4/5
V7F >= B5 ExactSet 5/5 folds   required >=3/5
```

Fold deltas:

| Fold | Delta BalAcc | Delta ExactSet |
|---|---:|---:|
| F0 | +0.075305 | +0.082707 |
| F1 | +0.032109 | +0.039773 |
| F2 | +0.027148 | +0.052632 |
| F3 | +0.070663 | +0.149068 |
| F4 | +0.031778 | +0.027322 |

Therefore:

\[
\boxed{D_{V7}^{secondary}=\texttt{MATERIAL\_STRONG\_IR\_SENSOR\_GAIN}}
\]

Paired candidate topology:

```text
V7F-only correct  481
B5-only correct   332
net candidate gain +149
```

Exact-set topology:

```text
V7F-only exact    144
B5-only exact      90
net exact episodes +54
```

Action-level balanced accuracy improved for 28/40 actions; 22/40 improved by at least +0.03. This is descriptive only.

## Convergence-warning note

The frozen hinge-SGD interface emitted convergence warnings for nearly every per-action fit at the fixed `max_iter=100`, including the reproduced V5 and B5 comparators. V7 did not introduce a new optimizer or change this fitting rule. Because the preregistered decision interface was intentionally held fixed and the historical comparator metrics reproduced exactly, these warnings are recorded as a property of the frozen classifier interface, not treated as a post-hoc reason to alter or invalidate the completed V7 contrast.

No optimizer rescue or rerun is authorized by this adjudication.

## Scientific interpretation

The licensed primary conclusion is:

> Under the frozen HAU `multi` subject-held-out protocol, the frozen DINOv2 ViT-B/14 IR interface preserves materially more usable candidate-action structure than the previously frozen cheap IR interface.

This directly distinguishes the tested cheap-interface limitation from a claim that the physical IR modality itself lacked useful information.

The licensed secondary conclusion is:

> Under the frozen simple-concatenation operator, the stronger IR representation is materially jointly exploitable with the B5 pose+IMU substrate.

The two results remain logically distinct even though both happened to pass:

\[
\boxed{\text{representation repair}\neq\text{joint exploitation}.}
\]

## Authority ceiling

V7 does **not** establish:

```text
DINOv2 optimality
IR modality sufficiency in general
causal importance of IR
mechanistic identification
general video understanding
Future Sufficiency
future preservation authority
future corrective viability
```

The strongest FS-facing compression licensed by this result is:

\[
\boxed{
\text{same measurement channel}
+
\text{different frozen representation interface}
\rightarrow
\text{materially different accessible decision structure under transfer}.
}
\]

That is an empirical representation/interface result, not a direct FS test.

## Stop state

```text
V7_DESIGN_FROZEN            = true
V7_EXECUTION_COMPLETE       = true
V7_PRIMARY_RESULT           = MATERIAL_IR_REPRESENTATION_GAIN
V7_SECONDARY_RESULT         = MATERIAL_STRONG_IR_SENSOR_GAIN
V7_RESULT_ARTIFACT_PRESERVED = true
POST_V7_SUCCESSOR           = UNFROZEN
```

No successor experiment is authorized by this artifact. The next operation is design selection from the newly earned V7 evidence, not automatic execution of another representation or fusion branch.
