---
description: Guia de Instalação e Integração dos Agentes MCP (Fundo Autônomo)
---

# INTEGRAÇÃO DO MCP NO DCF PIPELINE

O DCF Pipeline v3.2 foi projetado para extrair o máximo de autonomia quando integrado a ferramentas de Model Context Protocol (MCP).

Para habilitar a capacidade de Scraping, Memória Persistente e Banco de Dados, siga este guia:

## 1. Onde colocar o arquivo de configuração
O arquivo de configuração do Claude não fica na pasta do projeto, ele fica na raiz do sistema operacional do seu Computador (Windows / Mac).

**No Windows:**
Abra o "Executar" (`Win + R`) e digite:
`%APPDATA%\Claude\claude_desktop_config.json`

## 2. Configuração do Fundo de Hedge Box Stack
Copie o conteúdo do arquivo `claude_desktop_config.template.json` que está na raiz deste repositório e cole no seu json do passo 1.

### O que cada servidor ativado fará:

* **Fetch (Scraper):** O Claude agora conseguirá acessar URLs (notícias, fundamentus, release CVM). O pipeline foi instruído a usar essa ferramenta na Fase 1 (Auditoria) e Fase 0.2 se faltar dados.
* **Memory (Oracle):** Ao detectar que aprendeu uma lição importante na Fase 8, o Claude salvará a "Base-rate" no grafo de conhecimento. Na próxima empresa que analisar, ele perguntará ao Memory se já há viés conhecido.
* **SQLite (Storage):** Você terá um arquivo `dcf_database.db` no seu repositório. O Claude deverá disparar os `JSON_PAYLOADS` para o banco de dados em formato tabular ao final de cada pipeline, permitindo criar dashboards.

## 3. Pré-requisitos 
O Claude usará os empacotadores nativos (`uvx` do python e `npx` do node) para gerir os plugins em background.
Certifique-se de ter instalado globalmente no seu Windows:
- Node.js (`npm` e `npx`)
- uv (`pip install uv` em caso de falha do UV nativo)

## 4. Como testar
Reinicie o aplicativo Claude Desktop. Você deverá ver as ferramentas com ícones de chave-inglesa.
Digite no Claude: "Quais os seus servidores MCP ativos?" e ele deve reportar Fetch, Sqlite e Memory prontos para o Pipelining.
