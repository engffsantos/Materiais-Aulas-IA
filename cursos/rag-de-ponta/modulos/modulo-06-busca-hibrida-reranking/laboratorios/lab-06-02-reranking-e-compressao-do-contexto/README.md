# Laboratório 6.02 — Reranking e compressão do contexto

> **Obrigatório — 3h30.**

## Objetivos

- Aplicar cross-encoder ou serviço de reranking.
- Separar candidatos e contexto final.
- Medir qualidade versus latência.

## Ambiente recomendado

- Google Colab para notebooks e experimentos.
- GitHub Codespaces/VS Code Web para código estruturado.
- VS Code local é opcional.
- Credenciais somente em Secrets ou variáveis de ambiente.

## Roteiro

1. Execute baseline híbrido sem reranking.
2. Recupere 20 a 50 candidatos e registre scores originais.
3. Aplique reranker multilíngue e preserve metadados.
4. Deduplicate chunks e limite redundância por pai.
5. Compare candidate_k, top_k, Recall, MRR, nDCG, p95 e tokens.
6. Implemente timeout e fallback para o ranking híbrido.

## Entregáveis

- `src/reranking/cross_encoder.py`.
- Notebook comparativo.
- Testes de fallback.
- Relatório custo/qualidade/latência.

Use o template [`relatorio-laboratorio.md`](../../../../recursos-compartilhados/templates/relatorio-laboratorio.md) para documentar hipótese, ambiente, resultados e conclusão.

## Critério de avaliação

Qualidade 30%; falhas 25%; benchmark 30%; documentação 15%.

## Regras de segurança e qualidade

- Não inclua chaves, tokens ou dados pessoais no Git.
- Registre versões e parâmetros relevantes.
- Diferencie evidência observada de hipótese.
- Inclua tratamento de erros e testes quando aplicável.
- Não declare melhoria sem comparação antes/depois.

## Estrutura da pasta

- `starter/`: arquivos iniciais sugeridos.
- `entrega/`: área local para a entrega do aluno; arquivos grandes devem permanecer fora do Git.
