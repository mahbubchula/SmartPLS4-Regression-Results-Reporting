# Module 1: SmartPLS Regression Workflow

## Purpose

SmartPLS 4 supports several analysis routes. Before clicking calculate, researchers must decide whether their project needs observed-variable regression, logistic regression, path analysis, or PLS-SEM.

## Learning Objectives

After this module, learners should be able to:

- Explain the difference between linear regression and PLS-SEM in SmartPLS.
- Identify the dependent variable, independent variables, and controls.
- Decide whether the analysis goal is prediction, explanation, or theory testing.
- Select the correct SmartPLS workflow for the research question.

## Regression in SmartPLS

SmartPLS regression is used when the dependent variable is measured directly and is continuous. Examples:

- Satisfaction score predicted by usefulness, trust, and service quality.
- Commute time predicted by distance, income, age, and travel mode.
- Exam score predicted by study hours, attendance, and sleep.

SmartPLS can run single and multiple linear regression models and report coefficients in standardized and unstandardized form.

## PLS-SEM Structural Paths

PLS-SEM is used when variables are modeled as latent constructs measured by indicators. Examples:

- Perceived usefulness measured by several survey items.
- Trust measured by three or more indicators.
- Satisfaction measured as a construct with reflective items.

In PLS-SEM, structural paths are regression-like relationships among latent constructs, but results must be assessed in two stages:

1. Measurement model assessment
2. Structural model assessment

## Decision Guide

| Research Situation | SmartPLS Route |
|---|---|
| One continuous observed dependent variable | Linear regression |
| Binary dependent variable coded 0/1 | Logistic regression |
| Latent constructs measured by indicators | PLS-SEM |
| Mediation or moderation among observed variables | Path analysis or PROCESS-style model |
| Necessary but not sufficient conditions | Necessary condition analysis |

## Practical Workflow

1. Define the research question.
2. Identify the dependent variable.
3. Identify predictors and controls.
4. Prepare and import the data.
5. Draw the model in SmartPLS.
6. Run the algorithm.
7. Assess model results.
8. Run bootstrapping for final inference.
9. Export tables and figures.
10. Write results with criteria and interpretation.

## Practice

Write a one-paragraph plan:

- Research question
- Dependent variable
- Independent variables
- Control variables
- Analysis route in SmartPLS
- Why this route is appropriate

## Next Module

Continue to [Module 2: Data Preparation](02-data-preparation.md).
