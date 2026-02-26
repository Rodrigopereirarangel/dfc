---
name: "Fase 3 — Projeção dos Fluxos de Caixa"
description: |
  Projeção bottom-up de receita, margens, FCFF e validação probabilística.
  Triggers: "projeção", "receita", "FCFF", "fluxo de caixa", "Monte Carlo"
---

# FASE 3 — PROJEÇÃO DOS FLUXOS DE CAIXA

> **Entradas obrigatórias desta fase:**
> - Modelo 3-Statement da Fase 1 (`skills/fase1-auditoria-contabil/SKILL.md`)
> - Capex Red Queen e ROIC fade da Fase 2 (`skills/fase2-value-drivers/SKILL.md`)
> - Haircut de management e projetos da Fase 2.5 (`skills/fase25-management/SKILL.md`)
> - Base rates em `references/base-rates.md`

> **Saídas consumidas por:**
> - Fase 4 (WACC) → Fase 5A (Auditoria 360°) → Fase 5 (Terminal Value)

> **Primariamente fundamentalista. Probabilístico apenas para validação.**
> **Fonte primária: ITR/DFP oficial — métricas operacionais nas Notas Explicativas.**

## Passo 3.1 — Projeção da Receita (Bottom-Up)

**Ação:**
1. Decompor receita por segmento/produto/geografia.
2. Para cada segmento, projetar via drivers operacionais:
   - Volume × Preço | Clientes × ARPU × Retention | Lojas × Vendas/Loja | TAM × Share × Penetração.
3. Incorporar ramp-ups (Passo 2.5.3) com haircut do management.
4. Outside view: comparar com base rates do setor.
5. **NUNCA macro-crescimento flat.** Projetar período de ramp-up e término explicitamente.

**Referências:**
- **Livro 87** (McKinsey): Cap. 12 — Forecasting Performance por UEN.
- **Livro 86** (Lundholm/Sloan): Pg. 153, 165+168 — projeção DRE e EPS.
- **P46** (TAM): top-down vs bottom-up TAM.
- **P35** (Base Rates por Intangíveis).
- **P01** (Bayes): prior + evidência → posterior.
- **P36** (Customer Economics): LTV/CAC para projeção receita.

---

## Passo 3.2 — Projeção de Margens e Custos

**Ação:**
1. Custo variável como % receita por segmento.
2. Custos fixos nominais + inflação + step functions.
3. Margem incremental projetada: consistente com histórica?
4. SGA: investment vs. maintenance.
5. Margem EBITDA e EBIT projetadas explicitamente.
6. Validar com peers e posição no ciclo.

**Referências:**
- **Livro 06/84** (Expectations Investing): Cap. 4.
- **Livro 86** (Lundholm/Sloan): Pg. 153.
- **P09** (Measuring the Moat): margens por indústria.

---

## Passo 3.3 — Projeção do FCFF

**Ação:**
1. FCFF = NOPAT + D&A − ΔCapital de Giro − Capex Total.
2. Capex: mapeamento individual (Passo 2.5.3) + manutenção normalizada (Passo 2.2).
3. ΔWC: DSO, DIO, DPO modelados separadamente.
4. SBC ajustado (financing, não operating).
5. Projetar **10-15 anos explícitos** (capturar ramp-ups).
6. **Check fundamental: g = ROIIC × Taxa de Reinvestimento. Se não bate → ❗ erro lógico.**
7. Projetar EPS = NOPAT ajustado / shares outstanding.

**Referências:**
- **Livro 87** (McKinsey): Cap. 9 — DCF.
- **P24** (ROIC): cálculo detalhado.
- **P31** (Red Queen): manutenção.

**Output:** DREs projetados 10-15 anos. Tabela FCFF consolidada. EPS projetado.

---

## Passo 3.4 — Validação Probabilística (Monte Carlo)

**Ação:**
1. Definir distribuição para os 2-3 drivers mais sensíveis.
2. Monte Carlo (5.000-10.000 iterações) via `scripts/monte_carlo.py` → distribuição de valores.
3. Verificar: o valor fundamentalista está em qual percentil?
4. Resultado = intervalo de confiança, **não substituto**.

**Referências:**
- **Livro 90** (McLeish): Cap. 2 — path-by-path FCFF.
- **Livro 48** (Benninga): Monte Carlo.
- **P07** (Probabilities and Payoffs).

**Output:** Gráficos em percentil. Intervalo de confiança.
