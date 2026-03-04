---
name: "Fase 2.5 — Análise da Gestão: Track Record, Investimentos, Ramp-Ups"
description: |
  Avalia credibilidade do management, alocação de capital e projetos em andamento.
  Triggers: "gestão", "management", "capital allocation", "projetos", "ramp-up"
---

# FASE 2.5 — ANÁLISE DA GESTÃO

> **Regra Global:** Cada passo DEVE entregar os 5 Blocos Institucionais + Síntese §1–§5 + JSON Payload.

---

## Passo 2.5.1 — Histórico de Assertividade do Management

**Ação:**
1. Levantar guidances passados incluindo entrevistas e Teleconferências (5-10 anos).
2. Tabela: [Ano | Métrica | Guidance | Realizado | Desvio %].
3. Taxa de acerto, viés sistemático (otimista/pessimista), magnitude do erro.
4. Score de credibilidade: 1 (irrelevante) a 5 (altamente confiável).
5. **Haircut calculado**: descontar de todas as projeções.

**BLOCO 1 — Scorecard do Management:**

| Ano | Métrica | Guidance | Realizado | Desvio | Tipo de Desvio |
|---|---|---|---|---|---|
| 2023 | [KPI] | X | X | X% | Over/Under |
| 2024 | [KPI] | X | X | X% | Over/Under |
| 2025 | [KPI] | X | X | X% | Over/Under |

**Score de Credibilidade: X/5 | Haircut aplicado: X%**

**BLOCO 2 — Padrão de Comportamento Analítico:**
- Vetor 1: Há viés sistemático? (sempre otimista em X vertical, conservador em Y)
- Vetor 2: Magnitude do erro médio — é ruído ou sinal?
- Vetor 3: Under-promise/over-deliver ou over-promise/under-deliver?
- Vetor 4: Métricas Non-GAAP são "convenientemente" melhores que GAAP? Em quanto?

**BLOCO 3 — Impacto do Haircut nas Projeções + DataViz:**

| Métrica | Guidance Management | Com Haircut X% | Impacto Lucro | Impacto Fair Value |
|---|---|---|---|---|
| Receita 2026E | R$X | R$X | −R$X mi | −R$X/ação |
| Margem 2026E | X% | X% | −R$X mi | −R$X/ação |

> **📊 Instrução DataViz — Scorecard de Assertividade (Desvio vs. Guidance):**
> Gráfico de barras verticais por ano:
> - **Barra acima do zero (Azul Marinho):** Management entregou acima do guidance.
> - **Barra abaixo do zero (Vermelho Escuro):** entregou abaixo.
> - **Linha horizontal tracejada âmbar:** haircut médio calculado.
> - X: Anos. Anotar o KPI principal de cada year em rodapé.

**BLOCO 4 — Skin in the Game:**
O management compra ações com dinheiro próprio? Insider ownership como % do capital. Compara com peers.

**BLOCO 5 — Analogia de Management Quality:**
Empresa com management de track record similar. Como afetou o valuation no longo prazo?

```
╔══════════════════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — Passo 2.5.1                         ║
╚══════════════════════════════════════════════════════════════════╝
```

**Referências:**
- **P03** (Capital Allocation Updated): assessment skills, 5 usos × track record scoring.
- **Livro 55** (Arriscando a Própria Pele): Skin in the game.
- **Livro 04** (Jim Collins): Level 5 Leadership.

---

## Passo 2.5.2 — Capital Allocation Track Record

**Ação:**
1. Mapear alocação 10 anos: [Capex | M&A | Buybacks | Dividendos | Pagamento Dívida | Caixa].
2. ROIC incremental de cada M&A relevante.
3. Buybacks: comprou barato ou caro? Comparar preço médio vs. valor intrínseco.
4. Dividend payout sustentável? Crescente? Consistente?
5. Excess cash = oportunidade ou agency problem?

**BLOCO 1 — Histograma de Alocação de Capital (10 anos):**

| Uso do Capital | 2016–2020 | 2021–2025 | Tendência | Avaliação |
|---|---|---|---|---|
| Capex orgânico | X% | X% | ↗️/→ | ✅/🟠 |
| M&A | X% | X% | | |
| Buybacks | X% | X% | | |
| Dividendos + JCP | X% | X% | | |
| Acúmulo de caixa | X% | X% | | |

**BLOCO 2 — Qualidade de Cada Decisão de Alocação:**
- Capex: ROIC incremental dos últimos projetos acima ou abaixo do COE?
- M&A: aquisições entregaram o ROIC projetado? Em quanto tempo?
- Buybacks: feitos com ações baratas ou caras? Preço médio vs. EPV contemporâneo.

**BLOCO 3 — Excess Cash + DataViz:**

> **📊 Instrução DataViz — Stacked Bar Chart Capital Allocation 10A:**
> Gráfico de barras verticais 100% empilhadas por ano (2016-2025):
> - **Cada camada de cor** representa uso do capital: Capex (#003366), M&A (#336699), Buybacks (#4A4A4A), Dividendos (#A0A0A0), Caixa (#CBA052).
> - **Permite ver visualmente mudanças de regime** de alocação ao longo do tempo.
> - Legenda horizontal no topo. Rótulo % em cada segmento se > 10%.

**BLOCO 4 — A Decisão de Capital Allocation que Mais Preocupa:**
Qual alocação recente foi mais questionável? Impacto no ROE se desfeita?

**BLOCO 5 — Analogia de Capital Allocation:**
Empresa que foi de boa para excelente pela qualidade de alocação. E outra que destruiu valor por má alocação.

```
╔══════════════════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — Passo 2.5.2                         ║
╚══════════════════════════════════════════════════════════════════╝
```

**Referências:**
- **P03** (Capital Allocation Updated).
- **P28** (Wealth Transfers): buybacks como wealth transfer.
- **Livro 66** (Munger): allocation como decisão mais importante.

---

## Passo 2.5.3 — Projetos em Andamento e Ramp-Ups

**Ação:**
1. Listar todos os projetos em andamento.
2. Para cada projeto: Capex comprometido vs. investido, timeline, receita incremental, ROIC esperado.
3. Ramp-up curve: S-curve ou logistic curve; quantos trimestres/anos até maturação.
4. **Big project base rates**: poucos terminam on time/budget — usar como prior (P01). Haircut de 30-50%.

**BLOCO 1 — Inventário de Projetos:**

| Projeto | Fase | Investimento | ROIC Esperado | Risco | Status |
|---|---|---|---|---|---|
| [Projeto 1] | Ramp-up | R$X | X% | 🔴/🟠/✅ | [on-track / delayed] |
| [Projeto 2] | Operacional | R$X | X% | 🟠 | |

**BLOCO 2 — Análise de Ramp-up do Projeto Crítico:**
- Em que ponto do ramp-up estamos? S-curve posição.
- Cronograma original está sendo respeitado? Haircut de timeline (base rate: +30-50%).
- ROIC esperado é realista? (base rate: apenas 25% atingem ROIC projetado — P01).

**BLOCO 3 — Impacto nos Resultados + DataViz:**

| Projeto | Contribuição Lucro 2027E | Com haircut 50% ROIC | Diferença |
|---|---|---|---|
| [Projeto 1] | R$X | R$X | R$X |

> **📊 Instrução DataViz — S-Curves de Ramp-up por Projeto:**
> Gráfico de linhas logísticas (S-curve) por projeto:
> - **X:** Trimestres (T+0 a T+16).
> - **Y:** % da Receita Potencial Maturada (0–100%).
> - **Linha sólida Azul:** projeção conforme guidance.
> - **Linha tracejada Cinza:** com haircut de timeline +50%.
> - **Marcador âmbar (#CBA052):** posição atual no ramp-up.

**BLOCO 4 — O Projeto que Pode Surpreender Positivamente:**
Existe algum projeto early-stage não precificado pelo mercado? Upside se entregar?

**BLOCO 5 — Analogia de Ramp-up:**
Empresa que executou ramp-up similar. Quanto tempo levou vs. projetado?

```
╔══════════════════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — Fase 2.5 Completa                   ║
╚══════════════════════════════════════════════════════════════════╝
§1 Qual o nível de confiança no management e qual haircut aplicar?
§2 Impacto do haircut nas projeções da Fase 3?
§3 Os projetos em ramp-up são oportunidade ou risco de execução?
§4 O que observar nos próximos resultados trimestrais?
§5 O mercado está precificando adequadamente a qualidade do management?
```

**Referências:**
- **P01** (Bayes): base rates de big projects.
- **Livro 34** (Real Options): option to expand, abandon, delay.
- **Livro 08** (Measure Anything): reference class para projetos.

**JSON Payload ao final da Fase 2.5:**
```json
```json
{
  "fase": "F25_COMPLETA",
  "score_credibilidade_management": 0,
  "haircut_pct": 0.0,
  "alocacao_capital_5a": {
    "capex_pct": 0, "ma_pct": 0, "buybacks_pct": 0,
    "dividendos_pct": 0, "caixa_pct": 0
  },
  "projetos": [
    {"nome": "", "fase": "", "investimento": 0, "roic_esperado": 0.0, "risco": ""}
  ]
}
```
```

---

## ✅ CHECKLIST DE COMPLIANCE — VALIDAÇÃO OBRIGATÓRIA ANTES DE AVANÇAR

Antes de passar para a próxima fase, o Agente AI DEVE verificar e imprimir este checklist PREENCHIDO com **[V]** (Verdadeiro) ou **[F]** (Falso) em sua resposta:

```text
[CHECKLIST DE COMPLIANCE DO AGENTE — FASE F25]
[V/F] Eu abri e li integralmente este arquivo SKILL.md usando a minha ferramenta de leitura de arquivos.
[V/F] Eu executei TODOS os sub-passos desta fase (não pulei nenhum).
[V/F] Eu entreguei os 5 Blocos (Diagnóstico / Narrativa / DataViz / Trade-off / Analogia) em CADA sub-passo.
[V/F] Eu incluí a instrução DataViz específica (tipo de gráfico + paleta + eixos) no BLOCO 3 de cada passo.
[V/F] Eu apresentei a Síntese Institucional (§1 a §5) ao final desta fase.
[V/F] Eu fechei a resposta gerando o bloco ```json com a taxonomia exata desta fase.
```

**Se qualquer item for (F):** PARE. Não avance. Corrija a sua resposta e reentregue antes de prosseguir para a próxima fase.

Validação automática: `python scripts/validate_compliance.py --clipboard --fase F25`
