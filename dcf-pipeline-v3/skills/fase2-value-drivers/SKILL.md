---
name: "Fase 2 — Decomposição de Value Drivers"
description: |
  ROIC/ROIIC, fade rate, Red Queen capex, unit economics e tornado chart.
  Triggers: "drivers de valor", "ROIC", "fade", "capex", "Red Queen"
---

# FASE 2 — DECOMPOSIÇÃO DE VALUE DRIVERS

> **Regra Global:** Cada passo DEVE entregar os 5 Blocos Institucionais + Síntese §1–§5 + JSON Payload.

---

## Passo 2.1 — ROIC, Fade Rate e ROE Decomposition

**Ação:**
1. ROIC ajustado para intangíveis: NOPAT ajustado / Invested Capital ajustado.
2. Decompor: ROIC = NOPAT Margin × Capital Turnover.
3. ROIIC (Return on Incremental Invested Capital) dos últimos 3-5 anos.
4. Estimar fade rate: anos até ROIC → WACC (dados empíricos do setor). `fade rate = ln(2) / half-life empírica`.
5. Fade por segmento: consolidado = média ponderada.
6. CAP implícito no preço atual.

**BLOCO 1 — Painel ROIC e Fade por Segmento:**

| Segmento | ROIC Atual | COE | Spread | Half-Life Setorial | CAP Implícito | Avaliação |
|---|---|---|---|---|---|---|
| [Vertical 1] | X% | X% | Xpp | X anos | X anos | ✅/🟠/❗ |
| [Vertical 2] | X% | X% | Xpp | X anos | X anos | ✅/🟠/❗ |
| **Consolidado** | X% | X% | Xpp | X anos | X anos | |

**BLOCO 2 — Trajetória de Fade por Componente:**
- Componente 1 — Fonte cíclica do ROE atual: qual é, por que irá diminuir, em quanto tempo?
- Componente 2 — Fonte estrutural: por que pode ser sustentada? Evidências.
- Componente 3 — Fonte em construção: qual vertical expande o ROE? Risco de execução?
- Componente 4 — ROIIC dos últimos 3 anos: revela qualidade do crescimento?

**BLOCO 3 — Mapa de Fade por Cenário + DataViz:**

| Ano | ROE Base | ROE Bear | ROE Bull | Premissa divergente |
|---|---|---|---|---|
| 2025A | X% | X% | X% | — |
| 2027E | X% | X% | X% | [premissa] |
| 2030E | X% | X% | X% | [premissa] |
| Terminal | X% | X% | X% | [premissa] |

> **📊 Instrução DataViz — Gráfico de Fade ROIC → WACC:**
> Gráfico de linhas convergentes:
> - **Linha Azul Marinho (#003366) sólida:** ROIC projetado Base, com área sombreada representando range Bull-Bear.
> - **Linha Cinza tracejada (#A0A0A0):** WACC (custo de capital — a linha de criação zero de valor).
> - **Área Verde entre ROIC e WACC:** CAP — período de vantagem competitiva criando valor.
> - **Área Vermelha quando ROIC < WACC:** destruição de valor.
> - **Marcador vertical âmbar (#CBA052):** indicando o CAP implícito no preço atual.
> - X: 2020–2035. Paleta Bloomberg. Sem gridlines verticais.

💡 O CAP implícito no preço é X anos. Base rate setorial: Y anos. A diferença (X−Y) está justificada por qual característica específica?

**BLOCO 4 — O que o CAP Implícito diz sobre o Preço:**
O bull case precisa de que premissa específica para se verificar? Probabilidade?

**BLOCO 5 — Analogia de Fade:**
2 empresas que passaram por fade similar de ROE. Como o mercado precificou: cedo ou tarde?

```
╔══════════════════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — Passo 2.1                           ║
╚══════════════════════════════════════════════════════════════════╝
```

**Referências:**
- **P24** (Return on Invested Capital): 6 variações de cálculo.
- **P19** (ROIC and Investment Process): persistência ROIC 1990-2022 por setor.
- **Livro 06/84** (Expectations Investing): CAP, fade rates.
- **P41** (Math of Value and Growth): ROIIC framework.

---

## Passo 2.2 — Capex Manutenção vs. Crescimento (Red Queen)

**Ação:**
1. Separar capex por 3 métodos: D&A+inflação / Red Queen / Guidance com haircut.
2. Asset age analysis: PP&E líquido / PP&E bruto → se < 0.4 = sub-investimento → 🟠
3. CAPEX_total = CAPEX_manutenção + CAPEX_expansão (todos os anos).

**BLOCO 1 — Decomposição do Capex:**

| Componente | Método 1 (D&A+inflação) | Método 2 (Red Queen) | Método 3 (Guidance c/ haircut) | Média utilizada |
|---|---|---|---|---|
| Capex Manutenção | R$X | R$X | R$X | R$X |
| Capex Crescimento | R$X | R$X | R$X | R$X |
| **Total** | R$X | R$X | R$X | R$X |
| Asset Age (PP&E líq/bruto) | — | X% | — | ✅ se >40% |

**BLOCO 2 — O que o Red Queen revela sobre o negócio:**
- Para seguradoras/financeiras: o equivalente setorial ao capex de manutenção (provisões técnicas, capital regulatório). Qual o número real?
- Capex de crescimento: projetos específicos com ROIC esperado.
- FCFF real (após capex de manutenção) vs. FCFF aparente.

**BLOCO 3 — FCFF Real vs. FCFF Aparente + DataViz:**

| Métrica | Valor Aparente | Ajuste Red Queen | Valor Real | Impacto no Valuation |
|---|---|---|---|---|
| FCFF 2025E | R$X | −R$X | R$X | −R$X/ação |
| FCF Yield | X% | — | X% | |

> **📊 Instrução DataViz — Barra Simples FCFF Aparente vs Real:**
> Gráfico de barras verticais duplas por ano (2022-2026E):
> - **Barra esquerda (Azul Marinho):** FCFF Aparente.
> - **Barra direita (Vermelho Escuro #8B0000):** FCFF Real após Capex de Manutenção Red Queen.
> - **Delta em %, rótulo no topo de cada barra.**

**BLOCO 4 — Sub-investimento ou Super-investimento?**
Asset age < 40% indica sub-investimento. Capex > receita indica expansão agressiva. Qual o risco de cada extremo para o ROIC futuro?

**BLOCO 5 — Analogia Red Queen:**
Empresa que subestimou capex de manutenção. O que aconteceu com o FCFF real?

```
╔══════════════════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — Passo 2.2                           ║
╚══════════════════════════════════════════════════════════════════╝
```

**Referências:**
- **P31** (Red Queen): framework completo, 3 métodos.
- **P32** (Categorizing for Clarity): separação investment vs. maintenance.

---

## Passo 2.3 — Unit Economics por Vertical

**Ação:**
1. Margem incremental e Operating Leverage (DOL).
2. LTV, CAC, LTV/CAC, payback period.
3. Churn rate, cohort retention, NRR — se NRR > 100% = expansão orgânica; < 90% = red flag.
4. Sinergia ou canibalismo entre verticais.

**BLOCO 1 — Painel Comparativo da Vertical:**

| Métrica | [Empresa]/[Vertical] | Peer 1 | Peer 2 | Mediana Setor |
|---|---|---|---|---|
| Crescimento receita | X% | X% | X% | X% |
| Margem operacional | X% | X% | X% | X% |
| ROE estimado da vertical | X% | X% | X% | X% |
| NRR / Retenção | X% | X% | X% | X% |

**BLOCO 2 — Dinâmica Competitiva da Vertical:**
- Posicionamento: ganhando ou perdendo market share?
- Pricing power: repassa inflação de custos? Evidência.
- CAC/LTV: unidade econômica melhorando ou piorando?

**BLOCO 3 — Contribuição ao ROE Consolidado + DataViz:**

| Vertical | Lucro 2025E | % Lucro Total | ROE Vertical | ROE se crescer 20% |
|---|---|---|---|---|
| [V1] | R$X | X% | X% | +X pp consolidado |

> **📊 Instrução DataViz — Stacked Bar por Vertical:**
> Gráfico de barras empilhadas (anos 2022–2028E):
> - **Cada cor (paleta azul/cinza/âmbar)** representa uma vertical de negócio.
> - **Linha sobreposta:** Margem líquida consolidada %.
> - Identificar visualmente como o mix de verticais evoluiu.

**BLOCO 4 — Sinergia ou Canibalismo entre Verticais:**
As verticais se reforçam (flywheel) ou competem por recursos? LTV incremental do cross-sell vs. CAC de aquisição pura.

**BLOCO 5 — Analogia de Diversificação:**
Empresa que executou estratégia similar. Quais verticais entregaram? Quais decepcionaram?

```
╔══════════════════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — Passo 2.3                           ║
╚══════════════════════════════════════════════════════════════════╝
```

**Referências:**
- **P36** (Customer Economics): LTV, CAC, cohort, NRR.
- **Livro 06/84** (Expectations Investing): Cap. 4.

---

## Passo 2.4 — Sensibilidade dos Drivers e Causalidade (Tornado Chart)

**Ação:**
1. Tornado chart: quais variáveis mais impactam o fair value?
2. Distinguir correlação de causalidade (DAG — grafo acíclico dirigido).
3. Filtrar sinal do ruído: premissas não podem ser forjadas sobre correlações espúrias.
4. Identificar os 2-3 drivers que "fazem ou quebram" o case.

**BLOCO 1 — Tornado Chart Institucional:**

| Rank | Driver | Impacto +1σ | Impacto −1σ | Controlável? |
|---|---|---|---|---|
| 🎯 1 | [Driver mais crítico] | +R$X/ação | −R$X/ação | Sim/Parcial/Não |
| 2 | [Driver 2] | +R$X/ação | −R$X/ação | Sim/Parcial/Não |
| 3 | [Driver 3] | +R$X/ação | −R$X/ação | Sim/Parcial/Não |
| 4 | [Driver 4] | +R$X/ação | −R$X/ação | Sim/Parcial/Não |
| 5 | [Driver 5] | +R$X/ação | −R$X/ação | Sim/Parcial/Não |

**BLOCO 2 — Análise de Causalidade do Driver #1:**
Cadeia causal que conecta esse driver ao fair value — não correlação, mas mecanismo econômico preciso.

**BLOCO 3 — Cenário de Combinação Adversa + DataViz:**
Se os 3 drivers mais negativos se materializam simultaneamente: qual o fair value? Qual a probabilidade da combinação?

> **📊 Instrução DataViz — Tornado Chart Horizontal:**
> Gráfico de barras horizontais simétricas (padrão sell-side):
> - **Drivers no eixo Y** (ordenados do maior para o menor impacto).
> - **Barra esquerda (Vermelho Escuro):** impacto negativo (−1σ), em R$/ação.
> - **Barra direita (Azul Marinho):** impacto positivo (+1σ), em R$/ação.
> - **Linha central (Cinza tracejada):** Base Case R$/ação.
> - **🎯 Driver #1 destacado** com borda âmbar (#CBA052).
> - Rótulos com R$/ação no extremo de cada barra. Sem gridlines verticais.

**BLOCO 4 — O Driver que o Mercado está Ignorando:**
Existe um driver que o modelo identifica como crítico mas o consenso não monitora? Por quê está fora do radar?

**BLOCO 5 — Analogia de Driver Crítico Subestimado:**
Caso onde o mercado ignorou o driver principal até ser tarde demais.

```
╔══════════════════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — Fase 2 Completa                     ║
╚══════════════════════════════════════════════════════════════════╝
§1 Qual o perfil real de criação de valor da empresa?
§2 O preço atual está precificando o CAP correto?
§3 Confiança nas estimativas de ROIC e Fade?
§4 Quais drivers são os mais críticos para a Fase 3?
§5 Existe assimetria de informação nos drivers não monitorados?
```

**Referências:**
- **Livro 52** (The Book of Why, Pearl): Cap. 1-3 — Causalidade vs Correlação.
- **Livro 54** (The Signal and the Noise, Nate Silver).
- **Livro 44** (Tjia): sensitivity analysis.

**JSON Payload ao final da Fase 2:**
```json
<!-- JSON_PAYLOAD
{
  "fase": "F2_COMPLETA",
  "roic_atual": 0.0,
  "cap_implicito_anos": 0,
  "cap_base_rate_setor_anos": 0,
  "fcff_aparente": 0,
  "fcff_real_red_queen": 0,
  "asset_age_pct": 0.0,
  "tornado_drivers": [
    {"rank": 1, "driver": "", "impacto_positivo": 0.0, "impacto_negativo": 0.0},
    {"rank": 2, "driver": "", "impacto_positivo": 0.0, "impacto_negativo": 0.0},
    {"rank": 3, "driver": "", "impacto_positivo": 0.0, "impacto_negativo": 0.0}
  ]
}
-->
```

---

## ✅ CHECKLIST DE COMPLIANCE — VALIDAÇÃO OBRIGATÓRIA ANTES DE AVANÇAR

Antes de passar para a próxima fase, o Agente AI DEVE verificar e imprimir este checklist PREENCHIDO com **[V]** (Verdadeiro) ou **[F]** (Falso) em sua resposta:

```text
[CHECKLIST DE COMPLIANCE DO AGENTE — FASE F2]
[V/F] Eu abri e li integralmente este arquivo SKILL.md usando a minha ferramenta de leitura de arquivos.
[V/F] Eu executei TODOS os sub-passos desta fase (não pulei nenhum).
[V/F] Eu entreguei os 5 Blocos (Diagnóstico / Narrativa / DataViz / Trade-off / Analogia) em CADA sub-passo.
[V/F] Eu incluí a instrução DataViz específica (tipo de gráfico + paleta + eixos) no BLOCO 3 de cada passo.
[V/F] Eu apresentei a Síntese Institucional (§1 a §5) ao final desta fase.
[V/F] Eu fechei a resposta gerando o bloco <!-- JSON_PAYLOAD --> com a taxonomia exata desta fase.
```

**Se qualquer item for (F):** PARE. Não avance. Corrija a sua resposta e reentregue antes de prosseguir para a próxima fase.

Validação automática: `python scripts/validate_compliance.py --clipboard --fase F2`
