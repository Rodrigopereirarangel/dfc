---
description: Roda o DCF Pipeline v4.0 completo para um ticker — /dfc [TICKER]
---

# Workflow: /dfc [TICKER]

## Uso
```
/dfc PSSA3
/dfc ITUB4
/dfc VALE3
```

## O que este workflow faz

Executa o DCF Pipeline v4.0 em sequência completa para o ticker informado, do enquadramento estratégico até o PDF institucional. Cada fase entrega os **5 Blocos Institucionais + Síntese §1–§5 + DataViz + JSON Payload**.

---

## Passos

### 1. Extrair o ticker do comando

Identificar o ticker fornecido após `/dfc`. Se ausente → solicitar: _"Informe o ticker. Ex: `/dfc PSSA3`"_

### 2. Anunciar o início do pipeline

Exibir banner:

```
╔══════════════════════════════════════════════════════════════════╗
║  DCF PIPELINE v4.0 — ANÁLISE FUNDAMENTALISTA INSTITUCIONAL      ║
║  Ticker: [TICKER]  |  Início: [DATA/HORA]                       ║
║  Fases: 0 → 1 → 2 → 2.5 → 3 → 4 → 5A(GATE) → 5 → 6 → 7 → 8 → 9 ║
╚══════════════════════════════════════════════════════════════════╝
```

### 3. Buscar dados de mercado

Via `yfinance` / fontes públicas:
- Preço atual, market cap, volume, short interest, beta
- Histórico de preços (5 anos)
- Dividendos pagos

Registrar data e fonte de cada dado capturado.

### 4. Executar FASE 0 — Inteligência Competitiva

Seguir `skills/fase0-estrategia/SKILL.md` completo:
- Passo 0.1: 5 Forças Porter + Nota de Durabilidade do Moat
- Passo 0.2: Reverse DCF + MEROI + Diagnóstico de Mercado
- Passo 0.3: Sentimento de Mercado (short interest, dispersão sell-side)
- Passo 0.4: Narrativa → Números + Pre-mortem (inversão)
- **Exportar JSON_PAYLOAD F0_COMPLETA**

### 5. Executar FASE 1 — Auditoria Contábil Forense

Seguir `skills/fase1-auditoria-contabil/SKILL.md`:
- Passo 1.1: Beneish M-Score + Qualidade do Lucro
- Passo 1.2: Normalização + ROE DuPont 5 níveis
- Passo 1.3: 3-Statement Model + Tabelas históricas
- **Exportar JSON_PAYLOAD F1_COMPLETA**

### 6. Executar FASE 2 — Value Drivers

Seguir `skills/fase2-value-drivers/SKILL.md`:
- Passo 2.1: ROIC, Fade Rate, CAP implícito
- Passo 2.2: Capex Red Queen (manutenção vs. crescimento)
- Passo 2.3: Unit Economics por vertical
- Passo 2.4: Tornado Chart de Sensibilidade
- **Exportar JSON_PAYLOAD F2_COMPLETA**

### 7. Executar FASE 2.5 — Análise da Gestão

Seguir `skills/fase25-management/SKILL.md`:
- Passo 2.5.1: Track Record de Assertividade → haircut calculado
- Passo 2.5.2: Capital Allocation 10 anos
- Passo 2.5.3: Projetos em Ramp-up (S-curves)
- **Exportar JSON_PAYLOAD F25_COMPLETA**

### 8. Executar FASE 3 — Projeção dos Fluxos de Caixa

Seguir `skills/fase3-projecao-fcff/SKILL.md`:
- Passo 3.1: Projeção de Receita Bottom-Up
- Passo 3.2: Margens e Custos
- Passo 3.3: FCFF Projetado (10 anos) + Check g = ROIIC × Reinv.Rate
- **Exportar JSON_PAYLOAD F3_COMPLETA**

### 9. Executar FASE 4 — Taxa de Desconto (WACC)

Seguir `skills/fase4-wacc/SKILL.md`:
- Passo 4.1: COE via CAPM + Regra Penman
- Passo 4.2: WACC term structure + Penman test
- **Exportar JSON_PAYLOAD F4_COMPLETA**

### 10. Executar FASE 5A — GATE (Auditoria 360°)

Seguir `skills/fase5a-auditoria360/SKILL.md`.

> ⚠️ **PARADA OBRIGATÓRIA:**  
> Se **GATE = ❗ REPROVADO** → NÃO prosseguir. Reportar o bloco com erro e aguardar correção antes de continuar.  
> Se **GATE = ✅ APROVADO** → continuar para a Fase 5.

- **Exportar JSON_PAYLOAD F5A_GATE**

### 11. Executar FASE 5 — Valor Terminal

Seguir `skills/fase5-terminal-value/SKILL.md`:
- McKinsey Continuing Value + crosschecks (EPV, Exit Multiple, Penman)
- Sanity checks (TV/EV%, g vs GDP, ROIC terminal)
- **Exportar JSON_PAYLOAD F5_COMPLETA**

### 12. Executar FASE 6 — Agregação & Fair Value

Seguir `skills/fase6-agregacao/SKILL.md`:
- Cenários ponderados (Distress/Bear/Base/Bull) + Expected Value
- Bridge EV → Equity Value → Fair Value/Ação
- Tabela de sensibilidade 7×7 + ERP implícito
- Comparação com consenso sell-side
- **Exportar JSON_PAYLOAD F6_COMPLETA**

### 13. Executar FASE 7 — Stress Test & Triangulação

Seguir `skills/fase7-stress-test/SKILL.md`:
- Via Negativa (curto/médio/longo prazo)
- Auditoria de vieses cognitivos
- Football Field Valuation (triangulação ≥ 3 métodos) + QMJ Score
- **Exportar JSON_PAYLOAD F7_COMPLETA**

### 14. Executar FASE 8 — Decisão: Conviction & Sizing

Seguir `skills/fase8-decisao/SKILL.md`:
- Conviction Score composto (6 dimensões ponderadas)
- Position Sizing via Kelly (Half-Kelly recomendado)
- Watchlist de catalisadores + condições de stop-loss
- **Exportar JSON_PAYLOAD F8_COMPLETA**

### 15. Executar FASE 9 — Geração do PDF Institucional

Seguir `skills/fase9-pdf-institucional/SKILL.md`.

Apresentar o comando de geração do PDF ao usuário:

```bash
pip install reportlab matplotlib seaborn numpy pandas

# Com payload real (após coletar os JSON_PAYLOADs)
python scripts/generate_pdf.py \
    --ticker [TICKER] \
    --output "[TICKER]_Initiation_Coverage_2026.pdf"

# Modo demo (validar formatação)
python scripts/generate_pdf.py --ticker [TICKER] --demo
```

### 16. Banner de encerramento

```
╔══════════════════════════════════════════════════════════════════╗
║  ✅ DCF PIPELINE v4.0 — ANÁLISE CONCLUÍDA                       ║
║  Ticker: [TICKER]  |  Fair Value: R$X  |  Recomendação: X       ║
║  Conviction: X/10  |  Kelly: X%  |  Posição Máx: X% portfólio  ║
╚══════════════════════════════════════════════════════════════════╝
```
