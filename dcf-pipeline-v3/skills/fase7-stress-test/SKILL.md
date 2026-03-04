---
name: "Fase 7 — Stress Test & Validação Cruzada"
description: |
  Fat tails, Via Negativa, vieses cognitivos, triangulação, QMJ e sentimento de mercado.
  Triggers: "stress test", "validação", "vieses", "triangulação", "QMJ"
---

# FASE 7 — STRESS TEST & VALIDAÇÃO CRUZADA

> **Ponteiros de entrada:** Fases 3, 5 e 6.
> **Regra Global:** Cada passo DEVE entregar os 5 Blocos Institucionais + Síntese §1–§5 + JSON Payload.

---

## Passo 7.1 — Fat Tails e Via Negativa (Curto, Médio e Longo Prazo)

**Ação:**
1. Monte Carlo (`scripts/monte_carlo.py`): distribuição tem fat tails?
2. Cenário 3+ σ: a empresa sobrevive?
3. **Via Negativa:** O que NÃO deveria acontecer para a tese funcionar?
   - **Curto prazo (trimestre):** Que eventos invalidariam imediatamente?
   - **Médio prazo (1-3 anos):** Que mudanças estruturais destroem o moat?
   - **Longo prazo (5+ anos):** Que disruptions tornam o negócio obsoleto?

**BLOCO 1 — Mapa de Condições de Invalidação:**

| Condição | Timeline | Prob. | Severidade | Velocidade de queda | Preço no pior momento |
|---|---|---|---|---|---|
| [Condição 1] | Q1/Q2 2026 | X% | 🔴 | Abrupta/Gradual | R$X |
| [Condição 2] | 2027-2028 | X% | 🟠 | Gradual | R$X |
| [Condição 3] | 2029+ | X% | 🟡 | Lenta | R$X |

**BLOCO 2 — Narrativa de Materialização por Condição Crítica:**
Para cada condição 🔴 ou 🟠 — sequência completa:
- T+1: primeiro dado que sinaliza.
- T+2–4: confirmação e início de reprecificação.
- T+5–8: plena precificação.
- Velocidade: abrupta (>15% em 1 pregão) ou gradual (4-6 trimestres)?

**BLOCO 3 — "O que precisaria ser verdade para eu estar errado" + DataViz:**

| Se verdadeiro → análise conservadora demais | Probabilidade |
|---|---|
| [Afirmação bull 1] | X% |
| [Afirmação bull 2] | X% |

| Se verdadeiro → análise otimista demais | Probabilidade |
|---|---|
| [Afirmação bear 1] | X% |
| [Afirmação bear 2] | X% |

> **📊 Instrução DataViz — Distribuição Monte Carlo (KDE Plot):**
> Curva de densidade de probabilidade (KDE — Kernel Density Estimate) do Fair Value simulado:
> - **Eixo X:** R$/ação (de Distress ao Bull extremo).
> - **Eixo Y:** Densidade de probabilidade.
> - **Área sob a curva à esquerda do preço atual:** colorida em Vermelho (probabilidade de perda).
> - **Área à direita do preço atual:** colorida em Azul Marinho (probabilidade de ganho).
> - **Linha vertical âmbar:** Expected Value. **Linha tracejada cinza:** Preço atual.
> - Percentis P5, P25, P50, P75, P95 annotados acima da curva.

**BLOCO 4 — Tail Risk não Modelável:**
Existe risco que não pode ser modelado mas que destruiria a tese? (fraude não detectada, disruption regulatória, evento sistêmico.) Como se posicionar?

**BLOCO 5 — Analogia de Materialização de Tail Risk:**
Empresa onde o tail risk se materializou. Quanto tempo o mercado levou para perceber plenamente?

```
╔══════════════════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — Passo 7.1                           ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## Passo 7.2 — Vieses Cognitivos e Sentimento de Mercado

**Ação:**
1. Checklist de vieses: Anchoring, Overconfidence, Confirmation Bias, Narrative Fallacy, Recência.
2. Sentimento de mercado via yfinance: Short Ratios, Opções, P/E Histórico.
3. Dispersão alta de analistas = oportunidade de alpha ou armadilha?

**BLOCO 1 — Painel de Vieses Identificados:**

| Viés | Presente? | Como se manifestou | Como mitigamos |
|---|---|---|---|
| Anchoring (ao preço atual) | ✅/🟠 | [descrição] | [ação] |
| Narrative Fallacy | ✅/🟠 | [descrição] | |
| Recência | ✅/🟠 | [descrição] | |
| Confirmation Bias | ✅/🟠 | [descrição] | |
| Overconfidence | ✅/🟠 | [descrição] | |

**BLOCO 2 — O Viés Mais Perigoso Nesta Análise:**
Qual viés tem maior risco de ter distorcido nossa análise? Por quê este ativo/setor/momento é propenso a ele?

**BLOCO 3 — Sentimento de Mercado vs. Modelo + DataViz:**

> **📊 Instrução DataViz — Short Interest + P/E vs Histórico:**
> Gráfico duplo eixo por período (3-5 anos):
> - **Linha Azul Marinho:** P/E atual da empresa.
> - **Banda cinza opaca:** ±1σ do P/E histórico.
> - **Linha Âmbar eixo direito:** Short interest % do float.

**BLOCO 4 — Feedback Loop: Processo vs. Outcome:**
Esta análise foi feita com bom processo? O que garantiria que este é um bom processo independentemente do outcome?

**BLOCO 5 — Analogia de Viés Coletivo:**
Caso onde o sell-side inteiro compartilhou o mesmo viés. Quando e como o mercado se corrigiu?

```
╔══════════════════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — Fase 7 Completa                     ║
╚══════════════════════════════════════════════════════════════════╝
§1 O stress test via Monte Carlo refletiu as assimetrias conhecidas?
§2 Quão robusto é o case frente aos vieses cognitivos mapeados?
§3 Qual é o tail risk mais preocupante, mesmo de baixa probabilidade?
§4 Que KPIs trimestrais monitorar para o pior cenário?
§5 O mercado está ciente da Via Negativa (o que daria errado)?
```

**Referências:**
- **Livro 89** (Antifrágil, Taleb): Via Negativa.
- **P52** (Common Errors in DCF): checklist final.
- **Livro 62** (Kahneman): anchoring, overconfidence.

**JSON Payload ao final da Fase 7:**
```json
```json
{
  "fase": "F7_COMPLETA",
  "vieses_identificados": [],
  "condicoes_invalidacao": [
    {"descricao": "", "probabilidade": 0.0, "severidade": ""}
  ]
}
```
```

---

## ✅ CHECKLIST DE COMPLIANCE — VALIDAÇÃO OBRIGATÓRIA ANTES DE AVANÇAR

Antes de passar para a próxima fase, o Agente AI DEVE verificar e imprimir este checklist PREENCHIDO com **[V]** (Verdadeiro) ou **[F]** (Falso) em sua resposta:

```text
[CHECKLIST DE COMPLIANCE DO AGENTE — FASE F7]
[V/F] Eu abri e li integralmente este arquivo SKILL.md usando a minha ferramenta de leitura de arquivos.
[V/F] Eu executei TODOS os sub-passos desta fase (não pulei nenhum).
[V/F] Eu entreguei os 5 Blocos (Diagnóstico / Narrativa / DataViz / Trade-off / Analogia) em CADA sub-passo.
[V/F] Eu incluí a instrução DataViz específica (tipo de gráfico + paleta + eixos) no BLOCO 3 de cada passo.
[V/F] Eu apresentei a Síntese Institucional (§1 a §5) ao final desta fase.
[V/F] Eu fechei a resposta gerando o bloco ```json com a taxonomia exata desta fase.
```

**Se qualquer item for (F):** PARE. Não avance. Corrija a sua resposta e reentregue antes de prosseguir para a próxima fase.

Validação automática: `python scripts/validate_compliance.py --clipboard --fase F7`
