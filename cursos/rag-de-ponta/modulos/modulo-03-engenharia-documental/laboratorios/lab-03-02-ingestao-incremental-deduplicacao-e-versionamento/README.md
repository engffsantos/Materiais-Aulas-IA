# Laboratório 3.02 — Ingestão incremental, deduplicação e versionamento

> **Obrigatório — 3h30.**

## Objetivos

- Evitar reprocessamento desnecessário.
- Detectar mudanças e remoções.
- Manter trilha de auditoria.

## Ambiente recomendado

- Google Colab para notebooks e experimentos.
- GitHub Codespaces/VS Code Web para código estruturado.
- VS Code local é opcional.
- Credenciais somente em Secrets ou variáveis de ambiente.

## Roteiro

1. Execute carga inicial, repetição sem mudanças e carga com alterações/removidos.
2. Separe `document_id` lógico de `content_hash`.
3. Registre estado em JSON, Parquet ou SQLite embutido.
4. Classifique arquivos em novos, alterados, inalterados, duplicados, removidos e falhos.
5. Implemente tombstone ou exclusão e prove que conteúdo removido não é recuperado.
6. Crie teste de idempotência.

## Entregáveis

- `src/ingestion/incremental.py`.
- Catálogo de estado.
- Logs das três execuções.
- Teste de idempotência.
- ADR de remoção.

Use o template [`relatorio-laboratorio.md`](../../../../recursos-compartilhados/templates/relatorio-laboratorio.md) para documentar hipótese, ambiente, resultados e conclusão.

## Critério de avaliação

A segunda execução sem mudanças deve produzir zero duplicações e zero reindexações indevidas.

## Regras de segurança e qualidade

- Não inclua chaves, tokens ou dados pessoais no Git.
- Registre versões e parâmetros relevantes.
- Diferencie evidência observada de hipótese.
- Inclua tratamento de erros e testes quando aplicável.
- Não declare melhoria sem comparação antes/depois.

## Estrutura da pasta

- `starter/`: arquivos iniciais sugeridos.
- `entrega/`: área local para a entrega do aluno; arquivos grandes devem permanecer fora do Git.
