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

## Passo 6.4 — A Grande Triangulação (Valuation Engine)

**Ação:**
1. Reunir **todos** os métodos de avaliação no mesmo quadro comparativo.
2. DCF Base (FCFF via Fase 3).
3. EPV vs DCF: o mercado precifica destruição via growth?
4. Residual Income Model (Penman).
5. Múltiplos implícitos vs Histórico.
6. Comparação Institucional (Sell-Side / Consenso).
7. Quality Minus Junk score (QMJ).

**BLOCO 1 — Tabela de Triangulação Completa:**

| Método | Fair Value | Pressuposto Central | Limitação |
|---|---|---|---|
| DCF Base (FCFF Operacional) | R$X | FCFF curva Base (Fase 3) | Sensibilidade da margem |
| P/VP × ROE (Penman) | R$X | ROE X%, g X%, COE X% | ROE terminal |
| DDM Gordon | R$X | Ke X%, g X%, DPA X% | Crescimento retido |
| EPV Greenwald | R$X | Zero growth perpétuo | Floor conservador |
| P/L peers hist. | R$X | X× LPA 2026E | Assume rerating |
| Reverse DCF (implied) | R$X | Premissas atuais mkt | O que mkt paga |
| Consenso Sell-Side | R$X | Múltiplas teses médias | Efeito manada |

**BLOCO 2 — Convergência e Divergência:**
No mínimo 3 métodos convergem em torno de R$X–X? Quais métodos divergem fortemente? O que essa divergência revela sobre a sensibilidade do ativo neste momento? (Ex: "A enorme distância entre nosso DCF e o EPV mostra que a tese depende >60% de crescimento futuro").

**BLOCO 3 — Score QMJ + Valuation Football Field (DataViz):**

| Dimensão QMJ (Quality Minus Junk) | Score | Evidência |
|---|---|---|
| Rentabilidade (ROE, ROIC, margem) | X/10 | [dado] |
| Crescimento (CAGR receita, lucro) | X/10 | [dado] |
| Segurança (leverage, cobertura) | X/10 | [dado] |
| Payout (DY, payout ratio) | X/10 | [dado] |
| **QMJ Total** | **X/10** | |

> **📊 Instrução DataViz — Football Field Valuation (Barras Horizontais Rigorosas):**
> Gráfico de barras horizontais sobrepostas (padrão sell-side internacional):
> - **Eixo X:** R$/ação (range: Distress ao Bull extremo).
> - **Cada barra horizontal** = um método de valuation (DCF Base, Múltiplos Históricos, EPV, Sell-Side Consenso, Residual Income).
> - **Largura da barra** = range min-max do método.
> - **Traço central** = estimativa pontual de cada método.
> - **Linha vertical âmbar (#CBA052):** nosso Expected Value (calculado no Passo 6.1).
> - **Linha vertical cinza tracejada:** preço atual de mercado.
> - Cores: azul escuro (DCF), cinza médio (múltiplos), vermelho suave (EPV floor), verde suave (Bull range).

**BLOCO 4 — Convergência Final: Nossa Convicção de Preço:**
Dado o quadro completo da Grande Triangulação: qual é nossa restrita e conservadora estimativa de fair value pontual? Em qual range nos sentimos confortáveis para alocar capital de terceiros?

**BLOCO 5 — Divergência Institucional (Oportunidade ou Alerta?):**
A diferença entre nosso EV/Fair Value e o consenso Wall Street é sinal de alpha (nosso edge via pesquisa) ou sinal de que estamos cometendo um erro primário?

```
╔══════════════════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — Fase 6 Completa                     ║
╚══════════════════════════════════════════════════════════════════╝
§1 Qual o Expected Value e a assimetria de risco/retorno na Árvore de Cenários?
§2 A margem de segurança no Heatmap 7x7 é adequada ao moat (Fase 0)?
§3 Na Triangulação, existe convergência clara para apoiar o valuation?
§4 O EV atual representa uma oportunidade anticonsenso ou value trap?
§5 Qual KPI monitorar prioritariamente nos próximos 2-3 trimestres?
```

**Referências:**
- **Livro 13** (Damodaran): bridge EV → Equity.
- **Livro 87** (McKinsey, Cap. 10): From Enterprise to Equity.
- **P53** (QMJ, Asness Frazzini): quality factor scoring.
- **Livro 09** (Greenwald): EPV, triangulação.
- **P20** (SBC): diluição futura.

**JSON Payload ao final da Fase 6:**
```json
```json
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
  "qmj_score": 0.0,
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
  },
  "triangulacao": [
    {"metodo": "DCF Base", "fv_min": 0.0, "fv_ponto": 0.0, "fv_max": 0.0},
    {"metodo": "EPV", "fv_min": 0.0, "fv_ponto": 0.0, "fv_max": 0.0},
    {"metodo": "Multiplos Historicos", "fv_min": 0.0, "fv_ponto": 0.0, "fv_max": 0.0},
    {"metodo": "Consenso Sell-Side", "fv_min": 0.0, "fv_ponto": 0.0, "fv_max": 0.0}
  ]
}
```
```

---

## ✅ CHECKLIST DE COMPLIANCE — VALIDAÇÃO OBRIGATÓRIA ANTES DE AVANÇAR

Antes de passar para a próxima fase, o Agente AI DEVE verificar e imprimir este checklist PREENCHIDO com **[V]** (Verdadeiro) ou **[F]** (Falso) em sua resposta:

```text
[CHECKLIST DE COMPLIANCE DO AGENTE — FASE F6]
[V/F] Eu abri e li integralmente este arquivo SKILL.md usando a minha ferramenta de leitura de arquivos.
[V/F] Eu executei TODOS os sub-passos desta fase (não pulei nenhum).
[V/F] Eu entreguei os 5 Blocos (Diagnóstico / Narrativa / DataViz / Trade-off / Analogia) em CADA sub-passo.
[V/F] Eu incluí a instrução DataViz específica (tipo de gráfico + paleta + eixos) no BLOCO 3 de cada passo.
[V/F] Eu apresentei a Síntese Institucional (§1 a §5) ao final desta fase.
[V/F] Eu fechei a resposta gerando o bloco ```json com a taxonomia exata desta fase.
```

**Se qualquer item for (F):** PARE. Não avance. Corrija a sua resposta e reentregue antes de prosseguir para a próxima fase.

Validação automática: `python scripts/validate_compliance.py --clipboard --fase F6`
