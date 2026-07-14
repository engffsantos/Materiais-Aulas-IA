# Laboratório 1.01 — Matriz de decisão: RAG ou outra estratégia?

> **Obrigatório — 2h.**

## Objetivos

- Diferenciar RAG, contexto longo, fine-tuning, busca e ferramentas.
- Justificar decisões por requisitos.
- Identificar riscos de complexidade desnecessária.

## Ambiente recomendado

- Google Colab para notebooks e experimentos.
- GitHub Codespaces/VS Code Web para código estruturado.
- VS Code local é opcional.
- Credenciais somente em Secrets ou variáveis de ambiente.

## Roteiro

1. Analise: manual técnico atualizado; classificação de e-mails; consulta de saldo; assistente jurídico; FAQ pequena e estável.
2. Liste usuários, fontes, atualização, criticidade, citação, autorização, cálculo e ações.
3. Atribua notas para qualidade, custo, latência, governança e complexidade.
4. Selecione estratégia principal, fallback e condições que mudariam a decisão.

## Entregáveis

- `docs/architecture_decision_matrix.md`.
- Decisões dos cinco cenários.
- Riscos e hipóteses.

Use o template [`relatorio-laboratorio.md`](../../../../recursos-compartilhados/templates/relatorio-laboratorio.md) para documentar hipótese, ambiente, resultados e conclusão.

## Critério de avaliação

A justificativa baseada em requisitos vale mais do que a tecnologia escolhida.

## Regras de segurança e qualidade

- Não inclua chaves, tokens ou dados pessoais no Git.
- Registre versões e parâmetros relevantes.
- Diferencie evidência observada de hipótese.
- Inclua tratamento de erros e testes quando aplicável.
- Não declare melhoria sem comparação antes/depois.

## Estrutura da pasta

- `starter/`: arquivos iniciais sugeridos.
- `entrega/`: área local para a entrega do aluno; arquivos grandes devem permanecer fora do Git.
