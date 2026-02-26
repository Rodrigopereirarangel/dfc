"""
monte_carlo.py — Simulação Monte Carlo (Fase 3.4, 7.1)
Input: distribuições dos drivers-chave (growth, margem, WACC, etc.)
Output: distribuição de fair values + percentis
Ref: Livro 90 (McLeish) Cap. 2, Livro 48 (Benninga)
"""
import numpy as np


def run_monte_carlo(base_fcff: np.ndarray, wacc: float, tv_growth: float,
                    growth_std: float = 0.02, margin_std: float = 0.01,
                    wacc_std: float = 0.005, n_simulations: int = 10000,
                    seed: int = 42) -> dict:
    """
    Run Monte Carlo on FCFF projections.
    Returns distribution of enterprise values.
    """
    rng = np.random.default_rng(seed)
    n_years = len(base_fcff)
    results = np.zeros(n_simulations)

    for sim in range(n_simulations):
        growth_shock = rng.normal(0, growth_std, n_years)
        margin_shock = rng.normal(0, margin_std, n_years)
        wacc_shock = rng.normal(0, wacc_std)

        sim_wacc = max(wacc + wacc_shock, 0.01)
        sim_fcff = base_fcff * (1 + growth_shock) * (1 + margin_shock)

        # PV of explicit period
        discount = np.array([(1 + sim_wacc) ** -(t + 1) for t in range(n_years)])
        pv_explicit = np.sum(sim_fcff * discount)

        # Terminal value
        sim_g = tv_growth + rng.normal(0, growth_std / 2)
        sim_g = min(sim_g, sim_wacc - 0.005)
        tv = sim_fcff[-1] * (1 + sim_g) / (sim_wacc - sim_g)
        pv_tv = tv / (1 + sim_wacc) ** n_years

        results[sim] = pv_explicit + pv_tv

    percentiles = np.percentile(results, [5, 10, 25, 50, 75, 90, 95])
    return {
        "mean": np.mean(results),
        "std": np.std(results),
        "percentiles": {f"p{p}": v for p, v in zip([5, 10, 25, 50, 75, 90, 95], percentiles)},
        "n_simulations": n_simulations,
    }


if __name__ == "__main__":
    base = np.array([100, 110, 120, 130, 140, 150, 160, 170, 180, 190], dtype=float)
    result = run_monte_carlo(base, wacc=0.12, tv_growth=0.04)
    print(f"Mean EV: R$ {result['mean']:,.0f}")
    for k, v in result['percentiles'].items():
        print(f"  {k}: R$ {v:,.0f}")
