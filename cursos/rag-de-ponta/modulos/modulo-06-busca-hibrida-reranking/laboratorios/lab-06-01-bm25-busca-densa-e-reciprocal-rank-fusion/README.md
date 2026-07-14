# Laboratório 6.01 — BM25, busca densa e Reciprocal Rank Fusion

> **Obrigatório — 3h30.**

## Objetivos

- Implementar BM25.
- Comparar sinais lexicais e semânticos.
- Fundir rankings sem misturar escalas incompatíveis.

## Ambiente recomendado

- Google Colab para notebooks e experimentos.
- GitHub Codespaces/VS Code Web para código estruturado.
- VS Code local é opcional.
- Credenciais somente em Secrets ou variáveis de ambiente.

## Roteiro

1. Construa índice BM25 com tokenização documentada.
2. Reutilize FAISS com os mesmos chunks e IDs.
3. Implemente RRF e preserve a origem de cada sinal.
4. Compare lexical, denso e híbrido por categoria.
5. Aplique filtros de tenant, idioma, versão e status antes da geração.

## Entregáveis

- `src/retrieval/bm25.py`.
- `src/retrieval/hybrid.py`.
- Testes de RRF.
- Tabela por categoria.
- Recomendação.

Use o template [`relatorio-laboratorio.md`](../../../../recursos-compartilhados/templates/relatorio-laboratorio.md) para documentar hipótese, ambiente, resultados e conclusão.

## Critério de avaliação

O híbrido deve ser medido, não presumido superior.

## Regras de segurança e qualidade

- Não inclua chaves, tokens ou dados pessoais no Git.
- Registre versões e parâmetros relevantes.
- Diferencie evidência observada de hipótese.
- Inclua tratamento de erros e testes quando aplicável.
- Não declare melhoria sem comparação antes/depois.

## Estrutura da pasta

- `starter/`: arquivos iniciais sugeridos.
- `entrega/`: área local para a entrega do aluno; arquivos grandes devem permanecer fora do Git.
