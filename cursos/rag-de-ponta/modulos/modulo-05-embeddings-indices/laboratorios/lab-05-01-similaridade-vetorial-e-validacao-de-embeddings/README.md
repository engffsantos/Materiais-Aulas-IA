# Laboratório 5.01 — Similaridade vetorial e validação de embeddings

> **Obrigatório — 2h30.**

## Objetivos

- Calcular similaridade manualmente.
- Comparar comportamento por idioma e domínio.
- Reconhecer falsos positivos semânticos.

## Ambiente recomendado

- Google Colab para notebooks e experimentos.
- GitHub Codespaces/VS Code Web para código estruturado.
- VS Code local é opcional.
- Credenciais somente em Secrets ou variáveis de ambiente.

## Roteiro

1. Implemente cosseno, produto interno e distância euclidiana com NumPy.
2. Compare vetores normalizados e não normalizados.
3. Crie 30 frases com equivalências, negações, números, siglas e termos técnicos.
4. Gere matriz de similaridade e vizinhos mais próximos.
5. Use PCA apenas para visualização.
6. Compare duas configurações de embeddings no golden dataset.

## Entregáveis

- `notebooks/04_embeddings_validation.ipynb`.
- `src/embeddings/similarity.py`.
- Testes.
- Relatório de limitações.

Use o template [`relatorio-laboratorio.md`](../../../../recursos-compartilhados/templates/relatorio-laboratorio.md) para documentar hipótese, ambiente, resultados e conclusão.

## Critério de avaliação

Correção matemática 30%; experimento 30%; erros 30%; documentação 10%.

## Regras de segurança e qualidade

- Não inclua chaves, tokens ou dados pessoais no Git.
- Registre versões e parâmetros relevantes.
- Diferencie evidência observada de hipótese.
- Inclua tratamento de erros e testes quando aplicável.
- Não declare melhoria sem comparação antes/depois.

## Estrutura da pasta

- `starter/`: arquivos iniciais sugeridos.
- `entrega/`: área local para a entrega do aluno; arquivos grandes devem permanecer fora do Git.
