# Laboratório 4.01 — Benchmark de estratégias de chunking

> **Obrigatório — 3h30.**

## Objetivos

- Medir o efeito do chunking na recuperação.
- Identificar fragmentação e redundância.
- Recomendar estratégia por tipo documental.

## Ambiente recomendado

- Google Colab para notebooks e experimentos.
- GitHub Codespaces/VS Code Web para código estruturado.
- VS Code local é opcional.
- Credenciais somente em Secrets ou variáveis de ambiente.

## Roteiro

1. Compare chunking fixo, recursivo, estrutural e semântico.
2. Mantenha corpus, embedding, índice, top_k e perguntas fixos.
3. Meça quantidade e tamanho dos chunks, overlap, Recall@k, MRR e nDCG.
4. Registre ingestão, tamanho do índice, tokens recuperados e latência.
5. Teste dois tamanhos e dois overlaps e analise cinco falhas.

## Entregáveis

- `notebooks/03_chunking_benchmark.ipynb`.
- `src/chunking/strategies.py`.
- CSV por consulta.
- Gráficos.
- Recomendação final.

Use o template [`relatorio-laboratorio.md`](../../../../recursos-compartilhados/templates/relatorio-laboratorio.md) para documentar hipótese, ambiente, resultados e conclusão.

## Critério de avaliação

Controle experimental 30%; implementação 25%; análise 30%; clareza 15%.

## Regras de segurança e qualidade

- Não inclua chaves, tokens ou dados pessoais no Git.
- Registre versões e parâmetros relevantes.
- Diferencie evidência observada de hipótese.
- Inclua tratamento de erros e testes quando aplicável.
- Não declare melhoria sem comparação antes/depois.

## Estrutura da pasta

- `starter/`: arquivos iniciais sugeridos.
- `entrega/`: área local para a entrega do aluno; arquivos grandes devem permanecer fora do Git.
