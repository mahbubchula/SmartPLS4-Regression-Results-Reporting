# Regression in SmartPLS 4.0: Practical Analysis, Results Assessment, and Reporting

Complete practical course for learning how to run, assess, interpret, and report regression-based analysis in SmartPLS 4.

Created by Mahbub Hassan for students, thesis researchers, and applied quantitative researchers who need a step-by-step SmartPLS workflow from data preparation to final reporting.

## Course Scope

This course covers two practical SmartPLS 4 workflows:

1. **Observed-variable regression in SmartPLS 4**  
   Single and multiple linear regression using measured variables, including coefficients, standardized coefficients, significance testing, robust standard errors, diagnostics, and reporting.

2. **PLS-SEM structural path assessment**  
   Regression-like path modeling with latent constructs, including measurement model assessment, structural model assessment, bootstrapping, R-square, effect size, predictive relevance, PLSpredict, and reporting.

The course is intentionally practical. Learners follow SmartPLS menu steps, export results, fill assessment sheets, and write results in a publishable format.

## Paper-Based Case Study Track

This course now includes a dedicated paper-based track built around the shared 2026 SmartPLS software tutorial:

- [Paper-based learning track](paper-guide/README.md)
- [Simple explanation of the paper](paper-guide/paper-explainer.md)
- [Six-stage regression workflow](paper-guide/six-stage-regression-workflow.md)
- [HBAT-style variable map](case-study/hbat-variable-map.md)
- [SmartPLS click paths for linear and logistic regression](case-study/smartpls-click-paths.md)
- [Results assessment workbook](case-study/results-assessment-workbook.md)

Use this track if your main goal is to learn SmartPLS 4 regression exactly in the style of the published tutorial paper.

## Learning Outcomes

By the end of the course, learners should be able to:

- Prepare a clean dataset for SmartPLS 4.
- Build a regression model in the SmartPLS graphical interface.
- Run SmartPLS linear regression and regression bootstrapping.
- Interpret unstandardized and standardized coefficients.
- Assess p-values, t-values, standard errors, and confidence intervals.
- Use HC3/HC4 robust standard errors when appropriate.
- Inspect QQ plots and regression diagnostic output.
- Assess PLS-SEM measurement models using loadings, reliability, AVE, Fornell-Larcker, and HTMT.
- Assess structural models using VIF, path coefficients, R-square, f-square, bootstrapping, and predictive assessment.
- Write professional result sections for thesis, journal paper, or report submission.

## Course Structure

| Week | Module | Main Outcome |
|---|---|---|
| 1 | [SmartPLS Regression Workflow](modules/01-smartpls-regression-workflow.md) | Understand regression options in SmartPLS 4 |
| 2 | [Data Preparation](modules/02-data-preparation.md) | Prepare CSV/XLSX data and codebook |
| 3 | [Building a Regression Model](modules/03-building-regression-model.md) | Draw dependent, independent, and control variables |
| 4 | [Running Linear Regression](modules/04-running-linear-regression.md) | Estimate single and multiple regression |
| 5 | [Assessing Regression Results](modules/05-assessing-regression-results.md) | Interpret coefficients, R-square, and diagnostics |
| 6 | [Regression Bootstrapping](modules/06-regression-bootstrapping.md) | Test coefficient significance using bootstrapping |
| 7 | [Reporting Regression Results](modules/07-reporting-regression-results.md) | Write tables and result paragraphs |
| 8 | [PLS-SEM Measurement Model](modules/08-plssem-measurement-model.md) | Assess reliability and validity |
| 9 | [PLS-SEM Structural Model](modules/09-plssem-structural-model.md) | Assess paths, VIF, R-square, f-square, and significance |
| 10 | [Prediction and PLSpredict](modules/10-prediction-plspredict.md) | Assess predictive performance |
| 11 | [Common Reviewer Problems](modules/11-common-reviewer-problems.md) | Fix reporting and interpretation weaknesses |
| 12 | [Capstone SmartPLS Report](modules/12-capstone-smartpls-report.md) | Complete a full SmartPLS analysis report |

Optional paper-based extension:

| Module | Topic | Main Outcome |
|---|---|---|
| 13 | [Logistic Regression in SmartPLS 4](modules/13-logistic-regression-smartpls.md) | Run and report binary-outcome regression |

## Practical Labs

| Lab | Topic | File |
|---|---|---|
| 1 | Import dataset and create project | [Lab 1](labs/lab01-import-data-project.md) |
| 2 | Build and run a SmartPLS regression model | [Lab 2](labs/lab02-linear-regression.md) |
| 3 | Assess regression output | [Lab 3](labs/lab03-results-assessment.md) |
| 4 | Run regression bootstrapping | [Lab 4](labs/lab04-regression-bootstrapping.md) |
| 5 | Assess PLS-SEM measurement and structural results | [Lab 5](labs/lab05-plssem-assessment.md) |
| 6 | Write the final results section | [Lab 6](labs/lab06-reporting-results.md) |

## Included Materials

- SmartPLS-ready synthetic dataset
- HBAT-style synthetic dataset based on the paper's variable structure
- Codebook
- Step-by-step labs
- Result assessment checklists
- Regression reporting templates
- Logistic regression reporting template
- PLS-SEM reporting templates
- Export-result tracking sheets
- Python benchmark script for checking regression estimates outside SmartPLS
- GitHub Pages course homepage

## Quick Start

1. Download or clone this repository.
2. Open SmartPLS 4.
3. Import `datasets/smartpls_regression_training_data.csv`.
4. Start with [Lab 1](labs/lab01-import-data-project.md).
5. Use the templates in `templates/` while reporting your results.

For the paper-based track, import:

```text
datasets/hbat_smartpls_regression_case.csv
```

Then follow:

- [SmartPLS Click Path Guide](case-study/smartpls-click-paths.md)
- [Optional Module 13: Logistic Regression in SmartPLS 4](modules/13-logistic-regression-smartpls.md)

Optional Python benchmark:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python scripts/benchmark_regression.py
python scripts/benchmark_hbat_case.py
```

## Important Note

SmartPLS is proprietary software. This repository provides teaching materials, datasets, templates, and workflow guidance. It does not include SmartPLS software or a license.

## Official SmartPLS References Used

- [SmartPLS Regression documentation](https://www.smartpls.com/documentation/algorithms-and-techniques/regression/)
- [SmartPLS Regression Bootstrapping documentation](https://www.smartpls.com/documentation/algorithms-and-techniques/regression-bootstrapping/)
- [SmartPLS PLS-SEM Algorithm documentation](https://smartpls.com/documentation/algorithms-and-techniques/pls/)
- [SmartPLS PLSpredict documentation](https://www.smartpls.com/documentation/algorithms-and-techniques/predict/)
- [SmartPLS Algorithms and Techniques](https://www.smartpls.com/documentation/algorithms-and-techniques/)

## Citation

When reporting analyses conducted with SmartPLS, cite SmartPLS as recommended by the software provider:

Ringle, C. M., Wende, S., & Becker, J.-M. (2024). SmartPLS 4. SmartPLS. https://www.smartpls.com

## License

Course text and teaching materials are intended for open teaching and learning with attribution. Code examples are released under the MIT License.
