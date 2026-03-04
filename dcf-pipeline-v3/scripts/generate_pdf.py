#!/usr/bin/env python3
"""
generate_pdf.py — DCF Pipeline v4.0 (Markdown to PDF Engine)
Gera relatório PDF institucional através de HTML+CSS renderizado via Headless Browser.

Vantagens sobre ReportLab: Suporte nativo e perfeito a marcação rica do Markdown (Negrito,
Blockquotes, Tabelas dimensionadas automaticamente, parágrafos extensos sem corte).

Uso:
    python generate_pdf.py --ticker PSSA3 --report "output_payloads/PSSA3_report.md" --output "PSSA3_Initiation.pdf"
    python generate_pdf.py --ticker PSSA3 --demo          # Gera PDF de demonstração sem arquivo de análise
"""

import argparse
import json
import os
import sys
import re
from datetime import datetime
from pathlib import Path

# Tentativa de importar bibliotecas vitais
try:
    import markdown
    from bs4 import BeautifulSoup
except ImportError:
    print("❌ Faltam dependências. Rode: pip install markdown beautifulsoup4 playwright")
    sys.exit(1)

# Importa as rotinas de gráficos que já tínhamos (elas continuam gerando PNG)
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# ─────────────────────────────────────────────────────────────────
#  ESTILOS GLOBAIS (MATPLOTLIB) - Reaproveitando do v4.0
# ─────────────────────────────────────────────────────────────────
PAL = {
    "azul":    "#003366", "azul_m":  "#336699", "cinza":   "#4A4A4A",
    "cinza_l": "#A0A0A0", "ambar":   "#CBA052", "verde":   "#27AE60",
    "amarelo": "#F1C40F", "vermelho":"#C0392B", "verm_esc":"#8B0000",
}

def set_bloomberg_style():
    plt.rcParams.update({
        "figure.facecolor": "white", "axes.facecolor": "white",
        "axes.edgecolor": PAL["cinza_l"], "axes.grid": True,
        "grid.color": PAL["cinza_l"], "grid.linewidth": 0.4, "grid.alpha": 0.4,
        "axes.spines.top": False, "axes.spines.right": False, "axes.spines.left": False,
        "xtick.color": PAL["cinza"], "ytick.color": PAL["cinza"],
        "font.family": "DejaVu Sans", "font.size": 9,
        "axes.titlesize": 10, "axes.titleweight": "bold", "axes.titlecolor": PAL["azul"],
        "legend.frameon": False, "legend.loc": "upper left", "legend.fontsize": 8,
    })

# (Aqui manteríamos as func plot_radar_porter, etc do arquivo anterior se o json payload for acionado)
# Para simplificar o novo motor, o script atual se apoiará na capacidade do Markdown de já conter 
# embeds ou focará especificamente em converter O TEXTO rico. 
# Se a tool do assistente usa o template "output-dcf-completo.md", ele já cria a matriz de narrativa completa.

# ─────────────────────────────────────────────────────────────────
#  CSS INSTITUCIONAL (BASEADO NO ESTUDO BLOOMBERG/GOLDMAN)
# ─────────────────────────────────────────────────────────────────
INSTITUTIONAL_CSS = """
<style>
    @page { margin: 20mm 15mm 20mm 15mm; size: A4; }
    
    :root {
        --azul-marinho: #003366; --ambar: #CBA052;
        --cinza-texto: #333333; --cinza-claro: #F5F5F5;
        --fonte-corpo: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        --fonte-titulo: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        --verde: #27AE60; --vermelho: #C0392B; --amarelo: #F1C40F;
    }

    body {
        font-family: var(--fonte-corpo);
        color: var(--cinza-texto);
        line-height: 1.5;
        font-size: 10.5pt;
        background-color: white;
    }

    h1 { color: var(--azul-marinho); font-size: 18pt; border-bottom: 2px solid var(--azul-marinho); padding-bottom: 5px; margin-top: 30pt; page-break-after: avoid; }
    h2 { color: var(--azul-marinho); font-size: 14pt; margin-top: 20pt; page-break-after: avoid; }
    h3 { color: var(--ambar); font-size: 12pt; margin-top: 15pt; page-break-after: avoid; }
    
    /* Cover Page Elements */
    .cover-page { text-align: center; margin-top: 100pt; padding: 40pt; background-color: #001F3F; color: white; border-radius: 8px; page-break-after: always; }
    .cover-title { font-size: 32pt; color: var(--ambar); margin-bottom: 10pt; font-weight: bold; }
    .cover-subtitle { font-size: 16pt; margin-bottom: 30pt; font-weight: 300; }
    .cover-rec { font-size: 24pt; font-weight: bold; padding: 10px 20px; border: 2px solid white; display: inline-block; margin-bottom: 30pt; }
    
    .cover-metrics { font-size: 12pt; margin-bottom: 30pt; color: #E0E0E0; line-height: 1.8;}
    
    /* Blockquotes para Narrativas */
    blockquote {
        border-left: 4px solid var(--ambar);
        margin: 15pt 0; padding: 10pt 15pt;
        background-color: var(--cinza-claro);
        font-style: normal; font-size: 10pt;
        color: #555; border-radius: 0 4px 4px 0;
    }
    blockquote p { margin: 0 0 8pt 0; }
    blockquote p:last-child { margin-bottom: 0; }

    /* Tabelas */
    table { width: 100%; border-collapse: collapse; margin: 15pt 0; font-size: 9pt; }
    th { background-color: var(--azul-marinho); color: white; padding: 8pt; text-align: left; font-weight: bold; }
    td { padding: 8pt; border-bottom: 1px solid #ddd; }
    tr:nth-child(even) { background-color: var(--cinza-claro); }
    
    /* Status semáforo — aplicado via JS (CSS :contains() não é suportado em browsers modernos) */
    .status-verde  { color: var(--verde);    font-weight: bold; }
    .status-verm   { color: var(--vermelho); font-weight: bold; }
    .status-ambar  { color: var(--amarelo);  font-weight: bold; }

    /* Imagens (Gráficos) */
    img { max-width: 100%; height: auto; display: block; margin: 15pt auto; border: 1px solid #eee; border-radius: 4px; }
    
    /* Disclaimer */
    .disclaimer { font-size: 8pt; color: #888; border-top: 1px solid #ddd; padding-top: 10pt; margin-top: 40pt; text-align: justify; }

    /* Síntese Institucional (Caixas Destacadas) */
    .sintese-box { border: 2px solid var(--azul-marinho); padding: 15pt; margin: 20pt 0; background-color: #F8FBFF; border-left: 6px solid var(--azul-marinho); }
    .sintese-box p { margin: 5pt 0; font-weight: 500; font-size: 10pt; }

    /* Containers de Gráficos Plotly Inline */
    .chart-container { margin: 20pt 0; page-break-inside: avoid; border: 1px solid #e0e0e0; border-radius: 6px; overflow: hidden; }
    .chart-caption { background-color: var(--azul-marinho); color: white; padding: 6pt 12pt; margin: 0; font-size: 9pt; }
    .chart-caption a { color: var(--ambar); text-decoration: none; }
    .chart-container .plotly-graph-div { min-height: 350px; }
</style>
"""

# ─────────────────────────────────────────────────────────────────
#  MAIN RENDERER LOGIC
# ─────────────────────────────────────────────────────────────────

# Mapeamento fase → descrição do gráfico (para legenda no PDF)
CHART_LABELS = {
    "F0":  "Análise Competitiva — 5 Forças + Moat Radar",
    "F1A": "Auditoria Contábil — Waterfall Normalização",
    "F1B": "Auditoria Contábil — ROE DuPont vs COE",
    "F2A": "Value Drivers — Fade ROIC → WACC",
    "F2B": "Value Drivers — Tornado Chart",
    "F25": "Gestão — Capital Allocation 10 Anos",
    "F3":  "Projeções — FCFF vs Lucro Recorrente",
    "F4":  "WACC — Term Structure de Desconto",
    "F5":  "Valor Terminal — Comparação 4 Métodos",
    "F6A": "Valuation — Football Field",
    "F6B": "Valuation — Heatmap Sensibilidade 7×7",
    "F7":  "Stress Test — Monte Carlo KDE",
    "F8A": "Decisão — Conviction Score",
    "F8B": "Decisão — Timeline Catalisadores",
}


def collect_chart_htmls(payloads_dir: str, ticker: str) -> dict:
    """
    Varre output_payloads/ procurando por arquivos grafico_F*.html gerados pelo
    render_inline_dataviz.py. Retorna dict: {fase_key: caminho_absoluto_html}.
    """
    charts = {}
    if not os.path.isdir(payloads_dir):
        return charts

    import glob
    pattern = os.path.join(payloads_dir, f"grafico_F*.html")
    for path in glob.glob(pattern):
        fname = os.path.basename(path)                  # ex: grafico_F6A.html
        fase_key = fname.replace("grafico_", "").replace(".html", "").upper()
        charts[fase_key] = os.path.abspath(path)

    # Também aceita o ticker como prefixo: PSSA3_grafico_F0.html
    pattern2 = os.path.join(payloads_dir, f"{ticker}_grafico_F*.html")
    for path in glob.glob(pattern2):
        fname = os.path.basename(path)
        fase_key = fname.replace(f"{ticker}_grafico_", "").replace(".html", "").upper()
        charts[fase_key] = os.path.abspath(path)

    return charts


def inject_charts_into_html(body_html: str, charts: dict) -> str:
    """
    Para cada fase com gráfico disponível, injeta o conteúdo do HTML Plotly
    inline após o cabeçalho h2/h3 correspondente, dentro de um container responsivo.

    Os gráficos são embutidos como <div> inline (não iframe) para que o Playwright
    consiga renderizá-los corretamente no PDF.
    """
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(body_html, "html.parser")

    # Mapa de keywords que identificam cada seção no markdown convertido
    FASE_KEYWORDS = {
        "F0":  ["fase 0", "inteligência competitiva", "enquadramento", "porter"],
        "F1A": ["fase 1", "auditoria contábil", "normaliz"],
        "F1B": ["roe", "dupont", "decomposição"],
        "F2A": ["fade", "roic", "value drivers", "fase 2"],
        "F2B": ["tornado", "sensibilidade dos drivers"],
        "F25": ["fase 2.5", "gestão", "capital allocation", "management"],
        "F3":  ["fase 3", "projeção", "fcff", "fluxo de caixa"],
        "F4":  ["fase 4", "wacc", "taxa de desconto"],
        "F5":  ["fase 5", "valor terminal", "terminal value"],
        "F6A": ["fase 6", "agregação", "football field", "triangulação"],
        "F6B": ["heatmap", "sensibilidade", "7×7", "7x7"],
        "F7":  ["fase 7", "stress test", "monte carlo"],
        "F8A": ["fase 8", "conviction", "decisão", "sizing"],
        "F8B": ["catalisadores", "timeline", "kelly"],
    }

    injected = set()

    for fase_key, chart_path in charts.items():
        if fase_key in injected:
            continue

        # Ler o HTML do gráfico Plotly
        try:
            with open(chart_path, "r", encoding="utf-8") as f:
                chart_html = f.read()
        except Exception:
            continue

        # Extrair apenas o <body> do HTML do gráfico (evita <html> duplicado)
        chart_soup = BeautifulSoup(chart_html, "html.parser")
        body = chart_soup.find("body")
        chart_content = str(body) if body else chart_html

        # Construir bloco de injeção
        label = CHART_LABELS.get(fase_key, f"Gráfico {fase_key}")
        abs_path = chart_path.replace("\\", "/")
        chart_block = (
            f'<div class="chart-container" id="chart-{fase_key}">'
            f'<p class="chart-caption"><strong>📊 {label}</strong> '
            f'<a href="file:///{abs_path}" target="_blank">[Abrir Interativo]</a></p>'
            f'{chart_content}'
            f'</div>'
        )

        # Encontrar o heading mais próximo no HTML que mencione keywords da fase
        keywords = FASE_KEYWORDS.get(fase_key, [])
        best_heading = None
        for tag in soup.find_all(["h1", "h2", "h3"]):
            tag_text = tag.get_text(strip=True).lower()
            if any(kw in tag_text for kw in keywords):
                best_heading = tag
                break

        if best_heading:
            # Inserir o bloco após o próximo sibling (não imediatamente no heading)
            chart_node = BeautifulSoup(chart_block, "html.parser")
            best_heading.insert_after(chart_node)
            injected.add(fase_key)

    return str(soup)


def markdown_to_html(md_text):
    """Converte markdown limpo para HTML usando biblioteca oficial e extensões."""
    # Pré-processamento customizado para injetar classes em certos elementos da Síntese
    md_text = md_text.replace("╔══════════════════════════════════════════════════════════════════╗", "")
    md_text = md_text.replace("║  📌 SÍNTESE INSTITUCIONAL", "### 📌 SÍNTESE INSTITUCIONAL")
    md_text = md_text.replace("╚══════════════════════════════════════════════════════════════════╝", "")

    # Processando "§1 ... " para listas
    md_text = re.sub(r'(§[1-5].*)', r'- **\1**', md_text)

    html = markdown.markdown(md_text, extensions=['tables', 'fenced_code', 'nl2br'])
    return html

def create_cover_page(ticker, md_text):
    """Extrai meta-dados do header do Markdown ou gera Capa Padrão."""
    # Isso é um fallback inteligente. Um script refinado leria do payload json.
    rec = "ANÁLISE INICIADA"
    fv = "—"
    curr = "—"
    score = "—"
    
    if "Recomendação |" in md_text:
        match = re.search(r'Recomendação \|\s*([A-Za-z]+)', md_text)
        if match: rec = match.group(1).upper()
    if "Expected Value" in md_text:
        match = re.search(r'Expected Value.*?\|\s*(R\$[0-9,\.]+)', md_text)
        if match: fv = match.group(1)
    if "Preço Atual" in md_text:
        match = re.search(r'Preço Atual.*?\|\s*(R\$[0-9,\.]+)', md_text)
        if match: curr = match.group(1)
    if "Conviction Score" in md_text:
        match = re.search(r'Conviction Score.*?\|\s*([0-9,\.]+\/\d+)', md_text)
        if match: score = match.group(1)
        
    date_str = datetime.now().strftime("%d de %B de %Y")
    
    cover = f"""
    <div class="cover-page">
        <div class="cover-subtitle">DCF Pipeline v4.0 - Institucional</div>
        <div class="cover-title">{ticker}</div>
        <div class="cover-rec">{rec}</div>
        <div class="cover-metrics">
            <strong>Preço Alvo (FV):</strong> {fv} &nbsp;|&nbsp; 
            <strong>Preço Atual:</strong> {curr} <br><br>
            <strong>Conviction Score:</strong> {score}
        </div>
        <div style="font-size:10pt; margin-top:100pt; color:#A0A0A0;">Data da Emissão: {date_str}</div>
    </div>
    """
    return cover

def html_to_pdf_playwright(html_file, pdf_file):
    """Usa Chromium via Playwright para renderizar HTML perfeitamente para PDF corporativo."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("❌ Playwright não está instalado. Tente: pip install playwright && playwright install chromium")
        return False
        
    try:
        with sync_playwright() as p:
            # Baixa e lança um browser invisível
            browser = p.chromium.launch()
            page = browser.new_page()
            
            # Converte caminho local absoluto em URI
            abs_path = "file:///" + os.path.abspath(html_file).replace("\\", "/")
            page.goto(abs_path)
            
            # Emula a folha de mídia e injeta margens pelo Chromium
            page.emulate_media(media="print")
            page.pdf(
                path=pdf_file,
                format="A4",
                print_background=True,
                margin={"top": "20mm", "bottom": "20mm", "left": "15mm", "right": "15mm"},
                display_header_footer=True,
                header_template="<div style='font-size:8px; width:100%; text-align:right; margin-right:15mm; color:#888;'>DCF Pipeline v4.0 Institucional</div>",
                footer_template="<div style='font-size:8px; width:100%; text-align:center; color:#888;'>Página <span class='pageNumber'></span> de <span class='totalPages'></span></div>"
            )
            browser.close()
        return True
    except Exception as e:
        print(f"❌ Erro ao usar Playwright: {e}")
        return False

# ─────────────────────────────────────────────────────────────────
#  FLOW PRINCIPAL
# ─────────────────────────────────────────────────────────────────
DEMO_MD = """# {ticker} — DCF Pipeline v4.0 Demo

## ⚠️ Relatório de Demonstração

Este PDF foi gerado com o flag `--demo` para validar o pipeline de renderização.
Substitua por `--report output_payloads/{ticker}_report.md` após concluir a análise completa.

| Componente | Status |
|---|---|
| PDF Engine (Playwright) | ✅ Funcionando |
| CSS Institucional | ✅ Aplicado |
| Markdown Parser | ✅ Operacional |
| Coloração de Status | ✅ Testada |

## FASE 0 — Exemplo de Template

**BLOCO 1 — Diagnóstico Executivo**
| Campo | Valor | Status | Tendência |
|---|---|---|---|
| Métrica Demo | 100 | ✅ | ↗️ |
| Métrica 2 | 22% | 🟠 | → |
| Métrica 3 | -5% | 🔴 | ↘️ |

> **Vetor Demo:** Claim: Este é um PDF de demonstração. Evidence: Flag --demo utilizado. Implication: Nenhuma análise real foi gerada.

╔══════════════════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — Demo                                 ║
╚══════════════════════════════════════════════════════════════════╝
§1 Pipeline de PDF funcionando corretamente.
§2 Sem impacto em fair value — análise demo.
§3 **FATO** — este é um arquivo de teste.
§4 Executar `/dfc {ticker}` para análise completa.
§5 Nenhuma assimetria identificada neste demo.
"""


def main():
    parser = argparse.ArgumentParser(description="Markdown to PDF Institucional via Headless Browser.")
    parser.add_argument("--ticker", required=True, help="Ticker do ativo (ex: PSSA3)")
    parser.add_argument("--report", help="O arquivo markdown master contendo a narrativa completa.")
    parser.add_argument("--output", help="O arquivo PDF de saída.")
    parser.add_argument("--demo", action="store_true", help="Gera PDF de demonstração sem arquivo de análise.")
    args = parser.parse_args()

    ticker = args.ticker
    pdf_output = args.output or f"{ticker}_Initiation_Coverage.pdf"
    html_temp = f"tmp_{ticker}_render.html"

    # Modo demo: usa conteúdo embutido sem necessitar de arquivo externo
    if args.demo:
        print(f"🧪 Modo --demo ativado para {ticker}. Gerando PDF de validação...")
        md_content = DEMO_MD.format(ticker=ticker)
    else:
        report_file = args.report
        if not report_file:
            print("❌ Informe --report <arquivo.md> ou use --demo para modo de demonstração.", file=sys.stderr)
            sys.exit(1)
        if not os.path.exists(report_file):
            print(f"❌ O arquivo de report '{report_file}' não foi encontrado.")
            print("💡 Você precisa garantir que a ferramenta salvou o output (texto de análise) em um arquivo na pasta output_payloads/ antes de chamar este script.")
            sys.exit(1)
        print("📖 Lendo conteúdo da análise em Markdown...")
        with open(report_file, 'r', encoding='utf-8') as f:
            md_content = f.read()

    print("🎨 Renderizando HTML...")
    # 1. Capa
    cover_html = create_cover_page(ticker, md_content)

    # 2. Corpo (Parser)
    body_html = markdown_to_html(md_content)

    # 3. Injetar gráficos Plotly (se existirem em output_payloads/)
    payloads_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output_payloads")
    charts = collect_chart_htmls(payloads_dir, ticker)
    if charts:
        print(f"📊 {len(charts)} gráfico(s) encontrado(s) — injetando no HTML...")
        body_html = inject_charts_into_html(body_html, charts)
    else:
        print("ℹ️  Nenhum gráfico encontrado em output_payloads/. PDF será gerado sem dashboards.")
    
    disclaimer = "<div class='disclaimer'>Esta análise é produzida para fins educacionais e pesquisa fundamentalista. Não constitui uma oferta oficial nem recomendação regulada de compra ou venda de ações. Investimentos envolvem riscos de perda de capital.</div>"

    # Montagem do Arquivo Mestre HTML
    full_html = f"""<!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>{ticker} — Initiation Coverage</title>
        {INSTITUTIONAL_CSS}
    </head>
    <body>
        {cover_html}
        <div class="body-content">
            {body_html}
        </div>
        {disclaimer}
        
    <script>
        // 1. Formatar blocos SÍNTESE INSTITUCIONAL em caixa destacada
        document.querySelectorAll("h3").forEach(item => {{
            if(item.innerText.includes("SÍNTESE INSTITUCIONAL")) {{
                let nextEl = item.nextElementSibling;
                if(nextEl && (nextEl.tagName === "UL" || nextEl.tagName === "P")) {{
                    let box = document.createElement("div");
                    box.className = "sintese-box";
                    box.appendChild(item.cloneNode(true));
                    box.appendChild(nextEl.cloneNode(true));
                    item.parentNode.insertBefore(box, item);
                    item.style.display = 'none';
                    nextEl.style.display = 'none';
                }}
            }}
        }});

        // 2. Colorir células de tabela por conteúdo (substitui CSS :contains() não suportado)
        const VERDE_KW  = ["VERDE", "APROVADO", "Compra", "✅", "OK"];
        const VERM_KW   = ["VERMELHO", "REPROVADO", "Vender", "❗", "REPROV"];
        const AMBAR_KW  = ["AMARELO", "Manter", "ATENÇÃO", "🟠"];

        document.querySelectorAll("td").forEach(td => {{
            const t = td.innerText.trim();
            if (VERDE_KW.some(k => t.includes(k)))      td.classList.add("status-verde");
            else if (VERM_KW.some(k => t.includes(k)))  td.classList.add("status-verm");
            else if (AMBAR_KW.some(k => t.includes(k))) td.classList.add("status-ambar");
        }});
    </script>
    </body>
    </html>
    """

    with open(html_temp, 'w', encoding='utf-8') as f:
        f.write(full_html)
        
    print(f"✅ HTML compilado. Chamando renderizador Chromium para converter em {pdf_output}...")

    success = html_to_pdf_playwright(html_temp, pdf_output)
    if success:
        print(f"🎯 PDF Institucional gerado perfeitamente com todas as narrativas em: {pdf_output}")
        # Limpar temp
        try: os.remove(html_temp)
        except: pass
    else:
        print("⚠️ Falha na geração do PDF via Chromium. O arquivo HTML intermediário foi preservado.")
        print(f"👉 Você pode abrir '{html_temp}' no Chrome/Edge e usar 'Imprimir -> Salvar como PDF' manualmente. Isso garante a mesma estética perfeita.")

if __name__ == "__main__":
    main()
