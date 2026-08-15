# CUHK-X V7 — stronger IR representation preregistration

## 0. Status

```text
probe_id                              CUHKX_V7_STRONG_IR_DINOV2_B14
design_selection_state                FROZEN
scientific_locus                       VISUAL_REPRESENTATION_CAPACITY
physical_modality                      IR
primary_target                         HAU_MULTI_CANDIDATE_ACTION_PRESENCE
subject_folds                          FROZEN_CANONICAL_FIVE
strong_IR_representation_family       DINOV2_VITB14_LVD142M_FRAME_T32
implementation_authorized              false
execution_authorized                   false
next_operation                         YES_THIS_IS_THE_NEXT_STEP
```

This artifact freezes **one** stronger IR representation family before implementation or execution.

It creates no new CUHK-X empirical evidence and does not modify the FS core theory.

The governing chain remains:

\[
\boxed{
\mathrm{FREEZE}
\rightarrow
\mathrm{YES,\ this\ is\ the\ next\ step}
\rightarrow
\mathrm{EXECUTE}
\rightarrow
\mathrm{ADJUDICATE}
}
\]

Creation of this artifact completes only the first term.

---

# 1. Scientific question

The primary question is:

\[
\boxed{
O_{\rm IR}^{cheap}
\quad\text{vs}\quad
O_{\rm IR}^{strong}
}
\]

with the following held fixed:

```text
physical channel        IR
empirical unit          episode
source                  HAU
category                multi
candidate vocabulary    same 40 action phrases
subject folds           same canonical five folds
decision family         same per-action linear hinge-SGD
threshold               margin >= 0
```

The licensed primary question is:

> Does a frozen DINOv2 ViT-B/14 frame representation expose materially more subject-portable HAU candidate-action structure than the already-characterized V5 cheap IR interface?

This is a representation-capacity probe, not a general model comparison.

---

# 2. Why this representation family was selected

The design-selection set considered only three representation classes:

```text
A  frozen self-supervised image backbone + fixed temporal operator
B  frozen vision-language image backbone + fixed temporal operator
C  pretrained video backbone with learned temporal representation
```

Representative implementations used only to make the design decision were:

```text
A  DINOv2 ViT-B/14
B  SigLIP 2 ViT-B/16
C  VideoMAE V2 ViT-B
```

No CUHK-X score was observed for any of these candidates during selection.

The selection criteria were:

\[
\boxed{
\text{IR compatibility}
\times
\text{temporal adequacy}
\times
\text{subject-transfer plausibility}
\times
\text{offline reproducibility}
\times
\text{competition packaging}
\times
\text{licensing}
\times
\text{attribution cleanliness}.
}
\]

The selected class is **A**, instantiated by DINOv2 ViT-B/14, because it changes the visual representational interface while leaving temporal aggregation and the downstream decision machinery explicit and fixed.

This is the decisive methodological advantage:

\[
\boxed{
\text{stronger learned frame representation}
\neq
\text{new learned temporal reasoner}.
}
\]

A vision-language encoder would additionally import language-aligned pretraining semantics. A pretrained video encoder would change learned spatial and temporal representation jointly. Those are legitimate later classes but are not the cleanest first test of the currently localized bottleneck.

This selection is **not** evidence that DINOv2 is empirically superior to SigLIP 2 or VideoMAE V2 on CUHK-X.

---

# 3. Frozen pretrained backbone

```text
provider / project       Meta AI / facebookresearch/dinov2
source repository         facebookresearch/dinov2
source revision           7764ea0f912e53c92e82eb78a2a1631e92725fc8
hub symbol                dinov2_vitb14
architecture              ViT-B/14
register tokens           none
pretraining weights       LVD142M
parameters                86M
embedding dimension       768
patch size                14
fine-tuning               forbidden
license                    Apache-2.0 at design freeze
```

The source revision is pinned so later repository changes cannot silently redefine the representation.

Before the first CUHK-X feature extraction, implementation preflight must additionally bind and record:

```text
exact downloaded checkpoint SHA-256
exact torch version
exact torchvision version
exact preprocessing implementation SHA-256
```

If the official `dinov2_vitb14` LVD142M checkpoint cannot be acquired or hash-bound, the result is:

```text
V7_PRECHECK_BLOCKED
```

and execution stops before feature extraction.

No model substitution is permitted.

---

# 4. Frozen frame sampling

For an IR clip with decoded frame count \(N\ge1\), select exactly 32 normalized-time positions.

For \(j=0,\ldots,31\):

\[
\boxed{
i_j
=
\left\lfloor
\frac{j(N-1)}{31}+\frac12
\right\rfloor.
}
\]

The selected frame is the actual decoded frame at index \(i_j\).

Rules:

```text
sample_count             32
sampling                 deterministic uniform normalized time
inter-frame interpolation forbidden
duplicate frame indices  allowed when N < 32
random temporal crop      forbidden
window search             forbidden
```

This preserves the existing T32 temporal resolution convention while avoiding a new temporal-model search.

---

# 5. Frozen IR preprocessing

Each selected decoded IR frame is transformed as follows.

## 5.1 Grayscale constitution

The released IR MP4 decodes as three highly correlated channels. Define one grayscale plane by arithmetic channel mean:

\[
g=\frac{R+G+B}{3\cdot255}.
\]

Then form a three-channel tensor by replication:

\[
[g,g,g].
\]

No learned colorization or pseudo-color transform is allowed.

## 5.2 Resolution normalization

Resize every frame directly to:

```text
width   224
height  168
```

using bicubic interpolation.

Thus the tensor shape before batching is:

```text
3 x 168 x 224
```

Both dimensions are exact multiples of the DINOv2 patch size 14:

```text
224 / 14 = 16
168 / 14 = 12
```

This deliberately preserves the original 4:3 aspect ratio and maps both the 320x240 training stream and 640x480 test stream into one common measurement geometry.

No center crop, random crop, padding search, or resolution search is allowed.

## 5.3 Normalization

After conversion to float in `[0,1]`, apply the standard DINOv2/ImageNet channel normalization:

```text
mean = (0.485, 0.456, 0.406)
std  = (0.229, 0.224, 0.225)
```

No dataset-specific intensity normalization is learned.

---

# 6. Frozen frame representation

The DINOv2 backbone is always in evaluation/inference mode with gradients disabled.

For each selected frame \(j\), retain only the normalized class-token representation:

\[
\boxed{
e_j
=
\texttt{x\_norm\_clstoken}(I_j)
\in\mathbb R^{768}.
}
\]

Forbidden alternatives include:

```text
patch-token pooling
intermediate-layer concatenation
register-token variants
multi-scale extraction
fine-tuning
linear probing inside DINOv2
prompt/text conditioning
feature selection
PCA
learned dimensionality reduction
```

The 768-D CLS token is the complete frame-level learned representation for V7.

---

# 7. Frozen temporal aggregation

Let:

\[
E=(e_0,\ldots,e_{31}),
\qquad
\Delta e_j=e_{j+1}-e_j.
\]

The episode representation concatenates, in this exact order:

```text
1. 32 x 768 class-token trajectory
2. 31 x 768 first-difference trajectory
3. per-coordinate trajectory mean
4. per-coordinate trajectory std
5. per-coordinate trajectory min
6. per-coordinate trajectory max
7. per-coordinate difference mean
8. per-coordinate difference std
9. per-coordinate difference max-absolute value
10. log1p(decoded frame count)
11. decoded frame count / 10.0
```

Dimension:

\[
\boxed{
32(768)+31(768)+4(768)+3(768)+2
=53{,}762.
}
\]

No attention pooling, RNN, temporal transformer, optical flow, window max, learned temporal gate, or alternate summary is authorized.

This operator intentionally mirrors the temporal structure of the cheap V5 representation while replacing raw low-resolution pixels with one frozen learned frame embedding.

---

# 8. Frozen downstream decision interface

The downstream candidate-action classifier remains the same family used by the cheap ladder.

For each candidate action independently:

```text
StandardScaler
SGDClassifier(
    loss="hinge",
    penalty="l2",
    alpha=1e-4,
    class_weight="balanced",
    max_iter=100,
    tol=1e-3,
    shuffle=True,
    random_state=260813,
    average=True,
    n_jobs=-1,
)
```

Decision:

```text
margin >= 0  -> candidate present
margin < 0   -> candidate absent
```

No classifier-family change, hyperparameter search, threshold tuning, calibration, or action-specific architecture search is permitted.

---

# 9. Frozen populations

## 9.1 Primary representation comparison

Primary population:

```text
all 809 HAU multi episodes
3236 candidate-action pairs
same five subject-held-out folds
```

Compare:

```text
V5  cheap IR
V7  DINOv2-B/14 IR
```

Both are evaluated on identical episodes, candidate labels, folds, and classifier family.

## 9.2 Matched incumbent characterization

A secondary characterization uses the exact 786-episode B5 common support:

```text
786 episodes
3144 candidate-action pairs
```

On this support report V5, V7, and B5 separately.

This secondary standalone comparison does not itself authorize replacement of B5.

---

# 10. Primary materiality gate

Primary metrics:

```text
candidate balanced accuracy
candidate macro-F1
exact four-candidate set accuracy
fold-level balanced accuracy
fold-level exact-set accuracy
```

Macro-F1 is reported but is not a promotion threshold.

Freeze:

```text
MATERIAL_IR_REPRESENTATION_GAIN iff ALL:
    V7 - V5 pooled balanced accuracy >= +0.020
    V7 - V5 pooled exact-set accuracy >= +0.030
    V7 >= V5 balanced accuracy in >= 4/5 folds
    V7 >= V5 exact-set accuracy in >= 3/5 folds
```

Otherwise:

```text
NO_MATERIAL_IR_REPRESENTATION_GAIN
```

A numerically positive result below the gate may be described as positive but submaterial; it does not count as a material representation repair.

The threshold must not be changed after scoring.

---

# 11. Secondary fixed exploitation readout

The representation probe also preregisters **one** secondary joint readout. It is not a fusion search.

On the exact 786 B5 support define:

\[
\boxed{
X_{V7F}
=
[\phi_{pose},\phi_{IMU},\phi_{V7\text{-}IR}].
}
\]

Dimensions:

```text
pose              3,782
IMU               2,817
V7 strong IR     53,762
total            60,361
```

Use the same fixed StandardScaler + per-action hinge-SGD and zero-margin threshold.

The secondary gate is exactly the existing cheap-fusion materiality standard:

```text
MATERIAL_STRONG_IR_SENSOR_GAIN iff ALL:
    V7F - B5 pooled balanced accuracy >= +0.020
    V7F - B5 pooled exact-set accuracy >= +0.030
    V7F >= B5 balanced accuracy in >= 4/5 folds
    V7F >= B5 exact-set accuracy in >= 3/5 folds
```

Otherwise:

```text
NO_MATERIAL_STRONG_IR_SENSOR_GAIN
```

This secondary readout asks whether the newly frozen representation converts already-indicated IR complementarity into material joint gain.

Crucially:

\[
\boxed{
\text{material standalone representation gain}
\neq
\text{material joint exploitation gain}.
}
\]

Neither outcome may be imputed from the other.

No score-fusion follow-up is authorized by this preregistration.

---

# 12. Reproduction firewalls

Before V7 scoring is admitted:

```text
1. official QA archive hash must match frozen suite hash;
2. fold partition hash must match frozen suite hash;
3. V5 IR cache hash must match:
   265f27036b75afb3ae14eea9e3c1f03d091052f495deaf6c1ae903222eafea0e;
4. V5 pooled and fold metrics must reproduce within 1e-6;
5. for the secondary readout, pose and IMU cache hashes must match;
6. B5 pooled and fold metrics must reproduce within 1e-6;
7. DINOv2 source revision and exact checkpoint hash must be recorded before feature extraction.
```

Failure before scoring is a typed implementation/precheck failure, never an empirical negative.

\[
\boxed{
\text{plumbing failure}
\neq
\text{representation failure}.
}
\]

---

# 13. Compute and packaging constraints

The probe is intentionally bounded:

```text
one frozen backbone
32 frames per episode
no encoder fine-tuning
float32 inference
no mixed-precision requirement
feature extraction cached once
no architecture sweep
no augmentation
no test labels
no test-set model selection
```

A CUDA GPU may be used for operational speed, but device choice does not authorize any scientific change.

The DINOv2 code/model license is Apache-2.0 at design freeze. Final Kaggle packaging remains a separate competition-engineering operation and must independently verify then-current competition runtime and third-party asset requirements before submission.

No network access is part of the scientific inference operator once the official checkpoint has been acquired and hash-bound locally.

---

# 14. Explicitly forbidden branches

This freeze does not authorize:

```text
DINOv2 ViT-S/L/g comparison
DINOv2 register variant
SigLIP / SigLIP 2
CLIP / OpenCLIP
VideoMAE / VideoMAE V2
other pretrained vision backbones
encoder fine-tuning
end-to-end video model training
LVLM prompting
text-conditioned visual scoring
alternate frame counts
alternate spatial resolutions
crop search
augmentation search
PCA or learned feature compression
threshold search
score fusion
radar reopening
Depth reopening
Thermal escalation
use of test labels
```

A future branch must be earned by the adjudicated V7 evidence; it is not implied here.

---

# 15. Authority ceiling

A positive V7 primary result may establish only:

> Under the frozen HAU `multi` subject-held-out protocol, the selected frozen DINOv2-B/14 IR interface preserves materially more usable candidate-action structure than the previously frozen cheap IR interface.

It does not establish:

```text
IR modality sufficiency in general
DINOv2 optimality
causal importance of IR
mechanistic identification
general video understanding
Future Sufficiency
future preservation authority
future corrective viability
```

A positive secondary V7F result may additionally establish that this fixed stronger IR representation is jointly exploitable with B5 under the frozen simple-concatenation operator and materiality gate.

The strongest FS-facing interpretation remains representational:

\[
\boxed{
\text{same measurement channel}
+
\text{different frozen interface}
\rightarrow
\text{possibly different accessible decision structure}.
}
\]

---

# 16. Stop state

```text
V7_DESIGN_FROZEN                      = true
V7_REPRESENTATION_FAMILY              = DINOV2_VITB14_LVD142M_FRAME_T32
V7_PRIMARY_GATE_FROZEN                = true
V7_SECONDARY_EXPLOITATION_GATE_FROZEN = true
V7_IMPLEMENTATION_AUTHORIZED          = false
V7_EXECUTION_AUTHORIZED               = false

STOP = WAIT_FOR_YES_THIS_IS_THE_NEXT_STEP
```
