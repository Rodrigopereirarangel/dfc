---
name: "Fase 5 — Valor Terminal"
description: |
  Calcula Terminal Value via McKinsey CV, crosschecks com EPV/Exit Multiple e sanity checks.
  Triggers: "terminal value", "valor terminal", "perpetuidade"
---

# FASE 5 — VALOR TERMINAL

> **Regra Global:** Cada passo DEVE entregar os 5 Blocos Institucionais + Síntese §1–§5 + JSON Payload.

---

## Passo 5.1 — Gordon Growth / McKinsey Continuing Value

**Ação:**
1. g terminal ≤ GDP nominal de longo prazo.
2. g = RONIC × Reinvestment Rate (não arbitrar).
3. Se ROIC convergiu para WACC: growth irrelevante (NPV novos investimentos = 0).
4. TV = NOPAT(t+1) × (1 − g/RONIC) / (WACC − g) ← **McKinsey Continuing Value**.
5. **⚠️ Regra Penman**: se g terminal alto → WACC terminal não deveria ser maior?

**BLOCO 1 — Painel do Terminal Value:**

| Método | g terminal | ROE/ROIC terminal | COE/WACC | TV (R$ bi) | TV/EV total |
|---|---|---|---|---|---|
| McKinsey CV | X% | X% | X% | R$X bi | X% |
| Gordon Growth | X% | — | X% | R$X bi | X% |
| P/VP model | X% | X% | X% | R$X bi | X% |
| EPV (floor) | 0% | — | X% | R$X bi | X% |

**BLOCO 2 — O Paradoxo do Crescimento Terminal:**
"Se o ROIC no terminal convergir para o COE, qualquer investimento novo vale exatamente zero — crescimento sem rentabilidade acima do custo de capital é o equivalente corporativo de girar em falso."

Desdobrar para o caso específico: o g terminal de X% é justificado dado o ROE terminal de X% e o COE de X%?

**BLOCO 3 — Sanity Check do TV + DataViz:**

| Check | Resultado | Status |
|---|---|---|
| TV/EV total | X% | ✅ se <75% |
| g terminal vs PIB nominal BR LT | g=X% vs PIBn=X% | ✅/🟠 |
| ROIC terminal vs COE | ROIC=X% vs COE=X%, spread=Xpp | ✅/🟠 |
| P/VP terminal vs histórico | X× vs histórico X–X× | ✅/🟠 |
| EPV como floor | R$X bi vs EV atual R$X bi | ✅/❗ |

> **📊 Instrução DataViz — Comparação de Métodos de Terminal Value (Bar Chart):**
> Gráfico de barras horizontais lado a lado:
> - **Eixo X:** R$ bilhões de Terminal Value.
> - **Cada barra:** um método (McKinsey CV, Gordon, P/VP, EPV).
> - **Cores:** azul marinho (método principal), cinzas degradê (alternativos), vermelho (EPV como floor mínimo).
> - **Linha vertical âmbar:** EV atual como referência.
> - Rótulo com R$ bilhões no extremo de cada barra. Ordenar do maior para o menor.

**BLOCO 4 — Comparação P/VP Terminal com Histórico:**
A empresa negociou com que P/VP em: (a) auge de ciclo, (b) normalização, (c) crise. O P/VP terminal de X× é historicamente sustentável?

**BLOCO 5 — Analogia de Terminal Value Absurdo:**
Caso onde TV > 80% do EV e o ativo decepcionou. O sanity check teria revelado?

```
╔══════════════════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — Fase 5 Completa                     ║
╚══════════════════════════════════════════════════════════════════╝
§1 Qual o Terminal Value e sua participação no EV total?
§2 Os métodos convergem ou divergem? O que a divergência revela?
§3 O g terminal aprovado no Penman Test?
§4 Quais sanity checks passaram ou falharam?
§5 TV/EV elevado cria assimetria de risco não precificada?
```

**Referências:**
- **Livro 87** (McKinsey): Cap. 9 e 11 — Estimating Continuing Value.
- **Livro 09** (Greenwald): Cap. 4 — EPV; Cap. 7-8 — Franchise Value.
- **Livro 01** (Penman): growth → risk test.
- **P19** (ROIC and Investment Process).

**JSON Payload ao final da Fase 5:**
```json
<!-- JSON_PAYLOAD
{
  "fase": "F5_COMPLETA",
  "tv_mckinsey_bi": 0.0,
  "tv_gordon_bi": 0.0,
  "tv_pvp_bi": 0.0,
  "epv_bi": 0.0,
  "tv_ev_pct": 0.0,
  "g_terminal": 0.0,
  "roic_terminal": 0.0,
  "wacc_terminal": 0.0,
  "pvp_terminal_implicito": 0.0
}
-->
```

---

## ✅ CHECKLIST DE COMPLIANCE — VALIDAÇÃO OBRIGATÓRIA ANTES DE AVANÇAR

Antes de passar para a próxima fase, o Agente AI DEVE verificar e imprimir este checklist PREENCHIDO com **[V]** (Verdadeiro) ou **[F]** (Falso) em sua resposta:

```text
[CHECKLIST DE COMPLIANCE DO AGENTE — FASE F5]
[V/F] Eu abri e li integralmente este arquivo SKILL.md usando a minha ferramenta de leitura de arquivos.
[V/F] Eu executei TODOS os sub-passos desta fase (não pulei nenhum).
[V/F] Eu entreguei os 5 Blocos (Diagnóstico / Narrativa / DataViz / Trade-off / Analogia) em CADA sub-passo.
[V/F] Eu incluí a instrução DataViz específica (tipo de gráfico + paleta + eixos) no BLOCO 3 de cada passo.
[V/F] Eu apresentei a Síntese Institucional (§1 a §5) ao final desta fase.
[V/F] Eu fechei a resposta gerando o bloco <!-- JSON_PAYLOAD --> com a taxonomia exata desta fase.
```

**Se qualquer item for (F):** PARE. Não avance. Corrija a sua resposta e reentregue antes de prosseguir para a próxima fase.

Validação automática: `python scripts/validate_compliance.py --clipboard --fase F5`
