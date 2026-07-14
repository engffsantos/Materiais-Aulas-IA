# Laboratório 2.02 — Construção do Golden Dataset de RAG

> **Obrigatório — 3h.**

## Objetivos

- Representar perguntas e evidências esperadas.
- Incluir casos difíceis e negativos.
- Versionar um conjunto de avaliação auditável.

## Ambiente recomendado

- Google Colab para notebooks e experimentos.
- GitHub Codespaces/VS Code Web para código estruturado.
- VS Code local é opcional.
- Credenciais somente em Secrets ou variáveis de ambiente.

## Roteiro

1. Crie ao menos 30 perguntas: factuais, termos exatos, temporais, comparativas, multi-hop, ambíguas e não respondíveis.
2. Para cada caso, registre pergunta, resposta, documentos relevantes, categoria, dificuldade, permissões e `answerable`.
3. Revise cada caso contra a fonte original.
4. Separe 20% como holdout.
5. Versione alterações com justificativa.

## Entregáveis

- `data/eval/golden_dataset.jsonl`.
- `data/eval/holdout.jsonl`.
- Guia de anotação.
- Relatório de distribuição.

Use o template [`relatorio-laboratorio.md`](../../../../recursos-compartilhados/templates/relatorio-laboratorio.md) para documentar hipótese, ambiente, resultados e conclusão.

## Critério de avaliação

Toda pergunta deve ser auditável até a fonte; casos não respondíveis são obrigatórios.

## Regras de segurança e qualidade

- Não inclua chaves, tokens ou dados pessoais no Git.
- Registre versões e parâmetros relevantes.
- Diferencie evidência observada de hipótese.
- Inclua tratamento de erros e testes quando aplicável.
- Não declare melhoria sem comparação antes/depois.

## Estrutura da pasta

- `starter/`: arquivos iniciais sugeridos.
- `entrega/`: área local para a entrega do aluno; arquivos grandes devem permanecer fora do Git.
