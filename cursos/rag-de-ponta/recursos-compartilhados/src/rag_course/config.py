from dataclasses import dataclass
import os


@dataclass(frozen=True, slots=True)
class Settings:
    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")
    qdrant_url: str | None = os.getenv("QDRANT_URL")
    qdrant_api_key: str | None = os.getenv("QDRANT_API_KEY")
    environment: str = os.getenv("RAG_ENV", "development")


def require_secret(value: str | None, name: str) -> str:
    if not value:
        raise RuntimeError(f"Configure {name} em um Secret ou variável de ambiente.")
    return value
