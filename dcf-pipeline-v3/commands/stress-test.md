---
name: /stress-test
description: Executa Fase 7 (Stress Test & Validação Cruzada) isolada.
arguments:
  - ticker: "Ticker da empresa"
---

# /stress-test [TICKER]

## Comportamento
1. Fat Tails e cenários extremos (3+ σ).
2. Via Negativa: condições de invalidação curto/médio/longo prazo.
3. Auditoria de vieses cognitivos.
4. Validação cruzada: Reverse DCF × DCF × EPV × Múltiplos.
5. QMJ Score (Quality Minus Junk).
6. Análise de sentimento de mercado vs modelo.
7. Tabela de sensibilidade 7×7.

## Output
Relatório seguindo `templates/output-stress-test.md`.
