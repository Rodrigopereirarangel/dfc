---
name: "Fase 8 — Decisão: Conviction & Sizing"
description: |
  Conviction Score composto, Kelly Criterion fracional e assimetria Antifrágil.
  Triggers: "conviction", "sizing", "posição", "Kelly", "recomendação"
---

# FASE 8 — DECISÃO: CONVICTION & SIZING

> **Entradas obrigatórias:** Fair Value (Fase 6), Moat (Fase 0), Management Score (Fase 2.5), QMJ e Triangulação (Fase 7).
> **Calcular com:** `scripts/kelly_sizing.py`
> **Regra Global:** Cada passo DEVE entregar os 5 Blocos Institucionais + Síntese §1–§5 + JSON Payload.

---

## Passo 8.1 — Conviction Score

**Ação:**
Score composto (1 a 10) com pesos:
- **Upside/Downside Ratio** (25%): Expected Value / Preço Atual.
- **Qualidade do Moat** (20%): Nota Durabilidade do Passo 0.1.
- **Credibilidade do Management** (20%): Score do Passo 2.5.1.
- **Confiança nas Projeções** (15%): dispersão do MC, sensibilidade.
- **Confirmação de Validação Cruzada** (10%): convergência dos métodos.
- **Quality Minus Junk Score** (10%): quality factor QMJ.

Score ≥ 7 → posição relevante; 5-6 → menor; < 5 → não investir.

**BLOCO 1 — Breakdown Visual do Conviction Score:**

```
╔══════════════════════════════════════════════════════════════════╗
║  CONVICTION SCORE — BREAKDOWN INSTITUCIONAL                     ║
╠══════════════════════╦═══════╦═══════╦═══════╦═════════════════╣
║  Dimensão            ║ Peso  ║ Nota  ║Contrib║ Justificativa   ║
╠══════════════════════╬═══════╬═══════╬═══════╬═════════════════╣
║  Upside/Downside     ║  25%  ║  X/10 ║  X,XX ║ EV X% vs preço ║
║  Qualidade do Moat   ║  20%  ║  X/10 ║  X,XX ║ [1 frase]      ║
║  Credib. Management  ║  20%  ║  X/10 ║  X,XX ║ [1 frase]      ║
║  Conf. Projeções     ║  15%  ║  X/10 ║  X,XX ║ [1 frase]      ║
║  Triangulação        ║  10%  ║  X/10 ║  X,XX ║ [1 frase]      ║
║  QMJ Score           ║  10%  ║  X/10 ║  X,XX ║ [1 frase]      ║
╠══════════════════════╬═══════╬═══════╬═══════╬═════════════════╣
║  TOTAL               ║ 100%  ║       ║  X,XX ║                 ║
╠══════════════════════╬═══════╬═══════╬═══════╬═════════════════╣
║  Recomendação        ║ [Compra / Manter / Não investir]        ║
╚══════════════════════╩═══════╩═══════╩═══════╩═════════════════╝
```

**BLOCO 2 — Análise de Cada Dimensão do Score:**
Para cada dimensão com nota ≤ 5: o que precisaria mudar para elevar 2 pontos? Para cada nota ≥ 8: o que sustenta e por quanto tempo?

**BLOCO 3 — O Score Reflete a Realidade? + DataViz:**

> **📊 Instrução DataViz — Conviction Score Disaggregation (Bar-Chart Horizontal):**
> Gráfico de barras horizontais:
> - **Eixo Y:** Dimensões do score (6 dimensões).
> - **Eixo X:** Contribuição ponderada (0 a 2,5) de cada dimensão.
> - **Cor da barra:** Verde (#27AE60) se nota ≥ 7, Amarelo (#F1C40F) se 5-6, Vermelho (#C0392B) se < 5.
> - **Linha vertical âmbar:** Total Score resultante (com escala secundária 0-10).

**BLOCO 4 — Sensibilidade do Score:**
Se a premissa mais crítica (🎯 Passo 2.4) se revelar errada, como o conviction score mudaria? O que isso implicaria para o sizing?

**BLOCO 5 — Analogia de Conviction Score:**
Caso onde o conviction score foi alto mas o investimento decepcionou. Qual dimensão foi mal avaliada?

---

## Passo 8.2 — Position Sizing via Kelly

**Ação:**
1. Kelly: `f* = (p × b − q) / b`.
2. Usar Half-Kelly ou Quarter-Kelly na prática.
3. Stop-loss: em qual cenário a tese está errada?
4. **Assimetria Antifrágil**: downside limitado + upside convexo → mais agressivo. Downside ilimitado → conservador.
5. Correlação de Sentimento Extremo: se modelo bull + mercado pesimista + score elevado → Sizing Premium.

**BLOCO 1 — Cálculo do Kelly:**

| Input Kelly | Valor | Fonte |
|---|---|---|
| p (prob. upside) | X% | Prob. Bull + Base |
| b (razão upside/downside) | X× | Bull upside / Bear downside médio |
| q (prob. downside) | X% | 1 − p |
| **Full Kelly (f*)** | **X%** | f* = (p×b − q) / b |
| **Half-Kelly (recomendado)** | **X%** | f* × 0,5 |
| **Posição Máxima no Portfólio** | **X%** | Half-Kelly |

**BLOCO 2 — Intuição do Kelly para Este Ativo:**
"Um Kelly de X% significa que a matemática sugere alocar X% do portfólio. Se o Kelly é negativo, o downside esperado supera o upside esperado mesmo se você estiver certo na maioria das vezes. Abrir posição a este preço é, em termos esperados, destruir capital."

**BLOCO 3 — Condições de Stop-loss e Saída + DataViz:**

| Condição de Saída | KPI de monitoramento | Threshold | Ação |
|---|---|---|---|
| Tese fundamental quebrada | [KPI específico] | [valor] | Sair imediatamente |
| Crescimento abaixo do esperado | [KPI] | [valor] | Reduzir posição |
| ROE caindo consistentemente | [KPI] | [valor] | Reavaliar |

> **📊 Instrução DataViz — Watchlist de Catalisadores (Timeline Chart):**
> Gráfico de linha do tempo horizontal:
> - **Eixo X:** Datas (próximos 8 trimestres).
> - **Marcadores Bear (triângulo vermelho para baixo):** catalisadores negativos esperados.
> - **Marcadores Bull (triângulo azul para cima):** catalisadores positivos esperados.
> - **Tamanho do marcador:** proporcional ao impacto esperado em R$/ação.
> - **Rótulo:** breve descrição do catalisador.

**BLOCO 4 — Watchlist de Catalisadores — Entrada e Saída:**

| Catalisador | Direção | Prob. | Timeline | Impacto |
|---|---|---|---|---|
| [Resultado trimestral fraco] | 🔻 Bear | X% | Próx. trimestre | −R$X/ação |
| [Queda da Selic] | 🔻 Bear | X% | 2026 | −R$X/ação |
| [Novo cliente/contrato] | 🔺 Bull | X% | 2T26 | +R$X/ação |
| **Preço de entrada ideal** | 🎯 | — | Se [condições] | R$X–X |

**BLOCO 5 — Analogia de Sizing:**
Caso onde o Kelly indicou não investir e o investidor ignorou. O que aconteceu?

```
╔══════════════════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — Fase 8 Completa (Decisão Final)     ║
╚══════════════════════════════════════════════════════════════════╝
§1 A recomendação final é: Compra / Manter / Não investir?
§2 O conviction score e o Kelly são coerentes com o upside/downside?
§3 As condições de stop-loss são claras e monitoráveis?
§4 Quais catalisadores, positivos e negativos, observar nos próximos 6 meses?
§5 Existe assimetria suficiente neste ativo para justificar posição relevante?
```

**Referências:**
- **Livro 03** (Bernstein): Kelly Criterion.
- **Livro 18** (Paleologo): dimensionamento.
- **Livro 89** (Antifrágil): assimetria.
- **P07** (Probabilities and Payoffs).

**JSON Payload ao final da Fase 8:**
```json
```json
{
  "fase": "F8_COMPLETA",
  "conviction_score": 0.0,
  "recomendacao": "Compra / Manter / Não Investir",
  "kelly_full": 0.0,
  "kelly_half": 0.0,
  "posicao_maxima_pct_portfolio": 0.0,
  "conviction_breakdown": {
    "upside_downside": {"peso": 0.25, "nota": 0.0, "contrib": 0.0},
    "moat": {"peso": 0.20, "nota": 0.0, "contrib": 0.0},
    "management": {"peso": 0.20, "nota": 0.0, "contrib": 0.0},
    "confianca_projecoes": {"peso": 0.15, "nota": 0.0, "contrib": 0.0},
    "triangulacao": {"peso": 0.10, "nota": 0.0, "contrib": 0.0},
    "qmj": {"peso": 0.10, "nota": 0.0, "contrib": 0.0}
  },
  "catalistas": [
    {"descricao": "", "direcao": "Bull/Bear", "probabilidade": 0.0, "impacto_acao": 0.0}
  ]
}
```
```

---

## ✅ CHECKLIST DE COMPLIANCE — VALIDAÇÃO OBRIGATÓRIA ANTES DE AVANÇAR

Antes de passar para a próxima fase, o Agente AI DEVE verificar e imprimir este checklist PREENCHIDO com **[V]** (Verdadeiro) ou **[F]** (Falso) em sua resposta:

```text
[CHECKLIST DE COMPLIANCE DO AGENTE — FASE F8]
[V/F] Eu abri e li integralmente este arquivo SKILL.md usando a minha ferramenta de leitura de arquivos.
[V/F] Eu executei TODOS os sub-passos desta fase (não pulei nenhum).
[V/F] Eu entreguei os 5 Blocos (Diagnóstico / Narrativa / DataViz / Trade-off / Analogia) em CADA sub-passo.
[V/F] Eu incluí a instrução DataViz específica (tipo de gráfico + paleta + eixos) no BLOCO 3 de cada passo.
[V/F] Eu apresentei a Síntese Institucional (§1 a §5) ao final desta fase.
[V/F] Eu fechei a resposta gerando o bloco ```json com a taxonomia exata desta fase.
```

**Se qualquer item for (F):** PARE. Não avance. Corrija a sua resposta e reentregue antes de prosseguir para a próxima fase.

Validação automática: `python scripts/validate_compliance.py --clipboard --fase F8`
