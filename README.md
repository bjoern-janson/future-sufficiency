# Future Sufficiency

## Hypothesis

A representation that preserves a present invariant need not preserve the distinctions required for future transformation.

## Core claim

    ΔI = 0 does not imply ΔFuture = 0

More specifically, a representation I may identify states X and Y while those states differ in future-relevant behavior:

    I(X) = I(Y)
    and
    Future(X) ≠ Future(Y)

## Research question

Can representational closure defect predict when acquiring a missing distinction has positive value for future decision-making?

## Experimental principle

The project distinguishes:

- present-state equivalence
- dynamic closure
- future reachability
- predictive sufficiency
- viability
- reopenability
- adaptive value

These must not be collapsed into a single metric.

## Planned test

Construct environments in which:

1. Two latent states are aliased under the initial representation.
2. Their immediate observations/rewards are matched or nearly matched.
3. Their future viable possibilities differ.
4. The agent can optionally acquire information at a cost.
5. The agent's representation can be updated.
6. Later behavior is evaluated on held-out futures.

The critical behavioral chain is:

    representational insufficiency
    → information acquisition
    → new distinction
    → representation update
    → changed future policy
    → improved future outcome

## Controls

The main comparison should be:

    closure-directed refinement
    vs.
    generic extra representation

The experiment should distinguish:

    "more information helps"

from:

    "the specific missing distinction identified by closure analysis helps."

## Status

Research scaffold. No empirical claim is considered established until supported by a preregistered or otherwise reproducible experiment.

## Citation

If you use this repository in your work, please cite:

> Janson, Björn. *Future Sufficiency*. GitHub repository, 2026.

Machine-readable citation metadata is provided in [`CITATION.cff`](CITATION.cff), which enables GitHub's **Cite this repository** feature.

## License

This repository is licensed under the MIT License. See [`LICENSE`](LICENSE).
