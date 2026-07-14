# Laboratório 0.01 — Preparação do ambiente e repositório reproduzível

> **Obrigatório — 1h30.**

## Objetivos

- Criar um repositório organizado para o curso.
- Validar Google Colab e GitHub Codespaces.
- Proteger credenciais e fixar versões.
- Registrar evidências de execução.

## Ambiente recomendado

- Google Colab para notebooks e experimentos.
- GitHub Codespaces/VS Code Web para código estruturado.
- VS Code local é opcional.
- Credenciais somente em Secrets ou variáveis de ambiente.

## Roteiro

1. Crie a estrutura de diretórios definida no curso e confirme que nenhum segredo será versionado.
2. No Colab, instale `openai`, `faiss-cpu`, `numpy`, `pandas` e `scikit-learn`.
3. Cadastre `OPENAI_API_KEY` nos Secrets do Colab e valide a leitura sem imprimir o valor.
4. Abra o repositório em Codespaces, configure Codespaces Secrets e execute um smoke test.
5. Registre Python, sistema, bibliotecas, data, commit e resultado dos testes.

## Entregáveis

- Notebook `00_environment_check.ipynb`.
- Arquivo de dependências.
- Smoke test executável.
- Checklist de segurança preenchido.

Use o template [`relatorio-laboratorio.md`](../../../../recursos-compartilhados/templates/relatorio-laboratorio.md) para documentar hipótese, ambiente, resultados e conclusão.

## Critério de avaliação

Organização 25%; segurança 25%; reprodução 30%; documentação 20%.

## Regras de segurança e qualidade

- Não inclua chaves, tokens ou dados pessoais no Git.
- Registre versões e parâmetros relevantes.
- Diferencie evidência observada de hipótese.
- Inclua tratamento de erros e testes quando aplicável.
- Não declare melhoria sem comparação antes/depois.

## Estrutura da pasta

- `starter/`: arquivos iniciais sugeridos.
- `entrega/`: área local para a entrega do aluno; arquivos grandes devem permanecer fora do Git.
