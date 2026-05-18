# Logistic Regression Assessment Checklist

## Model Setup

- [ ] Dependent variable is binary.
- [ ] Binary coding is documented.
- [ ] Predictors are correctly scaled or coded.
- [ ] Sample size is sufficient for model complexity.
- [ ] Observations are independent.
- [ ] Intercept is included unless justified otherwise.

## Model Fit

- [ ] Log-likelihood reported.
- [ ] Deviance reported.
- [ ] AIC reported.
- [ ] BIC reported.
- [ ] McFadden's R-square reported.
- [ ] Cox and Snell's R-square reported.
- [ ] Nagelkerke's R-square reported.

## Predictive Accuracy

- [ ] Confusion matrix exported.
- [ ] Group 0 classification accuracy reported.
- [ ] Group 1 classification accuracy reported.
- [ ] Overall classification accuracy reported.
- [ ] Threshold/cutoff documented when applicable.

## Coefficients

- [ ] Logistic coefficients reported.
- [ ] Wald tests reported.
- [ ] p-values reported.
- [ ] Odds ratios reported or calculated.
- [ ] Coefficients are not interpreted as direct probability changes.

## Assumptions and Limitations

- [ ] No perfect multicollinearity checked.
- [ ] Linearity with log-odds considered.
- [ ] Influential observations considered.
- [ ] Small-sample limitations stated when applicable.
- [ ] Causal claims avoided unless design supports them.
