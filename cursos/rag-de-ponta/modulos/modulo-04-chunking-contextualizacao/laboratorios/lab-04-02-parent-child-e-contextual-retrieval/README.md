# Laboratório 4.02 — Parent-child e contextual retrieval

> **Obrigatório — 3h30.**

## Objetivos

- Recuperar unidades pequenas e fornecer contexto maior.
- Preservar relação pai-filho.
- Comparar contextualização com baseline.

## Ambiente recomendado

- Google Colab para notebooks e experimentos.
- GitHub Codespaces/VS Code Web para código estruturado.
- VS Code local é opcional.
- Credenciais somente em Secrets ou variáveis de ambiente.

## Roteiro

1. Crie seções-pai e chunks-filhos.
2. Armazene `parent_id`, `child_id`, título, seção e posição.
3. Indexe os filhos e expanda para pais antes da geração.
4. Teste prefixo determinístico e resumo contextual derivado.
5. Compare Recall, citações, tokens, latência e redundância.

## Entregáveis

- `src/chunking/parent_child.py`.
- Notebook comparativo.
- Visualização da árvore.
- ADR da estratégia.

Use o template [`relatorio-laboratorio.md`](../../../../recursos-compartilhados/templates/relatorio-laboratorio.md) para documentar hipótese, ambiente, resultados e conclusão.

## Critério de avaliação

A expansão deve preservar rastreabilidade até o chunk e a página originais.

## Regras de segurança e qualidade

- Não inclua chaves, tokens ou dados pessoais no Git.
- Registre versões e parâmetros relevantes.
- Diferencie evidência observada de hipótese.
- Inclua tratamento de erros e testes quando aplicável.
- Não declare melhoria sem comparação antes/depois.

## Estrutura da pasta

- `starter/`: arquivos iniciais sugeridos.
- `entrega/`: área local para a entrega do aluno; arquivos grandes devem permanecer fora do Git.
