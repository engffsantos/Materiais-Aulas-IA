# Laboratório 1.02 — Architecture Canvas do projeto final

> **Obrigatório — 3h.**

## Objetivos

- Converter o problema em componentes técnicos.
- Definir fronteiras, fluxo, armazenamento e controles.
- Planejar uma arquitetura incremental.

## Ambiente recomendado

- Google Colab para notebooks e experimentos.
- GitHub Codespaces/VS Code Web para código estruturado.
- VS Code local é opcional.
- Credenciais somente em Secrets ou variáveis de ambiente.

## Roteiro

1. Defina problema, público, fontes permitidas, perguntas dentro e fora do escopo.
2. Separe requisitos funcionais e não funcionais.
3. Desenhe fonte → ingestão → índice → recuperação → geração → resposta.
4. Adicione autenticação, ACL, avaliação, logs, custo e latência.
5. Escolha provisoriamente ambiente, armazenamento, chunking, embedding, busca, interface e API.
6. Registre ao menos dez riscos e um plano evolutivo em quatro versões.

## Entregáveis

- `docs/architecture_canvas.md`.
- Diagrama Mermaid.
- ADR inicial.
- Lista de hipóteses testáveis.

Use o template [`relatorio-laboratorio.md`](../../../../recursos-compartilhados/templates/relatorio-laboratorio.md) para documentar hipótese, ambiente, resultados e conclusão.

## Critério de avaliação

Clareza 25%; requisitos 30%; riscos 25%; simplicidade e evolução 20%.

## Regras de segurança e qualidade

- Não inclua chaves, tokens ou dados pessoais no Git.
- Registre versões e parâmetros relevantes.
- Diferencie evidência observada de hipótese.
- Inclua tratamento de erros e testes quando aplicável.
- Não declare melhoria sem comparação antes/depois.

## Estrutura da pasta

- `starter/`: arquivos iniciais sugeridos.
- `entrega/`: área local para a entrega do aluno; arquivos grandes devem permanecer fora do Git.
