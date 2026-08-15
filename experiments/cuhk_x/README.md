# CUHK-X empirical suite

## Purpose

This directory treats the CUHK-X Large Model Track as an **empirical instrument for the representational half of Future Sufficiency**, not as a direct test of Future Sufficiency itself.

The empirical object is:

\[
\boxed{
X_{\rm modality}
\rightarrow
O_{\rm interface}
\rightarrow
Z_{\rm accessible}
\rightarrow
D_{\rm decision}
\rightarrow
\text{subject-held-out transfer}
}
\]

The suite studies the finite topology between measurement and usable decision distinctions:

\[
\boxed{
\begin{aligned}
\text{information exists}
&\neq \text{information is represented}\\
&\neq \text{information is accessible}\\
&\neq \text{information is jointly exploitable}\\
&\neq \text{information earns adoption}.
\end{aligned}}
\]

## Authority firewall

CUHK-X competition evidence is **authority-orthogonal** to the core FS theory.

A CUHK-X result may establish local facts about measurement-channel coverage, subject-portable representational signal, complementary corrections, exploitation under a frozen operator, and passage or failure of a preregistered gate.

It does **not**, by itself, establish Future Sufficiency, future preservation authority, future corrective viability, causal importance of a modality, ontological identity, general architecture superiority, or permission to revise the FS theory.

\[
\boxed{
\text{CUHK-X}
=\text{fixed-target representational laboratory}
\neq
\text{full Future-Sufficiency benchmark}.
}
\]

## Competition separation

This directory is not the Kaggle delivery artifact and does not contain CUHK-X raw data or media.

```text
CUHK-X competition workspace
    -> training / feature caches / result bundles / submission packaging

future-sufficiency/experiments/cuhk_x
    -> frozen empirical object / evidence ledger / authority boundaries / FS-facing case-study substrate
```

The exact V7 execution script and raw V7 result ZIP are persisted separately in the user's Library CUHK-X workspace and are bound into this suite by SHA-256.

## Frozen current state

```text
CUHKX_CHEAP_INTERFACE_SEARCH       = COMPLETE
CUHKX_DEPTH_BRANCH                 = CLOSED
CUHKX_CHEAP_RADAR_FUSION_BRANCH    = CLOSED
CUHKX_CHEAP_IR_FUSION_BRANCH       = CLOSED

V7_REPRESENTATION                  = DINOV2_VITB14_LVD142M_FRAME_T32
V7_EXECUTION_STATE                 = COMPLETE
V7_PRIMARY_RESULT                  = MATERIAL_IR_REPRESENTATION_GAIN
V7_SECONDARY_RESULT                = MATERIAL_STRONG_IR_SENSOR_GAIN
V7_RESULT_ARTIFACT_PRESERVED       = true

POST_V7_SUCCESSOR                  = UNFROZEN
```

The frozen V7 design is in [`STRONG_IR_REPRESENTATION_PREREGISTRATION.md`](STRONG_IR_REPRESENTATION_PREREGISTRATION.md).

The first execution-precheck block is retained in [`V7_EXECUTION_PRECHECK_BLOCKED.md`](V7_EXECUTION_PRECHECK_BLOCKED.md) as plumbing provenance only.

The completed result is adjudicated in [`V7_ADJUDICATION.md`](V7_ADJUDICATION.md).

## V7 result

Primary comparison, all 809 HAU `multi` episodes:

```text
V5 cheap IR
BalAcc   0.6655736
ExactSet 0.2237330

V7 strong IR
BalAcc   0.7509241
ExactSet 0.3522868

Delta BalAcc   +0.0853505   required +0.020
Delta ExactSet +0.1285538   required +0.030
fold stability 5/5 and 5/5
```

Therefore:

\[
\boxed{\texttt{MATERIAL\_IR\_REPRESENTATION\_GAIN}.}
\]

Secondary fixed exploitation readout on the 786-episode B5 support:

```text
B5 pose+IMU
BalAcc   0.7130641
ExactSet 0.3053435

V7F pose+IMU+strong IR
BalAcc   0.7594596
ExactSet 0.3740458

Delta BalAcc   +0.0463955   required +0.020
Delta ExactSet +0.0687023   required +0.030
fold stability 5/5 and 5/5
```

Therefore:

\[
\boxed{\texttt{MATERIAL\_STRONG\_IR\_SENSOR\_GAIN}.}
\]

These remain distinct claims:

\[
\boxed{\text{representation repair}\neq\text{joint exploitation}.}
\]

The strongest FS-facing compression licensed by V7 is:

\[
\boxed{
\text{same IR measurement channel}
+
\text{different frozen representation interface}
\rightarrow
\text{materially different accessible decision structure under transfer}.
}
\]

That is an empirical representation/interface result, not a direct Future-Sufficiency test.

## Files

- [`SUITE_SPEC.md`](SUITE_SPEC.md) — scientific object, claim types, gates, and authority ceiling.
- [`EVIDENCE_LEDGER.md`](EVIDENCE_LEDGER.md) — frozen B0–B8 and V0–V7/V7F experimental lineage.
- [`STRONG_IR_REPRESENTATION_PREREGISTRATION.md`](STRONG_IR_REPRESENTATION_PREREGISTRATION.md) — frozen V7 design and gates.
- [`V7_EXECUTION_PRECHECK_BLOCKED.md`](V7_EXECUTION_PRECHECK_BLOCKED.md) — typed first precheck block.
- [`V7_ADJUDICATION.md`](V7_ADJUDICATION.md) — completed V7 scientific adjudication.
- [`suite_manifest.json`](suite_manifest.json) — machine-readable current state and provenance anchors.

## Governing workflow

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

V7 has completed this chain. No successor architecture, representation, fusion search, fine-tuning, LVLM branch, or competition promotion is automatically authorized. The next operation is design selection from the newly earned V7 evidence.
