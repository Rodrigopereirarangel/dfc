---
name: /reverse-dcf
description: Extrai premissas implícitas no preço atual via engenharia reversa do DCF.
arguments:
  - ticker: "Ticker da empresa"
---

# /reverse-dcf [TICKER]

## Comportamento
1. Buscar preço atual via yfinance.
2. Executar o Passo 0.2 da Fase 0 isoladamente.
3. Resolver reversamente: qual `g`, `ROIC` e `ERP` estão embutidos no preço atual?
4. Calcular o MEROI (Market-Expected Return on Investment).
5. Comparar premissas implícitas vs. base rates empíricas (P01, P09, P19).
6. Emitir diagnóstico: Otimista / Pessimista / Justo.

## Output
Relatório seguindo `templates/output-reverse-dcf.md`.
