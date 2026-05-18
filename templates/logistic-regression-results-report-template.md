# Logistic Regression Results Report Template

## Analysis Settings

The logistic regression analysis was conducted in SmartPLS 4. The dependent variable was `[binary dependent variable]`, coded as `[0 = ...]` and `[1 = ...]`. The independent variables were `[list predictors]`. The model was estimated using maximum likelihood estimation with `[default/custom]` maximum iterations and stopping criterion. Statistical significance was assessed using `[two-tailed/one-tailed]` tests at the `[0.05]` significance level.

## Model Fit

| Fit Criterion | Null Model | Estimated Model | Interpretation |
|---|---:|---:|---|
| Log-likelihood | | | |
| Deviance | | | |
| AIC | | | |
| BIC | | | |

The estimated model showed `[better/weaker]` fit than the null model because `[deviance/AIC/BIC]` was `[lower/higher]`.

## Pseudo R-Square

| Measure | Value | Interpretation |
|---|---:|---|
| McFadden's R-square | | |
| Cox and Snell's R-square | | |
| Nagelkerke's R-square | | |

## Confusion Matrix

| Classification Result | Value |
|---|---:|
| Correctly classified 0 group | |
| Correctly classified 1 group | |
| Overall classification accuracy | |

## Logistic Coefficients

| Predictor | Coefficient | Wald | p | Odds Ratio | Decision |
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

## Interpretation Paragraph

`[Predictor]` was a statistically significant predictor of group membership (`b = ...`, Wald = `...`, `p = ...`). The coefficient was `[positive/negative]`, indicating that higher values of `[predictor]` were associated with `[higher/lower]` log-odds of being in the group coded 1. The odds ratio was `[...]`, meaning that a one-unit increase in `[predictor]` multiplied the odds by `[...]`, holding the other predictors constant.

## Reporting Warning

Do not interpret logistic coefficients as direct changes in probability. Coefficients are changes in log-odds. Use odds ratios or predicted probabilities for clearer communication.

## Limitation Statement

The logistic model should be interpreted as a classification or association model unless the research design supports causal inference.
