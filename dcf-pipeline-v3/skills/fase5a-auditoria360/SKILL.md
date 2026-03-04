---
name: "⭐ Fase 5A — Auditoria de Integração 360° (GATE)"
description: |
  GATE OBRIGATÓRIO. Não prosseguir para Terminal Value sem aprovação.
  Triggers: "auditoria 360", "coerência", "integração", "conferir modelo"
---

# ⭐ FASE 5A — AUDITORIA DE INTEGRAÇÃO 360°

> **GATE OBRIGATÓRIO. Não prosseguir para o Terminal Value sem passar por esta fase.**
> **Se ≥ 1 ❗ → Reabrir bloco correspondente para correção.**
> **Regra Global:** Cada passo DEVE entregar os 5 Blocos Institucionais + Síntese §1–§5 + JSON Payload.

---

## Passo 5A.1 — Teste de Coerência & Integração Total

**Ação:**

**1. Chain Check: Receita → NOPAT → FCFF**
- NOPAT = Receita × Margem Operacional After Tax.
- FCFF = NOPAT + D&A − CAPEX_total − ΔWC.
- **Alerta ❗ se Δ recalculado vs. modelo > ±R$ 1 mi em qualquer ano.**

**2. Reconciliação Segmento ⇄ Consolidado**
- Σ(Receita segmentos) = Receita consolidada.
- **Alerta 🟠 se Δ > 0,1 pp (ROIC) ou R$ 1 mi (absoluto).**

**3. Cash-Flow Loop Circular**
- FCFF → Amortização dívida; Nova D/E → β_levered → Novo WACC.
- **Alerta ❗ se ΔWACC > ±10 bps entre iterações.** Máximo 5 iterações.

**4. CAPEX Integrity**
- CAPEX_total = CAPEX_manutenção + CAPEX_expansão (todos anos).
- **Alerta 🟠 se sobreposição > 0,1% Receita.**

**5. Teste Penman: Growth → Risk**
- Se g projetado > inflação + 1%, perguntar: "O WACC deveria ser maior?"

**BLOCO 1 — Painel de Alertas do GATE:**

| Check | Status | Detalhe | Ação requerida |
|---|---|---|---|
| Chain Check Receita→NOPAT→FCFF | ✅/❗ | Δ = R$X | [nenhuma / corrigir] |
| Reconciliação Segmento↔Consolidado | ✅/🟠 | Δ = X pp | |
| Loop Circular WACC (max 5 iter.) | ✅/❗ | Convergiu em X iter. | |
| Capex Integrity (man+exp=total) | ✅/🟠 | Δ = X% receita | |
| Penman Test | ✅/🟠 | g=X% vs X% threshold | |
| ROE vs BV consistency | ✅/❗ | g_BV = X% vs X% projetado | |
| **VEREDITO DO GATE** | **✅ APROVADO / ❗ REPROVADO** | | |

**BLOCO 2 — Para Cada Alerta: Análise de Impacto:**
Se algum check falhou: qual o impacto quantitativo no fair value? É material (>3%)? Como corrigir?

**BLOCO 3 — Desvios do Cenário Base vs. Base Rates + DataViz:**

| Premissa | Nossa Estimativa | Base Rate Setorial | Desvio | Justificativa |
|---|---|---|---|---|
| ROE projetado | X% | X–X% | +Xpp | [justificativa] |
| g terminal | X% | X% PIB nominal | Xpp | |
| CAP utilizado | X anos | X–X anos | Xpp | |

> **📊 Instrução DataViz — Semáforo de Checks GATE:**
> Tabela visual com codificação de cores tipo "dashboard":
> - Cada linha = um check. Coluna de Status com célula colorida: Verde (#27AE60), Laranja (#F39C12), Vermelho (#C0392B).
> - Badge final com APROVADO (Verde) ou REPROVADO (Vermelho).

**BLOCO 4 — Stress-check Relâmpago:**
+50bps WACC, −5% receita mais sensível, +2pp Capex Manutenção → qual o impacto no Terminal Value?
Se algum Δ > 15% → investigar antes de prosseguir.

**BLOCO 5 — Analogia de Erro de Modelo:**
Caso documentado onde erro de modelagem (chain check, WACC circular) gerou valuation distorcido.

```
╔══════════════════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — Fase 5A Completa (GATE)             ║
╚══════════════════════════════════════════════════════════════════╝
§1 O modelo está íntegro e consistente entre todas as fases?
§2 Existem erros materiais que afetam o fair value?
§3 Quais premissas desviam mais das base rates e por quê?
§4 Prosseguir (✅) ou reabrir alguma fase (↩️)?
§5 A auditoria revelou alguma assimetria de informação?
```

**Referências:**
- **Livro 01** (Penman): growth → risk.
- **Livro 87** (McKinsey): testes de integridade.
- **P52** (Common Errors in DCF): checklist de erros.

**JSON Payload ao final da Fase 5A:**
```json
```json
{
  "fase": "F5A_GATE",
  "gate_aprovado": true,
  "alertas_graves": [],
  "alertas_atencao": [],
  "desvios_base_rate": [
    {"premissa": "ROE projetado", "modelo": 0.0, "base_rate": 0.0, "desvio": 0.0},
    {"premissa": "g terminal", "modelo": 0.0, "base_rate": 0.0, "desvio": 0.0}
  ]
}
```
```

---

## ✅ CHECKLIST DE COMPLIANCE — VALIDAÇÃO OBRIGATÓRIA ANTES DE AVANÇAR

Antes de passar para a próxima fase, o Agente AI DEVE verificar e imprimir este checklist PREENCHIDO com **[V]** (Verdadeiro) ou **[F]** (Falso) em sua resposta:

```text
[CHECKLIST DE COMPLIANCE DO AGENTE — FASE F5A]
[V/F] Eu abri e li integralmente este arquivo SKILL.md usando a minha ferramenta de leitura de arquivos.
[V/F] Eu executei TODOS os sub-passos desta fase (não pulei nenhum).
[V/F] Eu entreguei os 5 Blocos (Diagnóstico / Narrativa / DataViz / Trade-off / Analogia) em CADA sub-passo.
[V/F] Eu incluí a instrução DataViz específica (tipo de gráfico + paleta + eixos) no BLOCO 3 de cada passo.
[V/F] Eu apresentei a Síntese Institucional (§1 a §5) ao final desta fase.
[V/F] Eu fechei a resposta gerando o bloco ```json com a taxonomia exata desta fase.
```

**Se qualquer item for (F):** PARE. Não avance. Corrija a sua resposta e reentregue antes de prosseguir para a próxima fase.

Validação automática: `python scripts/validate_compliance.py --clipboard --fase F5A`
