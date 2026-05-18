# Module 9: PLS-SEM Structural Model

## Purpose

After the measurement model is acceptable, researchers assess the structural model: collinearity, path coefficients, explanatory power, effect sizes, and significance.

## Learning Objectives

After this module, learners should be able to:

- Assess collinearity using VIF.
- Interpret path coefficients.
- Assess R-square and adjusted R-square.
- Interpret f-square effect sizes.
- Use bootstrapping for path significance.

## Assessment Sequence

1. Check structural collinearity.
2. Assess path coefficients.
3. Assess coefficient significance using bootstrapping.
4. Assess R-square and adjusted R-square.
5. Assess f-square effect sizes.
6. Assess predictive performance when relevant.

## Collinearity

Check VIF for predictor constructs.

Common guideline:

```text
VIF < 3.3 or VIF < 5.0 depending on discipline and source
```

High VIF suggests overlapping predictors and unstable estimates.

## Path Coefficients

Path coefficients are standardized regression-like effects between constructs.

Interpret:

- Direction
- Magnitude
- Significance
- Theoretical meaning

## R-Square

R-square is the explained variance of an endogenous construct.

Always interpret R-square in context. A low R-square can still be meaningful in behavioral research, while a high R-square does not prove causality.

## f-Square

f-square assesses how much an exogenous construct contributes to an endogenous construct's R-square.

Common rough guideline:

```text
0.02 small
0.15 medium
0.35 large
```

## Structural Reporting Template

```text
The structural model was assessed after confirming measurement quality. Predictor collinearity was not problematic because all VIF values were below the selected threshold. Bootstrapping with ... subsamples showed that [path] was significant (beta = ..., t = ..., p = ...), supporting H1. The model explained ...% of the variance in [endogenous construct] (R2 = ...).
```

## Checklist

Use [structural-model-checklist.md](../checklists/structural-model-checklist.md).

## Next Module

Continue to [Module 10: Prediction and PLSpredict](10-prediction-plspredict.md).
