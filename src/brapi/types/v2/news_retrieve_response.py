# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .news_story import NewsStory

__all__ = ["NewsRetrieveResponse", "Result", "ResultRelated"]


class ResultRelated(BaseModel):
    id: str

    description: Optional[str] = None

    importance: int

    published_at: str = FieldInfo(alias="publishedAt")

    sentiment: Literal["positive", "negative", "neutral", "mixed"]

    slug: str

    source_count: int = FieldInfo(alias="sourceCount")
    """Número de veículos que noticiaram o fato."""

    tickers: List[str]

    title: str


class Result(NewsStory):
    related: List[ResultRelated]
    """Até 6 notícias relacionadas, da mais parecida para a menos parecida."""


class NewsRetrieveResponse(BaseModel):
    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    results: List[Result]
    """A notícia encontrada, com a matéria completa e as notícias relacionadas."""

    took: int
    """Tempo de processamento, em milissegundos."""
