# Results Assessment Workbook

Use this workbook after running the HBAT-style case in SmartPLS.

## Part 1: Linear Regression Model

Model:

```text
X19 <- X6 + X7 + X9 + X11 + X12
```

### Overall Fit

| Item | SmartPLS Result | Interpretation |
|---|---|---|
| F-test or ANOVA significance | | |
| R-square | | |
| Adjusted R-square | | |
| Durbin-Watson | | |

### Collinearity

| Predictor | VIF | Condition Index Note |
|---|---:|---|
| X6 | | |
| X7 | | |
| X9 | | |
| X11 | | |
| X12 | | |

### Coefficients

| Predictor | b | beta | t | p | 95% CI | Interpretation |
|---|---:|---:|---:|---:|---|---|
| X6 | | | | | | |
| X7 | | | | | | |
| X9 | | | | | | |
| X11 | | | | | | |
| X12 | | | | | | |

### Assumptions

| Assumption | SmartPLS Evidence | Decision |
|---|---|---|
| Linearity | Predicted vs residual; predicted vs actual | |
| Homoscedasticity | Predicted vs residual; Breusch-Pagan | |
| Independence | Residual autocorrelation; Durbin-Watson | |
| Normality | QQ plot; residual histogram | |
| Collinearity | VIF; condition index | |

## Part 2: Logistic Regression Model

Model:

```text
X4 <- X6 + X7 + X8 + X9 + X10 + X11 + X12 + X13 + X14 + X15 + X16 + X17 + X18
```

### Fit Summary

| Item | Null Model | Estimated Model | Interpretation |
|---|---:|---:|---|
| Log-likelihood | | | |
| Deviance | | | |
| AIC | | | |
| BIC | | | |

### Pseudo R-Square

| Measure | Value | Interpretation |
|---|---:|---|
| McFadden's R-square | | |
| Cox and Snell's R-square | | |
| Nagelkerke's R-square | | |

### Classification

| Classification Item | Value | Interpretation |
|---|---:|---|
| Correctly classified group 0 | | |
| Correctly classified group 1 | | |
| Overall classification accuracy | | |

### Logistic Coefficients

| Predictor | Coefficient | Wald | p | Odds Ratio | Interpretation |
|---|---:|---:|---:|---:|---|
| X6 | | | | | |
| X7 | | | | | |
| X8 | | | | | |
| X9 | | | | | |
| X10 | | | | | |
| X11 | | | | | |
| X12 | | | | | |
| X13 | | | | | |
| X14 | | | | | |
| X15 | | | | | |
| X16 | | | | | |
| X17 | | | | | |
| X18 | | | | | |

## Final Interpretation Prompts

1. Which predictors matter most in the linear model?
2. Does the linear model explain a meaningful amount of satisfaction variance?
3. Which logistic predictors significantly separate region groups?
4. Are odds ratios interpreted correctly?
5. What limitations should be stated?
