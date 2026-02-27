#!/usr/bin/env python3
"""
fallback_repair.py — DCF Pipeline v3
Motor de fallback com auto-recuperação de compliance.

Lógica:
  1. Valida o output de uma fase
  2. Se reprovado → gera um "repair prompt" cirúrgico com os elementos ausentes
  3. Opcionalmente salva o prompt de reparo num arquivo para ser reenviado ao agente

Uso:
    # Modo 1 — ler do clipboard, gerar repair prompt
    python scripts/fallback_repair.py --clipboard --fase F0

    # Modo 2 — ler de arquivo
    python scripts/fallback_repair.py --file output.md --fase F1

    # Modo 3 — salvar prompt de reparo em arquivo
    python scripts/fallback_repair.py --file output.md --fase F1 --repair-out repair_F1.md

    # Modo 4 — validar E já exibir o caminho de fallback
    python scripts/fallback_repair.py --file output.md --fase F1 --chain
"""

import re
import sys
import argparse
import subprocess
from pathlib import Path

# Importar o validador do mesmo pacote
sys.path.insert(0, str(Path(__file__).parent))
from validate_compliance import validate_text, PATTERNS

# ─────────────────────────────────────────────────────────────
# Templates de repair prompt por elemento ausente
# ─────────────────────────────────────────────────────────────

REPAIR_TEMPLATES = {
    "BLOCO 1 — Diagnóstico Executivo": """
🔧 **FALLBACK — BLOCO 1 AUSENTE**
Você gerou análise mas não produziu o BLOCO 1 obrigatório. Reescreva AGORA:

**BLOCO 1 — Diagnóstico Executivo**
| Campo | Valor | Status | Tendência |
|---|---|---|---|
| [métrica 1] | [dado + unidade] | 🔴/🟠/✅ | ↗️/→/↘️ |
| [métrica 2] | [dado + unidade] | 🔴/🟠/✅ | ↗️/→/↘️ |
| [métrica 3] | [dado + unidade] | 🔴/🟠/✅ | ↗️/→/↘️ |
""",
    "Tabela snapshot no BLOCO 1": """
🔧 **FALLBACK — TABELA DO BLOCO 1 AUSENTE**
O BLOCO 1 existe mas não tem tabela markdown. Adicione:
| Campo | Valor | Status | Tendência |
|---|---|---|---|
| [dado] | [número] | 🔴/🟠/✅ | ↗️/→/↘️ |
""",
    "BLOCO 2 — Narrativa Analítica": """
🔧 **FALLBACK — BLOCO 2 AUSENTE**
Reescreva com MÍNIMO 2 vetores em blockquote:

**BLOCO 2 — Narrativa Analítica por Vetor**
> **[Vetor 1 — Nome]:** Claim: [afirmação]. Evidence: [dado]. Implication: [impacto].
> **[Vetor 2 — Nome]:** Claim: [afirmação]. Evidence: [dado]. Implication: [impacto].
""",
    "Blockquotes Claim→Evidence→Implication no BLOCO 2": """
🔧 **FALLBACK — BLOCKQUOTES DO BLOCO 2 AUSENTES OU MAL FORMATADOS**
Use EXATAMENTE este formato (> no início, negrito no vetor):
> **[Vetor N — Nome]:** Claim: X. Evidence: Y. Implication: Z.
""",
    "BLOCO 3 — Impacto Quantitativo + DataViz": """
🔧 **FALLBACK — BLOCO 3 AUSENTE**
Reescreva com tabela + DataViz + insight:

**BLOCO 3 — Impacto Quantitativo + DataViz**
| Cenário | Impacto Lucro (R$mi) | Impacto FV (R$/ação) |
|---|---|---|
| Base | X | X |
| Stress Moderado | X | X |
| Stress Severo | X | X |

💡 **Insight não óbvio:** [observação contraintuitiva]

> 📊 **Instrução DataViz:** Tipo: [gráfico] | Eixo X: [var] | Eixo Y: [var] | Paleta: [cores] | Destaque: [elemento]
""",
    "Instrução DataViz no BLOCO 3": """
🔧 **FALLBACK — INSTRUÇÃO DATAVIZ AUSENTE**
Adicione ao BLOCO 3 esta linha obrigatória:
> 📊 **Instrução DataViz:** Tipo: [bar/radar/waterfall/line] | Eixo X: [variável] | Eixo Y: [variável] | Paleta: ["#003366", "#A0A0A0"] | Destaque: [elemento principal]
""",
    "💡 Insight não óbvio no BLOCO 3": """
🔧 **FALLBACK — INSIGHT NÃO ÓBVIO AUSENTE**
Adicione ao BLOCO 3:
💡 **Insight não óbvio:** [observação contraintuitiva com dado quantitativo de suporte]
""",
    "BLOCO 4 — Dilema / Trade-off": """
🔧 **FALLBACK — BLOCO 4 AUSENTE**
Adicione:

**BLOCO 4 — Dilema Analítico / Trade-off**
| Opção | Vantagem | Custo | Histórico | Escolha ótima |
|---|---|---|---|---|
| [A] | | | | |
| [B] | | | | |

Julgamento explícito: [qual opção e por quê, fundamentado em dado].
""",
    "BLOCO 5 — Analogia Histórica": """
🔧 **FALLBACK — BLOCO 5 AUSENTE**
Adicione:

**BLOCO 5 — Analogia Histórica Documentada**
Empresa: [nome real da empresa] | Mercado: [país/setor] | Período: [anos] | Resultado: [desfecho] | Lição: [transferível para este case]
""",
    "Box SÍNTESE INSTITUCIONAL": """
🔧 **FALLBACK — SÍNTESE INSTITUCIONAL AUSENTE**
Adicione exatamente:

╔══════════════════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — [Passo X.Y]                         ║
╚══════════════════════════════════════════════════════════════════╝
§1 O que este passo revelou?
§2 Impacto no fair value (R$/ação)?
§3 Nível de confiança (FATO / INFERÊNCIA / HIPÓTESE)?
§4 Perguntas abertas para próximas fases?
§5 Assimetria de informação identificada?
""",
    "§1 na Síntese Institucional": "🔧 **FALLBACK — §1 AUSENTE DA SÍNTESE:** Adicione '§1 O que este passo revelou sobre a empresa/ativo?'",
    "§2 na Síntese Institucional": "🔧 **FALLBACK — §2 AUSENTE DA SÍNTESE:** Adicione '§2 Impacto no fair value (R$/ação): [valor quantificado]?'",
    "§3 na Síntese Institucional": "🔧 **FALLBACK — §3 AUSENTE DA SÍNTESE:** Adicione '§3 Nível de confiança: [FATO / INFERÊNCIA / HIPÓTESE] — justificativa?'",
    "§4 na Síntese Institucional": "🔧 **FALLBACK — §4 AUSENTE DA SÍNTESE:** Adicione '§4 Perguntas abertas que este passo abre para as próximas fases?'",
    "§5 na Síntese Institucional": "🔧 **FALLBACK — §5 AUSENTE DA SÍNTESE:** Adicione '§5 Assimetria de informação identificada (o que o mercado não vê)?'",
    "Bloco <!-- JSON_PAYLOAD --> exportado": """
🔧 **FALLBACK — JSON_PAYLOAD AUSENTE**
Adicione ao final da fase:
<!-- JSON_PAYLOAD
{
  "fase": "[FX_PY]",
  "metrica_principal": 0.0,
  "metrica_2": 0.0,
  "metrica_3": 0.0
}
-->
⚠️ Substitua os 0.0 pelos valores reais da análise.
""",
    "CHECKLIST DE COMPLIANCE DO AGENTE": """
🔧 **FALLBACK — CHECKLIST AUSENTE**
Adicione ao final:
```text
[CHECKLIST DE COMPLIANCE DO AGENTE — FASE X]
[V/F] BLOCO 1 entregue com tabela snapshot
[V/F] BLOCO 2 com ≥2 blockquotes Claim→Evidence→Implication
[V/F] BLOCO 3 com DataViz + insight
[V/F] BLOCO 4 com trade-offs
[V/F] BLOCO 5 com analogia nomeada
[V/F] SÍNTESE §1-§5 preenchida
[V/F] JSON_PAYLOAD exportado
```
""",
    "Checklist preenchido com [V] ou [F] (não [?])": """
🔧 **FALLBACK — CHECKLIST COM [?] DETECTADO**
Substitua TODOS os [?] por [V] (Verdadeiro) ou [F] (Falso).
[?] é inválido — o compliance check não é uma pergunta, é uma afirmação a confirmar.
""",
}


def get_repair_prompt(failed_items: list, fase: str) -> str:
    """Gera prompt de reparo cirúrgico baseado nos itens que falharam."""
    lines = []
    lines.append(f"\n{'='*65}")
    lines.append(f"  🚨 FALLBACK ATIVADO — Fase {fase}")
    lines.append(f"  {len(failed_items)} elemento(s) ausente(s). Reparo cirúrgico required.")
    lines.append(f"{'='*65}")
    lines.append("")
    lines.append("**INSTRUÇÃO DE REPARO:** Sua resposta anterior está INCOMPLETA.")
    lines.append(f"Antes de avançar para a próxima fase, você DEVE adicionar/reescrever:")
    lines.append("")

    for i, item in enumerate(failed_items, 1):
        lines.append(f"### Reparo {i}/{len(failed_items)}: {item}")
        repair = REPAIR_TEMPLATES.get(item)
        if repair:
            lines.append(repair.strip())
        else:
            lines.append(f"→ Adicione/complete: **{item}** conforme o template do SKILL.md raiz.")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("**Após completar os reparos**, preencha o checklist de compliance corrigido e execute:")
    lines.append(f"`python scripts/validate_compliance.py --clipboard --fase {fase}`")
    lines.append("")
    lines.append("Se Exit 0 → pode avançar. Se Exit 1 → novo ciclo de fallback.")

    return "\n".join(lines)


def run_fallback(text: str, fase: str, repair_out: str = None, chain: bool = False) -> int:
    """
    Executa validação + fallback.
    Retorna 0 se aprovado, 1 se reprovado (com repair prompt gerado).
    """
    result = validate_text(text, fase=fase)

    if result.ok:
        print(f"\n✅ COMPLIANCE OK — Fase {fase}. Sem fallback necessário.")
        print(f"   Score: {len(result.passed)}/{len(result.passed)+len(result.failed)} checks OK")
        return 0

    # Gerar prompt de reparo
    repair_prompt = get_repair_prompt(result.failed, fase)

    print(f"\n❌ COMPLIANCE REPROVADO — Fase {fase}")
    print(f"   Falhas: {len(result.failed)} | Aprovados: {len(result.passed)}")
    print(f"\n{repair_prompt}")

    if repair_out:
        Path(repair_out).write_text(repair_prompt, encoding="utf-8")
        print(f"\n📝 Repair prompt salvo em: {repair_out}")

    if result.warnings:
        print(f"\n🟠 AVISOS (não bloqueiam, mas corrigir):")
        for w in result.warnings:
            print(f"   ⚠️  {w}")

    return 1


# ─────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="DCF Pipeline — Motor de Fallback e Auto-Reparo"
    )
    parser.add_argument("--file", "-f", help="Arquivo markdown a validar")
    parser.add_argument("--text", "-t", help="Texto direto")
    parser.add_argument("--clipboard", "-c", action="store_true", help="Ler do clipboard")
    parser.add_argument("--fase", default="?", help="ID da fase (ex: F0, F1)")
    parser.add_argument("--repair-out", "-r", help="Salvar repair prompt em arquivo")
    parser.add_argument("--chain", action="store_true",
                        help="Modo encadeado: valida → se falha → mostra reparo → aguarda")
    args = parser.parse_args()

    text = None

    if args.file:
        try:
            text = Path(args.file).read_text(encoding="utf-8")
        except FileNotFoundError:
            print(f"❌ Arquivo não encontrado: {args.file}", file=sys.stderr)
            sys.exit(2)
    elif args.text:
        text = args.text
    elif args.clipboard:
        try:
            proc = subprocess.run(
                ["powershell", "-command", "Get-Clipboard"],
                capture_output=True, text=True
            )
            text = proc.stdout
        except Exception as e:
            print(f"❌ Erro ao ler clipboard: {e}", file=sys.stderr)
            sys.exit(2)
    else:
        text = sys.stdin.read()

    if not text or not text.strip():
        print("❌ Nenhum texto fornecido.", file=sys.stderr)
        sys.exit(2)

    exit_code = run_fallback(
        text=text,
        fase=args.fase,
        repair_out=args.repair_out,
        chain=args.chain,
    )
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
