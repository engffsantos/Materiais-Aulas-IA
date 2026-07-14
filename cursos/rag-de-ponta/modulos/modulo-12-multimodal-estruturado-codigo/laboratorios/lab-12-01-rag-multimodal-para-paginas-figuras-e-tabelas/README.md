# Laboratório 12.01 — RAG multimodal para páginas, figuras e tabelas

> **Obrigatório — 2h30.**

## Objetivos

- Extrair elementos de layout.
- Criar representações pesquisáveis.
- Manter vínculo com o artefato original.

## Ambiente recomendado

- Google Colab para notebooks e experimentos.
- GitHub Codespaces/VS Code Web para código estruturado.
- VS Code local é opcional.
- Credenciais somente em Secrets ou variáveis de ambiente.

## Roteiro

1. Use PDF público com texto, figura e tabela.
2. Extraia elementos com Docling ou equivalente.
3. Preserve texto, tabela, figura, legenda, página e coordenadas quando disponíveis.
4. Marque descrições geradas como derivadas.
5. Indexe com `element_type`, página e documento.
6. Teste perguntas por tipo de elemento e combinação.

## Entregáveis

- `src/multimodal/document_pipeline.py`.
- JSON de elementos.
- Notebook.
- Relatório por elemento.

Use o template [`relatorio-laboratorio.md`](../../../../recursos-compartilhados/templates/relatorio-laboratorio.md) para documentar hipótese, ambiente, resultados e conclusão.

## Critério de avaliação

Toda descrição derivada deve permanecer ligada ao elemento original.

## Regras de segurança e qualidade

- Não inclua chaves, tokens ou dados pessoais no Git.
- Registre versões e parâmetros relevantes.
- Diferencie evidência observada de hipótese.
- Inclua tratamento de erros e testes quando aplicável.
- Não declare melhoria sem comparação antes/depois.

## Estrutura da pasta

- `starter/`: arquivos iniciais sugeridos.
- `entrega/`: área local para a entrega do aluno; arquivos grandes devem permanecer fora do Git.
