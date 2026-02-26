---
name: "Fase 7 — Stress Test & Validação Cruzada"
description: |
  Fat tails, Via Negativa, vieses cognitivos, triangulação, QMJ e sentimento de mercado.
  Triggers: "stress test", "validação", "vieses", "triangulação", "QMJ"
---

# FASE 7 — STRESS TEST & VALIDAÇÃO CRUZADA

> **Ponteiros de entrada:** Usar outputs das Fases 3 (`skills/fase3-projecao-fcff/SKILL.md`), 5 (`skills/fase5-terminal-value/SKILL.md`) e 6 (`skills/fase6-agregacao/SKILL.md`).

## Passo 7.1 — Fat Tails e Via Negativa (Curto, Médio e Longo Prazo)

**Ação:**
1. Monte Carlo: verificar se distribuição tem fat tails (usar `scripts/monte_carlo.py`).
2. Cenário 3+ σ: a empresa sobrevive?
3. Perda completa de pricing power.
4. Rate shock: WACC +300bps.
5. **Via Negativa (Antifrágil)**: O que NÃO deveria acontecer para a tese funcionar?
   - **Curto prazo (trimestre)**: Que eventos trimestrais invalidariam imediatamente?
   - **Médio prazo (1-3 anos)**: Que mudanças estruturais de mercado ou produto destroem o moat?
   - **Longo prazo (5+ anos)**: Que disruptions tecnológicas, regulatórias ou competitivas tornam o negócio obsoleto?
6. Isso é mais informativo do que o que deveria acontecer.
7. **Aleatoriedade e ilusão de causalidade**: não confundir luck com skill na narrativa (L.56, L.58).

**Referências:**
- **Livro 89** (Antifrágil, Taleb): Livro IV — Via Negativa; Livro VII — Skin in the Game.
- **Livro 90** (McLeish): path-by-path FCFF fat tails.
- **Livro 51** (Fat Tails): distribuições Paretian.
- **Livro 56** (Iludidos pelo Acaso, Taleb): survivorship bias, confundir sorte com habilidade.
- **Livro 31** (Safe Haven, Spitznagel): hedging e proteção em tail events.
- **Livro 46** (Deep Simplicity, Gribbin): complexidade e emergência em sistemas econômicos.
- **Livro 58** (O Andar do Bêbado, Mlodinow): aleatoriedade e falsa causalidade.
- **P05** (Drawdowns): base rates de drawdowns e recuperação.

**Output:** Lista de condições de invalidação (curto/médio/longo prazo). Resultado do teste 3+σ.

---

## Passo 7.2 — Vieses Cognitivos e Sentimento de Mercado

**Ação:**
1. Anchoring: target ancorado no preço atual?
2. Overconfidence: intervalos calibrados?
3. Confirmation bias: buscou evidências contra?
4. Narrative fallacy: narrativa distorcendo números?
5. Sunk cost: persistindo sem suporte dos dados?
6. **Feedback loop**: a qualidade das decisões anteriores está acoplada ao resultado? Separar processo de outcome (P30).
7. **Sentimento de Mercado vs Modelo**: O sentimento de mercado (API yFinance Short Ratios, Opções, P/E Histórico) aponta Dispersão Altíssima? É uma alfa-oportunidade real descasada dos fundamentos ou o mercado sabe algo que não sabemos?

**Referências:**
- **Livro 62** (Kahneman, Rápido e Devagar): anchoring, overconfidence.
- **Livro 82** (Think Twice, Mauboussin): erros mentais.
- **Livro 27** (Tetlock, Superprevisões).
- **P15** (Pattern Recognition): quando padrões funcionam.
- **P44** (BIN There, Done That): superforecasting aplicado.
- **P43** (Dispersion and Alpha): dispersão como oportunidade.
- **P30** (Feedback): qualidade de feedback como proxy de qualidade de processo.
- **P42** (Myth Busting, Popular Delusions): 4 mitos de mercado desmontados.

---

## Passo 7.3 — Validação Cruzada — Triangulação

**Ação:**
1. **Reverse DCF final**: premissas implícitas no Fair Value são razoáveis?
2. **EPV vs. DCF**: se EPV > DCF → mercado precifica destruição via growth.
3. **Residual Income Model** (Penman).
4. **P/VP = 1 teste Penman**: se pago book value, o valor vem 100% do excess return.
5. **Múltiplos implícitos**: Fair Value implica P/E e EV/EBITDA de quanto? (P47, P48)
6. **Quality Minus Junk score (QMJ)**: a empresa é "quality" ou "junk"?
7. **Management credibility discount**: se score baixo (Passo 2.5.1 — vide `skills/fase25-management/SKILL.md`), discount adicional.
8. **Tabela de sensibilidade 3 cenários × preço atual 7×7** (usar `scripts/sensitivity_table.py`).

**Referências:**
- **Livro 06/84** (Expectations Investing): Reverse DCF.
- **Livro 09** (Greenwald): EPV, triangulação.
- **Livro 01** (Penman): residual income, P/B=1 test.
- **Livro 86** (Lundholm/Sloan).
- **P53** (QMJ, Asness Frazzini): quality factor scoring.
- **P52** (Common Errors in DCF): checklist final.
- **P12** (Valuation Multiples).
- **P47** (P/E): decomposição do múltiplo.
- **P48** (EV/EBITDA): decomposição.

**Output:** Tabela de Triangulação (Reverse DCF × DCF × EPV × Residual Income × Múltiplo). Via Negativa lista. QMJ Score. Diagnóstico Sentimento vs Modelo.
