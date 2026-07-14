# Laboratório 8.02 — Abstenção, ambiguidade e conflito entre fontes

> **Obrigatório — 2h30.**

## Objetivos

- Definir política de abstenção.
- Tratar ambiguidade e versões.
- Evitar confiança falsa.

## Ambiente recomendado

- Google Colab para notebooks e experimentos.
- GitHub Codespaces/VS Code Web para código estruturado.
- VS Code local é opcional.
- Credenciais somente em Secrets ou variáveis de ambiente.

## Roteiro

1. Teste ausência, cobertura parcial, versões distintas, conflito, dado externo e ambiguidade.
2. Defina sinais de insuficiência, ACL, validade e conflito.
3. Implemente responder, responder parcialmente, pedir esclarecimento e abster-se.
4. Inclua documentos irrelevantes semanticamente próximos.
5. Meça abstenção correta, resposta indevida e recusa indevida.

## Entregáveis

- `src/generation/abstention.py`.
- Suíte com 15 casos.
- Matriz de decisão.
- Análise de erros.

Use o template [`relatorio-laboratorio.md`](../../../../recursos-compartilhados/templates/relatorio-laboratorio.md) para documentar hipótese, ambiente, resultados e conclusão.

## Critério de avaliação

O sistema não deve apresentar como fato uma conclusão sem evidência.

## Regras de segurança e qualidade

- Não inclua chaves, tokens ou dados pessoais no Git.
- Registre versões e parâmetros relevantes.
- Diferencie evidência observada de hipótese.
- Inclua tratamento de erros e testes quando aplicável.
- Não declare melhoria sem comparação antes/depois.

## Estrutura da pasta

- `starter/`: arquivos iniciais sugeridos.
- `entrega/`: área local para a entrega do aluno; arquivos grandes devem permanecer fora do Git.
