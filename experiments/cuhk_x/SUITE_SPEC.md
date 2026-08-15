# CUHK-X suite specification

## 1. Status

```text
suite_id                         CUHKX_FS_EMPIRICAL_SUITE_V1
suite_role                       EMPIRICAL_CASE_STUDY_SUBSTRATE
creates_new_empirical_evidence   false
competition_object_modified      false
FS_core_theory_modified          false
```

This specification curates already-earned CUHK-X evidence into a Future-Sufficiency-facing empirical suite. It creates no new CUHK-X result and no new FS result.

## 2. Scientific object

For modality or modality-set \(X_m\), representation/interface \(O\), accessible state \(Z\), and frozen downstream decision contract \(D\):

\[
\boxed{
X_m\rightarrow O\rightarrow Z\rightarrow D.
}
\]

The primary HAU object used by the cheap ladder is candidate action presence in `multi` questions under canonical subject-held-out folds.

The suite distinguishes five layers:

\[
\boxed{
\text{measurement}
\rightarrow
\text{representation}
\rightarrow
\text{accessibility}
\rightarrow
\text{joint exploitation}
\rightarrow
\text{adoption}.
}
\]

No arrow may be inferred from a later layer merely because an earlier layer succeeded.

## 3. Frozen empirical unit and target

```text
empirical_unit          = episode
primary_source          = HAU
primary_category        = multi
primary_question        = Which of the following actions appear in this video?
HAU_multi_episodes      = 809
candidate_actions       = 40
candidate_pairs         = 3236
```

Each four-choice HAU `multi` row supplies explicit positive and negative candidate supervision.

The canonical fold partition is:

```text
F0 = {2,16,20}
F1 = {3,9,18,24}
F2 = {1,19,22}
F3 = {5,7,8,21}
F4 = {4,6,17,23}
```

Fold-partition SHA-256:

```text
0ae2bd6a594152dd1af444566416410043ac11f153d20c8a517bb2a6d5052b73
```

Row-level random cross-validation is outside the primary object.

## 4. Dataset constitution anchors

Official QA archive SHA-256:

```text
6a9dc7dd59c1bec120f4d408b911695e1592b81c10845dce3c1306a3cb876433
```

Observed QA constitution:

```text
training_qa.csv          4087 rows
  unique episodes        1333
  HAU                      809
  HARn                     524

test_qa.csv               682 rows
  unique episodes         208
  HAU                      144
  HARn                      64
```

There are seven distinct question strings across train/test. Output grammar and question category remain part of the competition contract, but the cheap HAU ladder freezes only the HAU `multi` candidate-action estimand unless a successor explicitly freezes another target.

## 5. Measurement channels

Observed episode channels relevant to the suite:

\[
\boxed{
X_{\rm episode}
=(X_{\rm pose},X_{\rm IMU},X_{\rm radar},X_{\rm depth},X_{\rm IR},X_{\rm thermal}).
}
\]

Primary visual coverage is complete for Depth and IR on QA-linked train/test episodes. Depth/Depth_Color/IR exhibit a systematic 320x240 train to 640x480 test resolution shift. The cheap visual probes neutralized that specific resolution change by mapping both train and test to a fixed 16x12 measurement grid before learning.

## 6. Claim types

### 6.1 Signal claim

A frozen interface may establish subject-portable signal for the frozen target.

This licenses only:

```text
this interface preserves operational information about this target on this support
```

and does not license causal or ontological claims.

### 6.2 Complementarity claim

A second interface may be called a supported complementarity candidate only under a frozen error-topology gate.

Complementarity means that the second channel/interface correctly resolves some decisions the incumbent misses.

\[
\boxed{
\text{complementarity}\neq\text{successful fusion}.
}
\]

### 6.3 Exploitation claim

A frozen joint operator may establish whether nonredundant information becomes materially useful under that operator.

\[
\boxed{
\text{available distinction}\neq\text{reachable joint decision gain}.
}
\]

### 6.4 Repair claim

A representation repair changes \(O\) while holding the measurement channel and downstream target fixed as far as the preregistration permits.

\[
\boxed{
\text{diagnosed complementarity}\neq\text{successful representation repair}.
}
\]

### 6.5 Adoption claim

Numerical improvement is not adoption.

Adoption requires passage of the already-frozen materiality and stability gate for that experiment.

\[
\boxed{
\text{better}\neq\text{worth keeping under the frozen gate}.
}
\]

## 7. Formal incumbent distinction

The formally promoted cheap incumbent is B5 pose+IMU:

```text
balanced_accuracy = 0.7130640619614627
macro_f1          = 0.7120487083722378
exact_set         = 0.3053435114503817
```

V6 B5+IR is numerically higher:

```text
balanced_accuracy = 0.73035 approximately
macro_f1          = 0.72854 approximately
exact_set         = 0.31807 approximately
```

but it did not satisfy the frozen magnitude thresholds:

```text
required delta balanced accuracy >= +0.020
observed delta balanced accuracy  = +0.017286

required delta exact-set          >= +0.030
observed delta exact-set           = +0.012723
```

Therefore:

\[
\boxed{
B5=\text{formal incumbent}
\quad\land\quad
V6=\text{positive but submaterial}.
}
\]

The gate must not be lowered retrospectively.

## 8. FS correspondence

CUHK-X is admitted to the FS repository for the following local correspondence:

\[
\boxed{
\text{finite laboratory for the topology between measurement and usable decision distinctions}.
}
\]

The already-observed ladder supports empirical separation among:

- channel availability;
- represented signal;
- decision accessibility;
- cross-channel complementarity;
- exploitation through a specified joint interface;
- adoption under a specified materiality gate;
- subject-held-out transfer.

## 9. FS authority ceiling

CUHK-X does not currently manipulate genuinely unknown future correction obligations. The task contract is largely fixed in advance.

Therefore the suite may inform the representational side of FS but does not establish:

\[
\boxed{
\operatorname{FSuff}(O_t;T_{t+h})
}
\]

for evolving future obligations.

The strongest admissible compression is:

\[
\boxed{
\text{CUHK-X provides evidence about present representational sufficiency, repair, exploitation, and transfer; true FS additionally requires future corrective viability.}
}
\]

## 10. Current frontier

Closed cheap branches:

```text
radar fusion    CLOSED
fixed Depth     CLOSED
cheap IR fusion CLOSED
```

The next earned locus remains visual representation capacity with IR as the leading channel, but the representation-design ambiguity has now been resolved.

Frozen successor design:

```text
probe_id                         CUHKX_V7_STRONG_IR_DINOV2_B14
strong_IR_representation_family DINOV2_VITB14_LVD142M_FRAME_T32
pretrained_backbone              DINOv2 ViT-B/14, no registers
source_revision                  7764ea0f912e53c92e82eb78a2a1631e92725fc8
frame_count                      32 normalized-time samples
input_geometry                   3 x 168 x 224
frame_feature                    normalized CLS token, 768D
episode_feature_dimension        53762
downstream_classifier            unchanged per-action hinge-SGD
primary_gate                     FROZEN
secondary_fixed_B5_fusion_gate   FROZEN
implementation_authorized        false
execution_authorized             false
```

The primary contrast is:

\[
\boxed{
O_{\rm IR}^{cheap}
\quad\text{vs}\quad
O_{\rm IR}^{strong}
}
\]

on all 809 HAU `multi` episodes with the same folds and downstream decision family.

The primary materiality gate is:

```text
V7 - V5 balanced accuracy >= +0.020
AND V7 - V5 exact-set >= +0.030
AND V7 >= V5 balanced accuracy in >=4/5 folds
AND V7 >= V5 exact-set in >=3/5 folds
```

One secondary fixed exploitation readout is also preregistered on the exact 786 B5 support using simple feature concatenation and the already-established +0.020/+0.030 fusion materiality thresholds. It is not a fusion search and authorizes no score-fusion successor.

The complete operator, preprocessing, temporal aggregation, reproduction firewalls, forbidden branches, and authority ceiling are frozen in:

[`STRONG_IR_REPRESENTATION_PREREGISTRATION.md`](STRONG_IR_REPRESENTATION_PREREGISTRATION.md).

The next authorized operation is only:

```text
YES_THIS_IS_THE_NEXT_STEP
```

No V7 implementation or execution is authorized at this checkpoint.
