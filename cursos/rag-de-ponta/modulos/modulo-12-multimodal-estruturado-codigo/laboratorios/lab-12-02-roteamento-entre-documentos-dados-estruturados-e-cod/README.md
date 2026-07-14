# Laboratório 12.02 — Roteamento entre documentos, dados estruturados e código

> **Obrigatório — 2h30.**

## Objetivos

- Consultar dados estruturados com controle.
- Recuperar código por símbolos.
- Rotear pela fonte adequada.

## Ambiente recomendado

- Google Colab para notebooks e experimentos.
- GitHub Codespaces/VS Code Web para código estruturado.
- VS Code local é opcional.
- Credenciais somente em Secrets ou variáveis de ambiente.

## Roteiro

1. Implemente ferramenta somente leitura para CSV ou SQLite embutido.
2. Use allowlist de tabelas/colunas, limite de linhas e timeout.
3. Divida código Python por AST, caminho, classe e função.
4. Combine busca lexical e semântica para código.
5. Classifique perguntas em documental, estruturada, código, combinação ou fora de escopo.
6. Teste tentativa de comando destrutivo.

## Entregáveis

- `src/routing/source_router.py`.
- Ferramenta read-only.
- Indexador de código.
- Testes de segurança.
- Relatório de roteamento.

Use o template [`relatorio-laboratorio.md`](../../../../recursos-compartilhados/templates/relatorio-laboratorio.md) para documentar hipótese, ambiente, resultados e conclusão.

## Critério de avaliação

Agregações e cálculos devem usar ferramenta estruturada, não aproximação vetorial.

## Regras de segurança e qualidade

- Não inclua chaves, tokens ou dados pessoais no Git.
- Registre versões e parâmetros relevantes.
- Diferencie evidência observada de hipótese.
- Inclua tratamento de erros e testes quando aplicável.
- Não declare melhoria sem comparação antes/depois.

## Estrutura da pasta

- `starter/`: arquivos iniciais sugeridos.
- `entrega/`: área local para a entrega do aluno; arquivos grandes devem permanecer fora do Git.
