---
name: "⭐ Fase 5A — Auditoria de Integração 360° (GATE)"
description: |
  GATE OBRIGATÓRIO. Não prosseguir para Terminal Value sem aprovação.
  Triggers: "auditoria 360", "coerência", "integração", "conferir modelo"
---

# ⭐ FASE 5A — AUDITORIA DE INTEGRAÇÃO 360°

> **GATE OBRIGATÓRIO. Não prosseguir para o Terminal Value sem passar por esta fase.**
> **Se ≥ 1 ❗ → Reabrir bloco correspondente para correção.**
>
> **Entradas:** Todos os outputs das Fases 1-4. Especificamente:
> - FCFF projetado da Fase 3 (`skills/fase3-projecao-fcff/SKILL.md`)
> - WACC da Fase 4 (`skills/fase4-wacc/SKILL.md`)
> - Capex breakdown da Fase 2 (`skills/fase2-value-drivers/SKILL.md`)
> - Script de validação: `scripts/validate_model.py`

## Passo 5A.1 — Teste de Coerência & Integração Total

**Ação:**

**1. Chain Check: Receita → NOPAT → FCFF**
- NOPAT = Receita × Margem Operacional After Tax.
- FCFF = NOPAT + D&A − CAPEX_total − ΔWC.
- **Alerta ❗ se Δ recalculado vs. modelo > ±R$ 1 mi em qualquer ano.**

**2. Reconciliação Segmento ⇄ Consolidado**
- Σ(Receita segmentos) = Receita consolidada.
- Σ(NOPAT segmentos) = NOPAT consolidado.
- Spread ROIC−WACC consolidado = média ponderada segmentos.
- **Alerta 🟠 se Δ > 0,1 pp (ROIC) ou R$ 1 mi (absoluto).**

**3. Cash-Flow Loop Circular**
- FCFF → Amortização dívida = Cash-sweep − Dividendos.
- Nova D/E → β_levered = β_unlevered × (1 + (1−IR) × D/E).
- Novo WACC.
- **Alerta ❗ se ΔWACC > ±10 bps entre iterações.** Máximo 5 iterações.

**4. CAPEX Manutenção vs. Expansão Integrity**
- CAPEX_total = CAPEX_manutenção + CAPEX_expansão (todos anos).
- Verificar: CAPEX_manutenção ≥ D&A ajustada por inflação?
- **Alerta 🟠 se sobreposição > 0,1% Receita.**

**5. Teste Penman: Growth → Risk**
- Se g projetado > inflação + 1%, perguntar: "O WACC deveria ser maior?"

**Referências:**
- **Livro 01** (Penman): growth → risk.
- **Livro 87** (McKinsey): testes de integridade.
- **Livro 86** (Lundholm/Sloan): reconciliação DRE↔Balanço.
- **P52** (Common Errors in DCF): checklist de erros.

---

## Passo 5A.2 — Desvios Ocultos do Cenário Base

**Ação:**
Construir tabela comparativa de cada premissa-chave vs. base rate empírica:

| Variável | Valor no Modelo | Base Rate Empírica | Δ (%) | Gravidade | Comentário |
|---|---|---|---|---|---|

- Incluir APENAS variáveis com Gravidade = 🟠 ou ❗.
- Comparar com base rates de Mauboussin (P01, P35, P19).

---

## Passo 5A.3 — Stress-Checks Relâmpago

**Ação:**
- +50 bps WACC → Δ% no Terminal Value.
- −5% na variável de receita mais sensível → Δ% FCFF último ano.
- +2 pp CAPEX Manutenção → Δ Spread ROIC−WACC Terminal.
- **Se algum Δ > 15% no valor → investigar antes de prosseguir.**

---

## Passo 5A.4 — Diagnóstico Estratégico Express

**Ação:**
- Avaliar robustez do capital allocation.
- Comparar fade ROIC projetado com pares maduros (>10 anos).
- Identificar **2 KPIs críticos** + nível de confiança.
- **Se ≥ 1 ❗ ou Gravidade Alta → "↩️ Reabrir Bloco para correção".**
- **Se tudo OK → prosseguir para Fase 5 (Terminal Value).**

**Output:** Relatório de Veredito: ✅ APROVADO ou ↩️ REABRIR BLOCO X. Lista de alertas.
