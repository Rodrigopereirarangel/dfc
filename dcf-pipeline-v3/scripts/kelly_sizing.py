"""
kelly_sizing.py — Kelly Criterion calculator (Fase 8.2)
Ref: Livro 03 (Bernstein), Livro 18 (Paleologo)
"""


def kelly_full(p: float, b: float) -> float:
    """Full Kelly: f* = (p*b - q) / b where q = 1-p"""
    q = 1 - p
    return (p * b - q) / b if b != 0 else 0


def kelly_fraction(p: float, b: float, fraction: float = 0.5) -> dict:
    """
    Fractional Kelly for practical use.
    fraction=0.5 → Half-Kelly, 0.25 → Quarter-Kelly
    """
    full = kelly_full(p, b)
    sized = max(full * fraction, 0)
    return {
        "full_kelly": round(full, 4),
        "fraction": fraction,
        "position_pct": round(sized, 4),
        "label": f"{'Half' if fraction == 0.5 else 'Quarter'}-Kelly" if fraction in [0.5, 0.25] else f"{fraction:.0%}-Kelly"
    }


def conviction_score(upside_ratio: float, moat_score: float, mgmt_score: float,
                     projection_confidence: float, triangulation: float,
                     qmj_score: float) -> dict:
    """
    Composite conviction score (0-10).
    Weights: Upside 25%, Moat 20%, Mgmt 20%, Projection 15%, Triangulation 10%, QMJ 10%
    """
    score = (upside_ratio * 0.25
             + moat_score * 0.20
             + mgmt_score * 0.20
             + projection_confidence * 0.15
             + triangulation * 0.10
             + qmj_score * 0.10)
    score = min(max(score, 0), 10)
    if score >= 7:
        rec = "Posição relevante"
    elif score >= 5:
        rec = "Posição menor"
    else:
        rec = "Não investir"
    return {"conviction_score": round(score, 2), "recommendation": rec}
