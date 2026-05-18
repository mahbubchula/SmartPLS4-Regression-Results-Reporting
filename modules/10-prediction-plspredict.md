# Module 10: Prediction and PLSpredict

## Purpose

SmartPLS models are often used for prediction. This module introduces how to assess predictive performance, especially with PLSpredict for PLS-SEM.

## Learning Objectives

After this module, learners should be able to:

- Explain why prediction assessment is different from significance testing.
- Interpret Q2_predict.
- Compare RMSE and MAE values.
- Report predictive performance responsibly.

## Prediction vs Explanation

Significant paths do not automatically mean strong prediction. Predictive assessment asks whether the model predicts new or holdout cases well.

## PLSpredict

PLSpredict uses cross-validation to generate prediction errors for indicators and constructs. SmartPLS documentation describes RMSE, MAE, and MAPE for manifest variables and RMSE/MAE for latent variables.

## Q2 Predict

If:

```text
Q2_predict > 0
```

then the model's prediction error is smaller than using a simple mean benchmark.

## LM Benchmark

SmartPLS can compare PLS-SEM prediction errors with a linear regression model benchmark for manifest variables. Lower RMSE or MAE indicates better predictive performance.

## Reporting Template

```text
Predictive performance was assessed using PLSpredict. The Q2_predict values were positive for ..., indicating that the model outperformed the mean benchmark. The PLS-SEM model produced lower RMSE/MAE than the linear model benchmark for ... indicators, suggesting [low/medium/high] predictive performance.
```

## Practice

1. Run PLSpredict if your model uses PLS-SEM.
2. Export Q2_predict results.
3. Compare RMSE and MAE with the LM benchmark.
4. Write one prediction assessment paragraph.

## Next Module

Continue to [Module 11: Common Reviewer Problems](11-common-reviewer-problems.md).
