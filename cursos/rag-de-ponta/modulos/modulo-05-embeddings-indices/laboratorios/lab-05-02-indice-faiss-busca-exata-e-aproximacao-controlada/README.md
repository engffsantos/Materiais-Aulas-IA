# Laboratório 5.02 — Índice FAISS: busca exata e aproximação controlada

> **Obrigatório — 2h30.**

## Objetivos

- Relacionar métrica, normalização e índice.
- Medir latência, memória e recall.
- Persistir índice e metadados.

## Ambiente recomendado

- Google Colab para notebooks e experimentos.
- GitHub Codespaces/VS Code Web para código estruturado.
- VS Code local é opcional.
- Credenciais somente em Secrets ou variáveis de ambiente.

## Roteiro

1. Crie índice exato e valide contra cálculo NumPy.
2. Experimente HNSW ou IVF quando o volume permitir.
3. Meça construção, média/p95, disco, memória e Recall@k.
4. Salve índice, mapeamento, configuração, versão do embedding e checksum.
5. Reabra em nova sessão e confirme os mesmos resultados.

## Entregáveis

- `src/embeddings/faiss_store.py`.
- Script de benchmark.
- Arquivos de índice fora do Git quando grandes.
- Relatório de decisão.

Use o template [`relatorio-laboratorio.md`](../../../../recursos-compartilhados/templates/relatorio-laboratorio.md) para documentar hipótese, ambiente, resultados e conclusão.

## Critério de avaliação

O índice reaberto deve manter associação correta entre vetor, chunk e metadados.

## Regras de segurança e qualidade

- Não inclua chaves, tokens ou dados pessoais no Git.
- Registre versões e parâmetros relevantes.
- Diferencie evidência observada de hipótese.
- Inclua tratamento de erros e testes quando aplicável.
- Não declare melhoria sem comparação antes/depois.

## Estrutura da pasta

- `starter/`: arquivos iniciais sugeridos.
- `entrega/`: área local para a entrega do aluno; arquivos grandes devem permanecer fora do Git.
