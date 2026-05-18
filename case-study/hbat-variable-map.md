# HBAT-Style Case Study Variable Map

This course includes a synthetic HBAT-style dataset for SmartPLS regression practice:

```text
datasets/hbat_smartpls_regression_case.csv
```

The variable structure follows the paper's teaching case, but the values are synthetic.

## Classification Variables

| Variable | Meaning | Coding |
|---|---|---|
| X1 | Customer type | 1 = short relationship, 2 = medium relationship, 3 = long relationship |
| X2 | Industry type | 0 = magazine industry, 1 = newsprint industry |
| X3 | Firm size | 0 = small firm, 1 = large firm |
| X4 | Region | 0 = USA/North America, 1 = outside North America |
| X5 | Distribution system | 0 = indirect, 1 = direct |

## Perception Variables

All perception variables use a 0 to 10 scale.

| Variable | Meaning |
|---|---|
| X6 | Product quality |
| X7 | E-commerce activities or website |
| X8 | Technical support |
| X9 | Complaint resolution |
| X10 | Advertising |
| X11 | Product line |
| X12 | Salesforce image |
| X13 | Competitive pricing |
| X14 | Warranty and claims |
| X15 | New products |
| X16 | Ordering and billing |
| X17 | Price flexibility |
| X18 | Delivery speed |

## Outcome Variables

| Variable | Meaning | Scale |
|---|---|---|
| X19 | Customer satisfaction | 0 to 10 |
| X20 | Likelihood of recommending HBAT | 0 to 10 |
| X21 | Likelihood of future purchase | 0 to 10 |
| X22 | Percentage of purchases from HBAT | 0 to 100 |
| X23 | Future relationship consideration | 0 = no, 1 = yes |

## Linear Regression Model for Practice

Use customer satisfaction as the dependent variable:

```text
X19 <- X6 + X7 + X9 + X11 + X12
```

This mirrors the paper's multiple linear regression teaching model.

## Logistic Regression Model for Practice

Use region as the binary dependent variable:

```text
X4 <- X6 + X7 + X8 + X9 + X10 + X11 + X12 + X13 + X14 + X15 + X16 + X17 + X18
```

This mirrors the paper's logistic regression teaching model.
