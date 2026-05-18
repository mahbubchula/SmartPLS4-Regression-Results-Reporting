# Module 4: Running Linear Regression

## Purpose

This module teaches how to run linear regression in SmartPLS 4 and select appropriate settings.

## Learning Objectives

After this module, learners should be able to:

- Run single and multiple regression in SmartPLS.
- Choose test type and significance level.
- Choose normal, HC3, or HC4 standard errors.
- Understand standardized and unstandardized coefficients.

## Regression Settings

Key settings:

| Setting | Practical Guidance |
|---|---|
| Test type | Use two-tailed unless directional hypothesis is justified before analysis |
| Significance level | Commonly 0.05 |
| Standard error type | Start with normal; use HC3/HC4 when heteroscedasticity or leverage is a concern |
| Intercept | Usually included |

SmartPLS documentation identifies HC3 and HC4 as heteroscedasticity-consistent alternatives to normal standard errors.

## Unstandardized and Standardized Coefficients

Unstandardized coefficient:

```text
One-unit change in X is associated with b-unit change in Y.
```

Standardized coefficient:

```text
One standard deviation change in X is associated with beta standard deviation change in Y.
```

Use unstandardized coefficients for practical interpretation and standardized coefficients for relative predictor comparison.

## Single vs Multiple Regression

Single regression:

```text
Y <- X1
```

Multiple regression:

```text
Y <- X1 + X2 + X3 + controls
```

Multiple regression coefficients are adjusted for other predictors in the model.

## Practice

1. Run the simple regression model.
2. Run the multiple regression model.
3. Export the result report.
4. Compare standardized and unstandardized coefficients.
5. Record R-square and adjusted R-square.

## Next Module

Continue to [Module 5: Assessing Regression Results](05-assessing-regression-results.md).
