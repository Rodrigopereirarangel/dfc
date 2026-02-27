---
name: "Fase 0 — Inteligência Competitiva, Enquadramento & Expectativa de Mercado"
description: |
  Mapeia o modelo de negócio, classifica o moat, faz reverse DCF,
  analisa sentimento de mercado e traduz narrativa em drivers numéricos.
  Triggers: "modelo de negócio", "moat", "vantagem competitiva", "reverse DCF"
---

# FASE 0 — INTELIGÊNCIA COMPETITIVA & ENQUADRAMENTO

> **Regra Global:** Cada passo desta fase DEVE entregar os 5 Blocos Institucionais + Síntese §1–§5.
> Consultar a Arquitetura Universal no `SKILL.md` raiz.

---

## Passo 0.1 — 5 Forças de Porter + Tipologia do Moat + Nota de Durabilidade

**Ação:**
1. Mapear as 5 Forças de Porter para a indústria da empresa.
2. Classificar tipo do Moat: Escala, Switching Costs, Network Effects, Intangíveis, Custo de Produção.
3. Usar checklist completo de "Measuring the Moat" (P09): fontes de valor adicionado, pricing power, regulação, marcas.
4. Emitir **Nota de Durabilidade (1 a 10)** com justificativa explícita.
5. Identificar fraquezas do moat com timeline e probabilidade.
6. Life Cycle via DFC (CFO/CFI/CFF). Se Declínio → EPV como valuation principal.

**BLOCO 1 — Diagnóstico Executivo das 5 Forças:**

Gerar tabela por força:

| Força | Intensidade | Tendência 3–5A | Segmento + exposto | Impacto fair value |
|---|---|---|---|---|
| Rivalidade Setorial | 🔴/🟠/🟢 + adjetivo | ↗️/→/↘️ + evento | Vertical (% receita) | R$X/ação por pp |
| Ameaça de Entrantes | ... | ... | ... | ... |
| Poder dos Fornecedores | ... | ... | ... | ... |
| Poder dos Compradores | ... | ... | ... | ... |
| Ameaça de Substitutos | ... | ... | ... | ... |

**BLOCO 2 — Narrativa por Vetor de Pressão:**
Para cada força relevante (≥ 🟠), blockquote com: evidência quantitativa + mecanismo de transmissão + limite temporal da ameaça.

**BLOCO 3 — Impacto Quantitativo + DataViz:**
- Tabela de cenários: base/stress moderado/stress severo — impacto no lucro (R$mi) e no fair value (R$/ação).
- 💡 Insight não óbvio sobre a força mais subestimada pelo mercado.

> **📊 Instrução DataViz — Radar Chart (Spider Plot) de Vantagem Competitiva:**
> Plotar duas séries sobrepostas no mesmo gráfico de teia de 5 eixos (uma por Força de Porter):
> - **Série Azul Marinho (#003366):** Score da empresa (1-10) em cada força.
> - **Série Cinza (#A0A0A0) com hachura:** Score médio do setor (base rate).
> - **Área superior à Cinza = vantagem; Área inferior = exposição.**
> - Paleta: `["#003366", "#A0A0A0"]`. Sem bordas externas. Legenda ao topo esquerdo.

**BLOCO 4 — Dilema Estratégico do Management:**
Tabela: 3 estratégias de resposta possíveis | vantagem | custo | qual a empresa escolheu historicamente | qual deveria escolher.

**BLOCO 5 — Analogia Histórica:**
Empresa do setor (nomeada) que enfrentou dinâmica competitiva análoga. Período. Resultado. Lição transferível.

```
╔══════════════════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — Passo 0.1                           ║
╚══════════════════════════════════════════════════════════════════╝
§1 O que revelou sobre o posicionamento competitivo?
§2 Impacto no fair value e no prêmio de moat implícito?
§3 Nível de confiança (fato / inferência / hipótese)?
§4 2-3 perguntas acionáveis para as próximas fases?
§5 Assimetria de informação identificada?
```

**Referências:**
- **Livro 05** (Magretta/Porter): Cap. 2 — 5 Forças; Cap. 5 — Trade-offs.
- **Livro 85** (Greenwald, Competition Demystified): Cap. 2 — Cola Wars; Cap. 6 — Supply Advantage.
- **Livro 04** (Jim Collins): Cap. 5 — Hedgehog; Cap. 8 — Flywheel.
- **P09** (Measuring the Moat 2024): checklist 12 itens, ROIC por indústria, life cycle.
- **P45** (Measuring the Moat 2016): persistência ROIC por 5/10/15 anos.

**JSON Payload ao final do Passo 0.1:**
```json
<!-- JSON_PAYLOAD
{
  "fase": "F0_P01",
  "forças_porter": {
    "rivalidade": {"score_empresa": 0, "score_setor": 0},
    "entrantes": {"score_empresa": 0, "score_setor": 0},
    "fornecedores": {"score_empresa": 0, "score_setor": 0},
    "compradores": {"score_empresa": 0, "score_setor": 0},
    "substitutos": {"score_empresa": 0, "score_setor": 0}
  },
  "nota_durabilidade_moat": 0,
  "tipo_moat": "Switching Costs / Escala / Network / Intangível / Custo"
}
-->
```

---

## Passo 0.2 — Reverse DCF + MEROI

**Ação:**
1. Buscar preço atual via yfinance.
2. Resolver reversamente: qual `g` (growth) e `ROIC` estão embutidos no preço atual?
3. Calcular MEROI = (EV − PV of FCFs) / Reinvestment.
4. Extrair ERP implícito no preço e comparar com Damodaran.
5. Comparar premissas implícitas vs. base rates empíricas do setor.
6. Emitir diagnóstico: O mercado está **Otimista**, **Pessimista** ou **Justo**?

**BLOCO 1 — Snapshot de Premissas Implícitas:**

| Premissa | Implícito no preço | Base rate setorial | Diagnóstico |
|---|---|---|---|
| ROE sustentado | X% | X–X% histórico | 🔴/🟠/✅ |
| g terminal | X% | X% PIB nominal BR | 🔴/🟠/✅ |
| CAP implícito | X anos | X–X anos (P45) | 🔴/🟠/✅ |
| ERP implícito | X% | X% Damodaran | 🔴/🟠/✅ |
| MEROI | X× | Mediana setor X× | 🔴/🟠/✅ |

**BLOCO 2 — Decomposição do que o Mercado Está Comprando:**
- Vetor 1: Premissa de crescimento implícita e o que seria necessário para justificá-la.
- Vetor 2: Premissa de rentabilidade (ROE implícito) vs. histórico.
- Vetor 3: Duração da vantagem competitiva implícita (CAP vs. base rate).
- Vetor 4: Risco subestimado (ERP comprimido vs. realidade macro).

**BLOCO 3 — Mapa de Sensibilidade do Preço Atual + DataViz:**
Tabela: se cada premissa implícita desviar 1pp para o lado conservador, qual o impacto no preço justo?

> **📊 Instrução DataViz — Tabela Bridge de Premissas Implícitas:**
> Gerar tabela colorida de duas colunas comparando "Implícito no Preço" vs. "Nossa Estimativa"
> com semáforo nas células: Verde (implícito < estimativa), Amarelo (neutro), Vermelho (implícito > estimativa).

**BLOCO 4 — Diagnóstico da Assimetria:**
O mercado está Otimista/Justo/Pessimista? Qual premissa singular mais responsável? Se estiver errada, qual o preço justo?

**BLOCO 5 — Analogia de Reverse DCF:**
Ativo similar que exibia premissas implícitas análogas. O que aconteceu quando as premissas se normalizaram? Velocidade e magnitude.

```
╔══════════════════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — Passo 0.2                           ║
╚══════════════════════════════════════════════════════════════════╝
```

**Referências:**
- **Livro 06/84** (Mauboussin, Expectations Investing): Cap. 3-5 — Price-Implied Expectations.
- **P34** (Everything Is a DCF Model): traduzir múltiplo → premissa de DCF.
- **P37** (MEROI): fórmula e aplicação.
- **P01** (Bayes and Base Rates): base rate como prior.

**JSON Payload ao final do Passo 0.2:**
```json
<!-- JSON_PAYLOAD
{
  "fase": "F0_P02",
  "preco_atual": 0,
  "g_implicito": 0,
  "roic_implicito": 0,
  "meroi": 0,
  "erp_implicito": 0,
  "diagnostico_mercado": "Otimista / Justo / Pessimista"
}
-->
```

---

## Passo 0.3 — Análise de Sentimento e Expectativas de Mercado

**Ação:**
1. Via yfinance: buscar short interest, volume anômalo, open interest de opções, P/E histórico.
2. Mapear divergências do sell-side: comparar Price Targets e premissas das casas de análise.
3. Avaliar se dispersão de analistas cria oportunidade de alpha.
4. Documentar alfa-oportunidade baseada em divergência sentimento vs fundamentos.

**BLOCO 1 — Mapa de Divergências do Sell-Side:**

| Casa | Recomendação | PT | Lucro E | Premissa divergente principal |
|---|---|---|---|---|
| [Casa 1] | Compra | R$X | R$X bi | ROE terminal X% |
| [Casa 2] | Neutro | R$X | R$X bi | COE X% |
| Nosso Modelo | — | EV R$X | R$X bi | COE X%, ROE fade |

**BLOCO 2 — Anatomia da Divergência:**
- Vetor 1: Qual premissa separa o bull do bear? Quantifique em R$ ou pp.
- Vetor 2: Por que o bull está otimista? Evidência.
- Vetor 3: Por que o bear está conservador? Evidência.
- Vetor 4: Qual das visões está mais próxima da nossa e por quê?

**BLOCO 3 — Análise de Reação do Mercado + DataViz:**
Como a ação se comportou nos últimos 4 resultados vs. expectativa vs. preço?

> **📊 Instrução DataViz — Short Interest e P/E Histórico Bandas:**
> Gráfico de linha dupla: P/E atual (linha azul) + banda histórica ±1σ (área cinza).
> Segunda linha: Short Interest como % do Float (eixo direito, cor âmbar #CBA052).

**BLOCO 4 — Alpha-Oportunidade ou Armadilha?**
A dispersão de analistas cria oportunidade? Ou o consenso converge para patamar sem upside? Julgamento explícito.

**BLOCO 5 — Analogia de Divergência de Sentimento:**
Ativo similar onde divergência foi resolvida. Quem estava certo? Que dado trimestral encerrou o debate?

```
╔══════════════════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — Passo 0.3                           ║
╚══════════════════════════════════════════════════════════════════╝
```

**Referências:**
- **P15** (Pattern Recognition): quando padrões funcionam.
- **P43** (Dispersion and Alpha): dispersão como oportunidade.
- **P44** (BIN There, Done That): superforecasting aplicado.

---

## Passo 0.4 — Narrativa → Números (Bridge PR/FAQ) + Pre-mortem (Inversão)

**Ação:**
1. Traduzir Narrativa em Números: 1 frase = 1-3 drivers quantificáveis.
2. **Aplicar INVERSÃO (pre-mortem):** listar as razões pelas quais o investimento pode falhar.
3. **Calcular EVPI** (Valor da Informação Perfeita): decidir onde vale investir mais tempo de análise.
4. FAQ: As 10 perguntas mais difíceis que um CIO experiente faria.

**BLOCO 1 — Mapa de Pontos de Falha:**

| Ponto de Falha | Tipo | Probabilidade | Timeline | Severidade |
|---|---|---|---|---|
| [Falha 1] | Cíclico | X% | 0–2a | 🔴/🟠/🟡 |
| [Falha 2] | Estrutural | X% | 2–5a | 🔴/🟠/🟡 |

**BLOCO 2 — Narrativa de Cada Cenário de Falha Crítico:**
Para cada falha 🔴 ou 🟠:
- T+1: o que acontece primeiro?
- T+2–4: como se propaga? Impacto no P&L?
- T+5–8: como o mercado precifica? Preço no pior momento?

**BLOCO 3 — Drivers Quantificáveis + DataViz:**
Lista dos 3–5 drivers que "fazem ou quebram" o case com valor base / otimista / pessimista / impacto por unidade de variação.

> **📊 Instrução DataViz — Mapa de Probabilidade de Falha:**
> Gráfico de bolhas: Eixo X = Probabilidade (%), Eixo Y = Severidade financeira (R$mi),
> Tamanho da bolha = Timeline (anos). Cor: 🔴 Vermelho escuro, 🟠 Laranja, 🟡 Amarelo.

**BLOCO 4 — EVPI — Onde Focar Mais Análise:**
Ranking por valor esperado da informação perfeita. Onde vale aprofundar.

**BLOCO 5 — Analogia de Pre-mortem:**
Empresa que falhou pela razão mais provável de falha desta. O que o pre-mortem teria previsto?

```
╔══════════════════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — Fase 0 Completa                     ║
╚══════════════════════════════════════════════════════════════════╝
§1 Qual o panorama competitivo e estratégico da empresa?
§2 O preço atual reflete as premissas corretas?
§3 Nível de confiança geral nesta fase?
§4 Principais incertezas para as fases seguintes?
§5 Existe alfa nesta assimetria de informação identificada?
```

**Referências:**
- **Livro 11** (Damodaran, Narrative and Numbers): Cap. 2-3.
- **Livro 92** (Working Backwards): Cap. 4 — PR/FAQ.
- **Livro 08** (How to Measure Anything): Cap. 7 — EVPI.
- **Livro 67** (All I Want to Know, Bevelin): inversão e pre-mortem.

**JSON Payload ao final da Fase 0:**
```json
<!-- JSON_PAYLOAD
{
  "fase": "F0_COMPLETA",
  "nota_durabilidade_moat": 0,
  "diagnostico_mercado": "Otimista / Justo / Pessimista",
  "preco_atual": 0,
  "g_implicito": 0,
  "roic_implicito": 0,
  "erp_implicito": 0,
  "drivers_criticos": ["driver1", "driver2", "driver3"],
  "pontos_de_falha_graves": ["falha1", "falha2"]
}
-->
```
