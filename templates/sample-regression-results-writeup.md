# Sample Regression Results Write-Up

This sample uses the synthetic training dataset and the optional Python benchmark. Use it as a writing model, not as real empirical evidence.

## Model Description

A multiple linear regression model was estimated to examine predictors of satisfaction with a digital learning platform. Satisfaction was regressed on usefulness, ease of use, trust, service quality, age, experience, and gender. The same model can be built and estimated in SmartPLS 4 using the regression algorithm.

## Example Results Paragraph

The model explained 53.9% of the variance in satisfaction (`R2 = 0.539`, adjusted `R2 = 0.518`). Usefulness was positively associated with satisfaction (`b = 0.324`, `p < 0.001`), indicating that higher perceived usefulness was linked with higher satisfaction, holding the other predictors constant. Ease of use (`b = 0.315`, `p < 0.001`), trust (`b = 0.269`, `p < 0.001`), and service quality (`b = 0.376`, `p < 0.001`) were also positive and statistically significant predictors. Age showed a negative association with satisfaction (`b = -0.417`, `p = 0.007`), while experience was positively associated with satisfaction (`b = 1.798`, `p = 0.018`). Gender was not statistically significant (`p = 0.143`).

## Example Diagnostic Statement

The QQ plot and residual diagnostics should be inspected before final reporting. If heteroscedasticity or influential observations are suspected, HC3 or HC4 robust standard errors should be considered and reported. In the benchmark model, HC3 robust standard errors did not materially change the substantive interpretation of the main predictors.

## Example Reporting Caveat

Because the example dataset is cross-sectional and synthetic, results should be interpreted as associations, not causal effects. In a real thesis or journal paper, causal language would require a stronger research design and explicit assumptions.
