---
name: /monitor
description: Update trimestral — compara projeção vs realizado usando último ITR.
arguments:
  - ticker: "Ticker da empresa"
---

# /monitor [TICKER]

## Comportamento
1. Buscar último ITR oficial disponível (prioridade CVM/RI).
2. Comparar KPIs projetados vs realizados (Delta Sales, Delta EBITDA, Capex vs Red Queen plan).
3. Recalcular fair value e TIR implícita.
4. Aplicar atualização Bayesiana nos priors (L.37).
5. Log de hipóteses: quais premissas originais foram confirmadas/refutadas? (L.92 PR/FAQ tracking).
6. Verificar KPIs com alertas estilo OKR (L.91 Doerr).
7. Decision Success Rate: separar skill vs luck na decisão original (L.83).
8. Emitir decisão: Manter / Aumentar / Reduzir / Sair.
9. Registrar Bayesian update e feedback para melhoria contínua (P30).

## Referências (incorporadas da Fase 9 removida)
- **Livro 91** (Measure What Matters, Doerr): OKR + KPI + alertas gatilho.
- **Livro 92** (Working Backwards): PR/FAQ como hipóteses vivas com outcome tracking.
- **Livro 37** (Bayesian Statistics): updating com novos dados trimestrais.
- **Livro 83** (Success Equation, Mauboussin): DSR — Decision Success Rate, skill vs luck.
- **Livro 76** (Naval): automação e leverage.
- **Livro 01** (Penman): relatório de pontos de atenção.
- **P30** (Feedback): melhoria contínua de processo analítico.

## Output
Relatório seguindo `templates/output-monitor-trimestral.md`.
