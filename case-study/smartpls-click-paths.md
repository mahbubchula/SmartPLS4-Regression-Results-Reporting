# SmartPLS Click Path Guide

This guide translates the shared paper into practical SmartPLS 4 menu steps.

## A. Import the HBAT-Style Dataset

1. Open SmartPLS 4.
2. Create a new project.
3. Import `datasets/hbat_smartpls_regression_case.csv`.
4. Confirm that `X1` to `X23` are visible.
5. Save the project.

## B. Build the Multiple Linear Regression Model

1. Create a new model.
2. Add `X19` as the dependent variable.
3. Add `X6`, `X7`, `X9`, `X11`, and `X12` as independent variables.
4. Draw arrows from each independent variable to `X19`.
5. Keep the intercept in the model unless your instructor asks for a no-intercept model.
6. Save the model as `HBAT Linear Regression`.

## C. Run Multiple Linear Regression

1. Select `Calculate`.
2. Choose `Regression`.
3. Use a two-tailed test unless you pre-specified directional hypotheses.
4. Use a 0.05 significance level.
5. Start with normal standard errors.
6. If diagnostics suggest heteroscedasticity or leverage concerns, compare HC3 or HC4 robust standard errors.
7. Tick `Open report`.
8. Start calculation.

## D. Export Linear Regression Results

Export:

- ANOVA or model summary
- R-square and adjusted R-square
- Coefficients
- Standardized coefficients
- VIF values
- Condition index
- Predicted vs residual plot
- Predicted vs actual plot
- Breusch-Pagan test
- Durbin-Watson test
- QQ plot
- Residual histogram

## E. Build the Logistic Regression Model

1. Create a new model.
2. Add `X4` as the binary dependent variable.
3. Add `X6` to `X18` as independent variables.
4. Draw arrows from all independent variables to `X4`.
5. Save the model as `HBAT Logistic Regression`.

## F. Run Logistic Regression

1. Select `Calculate`.
2. Choose `Logistic Regression`.
3. Use default maximum iteration and stop criterion settings unless convergence fails.
4. Use a two-tailed test and 0.05 significance level unless the study design justifies another choice.
5. Tick `Open report`.
6. Start calculation.

## G. Export Logistic Regression Results

Export:

- Fit summary
- Log-likelihood
- Deviance
- AIC
- BIC
- McFadden's R-square
- Cox and Snell's R-square
- Nagelkerke's R-square
- Confusion matrix
- Coefficients
- Wald test
- Odds ratios or exponential coefficients if available

## H. Reporting Rule

Do not paste SmartPLS output alone. Convert every exported table into:

- What was assessed
- What criterion was used
- What result was obtained
- What it means for the research question
