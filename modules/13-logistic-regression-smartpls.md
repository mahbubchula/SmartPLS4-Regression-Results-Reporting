# Optional Module 13: Logistic Regression in SmartPLS 4

## Purpose

The shared paper includes both multiple linear regression and logistic regression. This module teaches the logistic regression workflow in SmartPLS 4 for a binary dependent variable.

## Learning Objectives

After this module, learners should be able to:

- Decide when logistic regression is appropriate.
- Build a logistic regression model in SmartPLS 4.
- Interpret logit coefficients, Wald tests, and odds ratios.
- Assess model fit using deviance, AIC, BIC, pseudo R-square, and confusion matrix.
- Write a logistic regression results section.

## When to Use Logistic Regression

Use logistic regression when the dependent variable is binary:

```text
0 = no / reference group
1 = yes / focal group
```

Examples:

- Region: 0 = USA/North America, 1 = outside North America
- Adoption: 0 = not adopted, 1 = adopted
- Purchase: 0 = no purchase, 1 = purchase

## SmartPLS Model

For the HBAT-style dataset:

```text
X4 <- X6 + X7 + X8 + X9 + X10 + X11 + X12 + X13 + X14 + X15 + X16 + X17 + X18
```

where `X4` is binary region membership.

## SmartPLS Settings

1. Select `Calculate`.
2. Select `Logistic Regression`.
3. Use default maximum iterations and stop criterion unless convergence fails.
4. Use two-tailed test and 0.05 significance level unless theory justifies another setting.
5. Open the report after calculation.

## Fit Assessment

Assess:

- Log-likelihood
- Deviance
- AIC
- BIC
- McFadden's R-square
- Cox and Snell's R-square
- Nagelkerke's R-square
- Confusion matrix

Lower deviance, AIC, and BIC indicate better model fit when comparing models.

## Coefficient Interpretation

Logistic coefficients are changes in log-odds, not direct changes in probability.

If a coefficient is positive:

```text
Higher X increases the log-odds of being in the group coded 1.
```

If a coefficient is negative:

```text
Higher X decreases the log-odds of being in the group coded 1.
```

## Odds Ratio Interpretation

The odds ratio is:

```text
exp(coefficient)
```

If odds ratio > 1:

```text
The odds increase.
```

If odds ratio < 1:

```text
The odds decrease.
```

## Reporting Template

Use [logistic-regression-results-report-template.md](../templates/logistic-regression-results-report-template.md).

## Checklist

Use [logistic-regression-assessment-checklist.md](../checklists/logistic-regression-assessment-checklist.md).

## Practice

1. Run the HBAT-style logistic model in SmartPLS.
2. Export the fit summary.
3. Export the confusion matrix.
4. Export the coefficients and Wald tests.
5. Convert at least three coefficients into odds ratios.
6. Write a results paragraph without interpreting coefficients as direct probability changes.
