# Laboratório 11.01 — Mini-RAPTOR com recuperação hierárquica

> **Obrigatório — 2h30.**

## Objetivos

- Agrupar chunks.
- Gerar resumos com proveniência.
- Indexar múltiplos níveis.

## Ambiente recomendado

- Google Colab para notebooks e experimentos.
- GitHub Codespaces/VS Code Web para código estruturado.
- VS Code local é opcional.
- Credenciais somente em Secrets ou variáveis de ambiente.

## Roteiro

1. Gere embeddings e agrupe chunks com KMeans.
2. Analise grupos e registre membros.
3. Gere resumo por grupo somente com os chunks membros.
4. Indexe chunks e resumos com campo `level`.
5. Compare busca plana e hierárquica em detalhe e síntese.

## Entregáveis

- `src/hierarchical/mini_raptor.py`.
- Mapa dos grupos.
- Notebook comparativo.
- Análise de riscos.

Use o template [`relatorio-laboratorio.md`](../../../../recursos-compartilhados/templates/relatorio-laboratorio.md) para documentar hipótese, ambiente, resultados e conclusão.

## Critério de avaliação

Todo resumo deve apontar para os chunks e documentos originais.

## Regras de segurança e qualidade

- Não inclua chaves, tokens ou dados pessoais no Git.
- Registre versões e parâmetros relevantes.
- Diferencie evidência observada de hipótese.
- Inclua tratamento de erros e testes quando aplicável.
- Não declare melhoria sem comparação antes/depois.

## Estrutura da pasta

- `starter/`: arquivos iniciais sugeridos.
- `entrega/`: área local para a entrega do aluno; arquivos grandes devem permanecer fora do Git.
