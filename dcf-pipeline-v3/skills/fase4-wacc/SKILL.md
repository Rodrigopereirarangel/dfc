---
name: "Fase 4 — Taxa de Desconto Dinâmica (WACC)"
description: |
  Calcula Ke, Kd, WACC com term structure e aplica Regra Penman.
  Triggers: "WACC", "custo de capital", "taxa de desconto", "beta"
---

# FASE 4 — TAXA DE DESCONTO DINÂMICA (WACC)

> **Entradas:** Estrutura de capital (Fase 1), Beta setorial de peers, NTN-B e ERP de `references/contexto-brasil.md`.
> **Regra Global:** Cada passo DEVE entregar os 5 Blocos Institucionais + Síntese §1–§5 + JSON Payload.

---

## Passo 4.1 — Custo do Equity (Ke)

**Ação:**
1. Risk-free: **NTN-B longa** (Brasil), IPCA+ real.
2. ERP: Damodaran forward-looking.
3. Beta: bottom-up (unlevered de peers via yfinance → relever pela estrutura-alvo).
4. Size premium, Country Risk Premium (CRP = EMBI+ em bps).
5. `Ke = Rf + β × ERP + Size + CRP`.
6. Alternativa: implied cost of capital via reverse DCF.
7. **⚠️ REGRA PENMAN**: se g > inflação + 1%, questionar se Ke não deveria ser maior.

**BLOCO 1 — Componentes do COE:**

| Componente | Valor | Fonte | Data | Observação |
|---|---|---|---|---|
| Rf (NTN-B longa, real) | X% | Tesouro Direto | [data] | IPCA+ |
| Rf (nominal) | X% | IPCA esperado X% | [data] | |
| ERP Brasil | X% | Damodaran [ano] | Jan/[ano] | Forward-looking |
| Beta unlevered (peers) | X | yfinance [tickers] | [data] | |
| Beta relevado (D/E target) | X | D/E = X% | [data] | |
| Size Premium | X% | — | — | Large cap BR |
| CRP | X% | EMBI+ [bps] | [data] | |
| **COE = Ke** | **X%** | CAPM | | |

**BLOCO 2 — Intuição do COE para Decisão de Investimento:**
Traduzir: "Um COE de X% significa que você exige que [empresa] remunere X% ao ano para compensar o risco. A NTN-B paga X% real + IPCA com risco zero. O prêmio sobre o risco zero é de Xpp. Isso é [generoso / justo / exigente] para este ativo neste momento do ciclo?"

**BLOCO 3 — Sensibilidade do COE no Fair Value + DataViz:**

| COE utilizado | Fair Value (cenário base) | vs. Preço atual | Implicação |
|---|---|---|---|
| X% (nosso, conservador) | R$X | X% | Nossa estimativa |
| X% (sell-side bull) | R$X | X% | Preço-alvo bull |
| X% (teórico mínimo) | R$X | X% | Cenário extremo |

💡 Cada 1pp de COE impacta ~R$X/ação no fair value.

> **📊 Instrução DataViz — Term Structure of Discount Rates:**
> Gráfico de linhas por anos do período explícito (2026-2030):
> - **Linha Azul Marinho sólida:** WACC de cada ano (pode variar conforme desalavancagem).
> - **Linha Cinza tracejada:** Ke (Custo do Equity) estático.
> - **Linha Âmbar tracejada fino:** g projetado da Fase 3 (para verificar Regra Penman visualmente).
> - **Zona de Alerta Penman:** área sombreada vermelha quando g > Rf + 1%.
> - Legenda horizontal no topo. Eixo Y: % (0–20%).

**BLOCO 4 — Debate: COE Correto para Este Ativo:**
Por que usamos X% e não Y%? Quais 2 argumentos mais fortes para COE mais baixo (posição bull)? Por que não os aceitamos?

**BLOCO 5 — Analogia de Erro no COE:**
Caso onde o mercado usou COE incorreto (muito baixo em 2012-2021, muito alto em pico de pessimismo). O que aconteceu com os retornos?

```
╔══════════════════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — Passo 4.1                           ║
╚══════════════════════════════════════════════════════════════════╝
```

**Referências:**
- **P22** (Cost of Capital: Practical Guide): passo-a-passo Rf → ERP → β → Size → CRP → Ke.
- **Livro 19** (Andrew Ang): Cap. 6-10 — Factor Decomposition.
- **Livro 01** (Penman): regra "+1% growth → +1% required return".
- **Livro 59** (Renda Fixa Brasil): NTN-B como risk-free.

---

## Passo 4.2 — Custo da Dívida, Estrutura de Capital e WACC

**Ação:**
1. Kd = yield to worst (não taxa contábil).
2. Tax shield: Kd × (1−t) com taxa efetiva.
3. Target capital structure.
4. `WACC = Ke × (E/(D+E)) + Kd×(1−t) × (D/(D+E))`.
5. **WACC term structure**: se a empresa desalavanca com ramp-up, ajustar por período.
6. Para seguradoras/financeiras: por que o COE puro é o denominador correto (float ≠ dívida financeira).
7. Regra Penman aplicada: g projetado > inflação + 1%? Questionar WACC.

**BLOCO 1 — WACC Consolidado:**

| Componente | Para Industriais | Para Seguradoras/Financeiras |
|---|---|---|
| Ke | X% | X% (COE puro) |
| Kd after-tax | X% | N/A (equity-funded) |
| WACC | X% | = COE: X% |
| Penman Test | g=X% vs threshold X% | [OK / ⚠️ QUESTIONAR] |

**BLOCO 2 — Por que WACC vs COE Puro para Este Setor:**
Se seguradora: o float de prêmios não é dívida financeira — é passivo atuarial. Detalhar por que WACC convencional não se aplica.

**BLOCO 3 — Regra Penman Aplicada + DataViz:**
Detalhe do teste: g projetado = X%, threshold = inflação + 1% = X%. Conclusão com justificativa.

> **📊 Instrução DataViz — Decomposição do WACC (Waterfall de Prêmios):**
> Gráfico de cascata vertical (horizontal style):
> - **Barras empilhadas:** Rf → + ERP → + Beta Adj. → + Size Premium → + CRP → = Ke Final.
> - Cores progressivas escurecendo do Rf (cinza claro) até o Ke final (azul marinho).
> - Rótulo de % em cada componente. Total final destacado em negrito.

**BLOCO 4 — Sensibilidade WACC × Estrutura de Capital:**
Se a empresa mudar seu leverage, como muda o WACC? Qual o leverage ótimo teórico?

**BLOCO 5 — Analogia de Erro de Taxa de Desconto:**
Ciclo de juros baixos (2012-2021) → mercado usou COE de 10-11%. O que aconteceu quando Selic subiu para 13-14%?

```
╔══════════════════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — Fase 4 Completa                     ║
╚══════════════════════════════════════════════════════════════════╝
§1 O COE e WACC escolhidos são defensáveis frente ao CIO?
§2 Impacto de ±1pp de COE no fair value?
§3 A Regra Penman foi verificada? Resultado?
§4 Existe viés de ancoragem no COE utilizado?
§5 O mercado está usando COE diferente? Isso cria oportunidade?
```

**Referências:**
- **Livro 87** (McKinsey): Cap. 8 — Cost of Capital prático.
- **Livro 01** (Penman): P/B=1 test.
- **P13** (Cost of Capital): WACC em regimes easy money.

**JSON Payload ao final da Fase 4:**
```json
```json
{
  "fase": "F4_COMPLETA",
  "rf_real_ntnb": 0.0,
  "rf_nominal": 0.0,
  "erp_brasil": 0.0,
  "beta_relevado": 0.0,
  "size_premium": 0.0,
  "crp": 0.0,
  "ke_coe": 0.0,
  "kd_after_tax": 0.0,
  "wacc": 0.0,
  "penman_test_aprovado": true,
  "g_projetado": 0.0,
  "penman_threshold": 0.0
}
```
```

---

## ✅ CHECKLIST DE COMPLIANCE — VALIDAÇÃO OBRIGATÓRIA ANTES DE AVANÇAR

Antes de passar para a próxima fase, o Agente AI DEVE verificar e imprimir este checklist PREENCHIDO com **[V]** (Verdadeiro) ou **[F]** (Falso) em sua resposta:

```text
[CHECKLIST DE COMPLIANCE DO AGENTE — FASE F4]
[V/F] Eu abri e li integralmente este arquivo SKILL.md usando a minha ferramenta de leitura de arquivos.
[V/F] Eu executei TODOS os sub-passos desta fase (não pulei nenhum).
[V/F] Eu entreguei os 5 Blocos (Diagnóstico / Narrativa / DataViz / Trade-off / Analogia) em CADA sub-passo.
[V/F] Eu incluí a instrução DataViz específica (tipo de gráfico + paleta + eixos) no BLOCO 3 de cada passo.
[V/F] Eu apresentei a Síntese Institucional (§1 a §5) ao final desta fase.
[V/F] Eu fechei a resposta gerando o bloco ```json com a taxonomia exata desta fase.
```

**Se qualquer item for (F):** PARE. Não avance. Corrija a sua resposta e reentregue antes de prosseguir para a próxima fase.

Validação automática: `python scripts/validate_compliance.py --clipboard --fase F4`
