# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["NewsStory", "Asset", "Image", "Sentiment", "Source"]


class Asset(BaseModel):
    name: str

    reason: Optional[str] = None
    """Por que a notícia afeta o ativo."""

    relevance: Literal["primary", "secondary"]
    """`primary` quando a notícia é sobre o ativo.

    `secondary` quando o ativo é afetado.
    """

    sentiment: Optional[Literal["positive", "negative", "neutral"]] = None
    """Efeito provável da notícia no ativo."""

    ticker: str
    """Ticker principal do ativo."""

    tickers: List[str]
    """Todos os tickers do ativo citados na notícia."""

    type: Literal["stock", "fii", "fiagro", "fiinfra", "fidc", "fip", "etf", "bdr", "index", "currency"]
    """
    Tipo do ativo: `stock`, `fii`, `fiagro`, `fiinfra`, `fidc`, `fip`, `etf`, `bdr`,
    `index` ou `currency`.
    """


class Image(BaseModel):
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


class Sentiment(BaseModel):
    """Sentimento da notícia."""

    label: Literal["positive", "negative", "neutral", "mixed"]

    score: float
    """De -1 (muito negativa) a 1 (muito positiva)."""


class Source(BaseModel):
    name: str
    """Nome do veículo."""

    published_at: str = FieldInfo(alias="publishedAt")
    """Data e hora de publicação no veículo, em ISO 8601."""

    title: str
    """Título da matéria no veículo."""

    url: str
    """Link da matéria no veículo."""


class NewsStory(BaseModel):
    id: str

    article: Optional[str] = None
    """Matéria completa em Markdown.

    Vem só com `includeArticle=true` ou na consulta de uma notícia. `null` enquanto
    a matéria não foi escrita.
    """

    article_written_at: Optional[str] = FieldInfo(alias="articleWrittenAt", default=None)
    """Quando a matéria foi escrita, em ISO 8601."""

    assets: List[Asset]
    """Ativos sobre os quais a notícia trata ou que ela afeta."""

    description: Optional[str] = None
    """Uma frase sobre a notícia."""

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

    image: Optional[Image] = None
    """Imagem da notícia.

    Só as notícias mais importantes têm imagem; as outras vêm com `null`.
    """

    importance: int
    """De 1 (pequena) a 5 (move o mercado)."""

    key_points: List[str] = FieldInfo(alias="keyPoints")
    """Pontos principais."""

    published_at: str = FieldInfo(alias="publishedAt")
    """Data e hora da primeira publicação, em ISO 8601."""

    scope: Literal["company", "market"]
    """`company` para notícias de empresas e ativos.

    `market` para economia, juros, câmbio, política e o índice.
    """

    sentiment: Sentiment
    """Sentimento da notícia."""

    slug: str

    sources: List[Source]
    """Matérias dos veículos usadas para escrever a notícia."""

    summary: str
    """Resumo da notícia."""

    title: str

    topics: List[str]
    """Temas da notícia."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """Última mudança no conteúdo, em ISO 8601."""

    url: str
    """Página da notícia na brapi."""
