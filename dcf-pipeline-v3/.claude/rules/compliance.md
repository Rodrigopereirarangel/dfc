# REGRA CRÍTICA: ARQUITETURA UNIVERSAL DE EXPANSÃO — DCF PIPELINE

**Esta regra é carregada automaticamente em toda sessão. Não pode ser ignorada.**

---

## 🔒 CONSTRAINT: Todo sub-passo de toda fase DO PIPELINE DCF DEVE obrigatoriamente seguir esta estrutura. Não há exceções.

Quando executar qualquer fase do DCF Pipeline (/dfc [TICKER] ou análise de fase individual), **ANTES de escrever qualquer análise**, declare:

```
📋 Template ativo: 5 Blocos × [N sub-passos] × Síntese §1-§5 × JSON Payload × Checklist [V/F]
```

---

## TEMPLATE OBRIGATÓRIO — PREENCHER PARA CADA SUB-PASSO

```markdown
### [FASE X.Y — NOME DO PASSO]

**BLOCO 1 — Diagnóstico Executivo**
| Campo | Valor | Status | Tendência |
|---|---|---|---|
| [métrica principal] | [dado com unidade] | 🔴/🟠/✅ | ↗️/→/↘️ |
| [métrica 2] | | | |
| [métrica 3] | | | |

**BLOCO 2 — Narrativa Analítica por Vetor**
> **[Vetor 1 — Nome]:** Claim: [afirmação]. Evidence: [dado quantitativo]. Implication: [impacto].

> **[Vetor 2 — Nome]:** Claim: [afirmação]. Evidence: [dado quantitativo]. Implication: [impacto].

**BLOCO 3 — Impacto Quantitativo + DataViz**
| Cenário | Impacto Lucro (R$mi) | Impacto FV (R$/ação) |
|---|---|---|
| Base | | |
| Stress Moderado | | |
| Stress Severo | | |

💡 **Insight não óbvio:** [observação contraintuitiva com evidência]

> 📊 **Instrução DataViz:** [tipo de gráfico] × Eixo X: [variável] × Eixo Y: [variável] | Paleta: [hex cores] | Destaque: [elemento principal]

**BLOCO 4 — Dilema Analítico / Trade-off**
| Opção | Vantagem | Custo | Escolha histórica | Escolha ótima |
|---|---|---|---|---|
| [Opção A] | | | | |
| [Opção B] | | | | |

**BLOCO 5 — Analogia Histórica Documentada**
Empresa: [nome] | Mercado: [país/setor] | Período: [anos] | Resultado: [desfecho] | Lição: [aprendizado transferível]

╔══════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — [Passo X.Y]             ║
╚══════════════════════════════════════════════════════╝
§1 O que este passo revelou sobre a empresa/ativo?
§2 Impacto no fair value (R$/ação): [quantificado ou bounded]?
§3 Nível de confiança: [FATO / INFERÊNCIA / HIPÓTESE] — justificativa?
§4 Perguntas abertas que esta análise abre para as próximas fases?
§5 Assimetria de informação identificada (o que o mercado não vê)?

<!-- JSON_PAYLOAD
{
  "fase": "FX_PY",
  "metrica_principal": 0,
  "metrica_2": 0,
  "metrica_3": 0
}
-->
```

---

## CHECKLIST OBRIGATÓRIO — AO FINAL DE CADA FASE

Transcrever literalmente com [V] (Verdadeiro) ou [F] (Falso) ANTES de avançar:

```text
[CHECKLIST DE COMPLIANCE DO AGENTE — FASE X]
[V/F] BLOCO 1 entregue com tabela snapshot (status/tendência/impacto)
[V/F] BLOCO 2 entregue com ≥2 blockquotes Claim→Evidence→Implication
[V/F] BLOCO 3 entregue com tabela cenários + instrução DataViz + 💡 insight
[V/F] BLOCO 4 entregue com tabela de trade-offs e julgamento explícito
[V/F] BLOCO 5 entregue com analogia histórica NOMEADA (empresa, período, resultado)
[V/F] SÍNTESE §1-§5 entregue no box ╔╗ formatado com respostas completas
[V/F] JSON_PAYLOAD exportado com campos numéricos PREENCHIDOS (não zeros)
```

**Se qualquer linha for [F] → REESCREVER o bloco antes de avançar.**

---

## REGRAS DE PAGINAÇÃO

- **Uma fase = uma mensagem**
- Ao fechar o CHECKLIST DE COMPLIANCE, escrever: `▶️ Fase [X] concluída. Confirme para avançar para Fase [X+1] ou ajuste premissas.`
- **NUNCA** comprimir ou pular blocos para encurtar a resposta

---

## VALIDAÇÃO AUTOMÁTICA DE COMPLIANCE

Para validar programaticamente o output de qualquer fase:
```bash
python scripts/validate_compliance.py --file [arquivo_output.md] --fase F[X]
```

Ou via clipboard após copiar a resposta:
```bash
python scripts/validate_compliance.py --clipboard --fase F[X]
```
