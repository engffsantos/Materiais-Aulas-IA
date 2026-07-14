# Laboratório 14.01 — Red team de RAG: prompt injection, poisoning e isolamento

> **Obrigatório — 2h30.**

## Objetivos

- Reconhecer prompt injection indireta.
- Validar isolamento entre tenants.
- Detectar poisoning e fontes obsoletas.

## Ambiente recomendado

- Google Colab para notebooks e experimentos.
- GitHub Codespaces/VS Code Web para código estruturado.
- VS Code local é opcional.
- Credenciais somente em Secrets ou variáveis de ambiente.

## Roteiro

1. Use apenas corpus fictício e ambiente de teste.
2. Teste instrução maliciosa em documento, tentativa de revelar ambiente, fonte falsa, versão antiga, cruzamento de tenant, upload inválido e esgotamento de orçamento.
3. Aplique separação entre instrução e dados, ACL pré-recuperação, allowlists, validação de versão e limites.
4. Automatize cada cenário e registre severidade, resultado e correção.

## Entregáveis

- `tests/security/test_rag_attacks.py`.
- Catálogo de ameaças.
- Relatório red team.
- Plano de correções.
- Checklist de isolamento.

Use o template [`relatorio-laboratorio.md`](../../../../recursos-compartilhados/templates/relatorio-laboratorio.md) para documentar hipótese, ambiente, resultados e conclusão.

## Critério de avaliação

Nenhuma resposta pode revelar segredo, cruzar tenants ou obedecer instrução documental.

## Regras de segurança e qualidade

- Não inclua chaves, tokens ou dados pessoais no Git.
- Registre versões e parâmetros relevantes.
- Diferencie evidência observada de hipótese.
- Inclua tratamento de erros e testes quando aplicável.
- Não declare melhoria sem comparação antes/depois.

## Estrutura da pasta

- `starter/`: arquivos iniciais sugeridos.
- `entrega/`: área local para a entrega do aluno; arquivos grandes devem permanecer fora do Git.
