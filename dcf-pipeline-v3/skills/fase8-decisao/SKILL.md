---
name: "Fase 8 — Decisão: Conviction & Sizing"
description: |
  Conviction Score composto, Kelly Criterion fracional e assimetria Antifrágil.
  Triggers: "conviction", "sizing", "posição", "Kelly", "recomendação"
---

# FASE 8 — DECISÃO: CONVICTION & SIZING

> **Entradas obrigatórias:**
> - Fair Value e cenários da Fase 6 (`skills/fase6-agregacao/SKILL.md`)
> - Nota de Moat da Fase 0 (`skills/fase0-estrategia/SKILL.md`)
> - Score de Management da Fase 2.5 (`skills/fase25-management/SKILL.md`)
> - QMJ Score e triangulação da Fase 7 (`skills/fase7-stress-test/SKILL.md`)
> - Calcular com: `scripts/kelly_sizing.py`

## Passo 8.1 — Conviction Score

**Ação:**
Score composto (1 a 10):
- **Upside/Downside Ratio** (25%): Fair Value / Preço Atual.
- **Qualidade do Moat** (20%): Nota Durabilidade do Passo 0.1.
- **Credibilidade do Management** (20%): Score do Passo 2.5.1.
- **Confiança nas Projeções** (15%): dispersão do MC, sensibilidade.
- **Confirmação de Validação Cruzada** (10%): convergência dos métodos.
- **Quality Minus Junk Score** (10%): quality factor QMJ.

Score ≥ 7 → posição relevante; 5-6 → menor; < 5 → não investir.

**Referências:**
- **Livro 18** (Paleologo): conviction scoring multi-fator.
- **P07** (Probabilities and Payoffs).
- **P02** (Who Is On the Other Side?).
- **P43** (Dispersion and Alpha).
- **Livro 83** (Success Equation): skill vs. luck.
- **P53** (QMJ).

---

## Passo 8.2 — Position Sizing via Kelly

**Ação:**
1. Kelly: `f* = (p × b − q) / b`.
2. Usar **Half-Kelly ou Quarter-Kelly** na prática.
3. Stop-loss: em qual cenário a tese está errada?
4. Position size máximo como % do portfólio.
5. **Assimetria Antifrágil**: se downside é limitado e upside convexo, pode-se ser mais agressivo; se downside é ilimitado, ser mais conservador.
6. **Probabilidade do target**: usar framework Dragonfly Eye (Tetlock) para transparência.
7. **Correlação de Sentimento Extremo**: Se modelo bull + mercado ultra pessimista com baixa dispersão fundamental + score elevado → Sizing Premium (Antifrágil Position). Se sentimento eufórico + preço esticado (reverse DCF insano) sem moat seguro → rejeitar.

**Referências:**
- **Livro 03** (Bernstein, Desafio aos Deuses): Kelly Criterion.
- **Livro 18** (Paleologo): dimensionamento.
- **Livro 61** (Axiomas de Zurique).
- **Livro 89** (Antifrágil): Livro VII — Skin in the Game, assimetria.
- **Livro 27** (Tetlock, Superprevisões): Cap. 8 — Dragonfly Eye.
- **P07** (Probabilities and Payoffs).

**Output:** Conviction Score [0-10] com breakdown tabular. Position Sizing máximo (% portfólio). Cenário de invalidação (stop-loss).
