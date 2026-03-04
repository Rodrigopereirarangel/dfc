---
name: "Fase 9 — Empacotamento Institucional & Geração de PDF"
description: |
  Consolida toda a análise das Fases 0-8 em um relatório PDF de nível institucional.
  Triggers: "gerar PDF", "relatório final", "initiation report", "PDF"
---

# FASE 9 — EMPACOTAMENTO INSTITUCIONAL & GERAÇÃO DE PDF

> **Entradas:** JSON Payloads de todas as Fases 0-8.
> **Script:** `scripts/generate_pdf.py`

## 🎯 OBJETIVO

Consolidar toda a análise gerada nas Fases 0 a 8 e entregar um **Arquivo PDF de Nível Institucional**, visualmente equivalente a um relatório de iniciação de cobertura de banco de primeira linha (Goldman Sachs, BTG Pactual, Morgan Stanley).

---

## Passo 9.1 — Arquitetura do Relatório

**Estrutura Obrigatória do Documento:**

### Capa (Página 1)
- **Logo e Nome da Empresa / Ticker**
- **Recomendação:** Compra / Manter / Vender (em destaque, cor semáforo)
- **Preço Alvo (Expected Value):** R$X
- **Preço Atual:** R$X | **Upside/Downside:** X%
- **Conviction Score:** X/10
- **Data da Análise**
- **Investment Thesis:** 1 parágrafo (§1 da Síntese da Fase 0 compactado)

### Sumário Executivo (Página 2)
- Tabela de Cenários (Distress / Bear / Base / Bull / Expected Value)
- Tabela Triangulação (Football Field — versão compacta)
- Kelly Sizing e Recomendação de Posição
- Top 3 Riscos e Top 3 Catalisadores

### Corpo do Relatório (Páginas 3 a 5 — Síntese Magna de Investimento)
Em vez de tentar transcrever o chat inteiro (o que excede sua memória de contexto), redija uma **Síntese Magna / Executive Summary profundamente detalhada (alvo: ~3 páginas completas)**. Mergulhe a fundo nos seguintes pilares de tese, sem poupar tokens em argumentação analítica:
- **Tese de Qualidade e Fosso (F0 e F1):** Disseque as vantagens competitivas, a resiliência do modelo de negócio frente aos pares, e a qualidade intrínseca do lucro normalizado que você encontrou.
- **Microeconomia e Drivers (F2 e F2.5):** Aprofunde-se no período de vantagem competitiva (CAP), no Unit Economics, e como o Management tem alocado capital (Track Record).
- **Projeções e Crescimento (F3):** Descreva a trajetória baseada nos múltiplos métodos (Bottom-Up vs Consenso), detalhando onde o mercado está errando na precificação das margens e do crescimento de Receita/FCFF.
- **Valuation e Retorno (F4, F5, F6):** Explique detalhadamente o risco embutido (WACC) e fundamente qual foi o ponto exato da Triangulação Central (Football Field) que originou o Preço Justo apontado.
- **Assimetrias e Riscos Caudais (F7 e F8):** Explore as fragilidades reveladas na simulação de Monte Carlo/Via Negativa e descreva o Risco/Retorno assimétrico encontrado para justificar a Recomendação.

### Rodapé Padrão em Cada Página
- Ticker | Data | "Análise Fundamentalista — DCF Pipeline v4.0"
- Number de página
- *Disclaimer: Esta análise não constitui recomendação formal de investimento.*

---

## Passo 9.2 — Gráficos Obrigatórios por Fase

| Fase | Gráfico Obrigatório | Tipo |
|---|---|---|
| F0 | Spider Chart (Vantagem Competitiva) | Radar |
| F1 | Waterfall Lucro Reportado → Normalizado | Cascata |
| F1 | ROE DuPont com linha COE | Barras + Linha |
| F2 | Fade ROIC → WACC por cenário | Linhas convergentes |
| F2 | Tornado Chart de Sensibilidade | Barras horizontais |
| F2.5 | Capital Allocation Stacked 10A | Barras empilhadas |
| F3 | Receita e Margem (histórico vs. projetado) | Área + Linha |
| F4 | Term Structure do WACC | Linha escalonada |
| F5 | Comparação de Métodos de TV | Barras horizontais |
| F6 | Football Field Valuation | Barras horizontais sobrepostas |
| F6 | Heatmap Sensibilidade 7×7 | Mapa de calor |
| F7 | Distribuição Monte Carlo (KDE) | KDE Plot |
| F8 | Conviction Score Disaggregation | Bar-chart horizontal |
| F8 | Timeline de Catalisadores | Gantt/Timeline |

---

## Passo 9.3 — Instruções de Tipografia e Paleta Institucional

**Paleta Oficial:**
```python
PALETA = {
    "azul_marinho": "#003366",     # Cor primária, barras principais
    "azul_medio": "#336699",       # Cor secundária, barras alternativas
    "cinza_ardosia": "#4A4A4A",    # Texto corpo, tabelas
    "cinza_claro": "#A0A0A0",      # Gridlines, linhas secundárias
    "ambar": "#CBA052",            # Destaques, Expected Value
    "verde_aprovado": "#27AE60",   # Status OK, retorno positivo
    "amarelo_atencao": "#F1C40F",  # Status atenção, zona neutra
    "vermelho_grave": "#C0392B",   # Status grave, retorno negativo
    "vermelho_escuro": "#8B0000",  # Barras negativas em cascata
    "branco": "#FFFFFF",           # Fundo padrão
    "fundo_capa": "#001F3F"        # Azul marinho escuro para capa
}
```

**Tipografia:**
- Fonte do documento: **Helvetica Neue** ou **Calibri** (via reportlab).
- Títulos de seção: Bold, 14pt, Azul Marinho.
- Corpo do texto: Regular, 10pt, Cinza Ardósia.
- Cabeçalhos de tabela: Bold, 9pt, fundo Azul Marinho, texto Branco.
- Linhas de tabela zebradas: alternando Branco e Cinza 5% (#F5F5F5).
- Anotações de gráfico: Light, 8pt, Cinza Ardósia.

**Estilo de Gráficos (padrão Bloomberg):**
- Sem gridlines verticais.
- Gridlines horizontais com 20% de opacidade (cinza claro).
- Legendas no topo esquerdo.
- Títulos acima do gráfico, fonte Bold 10pt.
- Sem bordas de quadro (spine removido) — apenas eixo X inferior.

---

## Passo 9.4 — Execução do Script

**Comando (via Playwright / motor HTML):**
```bash
# 1. Escreva a "Síntese Magna / Executive Summary" baseada nos passos acima.
# 2. Salve seu texto executivo no arquivo `output_payloads/[TICKER]_report.md`.
# 3. Rode o script gerador do PDF final:

python scripts/generate_pdf.py \
    --ticker XXXX3 \
    --report "output_payloads/XXXX3_report.md" \
    --output "XXXX3_Initiation_Coverage_2026.pdf"
```

**Fallback (se o ambiente não tiver Playwright instalado):**
Certifique-se que executou o bootstrap:
```bash
python scripts/bootstrap.py
python scripts/generate_pdf.py --ticker XXXX3 --demo
```
O modo `--demo` gera um HTML corporativo com dados de exemplo.

---

```
╔══════════════════════════════════════════════════════════════════╗
║  📌 SÍNTESE INSTITUCIONAL — Fase 9 Completa                     ║
╚══════════════════════════════════════════════════════════════════╝
§1 O PDF consolida todo o trabalho analítico das Fases 0-8 em um único documento de referência.
§2 O relatório é o entregável final que pode ser compartilhado com comitê de investimentos.
§3 A qualidade depende diretamente da completude dos JSON Payloads exportados nas fases anteriores.
§4 Verificar que todos os 14 gráficos obrigatórios foram gerados antes de finalizar o PDF.
§5 Um PDF incompleto ou visualmente inferior ao padrão institucional é equivalente a não entregar.
```

**Referências:**
- `scripts/generate_pdf.py`: script Python autossuficiente.
- `references/base-rates.md`: dados para validação gráfica.
- Padrão visual: Goldman Sachs Equity Research / Bloomberg Intelligence.

---

## ✅ CHECKLIST DE COMPLIANCE — VALIDAÇÃO OBRIGATÓRIA ANTES DE AVANÇAR

Antes de passar para a próxima fase, o Agente AI DEVE verificar e imprimir este checklist PREENCHIDO com **[V]** (Verdadeiro) ou **[F]** (Falso) em sua resposta:

```text
[CHECKLIST DE COMPLIANCE DO AGENTE — FASE F9]
[V/F] Eu abri e li integralmente este arquivo SKILL.md usando a minha ferramenta de leitura de arquivos.
[V/F] Eu executei TODOS os sub-passos desta fase (não pulei nenhum).
[V/F] Eu entreguei os 5 Blocos (Diagnóstico / Narrativa / DataViz / Trade-off / Analogia) em CADA sub-passo.
[V/F] Eu incluí a instrução DataViz específica (tipo de gráfico + paleta + eixos) no BLOCO 3 de cada passo.
[V/F] Eu apresentei a Síntese Institucional (§1 a §5) ao final desta fase.
[V/F] Eu fechei a resposta gerando o bloco ```json com a taxonomia exata desta fase.
```

**Se qualquer item for (F):** PARE. Não avance. Corrija a sua resposta e reentregue antes de prosseguir para a próxima fase.

Validação automática: `python scripts/validate_compliance.py --clipboard --fase F9`
