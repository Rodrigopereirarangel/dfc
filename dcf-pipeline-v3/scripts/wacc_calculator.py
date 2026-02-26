"""
wacc_calculator.py — WACC dinâmico com term structure (Fase 4)
Ref: P22 (Cost of Capital), Livro 87 (McKinsey Cap. 8), Livro 01 (Penman)
"""


def cost_of_equity(rf: float, beta: float, erp: float,
                   size_premium: float = 0, crp: float = 0) -> float:
    """Ke = Rf + β × ERP + Size + CRP"""
    return rf + beta * erp + size_premium + crp


def unlever_beta(levered_beta: float, tax_rate: float, de_ratio: float) -> float:
    """β_unlevered = β_levered / (1 + (1-t) × D/E)"""
    return levered_beta / (1 + (1 - tax_rate) * de_ratio)


def relever_beta(unlevered_beta: float, tax_rate: float, target_de: float) -> float:
    """β_levered = β_unlevered × (1 + (1-t) × D/E)"""
    return unlevered_beta * (1 + (1 - tax_rate) * target_de)


def wacc(ke: float, kd: float, tax_rate: float,
         equity_weight: float, debt_weight: float) -> float:
    """WACC = Ke × (E/(D+E)) + Kd×(1-t) × (D/(D+E))"""
    return ke * equity_weight + kd * (1 - tax_rate) * debt_weight


def wacc_term_structure(base_wacc: float, de_ratios_by_year: list[float],
                        unlev_beta: float, rf: float, erp: float,
                        kd: float, tax_rate: float) -> list[dict]:
    """Generate WACC for each projection year based on changing D/E."""
    results = []
    for i, de in enumerate(de_ratios_by_year):
        beta_lev = relever_beta(unlev_beta, tax_rate, de)
        ke = cost_of_equity(rf, beta_lev, erp)
        we = 1 / (1 + de)
        wd = de / (1 + de)
        w = wacc(ke, kd, tax_rate, we, wd)
        results.append({"year": i + 1, "D/E": de, "beta": beta_lev, "Ke": ke, "WACC": w})
    return results


def penman_test(g_projected: float, inflation: float) -> dict:
    """Regra Penman: se g > inflação + 1%, alertar."""
    threshold = inflation + 0.01
    triggered = g_projected > threshold
    return {
        "g": g_projected,
        "threshold": threshold,
        "triggered": triggered,
        "msg": "⚠️ Growth alto — o WACC deveria ser maior?" if triggered else "✅ OK"
    }
