from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class DocumentChunk:
    chunk_id: str
    document_id: str
    text: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class RetrievedChunk:
    chunk: DocumentChunk
    score: float
    rank: int
    retriever: str
