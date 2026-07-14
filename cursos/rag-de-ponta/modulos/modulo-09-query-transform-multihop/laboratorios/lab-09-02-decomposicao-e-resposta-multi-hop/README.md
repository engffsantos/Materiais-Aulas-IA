# Laboratório 9.02 — Decomposição e resposta multi-hop

> **Obrigatório — 3h30.**

## Objetivos

- Detectar perguntas compostas.
- Recuperar evidências por etapa.
- Compor resposta com proveniência.

## Ambiente recomendado

- Google Colab para notebooks e experimentos.
- GitHub Codespaces/VS Code Web para código estruturado.
- VS Code local é opcional.
- Credenciais somente em Secrets ou variáveis de ambiente.

## Roteiro

1. Crie plano de subperguntas e dependências com limite de etapas.
2. Recupere, valide e registre resultado intermediário por subpergunta.
3. Diferencie fatos, inferências e cálculos.
4. Interrompa quando uma premissa crítica estiver ausente.
5. Compare consulta única e multi-hop.

## Entregáveis

- `src/retrieval/multihop.py`.
- Diagrama.
- Cinco casos completos.
- Análise de erros.

Use o template [`relatorio-laboratorio.md`](../../../../recursos-compartilhados/templates/relatorio-laboratorio.md) para documentar hipótese, ambiente, resultados e conclusão.

## Critério de avaliação

A trilha deve permitir reconstruir evidências de cada conclusão.

## Regras de segurança e qualidade

- Não inclua chaves, tokens ou dados pessoais no Git.
- Registre versões e parâmetros relevantes.
- Diferencie evidência observada de hipótese.
- Inclua tratamento de erros e testes quando aplicável.
- Não declare melhoria sem comparação antes/depois.

## Estrutura da pasta

- `starter/`: arquivos iniciais sugeridos.
- `entrega/`: área local para a entrega do aluno; arquivos grandes devem permanecer fora do Git.
