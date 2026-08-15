# CUHK-X frozen evidence ledger

This ledger records the already-adjudicated cheap-interface search. It is a provenance index, not a new empirical analysis.

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

Compared with the better standalone channel per metric:

```text
Delta balanced accuracy = +0.02897
Delta exact-set         = +0.05980
```

The fold requirements passed. B5 therefore became the formally promoted cheap incumbent.

### Radar complementarity without promotion

On 778 radar-common episodes:

```text
prediction disagreement   = 35.99%
radar-only correct         = 459/3112 = 14.75%
radar-only correction >=3% = 5/5 folds
```

Radar clearly preserved nonredundant decision information, but neither raw concatenation nor nested score fusion crossed the frozen materiality gate.

This is a direct empirical instance of:

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
| V5 | Cheap raw IR: same 16x12, T32, 13,442D | Matched BalAcc .6690154; MacroF1 .6676786; ExactSet .2442748 | `PARTIAL_IR_ACTION_PRESENCE`; B5 materially better; IR complementarity supported |
| V6 | B5+IR raw concat | BalAcc ~.73035; MacroF1 ~.72854; ExactSet ~.31807 | `NO_MATERIAL_IR_SENSOR_GAIN`; positive but submaterial; cheap IR fusion closed |

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

Therefore:

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

V6 held the B5 and IR representations fixed and concatenated them on the same 786-episode support.

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

Fold requirements themselves passed:

```text
V6 >= B5 balanced accuracy = 4/5 folds
V6 >= B5 exact-set         = 3/5 folds
```

Candidate topology:

```text
both correct  = 1862
B5-only       = 378
V6-only       = 429
both wrong    = 475
```

Exact episodes:

```text
B5 exact = 240
V6 exact = 250
net       = +10
```

Therefore V6 is descriptively positive and comparatively stable, but the preregistered magnitude thresholds were not met.

\[
\boxed{
\text{positive exploitation}\neq\text{adoption}.
}
\]

The cheap IR-fusion branch is closed without an IR score-fusion follow-up.

## Known plumbing defects preserved as provenance

These events did not alter the corresponding frozen empirical interpretations:

- V0 decode initially blocked because no decoder was installed; repaired with isolated `imageio-ffmpeg`.
- V2 initially hit `allow_pickle=False` on a hash-locked self-generated object-dtype cache; repaired only at serialization access.
- V3 first generated script contained an accidentally mutated pose-cache SHA suffix; repaired before scoring.
- V5 retained stale V1 Depth cache/result path names, causing IR to overwrite the disposable local Depth cache and produce a misleading filename. The V5 evidence identity was verified from IR decode members, feature version, V5 spec, and script hash.
- V6 first stopped because the verified IR cache had not yet been copied to the corrected V5 cache path; input plumbing was repaired before scoring.

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
&\text{Pose+IMU: material complementarity and formal promotion}\\
&\text{Radar, Depth, IR: nonredundant information demonstrated}\\
&\text{cheap Radar/Depth exploitation: not materially successful}\\
&\text{cheap IR exploitation: positive and fold-stable, but submaterial}.
\end{aligned}}
\]

The cheap-interface search is therefore complete.

## Next frontier

\[
\boxed{
\textbf{next locus = visual representation capacity}
}
\]

IR is the leading modality for escalation, but the stronger representation and its gate remain unfrozen. This ledger does not authorize implementation or execution.
