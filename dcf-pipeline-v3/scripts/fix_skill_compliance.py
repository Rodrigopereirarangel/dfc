#!/usr/bin/env python3
"""
fix_skill_compliance.py — Script de correção em lote dos sub-skills.
Corrige:
1. Marcadores [?] → [V/F] nos checklists
2. Adiciona comando validate_compliance ao final de cada checklist
3. Garante que a instrução de preenchimento é clara

Uso: python scripts/fix_skill_compliance.py
"""
import re
import os
from pathlib import Path

BASE = Path(__file__).parent.parent
SKILLS_DIR = BASE / "skills"

FASE_MAP = {
    "fase0-estrategia": "F0",
    "fase1-auditoria-contabil": "F1",
    "fase2-value-drivers": "F2",
    "fase25-management": "F25",
    "fase3-projecao-fcff": "F3",
    "fase4-wacc": "F4",
    "fase5-terminal-value": "F5",
    "fase5a-auditoria360": "F5A",
    "fase6-agregacao": "F6",
    "fase7-stress-test": "F7",
    "fase8-decisao": "F8",
    "fase9-pdf-institucional": "F9",
}

def fix_skill(path: Path, fase_id: str) -> bool:
    """Aplica correções de compliance no SKILL.md. Retorna True se modificado."""
    text = path.read_text(encoding="utf-8")
    original = text

    # 1. Substituir [?] por [V/F] nos checklists
    text = re.sub(r"\[\?\]", "[V/F]", text)

    # 2. Substituir padrão antigo do checklist header
    text = text.replace(
        "[CHECKLIST DE COMPLIANCE DO AGENTE]",
        f"[CHECKLIST DE COMPLIANCE DO AGENTE — FASE {fase_id}]"
    )

    # 3. Substituir "(V) ou (F)" por "[V] ou [F]" na instrução
    text = re.sub(
        r'PREENCHIDO com \(V\) ou \(F\)',
        'PREENCHIDO com **[V]** (Verdadeiro) ou **[F]** (Falso)',
        text
    )

    # 4. Se o checklist não tem ainda a linha de validação automática, adicionar
    validate_line = f"Validação automática: `python scripts/validate_compliance.py --clipboard --fase {fase_id}`"
    if validate_line not in text:
        # Adicionar após "**Se qualquer item for (F/[F]):"
        text = re.sub(
            r'(\*\*Se qualquer item for (?:\(F\)|\[F\]).*?prosseguir.*?fase\.?)\s*\n',
            lambda m: m.group(0).rstrip() + f"\n\n{validate_line}\n",
            text,
            flags=re.IGNORECASE
        )

    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main():
    print(f"🔧 DCF Pipeline — Fix Skills Compliance")
    print(f"   Base: {BASE}")
    print(f"   Skills: {SKILLS_DIR}\n")

    for phase_dir, fase_id in FASE_MAP.items():
        skill_path = SKILLS_DIR / phase_dir / "SKILL.md"
        if not skill_path.exists():
            print(f"  ⚠️  NÃO ENCONTRADO: {skill_path}")
            continue

        modified = fix_skill(skill_path, fase_id)
        status = "✅ Corrigido" if modified else "ℹ️  Sem alterações"
        print(f"  {status}: {phase_dir}/SKILL.md (Fase {fase_id})")

    print(f"\n✅ Concluído. Execute para verificar:")
    print(f"   python scripts/validate_compliance.py --file <output.md> --fase F0")


if __name__ == "__main__":
    main()
