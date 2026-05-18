# Module 2: Data Preparation

## Purpose

SmartPLS results are only as good as the dataset. This module teaches the data preparation steps needed before importing into SmartPLS 4.

## Learning Objectives

After this module, learners should be able to:

- Prepare a SmartPLS-ready CSV file.
- Create a codebook for variables and indicators.
- Identify missing values and incorrect coding.
- Decide whether variables are metric, binary, or indicators of constructs.

## SmartPLS Data Checklist

Before importing:

- First row contains variable names.
- Variable names are short and clear.
- No duplicate column names.
- Numeric variables use consistent decimal notation.
- Missing values are coded consistently.
- Binary variables are coded as 0/1.
- Reverse-coded items are corrected before analysis.
- Each row represents one respondent or case.

## Variable Naming

Use names like:

```text
PU1, PU2, PU3
TR1, TR2, TR3
SQ1, SQ2, SQ3
SAT
AGE
EXP
```

Avoid names with spaces, symbols, or very long descriptions.

## Codebook

A codebook should include:

- Variable name
- Full label
- Construct
- Measurement scale
- Coding direction
- Missing-value treatment

Use [codebook-template.md](../templates/codebook-template.md).

## Missing Data

Document:

- Number of missing values per variable.
- Whether missingness is random or systematic.
- Whether you used deletion or imputation.
- Whether SmartPLS case-wise deletion changes the sample size.

## Reverse Coding

Reverse-coded survey items should be corrected before import.

For a 1 to 5 scale:

```text
reversed = 6 - original
```

## Practice

1. Open `datasets/smartpls_regression_training_data.csv`.
2. Identify the dependent variable for observed-variable regression.
3. Identify the predictor variables.
4. Identify the indicator variables for PLS-SEM.
5. Complete one row of the codebook template.

## Lab

Complete [Lab 1: Import dataset and create project](../labs/lab01-import-data-project.md).

## Next Module

Continue to [Module 3: Building a Regression Model](03-building-regression-model.md).
