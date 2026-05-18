"""Generate synthetic SmartPLS training data.

The dataset is synthetic and intended only for teaching.
"""

from pathlib import Path

import numpy as np
import pandas as pd


def likert_from_latent(values: np.ndarray, noise: float, rng: np.random.Generator) -> np.ndarray:
    noisy = values + rng.normal(0, noise, len(values))
    cut = np.quantile(noisy, [0.12, 0.32, 0.58, 0.82])
    return np.digitize(noisy, cut) + 1


def scale_0_100(values: np.ndarray) -> np.ndarray:
    low, high = np.percentile(values, [2, 98])
    scaled = (values - low) / (high - low) * 100
    return np.clip(scaled, 1, 100).round(2)


def main() -> None:
    rng = np.random.default_rng(2026)
    n = 160

    age = rng.integers(19, 52, size=n)
    experience = np.clip(rng.normal(3.2, 1.8, size=n), 0, 10).round(1)
    gender_male = rng.binomial(1, 0.48, size=n)

    peou_latent = rng.normal(0, 1, n)
    trust_latent = rng.normal(0, 1, n)
    sq_latent = rng.normal(0, 1, n)
    pu_latent = 0.48 * peou_latent + 0.24 * sq_latent + rng.normal(0, 0.75, n)
    sat_latent = (
        0.42 * pu_latent
        + 0.22 * peou_latent
        + 0.28 * trust_latent
        + 0.31 * sq_latent
        + 0.08 * experience
        - 0.01 * (age - age.mean())
        + rng.normal(0, 0.8, n)
    )

    data = pd.DataFrame(
        {
            "ID": np.arange(1, n + 1),
            "AGE": age,
            "EXPERIENCE": experience,
            "GENDER_MALE": gender_male,
            "PU1": likert_from_latent(pu_latent, 0.55, rng),
            "PU2": likert_from_latent(pu_latent, 0.50, rng),
            "PU3": likert_from_latent(pu_latent, 0.60, rng),
            "PEOU1": likert_from_latent(peou_latent, 0.55, rng),
            "PEOU2": likert_from_latent(peou_latent, 0.55, rng),
            "PEOU3": likert_from_latent(peou_latent, 0.60, rng),
            "TR1": likert_from_latent(trust_latent, 0.50, rng),
            "TR2": likert_from_latent(trust_latent, 0.55, rng),
            "TR3": likert_from_latent(trust_latent, 0.60, rng),
            "SQ1": likert_from_latent(sq_latent, 0.50, rng),
            "SQ2": likert_from_latent(sq_latent, 0.55, rng),
            "SQ3": likert_from_latent(sq_latent, 0.60, rng),
            "SAT1": likert_from_latent(sat_latent, 0.55, rng),
            "SAT2": likert_from_latent(sat_latent, 0.55, rng),
            "SAT3": likert_from_latent(sat_latent, 0.60, rng),
        }
    )

    data["USEFULNESS"] = data[["PU1", "PU2", "PU3"]].mean(axis=1).mul(20).round(2)
    data["EASE_OF_USE"] = data[["PEOU1", "PEOU2", "PEOU3"]].mean(axis=1).mul(20).round(2)
    data["TRUST"] = data[["TR1", "TR2", "TR3"]].mean(axis=1).mul(20).round(2)
    data["SERVICE_QUALITY"] = data[["SQ1", "SQ2", "SQ3"]].mean(axis=1).mul(20).round(2)
    data["SATISFACTION"] = scale_0_100(sat_latent)

    ordered = [
        "ID",
        "SATISFACTION",
        "USEFULNESS",
        "EASE_OF_USE",
        "TRUST",
        "SERVICE_QUALITY",
        "AGE",
        "EXPERIENCE",
        "GENDER_MALE",
        "PU1",
        "PU2",
        "PU3",
        "PEOU1",
        "PEOU2",
        "PEOU3",
        "TR1",
        "TR2",
        "TR3",
        "SQ1",
        "SQ2",
        "SQ3",
        "SAT1",
        "SAT2",
        "SAT3",
    ]
    data = data[ordered]

    out = Path("datasets/smartpls_regression_training_data.csv")
    out.parent.mkdir(exist_ok=True)
    data.to_csv(out, index=False)
    print(out)


if __name__ == "__main__":
    main()
