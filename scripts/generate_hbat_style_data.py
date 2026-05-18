"""Generate a synthetic HBAT-style dataset for SmartPLS regression practice.

This is not the original HBAT dataset. It only mirrors the variable structure
used in the paper-based tutorial.
"""

from pathlib import Path

import numpy as np
import pandas as pd


def clip_0_10(values: np.ndarray) -> np.ndarray:
    return np.clip(values, 0, 10).round(2)


def main() -> None:
    rng = np.random.default_rng(4066)
    n = 100

    # Classification variables
    x1 = rng.choice([1, 2, 3], size=n, p=[0.25, 0.45, 0.30])
    x2 = rng.binomial(1, 0.46, n)
    x3 = rng.binomial(1, 0.52, n)
    x5 = rng.binomial(1, 0.55, n)

    # Latent service perception profile
    service = rng.normal(6.4, 1.5, n)
    digital = rng.normal(5.8, 1.7, n)
    sales = rng.normal(6.2, 1.4, n)
    price = rng.normal(5.7, 1.6, n)

    x6 = clip_0_10(service + rng.normal(0, 0.8, n))
    x7 = clip_0_10(digital + rng.normal(0, 0.9, n))
    x8 = clip_0_10(service + rng.normal(0, 0.9, n))
    x9 = clip_0_10(service + rng.normal(0, 0.8, n))
    x10 = clip_0_10(price + rng.normal(0, 1.0, n))
    x11 = clip_0_10(sales + rng.normal(0, 0.9, n))
    x12 = clip_0_10(0.45 * sales + 0.35 * service + rng.normal(1.8, 0.9, n))
    x13 = clip_0_10(price + rng.normal(0, 0.8, n))
    x14 = clip_0_10(service + rng.normal(0, 1.0, n))
    x15 = clip_0_10(0.55 * sales + 0.25 * digital + rng.normal(1.4, 1.0, n))
    x16 = clip_0_10(service + rng.normal(0, 0.8, n))
    x17 = clip_0_10(price + rng.normal(0, 1.0, n))
    x18 = clip_0_10(service + rng.normal(0, 0.9, n))

    # Linear regression outcome: satisfaction.
    x19 = clip_0_10(
        0.16 * x6
        - 0.11 * x7
        + 0.18 * x9
        + 0.14 * x11
        + 0.48 * x12
        + rng.normal(0.7, 0.85, n)
    )
    x20 = clip_0_10(0.65 * x19 + 0.18 * x12 + rng.normal(1.0, 1.0, n))
    x21 = clip_0_10(0.58 * x19 + 0.20 * x13 + rng.normal(1.2, 1.1, n))
    x22 = np.clip(8 + 7.5 * x19 + rng.normal(0, 8, n), 0, 100).round(1)
    x23 = rng.binomial(1, 1 / (1 + np.exp(-(x19 - 5.7))))

    # Logistic regression dependent variable region.
    logit_region = -2.5 - 0.70 * x7 - 0.30 * x10 + 0.95 * x12 + 0.15 * x3 + rng.normal(0, 0.9, n)
    p_region = 1 / (1 + np.exp(-logit_region))
    x4 = rng.binomial(1, p_region)

    data = pd.DataFrame(
        {
            "X1": x1,
            "X2": x2,
            "X3": x3,
            "X4": x4,
            "X5": x5,
            "X6": x6,
            "X7": x7,
            "X8": x8,
            "X9": x9,
            "X10": x10,
            "X11": x11,
            "X12": x12,
            "X13": x13,
            "X14": x14,
            "X15": x15,
            "X16": x16,
            "X17": x17,
            "X18": x18,
            "X19": x19,
            "X20": x20,
            "X21": x21,
            "X22": x22,
            "X23": x23,
        }
    )

    out = Path("datasets/hbat_smartpls_regression_case.csv")
    out.parent.mkdir(exist_ok=True)
    data.to_csv(out, index=False)
    print(out)


if __name__ == "__main__":
    main()
