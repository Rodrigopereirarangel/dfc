"""
roic_decomposition.py — ROIC tree + ROE decomposition (Fases 1.2, 2.1)
Ref: P24 (ROIC), Livro 86 (Lundholm/Sloan Pg. 110)
"""


def roic(nopat: float, invested_capital: float) -> float:
    """ROIC = NOPAT / Invested Capital"""
    return nopat / invested_capital if invested_capital != 0 else 0


def roic_decomposition(nopat: float, revenue: float, invested_capital: float) -> dict:
    """ROIC = NOPAT Margin × Capital Turnover"""
    margin = nopat / revenue if revenue != 0 else 0
    turnover = revenue / invested_capital if invested_capital != 0 else 0
    return {"roic": margin * turnover, "nopat_margin": margin, "capital_turnover": turnover}


def roiic(delta_nopat: float, delta_ic: float) -> float:
    """Return on Incremental Invested Capital"""
    return delta_nopat / delta_ic if delta_ic != 0 else 0


def roe_decomposition(roic_val: float, kd_after_tax: float, de_ratio: float) -> dict:
    """ROE = ROIC + (ROIC − Kd_after_tax) × D/E"""
    spread = roic_val - kd_after_tax
    leverage_effect = spread * de_ratio
    roe = roic_val + leverage_effect
    return {"roe": roe, "roic": roic_val, "spread": spread, "leverage_effect": leverage_effect,
            "verdict": "Alavancagem CRIA valor" if spread > 0 else "Alavancagem DESTRÓI valor"}


def fade_rate(half_life_years: float) -> float:
    """Fade rate = ln(2) / half-life (P19)"""
    import math
    return math.log(2) / half_life_years if half_life_years > 0 else 0
