# PLS-SEM Results Report Template

## Software and Estimation

The PLS-SEM analysis was conducted using SmartPLS 4. The PLS-SEM algorithm was used to estimate the model, and bootstrapping with `[number]` subsamples was used to assess significance.

## Measurement Model Assessment

The reflective measurement model was assessed using indicator loadings, internal consistency reliability, convergent validity, and discriminant validity.

### Reliability and Convergent Validity

| Construct | Loading Range | Cronbach's Alpha | rho_A | rho_C | AVE | Decision |
|---|---:|---:|---:|---:|---:|---|
| PU | | | | | | |
| PEOU | | | | | | |
| TRUST | | | | | | |
| SERVICE_QUALITY | | | | | | |
| SATISFACTION | | | | | | |

### Discriminant Validity

HTMT values were below `[0.85/0.90]`, supporting discriminant validity.

## Structural Model Assessment

Predictor collinearity was assessed using VIF. All VIF values were `[below/above]` the selected threshold of `[threshold]`.

| Hypothesis | Path | beta | t | p | 95% CI | Decision |
|---|---|---:|---:|---:|---|---|
| H1 | PU -> SATISFACTION | | | | | |
| H2 | PEOU -> SATISFACTION | | | | | |
| H3 | TRUST -> SATISFACTION | | | | | |
| H4 | SERVICE_QUALITY -> SATISFACTION | | | | | |

## Explanatory Power

The model explained `[R2]` of the variance in `[endogenous construct]`.

| Endogenous Construct | R2 | Adjusted R2 | Interpretation |
|---|---:|---:|---|
| SATISFACTION | | | |

## Prediction Assessment

PLSpredict was used/not used because `[reason]`. The Q2_predict values were `[positive/non-positive]`, and RMSE/MAE comparisons indicated `[interpretation]`.

## Conclusion

The structural results indicate that `[summary of supported hypotheses]`. The results should be interpreted in light of `[limitations]`.
