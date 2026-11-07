# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .news_story import NewsStory

__all__ = ["NewsRetrieveResponse", "Result", "ResultRelated", "ResultRelatedImage"]


class ResultRelatedImage(BaseModel):
    """Imagem da notícia.

    Só as notícias mais importantes têm imagem; as outras vêm com `null`.
    """

    alt: str
    """Descrição da imagem."""

    credit: Optional[str] = None
    """Autor da foto. `null` para imagem gerada por IA."""

    height: int

    license: Optional[str] = None

    license_url: Optional[str] = FieldInfo(alias="licenseUrl", default=None)

    small_url: str = FieldInfo(alias="smallUrl")
    """Imagem em WebP, 800 px de largura."""

    source: Literal["commons", "ai"]
    """`commons` para foto do Wikimedia Commons.

    `ai` para imagem ilustrativa gerada por IA.
    """

    source_url: Optional[str] = FieldInfo(alias="sourceUrl", default=None)
    """Página do arquivo no Wikimedia Commons."""

    url: str
    """Imagem em WebP, 1600 px de largura."""

    width: int


class ResultRelated(BaseModel):
    id: str

    description: Optional[str] = None

    event_type: Literal[
        "earnings",
        "dividends",
        "guidance",
        "mna",
        "financing",
        "buyback",
        "rating",
        "analyst",
        "management",
        "legal_regulatory",
        "operations",
        "market_move",
        "macro",
        "other",
    ] = FieldInfo(alias="eventType")

    image: Optional[ResultRelatedImage] = None
    """Imagem da notícia.

    Só as notícias mais importantes têm imagem; as outras vêm com `null`.
    """

    importance: int

    published_at: str = FieldInfo(alias="publishedAt")

    scope: Literal["company", "market"]

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
