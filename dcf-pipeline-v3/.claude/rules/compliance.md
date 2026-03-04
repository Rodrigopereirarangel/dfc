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
*(Não gere muralhas de texto; use listas, bolding para termos chave e parágrafos curtos de max 7-8 linhas)*
§1 O que este passo revelou sobre a empresa/ativo?
§2 Impacto no fair value (R$/ação): [quantificado ou bounded]?
§3 Nível de confiança: [FATO / INFERÊNCIA / HIPÓTESE] — justificativa?
§4 Perguntas abertas que esta análise abre para as próximas fases?
§5 Assimetria de informação identificada (o que o mercado não vê)?

```json
{
  "fase": "FX_PY",
  "metrica_principal": 0,
  "metrica_2": 0,
  "metrica_3": 0
}
```
```

---

## CHECKLIST OBRIGATÓRIO — AO FINAL DE CADA FASE (COMPUTAÇÃO INTERNA SILENCIOSA)

Ao finalizar cada fase, valide **internamente** os critérios abaixo (Tree of Thoughts). **NÃO imprima a lista no chat** — isso polui a leitura do usuário.

**Critérios de validação interna:**
- BLOCO 1 com tabela snapshot (≥3 linhas, colunas Status e Tendência preenchidas)?
- BLOCO 2 com **≥2** blockquotes no formato `Claim: X. Evidence: Y. Implication: Z.`?
- BLOCO 3 com tabela cenários + instrução DataViz + 💡 insight não óbvio?
- BLOCO 4 com tabela de trade-offs + julgamento explícito fundamentado?
- BLOCO 5 com analogia histórica NOMEADA (empresa real, período, resultado, lição)?
- SÍNTESE §1-§5 no box ╔╗ com respostas completas (sem placeholders `[X]`)?
- JSON_PAYLOAD com todos os campos numéricos PREENCHIDOS (nenhum zerado sem justificativa)?

**Se qualquer critério falhar → DESCARTAR a resposta internamente e reescrever antes de enviar.**

Após validação interna aprovada, imprimir **apenas esta linha** no chat:
```
✅ CHECKLIST DE COMPLIANCE OK. FASE [X] CONCLUÍDA.
```

Para validação programática (debug):
```bash
python scripts/validate_compliance.py --clipboard --fase F[X]
```

---

## REGRAS DE PAGINAÇÃO

- **Modo Autônomo (padrão `/dfc`):** Após o `✅ CHECKLIST...`, continuar gerando a próxima fase **na mesma resposta**. Pausar **somente** nos 3 Macro-Checkpoints (fim de Fase 2.5, 5 e 8) e se `❗ GATE REPROVADO`.
- **Modo Manual (`/dfc [TICKER] manual`):** Uma fase = uma mensagem. Ao fechar, perguntar: `👉 Fase [X] Concluída. Qual das Opções (A ou B) do Trade-Off acima você escolhe?`
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
