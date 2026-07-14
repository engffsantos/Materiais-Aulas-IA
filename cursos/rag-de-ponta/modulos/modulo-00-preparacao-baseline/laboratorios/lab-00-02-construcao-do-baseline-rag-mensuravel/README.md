# Laboratório 0.02 — Construção do baseline RAG mensurável

> **Obrigatório — 2h30.**

## Objetivos

- Percorrer ingestão, chunking, embeddings, busca e geração.
- Criar uma versão de referência comparável.
- Registrar resultados, fontes, custo e latência.

## Ambiente recomendado

- Google Colab para notebooks e experimentos.
- GitHub Codespaces/VS Code Web para código estruturado.
- VS Code local é opcional.
- Credenciais somente em Secrets ou variáveis de ambiente.

## Roteiro

1. Selecione de 5 a 10 arquivos Markdown ou TXT públicos ou criados para a aula.
2. Crie manifesto com `document_id`, título, origem e data.
3. Divida documentos por parágrafos e preserve metadados.
4. Gere embeddings e crie índice FAISS.
5. Implemente `retrieve(query, top_k=5)` retornando texto, metadados e score.
6. Monte contexto numerado e gere resposta citando `[F1]`, `[F2]` etc.
7. Crie dez perguntas: sete respondíveis, duas não respondíveis e uma ambígua.
8. Registre acertos, erros, latência e diagnóstico de recuperação ou geração.

## Entregáveis

- Notebook `01_baseline_rag.ipynb`.
- `data/eval/baseline_questions.json`.
- Tabela de resultados.
- Tag Git `baseline-v1`.

Use o template [`relatorio-laboratorio.md`](../../../../recursos-compartilhados/templates/relatorio-laboratorio.md) para documentar hipótese, ambiente, resultados e conclusão.

## Critério de avaliação

O baseline deve executar do início ao fim e permitir repetição com os mesmos parâmetros.

## Regras de segurança e qualidade

- Não inclua chaves, tokens ou dados pessoais no Git.
- Registre versões e parâmetros relevantes.
- Diferencie evidência observada de hipótese.
- Inclua tratamento de erros e testes quando aplicável.
- Não declare melhoria sem comparação antes/depois.

## Estrutura da pasta

- `starter/`: arquivos iniciais sugeridos.
- `entrega/`: área local para a entrega do aluno; arquivos grandes devem permanecer fora do Git.
