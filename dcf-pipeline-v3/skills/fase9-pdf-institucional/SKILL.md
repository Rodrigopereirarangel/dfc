---
name: "Fase 9 — Empacotamento Institucional & Geração de PDF"
description: |
  Consolida toda a análise das Fases 0-8 em um relatório PDF de nível institucional.
  Triggers: "gerar PDF", "relatório final", "initiation report", "PDF"
---

# FASE 9 — EMPACOTAMENTO INSTITUCIONAL & GERAÇÃO DE PDF

> **Entradas:** JSON Payloads de todas as Fases 0-8.
> **Script:** `scripts/generate_pdf.py`

## 🎯 OBJETIVO

Consolidar toda a análise gerada nas Fases 0 a 8 e entregar um **Arquivo PDF de Nível Institucional**, visualmente equivalente a um relatório de iniciação de cobertura de banco de primeira linha (Goldman Sachs, BTG Pactual, Morgan Stanley).

---

## Passo 9.1 — Arquitetura do Relatório

**Estrutura Obrigatória do Documento:**

### Capa (Página 1)
- **Logo e Nome da Empresa / Ticker**
- **Recomendação:** Compra / Manter / Vender (em destaque, cor semáforo)
- **Preço Alvo (Expected Value):** R$X
- **Preço Atual:** R$X | **Upside/Downside:** X%
- **Conviction Score:** X/10
- **Data da Análise**
- **Investment Thesis:** 1 parágrafo (§1 da Síntese da Fase 0 compactado)

### Sumário Executivo (Página 2)
- Tabela de Cenários (Distress / Bear / Base / Bull / Expected Value)
- Tabela Triangulação (Football Field — versão compacta)
- Kelly Sizing e Recomendação de Posição
- Top 3 Riscos e Top 3 Catalisadores

### Corpo do Relatório (Páginas 3-N)
Uma seção por Fase (0→8), incluindo:
- Tabelas diagnósticas do BLOCO 1 de cada passo
- Narrativas de destaque do BLOCO 2 (blockquotes formatados)
- Gráficos do BLOCO 3 (gerados pelo script)
- Síntese §1-§5 de cada fase em caixa destacada
- Analogia Histórica (BLOCO 5) em caixa de nota lateral

### Rodapé Padrão em Cada Página
- Ticker | Data | "Análise Fundamentalista — DCF Pipeline v4.0"
- Number de página
- *Disclaimer: Esta análise não constitui recomendação formal de investimento.*

---

## Passo 9.2 — Gráficos Obrigatórios por Fase

| Fase | Gráfico Obrigatório | Tipo |
|---|---|---|
| F0 | Spider Chart (Vantagem Competitiva) | Radar |
| F1 | Waterfall Lucro Reportado → Normalizado | Cascata |
| F1 | ROE DuPont com linha COE | Barras + Linha |
| F2 | Fade ROIC → WACC por cenário | Linhas convergentes |
| F2 | Tornado Chart de Sensibilidade | Barras horizontais |
| F2.5 | Capital Allocation Stacked 10A | Barras empilhadas |
| F3 | Receita e Margem (histórico vs. projetado) | Área + Linha |
| F4 | Term Structure do WACC | Linha escalonada |
| F5 | Comparação de Métodos de TV | Barras horizontais |
| F6 | Football Field Valuation | Barras horizontais sobrepostas |
| F6 | Heatmap Sensibilidade 7×7 | Mapa de calor |
| F7 | Distribuição Monte Carlo (KDE) | KDE Plot |
| F8 | Conviction Score Disaggregation | Bar-chart horizontal |
| F8 | Timeline de Catalisadores | Gantt/Timeline |

---

## Passo 9.3 — Instruções de Tipografia e Paleta Institucional

**Paleta Oficial:**
```python
PALETA = {
    "azul_marinho": "#003366",     # Cor primária, barras principais
    "azul_medio": "#336699",       # Cor secundária, barras alternativas
    "cinza_ardosia": "#4A4A4A",    # Texto corpo, tabelas
    "cinza_claro": "#A0A0A0",      # Gridlines, linhas secundárias
    "ambar": "#CBA052",            # Destaques, Expected Value
    "verde_aprovado": "#27AE60",   # Status OK, retorno positivo
    "amarelo_atencao": "#F1C40F",  # Status atenção, zona neutra
    "vermelho_grave": "#C0392B",   # Status grave, retorno negativo
    "vermelho_escuro": "#8B0000",  # Barras negativas em cascata
    "branco": "#FFFFFF",           # Fundo padrão
    "fundo_capa": "#001F3F"        # Azul marinho escuro para capa
}
```

**Tipografia:**
- Fonte do documento: **Helvetica Neue** ou **Calibri** (via reportlab).
- Títulos de seção: Bold, 14pt, Azul Marinho.
- Corpo do texto: Regular, 10pt, Cinza Ardósia.
- Cabeçalhos de tabela: Bold, 9pt, fundo Azul Marinho, texto Branco.
- Linhas de tabela zebradas: alternando Branco e Cinza 5% (#F5F5F5).
- Anotações de gráfico: Light, 8pt, Cinza Ardósia.

**Estilo de Gráficos (padrão Bloomberg):**
- Sem gridlines verticais.
- Gridlines horizontais com 20% de opacidade (cinza claro).
- Legendas no topo esquerdo.
- Títulos acima do gráfico, fonte Bold 10pt.
- Sem bordas de quadro (spine removido) — apenas eixo X inferior.

---

## Passo 9.4 — Execução do Script

**Comando (via Playwright / motor HTML):**
```bash
# 1. Salve o output compilado das fases 0-8 em arquivo Markdown (ex: output_payloads/XXXX3_report.md)
# 2. Rode o script:

python scripts/generate_pdf.py \
    --ticker XXXX3 \
    --report "output_payloads/XXXX3_report.md" \
    --output "XXXX3_Initiation_Coverage_2026.pdf"
```

**Fallback (se o ambiente não tiver Playwright instalado):**
Certifique-se que executou o bootstrap:
```bash
python scripts/bootstrap.py
python scripts/generate_pdf.py --ticker XXXX3 --demo
```
O modo `--demo` gera um HTML corporativo com dados de exemplo.

---

```
╔══════════════════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — Fase 9 Completa                     ║
╚══════════════════════════════════════════════════════════════════╝
§1 O PDF consolida todo o trabalho analítico das Fases 0-8 em um único documento de referência.
§2 O relatório é o entregável final que pode ser compartilhado com comitê de investimentos.
§3 A qualidade depende diretamente da completude dos JSON Payloads exportados nas fases anteriores.
§4 Verificar que todos os 14 gráficos obrigatórios foram gerados antes de finalizar o PDF.
§5 Um PDF incompleto ou visualmente inferior ao padrão institucional é equivalente a não entregar.
```

**Referências:**
- `scripts/generate_pdf.py`: script Python autossuficiente.
- `references/base-rates.md`: dados para validação gráfica.
- Padrão visual: Goldman Sachs Equity Research / Bloomberg Intelligence.
