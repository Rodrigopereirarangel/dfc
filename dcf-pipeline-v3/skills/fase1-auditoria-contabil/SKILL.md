---
name: "Fase 1 — Auditoria Contábil Forense & Qualidade"
description: |
  Detecta manipulações, normaliza demonstrativos, decompõe ROE e constrói 3-Statement Model.
  Triggers: "auditoria", "qualidade do lucro", "normalizar", "shenanigans"
---

# FASE 1 — AUDITORIA CONTÁBIL FORENSE

> **Fonte primária obrigatória: ITR/DFP oficial da CVM.**

## Passo 1.1 — Shenanigans + Beneish M-Score

**Ação:**
1. Aplicar check das 7 Categorias de Manipulação Contábil (Schilit).
2. Calcular Beneish M-Score: `M = −4.84 + 0.92×DSRI + 0.528×GMI + ...`
3. Threshold: M > −1.78 → alta probabilidade de manipulação → ❗
4. **Comparar Cash Earnings vs. Reported Earnings** — divergência persistente = red flag.
5. **FCF vs. Net Income divergência (5-10 anos):** se lucro cresce mas FCF estagna, investigar.
6. Checar red flags em FCF e aquisições (Cap. 10-11).
7. GAAP loser vs. real loser? (P26)

**Referências:**
- **Livro 07** (Financial Shenanigans, Schilit): Cap. 2-8 — 7 categorias; Cap. 10-11 — red flags FCF.
- **Livro 02** (Iudícibus): DuPont 5 níveis.
- **P26** (Good Losses, Bad Losses): Distinguir GAAP loser vs. real loser.

**Output:** M-Score (OK vs Alerta). Tabela de categorias acionadas.

---

## Passo 1.2 — Normalização e Ajustes Contábeis

**Ação:**
1. Ajustar EBITDA (não-recorrentes, SBC, leases IFRS 16).
2. Capitalizar intangíveis no balanço (R&D, SGA de aquisição de cliente).
3. Recalcular amortização dos intangíveis capitalizados.
4. Clean surplus accounting (Penman).
5. Reclassificar DFC: SBC → Atividade de Financiamento.
6. **Distinguir Perdas Boas (CAC gerador de LTV) vs Perdas Ruins (queima estrutural) (P26).**
7. **Aplicar regras locais de normatização (FIPECAFI - L10) para empresas da B3 (CPC vs IFRS).**
8. DuPont 5 níveis + **Decomposição ROE = ROIC + Leverage × Spread**:
   ```
   ROE = ROIC + (ROIC − Kd_after_tax) × D/E
   ```
   Mostra se a alavancagem cria ou destrói valor.
9. Ajustar lucro de minoritários em subsidiárias.

**Referências:**
- **Livro 01** (Penman): Cap. 3 — Clean Surplus; Cap. 5 — Residual Earnings.
- **Livro 86** (Lundholm/Sloan): Pg. 110 — Decomposição ROE.
- **Livro 10** (FIPECAFI): Normatização local BR.
- **P29** (Intangibles and Earnings): capitalizar R&D → amortizar 3-5 anos.
- **P23** (ROIC and Intangibles): ajuste ROIC para goodwill.
- **P20** (SBC): SBC como % receita por idade.
- **P32** (Categorizing for Clarity): SBC → financing, leases IFRS 16.

**Output:** EBITDA Reportado vs Ajustado. Árvore ROE Decomposed. Spread histórico.

---

## Passo 1.3 — 3-Statement Model + Tabelas-Base

**Ação:**
1. Montar modelo integrado DRE + Balanço + DFC (mínimo 10 anos históricos via DFP).
2. Implementar circularidade (juros → lucro → caixa → dívida → juros).
3. Checks de integridade (A = P + PL; DFC reconcilia com BP).
4. **Construir tabelas-base:**
   - Ciclo de caixa (DSO, DIO, DPO) por ano.
   - RNOA, ROIC, CAPEX/Receita, ΔWC/Receita.
   - DL/EBITDA, Interest Coverage.
   - Correlações históricas entre line items.
5. **Projetar EPS** explicitamente (NOPAT ajustado / shares outstanding).

**Referências:**
- **Livro 48** (Benninga): Cap. 1-5 — 3-Statement Model.
- **Livro 44** (Tjia): Cap. 3-8 — Circularidade e checks.
- **Livro 86** (Lundholm/Sloan): Pg. 153 — Framework projetivo.
- **Livro 87** (McKinsey): Arquitetura de modelo.

**Output:** Matriz 3-Statement histórica 100% coerente. Tabelas-base auxiliares. EPS histórico.
