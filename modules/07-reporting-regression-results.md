# Module 7: Reporting Regression Results

## Purpose

Regression results must be reported in a way that a supervisor, reviewer, or reader can understand and verify.

## Learning Objectives

After this module, learners should be able to:

- Create a regression results table.
- Write an interpretation paragraph.
- Report model fit and diagnostics.
- Avoid causal overclaiming.

## Minimum Reporting Items

Report:

- SmartPLS version
- Dataset and final sample size
- Dependent variable
- Independent variables
- Control variables
- Standard error type
- Test type and significance level
- Coefficients
- Standard errors
- t-values
- p-values
- Confidence intervals
- R-square and adjusted R-square
- Diagnostic summary

## Regression Table Structure

| Predictor | b | beta | SE | t | p | 95% CI |
|---|---:|---:|---:|---:|---:|---|
| Usefulness | | | | | | |
| Ease of use | | | | | | |
| Trust | | | | | | |
| Service quality | | | | | | |

## Results Paragraph Template

```text
A multiple linear regression was conducted in SmartPLS 4 to examine predictors of [dependent variable]. The model explained [R2]% of the variance in [dependent variable] (R2 = ..., adjusted R2 = ...). Holding the other predictors constant, [predictor] had a positive and significant association with [dependent variable] (b = ..., beta = ..., t = ..., p = ..., 95% CI [..., ...]). The diagnostic plots did/did not indicate major violations of regression assumptions.
```

## What Not to Write

Avoid:

- "The model proves..."
- "X has an impact" when the design only supports association.
- "The hypothesis is accepted" without explaining the effect size and direction.
- Reporting only p-values.
- Ignoring diagnostics.

## Lab

Complete [Lab 6: Write the final results section](../labs/lab06-reporting-results.md).

## Template

Use [regression-results-report-template.md](../templates/regression-results-report-template.md).

## Next Module

Continue to [Module 8: PLS-SEM Measurement Model](08-plssem-measurement-model.md).
