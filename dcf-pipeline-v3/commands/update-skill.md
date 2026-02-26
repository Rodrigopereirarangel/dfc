---
name: /update-skill
description: Comando de feedback — analisa interações recentes e propõe melhorias nas skills.
---

# /update-skill

## Comportamento
1. Analisar as últimas 3 interações com o usuário.
2. Identificar erros, correções manuais ou melhorias sugeridas.
3. Propor **reescrita específica** das instruções internas afetadas.
4. Apresentar **diff claro** (antes vs depois) para aprovação do usuário.
5. Se aprovado, salvar versão nova + log em `changelog/feedback-log.md`.

## Formato do Log
```
[Data] [Interação que gerou feedback]
[Erro identificado]
[Instrução anterior]
[Instrução nova (aprovada)]
[Status: aprovado/rejeitado/modificado]
```
