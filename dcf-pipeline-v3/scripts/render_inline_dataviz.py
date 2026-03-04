#!/usr/bin/env python3
"""
render_inline_dataviz.py — DCF Pipeline v4.0
Renderiza todos os 14 dashboards interativos obrigatórios via Plotly (HTML).

Gráficos implementados por fase:
  F0  — Spider/Radar (5 Forças Porter + Moat)
  F1a — Waterfall (Lucro Reportado → Normalizado)
  F1b — ROE DuPont stacked bars + linha COE
  F2a — Linhas convergentes ROIC → WACC (fade)
  F2b — Tornado Chart horizontal (sensibilidade drivers)
  F25 — Capital Allocation Stacked 100% (10 anos)
  F3  — Barras FCFF vs Lucro Recorrente projetado
  F4  — Term Structure of Discount Rates (WACC escalonado)
  F5  — Barras horizontais: 4 métodos Terminal Value
  F6a — Football Field Valuation (Grande Triangulação)
  F6b — Heatmap 7×7 Sensibilidade (COE × g)
  F7  — KDE Monte Carlo com áreas coloridas (P5/P25/P50/P75/P95)
  F8a — Conviction Score barras horizontais por dimensão
  F8b — Timeline Catalisadores (Gantt, próximos 8 trimestres)

Uso:
    python scripts/render_inline_dataviz.py --payload payload_F0.json --output grafico_F0.html --ticker PSSA3
"""

import argparse
import json
import os
import sys

try:
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    import numpy as np
except ImportError:
    print("❌ Faltam dependências. Rode: pip install plotly numpy")
    sys.exit(1)

# ─────────────────────────────────────────────────────────────────
#  PALETA E TEMPLATE GLOBAL (Bloomberg-like)
# ─────────────────────────────────────────────────────────────────
PAL = {
    "azul":     "#003366",
    "azul_m":   "#336699",
    "cinza":    "#4A4A4A",
    "cinza_l":  "#A0A0A0",
    "ambar":    "#CBA052",
    "verde":    "#27AE60",
    "amarelo":  "#F1C40F",
    "vermelho": "#C0392B",
    "verm_esc": "#8B0000",
    "branco":   "#FFFFFF",
}

BASE_LAYOUT = dict(
    plot_bgcolor="white",
    paper_bgcolor="white",
    font=dict(family="Helvetica Neue, Arial, sans-serif", color=PAL["cinza"], size=11),
    title_font=dict(family="Helvetica Neue, Arial, sans-serif", color=PAL["azul"], size=14),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    margin=dict(l=60, r=40, t=70, b=50),
)

def _save(fig, output_path, ticker, title):
    fig.update_layout(title=f"<b>{ticker}</b> — {title}", **BASE_LAYOUT)
    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)
    fig.write_html(output_path, include_plotlyjs="cdn")
    return True


# ─────────────────────────────────────────────────────────────────
#  F0 — Spider / Radar: 5 Forças Porter + Moat Score
# ─────────────────────────────────────────────────────────────────
def plot_f0_radar(data, output_path, ticker):
    """
    Payload esperado:
      "forcas_porter": {"rivalidade": 7, "fornecedores": 5, "compradores": 6,
                        "substitutos": 4, "entrantes": 8}
      "moat_score": 7.5
      "setor_mediana": {"rivalidade": 5, ...}  (opcional)
    """
    forcas = data.get("forcas_porter", {})
    if not forcas:
        return False

    categorias = list(forcas.keys())
    valores_emp = [forcas.get(k, 0) for k in categorias]

    setor = data.get("setor_mediana", {})
    valores_set = [setor.get(k, 5) for k in categorias] if setor else None

    # Fechar o polígono
    cats_closed = categorias + [categorias[0]]
    vals_closed = valores_emp + [valores_emp[0]]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=vals_closed, theta=cats_closed,
        fill="toself", fillcolor=f"rgba(0,51,102,0.15)",
        line=dict(color=PAL["azul"], width=2),
        name="Empresa"
    ))
    if valores_set:
        vals_set_closed = valores_set + [valores_set[0]]
        fig.add_trace(go.Scatterpolar(
            r=vals_set_closed, theta=cats_closed,
            fill="toself", fillcolor=f"rgba(160,160,160,0.10)",
            line=dict(color=PAL["cinza_l"], width=1.5, dash="dash"),
            name="Mediana Setor"
        ))

    moat = data.get("moat_score", None)
    subtitle = f" | Moat Score: {moat}/10" if moat else ""
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
        showlegend=True,
    )
    return _save(fig, output_path, ticker, f"5 Forças de Porter{subtitle}")


# ─────────────────────────────────────────────────────────────────
#  F1a — Waterfall: Lucro Reportado → Normalizado
# ─────────────────────────────────────────────────────────────────
def plot_f1a_waterfall(data, output_path, ticker):
    """
    Payload esperado:
      "waterfall": [
        {"label": "Lucro Reportado",         "value": 4200,  "type": "absolute"},
        {"label": "Itens Não-Recorrentes",    "value": -380,  "type": "relative"},
        {"label": "SBC",                      "value": -120,  "type": "relative"},
        {"label": "IFRS 16 / Leases",         "value": 60,   "type": "relative"},
        {"label": "Lucro Normalizado",        "value": 3760,  "type": "total"}
      ]
    """
    wf = data.get("waterfall", [])
    if not wf:
        return False

    labels = [d["label"] for d in wf]
    values = [d["value"] for d in wf]
    measures = []
    for d in wf:
        t = d.get("type", "relative")
        if t == "absolute":
            measures.append("absolute")
        elif t == "total":
            measures.append("total")
        else:
            measures.append("relative")

    colors = []
    for m, v in zip(measures, values):
        if m in ("absolute", "total"):
            colors.append(PAL["azul"])
        elif v >= 0:
            colors.append(PAL["verde"])
        else:
            colors.append(PAL["vermelho"])

    fig = go.Figure(go.Waterfall(
        name="Ajustes",
        orientation="v",
        measure=measures,
        x=labels,
        y=values,
        connector=dict(line=dict(color=PAL["cinza_l"], width=1)),
        increasing=dict(marker_color=PAL["verde"]),
        decreasing=dict(marker_color=PAL["vermelho"]),
        totals=dict(marker_color=PAL["azul"]),
        text=[f"R$ {v:,.0f}" for v in values],
        textposition="outside",
    ))
    return _save(fig, output_path, ticker, "Auditoria Contábil — Normalização do Lucro")


# ─────────────────────────────────────────────────────────────────
#  F1b — ROE DuPont Stacked Bars + Linha COE
# ─────────────────────────────────────────────────────────────────
def plot_f1b_roe_dupont(data, output_path, ticker):
    """
    Payload esperado:
      "dupont": [
        {"ano": 2020, "margem": 8.1, "giro": 0.6, "leverage": 1.8, "roe": 8.7},
        ...
      ]
      "coe": 12.5
    """
    dupont = data.get("dupont", [])
    if not dupont:
        return False

    anos = [str(d["ano"]) for d in dupont]
    margem = [d.get("margem", 0) for d in dupont]
    giro   = [d.get("giro", 0) * 10 for d in dupont]   # escala para visualizar junto
    lev    = [d.get("leverage", 0) * 2 for d in dupont]
    roe    = [d.get("roe", 0) for d in dupont]
    coe    = data.get("coe", None)

    fig = go.Figure()
    fig.add_trace(go.Bar(x=anos, y=margem, name="Margem Líquida",
                         marker_color=PAL["azul"], opacity=0.85))
    fig.add_trace(go.Bar(x=anos, y=giro, name="Giro × 10",
                         marker_color=PAL["azul_m"], opacity=0.75))
    fig.add_trace(go.Bar(x=anos, y=lev, name="Alavancagem × 2",
                         marker_color=PAL["cinza_l"], opacity=0.65))
    fig.add_trace(go.Scatter(x=anos, y=roe, name="ROE (%)",
                              mode="lines+markers",
                              line=dict(color=PAL["ambar"], width=2.5),
                              marker=dict(size=7)))
    if coe:
        fig.add_hline(y=coe, line_dash="dash", line_color=PAL["vermelho"],
                      annotation_text=f"COE = {coe}%",
                      annotation_position="right")

    fig.update_layout(barmode="stack", yaxis_title="%")
    return _save(fig, output_path, ticker, "ROE DuPont Decomposition vs COE")


# ─────────────────────────────────────────────────────────────────
#  F2a — Fade ROIC → WACC (linhas convergentes)
# ─────────────────────────────────────────────────────────────────
def plot_f2a_fade(data, output_path, ticker):
    """
    Payload esperado:
      "fade": [
        {"ano": 1, "roic_base": 22, "roic_bull": 25, "roic_bear": 18},
        ...
      ]
      "wacc": 11.5
      "cap_anos": 8
    """
    fade = data.get("fade", [])
    if not fade:
        return False

    anos  = [d["ano"] for d in fade]
    base  = [d.get("roic_base", 0) for d in fade]
    bull  = [d.get("roic_bull", base[i]) for i, d in enumerate(fade)]
    bear  = [d.get("roic_bear", base[i]) for i, d in enumerate(fade)]
    wacc  = data.get("wacc", 11.0)
    cap   = data.get("cap_anos", None)

    fig = go.Figure()
    # Área de incerteza (bull–bear)
    fig.add_trace(go.Scatter(
        x=anos + anos[::-1],
        y=bull + bear[::-1],
        fill="toself",
        fillcolor="rgba(0,51,102,0.10)",
        line=dict(color="rgba(0,0,0,0)"),
        name="Range Bull/Bear",
        hoverinfo="skip",
    ))
    fig.add_trace(go.Scatter(x=anos, y=base, name="ROIC Base",
                              line=dict(color=PAL["azul"], width=2.5),
                              mode="lines+markers"))
    fig.add_hline(y=wacc, line_dash="dash", line_color=PAL["vermelho"],
                  annotation_text=f"WACC = {wacc}%", annotation_position="right")
    if cap:
        fig.add_vrect(x0=cap - 0.5, x1=cap + 0.5,
                      fillcolor=PAL["ambar"], opacity=0.15,
                      annotation_text="CAP")

    fig.update_layout(yaxis_title="ROIC / WACC (%)", xaxis_title="Ano do Período Explícito")
    return _save(fig, output_path, ticker, "Fade ROIC → WACC (Competitive Advantage Period)")


# ─────────────────────────────────────────────────────────────────
#  F2b — Tornado Chart: Sensibilidade dos Drivers
# ─────────────────────────────────────────────────────────────────
def plot_f2b_tornado(data, output_path, ticker):
    """
    Payload esperado:
      "tornado": [
        {"driver": "Taxa de Crescimento Receita", "impacto_pos": 12.5, "impacto_neg": -9.8},
        {"driver": "Margem EBIT",                  "impacto_pos": 8.2,  "impacto_neg": -7.1},
        ...
      ]
      "fv_base": 85.0
    """
    tornado = data.get("tornado", [])
    if not tornado:
        return False

    # Ordenar por amplitude total (descendente)
    tornado = sorted(tornado, key=lambda d: abs(d.get("impacto_pos", 0)) + abs(d.get("impacto_neg", 0)),
                     reverse=True)

    drivers     = [d["driver"] for d in tornado]
    impacto_pos = [d.get("impacto_pos", 0) for d in tornado]
    impacto_neg = [d.get("impacto_neg", 0) for d in tornado]
    fv_base     = data.get("fv_base", 0)

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=impacto_pos, y=drivers, orientation="h",
        name="+1σ (Upside)", marker_color=PAL["verde"],
        text=[f"+R$ {v:.1f}" for v in impacto_pos], textposition="outside",
    ))
    fig.add_trace(go.Bar(
        x=impacto_neg, y=drivers, orientation="h",
        name="-1σ (Downside)", marker_color=PAL["vermelho"],
        text=[f"R$ {v:.1f}" for v in impacto_neg], textposition="outside",
    ))
    if fv_base:
        fig.add_vline(x=0, line_color=PAL["cinza"], line_width=1)

    fig.update_layout(
        barmode="overlay",
        xaxis_title="Impacto no Fair Value (R$/ação)",
        yaxis=dict(autorange="reversed"),
        height=max(300, len(drivers) * 45 + 100),
    )
    # Destacar driver #1 com borda âmbar
    if tornado:
        fig.update_traces(selector=dict(name="+1σ (Upside)"),
                          marker=dict(line=dict(color=PAL["ambar"], width=[3 if i == 0 else 0
                                                                             for i in range(len(drivers))])))

    return _save(fig, output_path, ticker, "Tornado Chart — Sensibilidade dos Drivers de Valor")


# ─────────────────────────────────────────────────────────────────
#  F2.5 — Capital Allocation Stacked 100% (10 anos)
# ─────────────────────────────────────────────────────────────────
def plot_f25_capital_allocation(data, output_path, ticker):
    """
    Payload esperado:
      "capital_allocation": [
        {"ano": 2015, "capex": 40, "ma": 10, "buybacks": 15, "dividendos": 20,
         "debt_paydown": 10, "caixa": 5},
        ...
      ]
    """
    alloc = data.get("capital_allocation", [])
    if not alloc:
        return False

    anos = [str(d["ano"]) for d in alloc]
    categorias = {
        "Capex":         (PAL["azul"],     "capex"),
        "M&A":           (PAL["azul_m"],   "ma"),
        "Buybacks":      (PAL["ambar"],    "buybacks"),
        "Dividendos":    (PAL["verde"],    "dividendos"),
        "Amort. Dívida": (PAL["cinza_l"], "debt_paydown"),
        "Caixa Retido":  (PAL["cinza"],   "caixa"),
    }

    fig = go.Figure()
    for nome, (cor, campo) in categorias.items():
        vals = [d.get(campo, 0) for d in alloc]
        if any(v > 0 for v in vals):
            fig.add_trace(go.Bar(x=anos, y=vals, name=nome,
                                 marker_color=cor, opacity=0.88))

    fig.update_layout(
        barmode="stack",
        yaxis_title="R$ milhões",
        xaxis_title="Ano",
    )
    return _save(fig, output_path, ticker, "Capital Allocation — Histórico 10 Anos")


# ─────────────────────────────────────────────────────────────────
#  F3 — FCFF vs Lucro Recorrente (barras agrupadas)
# ─────────────────────────────────────────────────────────────────
def plot_f3_fcff(data, output_path, ticker):
    """
    Payload esperado:
      "fcff_projetado_base_5_anos": [
        {"ano": 2025, "fcff": 3200, "lucro_recorrente": 4100},
        ...
      ]
    """
    fcff_data = data.get("fcff_projetado_base_5_anos", data.get("fcff_projetado_base", []))
    if not fcff_data:
        return False

    anos  = [str(d.get("ano", "")) for d in fcff_data]
    fcff  = [d.get("fcff", 0) for d in fcff_data]
    lucro = [d.get("lucro_recorrente", 0) for d in fcff_data]

    fig = go.Figure()
    fig.add_trace(go.Bar(x=anos, y=fcff, name="FCFF Projetado",
                         marker_color=PAL["azul"],
                         text=[f"R$ {v:.0f}" for v in fcff], textposition="outside"))
    fig.add_trace(go.Bar(x=anos, y=lucro, name="Lucro Recorrente",
                         marker_color=PAL["ambar"],
                         text=[f"R$ {v:.0f}" for v in lucro], textposition="outside"))

    fig.update_layout(barmode="group", yaxis_title="R$ milhões",
                      hovermode="x unified")
    return _save(fig, output_path, ticker, "Projeção de Caixa — FCFF vs Lucro Recorrente")


# ─────────────────────────────────────────────────────────────────
#  F4 — Term Structure of Discount Rates
# ─────────────────────────────────────────────────────────────────
def plot_f4_wacc_term_structure(data, output_path, ticker):
    """
    Payload esperado:
      "wacc_term_structure": [
        {"ano": 1, "ke": 14.2, "wacc": 12.1, "g": 8.5},
        ...
      ]
      "penman_alert_threshold": 9.0   (g > isso → zona vermelha)
    """
    ts = data.get("wacc_term_structure", [])
    if not ts:
        return False

    anos  = [d["ano"] for d in ts]
    ke    = [d.get("ke", 0) for d in ts]
    wacc  = [d.get("wacc", 0) for d in ts]
    g_arr = [d.get("g", 0) for d in ts]
    penman_thr = data.get("penman_alert_threshold", None)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=anos, y=ke, name="Ke (Custo do Equity)",
                              line=dict(color=PAL["azul"], width=2.5)))
    fig.add_trace(go.Scatter(x=anos, y=wacc, name="WACC",
                              line=dict(color=PAL["azul_m"], width=2, dash="dot")))
    fig.add_trace(go.Scatter(x=anos, y=g_arr, name="g Projetado",
                              line=dict(color=PAL["ambar"], width=2)))

    if penman_thr:
        fig.add_hline(y=penman_thr, line_dash="dash", line_color=PAL["vermelho"],
                      annotation_text=f"⚠️ Penman Alert (g = Rf+1% = {penman_thr}%)",
                      annotation_position="right")
        # Zona vermelha onde g > threshold
        above_thr = [g for g in g_arr if g > penman_thr]
        if above_thr:
            anos_above = [anos[i] for i, g in enumerate(g_arr) if g > penman_thr]
            fig.add_trace(go.Scatter(
                x=anos_above, y=[g for g in g_arr if g > penman_thr],
                fill="tozeroy", fillcolor="rgba(192,57,43,0.12)",
                line=dict(color="rgba(0,0,0,0)"),
                name="Zona Penman Alert", hoverinfo="skip",
            ))

    fig.update_layout(yaxis_title="Taxa (%)", xaxis_title="Ano Explícito")
    return _save(fig, output_path, ticker, "Term Structure — WACC · Ke · g Projetado")


# ─────────────────────────────────────────────────────────────────
#  F5 — Comparação Terminal Value (4 métodos)
# ─────────────────────────────────────────────────────────────────
def plot_f5_terminal_value(data, output_path, ticker):
    """
    Payload esperado:
      "terminal_value_methods": [
        {"metodo": "McKinsey CV",     "tv_bi": 52.3, "tv_ev_pct": 68},
        {"metodo": "Gordon Growth",   "tv_bi": 48.1, "tv_ev_pct": 63},
        {"metodo": "P/VP × ROE",      "tv_bi": 55.8, "tv_ev_pct": 72},
        {"metodo": "EPV (floor)",     "tv_bi": 38.0, "tv_ev_pct": 50},
      ]
      "ev_atual_bi": 76.5
    """
    methods = data.get("terminal_value_methods", [])
    if not methods:
        return False

    nomes  = [d["metodo"] for d in methods]
    tv_bi  = [d.get("tv_bi", 0) for d in methods]
    tv_pct = [d.get("tv_ev_pct", 0) for d in methods]
    ev_bi  = data.get("ev_atual_bi", None)

    # Cores: EPV = cinza (floor), outros = azul
    cores = [PAL["cinza_l"] if "EPV" in n or "floor" in n.lower() else PAL["azul"]
             for n in nomes]

    fig = go.Figure(go.Bar(
        x=tv_bi, y=nomes, orientation="h",
        marker_color=cores,
        text=[f"R$ {v:.1f}bi  ({p}% EV)" for v, p in zip(tv_bi, tv_pct)],
        textposition="outside",
    ))
    if ev_bi:
        fig.add_vline(x=ev_bi * 0.75, line_dash="dash", line_color=PAL["ambar"],
                      annotation_text="75% EV (limite prudente)")

    fig.update_layout(
        xaxis_title="Terminal Value (R$ bi)",
        yaxis=dict(autorange="reversed"),
        height=max(300, len(nomes) * 60 + 100),
    )
    return _save(fig, output_path, ticker, "Terminal Value — Comparação 4 Métodos")


# ─────────────────────────────────────────────────────────────────
#  F6a — Football Field Valuation
# ─────────────────────────────────────────────────────────────────
def plot_f6_football_field(data, output_path, ticker):
    """
    Payload esperado:
      "triangulacao": [
        {"metodo": "DCF FCFF Base",   "pior_cenario": 60, "cenario_base": 85, "melhor_cenario": 110},
        ...
      ]
      "preco_atual": 72.0
      "expected_value": 87.5
    """
    tri = data.get("triangulacao", [])
    if not tri:
        return False

    metodos  = [d.get("metodo", "...") for d in tri]
    pior     = [d.get("pior_cenario", 0) for d in tri]
    base     = [d.get("cenario_base", 0) for d in tri]
    otim     = [d.get("melhor_cenario", 0) for d in tri]
    preco    = data.get("preco_atual", None)
    ev       = data.get("expected_value", None)

    fig = go.Figure()
    for i, m in enumerate(metodos):
        # Barra de range
        fig.add_trace(go.Scatter(
            x=[pior[i], otim[i]], y=[m, m],
            mode="lines", line=dict(color=PAL["azul_m"], width=20),
            opacity=0.35, name=f"{m} range", showlegend=False, hoverinfo="skip",
        ))
        # Ponto base
        fig.add_trace(go.Scatter(
            x=[base[i]], y=[m],
            mode="markers+text",
            marker=dict(color=PAL["ambar"], size=12, symbol="diamond"),
            text=[f"R$ {base[i]:.2f}"], textposition="top center",
            name="Base" if i == 0 else None,
            showlegend=(i == 0),
        ))
        fig.add_annotation(x=pior[i], y=m, text=f"R$ {pior[i]:.2f}",
                           showarrow=False, xanchor="right", xshift=-8,
                           font=dict(size=9, color=PAL["cinza"]))
        fig.add_annotation(x=otim[i], y=m, text=f"R$ {otim[i]:.2f}",
                           showarrow=False, xanchor="left", xshift=8,
                           font=dict(size=9, color=PAL["cinza"]))

    if preco:
        fig.add_vline(x=preco, line_width=2, line_dash="dash",
                      line_color=PAL["vermelho"],
                      annotation_text=f"Preço Atual R$ {preco:.2f}",
                      annotation_position="top left")
    if ev:
        fig.add_vline(x=ev, line_width=2, line_color=PAL["ambar"],
                      annotation_text=f"Expected Value R$ {ev:.2f}",
                      annotation_position="top right")

    fig.update_layout(
        xaxis_title="Valor Intrínseco por Ação (R$)",
        yaxis=dict(type="category", autorange="reversed"),
        height=max(350, len(metodos) * 55 + 120),
        margin=dict(l=180),
    )
    return _save(fig, output_path, ticker, "Football Field — Grande Triangulação Central")


# ─────────────────────────────────────────────────────────────────
#  F6b — Heatmap 7×7 Sensibilidade (COE × g_terminal)
# ─────────────────────────────────────────────────────────────────
def plot_f6b_heatmap(data, output_path, ticker):
    """
    Payload esperado:
      "heatmap_7x7": {
        "eixo_x_label": "g Terminal (%)",
        "eixo_y_label": "COE / WACC (%)",
        "eixo_x": [2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0],
        "eixo_y": [10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0],
        "valores": [[...], ...],   # 7×7 com R$/ação
        "base_x": 3.0,
        "base_y": 11.5
      }
      "preco_atual": 72.0
    """
    hm = data.get("heatmap_7x7", {})
    if not hm or "valores" not in hm:
        return False

    z       = hm["valores"]
    x_vals  = hm.get("eixo_x", list(range(7)))
    y_vals  = hm.get("eixo_y", list(range(7)))
    x_label = hm.get("eixo_x_label", "g Terminal (%)")
    y_label = hm.get("eixo_y_label", "COE (%)")
    base_x  = hm.get("base_x", None)
    base_y  = hm.get("base_y", None)
    preco   = data.get("preco_atual", None)

    # Flat list for color scale reference
    flat = [v for row in z for v in row]
    vmin, vmax = min(flat), max(flat)
    vmid = preco if preco else (vmin + vmax) / 2

    fig = go.Figure(go.Heatmap(
        z=z, x=[str(v) for v in x_vals], y=[str(v) for v in y_vals],
        colorscale=[
            [0.0,              PAL["verm_esc"]],
            [(vmid - vmin) / max(vmax - vmin, 1), PAL["amarelo"]],
            [1.0,              PAL["verde"]],
        ],
        text=[[f"R$ {v:.1f}" for v in row] for row in z],
        texttemplate="%{text}",
        showscale=True,
        hovertemplate=f"{x_label}: %{{x}}<br>{y_label}: %{{y}}<br>FV: %{{text}}<extra></extra>",
    ))

    # Marcar caso base
    if base_x is not None and base_y is not None:
        fig.add_trace(go.Scatter(
            x=[str(base_x)], y=[str(base_y)],
            mode="markers",
            marker=dict(symbol="circle-open", size=16, color=PAL["ambar"], line=dict(width=3)),
            name="Caso Base", showlegend=True,
        ))

    fig.update_layout(
        xaxis_title=x_label, yaxis_title=y_label,
        height=420,
    )
    return _save(fig, output_path, ticker, "Heatmap 7×7 — Sensibilidade Fair Value")


# ─────────────────────────────────────────────────────────────────
#  F7 — KDE Monte Carlo com percentis
# ─────────────────────────────────────────────────────────────────
def plot_f7_monte_carlo(data, output_path, ticker):
    """
    Payload esperado:
      "monte_carlo": {
        "amostras": [75.2, 83.1, 90.0, ...],   # OU
        "percentis": {"p5": 55, "p25": 72, "p50": 85, "p75": 98, "p95": 115}
      }
      "preco_atual": 72.0
    """
    mc = data.get("monte_carlo", {})
    preco = data.get("preco_atual", None)

    amostras = mc.get("amostras", [])
    pcts     = mc.get("percentis", {})

    if not amostras and not pcts:
        return False

    fig = go.Figure()

    if amostras:
        arr = np.array(amostras, dtype=float)
        # KDE manual via histograma normalizado
        counts, edges = np.histogram(arr, bins=60, density=True)
        mids = (edges[:-1] + edges[1:]) / 2

        # Área verde (acima do preço atual)
        if preco:
            idx_split = np.searchsorted(mids, preco)
            fig.add_trace(go.Scatter(x=mids[:idx_split], y=counts[:idx_split],
                                      fill="tozeroy", fillcolor="rgba(192,57,43,0.25)",
                                      line=dict(color="rgba(0,0,0,0)"),
                                      name="Prob. Perda", hoverinfo="skip"))
            fig.add_trace(go.Scatter(x=mids[idx_split:], y=counts[idx_split:],
                                      fill="tozeroy", fillcolor="rgba(39,174,96,0.25)",
                                      line=dict(color="rgba(0,0,0,0)"),
                                      name="Prob. Ganho", hoverinfo="skip"))

        fig.add_trace(go.Scatter(x=mids, y=counts, mode="lines",
                                  line=dict(color=PAL["azul"], width=2),
                                  name="Distribuição KDE"))
        pcts = {
            "p5":  float(np.percentile(arr, 5)),
            "p25": float(np.percentile(arr, 25)),
            "p50": float(np.percentile(arr, 50)),
            "p75": float(np.percentile(arr, 75)),
            "p95": float(np.percentile(arr, 95)),
        }
    else:
        # Sem amostras, simula curva gaussiana a partir dos percentis
        p50 = pcts.get("p50", 85)
        p25 = pcts.get("p25", 72)
        sigma = (p50 - p25) / 0.674
        x = np.linspace(p50 - 4*sigma, p50 + 4*sigma, 300)
        y = (1/(sigma * np.sqrt(2*np.pi))) * np.exp(-0.5 * ((x - p50)/sigma)**2)
        if preco:
            idx = np.searchsorted(x, preco)
            fig.add_trace(go.Scatter(x=x[:idx], y=y[:idx], fill="tozeroy",
                                      fillcolor="rgba(192,57,43,0.20)",
                                      line=dict(color="rgba(0,0,0,0)"),
                                      name="Prob. Perda", hoverinfo="skip"))
            fig.add_trace(go.Scatter(x=x[idx:], y=y[idx:], fill="tozeroy",
                                      fillcolor="rgba(39,174,96,0.20)",
                                      line=dict(color="rgba(0,0,0,0)"),
                                      name="Prob. Ganho", hoverinfo="skip"))
        fig.add_trace(go.Scatter(x=x, y=y, mode="lines",
                                  line=dict(color=PAL["azul"], width=2),
                                  name="Distribuição (aprox.)"))

    # Linhas de percentis
    pct_labels = {"p5": "P5", "p25": "P25", "p50": "P50 (Mediana)", "p75": "P75", "p95": "P95"}
    pct_colors = [PAL["verm_esc"], PAL["vermelho"], PAL["ambar"], PAL["verde"], PAL["azul"]]
    for (k, label), cor in zip(pct_labels.items(), pct_colors):
        if k in pcts:
            fig.add_vline(x=pcts[k], line_dash="dot", line_color=cor,
                          annotation_text=f"{label}: R${pcts[k]:.1f}",
                          annotation_position="top")

    if preco:
        fig.add_vline(x=preco, line_dash="dash", line_color=PAL["cinza"],
                      annotation_text=f"Preço Atual: R${preco:.2f}",
                      annotation_position="bottom right")

    fig.update_layout(xaxis_title="Fair Value (R$/ação)",
                      yaxis_title="Densidade de Probabilidade")
    return _save(fig, output_path, ticker, "Stress Test — Distribuição Monte Carlo")


# ─────────────────────────────────────────────────────────────────
#  F8a — Conviction Score por Dimensão
# ─────────────────────────────────────────────────────────────────
def plot_f8a_conviction(data, output_path, ticker):
    """
    Payload esperado:
      "conviction": [
        {"dimensao": "Upside/Downside Ratio", "peso": 25, "nota": 8, "contrib": 2.0},
        {"dimensao": "Qualidade do Moat",      "peso": 20, "nota": 7, "contrib": 1.4},
        ...
      ]
      "conviction_total": 7.2
    """
    conv = data.get("conviction", [])
    if not conv:
        return False

    dims    = [d["dimensao"] for d in conv]
    notas   = [d.get("nota", 0) for d in conv]
    contribs = [d.get("contrib", 0) for d in conv]
    total   = data.get("conviction_total", None)

    cores = [PAL["verde"] if n >= 7 else PAL["ambar"] if n >= 5 else PAL["vermelho"]
             for n in notas]

    fig = go.Figure(go.Bar(
        x=contribs, y=dims, orientation="h",
        marker_color=cores,
        text=[f"{n}/10  (contribuição: {c:.1f})" for n, c in zip(notas, contribs)],
        textposition="outside",
    ))
    if total:
        fig.add_vline(x=total * max(contribs) / 10, line_color=PAL["ambar"],
                      line_dash="dash",
                      annotation_text=f"Score Total: {total}/10",
                      annotation_position="top right")

    fig.update_layout(
        xaxis_title="Contribuição Ponderada",
        yaxis=dict(autorange="reversed"),
        height=max(300, len(dims) * 50 + 100),
    )
    return _save(fig, output_path, ticker, f"Conviction Score — Disaggregation (Total: {total}/10)")


# ─────────────────────────────────────────────────────────────────
#  F8b — Timeline de Catalisadores (Gantt simplificado)
# ─────────────────────────────────────────────────────────────────
def plot_f8b_catalysts(data, output_path, ticker):
    """
    Payload esperado:
      "catalysts": [
        {"label": "Resultado 1T26",   "trimestre": "1T26", "tipo": "bull",  "impacto": 8},
        {"label": "Vencimento Dívida","trimestre": "2T26", "tipo": "bear",  "impacto": 5},
        {"label": "Expansão Saúde",   "trimestre": "3T26", "tipo": "bull",  "impacto": 6},
        ...
      ]
    """
    cats = data.get("catalysts", [])
    if not cats:
        return False

    bull_cats = [c for c in cats if c.get("tipo", "bull") == "bull"]
    bear_cats = [c for c in cats if c.get("tipo", "bear") == "bear"]

    fig = go.Figure()

    if bull_cats:
        fig.add_trace(go.Scatter(
            x=[c["trimestre"] for c in bull_cats],
            y=[c.get("impacto", 5) for c in bull_cats],
            mode="markers+text",
            marker=dict(symbol="triangle-up",
                        size=[c.get("impacto", 5) * 4 for c in bull_cats],
                        color=PAL["verde"]),
            text=[c["label"] for c in bull_cats],
            textposition="top center",
            name="Catalisador Bull 📈",
        ))

    if bear_cats:
        fig.add_trace(go.Scatter(
            x=[c["trimestre"] for c in bear_cats],
            y=[-c.get("impacto", 5) for c in bear_cats],
            mode="markers+text",
            marker=dict(symbol="triangle-down",
                        size=[c.get("impacto", 5) * 4 for c in bear_cats],
                        color=PAL["vermelho"]),
            text=[c["label"] for c in bear_cats],
            textposition="bottom center",
            name="Risco Bear 📉",
        ))

    fig.add_hline(y=0, line_color=PAL["cinza_l"], line_width=1)
    fig.update_layout(
        xaxis_title="Trimestre",
        yaxis_title="Impacto Estimado (magnitude)",
        hovermode="x unified",
        height=420,
    )
    return _save(fig, output_path, ticker, "Timeline de Catalisadores — Próximos 8 Trimestres")


# ─────────────────────────────────────────────────────────────────
#  ROTEADOR PRINCIPAL
# ─────────────────────────────────────────────────────────────────
CHART_ROUTER = {
    "F0":   plot_f0_radar,
    "F1A":  plot_f1a_waterfall,
    "F1B":  plot_f1b_roe_dupont,
    "F2A":  plot_f2a_fade,
    "F2B":  plot_f2b_tornado,
    "F25":  plot_f25_capital_allocation,
    "F3":   plot_f3_fcff,
    "F4":   plot_f4_wacc_term_structure,
    "F5":   plot_f5_terminal_value,
    "F6A":  plot_f6_football_field,
    "F6B":  plot_f6b_heatmap,
    "F6":   plot_f6_football_field,   # alias retrocompatível
    "F7":   plot_f7_monte_carlo,
    "F8A":  plot_f8a_conviction,
    "F8B":  plot_f8b_catalysts,
}

def plot_generic_bar(data, output_path, ticker):
    """Fallback genérico para fases sem roteador específico."""
    labels, values = [], []
    for k, v in data.items():
        if isinstance(v, (int, float)) and not k.startswith("fase") and not isinstance(v, bool):
            labels.append(k.replace("_", " ").title()[:24])
            values.append(v)
            if len(labels) >= 8:
                break
    if not labels:
        return False
    fig = go.Figure(go.Bar(
        x=values, y=labels, orientation="h",
        marker_color=PAL["azul"],
        text=[f"{v}" for v in values], textposition="outside",
    ))
    fig.update_layout(yaxis=dict(autorange="reversed"))
    return _save(fig, output_path, ticker, "Key Metrics Snapshot")


def main():
    parser = argparse.ArgumentParser(
        description="DCF Pipeline v4.0 — Renderizador de Dashboards Interativos (Plotly)"
    )
    parser.add_argument("--payload", required=True, help="Caminho para o JSON payload da fase")
    parser.add_argument("--output",  required=True, help="Caminho de saída do arquivo HTML")
    parser.add_argument("--ticker",  default="TICKER", help="Ticker do ativo (ex: PSSA3)")
    args = parser.parse_args()

    if not os.path.exists(args.payload):
        print(f"❌ Arquivo {args.payload} não encontrado.")
        sys.exit(1)

    try:
        with open(args.payload, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ Erro ao ler JSON: {e}")
        sys.exit(1)

    fase_raw = data.get("fase", "").upper().replace("_", "").replace(".", "")
    # Normalizar: "F2_5" → "F25", "F6_1" → "F6A", etc.
    fase_key = fase_raw.replace("F2P5", "F25").replace("F25", "F25")

    renderer = CHART_ROUTER.get(fase_key, None)

    # Tentativa com variantes se não encontrar direto
    if renderer is None:
        for key in CHART_ROUTER:
            if fase_raw.startswith(key):
                renderer = CHART_ROUTER[key]
                break

    if renderer is None:
        print(f"⚠️  Fase '{fase_raw}' sem renderer específico. Usando gráfico genérico.")
        renderer = plot_generic_bar

    success = renderer(data, args.output, args.ticker)

    if success:
        abs_path = os.path.abspath(args.output).replace("\\", "/")
        print(f"✅ Dashboard gerado: {args.output}")
        print(f"👉 [Abrir Dashboard Interativo](file:///{abs_path})")
    else:
        print(f"⚠️  Sem dados suficientes no payload para renderizar fase {fase_raw}.")
        sys.exit(1)


if __name__ == "__main__":
    main()
