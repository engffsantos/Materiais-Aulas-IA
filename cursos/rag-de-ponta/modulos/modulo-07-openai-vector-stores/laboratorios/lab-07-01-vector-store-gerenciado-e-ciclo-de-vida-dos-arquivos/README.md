# Laboratório 7.01 — Vector Store gerenciado e ciclo de vida dos arquivos

> **Obrigatório — 2h30.**

## Objetivos

- Criar e administrar um vector store.
- Acompanhar processamento.
- Executar limpeza e governança.

## Ambiente recomendado

- Google Colab para notebooks e experimentos.
- GitHub Codespaces/VS Code Web para código estruturado.
- VS Code local é opcional.
- Credenciais somente em Secrets ou variáveis de ambiente.

## Roteiro

1. Prepare subconjunto público do corpus e um manifesto.
2. Crie store com nome de turma e ambiente.
3. Mantenha IDs fora do Git e configure expiração quando disponível.
4. Envie, associe e acompanhe estados de processamento.
5. Execute cinco consultas e registre citações, latência e arquivos.
6. Documente remoção de arquivo e exclusão do store.

## Entregáveis

- `notebooks/07_managed_vector_store.ipynb`.
- Scripts de criação e limpeza.
- Manifesto.
- Checklist de governança.

Use o template [`relatorio-laboratorio.md`](../../../../recursos-compartilhados/templates/relatorio-laboratorio.md) para documentar hipótese, ambiente, resultados e conclusão.

## Critério de avaliação

Demonstrar criação, consulta e limpeza sem expor credenciais.

## Regras de segurança e qualidade

- Não inclua chaves, tokens ou dados pessoais no Git.
- Registre versões e parâmetros relevantes.
- Diferencie evidência observada de hipótese.
- Inclua tratamento de erros e testes quando aplicável.
- Não declare melhoria sem comparação antes/depois.

## Estrutura da pasta

- `starter/`: arquivos iniciais sugeridos.
- `entrega/`: área local para a entrega do aluno; arquivos grandes devem permanecer fora do Git.
