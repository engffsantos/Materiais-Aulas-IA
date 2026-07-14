# Laboratório 14.02 — API, CI e defesa técnica do projeto final

> **Obrigatório — 3h30.**

## Objetivos

- Expor RAG com FastAPI.
- Automatizar testes e qualidade.
- Preparar documentação e defesa final.

## Ambiente recomendado

- Google Colab para notebooks e experimentos.
- GitHub Codespaces/VS Code Web para código estruturado.
- VS Code local é opcional.
- Credenciais somente em Secrets ou variáveis de ambiente.

## Roteiro

1. Implemente `/health`, `/ready`, `/query` e `/evaluate` restrito.
2. Inclua texto, fontes, suporte, trace_id e latência na resposta.
3. Valide tamanho, tenant, timeout, resultados e schema.
4. Crie testes unitários, integração e smoke test.
5. Configure GitHub Actions com Ruff, pytest e verificação de segredos.
6. Documente arquitetura, instalação, segurança, execução, avaliação e limitações.
7. Prepare apresentação de 10 a 15 minutos com baseline e evidências.

## Entregáveis

- API FastAPI.
- Testes e workflow CI.
- README completo.
- Relatório final.
- Apresentação reproduzível.

Use o template [`relatorio-laboratorio.md`](../../../../recursos-compartilhados/templates/relatorio-laboratorio.md) para documentar hipótese, ambiente, resultados e conclusão.

## Critério de avaliação

Técnica 25%; evidências 25%; segurança 20%; reprodução 15%; comunicação 15%.

## Regras de segurança e qualidade

- Não inclua chaves, tokens ou dados pessoais no Git.
- Registre versões e parâmetros relevantes.
- Diferencie evidência observada de hipótese.
- Inclua tratamento de erros e testes quando aplicável.
- Não declare melhoria sem comparação antes/depois.

## Estrutura da pasta

- `starter/`: arquivos iniciais sugeridos.
- `entrega/`: área local para a entrega do aluno; arquivos grandes devem permanecer fora do Git.
