# Laboratório 11.02 — Mini-GraphRAG: entidades, relações e consultas globais

> **Obrigatório — 2h30.**

## Objetivos

- Extrair entidades e relações.
- Criar grafo auditável.
- Comparar busca local e global.

## Ambiente recomendado

- Google Colab para notebooks e experimentos.
- GitHub Codespaces/VS Code Web para código estruturado.
- VS Code local é opcional.
- Credenciais somente em Secrets ou variáveis de ambiente.

## Roteiro

1. Extraia entidades, tipos, relações, descrição e `source_chunk_id`.
2. Normalize nomes de forma conservadora.
3. Crie grafo em NetworkX e detecte comunidades.
4. Gere resumos por comunidade com fontes.
5. Implemente consulta local e síntese global.
6. Audite amostra de entidades e relações.

## Entregáveis

- `src/graphrag/mini_graph.py`.
- JSON de entidades e relações.
- Visualização.
- Relatório local/global.
- Matriz de decisão.

Use o template [`relatorio-laboratorio.md`](../../../../recursos-compartilhados/templates/relatorio-laboratorio.md) para documentar hipótese, ambiente, resultados e conclusão.

## Critério de avaliação

Relações sem evidência textual devem ser rejeitadas.

## Regras de segurança e qualidade

- Não inclua chaves, tokens ou dados pessoais no Git.
- Registre versões e parâmetros relevantes.
- Diferencie evidência observada de hipótese.
- Inclua tratamento de erros e testes quando aplicável.
- Não declare melhoria sem comparação antes/depois.

## Estrutura da pasta

- `starter/`: arquivos iniciais sugeridos.
- `entrega/`: área local para a entrega do aluno; arquivos grandes devem permanecer fora do Git.
