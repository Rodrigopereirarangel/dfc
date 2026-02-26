"""
beneish_score.py — Beneish M-Score (Fase 1.1)
Ref: Livro 07 (Schilit), threshold M > -1.78
"""


def beneish_m_score(dsri: float, gmi: float, aqi: float, sgi: float,
                    depi: float, sgai: float, lvgi: float, tata: float) -> dict:
    """
    Calculate Beneish M-Score.
    M = −4.84 + 0.92×DSRI + 0.528×GMI + 0.404×AQI + 0.892×SGI
        + 0.115×DEPI − 0.172×SGAI + 4.679×TATA − 0.327×LVGI
    """
    m = (-4.84
         + 0.920 * dsri
         + 0.528 * gmi
         + 0.404 * aqi
         + 0.892 * sgi
         + 0.115 * depi
         - 0.172 * sgai
         + 4.679 * tata
         - 0.327 * lvgi)

    alert = "❗ ALTA PROBABILIDADE DE MANIPULAÇÃO" if m > -1.78 else "✅ OK"
    return {"m_score": round(m, 4), "alert": alert, "threshold": -1.78}


def calculate_indicators(current: dict, prior: dict) -> dict:
    """Calculate input ratios from two periods of financial data."""
    dsri = (current["receivables"] / current["revenue"]) / (prior["receivables"] / prior["revenue"])
    gmi = prior["gross_margin"] / current["gross_margin"]
    aqi = 1 - ((current["ppe"] + current["current_assets"]) / current["total_assets"]) / \
              (1 - ((prior["ppe"] + prior["current_assets"]) / prior["total_assets"]))
    sgi = current["revenue"] / prior["revenue"]
    depi = prior["depreciation_rate"] / current["depreciation_rate"]
    sgai = (current["sga"] / current["revenue"]) / (prior["sga"] / prior["revenue"])
    lvgi = (current["total_debt"] / current["total_assets"]) / (prior["total_debt"] / prior["total_assets"])
    tata = (current["net_income"] - current["cfo"]) / current["total_assets"]
    return {"dsri": dsri, "gmi": gmi, "aqi": aqi, "sgi": sgi,
            "depi": depi, "sgai": sgai, "lvgi": lvgi, "tata": tata}
