---
name: /management-check
description: Executa Fase 2.5 isolada — análise de gestão e capital allocation.
arguments:
  - ticker: "Ticker da empresa"
---

# /management-check [TICKER]

## Comportamento
1. Levantar guidances passados (5-10 anos).
2. Gerar Score de Credibilidade (1-5) e % Haircut.
3. Mapear alocação de capital (10 anos).
4. Avaliar buybacks, M&A, dividendos.
5. Mapear projetos em andamento com S-curve.

## Output
Relatório seguindo `templates/output-management-check.md`.
