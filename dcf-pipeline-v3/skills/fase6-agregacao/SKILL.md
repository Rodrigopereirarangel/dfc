---
name: "Fase 6 — Agregação, Cenários & Bridge para Equity"
description: |
  Cenários ponderados, bridge EV→Equity, sensibilidade 7×7 e comparação institucional.
  Triggers: "cenários", "fair value", "preço justo", "bridge", "sensibilidade"
---

# FASE 6 — AGREGAÇÃO, CENÁRIOS & BRIDGE PARA EQUITY

> **Entradas:** Terminal Value (Fase 5), WACC (Fase 4), FCFF (Fase 3).
> **Calcular com:** `scripts/sensitivity_table.py` para tabela 7×7.
> **Regra Global:** Cada passo DEVE entregar os 5 Blocos Institucionais + Síntese §1–§5 + JSON Payload.

---

## Passo 6.1 — Cenários Ponderados + Árvore de Cenários

**Ação:**
1. Definir 3-5 cenários com premissas explícitas: Distress (5-10%), Bear (20-25%), Base (40-50%), Bull (20-25%).
2. EV e equity value por cenário.
3. Expected Value = Σ(Prob × Valor).
4. Para cada cenário, extrair: ERP implícito, Custo de Capital Real implícito.

**BLOCO 1 — Tabela de Cenários:**

| Cenário | Prob | Fair Value | Upside | Driver Principal | Macro | Execução |
|---|---|---|---|---|---|---|
| Distress | X% | R$X | X% | [driver] | [Selic, PIB] | [execução] |
| Bear | X% | R$X | X% | [driver] | | |
| Base | X% | R$X | X% | [driver] | | |
| Bull | X% | R$X | X% | [driver] | | |
| **Expected Value** | 100% | **R$X** | **X%** | | | |

**BLOCO 2 — Narrativa de Cada Cenário como Mundo Completo:**
Para cada cenário com prob ≥ 20%, parágrafo narrativo: como está a macro brasileira, a empresa em termos competitivos, o management entregou, o sentimento do mercado?

**BLOCO 3 — Expected Value e Assimetria + DataViz:**

| Métrica | Resultado | Interpretação |
|---|---|---|
| Expected Value | R$X | |
| Upside máximo (Bull) | +X% | |
| Downside máximo (Distress) | −X% | |
| Razão Upside/Downside | X× | >2× ideal; <1× → não investir |
| Kelly Implícito | X% | Negativo → não abrir posição |

> **📊 Instrução DataViz — Distribuição de Cenários (Bar Chart com Dispersão):**
> Gráfico de barras horizontais por cenário:
> - **Eixo X:** R$/ação de Fair Value (mínimo=Distress, máximo=Bull).
> - **Barra horizontal** por cenário com largura proporcional à probabilidade.
> - **Diamante âmbar (#CBA052) sobreposto:** Expected Value ponderado.
> - **Linha vertical cinza:** Preço atual de mercado (para mostrar upside/downside visualmente).
> - Rótulos: R$/ação + % de upside/downside.

💡 A razão Upside/Downside de X× é o indicador primário de assimetria. Kelly negativo = não investir a este preço.

**BLOCO 4 — O que Precisa ser Verdade para o Bull Case:**
Liste 5 premissas que precisam se materializar para o PT bull. Probabilidade individual e conjunta.

**BLOCO 5 — Analogia de Cenários:**
Ativo onde o cenário base se revelou otimista e o bear se materializou. Quais eram os sinais antecedentes?

```
╔══════════════════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — Passo 6.1                           ║
╚══════════════════════════════════════════════════════════════════╝
```

**Referências:**
- **P07** (Probabilities and Payoffs).
- **P21** (Confidence): separar probabilidade × confiança.
- **Livro 27** (Superprevisões).

---

## Passo 6.2 — Real Options (se aplicável)

**Ação:**
1. Identificar opções reais: expansion, abandonment, switching, timing.
2. Valuar via framework qualitativo ou B-S adaptado.
3. EV = DCF Base + Σ(Real Options).

**Referências:**
- **Livro 34** (Real Options, Trigeorgis).

---

## Passo 6.3 — Bridge EV → Equity Value + Sensibilidade 7×7

**Ação:**
1. Equity Value = EV − Dívida Líquida − Minority Interests − Preferred + Associates + Excess Cash.
2. Ajustar shares por SBC dilution futura + bonificações.
3. Tabela de sensibilidade NTN-B × premissa-chave 7×7.
4. Calcular ERP implícito no Fair Value e comparar com Damodaran.
5. Net Payout Yield: (Buybacks + Dividendos − Emissões) / Market Cap.

**BLOCO 1 — Bridge EV → Equity:**

| Item | Valor |
|---|---|
| Enterprise Value (EV) | R$X bi |
| (−) Dívida Bruta | −R$X bi |
| (+) Caixa e Equivalentes | +R$X bi |
| (−) Minority Interests | −R$X bi |
| Equity Value | **R$X bi** |
| Shares Outstanding (diluted) | X mi ações |
| **Fair Value por Ação** | **R$X** |

**BLOCO 2 — ERP Implícito no Fair Value:**
O ERP implícito no nosso fair value é X%. Compare com ERP histórico de ativos similares.

**BLOCO 3 — Heatmap de Sensibilidade 7×7 + DataViz:**
Tabela 7×7 cruzando COE (ou NTN-B) × g terminal (ou outra premissa-chave):

```
🟢 COMPRA FORTE  → Fair Value > preço atual + 20%
🟡 NEUTRO/MANTER → Fair Value entre −10% e +20% do preço atual  
🔴 VENDER/EVITAR → Fair Value < preço atual − 10%
```

> **📊 Instrução DataViz — Heatmap Térmico 7×7:**
> Matriz de calor 7×7:
> - **Eixo X:** COE (ou NTN-B) em 7 valores (ex: 12% a 18%, em steps de 1pp).
> - **Eixo Y:** g terminal em 7 valores (ex: 2% a 8%, em steps de 1pp).
> - **Célula:** R$/ação de Fair Value.
> - **Gradiente de cor:** Paleta divergente — Verde (#27AE60) quando FV > preço + 20%, Amarelo (#F1C40F) para zona neutra, Vermelho (#C0392B) quando FV < preço − 10%.
> - **Círculo âmbar na célula Base Case** (nosso cenário central).
> - Rótulos R$/ação em cada célula. Fonte monospaced.

**BLOCO 4 — Zona de Segurança:**
Qual região do heatmap oferece margem de segurança adequada independentemente de flutuações razoáveis? Qual seria o preço de entrada ideal?

**BLOCO 5 — Analogia de Sensibilidade:**
Ativo onde a tabela teria revelado zona de risco elevado. O que aconteceu?

---

## Passo 6.4 — Comparação Institucional (Sell-Side / Consenso)

**Ação:**
1. Buscar target prices e projeções-chave de múltiplas casas.
2. Comparar fair value e projeções do nosso modelo vs. consenso.
3. Avaliar onde concordamos (para não agir) e onde divergimos (oportunidade de alpha).

**Referências:**
- **Livro 13** (Damodaran): bridge EV → Equity.
- **Livro 87** (McKinsey, Cap. 10): From Enterprise to Equity.
- **P20** (SBC): diluição futura.

```
╔══════════════════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — Fase 6 Completa                     ║
╚══════════════════════════════════════════════════════════════════╝
§1 Qual o Expected Value e a assimetria de risco/retorno?
§2 A margem de segurança é adequada ao moat identificado na Fase 0?
§3 Alta / Moderada / Baixa confiança no range de fair value?
§4 Qual região do heatmap monitorar nos próximos trimestres?
§5 A diferença entre nosso EV e o consenso é oportunidade ou sinal de alerta?
```

**JSON Payload ao final da Fase 6:**
```json
<!-- JSON_PAYLOAD
{
  "fase": "F6_COMPLETA",
  "ev_base": 0.0,
  "equity_value": 0.0,
  "fair_value_acao": 0.0,
  "preco_atual": 0.0,
  "upside_pct": 0.0,
  "expected_value_acao": 0.0,
  "razao_upside_downside": 0.0,
  "kelly_implicito": 0.0,
  "erp_implicito": 0.0,
  "cenarios": [
    {"nome": "Distress", "prob": 0, "fv": 0.0},
    {"nome": "Bear", "prob": 0, "fv": 0.0},
    {"nome": "Base", "prob": 0, "fv": 0.0},
    {"nome": "Bull", "prob": 0, "fv": 0.0}
  ],
  "heatmap_7x7": {
    "eixo_x_coe": [0,0,0,0,0,0,0],
    "eixo_y_g": [0,0,0,0,0,0,0],
    "valores": []
  }
}
-->
```

---

## ✅ CHECKLIST DE COMPLIANCE — VALIDAÇÃO OBRIGATÓRIA ANTES DE AVANÇAR

Antes de passar para a próxima fase, o Agente AI DEVE verificar e imprimir este checklist PREENCHIDO com (V) ou (F) em sua resposta:

```text
[CHECKLIST DE COMPLIANCE DO AGENTE]
[?] Eu abri e li integralmente este arquivo SKILL.md usando a minha ferramenta de leitura de arquivos.
[?] Eu executei TODOS os sub-passos desta fase (não pulei nenhum).
[?] Eu entreguei os 5 Blocos (Diagnóstico / Narrativa / DataViz / Trade-off / Analogia) em CADA sub-passo.
[?] Eu incluí a instrução DataViz específica (tipo de gráfico + paleta + eixos) no BLOCO 3 de cada passo.
[?] Eu apresentei a Síntese Institucional (§1 a §5) ao final desta fase.
[?] Eu fechei a resposta gerando o bloco <!-- JSON_PAYLOAD --> com a taxonomia exata desta fase.
```

**Se qualquer item for (F):** PARE. Não avance. Corrija a sua resposta e reentregue antes de prosseguir para a próxima fase.

