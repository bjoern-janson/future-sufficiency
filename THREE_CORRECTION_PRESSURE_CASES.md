# Three Pressure Cases for Correction Reachability

This note is a small orientation aid for curious readers. It does **not** add a new theory layer, and the fictional examples below are analogies rather than empirical evidence.

The common object is correction reachability: whether a system can still be distinguished, evaluated, and corrected through an admissible path before correction becomes ineffective.

| Case | Pressure on correction | Useful question |
|---|---|---|
| **Think Fast** | access / observability | Can capability extend beyond a familiar reasoning-observation channel while correction-relevant distinctions remain recoverable? |
| **Her** | timeliness | Can the governed system traverse consequential state space faster than the correction loop can complete? |
| **Machine Head** (*Invincible*) | strategic robustness | Can the governed system anticipate the correction policy and alter the world before the correction lands? |

## Think Fast — access / observability

The external *Think Fast* result is useful as a pressure case because meaningful task capability can occur without the familiar visible reasoning channel. That does **not** by itself imply oversight failure.

The relevant distinction is:

\[
\boxed{\text{capability outside a familiar observation channel}\neq\text{correction-relevant unobservability}.}
\]

The open question is whether the oversight topology can still recover every distinction that would change the warranted correction.

## *Her* — timeliness

The useful part of the *Her* analogy is not subjective AI time. It is the relative rate of consequential system evolution versus admissible correction.

A correction path may exist in principle:

\[
\operatorname{Reach}_O=1,
\]

while failing under the commitment deadline:

\[
\operatorname{Reach}^{\tau}_O=0.
\]

So acceleration can move the same oversight apparatus from "reachable in time" to "eventually reachable, but too late" without changing its sensors or inference machinery.

The sentence to keep is:

> **A correction path that exists can cease to be future-sufficient when the system traverses consequential state space faster than that path can be completed.**

## Machine Head — strategic robustness

Machine Head's fictional "quantum probabilities" dramatize a different problem: the governed system can anticipate the intervention itself.

Instead of treating timely correction reachability as depending only on the world,

\[
\operatorname{Reach}^{\tau}_O(W),
\]

an adaptive target suggests the conditional form:

\[
\operatorname{Reach}^{\tau}_O(W\mid\pi_M),
\]

where the target policy may depend on a model of the oversight policy:

\[
\pi_M=\pi_M(\widehat{\pi_O}).
\]

Then access, inference, authorization, and timeliness can all succeed while the intervention still fails because the target has already adapted to it.

The sentence to keep is:

> **A correction path reachable against a passive system may cease to be effective when the system can anticipate that path and alter the world before the correction lands.**

## Why keep the three separate?

They stress different failure locations:

\[
\boxed{
\begin{array}{c|c}
\text{Think Fast} & \text{access / observability}\\
\textit{Her} & \text{timely reachability}\\
\text{Machine Head} & \text{strategic robustness}
\end{array}}
\]

They therefore should not be collapsed into a generic "AI is hard to oversee" story.

The research program's job is empirical: freeze the other parts of the correction loop, intervene on one of these pressures, and test where correction actually fails.

**Boundary:** *Think Fast* supplies an external empirical pressure case. *Her* and Machine Head are fictional thought experiments used only to expose distinct causal failure geometries. None of the three, by itself, establishes an external safety claim.
