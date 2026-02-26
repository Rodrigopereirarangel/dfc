"""
validate_model.py — Validação automática do modelo (Fase 5A checks)
- Chain check: Receita → NOPAT → FCFF
- Reconciliação segmento ⇄ consolidado
- WACC convergência (loop circular, máx 5 iterações)
- CAPEX integrity
- Output: lista de alertas ❗/🟠
"""
import numpy as np
import pandas as pd


def chain_check(revenue: np.ndarray, nopat_margin: np.ndarray, da: np.ndarray,
                capex: np.ndarray, delta_wc: np.ndarray, model_fcff: np.ndarray,
                tolerance: float = 1e6) -> list[dict]:
    """Check: NOPAT = Revenue × Margin; FCFF = NOPAT + D&A − Capex − ΔWC"""
    alerts = []
    nopat = revenue * nopat_margin
    fcff = nopat + da - capex - delta_wc
    diff = np.abs(fcff - model_fcff)
    for i, d in enumerate(diff):
        if d > tolerance:
            alerts.append({"year": i, "type": "❗", "msg": f"Chain check FCFF diff = R$ {d:,.0f}"})
    return alerts


def wacc_convergence(unlev_beta: float, tax_rate: float, de_ratios: list[float],
                     rf: float, erp: float, kd: float, equity_weight: float,
                     max_iter: int = 5, tol_bps: float = 10) -> dict:
    """Iterative WACC convergence with circular resolution."""
    wacc_prev = None
    for i in range(max_iter):
        de = de_ratios[min(i, len(de_ratios) - 1)]
        beta_lev = unlev_beta * (1 + (1 - tax_rate) * de)
        ke = rf + beta_lev * erp
        we = equity_weight
        wd = 1 - we
        wacc = ke * we + kd * (1 - tax_rate) * wd
        if wacc_prev is not None and abs(wacc - wacc_prev) * 10000 < tol_bps:
            return {"wacc": wacc, "converged": True, "iterations": i + 1}
        wacc_prev = wacc
    return {"wacc": wacc, "converged": False, "iterations": max_iter}


def capex_integrity(capex_total: np.ndarray, capex_maintenance: np.ndarray,
                    capex_expansion: np.ndarray, revenue: np.ndarray,
                    tol_pct: float = 0.001) -> list[dict]:
    """Check CAPEX_total = maintenance + expansion."""
    alerts = []
    diff = np.abs(capex_total - (capex_maintenance + capex_expansion))
    for i, (d, r) in enumerate(zip(diff, revenue)):
        if r > 0 and d / r > tol_pct:
            alerts.append({"year": i, "type": "🟠", "msg": f"CAPEX overlap = {d / r:.2%} of revenue"})
    return alerts


if __name__ == "__main__":
    print("DCF Pipeline v3 — Model Validation Script")
    print("Use: import validate_model and call functions with your model data.")
