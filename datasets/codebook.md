# Dataset Codebook

Dataset:

```text
smartpls_regression_training_data.csv
```

The dataset is synthetic and intended only for teaching SmartPLS workflows.

## Observed Regression Variables

| Variable | Label | Type | Coding |
|---|---|---|---|
| ID | Case ID | Identifier | 1 to 160 |
| SATISFACTION | Overall satisfaction | Dependent variable | 1 to 100 |
| USEFULNESS | Perceived usefulness composite | Predictor | 20 to 100 |
| EASE_OF_USE | Perceived ease of use composite | Predictor | 20 to 100 |
| TRUST | Trust composite | Predictor | 20 to 100 |
| SERVICE_QUALITY | Service quality composite | Predictor | 20 to 100 |
| AGE | Respondent age | Control | Years |
| EXPERIENCE | Prior platform experience | Control | Years |
| GENDER_MALE | Gender dummy | Control | 1 = male, 0 = otherwise |

## PLS-SEM Indicator Variables

| Construct | Indicators | Scale |
|---|---|---|
| PU | PU1, PU2, PU3 | 1 to 5 Likert |
| PEOU | PEOU1, PEOU2, PEOU3 | 1 to 5 Likert |
| TRUST | TR1, TR2, TR3 | 1 to 5 Likert |
| SERVICE_QUALITY | SQ1, SQ2, SQ3 | 1 to 5 Likert |
| SATISFACTION | SAT1, SAT2, SAT3 | 1 to 5 Likert |

## Suggested Regression Model

```text
SATISFACTION <- USEFULNESS + EASE_OF_USE + TRUST + SERVICE_QUALITY + AGE + EXPERIENCE + GENDER_MALE
```

## Suggested PLS-SEM Structural Model

```text
PU -> SATISFACTION
PEOU -> SATISFACTION
TRUST -> SATISFACTION
SERVICE_QUALITY -> SATISFACTION
PEOU -> PU
```
