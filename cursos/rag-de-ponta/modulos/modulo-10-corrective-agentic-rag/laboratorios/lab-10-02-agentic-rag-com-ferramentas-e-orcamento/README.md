# Laboratório 10.02 — Agentic RAG com ferramentas e orçamento

> **Obrigatório — 3h30.**

## Objetivos

- Criar ferramentas com contratos claros.
- Aplicar allowlist, orçamento e permissões.
- Comparar roteamento determinístico e agêntico.

## Ambiente recomendado

- Google Colab para notebooks e experimentos.
- GitHub Codespaces/VS Code Web para código estruturado.
- VS Code local é opcional.
- Credenciais somente em Secrets ou variáveis de ambiente.

## Roteiro

1. Crie ferramentas de busca pública, restrita, consulta estruturada simulada, calculadora e status.
2. Defina schemas, timeout, erros e autorização.
3. Implemente agente em LangGraph.
4. Limite chamadas, tokens, tempo e resultados.
5. Trate conteúdo recuperado como não confiável.
6. Compare qualidade, custo, latência e previsibilidade.

## Entregáveis

- `src/agentic/tool_agent.py`.
- Schemas.
- Testes de orçamento e ACL.
- Tabela comparativa.

Use o template [`relatorio-laboratorio.md`](../../../../recursos-compartilhados/templates/relatorio-laboratorio.md) para documentar hipótese, ambiente, resultados e conclusão.

## Critério de avaliação

O agente deve encerrar com segurança ao atingir qualquer limite.

## Regras de segurança e qualidade

- Não inclua chaves, tokens ou dados pessoais no Git.
- Registre versões e parâmetros relevantes.
- Diferencie evidência observada de hipótese.
- Inclua tratamento de erros e testes quando aplicável.
- Não declare melhoria sem comparação antes/depois.

## Estrutura da pasta

- `starter/`: arquivos iniciais sugeridos.
- `entrega/`: área local para a entrega do aluno; arquivos grandes devem permanecer fora do Git.
