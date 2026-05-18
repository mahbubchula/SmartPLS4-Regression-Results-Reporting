"""Benchmark the synthetic HBAT-style case outside SmartPLS.

Run from repository root:
    python scripts/benchmark_hbat_case.py
"""

from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf


def main() -> None:
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)
    data = pd.read_csv("datasets/hbat_smartpls_regression_case.csv")

    linear = smf.ols("X19 ~ X6 + X7 + X9 + X11 + X12", data=data).fit()
    logistic = smf.logit("X4 ~ X6 + X7 + X8 + X9 + X10 + X11 + X12 + X13 + X14 + X15 + X16 + X17 + X18", data=data).fit(disp=False)

    print("Multiple linear regression benchmark")
    print(linear.summary())
    print("\nLogistic regression benchmark")
    print(logistic.summary())

    linear_table = pd.DataFrame(
        {
            "term": linear.params.index,
            "b": linear.params.values,
            "se": linear.bse.values,
            "t": linear.tvalues.values,
            "p": linear.pvalues.values,
        }
    )
    linear_table.to_csv(output_dir / "hbat_linear_benchmark.csv", index=False)

    logistic_table = pd.DataFrame(
        {
            "term": logistic.params.index,
            "b": logistic.params.values,
            "se": logistic.bse.values,
            "z": logistic.tvalues.values,
            "p": logistic.pvalues.values,
            "odds_ratio": np.exp(logistic.params.values),
        }
    )
    logistic_table.to_csv(output_dir / "hbat_logistic_benchmark.csv", index=False)


if __name__ == "__main__":
    main()
