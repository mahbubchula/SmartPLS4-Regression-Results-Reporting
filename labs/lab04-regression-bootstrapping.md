# Lab 4: Regression Bootstrapping

## Goal

Run regression bootstrapping in SmartPLS 4 and use bootstrap confidence intervals for final inference.

## Recommended Settings

Initial check:

```text
Subsamples: 1,000
```

Final reporting:

```text
Subsamples: 10,000
Confidence interval: Percentile bootstrap
Test type: Two-tailed unless directional hypothesis was pre-specified
Significance level: 0.05
Seed: Fixed seed for reproducibility
```

## Steps

1. Return to the model window.
2. Select Calculate.
3. Select Regression Bootstrapping.
4. Choose the final settings.
5. Run the calculation.
6. Open the bootstrapping report.
7. Export coefficient table and confidence intervals.

## Interpretation

A coefficient is significant when its confidence interval does not include zero at the selected confidence level.

## Deliverable

Submit a bootstrapping table:

| Predictor | b | t | p | 95% CI | Decision |
|---|---:|---:|---:|---|---|

## Next Lab

Continue to [Lab 5](lab05-plssem-assessment.md).
