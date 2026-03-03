#!/usr/bin/env python3
"""
render_inline_dataviz_plotly.py — Renderiza Dashboards Dinâmicos em HTML via Plotly
Gera gráficos ricos em detalhamento (Dicas de Ferramenta, Zoom) com design Bloomberg/Goldman.

Uso:
    python scripts/render_inline_dataviz_plotly.py --payload "caminho/do/payload.json" --output "caminho/do/grafico.html" --ticker "TICKER"
"""

import argparse
import json
import os
import sys

try:
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
except ImportError:
    print("❌ Faltam dependências. Rode: pip install plotly pandas")
    sys.exit(1)

# ─────────────────────────────────────────────────────────────────
#  ESTÉTICA E TEMPLATE UNIFICADO (BLOOMBERG-LIKE)
# ─────────────────────────────────────────────────────────────────
PAL = {
    "azul":    "#003366", "azul_m":  "#336699", "cinza":   "#4A4A4A",
    "cinza_l": "#A0A0A0", "ambar":   "#CBA052", "verde":   "#27AE60",
    "amarelo": "#F1C40F", "vermelho":"#C0392B", "verm_esc":"#8B0000",
}

TEMPLATE_FIG = go.layout.Template(
    layout=go.Layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(family="Helvetica Neue, Arial, sans-serif", color=PAL["cinza"]),
        title=dict(font=dict(family="Helvetica Neue, Arial, sans-serif", color=PAL["azul"], size=16)),
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=True,
            linecolor=PAL["cinza_l"],
            linewidth=1,
            tickfont=dict(color=PAL["cinza"])
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(200, 200, 200, 0.3)',
            gridwidth=1,
            zeroline=False,
            showline=False,
            tickfont=dict(color=PAL["cinza"])
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
)

# ─────────────────────────────────────────────────────────────────
#  FUNÇÕES GERADORAS ESPECÍFICAS
# ─────────────────────────────────────────────────────────────────
def plot_f3_fcff(data, output_path, ticker):
    """Gera gráfico interativo de barras FCFF vs LPA (Fase 3)."""
    fcff_data = data.get("fcff_projetado_base_5_anos", data.get("fcff_projetado_base", []))
    if not fcff_data:
        return False

    anos = [str(d.get("ano", "")) for d in fcff_data]
    fcff = [d.get("fcff", 0) for d in fcff_data]
    lpa = [d.get("lucro_recorrente", 0) for d in fcff_data]
    
    fig = go.Figure()
    
    # Barra 1: FCFF
    fig.add_trace(go.Bar(
        x=anos, 
        y=fcff, 
        name='FCFF Projetado', 
        marker_color=PAL["azul"],
        text=[f'R$ {val:.1f}' for val in fcff],
        textposition='outside'
    ))
    
    # Barra 2: Lucro Recorrente
    fig.add_trace(go.Bar(
        x=anos, 
        y=lpa, 
        name='Lucro Recorrente Projetado', 
        marker_color=PAL["ambar"],
        text=[f'R$ {val:.1f}' for val in lpa],
        textposition='outside'
    ))

    fig.update_layout(
        template=TEMPLATE_FIG,
        title=f'{ticker}: Matriz de Geração de Caixa Futuro (FCFF vs Lucro)',
        barmode='group',
        yaxis_title="R$ milhões",
        hovermode="x unified"
    )

    fig.write_html(output_path, include_plotlyjs="cdn")
    return True

def plot_f6_football_field(data, output_path, ticker):
    """Gera o Football Field interativo para predições do Valor Justo (Fase 6)."""
    triangulacao = data.get("triangulacao", [])
    if not triangulacao:
         return False

    metodos = [d.get("metodo", "...") for d in triangulacao]
    pior = [d.get("pior_cenario", 0) for d in triangulacao]
    base = [d.get("cenario_base", 0) for d in triangulacao]
    otim = [d.get("melhor_cenario", 0) for d in triangulacao]
    preco_atual = data.get("preco_atual", None)
    
    fig = go.Figure()

    for i in range(len(metodos)):
        # Range total do Football Field (Base grossa)
        fig.add_trace(go.Scatter(
            x=[pior[i], otim[i]],
            y=[metodos[i], metodos[i]],
            mode='lines',
            line=dict(color=PAL["azul_m"], width=24),
            opacity=0.4,
            name=f'{metodos[i]} Range',
            showlegend=False,
            hoverinfo='skip'
        ))
        
        # Ponto Base
        fig.add_trace(go.Scatter(
            x=[base[i]],
            y=[metodos[i]],
            mode='markers+text',
            marker=dict(color=PAL["ambar"], size=12, symbol='diamond'),
            text=[f'<b>R$ {base[i]:.2f}</b>'],
            textposition='top center',
            name='Cenário Base',
            showlegend=(i == 0),
            hoverinfo='x+y'
        ))

        # Extremos (Anotações escondidas feitas visíveis no hover automático ou texto fixo)
        fig.add_annotation(x=pior[i], y=metodos[i], text=f'R$ {pior[i]:.2f}', showarrow=False, xanchor='right', xshift=-10, font=dict(size=10, color=PAL['cinza']))
        fig.add_annotation(x=otim[i], y=metodos[i], text=f'R$ {otim[i]:.2f}', showarrow=False, xanchor='left', xshift=10, font=dict(size=10, color=PAL['cinza']))

    if preco_atual and preco_atual > 0:
        fig.add_vline(x=preco_atual, line_width=2, line_dash="dash", line_color=PAL["vermelho"])
        fig.add_annotation(x=preco_atual, y=len(metodos)-0.5, text=f"Mercado Hoje: R${preco_atual:.2f}", showarrow=False, bgcolor="white", opacity=0.8, xanchor='left')

    fig.update_layout(
        template=TEMPLATE_FIG,
        title=f'{ticker}: Football Field Valuation (Agregação Central)',
        xaxis_title="Valor Intrínseco por Ação (R$)",
        yaxis=dict(type='category', autorange="reversed"),
        height=400 + (len(metodos)*40),
        margin=dict(l=150)
    )
    
    fig.write_html(output_path, include_plotlyjs="cdn")
    return True

def plot_generic_bar(data, output_path, ticker):
    """Gráfico interativo genérico minimalista."""
    labels, values = [], []
    
    for k, v in data.items():
        if isinstance(v, (int, float)) and not k.startswith("fase") and not isinstance(v, bool):
            labels.append(k.replace('_', ' ').title()[:20])
            values.append(v)
            if len(labels) > 8: break 
            
    if not labels:
        return False
        
    fig = go.Figure(go.Bar(
        x=values,
        y=labels,
        orientation='h',
        marker_color=PAL["azul"],
        text=[f'{v}' for v in values],
        textposition='outside'
    ))
    
    fig.update_layout(
        template=TEMPLATE_FIG,
        title=f'{ticker} - Key Metrics Snapshot',
        yaxis=dict(autorange="reversed")
    )

    fig.write_html(output_path, include_plotlyjs="cdn")
    return True

# ─────────────────────────────────────────────────────────────────
#  MAIN EXECUTION
# ─────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--payload", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--ticker", default="TICKER")
    args = parser.parse_args()

    if not os.path.exists(args.payload):
         print(f"❌ Erro: Arquivo {args.payload} não encontrado.")
         sys.exit(1)

    try:
        with open(args.payload, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ Erro ao ler JSON: {e}")
        sys.exit(1)

    fase = data.get("fase", "")
    os.makedirs(os.path.dirname(args.output) if os.path.dirname(args.output) else ".", exist_ok=True)

    success = False
    
    if "F3" in fase: success = plot_f3_fcff(data, args.output, args.ticker)
    elif "F6" in fase: success = plot_f6_football_field(data, args.output, args.ticker)
    else: success = plot_generic_bar(data, args.output, args.ticker)
            
    if success:
        print(f"✅ Dashboard Interativo renderizado em: {args.output}")
    else:
        print(f"⚠️ Sem dados óbvios para visualização gráfica na fase {fase}.")
        sys.exit(1)

if __name__ == "__main__":
    main()
