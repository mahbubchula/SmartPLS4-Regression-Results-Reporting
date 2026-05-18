# Module 6: Regression Bootstrapping

## Purpose

Bootstrapping provides nonparametric standard errors and confidence intervals for regression estimates. SmartPLS supports regression bootstrapping for significance assessment.

## Learning Objectives

After this module, learners should be able to:

- Explain why bootstrapping is used.
- Select appropriate bootstrap settings.
- Interpret bootstrap confidence intervals.
- Report bootstrapped coefficients and significance.

## What Bootstrapping Does

Bootstrapping repeatedly draws samples from the original dataset with replacement and re-estimates the model. The distribution of bootstrap estimates is used to estimate standard errors, t-values, p-values, and confidence intervals.

## Recommended Workflow

For initial checking:

```text
1,000 bootstrap subsamples
```

For final reporting:

```text
10,000 bootstrap subsamples
```

Use a fixed seed for reproducibility.

## Confidence Intervals

If the confidence interval for a coefficient does not include zero, the coefficient is statistically significant at the chosen confidence level.

Example:

```text
b = 0.42, 95% CI [0.18, 0.66]
```

This coefficient is positive and statistically significant.

## Percentile vs BCa

SmartPLS documentation lists percentile, studentized, and BCa bootstrap options. Percentile bootstrap is the default recommendation. BCa can be considered when the bootstrap distribution is clearly non-normal.

## Reporting Template

```text
Bootstrapping with 10,000 subsamples was used to assess the significance of the regression coefficients. The effect of X on Y was positive and significant (b = ..., t = ..., p = ..., 95% CI [..., ...]).
```

## Lab

Complete [Lab 4: Run regression bootstrapping](../labs/lab04-regression-bootstrapping.md).

## Next Module

Continue to [Module 7: Reporting Regression Results](07-reporting-regression-results.md).
