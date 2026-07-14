# Laboratório 9.01 — Query rewriting, multi-query e HyDE

> **Obrigatório — 3h30.**

## Objetivos

- Tornar consultas conversacionais autônomas.
- Expandir busca sem alterar intenção.
- Avaliar HyDE de forma controlada.

## Ambiente recomendado

- Google Colab para notebooks e experimentos.
- GitHub Codespaces/VS Code Web para código estruturado.
- VS Code local é opcional.
- Credenciais somente em Secrets ou variáveis de ambiente.

## Roteiro

1. Reescreva consultas dependentes de histórico preservando entidades e datas.
2. Gere 3 a 5 variações, recupere e faça união/RRF.
3. Implemente HyDE, marcando o texto hipotético como não-evidência.
4. Crie roteador para consulta direta, rewriting, multi-query ou HyDE.
5. Compare Recall, MRR, latência e número de buscas.

## Entregáveis

- `src/retrieval/query_transform.py`.
- Notebook comparativo.
- Testes de entidades.
- Tabela de decisão.

Use o template [`relatorio-laboratorio.md`](../../../../recursos-compartilhados/templates/relatorio-laboratorio.md) para documentar hipótese, ambiente, resultados e conclusão.

## Critério de avaliação

A transformação não pode inventar restrições nem mudar a intenção.

## Regras de segurança e qualidade

- Não inclua chaves, tokens ou dados pessoais no Git.
- Registre versões e parâmetros relevantes.
- Diferencie evidência observada de hipótese.
- Inclua tratamento de erros e testes quando aplicável.
- Não declare melhoria sem comparação antes/depois.

## Estrutura da pasta

- `starter/`: arquivos iniciais sugeridos.
- `entrega/`: área local para a entrega do aluno; arquivos grandes devem permanecer fora do Git.
