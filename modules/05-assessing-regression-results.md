# Module 5: Assessing Regression Results

## Purpose

This module teaches how to assess SmartPLS regression output systematically.

## Learning Objectives

After this module, learners should be able to:

- Interpret coefficient direction, size, and significance.
- Assess R-square and adjusted R-square.
- Inspect diagnostic plots.
- Identify multicollinearity and unstable estimates.

## Regression Assessment Order

1. Confirm the model ran successfully.
2. Check sample size after missing-data handling.
3. Check descriptive statistics.
4. Assess collinearity among predictors.
5. Interpret unstandardized coefficients.
6. Interpret standardized coefficients.
7. Assess p-values, t-values, and confidence intervals.
8. Assess R-square and adjusted R-square.
9. Inspect QQ plot and residual diagnostics.
10. Decide whether robust standard errors are needed.

## Coefficient Interpretation

Template:

```text
Holding the other predictors constant, a one-unit increase in X was associated with a b-unit change in Y.
```

Example:

```text
Holding ease of use, trust, service quality, age, and experience constant, perceived usefulness was positively associated with satisfaction.
```

## R-Square

R-square represents the proportion of variance in the dependent variable explained by the predictors.

Adjusted R-square penalizes unnecessary predictors and is usually better for comparing models with different numbers of predictors.

## Diagnostics

Check:

- QQ plot for residual normality
- Residual patterns
- Influential cases if available
- Multicollinearity among predictors
- Heteroscedasticity concerns

## Red Flags

- Significant coefficient with wrong theoretical sign
- Very high standard errors
- Predictors highly correlated with each other
- R-square very high but weak theory
- Results change strongly after adding controls
- Reporting p-values without effect interpretation

## Lab

Complete [Lab 3: Assess regression output](../labs/lab03-results-assessment.md).

## Next Module

Continue to [Module 6: Regression Bootstrapping](06-regression-bootstrapping.md).
