# CUHK-X V7 — preregistered matched-support characterization

The V7 preregistration required a secondary standalone characterization of V5, V7, and B5 on the exact 786-episode B5 common support.

The execution result bundle emitted the all-809 V7 candidate/exact predictions and the matched B5 membership but did not surface the V7-matched scalar metrics in `summary.json`. The following values are therefore a deterministic reporting completion computed only by filtering the already-frozen V7 predictions to the 786 `qa_id` values present in the B5 matched predictions. No model was refit, no threshold changed, and no new scientific branch was executed.

```text
population                  786 episodes / 3144 candidate decisions

V5 matched
BalAcc                      0.6690153668069166
MacroF1                     0.6676785806852936
ExactSet                    0.24427480916030533

B5 matched
BalAcc                      0.7130640619614627
MacroF1                     0.7120487083722378
ExactSet                    0.3053435114503817

V7 strong IR matched
candidate accuracy          0.7531806615776081
BalAcc                      0.7524760523628986
MacroF1                     0.7522759496848092
ExactSet                    0.356234096692112

V7F B5 + strong IR matched
BalAcc                      0.7594595605210277
MacroF1                     0.7590965236694271
ExactSet                    0.37404580152671757
```

Descriptive matched-support contrasts:

```text
V7 - B5 BalAcc              +0.0394119904014359
V7 - B5 ExactSet            +0.0508905852417303

V7F - V7 BalAcc             +0.0069835081581291
V7F - V7 ExactSet           +0.0178117048346056
```

These contrasts were not separate preregistered promotion gates. They do not retroactively promote V7 as a competition incumbent and do not alter the frozen V7 primary/secondary adjudications.

The licensed descriptive statement is only:

> On the exact B5 common support, the frozen strong-IR representation is individually stronger than B5 on the reported metrics, while the fixed B5+strong-IR concatenation provides a further smaller numerical gain.

This artifact closes a reporting omission; it does not create a new fitted result.
