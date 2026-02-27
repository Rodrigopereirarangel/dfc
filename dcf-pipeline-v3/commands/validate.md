---
description: Valida se o output de uma fase segue o layout institucional obrigatório (5 Blocos, Síntese §1-§5, DataViz, JSON Payload, Checklist)
---

# /validate — Validador de Compliance DCF Pipeline

## O que faz

Valida se o texto de uma fase do DCF Pipeline segue a **Arquitetura Universal de Expansão** obrigatória.

Verifica presença de:
- ✅ 5 Blocos (Diagnóstico / Narrativa / DataViz / Trade-off / Analogia)
- ✅ Tabela snapshot no Bloco 1
- ✅ Blockquotes Claim→Evidence→Implication no Bloco 2
- ✅ Instrução DataViz + 💡 Insight no Bloco 3
- ✅ Síntese Institucional §1-§5
- ✅ JSON_PAYLOAD com campos numéricos
- ✅ Checklist preenchido com [V] ou [F] (não [?])

## Uso

**Validar um arquivo de output salvo:**
```bash
python scripts/validate_compliance.py --file output_payloads/[TICKER]_fase0.md --fase F0
```

**Validar texto da área de transferência (após copiar resposta do Claude):**
```bash
python scripts/validate_compliance.py --clipboard --fase F1
```

**Validar e exportar resultado em JSON:**
```bash
python scripts/validate_compliance.py --file output.md --fase F2 --json
```

**Saída rápida (só status):**
```bash
python scripts/validate_compliance.py --file output.md --fase F3 --quiet
```

## Interpretação do resultado

- **Exit 0 + ✅ APROVADO** → Fase compliant. Pode avançar.
- **Exit 1 + ❌ REPROVADO** → Lista os elementos ausentes. Reescrever antes de avançar.
- **🟠 AVISOS** → JSON com zeros ou marcadores [?] — preencher com dados reais.

## Integração no workflow

Após cada fase do /dfc, o agente DEVE rodar este comando e só avançar se Exit 0.

Registro do resultado no changelog:
```bash
python scripts/validate_compliance.py --file output.md --fase FX --json >> changelog/compliance_log.jsonl
```
