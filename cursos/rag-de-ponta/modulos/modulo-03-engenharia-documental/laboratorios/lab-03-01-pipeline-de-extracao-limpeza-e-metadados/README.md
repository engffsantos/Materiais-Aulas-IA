# Laboratório 3.01 — Pipeline de extração, limpeza e metadados

> **Obrigatório — 3h30.**

## Objetivos

- Extrair conteúdo preservando estrutura.
- Comparar extração simples e orientada a layout.
- Criar metadados consistentes.

## Ambiente recomendado

- Google Colab para notebooks e experimentos.
- GitHub Codespaces/VS Code Web para código estruturado.
- VS Code local é opcional.
- Credenciais somente em Secrets ou variáveis de ambiente.

## Roteiro

1. Use PDF, DOCX, HTML/Markdown e documento com tabela.
2. Crie inventário com MIME, tamanho, origem, licença e SHA-256.
3. Compare extração simples com Docling em documento complexo.
4. Normalize espaços e ruído sem apagar números, unidades, datas ou negações.
5. Inclua ID, título, versão, seção, página, idioma, tenant, ACL e hash.
6. Valide documento vazio, tabela perdida, duplicação e texto curto demais.

## Entregáveis

- `src/ingestion/loaders.py`.
- `src/ingestion/normalization.py`.
- Manifesto JSON.
- Relatório comparativo.
- Testes das regras.

Use o template [`relatorio-laboratorio.md`](../../../../recursos-compartilhados/templates/relatorio-laboratorio.md) para documentar hipótese, ambiente, resultados e conclusão.

## Critério de avaliação

Fidelidade 35%; metadados 25%; validação 20%; documentação 20%.

## Regras de segurança e qualidade

- Não inclua chaves, tokens ou dados pessoais no Git.
- Registre versões e parâmetros relevantes.
- Diferencie evidência observada de hipótese.
- Inclua tratamento de erros e testes quando aplicável.
- Não declare melhoria sem comparação antes/depois.

## Estrutura da pasta

- `starter/`: arquivos iniciais sugeridos.
- `entrega/`: área local para a entrega do aluno; arquivos grandes devem permanecer fora do Git.
