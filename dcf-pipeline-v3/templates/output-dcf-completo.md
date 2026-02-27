# DCF Pipeline v3 — Output Completo (Template v4.0)
# Ticker: [TICKER] | Data: [DATA] | Analista: DCF Pipeline v4.0

---

## 📋 HEADER

| Campo | Valor |
|---|---|
| Empresa | [NOME COMPLETO] |
| Ticker | [TICKER] |
| Recomendação | Compra / Manter / Vender |
| Expected Value (Fair Value) | R$X,XX |
| Preço Atual | R$X,XX |
| Upside/(Downside) | X,X% |
| Conviction Score | X,X/10 |
| Date | [DATA] |

---

## 📌 SUMÁRIO EXECUTIVO

> **Investment Thesis (§1 da Fase 0 condensado):**
> [1 parágrafo]

### Tabela de Cenários

| Cenário | Prob | Fair Value | Upside |
|---|---|---|---|
| Distress | X% | R$X | X% |
| Bear | X% | R$X | X% |
| Base | X% | R$X | X% |
| Bull | X% | R$X | X% |
| **Expected Value** | 100% | **R$X** | **X%** |

### Kelly & Sizing
| Conviction Score | Full Kelly | Half-Kelly | Posição Máxima |
|---|---|---|---|
| X,X/10 | X% | X% | X% portfólio |

### Top 3 Riscos | Top 3 Catalisadores
| Risco | Catalisador |
|---|---|
| [1] | [1] |
| [2] | [2] |
| [3] | [3] |

---

## FASE 0 — Inteligência Competitiva & Enquadramento

### Passo 0.1 — 5 Forças + Moat
> **BLOCO 1** — Diagnóstico Executivo (tabela de Forças)
> **BLOCO 2** — Narrativa por Vetor
> **BLOCO 3** — 📊 Radar Chart | Impacto Quantitativo
> **BLOCO 4** — Dilema Analítico
> **BLOCO 5** — Analogia Histórica

📌 Síntese §1–§5: [...]

```json
<!-- JSON_PAYLOAD F0_P01 aqui -->
```

### Passo 0.2 — Reverse DCF + MEROI
> [5 Blocos + Síntese]
```json
<!-- JSON_PAYLOAD F0_P02 aqui -->
```

### Passo 0.3 — Sentimento de Mercado
> [5 Blocos + Síntese]

### Passo 0.4 — Narrativa → Números (Pre-mortem)
> [5 Blocos + Síntese]

```json
<!-- JSON_PAYLOAD F0_COMPLETA aqui -->
```

---

## FASE 1 — Auditoria Contábil Forense

### Passo 1.1 — M-Score + Qualidade do Lucro
> **BLOCO 3** — 📊 Waterfall Lucro Reportado → Normalizado
📌 Síntese §1–§5: [...]

### Passo 1.2 — Normalização + ROE DuPont
> **BLOCO 3** — 📊 Barras DuPont com linha COE

### Passo 1.3 — 3-Statement Model
> **BLOCO 3** — 📊 Gráfico de Linhas Históricas

```json
<!-- JSON_PAYLOAD F1_COMPLETA aqui -->
```

---

## FASE 2 — Decomposição de Value Drivers

### Passo 2.1 — ROIC, Fade Rate, CAP
> **BLOCO 3** — 📊 Gráfico Fade ROIC→WACC (linhas convergentes + área verde/vermelha)

### Passo 2.2 — Capex Red Queen
> [5 Blocos + Síntese]

### Passo 2.3 — Unit Economics
> [5 Blocos + Síntese]

### Passo 2.4 — Tornado Chart
> **BLOCO 3** — 📊 Tornado Chart Horizontal (barras simétricas ±1σ)

```json
<!-- JSON_PAYLOAD F2_COMPLETA aqui -->
```

---

## FASE 2.5 — Análise da Gestão

### Passo 2.5.1 — Track Record Assertividade
> **BLOCO 3** — 📊 Barras Desvio vs. Guidance com linha haircut

### Passo 2.5.2 — Capital Allocation
> **BLOCO 3** — 📊 Stacked Bar 100% Capital Allocation 10A

### Passo 2.5.3 — Ramp-ups e Projetos
> **BLOCO 3** — 📊 S-Curves de Ramp-up por Projeto

```json
<!-- JSON_PAYLOAD F25_COMPLETA aqui -->
```

---

## FASE 3 — Projeção dos Fluxos de Caixa

### Passo 3.1–3.2 — Receita e Margens
> **BLOCO 3** — 📊 Gráfico Área (padrão Goldman Sachs: sólido histórico / hachurado projetado)

### Passo 3.3 — FCFF Projetado
> **BLOCO 3** — 📊 Barras Duplas FCFF vs Lucro Recorrente por ano

```json
<!-- JSON_PAYLOAD F3_COMPLETA aqui -->
```

---

## FASE 4 — Taxa de Desconto (WACC)

### Passo 4.1 — Custo do Equity (COE)
> **BLOCO 3** — 📊 Term Structure do WACC (linha escalonada + zona Penman)

### Passo 4.2 — WACC Consolidado
> **BLOCO 3** — 📊 Waterfall de Decomposição do COE (Rf + ERP + Beta + Prêmios)

```json
<!-- JSON_PAYLOAD F4_COMPLETA aqui -->
```

---

## ⭐ FASE 5A — Auditoria de Integração 360° (GATE)

### Resultado do GATE

| Check | Status | Detalhe |
|---|---|---|
| Chain Check | ✅/❗ | |
| Reconciliação Segmento | ✅/🟠 | |
| Loop Circular WACC | ✅/❗ | |
| Capex Integrity | ✅/🟠 | |
| Penman Test | ✅/🟠 | |
| **VEREDITO** | **✅ APROVADO / ❗ REPROVADO** | |

> **📊 Painel Semáforo:** Tabela com células coloridas por status

```json
<!-- JSON_PAYLOAD F5A_GATE aqui -->
```

---

## FASE 5 — Valor Terminal

### Comparação de Métodos de TV

| Método | Fair Value | TV/EV | Status |
|---|---|---|---|
| McKinsey CV | R$X | X% | |
| Gordon Growth | R$X | X% | |
| EPV (floor) | R$X | X% | |
| Exit Multiple | R$X | X% | |

> **📊 Bar Chart Comparativo de Métodos de TV**

```json
<!-- JSON_PAYLOAD F5_COMPLETA aqui -->
```

---

## FASE 6 — Agregação, Cenários & Bridge para Equity

### Bridge EV → Equity

| Item | Valor |
|---|---|
| EV | R$X bi |
| (−) Dívida Líquida | R$X bi |
| Equity Value | R$X bi |
| Shares (diluted) | X mi |
| **Fair Value/Ação** | **R$X** |

> **📊 Heatmap Térmico 7×7** (COE × g Terminal)  
> **📊 Bar Chart Cenários com Expected Value**

```json
<!-- JSON_PAYLOAD F6_COMPLETA aqui -->
```

---

## FASE 7 — Stress Test & Validação Cruzada

### Tabela de Triangulação

| Método | FV Mín | FV Ponto | FV Máx |
|---|---|---|---|
| DCF Base | R$X | R$X | R$X |
| EPV | R$X | R$X | R$X |
| Múltiplos | R$X | R$X | R$X |

> **📊 Football Field Valuation** (barras horizontais sobrepostas)  
> **📊 Monte Carlo KDE** com P5/P50/P95 e preço atual

```json
<!-- JSON_PAYLOAD F7_COMPLETA aqui -->
```

---

## FASE 8 — Decisão: Conviction & Sizing

> **📊 Conviction Score Disaggregation** (bar-chart horizontal por dimensão)  
> **📊 Timeline de Catalisadores** (gantt dos próximos 8 tri)

```json
<!-- JSON_PAYLOAD F8_COMPLETA aqui -->
```

---

## 📄 FASE 9 — Geração do PDF Institucional

**ATENÇÃO AGENTE:** Salve OBRIGATORIAMENTE este template preenchido na pasta `output_payloads/` com o formato `[TICKER]_report.md`. Em seguida execute o comando abaixo com a nova arquitetura Playwright:

```bash
python scripts/generate_pdf.py \
    --ticker [TICKER] \
    --report "output_payloads/[TICKER]_report.md" \
    --output "[TICKER]_Initiation_Coverage_[DATA].pdf"
```

Para testar/validar o PDF engine caso necessário:
```bash
python scripts/generate_pdf.py --ticker [TICKER] --demo
```

---

## ⚖️ DISCLAIMER

*Esta análise é produzida para fins educacionais e de pesquisa fundamentalista. Não constitui recomendação formal de investimento. Verifique as informações com fontes primárias antes de tomar decisões de alocação de capital.*
