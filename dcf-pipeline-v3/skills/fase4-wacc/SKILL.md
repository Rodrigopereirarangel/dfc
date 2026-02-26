---
name: "Fase 4 — Taxa de Desconto Dinâmica (WACC)"
description: |
  Calcula Ke, Kd, WACC com term structure e aplica Regra Penman.
  Triggers: "WACC", "custo de capital", "taxa de desconto", "beta"
---

# FASE 4 — TAXA DE DESCONTO DINÂMICA (WACC)

> **Entradas:** Estrutura de capital e dívida da Fase 1 (`skills/fase1-auditoria-contabil/SKILL.md`). Beta setorial de peers. NTN-B e ERP de `references/contexto-brasil.md`.
> **Saídas:** WACC anual flutuante → usado em Fases 5, 5A, 6 e 7.

## Passo 4.1 — Custo do Equity (Ke)

**Ação:**
1. Risk-free: **NTN-B longa** (Brasil) ou Treasury 10Y (global).
2. ERP: Damodaran forward-looking. **Cruzar com Expected Returns (L21 - Ilmanen) para checar se atende condições macro-estruturais.**
3. Beta: bottom-up (unlevered de peers via yfinance → relever pela estrutura-alvo).
4. Size premium, Country Risk Premium (CRP).
5. `Ke = Rf + β × ERP + Size + CRP`.
6. Alternativa: implied cost of capital via reverse DCF.
7. **⚠️ REGRA PENMAN**: se g > inflação + 1%, questionar se Ke não deveria ser maior.

**Referências:**
- **P22** (Cost of Capital: Practical Guide): passo-a-passo Rf → ERP → β → Size → CRP → Ke.
- **Livro 19** (Andrew Ang): Cap. 6-10 — Factor Decomposition.
- **Livro 21** (Expected Returns, Ilmanen): Cap. 3 — Equity Premium decomposition.
- **Livro 01** (Penman): regra "+1% growth → +1% required return".
- **Livro 06/84** (Expectations Investing): Cap. 8 — Market-Implied.
- **Livro 86** (Lundholm/Sloan): Cap. 9, Pg. 190 — custo de capital.
- **Livro 59** (Renda Fixa Brasil): NTN-B como risk-free.

---

## Passo 4.2 — Custo da Dívida e Estrutura de Capital

**Ação:**
1. Kd = yield to worst (não taxa contábil).
2. Tax shield: Kd × (1−t) com taxa efetiva.
3. Target capital structure.
4. `WACC = Ke × (E/(D+E)) + Kd×(1−t) × (D/(D+E))`.
5. **WACC term structure**: se a empresa desalavanca com ramp-up, ajustar por período.
6. Análise de minoritários e majoritários: impacto no custo efetivo.
7. Experimentar P/VP=1 como teste Penman.

**Referências:**
- **Livro 87** (McKinsey): Cap. 8 — Cost of Capital prático.
- **Livro 01** (Penman): P/B=1 test.
- **P13** (Cost of Capital): WACC em regimes easy money.
- **P39** (WACC and Vol): real options benefício.

**Output:** Tabela Custo de Capital (Rf, ERP, β, Size, CRP → Ke, Kd, WACC). WACC flutuante anual. Log Penman.
