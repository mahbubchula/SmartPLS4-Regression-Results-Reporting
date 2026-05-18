# Lab 5: PLS-SEM Measurement and Structural Assessment

## Goal

Practice PLS-SEM assessment using the same dataset's indicator variables.

## Construct Setup

Reflective constructs:

| Construct | Indicators |
|---|---|
| PU | PU1, PU2, PU3 |
| PEOU | PEOU1, PEOU2, PEOU3 |
| TRUST | TR1, TR2, TR3 |
| SERVICE_QUALITY | SQ1, SQ2, SQ3 |
| SATISFACTION | SAT1, SAT2, SAT3 |

Structural paths:

```text
PU -> SATISFACTION
PEOU -> SATISFACTION
TRUST -> SATISFACTION
SERVICE_QUALITY -> SATISFACTION
```

Optional path:

```text
PEOU -> PU
```

## Measurement Model Assessment

Export and assess:

- Outer loadings
- Cronbach's alpha
- rho_A
- Composite reliability rho_C
- AVE
- HTMT
- Fornell-Larcker criterion

## Structural Model Assessment

Export and assess:

- VIF
- Path coefficients
- t-values and p-values from bootstrapping
- R-square
- Adjusted R-square
- f-square

## Deliverable

Submit:

- Measurement model table
- Structural model table
- One paragraph explaining whether hypotheses are supported

## Next Lab

Continue to [Lab 6](lab06-reporting-results.md).
