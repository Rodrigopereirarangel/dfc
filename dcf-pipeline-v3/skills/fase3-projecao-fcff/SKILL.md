---
name: "Fase 3 — Projeção dos Fluxos de Caixa"
description: |
  Projeção bottom-up de receita, margens, FCFF e validação probabilística.
  Triggers: "projeção", "receita", "FCFF", "fluxo de caixa", "Monte Carlo"
---

# FASE 3 — PROJEÇÃO DOS FLUXOS DE CAIXA

> **Entradas obrigatórias:** Modelo 3-Statement (Fase 1), Capex Red Queen e ROIC fade (Fase 2), Haircut de management e projetos (Fase 2.5), Base rates em `references/base-rates.md`.
> **Regra Global:** Cada passo DEVE entregar os 5 Blocos Institucionais + Síntese §1–§5 + JSON Payload.

---

## Passo 3.1 — Projeção de Receita (Bottom-Up)

**Ação:**
1. Decompor receita por segmento: Volume × Preço | Clientes × ARPU × Retention | TAM × Share × Penetração.
2. Incorporar ramp-ups (Passo 2.5.3) com haircut do management.
3. Outside view: comparar com base rates do setor.
4. **NUNCA macro-crescimento flat.** Projetar período de ramp-up e término explicitamente.

**BLOCO 1 — Matriz de Premissas de Crescimento:**

| Vertical | Base Rate Setorial | Guidance Management | Haircut Aplicado | Nossa Projeção | Justificativa do Desvio |
|---|---|---|---|---|---|
| [V1] | X% | X% | X% | X% | [acima/abaixo da base rate porque...] |
| [V2] | X% | X% | X% | X% | |

🎯 **Premissa mais crítica:** [Vertical X] — cada +1pp = +R$Xmi no lucro e +R$X/ação no fair value.

**BLOCO 2 — Decomposição dos Drivers por Vertical:**
Para cada vertical: qual componente está crescendo (volume ou preço)? É sustentável? O mercado está saturando ou em penetração inicial?

**BLOCO 3 — Cenários de Crescimento + DataViz:**

| Cenário | CAGR Receita 2026–2030 | Receita 2030E | Premissa Diferencial |
|---|---|---|---|
| Bear | X% | R$X bi | [premissa] |
| Base | X% | R$X bi | [premissa] |
| Bull | X% | R$X bi | [premissa] |

> **📊 Instrução DataViz — Gráfico de Área Receita e Margem (estilo Goldman Sachs):**
> Gráfico combinado linha + área por ano:
> - **Barras empilhadas (Azul Marinho + variações):** Receita por vertical em R$bi — eixo esquerdo.
> - **Linha âmbar (#CBA052):** Margem EBIT % — eixo direito.
> - **Separador visual na linha do tempo:** área sólida = Histórico (2019-2025A); área hachurada (listras diagonais) = Projetado (2026E-2030E).
> - **Cenário Bear vs. Bull:** sombra cinza ao redor da linha base representando o range de incerteza.
> - Etiquetas explícitas "A" (actual) e "E" (estimated) nos anos.

**BLOCO 4 — A Premissa de Crescimento que mais Divide o Mercado:**
Qual vertical bulls e bears mais discordam? Qual dado nos próximos 2 trimestres resolverá o debate?

**BLOCO 5 — Analogia de Trajetória de Receita:**
Empresa que projetou crescimento similar. Entregou ou decepcionou? O dado ex-ante teria revelado o risco?

```
╔══════════════════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — Passo 3.1                           ║
╚══════════════════════════════════════════════════════════════════╝
```

**Referências:**
- **Livro 87** (McKinsey): Cap. 12 — Forecasting Performance por UEN.
- **P46** (TAM): top-down vs bottom-up TAM.
- **P01** (Bayes): prior + evidência → posterior.

---

## Passo 3.2 — Projeção de Margens e Custos

**Ação:**
1. Custo variável como % receita por segmento.
2. Custos fixos nominais + inflação + step functions.
3. Margem incremental projetada: consistente com histórica?
4. Separar componentes cíclicos vs. estruturais de margem.

**BLOCO 1 — Decomposição de Margem:**

| Componente | 2023A | 2024A | 2025A | 2026E | Tendência | Natureza |
|---|---|---|---|---|---|---|
| Receita | | | | | | |
| Sinistros / COGS | | | | | | Variável |
| Despesas operacionais | | | | | | Semi-fixo |
| Resultado financeiro | | | | | | Cíclico |
| Margem Líquida | | | | | ↗️/↘️ | |

**BLOCO 2 — Separação Estrutural vs. Cíclico:**
- Componentes cíclicos (revertem com ciclo de juros, sinistros, câmbio): quanto representam do lucro atual?
- Componentes estruturais (persistem independente do ciclo): qual é o ROE "limpo"?
- Alavancagem operacional: se receita cair 10%, o lucro cai quanto?

**BLOCO 3 — Normalização de Margem Longo Prazo + DataViz:**

| Horizonte | Margem Projetada | Premissa Principal | Risco de Erro |
|---|---|---|---|
| 2026E | X% | [premissa] | 🔴/🟠/✅ |
| 2028E | X% | [premissa] | |
| Terminal | X% | [premissa] | |

> **📊 Instrução DataViz — Waterfall de Expansão/Contração de Margem:**
> Gráfico de cascata de Margem EBIT ao longo dos anos, mostrando os drivers:
> - **Incrementos positivos (Cinza #4A4A4A):** Alavancagem operacional, melhoria de mix.
> - **Incrementos negativos (Vermelho #8B0000):** Inflação de custos, queda de componente financeiro.
> - **Barra final (Azul Marinho):** Margem 2028E projetada.

**BLOCO 4 — O Componente de Margem que Pode Surpreender:**
Existe algum custo que pode melhorar ou piorar materialmente vs. o projetado?

**BLOCO 5 — Analogia de Compressão/Expansão de Margem:**
Empresa que passou por trajetória similar. Quanto tempo para estabilizar?

```
╔══════════════════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — Passo 3.2                           ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## Passo 3.3 — Projeção do FCFF e Lucro Recorrente

**Ação:**
1. FCFF = NOPAT + D&A − ΔCapital de Giro − Capex Total.
2. Projetar **10-15 anos explícitos** (capturar ramp-ups).
3. **Check fundamental: g = ROIIC × Taxa de Reinvestimento. Se não bate → ❗ erro lógico.**
4. Projetar EPS = NOPAT ajustado / shares outstanding.

**BLOCO 1 — Reconciliação Lucro → Caixa:**

| Item | 2025A | 2026E | 2027E | 2028E |
|---|---|---|---|---|
| Lucro Líquido Recorrente | R$X | R$X | R$X | R$X |
| (−) Reinvestimento necessário | −R$X | −R$X | −R$X | −R$X |
| FCFF / Lucro Disponível | R$X | R$X | R$X | R$X |
| g = ROIIC × Reinv. Rate (check) | X% | X% | X% | X% |
| g projetado | X% | X% | X% | X% |
| Consistência | ✅/❗ | | | |

**BLOCO 2 — Para Seguradoras/Financeiras — por que Lucro Recorrente ≠ FCFF:**
O float de prêmios inflaciona o caixa operacional. Explicar o mecanismo e por que o lucro recorrente normalizado é o proxy correto.

**BLOCO 3 — Sensibilidade do FCFF + DataViz:**

| Se [premissa] variar X pp | Impacto no FCFF 2026E | Impacto na Margem FCFF |
|---|---|---|
| Sinistralidade +1pp | −R$Xmi | −X pp |
| Selic −100bps | −R$Xmi | −X pp |

**BLOCO 3.2 — Matriz de Projeções (Múltiplas Curvas FCFF):**
Analise a matriz de 3 projeções distintas para o FCFF de longo prazo, fornecendo valores tanto para o marco de 5 anos (2030E) quanto de 10 anos (2035E):

| Método de Projeção | FCFF 2026E | FCFF 5 Anos (2030E) | FCFF 10 Anos (2035E) | Justificativa Analítica |
|---|---|---|---|---|
| 1. Bottom-up Operacional (Base) | R$X | R$X | R$X | Nossa tese decomposta |
| 2. Extrapolação Histórica (5/10A) | R$X | R$X | R$X | Trendline mantida |
| 3. Consenso / Guidance | R$X | R$X | R$X | Expectativa mkt / mgmt |

> **📊 Instrução DataViz — Gráfico de Barras FCFF Projetado vs LPA (5 vs 10 Anos):**
> Gráfico de barras duplas por ano (Cenário de 10 anos: 2026E-2035E):
> - **Barra esquerda (Azul Marinho):** FCFF (R$mi).
> - **Barra direita (Âmbar #CBA052):** Lucro Recorrente (R$mi).
> - **Marco temporal (Linha pontilhada):** Indicador visual separando o período curto (Ano 1-5) do período longo (Ano 6-10) demonstrando o fade de crescimento.

**BLOCO 4 — Consistência Interna das Projeções:**
O crescimento do lucro é consistente com o crescimento do BV? `g = ROE × (1 − payout)`.

**BLOCO 5 — Analogia de Projeção de Fluxo:**
Empresa cujas projeções de FCFF foram sistematicamente otimistas. O que o dado ex-ante revelaria?

```
╔══════════════════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — Fase 3 Completa                     ║
╚══════════════════════════════════════════════════════════════════╝
§1 Quais são os FCFF projetados e sua qualidade analítica?
§2 Qual a divergência entre nossa curva Bottom-up e o Consenso?
§3 Alta / Moderada / Baixa confiança nas projeções?
§4 Que KPIs trimestrais confirmarão ou refutarão as projeções?
§5 O mercado está embutindo premissas de crescimento realistas?
```

**Referências:**
- **Livro 87** (McKinsey): Cap. 9 — DCF.
- **P24** (ROIC): cálculo detalhado.
- **Livro 90** (McLeish): path-by-path FCFF.

**JSON Payload ao final da Fase 3:**
```json
```json
{
  "fase": "F3_COMPLETA",
  "fcff_projetado_base_5_anos": [
    {"ano": 2026, "fcff": 0, "lucro_recorrente": 0, "lpa": 0.0},
    {"ano": 2027, "fcff": 0, "lucro_recorrente": 0, "lpa": 0.0},
    {"ano": 2028, "fcff": 0, "lucro_recorrente": 0, "lpa": 0.0},
    {"ano": 2029, "fcff": 0, "lucro_recorrente": 0, "lpa": 0.0},
    {"ano": 2030, "fcff": 0, "lucro_recorrente": 0, "lpa": 0.0}
  ],
  "fcff_projetado_base_10_anos": [
    {"ano": 2031, "fcff": 0, "lucro_recorrente": 0, "lpa": 0.0},
    {"ano": 2032, "fcff": 0, "lucro_recorrente": 0, "lpa": 0.0},
    {"ano": 2033, "fcff": 0, "lucro_recorrente": 0, "lpa": 0.0},
    {"ano": 2034, "fcff": 0, "lucro_recorrente": 0, "lpa": 0.0},
    {"ano": 2035, "fcff": 0, "lucro_recorrente": 0, "lpa": 0.0}
  ],
  "fcff_10y_cagr": 0.0,
  "fcff_projetado_historico": [
    {"ano_5": 2030, "fcff": 0},
    {"ano_10": 2035, "fcff": 0}
  ],
  "fcff_projetado_consenso": [
    {"ano_5": 2030, "fcff": 0},
    {"ano_10": 2035, "fcff": 0}
  ],
  "cagr_receita_2026_2030": 0.0,
  "margem_ebit_terminal_e": 0.0
}
```
```

---

## ✅ CHECKLIST DE COMPLIANCE — VALIDAÇÃO OBRIGATÓRIA ANTES DE AVANÇAR

Antes de passar para a próxima fase, o Agente AI DEVE verificar e imprimir este checklist PREENCHIDO com **[V]** (Verdadeiro) ou **[F]** (Falso) em sua resposta:

```text
[CHECKLIST DE COMPLIANCE DO AGENTE — FASE F3]
[V/F] Eu abri e li integralmente este arquivo SKILL.md usando a minha ferramenta de leitura de arquivos.
[V/F] Eu executei TODOS os sub-passos desta fase (não pulei nenhum).
[V/F] Eu entreguei os 5 Blocos (Diagnóstico / Narrativa / DataViz / Trade-off / Analogia) em CADA sub-passo.
[V/F] Eu incluí a instrução DataViz específica (tipo de gráfico + paleta + eixos) no BLOCO 3 de cada passo.
[V/F] Eu apresentei a Síntese Institucional (§1 a §5) ao final desta fase.
[V/F] Eu fechei a resposta gerando o bloco ```json com a taxonomia exata desta fase.
```

**Se qualquer item for (F):** PARE. Não avance. Corrija a sua resposta e reentregue antes de prosseguir para a próxima fase.

Validação automática: `python scripts/validate_compliance.py --clipboard --fase F3`
