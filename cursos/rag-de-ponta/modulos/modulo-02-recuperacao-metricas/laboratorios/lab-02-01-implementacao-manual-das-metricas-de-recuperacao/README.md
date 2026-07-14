# Laboratório 2.01 — Implementação manual das métricas de recuperação

> **Obrigatório — 2h30.**

## Objetivos

- Compreender as métricas matematicamente.
- Validar resultados com exemplos conhecidos.
- Evitar uso mecânico de frameworks.

## Ambiente recomendado

- Google Colab para notebooks e experimentos.
- GitHub Codespaces/VS Code Web para código estruturado.
- VS Code local é opcional.
- Credenciais somente em Secrets ou variáveis de ambiente.

## Roteiro

1. Crie cinco consultas com documentos relevantes e ranking de dez itens.
2. Implemente `precision_at_k`, `recall_at_k`, `hit_rate_at_k`, `reciprocal_rank`, `dcg_at_k` e `ndcg_at_k`.
3. Calcule manualmente um exemplo e transforme-o em teste unitário.
4. Compare k=1, 3, 5 e 10.
5. Explique casos de recall alto com precision baixa.

## Entregáveis

- `src/evaluation/retrieval_metrics.py`.
- `tests/test_retrieval_metrics.py`.
- Notebook de exemplos.
- Relatório interpretativo.

Use o template [`relatorio-laboratorio.md`](../../../../recursos-compartilhados/templates/relatorio-laboratorio.md) para documentar hipótese, ambiente, resultados e conclusão.

## Critério de avaliação

Correção 40%; testes 25%; interpretação 25%; organização 10%.

## Regras de segurança e qualidade

- Não inclua chaves, tokens ou dados pessoais no Git.
- Registre versões e parâmetros relevantes.
- Diferencie evidência observada de hipótese.
- Inclua tratamento de erros e testes quando aplicável.
- Não declare melhoria sem comparação antes/depois.

## Estrutura da pasta

- `starter/`: arquivos iniciais sugeridos.
- `entrega/`: área local para a entrega do aluno; arquivos grandes devem permanecer fora do Git.
