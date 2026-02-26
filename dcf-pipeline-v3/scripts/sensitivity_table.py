"""
sensitivity_table.py — Gera tabela NTN-B × Driver 7×7 (Fase 6.3)
"""
import numpy as np
import pandas as pd


def generate_sensitivity(base_fcff: np.ndarray, base_wacc: float,
                         base_growth: float, ntnb_range: list[float] = None,
                         driver_range: list[float] = None,
                         shares_outstanding: float = 1.0) -> pd.DataFrame:
    """
    Generate 7×7 sensitivity table: NTN-B (risk-free) vs key driver.
    Returns DataFrame with Fair Value per share for each combination.
    """
    if ntnb_range is None:
        ntnb_range = [0.055, 0.060, 0.065, 0.070, 0.075, 0.080, 0.085]
    if driver_range is None:
        driver_range = [base_growth * (1 + d) for d in [-0.30, -0.20, -0.10, 0, 0.10, 0.20, 0.30]]

    n_years = len(base_fcff)
    results = np.zeros((len(driver_range), len(ntnb_range)))

    for i, g in enumerate(driver_range):
        for j, ntnb in enumerate(ntnb_range):
            wacc = base_wacc + (ntnb - 0.070)  # adjust WACC by Rf change
            wacc = max(wacc, 0.01)
            g_eff = min(g, wacc - 0.005)

            discount = np.array([(1 + wacc) ** -(t + 1) for t in range(n_years)])
            pv = np.sum(base_fcff * discount)
            tv = base_fcff[-1] * (1 + g_eff) / (wacc - g_eff)
            pv_tv = tv / (1 + wacc) ** n_years

            results[i, j] = (pv + pv_tv) / shares_outstanding

    return pd.DataFrame(
        results,
        index=[f"g={g:.1%}" for g in driver_range],
        columns=[f"NTN-B={n:.1%}" for n in ntnb_range]
    )


if __name__ == "__main__":
    base = np.array([100, 110, 120, 130, 140, 150, 160, 170, 180, 190], dtype=float)
    df = generate_sensitivity(base, base_wacc=0.12, base_growth=0.04, shares_outstanding=100)
    print(df.to_string())
