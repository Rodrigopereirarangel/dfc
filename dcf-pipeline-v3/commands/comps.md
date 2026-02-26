---
name: /comps
description: Análise de comparáveis (peers) com múltiplos, ROIC relativo, fade relativo.
arguments:
  - ticker: "Ticker da empresa"
---

# /comps [TICKER]

## Comportamento
1. Identificar 5-10 peers comparáveis (mesmo setor/mercado).
2. Comparar múltiplos: P/E, EV/EBITDA, P/B, EV/Revenue.
3. Comparar ROIC, margens, growth e fade rate.
4. Posicionamento relativo (premium/desconto justificado?).
5. Implied value por múltiplo de peers.

## Output
Relatório seguindo `templates/output-comps.md`.
