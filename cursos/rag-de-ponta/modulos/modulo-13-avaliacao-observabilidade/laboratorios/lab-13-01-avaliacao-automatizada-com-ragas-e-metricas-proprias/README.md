# Laboratório 13.01 — Avaliação automatizada com Ragas e métricas próprias

> **Obrigatório — 3h30.**

## Objetivos

- Integrar golden dataset ao pipeline.
- Aplicar métricas determinísticas e LLM-as-judge.
- Criar gate de regressão.

## Ambiente recomendado

- Google Colab para notebooks e experimentos.
- GitHub Codespaces/VS Code Web para código estruturado.
- VS Code local é opcional.
- Credenciais somente em Secrets ou variáveis de ambiente.

## Roteiro

1. Converta o dataset preservando pergunta, resposta, contexto e fontes.
2. Calcule Recall, MRR, nDCG, abstenção, citações, latência e custo.
3. Execute métricas Ragas compatíveis com a versão instalada.
4. Registre modelo avaliador, prompt, versão e parâmetros.
5. Compare ao menos 20 casos com avaliação humana.
6. Defina limites e faça o pipeline falhar em regressão.

## Entregáveis

- `src/evaluation/evaluate_pipeline.py`.
- Configuração.
- Relatório.
- Testes do gate.
- Análise humano versus judge.

Use o template [`relatorio-laboratorio.md`](../../../../recursos-compartilhados/templates/relatorio-laboratorio.md) para documentar hipótese, ambiente, resultados e conclusão.

## Critério de avaliação

Reprodução 25%; cobertura 25%; análise 30%; gate 20%.

## Regras de segurança e qualidade

- Não inclua chaves, tokens ou dados pessoais no Git.
- Registre versões e parâmetros relevantes.
- Diferencie evidência observada de hipótese.
- Inclua tratamento de erros e testes quando aplicável.
- Não declare melhoria sem comparação antes/depois.

## Estrutura da pasta

- `starter/`: arquivos iniciais sugeridos.
- `entrega/`: área local para a entrega do aluno; arquivos grandes devem permanecer fora do Git.
