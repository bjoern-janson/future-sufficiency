# CUHK-X frozen evidence ledger

This ledger records the adjudicated CUHK-X empirical ladder. It is a provenance index, not a theory update.

## Governing rule

\[
\boxed{
\mathrm{FREEZE}
\rightarrow
\mathrm{EXECUTE}
\rightarrow
\mathrm{ADJUDICATE}
}
\]

Pre-score plumbing failures are not empirical negative results.

\[
\boxed{
\text{implementation/environment failure}\neq\text{scientific failure}.
}
\]

## Nonvisual ladder

| Probe | Frozen object | Key result | Frozen adjudication |
|---|---|---|---|
| B0 | Skeleton -> 40-way HARn | Acc .40588; BalAcc .33945; MacroF1 .33106; Top-3 .59857 | `PARTIAL_POSE_SIGNAL` |
| B1 | Skeleton -> HARn MCQ | MCQ Acc .78026; class-balanced .77205; min fold .700 | `STRONG_POSE_MCQ_SIGNAL` |
| B2 | Skeleton -> HAU multi candidate presence | BalAcc .67913; MacroF1 .67871; ExactSet .25062 | `PARTIAL_HAU_POSE_ACTION_PRESENCE` |
| B3 | Frozen pose temporal-window operator | BalAcc ~.63916; MacroF1 ~.61113; ExactSet ~.15261 | `NO_MATERIAL_REPAIR_BY_THIS_TEMPORAL_OPERATOR` |
| B4 | IMU -> HAU multi candidate presence | BalAcc .68410; MacroF1 .68310; ExactSet .23410 on matched support | `PARTIAL_IMU_ACTION_PRESENCE`; no material modality separation vs pose |
| B5 | Pose+IMU raw concat | BalAcc .7130641; MacroF1 .7120487; ExactSet .3053435 | `MATERIAL_MODAL_COMPLEMENTARITY` |
| B6 | Radar -> HAU multi candidate presence | BalAcc .64612; MacroF1 .64575; ExactSet .18766 | `PARTIAL_RADAR_ACTION_PRESENCE`; complementarity candidate supported |
| B7 | B5+Radar raw concat | BalAcc .72872; MacroF1 .72800; ExactSet .33033 | `NO_MATERIAL_TRIMODAL_GAIN` |
| B8 | Nested B5/Radar score fusion | BalAcc ~.72642; MacroF1 ~.72552; ExactSet ~.31234 | `NO_MATERIAL_SCORE_FUSION_GAIN`; cheap radar-fusion branch closed |

### B5 promotion

B5 used 786 common pose+usable-IMU HAU `multi` episodes / 3144 candidate decisions.

```text
Delta balanced accuracy = +0.02897
Delta exact-set         = +0.05980
```

The fold requirements passed. B5 became the formally promoted cheap incumbent.

### Radar complementarity without promotion

On 778 radar-common episodes:

```text
prediction disagreement   = 35.99%
radar-only correct         = 459/3112 = 14.75%
radar-only correction >=3% = 5/5 folds
```

Radar preserved nonredundant decision information, but neither raw concatenation nor nested score fusion crossed the frozen materiality gate.

\[
\boxed{
\text{nonredundant information}\neq\text{materially exploitable information under the tested interface}.
}
\]

## Visual constitution

### V0 visual audit

```text
QA-linked train visual coverage = 1333/1333 episodes
QA-linked test visual coverage  = 208/208 episodes
observed MP4 streams            = 13128
modalities                       = Depth, Depth_Color, IR, Thermal
Depth/Depth_Color/IR fps         = 10 Hz
Thermal fps                      = 25 Hz
```

Systematic resolution shift:

```text
train Depth/Depth_Color/IR = 320x240
 test Depth/Depth_Color/IR = 640x480
```

Depth and IR are complete across QA-linked train/test. Depth_Color has structured missingness for HARn classes 40-43; Thermal is HAU-only and asynchronous/missing enough not to be the clean first visual channel.

V0 decode benchmark after an isolated decoder repair decoded 42/42 frozen streams successfully; median stream decode was ~0.0466 s. Visual decode was therefore not a meaningful compute bottleneck.

## Visual ladder

| Probe | Frozen object | Key result | Frozen adjudication |
|---|---|---|---|
| V1 | Cheap raw Depth: 16x12, T32, 13,442D | Matched BalAcc .66694; MacroF1 .66663; ExactSet .22010 | `PARTIAL`; B5 materially better; Depth complementarity supported |
| V2 | B5+Depth raw concat | BalAcc .70076; MacroF1 .70043; ExactSet .26718 | `NO_MATERIAL_VISUAL_SENSOR_GAIN` |
| V3 | Nested B5/Depth score fusion | BalAcc .70594; MacroF1 .70433; ExactSet .26972 | `NO_MATERIAL_DEPTH_SCORE_FUSION_GAIN` |
| V4 | Preregistered Depth-motion repair | BalAcc .65287; MacroF1 .65171; ExactSet .19211 | failed representation repair; fixed Depth branch closed |
| V5 | Cheap raw IR: 16x12, T32, 13,442D | all-809 BalAcc .66557; ExactSet .22373; matched BalAcc .66902; ExactSet .24427 | `PARTIAL_IR_ACTION_PRESENCE`; B5 materially better; IR complementarity supported |
| V6 | B5+cheap-IR raw concat | BalAcc ~.73035; MacroF1 ~.72854; ExactSet ~.31807 | `NO_MATERIAL_IR_SENSOR_GAIN`; positive but submaterial; cheap IR fusion closed |
| V7 | Frozen DINOv2-B/14 IR representation, T32, 53,762D | all-809 BalAcc .7509241; MacroF1 .7506303; ExactSet .3522868 | `MATERIAL_IR_REPRESENTATION_GAIN` |
| V7F | B5 + frozen V7 strong-IR raw concat, 60,361D | matched BalAcc .7594596; MacroF1 .7590965; ExactSet .3740458 | `MATERIAL_STRONG_IR_SENSOR_GAIN` |

### V1 Depth complementarity

On the 786 B5-matched episodes / 3144 candidate decisions:

```text
prediction disagreement = 35.97%
B5-only correct         = 636
Depth-only correct      = 495
Depth-only rate         = 15.74%
Depth-only >=3%         = 5/5 folds
```

Depth nevertheless remained below B5 in all five folds. V2 and V3 failed to exploit the complementarity materially, and the single preregistered V4 representation repair regressed relative to V1.

\[
\boxed{
\text{Depth complementarity supported}
\land
\text{tested fixed-Depth exploitation/repair unsuccessful}.
}
\]

The fixed Depth branch is closed.

### V5 IR complementarity

Matched IR:

```text
candidate accuracy          = 0.6679389312977099
balanced accuracy           = 0.6690153668069166
macro-F1                    = 0.6676785806852936
exact-set                   = 0.24427480916030533
```

Error topology against B5:

```text
both correct      = 1613
B5-only correct   = 627
IR-only correct   = 487
both wrong        = 417
prediction disagreement = 35.43%
IR-only rate           = 15.49%
IR-only >=3%           = 5/5 folds
```

Thus IR preserved substantial nonredundant subject-portable information even though its cheap standalone interface was materially weaker than B5.

### V6 positive but submaterial exploitation

```text
B5 balanced accuracy   = 0.7130641
V6 balanced accuracy   = ~0.73035
Delta                  = +0.017286
required               = +0.020000

B5 exact-set           = 0.3053435
V6 exact-set           = ~0.31807
Delta                  = +0.012723
required               = +0.030000
```

Fold requirements passed at 4/5 BalAcc and 3/5 ExactSet, but the magnitude thresholds did not.

\[
\boxed{
\text{positive exploitation}\neq\text{adoption}.
}
\]

The cheap IR-fusion branch was closed without an IR score-fusion follow-up.

## V7 — stronger IR representation

V7 changed the IR representational interface while holding the physical IR channel, 809-episode HAU `multi` target, canonical subject folds, candidate vocabulary, and downstream per-action hinge-SGD interface fixed.

Frozen operator:

```text
IR
-> 32 deterministic normalized-time frames
-> grayscale replication
-> 224x168 bicubic normalization
-> frozen DINOv2 ViT-B/14 LVD-142M x_norm_clstoken
-> frozen T32 trajectory/difference/statistics aggregation
-> 53,762D episode representation
```

Historical reproduction firewalls all passed before scoring. The embedded execution-script SHA-256 matched the frozen implementation exactly:

```text
473d83342c680836badc0aa5232f32df5aecb7ae7d5755ec7986798eac13b544
```

### V7 primary: cheap IR vs strong IR

All 809 episodes / 3236 candidate decisions:

```text
V5 BalAcc     = 0.6655735735643534
V7 BalAcc     = 0.7509240663293679
Delta         = +0.0853504927650145
required      = +0.020

V5 ExactSet   = 0.22373300370828184
V7 ExactSet   = 0.3522867737948084
Delta         = +0.12855377008652655
required      = +0.030

BalAcc folds nonnegative = 5/5, required >=4/5
ExactSet folds nonnegative = 5/5, required >=3/5
```

Paired topology:

```text
V7-only correct candidate decisions = 565
V5-only correct candidate decisions = 284
net candidate gain                  = +281

V7-only exact episodes = 163
V5-only exact episodes = 59
net exact gain         = +104
```

Therefore:

\[
\boxed{D_{V7}^{primary}=\texttt{MATERIAL\_IR\_REPRESENTATION\_GAIN}.}
\]

Licensed interpretation:

> Under the frozen HAU `multi` subject-held-out protocol, the frozen DINOv2 ViT-B/14 IR interface preserves materially more usable candidate-action structure than the previously frozen cheap IR interface.

### V7 secondary: joint exploitation with B5

On the exact 786-episode B5 support / 3144 candidate decisions:

```text
B5 BalAcc     = 0.7130640619614627
V7F BalAcc    = 0.7594595605210277
Delta         = +0.04639549855956504
required      = +0.020

B5 ExactSet   = 0.3053435114503817
V7F ExactSet  = 0.37404580152671757
Delta         = +0.06870229007633588
required      = +0.030

BalAcc folds nonnegative = 5/5, required >=4/5
ExactSet folds nonnegative = 5/5, required >=3/5
```

Paired topology:

```text
V7F-only correct candidate decisions = 481
B5-only correct candidate decisions  = 332
net candidate gain                   = +149

V7F-only exact episodes = 144
B5-only exact episodes  = 90
net exact gain           = +54
```

Therefore:

\[
\boxed{D_{V7}^{secondary}=\texttt{MATERIAL\_STRONG\_IR\_SENSOR\_GAIN}.}
\]

The primary and secondary results remain conceptually separate despite both passing:

\[
\boxed{\text{representation repair}\neq\text{joint exploitation}.}
\]

### Convergence-warning provenance

The frozen `max_iter=100` hinge-SGD interface emitted convergence warnings for nearly all per-action fits for V5, B5, V7, and V7F. Because comparator metrics reproduced exactly and the classifier interface was frozen before V7, no optimizer rescue or post-hoc rerun is authorized. This is a recorded property of the fixed downstream interface, not a V7-specific implementation failure.

## Known plumbing defects preserved as provenance

These events did not alter the corresponding frozen empirical interpretations:

- V0 decode initially blocked because no decoder was installed; repaired with isolated `imageio-ffmpeg`.
- V2 initially hit `allow_pickle=False` on a hash-locked self-generated object-dtype cache; repaired only at serialization access.
- V3 first generated script contained an accidentally mutated pose-cache SHA suffix; repaired before scoring.
- V5 retained stale V1 Depth cache/result path names; evidence identity was verified from IR decode members, feature version, V5 spec, and script hash.
- V6 first stopped because the verified IR cache had not yet been copied to the corrected V5 cache path; repaired before scoring.
- V7 first stopped in the ChatGPT runtime because local media/caches were absent; local execution then encountered missing Pillow and Torch dependencies. These were dependency-precheck blocks before feature extraction, repaired without changing the frozen V7 script.

General rule:

\[
\boxed{
\text{pre-score plumbing failure}\neq\text{empirical negative result}.
}
\]

## Current empirical compression

\[
\boxed{
\begin{aligned}
&\text{Pose and IMU: partial individually}\\
&\text{Pose+IMU: material complementarity and formal cheap promotion}\\
&\text{Radar, Depth, cheap IR: nonredundant information demonstrated}\\
&\text{cheap Radar/Depth exploitation: not materially successful}\\
&\text{cheap IR exploitation: positive and fold-stable, but submaterial}\\
&\text{strong IR representation: material repair}\\
&\text{B5 + strong IR: material joint exploitation}.
\end{aligned}}
\]

The key V7 result is:

\[
\boxed{
\text{same IR measurement channel}
+
\text{different frozen interface}
\rightarrow
\text{materially different accessible decision structure under subject transfer}.
}
\]

This is an empirical representation/interface result, not a direct Future-Sufficiency test.

## Current frontier

V7 execution and adjudication are complete. The post-V7 successor is intentionally **unfrozen**.

```text
V7_PRIMARY_RESULT      = MATERIAL_IR_REPRESENTATION_GAIN
V7_SECONDARY_RESULT    = MATERIAL_STRONG_IR_SENSOR_GAIN
POST_V7_SUCCESSOR      = UNFROZEN
```

No automatic DINO variant, video model, LVLM, fine-tuning, fusion search, or competition incumbent promotion is authorized by this ledger. The next operation is design selection from the newly earned V7 evidence.
