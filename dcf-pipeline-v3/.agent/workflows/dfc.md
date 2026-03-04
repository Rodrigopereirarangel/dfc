---
description: Roda o DCF Pipeline v4.0 completo para um ticker — /dfc [TICKER]
---

# Workflow: /dfc [TICKER]

## Uso
```
`/dfc PSSA3` (Modo Autônomo com Macro-Checkpoints — Padrão)
`/dfc ITUB4 manual` (Modo Manual com pausas em cada fase)
`/dfc VALE3`
```

## O que este workflow faz

Executa o DCF Pipeline v4.0 em sequência completa para o ticker informado, do enquadramento estratégico até o PDF institucional. Cada fase entrega os **5 Blocos Institucionais + Síntese §1–§5 + DataViz + JSON Payload**.

> 🧠 **REGRA DE OURO — FLUXO CONTÍNUO E INTEGRAÇÃO DE NARRATIVA:**
> 1. **Modo Autônomo com Macro-Checkpoints (Padrão):** O comando `/dfc [TICKER]` executará a análise em fluxo contínuo. Sua ÚNICA restrição é que **VOCÊ DEVE PAUSAR OBRIGATORIAMENTE EM 3 MACRO-CHECKPOINTS** (fim das Fases 2.5, 5 e 8) para apresentar as escolhas A/B dos "Trade-offs" e aguardar a escolha do usuário antes de continuar. Fora desses 3 pontos (ou em caso de erro), **NÃO PARE** e continue gerando o texto imediatamente na mesma resposta.
> 2. **Modo Manual:** Se chamado com `/dfc [TICKER] manual`, você deve paurar e exibir "Aguardando confirmação do usuário para avançar" após o banner de roda Fase.
> 3. **Integração Coesa:** Trate cada fase como o próximo capítulo de um único Relatório Institucional. Não repita informações (como a descrição básica da empresa) nas fases subsequentes. Conecte as ideias, citando as descobertas das fases anteriores. Se houver discrepância entre premissas, explique-as no texto.
> 4. **Leitura Segmentada e Estética:** Faça uso criterioso de formatação rica. Use listas (`-`), sub-cabeçalhos (`###`), negritos vitais, e introduza emojis estratégicos para estruturar visualmente a leitura (ex: 💡 Insight, ⚠️ Risco, 🚀 Oportunidade, ⚖️ Trade-off, 📉 Queda, 📈 Crescimento).

---

## Passos

### 0. Bootstrap Automático (AÇÃO DO AGENTE)
**ANTES DE QUALQUER COISA**, assim que receber o comando `/dfc`, VOCÊ (Claude/Agente) deve abrir o terminal (Computer Use) e rodar autonomamente:
```bash
python scripts/bootstrap.py
```
Aguarde a execução terminar para garantir que Python, Playwright, Markdown e YFinance estejam corretos antes de fazer o Passo 1. O usuário NÃO precisa e NÃO deve rodar isso, é sua obrigação.

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

### 3. Declarar Template Ativo (PRIMEIRA SAÍDA OBRIGATÓRIA)

**Sua PRIMEIRA linha de resposta ao receber `/dfc [TICKER]` DEVE ser:**

```
╔══════════════════════════════════════════════════════════════════╗
║  📋 DCF Pipeline v4.0 — [TICKER] | Template ativo               ║
║  Estrutura: 5 Blocos × N passos × Síntese §1-§5 × JSON Payload  ║
║  Fallback: validate → repair → re-validate antes de avançar      ║
╚══════════════════════════════════════════════════════════════════╝
```

NUNCA escreva análise antes deste banner. NUNCA comprima fases numa única resposta.

### 4. Executar FASE 0 — Inteligência Competitiva

> 🛑 **SEQUÊNCIA OBRIGATÓRIA PARA O AGENTE AI:**
> 1. Preencha o template de 5 Blocos célula a célula (ver SKILL.md raiz — seção TEMPLATE OBRIGATÓRIO)
> 2. Após cada Bloco, execute o auto-check da tabela de critérios mínimos (FALLBACK Nível 1)
> 3. Ao fechar a fase, rode: `python scripts/fallback_repair.py --clipboard --fase F0`
> 4. Se Exit 1 → aplique reparos listados e re-valide. Se Exit 0 → **MACRO-CHECKPOINT MODE: GERAR A PRÓXIMA FASE NA MESMA RESPOSTA!** Não pare de escrever, exceto se estiver no Checkpoint Alpha, Beta ou Final.

**Passos desta fase:**
- Passo 0.1: 5 Forças Porter + Nota de Durabilidade do Moat
- Passo 0.2: Reverse DCF + MEROI + Diagnóstico de Mercado
- Passo 0.3: Sentimento de Mercado (short interest, dispersão sell-side)
- Passo 0.4: Narrativa → Números + Pre-mortem (inversão)
- **Exportar JSON_PAYLOAD F0_COMPLETA**


### 5. Executar FASE 1 — Auditoria Contábil Forense

> 🛑 **AÇÃO BLOQUEANTE PARA O AGENTE AI:**
> VOCÊ É OBRIGADO a acionar a tool de leitura de arquivos (`view_file`/`read`) para ler o arquivo `skills/fase1-auditoria-contabil/SKILL.md` INTEGRALMENTE agora mesmo. NUNCA inicie a fase baseando-se apenas num resumo. Omitir a leitura constitui falha crítica.
> Após a confirmação da leitura, execute a fase seguindo o formato de 5 Blocos Institucionais e feche imprimindo o seu ✅ CHECKLIST DE COMPLIANCE.

**Resumo (Não substitui a leitura):**
- Passo 1.1: Beneish M-Score + Qualidade do Lucro
- Passo 1.2: Normalização + ROE DuPont 5 níveis
- Passo 1.3: 3-Statement Model + Tabelas históricas
- **Exportar JSON_PAYLOAD F1_COMPLETA**

### 6. Executar FASE 2 — Value Drivers

> 🛑 **AÇÃO BLOQUEANTE PARA O AGENTE AI:**
> VOCÊ É OBRIGADO a acionar a tool de leitura de arquivos (`view_file`/`read`) para ler o arquivo `skills/fase2-value-drivers/SKILL.md` INTEGRALMENTE agora mesmo. NUNCA inicie a fase baseando-se apenas num resumo. Omitir a leitura constitui falha crítica.
> Após a confirmação da leitura, execute a fase seguindo o formato de 5 Blocos Institucionais e feche imprimindo o seu ✅ CHECKLIST DE COMPLIANCE.

**Resumo (Não substitui a leitura):**
- Passo 2.1: ROIC, Fade Rate, CAP implícito
- Passo 2.2: Capex Red Queen (manutenção vs. crescimento)
- Passo 2.3: Unit Economics por vertical
- Passo 2.4: Tornado Chart de Sensibilidade
- **Exportar JSON_PAYLOAD F2_COMPLETA**

### 7. Executar FASE 2.5 — Análise da Gestão

> 🛑 **AÇÃO BLOQUEANTE PARA O AGENTE AI:**
> VOCÊ É OBRIGADO a acionar a tool de leitura de arquivos (`view_file`/`read`) para ler o arquivo `skills/fase25-management/SKILL.md` INTEGRALMENTE agora mesmo. NUNCA inicie a fase baseando-se apenas num resumo. Omitir a leitura constitui falha crítica.
> Após a confirmação da leitura, execute a fase seguindo o formato de 5 Blocos Institucionais e feche imprimindo o seu ✅ CHECKLIST DE COMPLIANCE.

**Resumo (Não substitui a leitura):**
- Passo 2.5.1: Track Record de Assertividade → haircut calculado
- Passo 2.5.2: Capital Allocation 10 anos
- Passo 2.5.3: Projetos em Ramp-up (S-curves)
- **Exportar JSON_PAYLOAD F25_COMPLETA**

### 8. Executar FASE 3 — Projeção dos Fluxos de Caixa

> 🛑 **AÇÃO BLOQUEANTE PARA O AGENTE AI:**
> VOCÊ É OBRIGADO a acionar a tool de leitura de arquivos (`view_file`/`read`) para ler o arquivo `skills/fase3-projecao-fcff/SKILL.md` INTEGRALMENTE agora mesmo. NUNCA inicie a fase baseando-se apenas num resumo. Omitir a leitura constitui falha crítica.
> Após a confirmação da leitura, execute a fase seguindo o formato de 5 Blocos Institucionais e feche imprimindo o seu ✅ CHECKLIST DE COMPLIANCE.

**Resumo (Não substitui a leitura):**
- Passo 3.1: Projeção de Receita Bottom-Up
- Passo 3.2: Margens e Custos
- Passo 3.3: FCFF Projetado (10 anos) + Check g = ROIIC × Reinv.Rate
- **Exportar JSON_PAYLOAD F3_COMPLETA**

### 9. Executar FASE 4 — Taxa de Desconto (WACC)

> 🛑 **AÇÃO BLOQUEANTE PARA O AGENTE AI:**
> VOCÊ É OBRIGADO a acionar a tool de leitura de arquivos (`view_file`/`read`) para ler o arquivo `skills/fase4-wacc/SKILL.md` INTEGRALMENTE agora mesmo. NUNCA inicie a fase baseando-se apenas num resumo. Omitir a leitura constitui falha crítica.
> Após a confirmação da leitura, execute a fase seguindo o formato de 5 Blocos Institucionais e feche imprimindo o seu ✅ CHECKLIST DE COMPLIANCE.

**Resumo (Não substitui a leitura):**
- Passo 4.1: COE via CAPM + Regra Penman
- Passo 4.2: WACC term structure + Penman test
- **Exportar JSON_PAYLOAD F4_COMPLETA**

### 10. Executar FASE 5A — GATE (Auditoria 360°)

> 🛑 **AÇÃO BLOQUEANTE PARA O AGENTE AI:**
> VOCÊ É OBRIGADO a acionar a tool de leitura de arquivos (`view_file`/`read`) para ler o arquivo `skills/fase5a-auditoria360/SKILL.md` INTEGRALMENTE agora mesmo. NUNCA inicie a fase baseando-se apenas num resumo. Omitir a leitura constitui falha crítica.
> Após a confirmação da leitura, execute a fase seguindo o formato de 5 Blocos Institucionais e feche imprimindo o seu ✅ CHECKLIST DE COMPLIANCE.

**Resumo (Não substitui a leitura):**

> ⚠️ **PARADA OBRIGATÓRIA:**  
> Se **GATE = ❗ REPROVADO** → NÃO prosseguir. Reportar o bloco com erro e aguardar correção antes de continuar.  
> Se **GATE = ✅ APROVADO** → **MODO AUTÔNOMO: GERAR A FASE 5 NA MESMA RESPOSTA!** Não pare de escrever. **MODO MANUAL: parar.**

- **Exportar JSON_PAYLOAD F5A_GATE**

### 11. Executar FASE 5 — Valor Terminal

> 🛑 **AÇÃO BLOQUEANTE PARA O AGENTE AI:**
> VOCÊ É OBRIGADO a acionar a tool de leitura de arquivos (`view_file`/`read`) para ler o arquivo `skills/fase5-terminal-value/SKILL.md` INTEGRALMENTE agora mesmo. NUNCA inicie a fase baseando-se apenas num resumo. Omitir a leitura constitui falha crítica.
> Após a confirmação da leitura, execute a fase seguindo o formato de 5 Blocos Institucionais e feche imprimindo o seu ✅ CHECKLIST DE COMPLIANCE.

**Resumo (Não substitui a leitura):**
- McKinsey Continuing Value + crosschecks (EPV, Exit Multiple, Penman)
- Sanity checks (TV/EV%, g vs GDP, ROIC terminal)
- **Exportar JSON_PAYLOAD F5_COMPLETA**

### 12. Executar FASE 6 — Agregação & Fair Value

> 🛑 **AÇÃO BLOQUEANTE PARA O AGENTE AI:**
> VOCÊ É OBRIGADO a acionar a tool de leitura de arquivos (`view_file`/`read`) para ler o arquivo `skills/fase6-agregacao/SKILL.md` INTEGRALMENTE agora mesmo. NUNCA inicie a fase baseando-se apenas num resumo. Omitir a leitura constitui falha crítica.
> Após a confirmação da leitura, execute a fase seguindo o formato de 5 Blocos Institucionais e feche imprimindo o seu ✅ CHECKLIST DE COMPLIANCE.

**Resumo (Não substitui a leitura):**
- Cenários ponderados (Distress/Bear/Base/Bull) + Expected Value
- Bridge EV → Equity Value → Fair Value/Ação
- Tabela de sensibilidade 7×7 + ERP implícito
- Comparação com consenso sell-side
- **Exportar JSON_PAYLOAD F6_COMPLETA**

### 13. Executar FASE 7 — Stress Test & Triangulação

> 🛑 **AÇÃO BLOQUEANTE PARA O AGENTE AI:**
> VOCÊ É OBRIGADO a acionar a tool de leitura de arquivos (`view_file`/`read`) para ler o arquivo `skills/fase7-stress-test/SKILL.md` INTEGRALMENTE agora mesmo. NUNCA inicie a fase baseando-se apenas num resumo. Omitir a leitura constitui falha crítica.
> Após a confirmação da leitura, execute a fase seguindo o formato de 5 Blocos Institucionais e feche imprimindo o seu ✅ CHECKLIST DE COMPLIANCE.

**Resumo (Não substitui a leitura):**
- Via Negativa (curto/médio/longo prazo)
- Auditoria de vieses cognitivos
- Football Field Valuation (triangulação ≥ 3 métodos) + QMJ Score
- **Exportar JSON_PAYLOAD F7_COMPLETA**

### 14. Executar FASE 8 — Decisão: Conviction & Sizing

> 🛑 **AÇÃO BLOQUEANTE PARA O AGENTE AI:**
> VOCÊ É OBRIGADO a acionar a tool de leitura de arquivos (`view_file`/`read`) para ler o arquivo `skills/fase8-decisao/SKILL.md` INTEGRALMENTE agora mesmo. NUNCA inicie a fase baseando-se apenas num resumo. Omitir a leitura constitui falha crítica.
> Após a confirmação da leitura, execute a fase seguindo o formato de 5 Blocos Institucionais e feche imprimindo o seu ✅ CHECKLIST DE COMPLIANCE.

**Resumo (Não substitui a leitura):**
- Conviction Score composto (6 dimensões ponderadas)
- Position Sizing via Kelly (Half-Kelly recomendado)
- Watchlist de catalisadores + condições de stop-loss
- **Exportar JSON_PAYLOAD F8_COMPLETA**

### 15. Executar FASE 9 — Geração do PDF Institucional

> 🛑 **AÇÃO BLOQUEANTE PARA O AGENTE AI:**
> VOCÊ É OBRIGADO a acionar a tool de leitura de arquivos (`view_file`/`read`) para ler o arquivo `skills/fase9-pdf-institucional/SKILL.md` INTEGRALMENTE agora mesmo. NUNCA inicie a fase baseando-se apenas num resumo. Omitir a leitura constitui falha crítica.
> Após a confirmação da leitura, execute a fase seguindo o formato de 5 Blocos Institucionais e feche imprimindo o seu ✅ CHECKLIST DE COMPLIANCE.

**Resumo (Não substitui a leitura):**

**Como o PDF Institucional V4 usa Playwright renderizando Markdown Rico:**
A análise de todas as fases da Fase 0 à Fase 8 DEVE SER salva em um arquivo de Markdown consolidado: `output_payloads/[TICKER]_report.md`.
Use o `output-dcf-completo.md` como base, e certifique-se de que o arquivo final contém **TODO o texto narrativo, análises de todos os Blocos e Sínteses** que você gerou, segmentados com Títulos e formatação clara com emojis. **NÃO OMITA A NARRATIVA**.
Depois, execute:

```bash
python scripts/generate_pdf.py \
    --ticker [TICKER] \
    --report "output_payloads/[TICKER]_report.md" \
    --output "[TICKER]_Initiation_Coverage_2026.pdf"

# Modo demo (validar motor HTML/Chromium)
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
