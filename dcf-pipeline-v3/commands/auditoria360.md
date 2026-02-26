---
name: /auditoria360
description: Executa a Fase 5A (GATE) isolada sobre modelo já construído.
---

# /auditoria360

## Comportamento
1. Executar todos os checks da Fase 5A sobre o modelo DCF já em memória.
2. Chain Check: Receita → NOPAT → FCFF.
3. Reconciliação segmento ⇄ consolidado.
4. Loop circular WACC ↔ Dívida (máx 5 iterações).
5. Capex Integrity (Red Queen).
6. Teste Penman: growth → risk.
7. Emitir alertas ❗/🟠 e veredito final.

## Output
Relatório seguindo `templates/output-auditoria360.md`.
