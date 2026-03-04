#!/usr/bin/env python3
"""
validate_compliance.py — DCF Pipeline v3
Valida se o output de uma fase segue a ARQUITETURA UNIVERSAL DE EXPANSÃO.
Verifica: 5 Blocos, Síntese §1-§5, DataViz, JSON_PAYLOAD, Checklist [V/F].

Uso:
    python scripts/validate_compliance.py --file output.md --fase F0
    python scripts/validate_compliance.py --text "$(cat output.md)" --fase F1
    python scripts/validate_compliance.py --clipboard --fase F2   # valida conteúdo da área de transferência

Retorna:
    Exit 0 → Compliance OK
    Exit 1 → Falhas encontradas (lista os blocos ausentes)
"""

import re
import sys
import argparse
import json
from dataclasses import dataclass, field
from typing import List, Optional


# ─────────────────────────────────────────────────────────────
# Padrões de compliance esperados em TODO sub-passo
# ─────────────────────────────────────────────────────────────

PATTERNS = {
    "BLOCO_1": {
        "regex": r"(?i)BLOCO\s*1\s*[—–-]\s*Diagn[oó]stico\s*Executivo",
        "desc": "BLOCO 1 — Diagnóstico Executivo",
        "required": True,
    },
    "BLOCO_1_TABLE": {
        "regex": r"\|.+\|.+\|.+\|",
        "desc": "Tabela snapshot no BLOCO 1",
        "required": True,
    },
    "BLOCO_2": {
        "regex": r"(?i)BLOCO\s*2\s*[—–-]\s*Narrativa\s*Anal[ií]tica",
        "desc": "BLOCO 2 — Narrativa Analítica",
        "required": True,
    },
    "BLOCO_2_BLOCKQUOTE": {
        "regex": r"^>\s+\*\*\[?Vetor|^>\s+\*\*Claim|^>\s+Claim\s*→",
        "desc": "Blockquotes Claim→Evidence→Implication no BLOCO 2",
        "required": True,
    },
    "BLOCO_3": {
        "regex": r"(?i)BLOCO\s*3\s*[—–-]\s*Impacto\s*Quantitativo",
        "desc": "BLOCO 3 — Impacto Quantitativo + DataViz",
        "required": True,
    },
    "BLOCO_3_DATAVIZ": {
        "regex": r"(?i)(📊|Instru[çc][aã]o\s*DataViz|DataViz)",
        "desc": "Instrução DataViz no BLOCO 3",
        "required": True,
    },
    "BLOCO_3_INSIGHT": {
        "regex": r"(?i)(💡|Insight\s*n[aã]o|insight\s+oculto|insight\s+n[ãa]o[\s-]+[oó]bvio)",
        "desc": "💡 Insight não óbvio no BLOCO 3",
        "required": True,
    },
    "BLOCO_4": {
        "regex": r"(?i)BLOCO\s*4\s*[—–-]\s*(Dilema|Trade[\s-]?off)",
        "desc": "BLOCO 4 — Dilema / Trade-off",
        "required": True,
    },
    "BLOCO_5": {
        "regex": r"(?i)BLOCO\s*5\s*[—–-]\s*Analogia\s*Hist[oó]rica",
        "desc": "BLOCO 5 — Analogia Histórica",
        "required": True,
    },
    "SINTESE_BOX": {
        "regex": r"(?i)(SÍNTESE\s*INSTITUCIONAL|SINTESE\s*INSTITUCIONAL|╔.*SÍNTESE)",
        "desc": "Box SÍNTESE INSTITUCIONAL",
        "required": True,
    },
    "SINTESE_S1": {
        "regex": r"(?i)§\s*1\s+",
        "desc": "§1 na Síntese Institucional",
        "required": True,
    },
    "SINTESE_S2": {
        "regex": r"(?i)§\s*2\s+",
        "desc": "§2 na Síntese Institucional",
        "required": True,
    },
    "SINTESE_S3": {
        "regex": r"(?i)§\s*3\s+",
        "desc": "§3 na Síntese Institucional",
        "required": True,
    },
    "SINTESE_S4": {
        "regex": r"(?i)§\s*4\s+",
        "desc": "§4 na Síntese Institucional",
        "required": True,
    },
    "SINTESE_S5": {
        "regex": r"(?i)§\s*5\s+",
        "desc": "§5 na Síntese Institucional",
        "required": True,
    },
    "JSON_PAYLOAD": {
        "regex": r"```json",
        "desc": "Bloco ```json exportado",
        "required": True,
    },
    "CHECKLIST": {
        "regex": r"(?i)CHECKLIST\s*DE\s*COMPLIANCE",
        "desc": "CHECKLIST DE COMPLIANCE DO AGENTE",
        "required": True,
    },
    "CHECKLIST_VF": {
        "regex": r"\[(V|F|✅|❌)\]",
        "desc": "Checklist preenchido com [V] ou [F] (não [?])",
        "required": True,
    },
}

# ─────────────────────────────────────────────────────────────
# Engine de validação
# ─────────────────────────────────────────────────────────────

@dataclass
class ValidationResult:
    fase: str
    passed: List[str] = field(default_factory=list)
    failed: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return len(self.failed) == 0

    def summary(self) -> str:
        lines = []
        status = "✅ APROVADO" if self.ok else "❌ REPROVADO"
        lines.append(f"\n{'='*60}")
        lines.append(f"  DCF Compliance Validator — Fase {self.fase}")
        lines.append(f"  Status: {status}")
        lines.append(f"  Score: {len(self.passed)}/{len(self.passed)+len(self.failed)} checks OK")
        lines.append(f"{'='*60}")

        if self.failed:
            lines.append("\n🔴 BLOCOS / ELEMENTOS AUSENTES:")
            for f in self.failed:
                lines.append(f"  ✗ {f}")

        if self.passed:
            lines.append("\n✅ ELEMENTOS PRESENTES:")
            for p in self.passed:
                lines.append(f"  ✓ {p}")

        if self.warnings:
            lines.append("\n🟠 AVISOS:")
            for w in self.warnings:
                lines.append(f"  ⚠️  {w}")

        lines.append(f"\n{'='*60}")

        if not self.ok:
            lines.append("\n📋 AÇÃO REQUERIDA: Reescreva os elementos ausentes antes de avançar.")
            # Gerar checklist preenchido
            lines.append("\n[CHECKLIST DE COMPLIANCE AI — PREENCHIDO AUTOMATICAMENTE]")
            all_items = {
                "5 Blocos entregues completos": all(
                    f"BLOCO {i}" not in "\n".join(self.failed) for i in ["1","2","3","4","5"]
                    if any(f"BLOCO {i}" in p for p in self.failed)
                ),
            }
            # Itens explícitos
            checks = {
                "BLOCO 1 com tabela snapshot": "BLOCO_1_TABLE" not in "\n".join([f for f in self.failed]),
                "BLOCO 2 com ≥2 blockquotes Claim→Evidence→Implication": "BLOCO_2_BLOCKQUOTE" not in "\n".join(self.failed),
                "BLOCO 3 com instrução DataViz + Insight não óbvio": not any("DataViz" in f or "Insight" in f for f in self.failed),
                "BLOCO 4 com tabela de trade-offs": "BLOCO_4" not in "\n".join(self.failed),
                "BLOCO 5 com analogia histórica nomeada": "BLOCO_5" not in "\n".join(self.failed),
                "SÍNTESE §1-§5 entregue no box formatado": not any("§" in f for f in self.failed),
                "JSON_PAYLOAD exportado": "JSON_PAYLOAD" not in "\n".join(self.failed),
                "CHECKLIST preenchido com [V] ou [F]": "CHECKLIST_VF" not in "\n".join(self.failed),
            }
            for check, passed in checks.items():
                mark = "V" if passed else "F"
                lines.append(f"[{mark}] {check}")
        else:
            lines.append("\n🎯 Compliance total! Pode avançar para a próxima fase.")

        return "\n".join(lines)

    def to_json(self) -> dict:
        return {
            "fase": self.fase,
            "ok": self.ok,
            "score": f"{len(self.passed)}/{len(self.passed)+len(self.failed)}",
            "passed": self.passed,
            "failed": self.failed,
            "warnings": self.warnings,
        }


def validate_text(text: str, fase: str = "?") -> ValidationResult:
    result = ValidationResult(fase=fase)

    for key, rule in PATTERNS.items():
        pattern = re.compile(rule["regex"], re.MULTILINE)
        found = pattern.search(text)
        if found:
            result.passed.append(rule["desc"])
        elif rule["required"]:
            result.failed.append(rule["desc"])

    # Verificação extra: JSON_PAYLOAD deve ter campos numéricos
    json_match = re.search(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL)
    if json_match:
        try:
            payload = json.loads(json_match.group(1))
            numeric_fields = [k for k, v in payload.items() if isinstance(v, (int, float)) and v != 0]
            if not numeric_fields:
                result.warnings.append("JSON_PAYLOAD encontrado mas todos os campos numéricos são 0 — preencha com dados reais")
        except json.JSONDecodeError:
            result.warnings.append("JSON_PAYLOAD com JSON inválido — verifique a sintaxe")

    # Verificação: checklist com [?] (bug de formato)
    placeholders = re.findall(r"\[\?\]", text)
    if placeholders:
        result.warnings.append(
            f"Encontrados {len(placeholders)}x marcadores [?] no checklist — deveriam ser [V] ou [F]"
        )

    return result


# ─────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="DCF Pipeline — Validador de Compliance de Output"
    )
    parser.add_argument("--file", "-f", help="Arquivo markdown a validar")
    parser.add_argument("--text", "-t", help="Texto direto a validar (string)")
    parser.add_argument("--clipboard", "-c", action="store_true", help="Validar conteúdo da área de transferência")
    parser.add_argument("--fase", default="?", help="Nome/ID da fase (ex: F0, F1, F2)")
    parser.add_argument("--json", action="store_true", help="Saída em JSON")
    parser.add_argument("--quiet", "-q", action="store_true", help="Mostrar apenas status final")
    args = parser.parse_args()

    text = None

    if args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                text = f.read()
        except FileNotFoundError:
            print(f"❌ Arquivo não encontrado: {args.file}", file=sys.stderr)
            sys.exit(2)

    elif args.text:
        text = args.text

    elif args.clipboard:
        try:
            import subprocess
            result = subprocess.run(["powershell", "-command", "Get-Clipboard"], capture_output=True, text=True)
            text = result.stdout
        except Exception as e:
            print(f"❌ Erro ao ler clipboard: {e}", file=sys.stderr)
            sys.exit(2)

    else:
        # Lê stdin
        text = sys.stdin.read()

    if not text or not text.strip():
        print("❌ Nenhum texto fornecido para validação.", file=sys.stderr)
        sys.exit(2)

    result = validate_text(text, fase=args.fase)

    if args.json:
        print(json.dumps(result.to_json(), ensure_ascii=False, indent=2))
    elif args.quiet:
        status = "APROVADO" if result.ok else f"REPROVADO ({len(result.failed)} falhas)"
        print(f"Fase {args.fase}: {status}")
    else:
        print(result.summary())

    sys.exit(0 if result.ok else 1)


if __name__ == "__main__":
    main()
