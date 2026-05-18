# Six-Stage Regression Workflow

The shared paper follows the regression workflow from Hair et al. This course turns that workflow into a practical SmartPLS checklist.

## Stage 1: Select the Objective

Decide whether the analysis is for:

- Explanation
- Prediction
- Both explanation and prediction

Output:

```text
Research objective statement
```

Example:

```text
The objective is to explain customer satisfaction using customer perceptions of product quality, e-commerce, complaint resolution, product line, and salesforce image.
```

## Stage 2: Design the Regression Analysis

Define:

- Dependent variable
- Independent variables
- Controls
- Sample size
- Measurement level
- Linear or logistic regression

Output:

```text
Model specification table
```

## Stage 3: Test Assumptions

For multiple linear regression, check:

- Linearity in parameters
- Random sampling
- No perfect multicollinearity
- Exogeneity
- Homoscedasticity
- Independence of residuals
- Approximate normality of residuals for inference

For logistic regression, check:

- Binary dependent variable
- Independent observations
- No perfect multicollinearity
- Linearity between predictors and log-odds
- Adequate sample size

Output:

```text
Assumption assessment table
```

## Stage 4: Estimate the Model and Assess Overall Fit

For multiple linear regression, assess:

- ANOVA or F-test
- R-square
- Adjusted R-square
- Durbin-Watson test if relevant
- Residual plots

For logistic regression, assess:

- Log-likelihood
- Deviance
- AIC
- BIC
- McFadden's R-square
- Cox and Snell's R-square
- Nagelkerke's R-square
- Confusion matrix

Output:

```text
Model fit assessment table
```

## Stage 5: Interpret the Regression Variate

For multiple linear regression, interpret:

- Unstandardized coefficients
- Standardized coefficients
- t-values
- p-values
- Confidence intervals
- Relative importance

For logistic regression, interpret:

- Logit coefficients
- Wald test
- p-values
- Odds ratios
- Direction of group membership probability

Output:

```text
Hypothesis decision table
```

## Stage 6: Validate the Results

Validation can include:

- Holdout sample
- Cross-validation
- Prediction accuracy
- Sensitivity checks
- Robust standard errors
- Alternative model specification

Output:

```text
Validation and limitation paragraph
```

## Final Course Deliverable

At the end of the workflow, students should produce:

- Model diagram
- Exported SmartPLS tables
- Assumption checklist
- Model fit table
- Coefficient table
- Written result section
- Limitations paragraph
