# RAG de Ponta — Engenharia de Recuperação, Agentic RAG e GraphRAG

Curso avançado de 96 horas, organizado em 15 módulos e 30 laboratórios obrigatórios.

## Ambientes

- Google Colab para experimentos e notebooks.
- GitHub Codespaces/VS Code Web para projetos estruturados.
- VS Code local como alternativa opcional.
- FAISS/Chroma efêmero, OpenAI Vector Stores e Qdrant Cloud, sem exigir banco instalado nas máquinas.

## Navegação

Consulte [`modulos/README.md`](./modulos/README.md) para o índice completo.

## Convenção de cada laboratório

```text
lab-XX-YY-nome/
├── README.md       # roteiro completo
├── starter/        # arquivos iniciais sugeridos
└── entrega/        # artefatos do aluno; não contém solução oficial
```

## Execução inicial

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requisitos/dev.txt
python scripts/validar_estrutura.py
```

## Segurança

Copie `.env.example` para `.env` apenas no seu ambiente. O arquivo real está ignorado pelo Git.
