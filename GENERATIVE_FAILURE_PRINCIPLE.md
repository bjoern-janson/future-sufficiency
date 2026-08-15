# Generative Failure Principle — the billiard principle

Status: methodological operating principle frozen on 2026-08-15. This document does **not** assert a universal theory of failure, intelligence, or mechanism discovery. It freezes a disciplined rule for preserving and using failure evidence in future experiments.

## Core principle

> **The wall is part of the map.**

A failure is not merely a negative outcome. It can be a contact event between an attempted transition and the constraints encountered through the current system.

The apparent reachable boundary is therefore indexed by the constituted system:

    ∂R^{A,O,M,C}

where `A` denotes the admissible action/intervention set, `O` the observation or representation interface, `M` the current model/estimator/mechanism class, and `C` the experimental or operational context.

Thus:

    contact
    != ontic boundary identified

A collision may reflect a world constraint, interface constraint, action-space limitation, estimator artifact, implementation defect, or an interaction among them.

## Preserved collision witness

Let the system propose a transition

    s_hat_{t+1} = G(s_t, a_t)

and observe

    s_{t+1}.

The preserved witness is

    W_t = (s_t, a_t, s_hat_{t+1}, s_{t+1}, δ_t, C_t)

with a constituted discrepancy witness

    δ_t = D(s_hat_{t+1}, s_{t+1}; C_t).

`D` need not be Euclidean subtraction. It may be vector-valued, relational, categorical, order-based, graph-structured, or otherwise appropriate to the scientific object.

A numerical residual

    r_t = s_{t+1} - s_hat_{t+1}

is only a special case when subtraction is licensed by the state representation.

The first legitimate role of `W_t` is to constrain explanations of the encountered boundary, not to identify a mechanism:

    W_t -> ΔH_{∂R}

subject to the measurement, representation, and intervention contract under which the witness was constituted.

## Authority firewall

The evidential hierarchy is:

    discrepancy
    != boundary identified
    != mechanism identified
    != repair authorized

Likewise:

    W_t
    -> Π_{t+1}^{admissible}
    != a*_{t+1}

A collision may reshape the candidate probe space. It does not select or authorize a particular repair.

Successful redirection still requires a fresh test.

## Four stages

Failure use is separated into four stages.

### 1. Preservation

    W_t remains available

The state, attempted transition, expectation, observed consequence, discrepancy, and contact context are retained with provenance.

### 2. Interpretation

    W_t contracts B_t

where `B_t` is the surviving family of boundary/explanation hypotheses compatible with the evidence.

The licensed update is constraint, not mechanism identification.

### 3. Generation

    W_t^{collision} -> ΔΠ_{t+1}

where `Π_{t+1}` is the admissible next-probe space.

This is the point at which failure becomes generative: preserved reality-contact changes the warranted geometry of future search.

### 4. Validation

    discriminating probe -> fresh evidence

The redirected probe must be executed and adjudicated under a fresh evidential contract before any stronger repair or causal authority is granted.

Therefore:

    preservation
    != interpretation
    != generation
    != validation

## One collision constrains; varied contacts characterize

Let

    W_k = {W_1, ..., W_k}

and let `B_k` denote the surviving family of boundary/explanation hypotheses after those contacts.

When new evidence is genuinely discriminating, the intended relation is

    B_{k+1} ⊆ B_k.

But repeated nominal failures are not automatically informative. Contacts may share the same implementation defect, hidden confounder, selection mechanism, malformed interface, or intervention geometry.

Therefore the stronger experimental rule is:

> **One collision constrains; varied independently grounded collisions characterize.**

The next probe should be chosen partly for how sharply its possible outcomes discriminate among the surviving boundary hypotheses, subject to cost, safety, admissibility, and the declared experimental contract.

Repeated contact from effectively the same direction may add little even when the failure count increases.

## Functional recovery and epistemic recovery

Every failure exposes two distinct recovery objectives:

    F_t -> (R_t^{functional}, R_t^{epistemic}).

Functional recovery restores viable operation.

Epistemic recovery preserves what the contact taught about the encountered constraint and its uncertainty.

The desired regime is

    R_t^{functional} = 1
    and
    R_t^{epistemic} = 1.

A system may instead achieve

    R_t^{functional} = 1,
    R_t^{epistemic} = 0

by quietly patching the consequence while erasing the collision witness.

This creates **epistemic debt**:

    successful patching
    + collision-witness erasure
    -> reduced future diagnostic capacity.

Provenance is therefore part of the adaptive substrate rather than merely administrative bookkeeping. Preserved collision history can retain information needed to diagnose future contacts.

## Generative chain

The operating chain is:

    contact
    -> constraint
    -> probe-space deformation
    -> discriminating probe
    -> fresh evidence.

The compact formulation is:

> **Failure becomes generative when preserved contact with reality changes the warranted geometry of future search.**

This is stronger than preserving a failure label and weaker than claiming the failure has explained its cause.

## Relation to C_improve

The principle motivates a candidate component of improvement capacity:

    C_{contact->search}
    = capacity to transform warranted discrepancy structure
      into better-directed future intervention geometry.

Conceptually:

    C_{contact->search} ⊆ C_improve.

This document does not identify the two quantities and does not claim that lower failure rate, higher information gain, or faster repair is sufficient for `C_improve`.

A relevant adaptive question is instead:

> Does experience make the next contact more discriminating, not merely less likely?

## CUHK-X methodological illustration

The CUHK-X V4 and V7 sequence is a useful retrospective illustration of the pattern, not causal proof of failure-driven search.

V4 showed that one tested representation direction — a fixed Depth-motion repair — produced degradation under the frozen task and validation contract.

V7 later tested a substantially different strong-IR representation direction and found a large material gain.

The licensed methodological reading is only:

    contact
    -> constraint on one tested direction
    -> different direction tested
    -> fresh outcome.

Do not infer:

    V4 caused V7

or

    V4 identified the successful mechanism.

## Five operating rules

1. **The wall is part of the map.**
2. **Contact does not identify which layer generated the wall.**
3. **One collision constrains; varied independently grounded collisions characterize.**
4. **A collision reshapes the candidate probe space; it does not authorize a particular repair.**
5. **Successful redirection still requires a fresh test.**

## Claim boundary

This principle currently has methodological authority only.

It does not establish that all failures are informative, that every discrepancy corresponds to a stable boundary, that repeated contacts identify an ontic mechanism, or that preserving every failure is worth its cost.

Future experiments may test when collision witnesses improve probe selection, when they fail to do so, what forms of independence are required for boundary characterization, and whether functional recovery can preserve epistemic recovery without excessive cost.

**Scientific rule:** preserve enough structure in reality-contact that later evidence can use the contact to constrain and redirect search without smuggling in mechanism or repair authority.
