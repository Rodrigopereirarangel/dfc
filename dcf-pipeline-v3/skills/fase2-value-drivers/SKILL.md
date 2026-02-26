---
name: "Fase 2 — Decomposição de Value Drivers"
description: |
  ROIC/ROIIC, fade rate, Red Queen capex, unit economics e tornado chart.
  Triggers: "drivers de valor", "ROIC", "fade", "capex", "Red Queen"
---

# FASE 2 — DECOMPOSIÇÃO DE VALUE DRIVERS

## Passo 2.1 — ROIC, Fade Rate e ROE Decomposition

**Ação:**
1. ROIC ajustado para intangíveis: NOPAT ajustado / Invested Capital ajustado.
2. Decompor: ROIC = NOPAT Margin × Capital Turnover (e sub-componentes).
3. ROIIC (Return on Incremental Invested Capital) dos últimos 3-5 anos.
4. Estimar fade rate: anos até ROIC → WACC (dados empíricos do setor). `fade rate = ln(2) / half-life empírica`.
5. **Fade por segmento**: se múltiplos segmentos, estimar fade de cada um separadamente. Consolidado = média ponderada.
6. Competitive Advantage Period (CAP) implícito no preço atual.
7. Medir pressão concorrencial por segmento e projetar curva de fade ROIC → WACC.
8. Decomposição ROE = ROIC + (ROIC − Kd_after_tax) × D/E → leverage ajuda ou atrapalha?

**Referências:**
- **P24** (Return on Invested Capital): 6 variações de cálculo. ROIIC = ΔNOPAT / ΔIC.
- **P19** (ROIC and Investment Process): persistência ROIC 1990-2022 por setor. Half-life empírica.
- **Livro 06/84** (Expectations Investing): CAP, fade rates.
- **Livro 85** (Competition Demystified): pressão competitiva por tipo de mercado.
- **Livro 86** (Lundholm/Sloan): Decomposição ROE.
- **P41** (Math of Value and Growth): ROIIC framework.

**Output:** Gráfico projetado de Fade ROIC vs WACC no tempo. CAP implícito.

---

## Passo 2.2 — Capex Manutenção vs. Crescimento (Red Queen)

**Ação:**
1. Separar capex por 3 métodos:
   - Método 1: D&A ajustada por inflação como proxy.
   - Método 2: Capex necessário para manter receita flat (Red Queen).
   - Método 3: Management guidance decomposition (com haircut).
2. Asset age analysis: PP&E líquido / PP&E bruto → se < 0.4 = sub-investimento → 🟠
3. Separar SGA: componente de investimento vs. manutenção.
4. **CAPEX_total = CAPEX_manutenção + CAPEX_expansão em todos os anos** — se não fecha, investigar.

**Referências:**
- **P31** (Red Queen): framework completo, 3 métodos.
- **P32** (Categorizing for Clarity): separação investment vs. maintenance em SGA.
- **Livro 87** (McKinsey): reinvestment chapter.

**Output:** Tabela Capex Manutenção vs Expansão (anual).

---

## Passo 2.3 — Unit Economics e Dinâmica de Clientes

**Ação:**
1. Margem incremental.
2. Operating leverage (DOL).
3. Se aplicável: LTV, CAC, LTV/CAC, payback period.
4. **Churn rate, cohort retention curves e NRR (Net Revenue Retention)** — se NRR > 100%, expansão orgânica; se < 90%, red flag.
5. Custo operacional e impacto em margem segmentada.

**Referências:**
- **P36** (Customer Economics): LTV, CAC, cohort, NRR.
- **Livro 06/84** (Expectations Investing): Cap. 4.
- **Livro 77** (O Preço é o Lucro).

---

## Passo 2.4 — Sensibilidade dos Drivers e Causalidade

**Ação:**
1. Tornado chart: quais variáveis mais impactam o valor?
2. Distinguir correlação de causalidade (DAG - grafo acíclico dirigido).
3. **Filtrar Sinal do Ruído (L54)**: premissas não podem ser forjadas sobre correlações espúrias temporárias.
4. Identificar os 2-3 drivers que "fazem ou quebram" o case.

**Referências:**
- **Livro 52** (The Book of Why, Pearl): Cap. 1-3 — Causalidade vs Correlação.
- **Livro 54** (The Signal and the Noise, Nate Silver).
- **Livro 44** (Tjia): sensitivity analysis.

**Output:** Tornado Chart top 5 drivers. Lista dos 2-3 drivers críticos.
