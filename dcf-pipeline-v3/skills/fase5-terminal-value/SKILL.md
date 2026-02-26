---
name: "Fase 5 — Valor Terminal"
description: |
  Calcula Terminal Value via McKinsey CV, crosschecks com EPV/Exit Multiple e sanity checks.
  Triggers: "terminal value", "valor terminal", "perpetuidade"
---

# FASE 5 — VALOR TERMINAL

## Passo 5.1 — Gordon Growth com ROIC Fade

**Ação:**
1. g terminal ≤ GDP nominal de longo prazo.
2. g = RONIC × Reinvestment Rate (não arbitrar).
3. Se ROIC convergiu para WACC no terminal → growth irrelevante (NPV novos investimentos = 0).
4. Se ROIC > WACC (moat duradouro) → fade residual modelado.
5. **Convexidade de buyback como payout tampão.**
6. TV = NOPAT(t+1) × (1 − g/RONIC) / (WACC − g) ← **McKinsey Continuing Value** (superior a Gordon simples).
7. **⚠️ Regra Penman**: se g terminal alto → WACC terminal não deveria ser maior?

**Referências:**
- **Livro 87** (McKinsey): Cap. 9 e 11 — DCF e Estimating Continuing Value.
- **Livro 06/84** (Expectations Investing): CAP.
- **Livro 01** (Penman): growth → risk test.
- **P19** (ROIC and Investment Process).
- **P41** (Math of Value and Growth).

---

## Passo 5.2 — Crosschecks do Terminal Value

**Ação:**
1. Exit Multiple: EV/EBITDA terminal calibrado por peers e ciclo.
2. EPV: NOPAT normalizado / WACC (floor do valor).
3. **Reproduction Value** (Greenwald): quanto custaria replicar os ativos da empresa do zero? Se EV < Reproduction Value → margem de segurança física.
4. Real Options overlay (se opcionalidade significativa).
5. **Accounting for Value crosscheck**: Forward Earnings via Penman → coerência EV.

**Referências:**
- **Livro 09** (Greenwald): Cap. 4 — EPV; Cap. 7-8 — Franchise Value.
- **Livro 01** (Penman): Cap. 6 — Forward Earnings.
- **Livro 34** (Real Options).
- **P12** (Valuation Multiples): exit multiple calibração.
- **P48** (EV/EBITDA).

---

## Passo 5.3 — Sanity Check

**Ação:**
1. TV como % do EV total. **Se > 75% → extender período explícito.**
2. Implied growth rate do TV — faz sentido vs. GDP?
3. Implied ROIC do TV — faz sentido vs. WACC?
4. Comparar TV pelas 3+ abordagens — se divergem muito, investigar.

**Output:** TV calculado via McKinsey CV. EPV estático. Exit Multiple implícito. Tabela Sanity Check (TV/EV %).
