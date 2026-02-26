---
name: "Fase 6 — Agregação, Cenários & Bridge para Equity"
description: |
  Cenários ponderados, bridge EV→Equity, sensibilidade 7×7 e comparação institucional.
  Triggers: "cenários", "fair value", "preço justo", "bridge", "sensibilidade"
---

# FASE 6 — AGREGAÇÃO, CENÁRIOS & BRIDGE PARA EQUITY

> **Entradas:** Terminal Value da Fase 5 (`skills/fase5-terminal-value/SKILL.md`). WACC da Fase 4. FCFF da Fase 3.
> **Calcular com:** `scripts/sensitivity_table.py` para tabela 7×7.
> **Saídas:** Fair Value → Fases 7 e 8.

## Passo 6.1 — Cenários Ponderados + Árvore de Cenários

**Ação:**
1. Definir 3-5 cenários com premissas explícitas:
   - **Distress** (5-10%): perda de moat, restructuring.
   - **Bear** (20-25%): ramp-ups falham, ROIC decai rápido.
   - **Base** (40-50%): ramp-ups parciais, fade gradual.
   - **Bull** (20-25%): projetos excedem, moat fortalece.
2. EV e equity value por cenário.
3. Expected Value = Σ(Prob × Valor).
4. Upside/Downside ratio.
5. **Árvore de cenários visual**: cada nó = premissa-chave.
6. **Para cada cenário, extrair e registrar:**
   - ERP Implícito.
   - Custo de Capital Implícito.
   - Custo de Capital Acima da Inflação (Real Return implícito).

**Referências:**
- **P07** (Probabilities and Payoffs).
- **P21** (Confidence): separar probabilidade × confiança.
- **Livro 08** (How to Measure Anything).
- **Livro 27** (Superprevisões).

---

## Passo 6.2 — Real Options (se aplicável)

**Ação:**
1. Identificar opções reais: expansion, abandonment, switching, timing.
2. Valuar via framework ou B-S adaptado.
3. EV = DCF Base + Σ(Real Options).

**Referências:**
- **Livro 34** (Real Options, Trigeorgis).
- **P39** (WACC and Vol): real options benefício.

---

## Passo 6.3 — Bridge para Equity Value

**Ação:**
1. Equity Value = EV − Dívida Líquida − Minority Interests − Preferred + Associates + Excess Cash.
2. **Detalhar ajuste de minoritários.**
3. Fair Value / Ação = Equity Value / Shares Outstanding.
4. **Ajustar shares por SBC dilution futura + stock splits + bonificações.**
5. Banda de valor: Fair Value ± margem de segurança.
6. **Calcular ERP implícito no Fair Value** e comparar com ERP de mercado (Damodaran).
7. **Calcular Net Payout Yield**: (Buybacks + Dividendos − Emissões) / Market Cap.
8. **Tabela de sensibilidade NTN-B × premissa-chave 7×7.**
9. **Apresentar a expectativa integrada do ERP e Custo de Capital Real do modelo consolidado.**

**Referências:**
- **Livro 13** (Damodaran): bridge EV → Equity.
- **Livro 87** (McKinsey, Cap. 10): From Enterprise to Equity.
- **Livro 86** (Lundholm/Sloan, Cap. 10): bridge contábil.
- **Livro 12** (Marks): margin of safety.
- **P20** (SBC): diluição futura.

---

## Passo 6.4 — Comparação Institucional (Sell-Side / Consenso)

**Ação:**
1. Buscar target prices e projeções-chave de múltiplas casas de análise e Equity Research institucionais.
2. Comparar o Fair Value final e as projeções de crescimento e margens do nosso modelo contra o consenso.
3. Avaliar explicitamente:
   - **Similaridades**: Onde concordamos com o mercado.
   - **Divergências**: O que o mercado está precificando errado segundo nosso framework.
4. Documentar se a divergência é uma oportunidade de alfa ou se há informação que estamos ignorando.

**Output:** Fair Value por Ação. Tabela Bridge Equity. Tabela Sensibilidade 7×7. Expected Value por cenário. ERP e Custo de Capital implícitos. Tabela de Comparação Institucional.
