# Module 3: Building a Regression Model

## Purpose

This module teaches how to draw a regression model in SmartPLS 4 and specify the dependent variable, predictors, controls, and intercept.

## Learning Objectives

After this module, learners should be able to:

- Create a graphical regression model.
- Add a dependent variable and independent variables.
- Add controls.
- Include or remove the intercept intentionally.
- Save a clean model for reporting.

## Example Model

Research question:

```text
Which factors predict student satisfaction with a digital learning platform?
```

Dependent variable:

```text
SATISFACTION
```

Predictors:

```text
USEFULNESS
EASE_OF_USE
TRUST
SERVICE_QUALITY
```

Controls:

```text
AGE
EXPERIENCE
GENDER_MALE
```

## SmartPLS Steps

1. Create a new project.
2. Import the dataset.
3. Create a new model.
4. Add the dependent variable.
5. Add independent variables.
6. Draw arrows from predictors to the dependent variable.
7. Keep the intercept unless your research design requires removing it.
8. Save the model with a clear name.

## Intercept Rule

For most regression models, keep the intercept. Removing it changes the meaning of coefficients and is rarely appropriate unless theory and design justify a zero-intercept model.

## Model Documentation

Record:

- Model name
- Dataset name
- Dependent variable
- Predictors
- Controls
- Whether intercept is included
- SmartPLS version

## Practice

Create two models:

1. Simple model: `SATISFACTION <- USEFULNESS`
2. Multiple model: `SATISFACTION <- USEFULNESS + EASE_OF_USE + TRUST + SERVICE_QUALITY + AGE + EXPERIENCE`

## Lab

Complete [Lab 2: Build and run a SmartPLS regression model](../labs/lab02-linear-regression.md).

## Next Module

Continue to [Module 4: Running Linear Regression](04-running-linear-regression.md).
