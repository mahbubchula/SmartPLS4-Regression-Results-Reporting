# Module 8: PLS-SEM Measurement Model

## Purpose

When variables are latent constructs measured by indicators, results assessment starts with the measurement model. Do not interpret structural paths before measurement quality is acceptable.

## Learning Objectives

After this module, learners should be able to:

- Distinguish reflective and formative measurement.
- Assess indicator reliability.
- Assess internal consistency reliability.
- Assess convergent validity.
- Assess discriminant validity.

## Reflective Measurement Assessment

Typical assessment sequence:

1. Indicator loadings
2. Internal consistency reliability
3. Convergent validity
4. Discriminant validity

## Indicator Loadings

Common guideline:

```text
Outer loading >= 0.708
```

Lower loadings require judgment. Do not delete indicators mechanically. Consider theory, reliability, AVE, and content validity.

## Reliability

Report:

- Cronbach's alpha
- rho_A
- Composite reliability rho_C

Common guideline:

```text
0.70 to 0.95 is usually acceptable
```

Very high reliability may indicate redundant items.

## Convergent Validity

Use average variance extracted:

```text
AVE >= 0.50
```

This means the construct explains at least half of the variance of its indicators on average.

## Discriminant Validity

Use:

- HTMT
- Fornell-Larcker criterion
- Cross-loadings when needed

Common HTMT guideline:

```text
HTMT < 0.85
```

or:

```text
HTMT < 0.90 for conceptually similar constructs
```

Bootstrap confidence intervals can be used for HTMT assessment.

## Reporting Template

```text
The reflective measurement model was assessed using indicator loadings, internal consistency reliability, convergent validity, and discriminant validity. All retained indicators loaded above ..., composite reliability values ranged from ... to ..., and AVE values exceeded 0.50. HTMT values were below the selected threshold, supporting discriminant validity.
```

## Lab

Complete [Lab 5: Assess PLS-SEM measurement and structural results](../labs/lab05-plssem-assessment.md).

## Checklist

Use [measurement-model-checklist.md](../checklists/measurement-model-checklist.md).

## Next Module

Continue to [Module 9: PLS-SEM Structural Model](09-plssem-structural-model.md).
