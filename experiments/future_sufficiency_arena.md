# Future-Sufficiency Arena — Experiment 001

## Falsifiable claim

> **Closure defect predicts the value of acquiring a missing distinction.**

Operationally, when the current representation aliases latent states whose future consequences differ, a targeted information probe should have positive decision value; when the aliased states are future-equivalent, the same probe should not be worth its cost.

The repository treats this as an empirical claim, not as a consequence of the formalism.

## Minimal arena

Each episode begins in one of two latent states, `x_a` or `x_b`. The initial representation `I` intentionally hides that distinction. Immediate observation and reward are identical across the pair.

There are two visible regimes:

- **divergent**: `x_a` and `x_b` require different terminal actions for the best future outcome;
- **aligned**: `x_a` and `x_b` have the same best terminal action.

The binary arena defect is defined before observing the terminal outcome:

    Gamma_I = 1  if an I-equivalence class contains states with different action-conditioned futures
    Gamma_I = 0  otherwise

This is an operational closure-defect measure for the arena, not a claim that all useful closure defects are binary.

## Information conditions

Before the terminal decision, the agent may choose one of three conditions:

1. **no probe** — acquire no extra information and pay no cost;
2. **generic probe** — pay the probe cost to reveal an equally sized but decision-irrelevant nuisance bit;
3. **closure-targeted probe** — pay the same cost to reveal whether the latent state is `x_a` or `x_b`.

The generic probe controls for the weaker explanation that additional information is beneficial merely because it is additional information.

## Primary prediction

Across held-out episodes:

    Gamma_I ↑  =>  P(targeted probe) ↑

and the targeted probe should have positive net value specifically in the divergent regime:

    value(targeted probe | Gamma_I = 1) > 0
    value(targeted probe | Gamma_I = 0) <= 0

The stronger behavioral chain to test with a learning agent is:

    representation insufficiency
    -> targeted information acquisition
    -> newly available distinction
    -> persistent policy change
    -> improved held-out future outcome

## Controls

The critical comparison is:

    closure-targeted probe > generic probe

under equal probe cost and matched information capacity.

Report probe rate and net return separately. A higher score alone is not sufficient evidence for the hypothesis.

## Falsification / failure conditions

The initial claim is not supported if any of the following persists under reproducible evaluation:

- the measured defect does not predict when the targeted probe has positive net value;
- probing rises equally in aligned and divergent regimes;
- generic extra information performs as well as the closure-targeted distinction;
- any improvement disappears on held-out latent-state/regime sequences;
- the agent verbalizes uncertainty or model error without changing information acquisition and later policy.

## Scope

This experiment tests representation closure, information acquisition, and future decision value only. It makes no claim about consciousness, JT, or broader cognitive architecture.

**Scientific rule:** empirical obligation > further abstraction.
