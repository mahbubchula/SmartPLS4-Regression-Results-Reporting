# Lab 2: Build and Run a SmartPLS Linear Regression Model

## Goal

Build a multiple regression model predicting satisfaction.

## Model

Dependent variable:

```text
SATISFACTION
```

Predictors:

```text
USEFULNESS
EASE_OF_USE
TRUST
SERVICE_QUALITY
```

Controls:

```text
AGE
EXPERIENCE
GENDER_MALE
```

## Steps

1. Create a new model.
2. Add `SATISFACTION` as the dependent variable.
3. Add each predictor and control variable.
4. Draw arrows from all predictors to `SATISFACTION`.
5. Keep the intercept in the model.
6. Open Calculate.
7. Select Regression.
8. Use two-tailed test and 0.05 significance level.
9. Run once with normal standard errors.
10. Run again with HC3 or HC4 standard errors if diagnostic concerns exist.
11. Open the report.
12. Export the results.

## Deliverable

Submit:

- Model screenshot
- Regression coefficients table
- R-square and adjusted R-square
- Short interpretation of each main predictor

## Next Lab

Continue to [Lab 3](lab03-results-assessment.md).
