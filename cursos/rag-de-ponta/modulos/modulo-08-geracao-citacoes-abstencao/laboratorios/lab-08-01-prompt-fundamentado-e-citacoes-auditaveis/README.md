# Laboratório 8.01 — Prompt fundamentado e citações auditáveis

> **Obrigatório — 2h30.**

## Objetivos

- Separar instruções e conteúdo.
- Criar contexto rastreável.
- Validar afirmações e fontes.

## Ambiente recomendado

- Google Colab para notebooks e experimentos.
- GitHub Codespaces/VS Code Web para código estruturado.
- VS Code local é opcional.
- Credenciais somente em Secrets ou variáveis de ambiente.

## Roteiro

1. Inclua ID, documento, título, página/seção e texto em cada fonte.
2. Defina saída com resposta, afirmações, fontes e status de suporte.
3. Imponha orçamento de contexto.
4. Rejeite IDs citados que não existam no contexto.
5. Teste dez perguntas e um caso de evidência no final do contexto.

## Entregáveis

- `src/generation/grounded_answer.py`.
- Schema da resposta.
- Testes de citação.
- Relatório de precisão.

Use o template [`relatorio-laboratorio.md`](../../../../recursos-compartilhados/templates/relatorio-laboratorio.md) para documentar hipótese, ambiente, resultados e conclusão.

## Critério de avaliação

Rastreabilidade 35%; validação 30%; qualidade 20%; documentação 15%.

## Regras de segurança e qualidade

- Não inclua chaves, tokens ou dados pessoais no Git.
- Registre versões e parâmetros relevantes.
- Diferencie evidência observada de hipótese.
- Inclua tratamento de erros e testes quando aplicável.
- Não declare melhoria sem comparação antes/depois.

## Estrutura da pasta

- `starter/`: arquivos iniciais sugeridos.
- `entrega/`: área local para a entrega do aluno; arquivos grandes devem permanecer fora do Git.
