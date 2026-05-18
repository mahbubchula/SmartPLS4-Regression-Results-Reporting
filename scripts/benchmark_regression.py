"""Optional benchmark for SmartPLS regression output.

Run from repository root:
    python scripts/benchmark_regression.py
"""

from pathlib import Path

import pandas as pd
import statsmodels.formula.api as smf


def main() -> None:
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    data = pd.read_csv("datasets/smartpls_regression_training_data.csv")
    formula = (
        "SATISFACTION ~ USEFULNESS + EASE_OF_USE + TRUST + "
        "SERVICE_QUALITY + AGE + EXPERIENCE + GENDER_MALE"
    )
    model = smf.ols(formula, data=data).fit()
    robust = model.get_robustcov_results(cov_type="HC3")

    print(model.summary())
    print("\nHC3 robust standard errors:")
    print(robust.summary())

    table = pd.DataFrame(
        {
            "predictor": model.params.index,
            "b": model.params.values,
            "se_normal": model.bse.values,
            "p_normal": model.pvalues.values,
            "se_hc3": robust.bse,
            "p_hc3": robust.pvalues,
        }
    )
    table.to_csv(output_dir / "benchmark_regression_results.csv", index=False)


if __name__ == "__main__":
    main()
