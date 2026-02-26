---
name: /dcf
description: Executa o pipeline DCF completo (Fase 0 → 8) para um ticker específico.
arguments:
  - ticker: "Ticker da empresa (ex: WEGE3, KLBN11)"
  - --fase: "Opcional. Executar fase específica (ex: --fase=3)"
  - --resumo: "Opcional. Retorna apenas conviction score + fair value"
  - --express: "Opcional. Pula Monte Carlo e Real Options"
---

# /dcf [TICKER]

## Comportamento
1. Receber o ticker e buscar dados primários (ITR/DFP oficial, yfinance para preço).
2. Executar sequencialmente as Fases 0 → 8, seguindo cada sub-skill.
3. A Fase 5A é um **GATE obrigatório** — se falhar, o pipeline **não avança**.
4. Ao final, preencher o template `templates/output-dcf-completo.md`.

## Parâmetros
- `--fase=N`: Executa apenas a fase N (ex: `--fase=3` para projeções).
- `--resumo`: Retorna apenas o Conviction Score e Fair Value final.
- `--express`: Pula Monte Carlo (Passo 3.4) e Real Options (Passo 6.2).

## Output
Relatório completo seguindo `templates/output-dcf-completo.md`.
