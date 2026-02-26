"""
fade_rate.py — Estima fade rate ROIC por setor (Fase 2.1)
Ref: P19 (ROIC and Investment Process) — persistência por setor
"""
import math


SECTOR_HALF_LIVES = {
    "Technology": 6,
    "Healthcare": 8,
    "Consumer Staples": 10,
    "Consumer Discretionary": 5,
    "Industrials": 7,
    "Financials": 8,
    "Energy": 4,
    "Utilities": 12,
    "Materials": 5,
    "Real Estate": 9,
    "Telecom": 6,
}


def estimate_fade_rate(sector: str) -> dict:
    """Fade rate = ln(2) / half-life."""
    hl = SECTOR_HALF_LIVES.get(sector, 7)
    rate = math.log(2) / hl
    return {"sector": sector, "half_life_years": hl, "fade_rate": round(rate, 4)}


def project_roic_fade(initial_roic: float, wacc: float, fade_rate_val: float,
                       years: int = 15) -> list[float]:
    """Project ROIC path converging to WACC via exponential decay."""
    spread = initial_roic - wacc
    return [wacc + spread * math.exp(-fade_rate_val * t) for t in range(years)]
