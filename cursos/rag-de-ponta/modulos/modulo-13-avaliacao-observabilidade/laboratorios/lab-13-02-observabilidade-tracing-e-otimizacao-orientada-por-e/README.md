# Laboratório 13.02 — Observabilidade, tracing e otimização orientada por evidências

> **Obrigatório — 3h30.**

## Objetivos

- Registrar traces sem vazamento.
- Decompor latência e custo.
- Promover somente mudanças comprovadas.

## Ambiente recomendado

- Google Colab para notebooks e experimentos.
- GitHub Codespaces/VS Code Web para código estruturado.
- VS Code local é opcional.
- Credenciais somente em Secrets ou variáveis de ambiente.

## Roteiro

1. Registre trace_id, versão, tipo, consulta transformada, IDs, scores, tokens, tempo, cache e status.
2. Aplique mascaramento ou hashing para dados sensíveis.
3. Calcule média, mediana e p95 por etapa.
4. Escolha uma única variável para otimização.
5. Defina ganho mínimo e regressão máxima antes do experimento.
6. Classifique a decisão como PROMOVER, REJEITAR ou INCONCLUSIVO.

## Entregáveis

- `src/observability/tracing.py`.
- Dashboard ou relatório.
- Antes/depois.
- ADR.
- Teste de segredos nos logs.

Use o template [`relatorio-laboratorio.md`](../../../../recursos-compartilhados/templates/relatorio-laboratorio.md) para documentar hipótese, ambiente, resultados e conclusão.

## Critério de avaliação

Otimização sem baseline e hipótese explícita não será aceita.

## Regras de segurança e qualidade

- Não inclua chaves, tokens ou dados pessoais no Git.
- Registre versões e parâmetros relevantes.
- Diferencie evidência observada de hipótese.
- Inclua tratamento de erros e testes quando aplicável.
- Não declare melhoria sem comparação antes/depois.

## Estrutura da pasta

- `starter/`: arquivos iniciais sugeridos.
- `entrega/`: área local para a entrega do aluno; arquivos grandes devem permanecer fora do Git.
