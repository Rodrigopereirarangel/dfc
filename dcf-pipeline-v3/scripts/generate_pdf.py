#!/usr/bin/env python3
"""
generate_pdf.py — DCF Pipeline v4.0
Gerador de Relatório Institucional PDF

Autor: DCF Pipeline v4.0
Uso:
    python generate_pdf.py --ticker PSSA3 --output PSSA3_Initiation_Coverage_2026.pdf
    python generate_pdf.py --demo  # Gera PDF com dados de exemplo

Dependências:
    pip install reportlab matplotlib seaborn numpy pandas

Paleta Bloomberg/Goldman Sachs:
    Azul Marinho    : #003366  (cor primária)
    Cinza Ardósia   : #4A4A4A  (texto corpo)
    Âmbar           : #CBA052  (destaque)
    Verde           : #27AE60  (OK / positivo)
    Vermelho        : #C0392B  (grave / negativo)
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mticker
import numpy as np
from matplotlib.patches import FancyBboxPatch

# ── ReportLab ──────────────────────────────────────────────────
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    Image,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
    HRFlowable,
)
from reportlab.lib.colors import HexColor, white, black

# ─────────────────────────────────────────────────────────────────
#  PALETA E ESTILOS GLOBAIS
# ─────────────────────────────────────────────────────────────────
PAL = {
    "azul":    "#003366",
    "azul_m":  "#336699",
    "cinza":   "#4A4A4A",
    "cinza_l": "#A0A0A0",
    "ambar":   "#CBA052",
    "verde":   "#27AE60",
    "amarelo": "#F1C40F",
    "vermelho":"#C0392B",
    "verm_esc":"#8B0000",
    "bg_capa": "#001F3F",
    "faixa":   "#F5F5F5",
}

def hex_mpl(h):
    """Cor hex para matplotlib."""
    return h

def set_bloomberg_style():
    """Aplica estilo Bloomberg/Goldman em todos os gráficos matplotlib."""
    plt.rcParams.update({
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "axes.edgecolor": PAL["cinza_l"],
        "axes.grid": True,
        "grid.color": PAL["cinza_l"],
        "grid.linewidth": 0.4,
        "grid.alpha": 0.4,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.spines.left": False,
        "xtick.color": PAL["cinza"],
        "ytick.color": PAL["cinza"],
        "font.family": "DejaVu Sans",
        "font.size": 9,
        "axes.titlesize": 10,
        "axes.titleweight": "bold",
        "axes.titlecolor": PAL["azul"],
        "legend.frameon": False,
        "legend.loc": "upper left",
        "legend.fontsize": 8,
    })

# ─────────────────────────────────────────────────────────────────
#  GRÁFICOS POR FASE
# ─────────────────────────────────────────────────────────────────

def plot_radar_porter(scores_empresa, scores_setor, labels, out_path):
    """F0 — Radar Chart Spider das 5 Forças de Porter."""
    set_bloomberg_style()
    N = len(labels)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]
    emp = scores_empresa + scores_empresa[:1]
    set_ = scores_setor + scores_setor[:1]

    fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))
    ax.plot(angles, emp, "o-", linewidth=2, color=PAL["azul"], label="Empresa")
    ax.fill(angles, emp, alpha=0.2, color=PAL["azul"])
    ax.plot(angles, set_, "o--", linewidth=1, color=PAL["cinza_l"], label="Setor (médio)")
    ax.fill(angles, set_, alpha=0.07, color=PAL["cinza_l"])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, size=8, color=PAL["cinza"])
    ax.set_ylim(0, 10)
    ax.set_title("Vantagem Competitiva — 5 Forças de Porter", pad=15)
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close()


def plot_waterfall(labels, values, out_path, title="Waterfall Lucro Reportado → Normalizado"):
    """F1 — Waterfall Bridge do Lucro."""
    set_bloomberg_style()
    n = len(values)
    fig, ax = plt.subplots(figsize=(8, 4))

    running = 0
    for i, (lbl, val) in enumerate(zip(labels, values)):
        if i == 0 or i == n - 1:
            color = PAL["azul"]
            bottom = 0
            bar_val = abs(val)
        else:
            color = PAL["verde"] if val > 0 else PAL["verm_esc"]
            if val < 0:
                bottom = running + val
            else:
                bottom = running
            bar_val = abs(val)

        ax.bar(i, bar_val, bottom=bottom, color=color, width=0.55, zorder=3)
        ax.text(i, bottom + bar_val / 2, f"R${val:,.0f}m", ha="center", va="center",
                color="white", fontsize=7.5, fontweight="bold")

        if i > 0 and i < n - 1:
            running += val

    ax.set_xticks(range(n))
    ax.set_xticklabels(labels, rotation=15, ha="right", fontsize=8)
    ax.set_ylabel("R$ Milhões", fontsize=8)
    ax.set_title(title, fontweight="bold")
    ax.axhline(0, color=PAL["cinza"], linewidth=0.5)
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close()


def plot_tornado(drivers, impacts_pos, impacts_neg, out_path, base_fv=0):
    """F2 — Tornado Chart de Sensibilidade (estilo sell-side)."""
    set_bloomberg_style()
    y = np.arange(len(drivers))
    fig, ax = plt.subplots(figsize=(8, max(4, len(drivers) * 0.7)))

    ax.barh(y, impacts_pos, color=PAL["azul"], height=0.5, label="+1σ", zorder=3)
    ax.barh(y, [-v for v in impacts_neg], color=PAL["vermelho"], height=0.5, label="-1σ", zorder=3)
    ax.axvline(0, color=PAL["cinza"], linewidth=1.0)
    ax.set_yticks(y)
    ax.set_yticklabels(drivers, fontsize=9)
    ax.set_xlabel("Impacto no Fair Value (R$/ação)", fontsize=8)
    ax.set_title("Tornado Chart — Sensibilidade dos Value Drivers", fontweight="bold")

    # Adicionar rótulos
    for i, (p, n) in enumerate(zip(impacts_pos, impacts_neg)):
        ax.text(p + 0.01, i, f"+R${p:.2f}", va="center", fontsize=7, color=PAL["azul"])
        ax.text(-n - 0.01, i, f"-R${n:.2f}", va="center", ha="right", fontsize=7, color=PAL["vermelho"])

    ax.legend(fontsize=8)
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close()


def plot_heatmap_7x7(coe_vals, g_vals, fv_matrix, preco_atual, out_path):
    """F6 — Heatmap Térmico 7×7 Fair Value vs. COE e g."""
    import matplotlib.colors as mcolors
    set_bloomberg_style()
    fig, ax = plt.subplots(figsize=(8, 6))

    # Normalização centrada no preço atual
    vmin = preco_atual * 0.6
    vmax = preco_atual * 1.6
    norm = mcolors.TwoSlopeNorm(vmin=vmin, vcenter=preco_atual, vmax=vmax)
    cmap = mcolors.LinearSegmentedColormap.from_list(
        "traffic",
        [PAL["vermelho"], PAL["amarelo"], PAL["verde"]]
    )

    matrix = np.array(fv_matrix) if fv_matrix else np.random.uniform(vmin, vmax, (7, 7))
    im = ax.imshow(matrix, cmap=cmap, norm=norm, aspect="auto")

    ax.set_xticks(range(len(coe_vals)))
    ax.set_xticklabels([f"{v:.0%}" for v in coe_vals], fontsize=8)
    ax.set_yticks(range(len(g_vals)))
    ax.set_yticklabels([f"{v:.0%}" for v in g_vals], fontsize=8)
    ax.set_xlabel("COE / WACC", fontsize=9)
    ax.set_ylabel("g Terminal", fontsize=9)
    ax.set_title("Heatmap de Sensibilidade 7×7 — Fair Value por Ação (R$)", fontweight="bold")

    for i in range(len(g_vals)):
        for j in range(len(coe_vals)):
            val = matrix[i, j]
            txt_color = "white" if abs(val - preco_atual) > preco_atual * 0.15 else "black"
            ax.text(j, i, f"R${val:.0f}", ha="center", va="center",
                    fontsize=7, color=txt_color, fontweight="bold")

    plt.colorbar(im, ax=ax, label="R$/ação", fraction=0.03)
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close()


def plot_football_field(metodos, fv_min, fv_ponto, fv_max, expected_value, preco_atual, out_path):
    """F7 — Football Field Valuation."""
    set_bloomberg_style()
    n = len(metodos)
    cores = [PAL["azul"], PAL["azul_m"], PAL["verm_esc"], PAL["cinza"], PAL["cinza_l"]]
    fig, ax = plt.subplots(figsize=(9, max(4, n * 0.9)))

    for i, (met, mn, pt, mx) in enumerate(zip(metodos, fv_min, fv_ponto, fv_max)):
        c = cores[i % len(cores)]
        ax.barh(i, mx - mn, left=mn, color=c, height=0.45, alpha=0.85, zorder=3)
        ax.plot([pt, pt], [i - 0.25, i + 0.25], color="white", linewidth=2, zorder=4)
        ax.text(mx + 0.3, i, f"R${mx:.0f}", va="center", fontsize=7.5, color=PAL["cinza"])
        ax.text(mn - 0.3, i, f"R${mn:.0f}", va="center", ha="right", fontsize=7.5, color=PAL["cinza"])

    ax.axvline(expected_value, color=PAL["ambar"], linewidth=2, linestyle="--",
               label=f"Expected Value R${expected_value:.0f}", zorder=5)
    ax.axvline(preco_atual, color=PAL["cinza_l"], linewidth=1.5, linestyle=":",
               label=f"Preço Atual R${preco_atual:.0f}", zorder=5)

    ax.set_yticks(range(n))
    ax.set_yticklabels(metodos, fontsize=9)
    ax.set_xlabel("Fair Value (R$/ação)", fontsize=9)
    ax.set_title("Football Field — Triangulação de Métodos de Valuation", fontweight="bold")
    ax.legend(fontsize=8)
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close()


def plot_conviction_bar(dimensoes, pesos, notas, out_path):
    """F8 — Conviction Score Breakdown."""
    set_bloomberg_style()
    contribs = [p * n for p, n in zip(pesos, notas)]
    colunas = ["royalblue" if c >= 1.4 else PAL["amarelo"] if c >= 0.8 else PAL["vermelho"]
               for c in contribs]
    fig, ax = plt.subplots(figsize=(7, 4))
    y = np.arange(len(dimensoes))
    ax.barh(y, contribs, color=colunas, height=0.5, zorder=3)
    ax.axvline(sum(contribs) / len(contribs), color=PAL["ambar"],
               linewidth=1.5, linestyle="--", label=f"Score Total: {sum(contribs):.2f}/10")
    ax.set_yticks(y)
    ax.set_yticklabels(dimensoes, fontsize=9)
    ax.set_xlabel("Contribuição Ponderada (0–2.5)", fontsize=8)
    ax.set_title("Conviction Score — Decomposição por Dimensão", fontweight="bold")
    for i, val in enumerate(contribs):
        ax.text(val + 0.02, i, f"{val:.2f}", va="center", fontsize=8, color=PAL["cinza"])
    ax.legend(fontsize=8)
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close()


# ─────────────────────────────────────────────────────────────────
#  BUILDER DO PDF (ReportLab Platypus)
# ─────────────────────────────────────────────────────────────────

def build_pdf(payload, ticker, output_path):
    """Monta o documento PDF completo."""
    tmp = Path("./tmp_charts")
    tmp.mkdir(exist_ok=True)

    styles = getSampleStyleSheet()
    style_h1 = ParagraphStyle("H1", parent=styles["Heading1"],
                               textColor=HexColor(PAL["azul"]), fontSize=14)
    style_h2 = ParagraphStyle("H2", parent=styles["Heading2"],
                               textColor=HexColor(PAL["azul"]), fontSize=11)
    style_body = ParagraphStyle("Body", parent=styles["Normal"],
                                 textColor=HexColor(PAL["cinza"]), fontSize=9, leading=13)
    style_caption = ParagraphStyle("Caption", parent=styles["Normal"],
                                    textColor=HexColor(PAL["cinza_l"]), fontSize=7, italic=True)
    style_header = ParagraphStyle("FundHeader", parent=styles["Normal"],
                                   textColor=white, fontSize=18, fontName="Helvetica-Bold",
                                   alignment=1)
    style_sub = ParagraphStyle("Sub", parent=styles["Normal"],
                                textColor=HexColor(PAL["ambar"]), fontSize=12,
                                fontName="Helvetica-Bold", alignment=1)
    style_thesis = ParagraphStyle("Thesis", parent=styles["Normal"],
                                   textColor=HexColor(PAL["cinza_l"]), fontSize=9, leading=14,
                                   alignment=1)
    style_disclaimer = ParagraphStyle("Disclaimer", parent=styles["Normal"],
                                      textColor=HexColor(PAL["cinza_l"]), fontSize=6.5, italic=True)

    doc = BaseDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=1.5*cm,
        leftMargin=1.5*cm,
        topMargin=1.5*cm,
        bottomMargin=1.5*cm,
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin,
                  doc.width, doc.height, id="normal")
    doc.addPageTemplates([PageTemplate(id="main", frames=frame)])

    # Dados do payload
    ticker_name = payload.get("ticker", ticker)
    preco_atual = payload.get("preco_atual", 52.0)
    expected_val = payload.get("expected_value_acao", 46.5)
    upside_pct = (expected_val / preco_atual - 1) * 100
    conv_score = payload.get("conviction_score", 0.0)
    recomendacao = payload.get("recomendacao", "Manter")
    thesis_text = payload.get("investment_thesis", "Tese de investimento a ser preenchida conforme análise das Fases 0-8.")
    data_analise = datetime.now().strftime("%d/%B/%Y")

    rec_color = PAL["verde"] if "Compra" in recomendacao else (PAL["vermelho"] if "Vend" in recomendacao else PAL["amarelo"])

    story = []

    # ── CAPA ──────────────────────────────────────────────────────
    capa_data = [
        [Paragraph(f"INITIATION OF COVERAGE", style_header)],
        [Paragraph(f"{ticker_name}", ParagraphStyle("TK", parent=style_header, fontSize=28, textColor=HexColor(PAL["ambar"])))],
        [Spacer(1, 0.5*cm)],
        [Paragraph(recomendacao.upper(), ParagraphStyle("REC", parent=style_sub, fontSize=22, textColor=HexColor(rec_color)))],
        [Spacer(1, 0.3*cm)],
        [Paragraph(f"Preço Alvo: R${expected_val:.2f}  |  Preço Atual: R${preco_atual:.2f}  |  Upside: {upside_pct:+.1f}%", style_sub)],
        [Paragraph(f"Conviction Score: {conv_score:.1f}/10", ParagraphStyle("CS", parent=style_sub, fontSize=12, textColor=HexColor(PAL["cinza_l"])))],
        [Spacer(1, 0.6*cm)],
        [HRFlowable(width="100%", thickness=1, color=HexColor(PAL["ambar"]))],
        [Spacer(1, 0.3*cm)],
        [Paragraph("<b>Investment Thesis</b>", ParagraphStyle("ITTitle", parent=style_sub, fontSize=10, textColor=white))],
        [Paragraph(thesis_text, style_thesis)],
        [Spacer(1, 1*cm)],
        [Paragraph(f"DCF Pipeline v4.0  |  {data_analise}  |  Análise Fundamentalista Institucional", style_disclaimer)],
        [Paragraph("Este relatório não constitui recomendação formal de investimento.", style_disclaimer)],
    ]
    capa_table = Table(capa_data, colWidths=[doc.width])
    capa_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), HexColor(PAL["bg_capa"])),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
    ]))
    story.append(capa_table)
    story.append(PageBreak())

    # ── SEÇÕES DE CONTEÚDO ────────────────────────────────────────
    def section_title(text):
        story.append(Spacer(1, 0.4*cm))
        story.append(HRFlowable(width="100%", thickness=2, color=HexColor(PAL["azul"])))
        story.append(Paragraph(text, style_h1))
        story.append(Spacer(1, 0.2*cm))

    def subsection(text):
        story.append(Spacer(1, 0.2*cm))
        story.append(Paragraph(text, style_h2))

    def body(text):
        story.append(Paragraph(text, style_body))

    def add_chart(img_path, caption="", w=14*cm, h=8*cm):
        if os.path.exists(img_path):
            story.append(Image(img_path, width=w, height=h))
            if caption:
                story.append(Paragraph(caption, style_caption))
            story.append(Spacer(1, 0.3*cm))

    def table_inst(data, col_widths=None):
        """Tabela Institucional zebrada."""
        if col_widths is None:
            col_widths = [doc.width / len(data[0])] * len(data[0])
        t = Table(data, colWidths=col_widths, repeatRows=1)
        style = TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), HexColor(PAL["azul"])),
            ("TEXTCOLOR", (0, 0), (-1, 0), white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 8),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, HexColor(PAL["faixa"])]),
            ("FONTSIZE", (0, 1), (-1, -1), 8),
            ("TEXTCOLOR", (0, 1), (-1, -1), HexColor(PAL["cinza"])),
            ("GRID", (0, 0), (-1, -1), 0.3, HexColor(PAL["cinza_l"])),
            ("ALIGN", (1, 0), (-1, -1), "CENTER"),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ])
        t.setStyle(style)
        story.append(t)
        story.append(Spacer(1, 0.3*cm))

    # ── F0: INTELIGÊNCIA COMPETITIVA ──────────────────────────────
    section_title("Fase 0 — Inteligência Competitiva & Enquadramento")
    subsection("5 Forças de Porter — Vantagem Competitiva")

    f0 = payload.get("F0_COMPLETA", {})
    porter = f0.get("forcas_porter", {})
    porter_labels = ["Rivalidade", "Entrantes", "Fornecedores", "Compradores", "Substitutos"]
    e_scores = [porter.get(k.lower(), {}).get("score_empresa", 5) for k in porter_labels]
    s_scores = [porter.get(k.lower(), {}).get("score_setor", 5) for k in porter_labels]

    radar_path = str(tmp / "f0_radar.png")
    plot_radar_porter(e_scores, s_scores, porter_labels, radar_path)
    add_chart(radar_path, "Radar Chart — Empresa vs. Setor em 5 dimensões estratégicas (Score 1-10)")

    nota_moat = f0.get("nota_durabilidade_moat", 0)
    tipo_moat = f0.get("tipo_moat", "—")
    diag = f0.get("diagnostico_mercado", "—")

    table_inst([
        ["Métrica", "Valor"],
        ["Nota de Durabilidade do Moat", f"{nota_moat}/10"],
        ["Tipo de Moat Identificado", tipo_moat],
        ["Diagnóstico de Mercado", diag],
        ["Preço Atual", f"R${f0.get('preco_atual', preco_atual):.2f}"],
        ["g Implícito no Preço", f"{f0.get('g_implicito', 0):.1%}"],
        ["ROIC Implícito no Preço", f"{f0.get('roic_implicito', 0):.1%}"],
        ["ERP Implícito", f"{f0.get('erp_implicito', 0):.1%}"],
    ], col_widths=[9*cm, 7*cm])
    story.append(PageBreak())

    # ── F1: AUDITORIA CONTÁBIL ────────────────────────────────────
    section_title("Fase 1 — Auditoria Contábil Forense")
    subsection("Waterfall — Lucro Reportado → Normalizado")

    f1 = payload.get("F1_COMPLETA", {})
    wf = f1.get("waterfall_steps", [
        {"label": "Lucro Reportado", "valor": 4200},
        {"label": "Não-Recorrentes", "valor": -200},
        {"label": "SBC", "valor": -80},
        {"label": "IFRS 16", "valor": -100},
        {"label": "Lucro Normalizado", "valor": 3820},
    ])
    wf_labels = [s["label"] for s in wf]
    wf_values = [s["valor"] for s in wf]

    wf_path = str(tmp / "f1_waterfall.png")
    plot_waterfall(wf_labels, wf_values, wf_path)
    add_chart(wf_path, "Waterfall — Bridge do Lucro GAAP Reportado para o Lucro Normalizado (R$ Milhões)")

    roae = f1.get("roae_normalizado", 0)
    table_inst([
        ["Indicador", "Valor"],
        ["ROAE Normalizado", f"{roae:.1f}%"],
        ["FCF / Net Income (5A)", f"{f1.get('fcf_netincome_ratio_5a', 0):.0%}"],
        ["Accruals Ratio", f"{f1.get('accruals_ratio', 0):.1%}"],
        ["DL/EBITDA", f"{f1.get('dl_ebitda', 0):.1f}×"],
        ["LPA Normalizado", f"R${f1.get('lpa_normalizado', 0):.2f}"],
    ], col_widths=[9*cm, 7*cm])
    story.append(PageBreak())

    # ── F2: VALUE DRIVERS ─────────────────────────────────────────
    section_title("Fase 2 — Decomposição de Value Drivers")
    subsection("Tornado Chart — Sensibilidade dos Drivers ao Fair Value")

    f2 = payload.get("F2_COMPLETA", {})
    drivers = f2.get("tornado_drivers", [
        {"rank": 1, "driver": "Driver 1 (placeholder)", "impacto_positivo": 4.0, "impacto_negativo": 4.5},
        {"rank": 2, "driver": "Driver 2 (placeholder)", "impacto_positivo": 3.0, "impacto_negativo": 3.2},
        {"rank": 3, "driver": "Driver 3 (placeholder)", "impacto_positivo": 2.0, "impacto_negativo": 2.1},
    ])
    dr_labels = [d["driver"] for d in drivers]
    dr_pos = [d["impacto_positivo"] for d in drivers]
    dr_neg = [d["impacto_negativo"] for d in drivers]

    tornado_path = str(tmp / "f2_tornado.png")
    plot_tornado(dr_labels, dr_pos, dr_neg, tornado_path)
    add_chart(tornado_path, "Tornado Chart — Impacto de ±1σ de cada driver no Fair Value (R$/ação)")
    story.append(PageBreak())

    # ── F6: FAIR VALUE & SENSIBILIDADE ───────────────────────────
    section_title("Fase 6 — Agregação, Cenários & Sensibilidade")
    subsection("Heatmap 7×7 — Fair Value vs. COE e g Terminal")

    f6 = payload.get("F6_COMPLETA", {})
    hm = f6.get("heatmap_7x7", {})
    coe_vals = hm.get("eixo_x_coe", [0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18])
    g_vals = hm.get("eixo_y_g", [0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08])
    fv_matrix = hm.get("valores", [])

    hm_path = str(tmp / "f6_heatmap.png")
    plot_heatmap_7x7(coe_vals, g_vals, fv_matrix or None, preco_atual, hm_path)
    add_chart(hm_path, "Heatmap Térmico — Fair Value por Ação. Verde=Compra, Amarelo=Neutro, Vermelho=Vender")

    cenarios = f6.get("cenarios", [
        {"nome": "Distress", "prob": 5, "fv": 25.0},
        {"nome": "Bear", "prob": 25, "fv": 35.0},
        {"nome": "Base", "prob": 45, "fv": 46.5},
        {"nome": "Bull", "prob": 25, "fv": 62.0},
    ])
    table_inst(
        [["Cenário", "Probabilidade", "Fair Value", "Upside"]] +
        [[c["nome"], f"{c['prob']}%", f"R${c['fv']:.2f}", f"{(c['fv']/preco_atual - 1)*100:+.1f}%"]
         for c in cenarios] +
        [["Expected Value", "100%", f"R${f6.get('expected_value_acao', expected_val):.2f}",
          f"{(f6.get('expected_value_acao', expected_val)/preco_atual - 1)*100:+.1f}%"]],
        col_widths=[5*cm, 4*cm, 4*cm, 3*cm]
    )
    story.append(PageBreak())

    # ── F7: TRIANGULAÇÃO / FOOTBALL FIELD ────────────────────────
    section_title("Fase 7 — Stress Test & Triangulação")
    subsection("Football Field — Triangulação de Métodos")

    f7 = payload.get("F7_COMPLETA", {})
    tri = f7.get("triangulacao", [
        {"metodo": "DCF Base", "fv_min": 40.0, "fv_ponto": 46.5, "fv_max": 55.0},
        {"metodo": "EPV (Floor)", "fv_min": 32.0, "fv_ponto": 36.0, "fv_max": 40.0},
        {"metodo": "Múltiplos Históricos", "fv_min": 44.0, "fv_ponto": 50.0, "fv_max": 60.0},
    ])
    ff_path = str(tmp / "f7_football.png")
    plot_football_field(
        [t["metodo"] for t in tri],
        [t["fv_min"] for t in tri],
        [t["fv_ponto"] for t in tri],
        [t["fv_max"] for t in tri],
        expected_val, preco_atual, ff_path
    )
    add_chart(ff_path, "Football Field — Sobreposição de Faixas de Valuation por Método")
    story.append(PageBreak())

    # ── F8: DECISÃO E CONVICTION ──────────────────────────────────
    section_title("Fase 8 — Decisão: Conviction & Position Sizing")

    f8 = payload.get("F8_COMPLETA", {})
    breakdown = f8.get("conviction_breakdown", {
        "upside_downside": {"peso": 0.25, "nota": 6.0, "contrib": 1.5},
        "moat":            {"peso": 0.20, "nota": 7.0, "contrib": 1.4},
        "management":      {"peso": 0.20, "nota": 6.5, "contrib": 1.3},
        "confianca_projecoes": {"peso": 0.15, "nota": 6.0, "contrib": 0.9},
        "triangulacao":    {"peso": 0.10, "nota": 7.0, "contrib": 0.7},
        "qmj":             {"peso": 0.10, "nota": 6.5, "contrib": 0.65},
    })

    dim_names = list(breakdown.keys())
    pesos = [breakdown[d]["peso"] for d in dim_names]
    notas = [breakdown[d]["nota"] for d in dim_names]
    dim_labels = [d.replace("_", " ").title() for d in dim_names]

    conv_path = str(tmp / "f8_conviction.png")
    plot_conviction_bar(dim_labels, pesos, notas, conv_path)
    add_chart(conv_path, "Conviction Score — Decomposição por Dimensão (10 = máximo)")

    kelly_full = f8.get("kelly_full", 0.0)
    kelly_half = f8.get("kelly_half", 0.0)
    pos_max = f8.get("posicao_maxima_pct_portfolio", 0.0)

    table_inst([
        ["Parâmetro", "Valor"],
        ["Conviction Score Final", f"{conv_score:.2f}/10"],
        ["Recomendação", recomendacao],
        ["Full Kelly", f"{kelly_full:.1%}"],
        ["Half-Kelly (recomendado)", f"{kelly_half:.1%}"],
        ["Posição Máxima no Portfólio", f"{pos_max:.1%}"],
    ], col_widths=[9*cm, 7*cm])

    # Disclaimer final
    story.append(Spacer(1, 1*cm))
    story.append(HRFlowable(width="100%", thickness=0.5, color=HexColor(PAL["cinza_l"])))
    story.append(Spacer(1, 0.2*cm))
    story.append(Paragraph(
        f"DCF Pipeline v4.0 | Análise gerada em {data_analise} | Ticker: {ticker_name} | "
        "Esta análise não constitui recomendação formal de investimento. Não considere este "
        "documento como oferta de compra ou venda de valores mobiliários.",
        style_disclaimer
    ))

    # ── GERAR PDF ─────────────────────────────────────────────────
    doc.build(story)
    print(f"✅ PDF gerado com sucesso: {output_path}")


# ─────────────────────────────────────────────────────────────────
#  CARREGADOR DE PAYLOADS
# ─────────────────────────────────────────────────────────────────

def load_payloads(payload_dir):
    """Carrega e mescla todos os JSON Payloads exportados pelas Skills."""
    payload = {}
    if not payload_dir or not os.path.isdir(payload_dir):
        return payload
    for f in Path(payload_dir).glob("*.json"):
        try:
            with open(f) as jf:
                data = json.load(jf)
                fase = data.get("fase", "")
                payload[fase] = data
                # Também mescla chaves de alto nível para acesso direto
                payload.update(data)
        except Exception as e:
            print(f"⚠️  Erro ao carregar {f}: {e}")
    return payload


def demo_payload(ticker):
    """Payload de demonstração para validar a formatação do PDF."""
    return {
        "ticker": ticker,
        "preco_atual": 52.0,
        "expected_value_acao": 46.5,
        "conviction_score": 6.8,
        "recomendacao": "Manter",
        "investment_thesis": (
            "Empresa de seguro com ROAE de 22,7% e moat moderado em dados de sinistros. "
            "O preço atual de R$52 implica premissas de ROE terminal e crescimento que "
            "consideramos excessivamente otimistas dado o ciclo de juros em curso. "
            "Aguardamos convergência ao nosso Expected Value de R$46,50 para posição relevante."
        ),
        "F0_COMPLETA": {
            "nota_durabilidade_moat": 7,
            "tipo_moat": "Escala de Dados + Switching Costs",
            "diagnostico_mercado": "Otimista",
            "preco_atual": 52.0,
            "g_implicito": 0.068,
            "roic_implicito": 0.22,
            "erp_implicito": 0.065,
            "forcas_porter": {
                "rivalidade": {"score_empresa": 4, "score_setor": 6},
                "entrantes":  {"score_empresa": 7, "score_setor": 5},
                "fornecedores": {"score_empresa": 8, "score_setor": 6},
                "compradores":  {"score_empresa": 6, "score_setor": 5},
                "substitutos":  {"score_empresa": 5, "score_setor": 5},
            },
        },
        "F1_COMPLETA": {
            "roae_normalizado": 16.1,
            "lpa_normalizado": 5.93,
            "fcf_netincome_ratio_5a": 0.82,
            "accruals_ratio": 0.04,
            "dl_ebitda": -3.68,
            "waterfall_steps": [
                {"label": "Lucro Reportado", "valor": 4200},
                {"label": "Não-Recorrentes", "valor": -180},
                {"label": "SBC", "valor": -60},
                {"label": "Resultado Fin.", "valor": -540},
                {"label": "Lucro Normalizado", "valor": 3420},
            ],
        },
        "F2_COMPLETA": {
            "roic_atual": 0.227,
            "cap_implicito_anos": 10,
            "cap_base_rate_setor_anos": 6,
            "tornado_drivers": [
                {"rank": 1, "driver": "Sinistralidade Auto", "impacto_positivo": 5.2, "impacto_negativo": 5.8},
                {"rank": 2, "driver": "Selic (Resultado Fin.)", "impacto_positivo": 3.8, "impacto_negativo": 4.1},
                {"rank": 3, "driver": "Crescimento Saúde", "impacto_positivo": 3.1, "impacto_negativo": 2.9},
                {"rank": 4, "driver": "Inadimplência Bank", "impacto_positivo": 1.8, "impacto_negativo": 2.2},
                {"rank": 5, "driver": "g Terminal", "impacto_positivo": 1.5, "impacto_negativo": 1.7},
            ],
        },
        "F6_COMPLETA": {
            "expected_value_acao": 46.5,
            "upside_pct": -10.6,
            "razao_upside_downside": 1.4,
            "kelly_implicito": -0.05,
            "erp_implicito": 0.072,
            "cenarios": [
                {"nome": "Distress", "prob": 5, "fv": 22.0},
                {"nome": "Bear", "prob": 25, "fv": 35.0},
                {"nome": "Base", "prob": 45, "fv": 47.3},
                {"nome": "Bull", "prob": 25, "fv": 65.0},
            ],
            "heatmap_7x7": {
                "eixo_x_coe": [0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18],
                "eixo_y_g": [0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08],
                "valores": [],
            },
        },
        "F7_COMPLETA": {
            "qmj_score": 7.2,
            "triangulacao": [
                {"metodo": "DCF Base (P/VP × ROE)", "fv_min": 40.0, "fv_ponto": 46.5, "fv_max": 55.0},
                {"metodo": "EPV Greenwald (Floor)", "fv_min": 28.0, "fv_ponto": 33.0, "fv_max": 38.0},
                {"metodo": "Múltiplos Históricos P/L", "fv_min": 42.0, "fv_ponto": 50.0, "fv_max": 60.0},
                {"metodo": "DDM Gordon", "fv_min": 38.0, "fv_ponto": 44.0, "fv_max": 51.0},
            ],
        },
        "F8_COMPLETA": {
            "conviction_score": 6.8,
            "recomendacao": "Manter",
            "kelly_full": -0.02,
            "kelly_half": 0.0,
            "posicao_maxima_pct_portfolio": 0.0,
            "conviction_breakdown": {
                "upside_downside":     {"peso": 0.25, "nota": 4.5, "contrib": 1.125},
                "moat":                {"peso": 0.20, "nota": 7.0, "contrib": 1.40},
                "management":          {"peso": 0.20, "nota": 7.5, "contrib": 1.50},
                "confianca_projecoes": {"peso": 0.15, "nota": 6.0, "contrib": 0.90},
                "triangulacao":        {"peso": 0.10, "nota": 7.0, "contrib": 0.70},
                "qmj":                 {"peso": 0.10, "nota": 7.2, "contrib": 0.72},
            },
        },
    }


# ─────────────────────────────────────────────────────────────────
#  CLI
# ─────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="DCF Pipeline v4.0 — Gerador de Relatório Institucional PDF"
    )
    parser.add_argument("--ticker", default="TICKER", help="Ticker do ativo (ex: PSSA3)")
    parser.add_argument("--output", default=None, help="Caminho do arquivo PDF de saída")
    parser.add_argument("--payload-dir", default=None, help="Pasta com os arquivos JSON Payload das fases")
    parser.add_argument("--demo", action="store_true", help="Gera PDF com dados de exemplo")
    args = parser.parse_args()

    ticker = args.ticker
    output = args.output or f"{ticker}_Initiation_Coverage_{datetime.now().strftime('%Y%m%d')}.pdf"

    if args.demo:
        payload = demo_payload(ticker)
        print(f"🚀 Modo demonstração ativado para: {ticker}")
    else:
        payload = load_payloads(args.payload_dir)
        payload["ticker"] = ticker

    build_pdf(payload, ticker, output)


if __name__ == "__main__":
    main()
