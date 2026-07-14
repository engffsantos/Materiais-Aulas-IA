# Laboratório 10.01 — Corrective RAG com LangGraph

> **Obrigatório — 3h30.**

## Objetivos

- Modelar estado e nós.
- Corrigir busca insuficiente.
- Limitar ciclos e registrar decisões.

## Ambiente recomendado

- Google Colab para notebooks e experimentos.
- GitHub Codespaces/VS Code Web para código estruturado.
- VS Code local é opcional.
- Credenciais somente em Secrets ou variáveis de ambiente.

## Roteiro

1. Defina estado com pergunta, consulta, tentativas, documentos, avaliação, resposta e erro.
2. Implemente nós retrieve, grade, rewrite, generate, abstain e finish.
3. Crie roteamento condicional.
4. Limite a duas correções e configure timeout por nó.
5. Registre traces sem conteúdo sensível.
6. Teste caminhos direto, corrigido, sem sucesso, falha e não respondível.

## Entregáveis

- `src/agentic/corrective_graph.py`.
- Diagrama Mermaid.
- Testes dos caminhos.
- Relatório de traces.

Use o template [`relatorio-laboratorio.md`](../../../../recursos-compartilhados/templates/relatorio-laboratorio.md) para documentar hipótese, ambiente, resultados e conclusão.

## Critério de avaliação

Fluxo 35%; limites 25%; testes 25%; observabilidade 15%.

## Regras de segurança e qualidade

- Não inclua chaves, tokens ou dados pessoais no Git.
- Registre versões e parâmetros relevantes.
- Diferencie evidência observada de hipótese.
- Inclua tratamento de erros e testes quando aplicável.
- Não declare melhoria sem comparação antes/depois.

## Estrutura da pasta

- `starter/`: arquivos iniciais sugeridos.
- `entrega/`: área local para a entrega do aluno; arquivos grandes devem permanecer fora do Git.
