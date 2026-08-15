# CUHK-X V7 — execution implementation and precheck audit

## Status

```text
probe_id                         CUHKX_V7_STRONG_IR_DINOV2_B14
design_state                     FROZEN
implementation_authorized        true
implementation_constructed       true
execution_authorized             true
execution_precheck               V7_PRECHECK_BLOCKED
first_IR_frame_extracted         false
V7_feature_rows_created          0
V7_scores_computed               false
V7_scientific_evidence_seen      false
```

This audit records the first execution attempt after the explicit `YES_THIS_IS_THE_NEXT_STEP` authorization.

The attempt stopped before any CUHK-X feature extraction because the current ChatGPT execution runtime does not contain the local CUHK-X media and frozen feature caches required by the preregistration.

The governing firewall is:

\[
\boxed{
\texttt{V7\_PRECHECK\_BLOCKED}
\neq
\text{representation failure}
\neq
\text{joint-exploitation failure}.
}
\]

## Frozen implementation

The exact execution implementation is persisted in the user's CUHK-X Library workspace as:

```text
/CUHK-X/cuhkx_v7_strong_ir_dinov2.py
```

SHA-256:

```text
473d83342c680836badc0aa5232f32df5aecb7ae7d5755ec7986798eac13b544
```

The script implements only the preregistered V7 operator:

```text
IR
-> 32 deterministic normalized-time frames
-> arithmetic RGB mean grayscale
-> 3-channel replication
-> 224x168 bicubic normalization
-> frozen DINOv2 ViT-B/14 LVD-142M x_norm_clstoken
-> frozen T32 trajectory/difference/statistics aggregation
-> unchanged subject-held-out per-action hinge-SGD
```

It also contains the single preregistered secondary readout `[pose, IMU, V7 strong IR]`. No alternate backbone, frame count, resolution, crop, augmentation, threshold, classifier family, score fusion, fine-tuning, or test-set branch is implemented.

The implementation concretizes the preregistered `bicubic` resize as Pillow `Image.Resampling.BICUBIC` on the float32 grayscale plane. This is a fixed implementation semantic, not a searched alternative; the exact Pillow version is recorded by a successful run.

## Precheck actually executed

The script was syntax-checked successfully and invoked once in the current ChatGPT runtime.

Observed terminal output:

```text
FREEZE = CUHKX_V7_STRONG_IR_DINOV2_B14
EXECUTION = EXACT_FROZEN_OPERATOR
[0/10] Prechecking frozen local inputs...
STOP = V7_PRECHECK_BLOCKED
REASON = FileNotFoundError
missing required local inputs:
/mnt/data/HAU-001.zip
/mnt/data/Training-20260813T154030Z-1-002.zip
/mnt/data/cuhkx_b2_hau_pose_cache/features.npz
/mnt/data/cuhkx_b4_imu_v2_cache/features.npz
/mnt/data/cuhkx_v5_ir_cache/features.npz
```

Therefore the current runtime did **not** reach DINOv2 source/checkpoint acquisition, model construction, media decoding, feature extraction, model fitting, or scoring.

The Library contains the historical scripts and result bundles but not the required multi-gigabyte media archive or the three frozen `features.npz` caches as executable local inputs. No substitute was made from prior predictions, result ZIPs, synthetic frames, sample episodes, unofficial mirrors, test media, another cache, or another DINO variant.

## DINOv2 preflight encoded in the implementation

A local execution must bind:

```text
source repository   facebookresearch/dinov2
source revision     7764ea0f912e53c92e82eb78a2a1631e92725fc8
hub symbol          dinov2_vitb14
weights             LVD142M
checkpoint URL      official dl.fbaipublicfiles.com DINOv2 ViT-B/14 pretrain asset
checkpoint SHA-256  recorded before first CUHK-X feature extraction
```

The checkpoint is strict-loaded into the pinned `dinov2_vitb14` model before any CUHK-X frame is processed. Source/checkpoint acquisition failure produces `V7_PRECHECK_BLOCKED` and stops.

## Frozen historical reproduction firewalls

The implementation requires and hash-checks:

```text
training outer ZIP
667a00cb03ec67e1eeb49a744cb4fc764878fadae0b35ea873e25c2f7b3868bc

pose cache
d7e609a5e8a9ebc4bbdda92f8fe601d8b0c6ccfd4a2757f9a632a1ac9211b89a

IMU cache
8c4656e2c76029783c18d0b76f92f58fa8165a786a7049c3be7bf90a28aa0234

V5 IR cache
265f27036b75afb3ae14eea9e3c1f03d091052f495deaf6c1ae903222eafea0e

subject-fold manifest
0ae2bd6a594152dd1af444566416410043ac11f153d20c8a517bb2a6d5052b73
```

Before V7 scoring is admitted, it reproduces V5 on all 809 HAU episodes, V5 on matched support, and B5 on matched support within `1e-6`, including fold-level balanced accuracy and exact-set accuracy.

## Current licensed state

```text
V7_DESIGN_FROZEN                = true
V7_IMPLEMENTATION_AUTHORIZED    = true
V7_IMPLEMENTATION_CONSTRUCTED   = true
V7_EXECUTION_AUTHORIZED         = true
V7_EXECUTION_PRECHECK           = V7_PRECHECK_BLOCKED
V7_FIRST_FEATURE_EXTRACTED      = false
V7_PRIMARY_RESULT               = NOT_OBSERVED
V7_SECONDARY_RESULT             = NOT_OBSERVED
V7_SCIENTIFIC_EVIDENCE_SEEN     = false
```

The only remaining operation is operational execution of this exact frozen script in the local CUHK-X workspace containing the required inputs. No scientific redesign is licensed by the block.
