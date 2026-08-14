# Generality Principle

Status: methodological principle frozen after the `a47e534` minimal-substrate correction.

## Principle

> **Generality is an empirical intersection, not an assumption.**

A dependency may be called general only to the extent that it recurs across independently specified task families and preregistered repair contracts.

Formally, for task families and property sets

    (T_1, P_1), ..., (T_K, P_K),

let

    S_min(T_k, P_k)

be a minimal sufficient substrate relative to the declared task family, repair contract, and substrate partial order.

The candidate cross-family core is then

    G_core(K) = intersection_k S_min(T_k, P_k).

A recurring dependency is evidence for a more general mechanism only if it survives deliberate attempts to remove it across materially different task families.

## Positive and negative outcomes

If

    intersection_k S_min(T_k, P_k) != empty,

then recurring elements become candidates for a task-family-invariant repair substrate.

If

    intersection_k S_min(T_k, P_k) = empty,

then the theory should contract. The result would indicate that no small substrate-independent core has been established in the tested regime.

Neither outcome is treated as a failure of the research program.

## Edge acquisition rule

For a candidate dependency `s_i -> F_j`, use the evidential chain:

    remove(s_i)
    -> preregistered failure F_j
    -> replication
    -> matched control
    -> dependency edge acquisition

The mere fact that

    S^{-i} does not satisfy P

is insufficient to conclude that `s_i` is necessary. Incidental coupling, resource loss, changed search volume, or an altered problem definition must be ruled out first.

## Constitutive boundary

A dependency edge is empirical only when the intervention preserves the meaning of the target property.

If removing `s_i` makes the property itself undefined rather than violated, `s_i` is constitutive of the declared problem rather than empirically necessary for the repair mechanism.

## Current candidate core

The present sequence motivates, but has not yet established, the following candidate cross-family core:

    {
      relational evidence,
      future consequences,
      value-sensitive authorization,
      persistent state change,
      reopenability,
      termination discipline
    }

These are hypotheses to be attacked independently, not bundled into a single construct called "future sufficiency."

## Program-level criterion for generality

A claim of a general repair mechanism requires more than repeated benchmark success. It requires a recurring dependency structure across materially different task families:

    Dep(R | T_1, P_1),
    ...,
    Dep(R | T_K, P_K)

with a stable non-trivial intersection that survives substrate ablation.

Therefore:

    capability recurrence != mechanism generality

and

    mechanism generality must be earned by cross-family dependency recurrence.

## Scientific rule

**Generality is an empirical intersection, not an assumption.**

If the intersection disappears under broader task families, the theory contracts accordingly.
