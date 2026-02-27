---
name: "Fase 1 — Auditoria Contábil Forense & Qualidade"
description: |
  Detecta manipulações, normaliza demonstrativos, decompõe ROE e constrói 3-Statement Model.
  Triggers: "auditoria", "qualidade do lucro", "normalizar", "shenanigans"
---

# FASE 1 — AUDITORIA CONTÁBIL FORENSE

> **Fonte primária obrigatória: ITR/DFP oficial da CVM.**
> **Regra Global:** Cada passo DEVE entregar os 5 Blocos Institucionais + Síntese §1–§5 + JSON Payload.

---

## Passo 1.1 — Shenanigans + Beneish M-Score + Qualidade do Lucro

**Ação:**
1. Aplicar check das 7 Categorias de Manipulação Contábil (Schilit).
2. Calcular Beneish M-Score: `M = −4.84 + 0.92×DSRI + 0.528×GMI + ...`
3. Threshold: M > −1.78 → alta probabilidade de manipulação → ❗
4. Comparar Cash Earnings vs. Reported Earnings — divergência persistente = red flag.
5. FCF vs. Net Income divergência (5-10 anos).
6. GAAP loser vs. real loser? (P26)

**BLOCO 1 — Painel de Qualidade Contábil:**

| Indicador | Resultado | Threshold | Status | Interpretação |
|---|---|---|---|---|
| Beneish M-Score | X,XX | > −1,78 | ✅/❗ | [1 frase] |
| Cash Earnings vs. Reported | X% divergência | < 5% | ✅/🟠 | [1 frase] |
| FCF / Net Income (5A) | X% | > 80% saudável | ✅/🟠 | [1 frase] |
| Accruals Ratio | X% | < 5% ideal | ✅/🟠 | [1 frase] |
| Crescimento Recebíveis vs Receita | X pp | Deve acompanhar | ✅/🟠 | [1 frase] |
| GAAP vs. Non-GAAP spread | X% | < 10% | ✅/🟠 | [1 frase] |

**BLOCO 2 — Análise por Componente do M-Score:**
Para cada componente com alerta (🟠 ou ❗): o que mede, valor vs. threshold, existe explicação legítima (IFRS 16, sazonalidade)?

Tabela de Red Flags AUSENTES (informação positiva):

| Red Flag Comum no Setor | Status | Evidência da Ausência |
|---|---|---|
| [Red flag 1] | 🔒 Não encontrado | [dado específico] |
| [Red flag 2] | 🔒 Não encontrado | [dado específico] |

**BLOCO 3 — Qualidade do Lucro: o que o Caixa diz + DataViz:**
FCF vs. lucro reportado dos últimos 5 anos: divergência crescente ou convergente?

> **📊 Instrução DataViz — Waterfall Chart (Cascata):**
> Gráfico de barras cascata horizontal mostrando o walk-down do Lucro Reportado (GAAP) até o Lucro Normalizado (FCFF real):
> - **Barra inicial (Azul Marinho #003366):** Lucro Reportado GAAP.
> - **Barras intermediárias (Vermelho Escuro #8B0000):** Cada ajuste negativo (não-recorrentes, SBC, leases).
> - **Barras de ganho (Cinza Médio #4A4A4A):** Ajustes positivos eventuais.
> - **Barra final (Azul Marinho):** Lucro Normalizado total.
> - Rótulos com R$mi em cada barra. Linha de baseline horizontal.

💡 Insight: a **ausência** de red flags em company de alto ROIC é evidência positiva ativa — documentar explicitamente.

**BLOCO 4 — Dilema de Interpretação:**
Há algum item em que bull interpretaria diferentemente do bear? Qual o impacto no LPA normalizado e no fair value?

**BLOCO 5 — Analogia de Fraude ou Qualidade Contábil:**
Empresa do setor que passou por ajuste contábil relevante. O M-Score teria sinalizado?

```
╔══════════════════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — Passo 1.1                           ║
╚══════════════════════════════════════════════════════════════════╝
§1 O que a auditoria revelou sobre a qualidade do lucro?
§2 Impacto no LPA normalizado e no fair value?
§3 Confiança: fato vs. inferência vs. hipótese?
§4 O que esta auditoria abre de perguntas para o Passo 1.2?
§5 Existe algo que o mercado não vê no M-Score desta empresa?
```

**Referências:**
- **Livro 07** (Financial Shenanigans, Schilit): Cap. 2-8 — 7 categorias; Cap. 10-11 — red flags FCF.
- **Livro 02** (Iudícibus): DuPont 5 níveis.
- **P26** (Good Losses, Bad Losses).

**JSON Payload ao final do Passo 1.1:**
```json
<!-- JSON_PAYLOAD
{
  "fase": "F1_P11",
  "beneish_mscore": 0.0,
  "fcf_netincome_ratio_5a": 0.0,
  "accruals_ratio": 0.0,
  "gaap_nongaap_spread": 0.0,
  "waterfall_steps": [
    {"label": "Lucro Reportado", "valor": 0},
    {"label": "Ajuste Não-Recorrentes", "valor": 0},
    {"label": "SBC", "valor": 0},
    {"label": "Leases IFRS16", "valor": 0},
    {"label": "Lucro Normalizado", "valor": 0}
  ]
}
-->
```

---

## Passo 1.2 — Normalização e Ajustes Contábeis + ROE Decomposition

**Ação:**
1. Ajustar EBITDA (não-recorrentes, SBC, leases IFRS 16).
2. Capitalizar intangíveis no balanço (R&D, SGA de aquisição de cliente).
3. Clean surplus accounting (Penman).
4. DuPont 5 níveis + Decomposição ROE = ROIC + Leverage × Spread.
5. Spread ROIC vs. COE histórico (5 anos): criando ou destruindo valor?

**BLOCO 1 — Painel de Ajustes:**

| Item Ajustado | Reportado | Ajuste | Normalizado | Justificativa |
|---|---|---|---|---|
| Não-recorrentes | R$X | −R$X | R$X | [tipo] |
| SBC reclassificado | R$X | −R$X | R$X | IFRS/CPC |
| IFRS 16 leases | R$X | ±R$X | R$X | Ajuste padrão |
| **Lucro Normalizado** | — | — | **R$X** | |

**BLOCO 2 — Decomposição ROE Camada a Camada:**
- Camada 1 — Margem Líquida: pricing power e estrutura de custos.
- Camada 2 — Giro de Ativos: eficiência de uso do capital.
- Camada 3 — Leverage: está criando ou destruindo valor? (ROE = ROIC + spread × D/E)
- Camada 4 — Evolução histórica 3–5 anos: qual componente foi o principal motor?
- Camada 5 — Sustentabilidade: cíclico vs. estrutural.

**BLOCO 3 — Spread ROIC vs. COE + DataViz:**

| Ano | ROIC | COE | Spread | Criando valor? |
|---|---|---|---|---|
| 2021 | X% | X% | X pp | ✅/❗ |
| 2022 | X% | X% | X pp | ✅/❗ |
| 2023 | X% | X% | X pp | ✅/❗ |
| 2024 | X% | X% | X pp | ✅/❗ |
| 2025 | X% | X% | X pp | ✅/❗ |

> **📊 Instrução DataViz — Waterfall Decomposição ROE (DuPont):**
> Gráfico de barras verticais agrupadas:
> - **Barras empilhadas (Azul Marinho + Azul Médio + Cinza)** mostrando a contribuição de cada camada DuPont para o ROE final de cada ano.
> - **Linha amarela (#CBA052)** sobreposta: COE de cada ano (custo de oportunidade).
> - **Área de sombra entre ROE e COE:** Verde quando ROE > COE, Vermelha quando ROE < COE.
> - Eixo X: anos 2021-2025. Paleta: `["#003366", "#336699", "#A0A0A0", "#CBA052"]`.

💡 A **tendência do spread** é mais informativa que o nível absoluto. Spread crescente com margem em expansão = qualidade. Spread crescente apenas por alavancagem = risco.

**BLOCO 4 — Normalização como Decisão Analítica:**
Qual a maior controvérsia na normalização? Bull vs. bear interpretariam diferente?

**BLOCO 5 — Analogia de Normalização:**
Empresa mal avaliada por o mercado não normalizar corretamente. O que foi ignorado? Quando o mercado percebeu?

```
╔══════════════════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — Passo 1.2                           ║
╚══════════════════════════════════════════════════════════════════╝
```

**Referências:**
- **Livro 01** (Penman): Cap. 3 — Clean Surplus; Cap. 5 — Residual Earnings.
- **Livro 86** (Lundholm/Sloan): Pg. 110 — Decomposição ROE.
- **P29** (Intangibles and Earnings): capitalizar R&D → amortizar 3-5 anos.

**JSON Payload ao final do Passo 1.2:**
```json
<!-- JSON_PAYLOAD
{
  "fase": "F1_P12",
  "roae_reportado": 0.0,
  "roae_normalizado": 0.0,
  "spread_roic_coe_5a": [
    {"ano": 2021, "roic": 0, "coe": 0, "spread": 0},
    {"ano": 2022, "roic": 0, "coe": 0, "spread": 0},
    {"ano": 2023, "roic": 0, "coe": 0, "spread": 0},
    {"ano": 2024, "roic": 0, "coe": 0, "spread": 0},
    {"ano": 2025, "roic": 0, "coe": 0, "spread": 0}
  ],
  "dupon_margem": 0.0,
  "dupont_giro": 0.0,
  "dupont_leverage": 0.0
}
-->
```

---

## Passo 1.3 — 3-Statement Model + Tabelas-Base Históricas

**Ação:**
1. Montar modelo integrado DRE + Balanço + DFC (mínimo 10 anos históricos via DFP).
2. Checks de integridade (A = P + PL; DFC reconcilia com BP).
3. Construir tabelas-base: ciclo de caixa (DSO, DIO, DPO), ROIC, CAPEX/Receita, DL/EBITDA.
4. Projetar EPS = NOPAT ajustado / shares outstanding.

**BLOCO 1 — Painel de Tendências Críticas:**

| Métrica | 2021 | 2022 | 2023 | 2024 | 2025 | Tendência | Qualidade |
|---|---|---|---|---|---|---|---|
| Receita (R$bi) | | | | | | ↗️/→/↘️ | ✅/🟠 |
| Margem EBIT | | | | | | | |
| FCF Yield | | | | | | | |
| ROIC | | | | | | | |
| DL/EBITDA | | | | | | | |
| Payout | | | | | | | |

**BLOCO 2 — As 3 Tendências Mais Informativas:**
Para cada tendência relevante: o que está dizendo sobre o modelo de negócio? É estrutural ou cíclica? O mercado está incorporando?

**BLOCO 3 — FCF Yield e Ciclo de Caixa + DataViz:**

> **📊 Instrução DataViz — Gráfico de Linhas Múltiplas Tendências Históricas:**
> Gráfico de linhas com eixos duplos:
> - **Barras preenchidas (Azul Marinho):** Receita em R$bi (eixo esquerdo).
> - **Linha âmbar (#CBA052):** Margem EBIT % (eixo direito).
> - **Linha cinza tracejada:** ROIC % (eixo direito).
> - Divisória vertical clara indicando "HISTÓRICO" vs. "PROJETADO" (cinza hachura na área projetada).
> - X: anos. Sem gridlines verticais. Fonte profissional sans-serif.

**BLOCO 4 — Ciclo de Caixa e Eficiência Operacional:**
DSO, DIO, DPO histórico: empresa ficando mais ou menos eficiente? Poder de barganha com clientes e fornecedores.

**BLOCO 5 — Analogia de 3-Statement:**
Empresa com padrão histórico similar. A análise do histórico teria sido preditiva?

```
╔══════════════════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — Fase 1 Completa                     ║
╚══════════════════════════════════════════════════════════════════╝
§1 Qual o retrato fiel da qualidade contábil e do ROE real da empresa?
§2 Impacto no LPA normalizado usado nas projeções da Fase 3?
§3 Alta / Moderada / Baixa confiança nos números agora disponíveis?
§4 Quais ajustes serão carregados para as fases seguintes?
§5 O mercado está subestimando ou superestimando a qualidade contábil?
```

**Referências:**
- **Livro 48** (Benninga): Cap. 1-5 — 3-Statement Model.
- **Livro 44** (Tjia): Cap. 3-8 — Circularidade e checks.
- **Livro 87** (McKinsey): Arquitetura de modelo.

**JSON Payload ao final da Fase 1:**
```json
<!-- JSON_PAYLOAD
{
  "fase": "F1_COMPLETA",
  "lucro_normalizado": 0,
  "lpa_normalizado": 0.0,
  "fcf_yield": 0.0,
  "dso": 0, "dio": 0, "dpo": 0,
  "dl_ebitda": 0.0,
  "roic_5a": [0,0,0,0,0],
  "receita_5a": [0,0,0,0,0],
  "margem_ebit_5a": [0.0,0.0,0.0,0.0,0.0]
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

