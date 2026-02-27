#!/usr/bin/env python3
"""
generate_pdf.py — DCF Pipeline v4.1 (Markdown to PDF Engine)
Gera relatório PDF institucional através de HTML+CSS renderizado via Headless Browser.

Vantagens sobre ReportLab: Suporte nativo e perfeito a marcação rica do Markdown (Negrito, 
Blockquotes, Tabelas dimensionadas automaticamente, parágrafos extensos sem corte).

Uso:
    python generate_pdf.py --ticker PSSA3 --report "output_payloads/PSSA3_report.md" --output "PSSA3_Initiation.pdf"
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
    
    /* Semáforos nas tabelas */
    td:contains("VERDE"), td:contains("APROVADO"), td:contains("Compra") { color: var(--verde); font-weight: bold; }
    td:contains("VERMELHO"), td:contains("REPROVADO"), td:contains("Vender") { color: var(--vermelho); font-weight: bold; }
    td:contains("AMARELO"), td:contains("Manter") { color: var(--amarelo); font-weight: bold; }

    /* Imagens (Gráficos) */
    img { max-width: 100%; height: auto; display: block; margin: 15pt auto; border: 1px solid #eee; border-radius: 4px; }
    
    /* Disclaimer */
    .disclaimer { font-size: 8pt; color: #888; border-top: 1px solid #ddd; padding-top: 10pt; margin-top: 40pt; text-align: justify; }

    /* Síntese Institucional (Caixas Destacadas) */
    .sintese-box { border: 2px solid var(--azul-marinho); padding: 15pt; margin: 20pt 0; background-color: #F8FBFF; border-left: 6px solid var(--azul-marinho); }
    .sintese-box p { margin: 5pt 0; font-weight: 500; font-size: 10pt; }
</style>
"""

# ─────────────────────────────────────────────────────────────────
#  MAIN RENDERER LOGIC
# ─────────────────────────────────────────────────────────────────
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
def main():
    parser = argparse.ArgumentParser(description="Markdown to PDF Institucional via Headless Browser.")
    parser.add_argument("--ticker", required=True, help="Ticker do ativo (ex: PSSA3)")
    parser.add_argument("--report", required=True, help="O arquivo markdown master contendo a narrativa completa.")
    parser.add_argument("--output", help="O arquivo PDF de saída.")
    args = parser.parse_args()

    ticker = args.ticker
    report_file = args.report
    pdf_output = args.output or f"{ticker}_Initiation_Coverage.pdf"
    html_temp = f"tmp_{ticker}_render.html"

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
        // JS opcional para injeção de CSS em runtime (p.e. formatar blocos de sintese)
        document.querySelectorAll("h3").forEach(item => {{
            if(item.innerText.includes("SÍNTESE INSTITUCIONAL")) {{
                let nextList = item.nextElementSibling;
                if(nextList && nextList.tagName === "UL") {{
                    let box = document.createElement("div");
                    box.className = "sintese-box";
                    box.appendChild(item.cloneNode(true));
                    box.appendChild(nextList.cloneNode(true));
                    item.parentNode.insertBefore(box, item);
                    item.style.display = 'none';
                    nextList.style.display = 'none';
                }}
            }}
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
