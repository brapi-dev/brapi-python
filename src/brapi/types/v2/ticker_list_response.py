# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TickerListResponse", "Facets", "Index", "Pagination", "Result", "ResultQuote"]


class Facets(BaseModel):
    asset_types: List[str] = FieldInfo(alias="assetTypes")
    """Valores aceitos em `type`."""

    sectors: List[str]
    """Valores aceitos em `sector`."""

    subsectors: List[str]
    """Valores aceitos em `subsector`."""

    sub_types: List[str] = FieldInfo(alias="subTypes")
    """Valores aceitos em `subType`."""


class Index(BaseModel):
    asset_type: Literal["index"] = FieldInfo(alias="assetType")

    exchange: Literal["B3"]

    name: str

    symbol: str


class Pagination(BaseModel):
    has_next_page: bool = FieldInfo(alias="hasNextPage")

    limit: float

    page: float

    total_items: float = FieldInfo(alias="totalItems")

    total_pages: float = FieldInfo(alias="totalPages")


class ResultQuote(BaseModel):
    change_percent: Optional[float] = FieldInfo(alias="changePercent", default=None)
    """Variação no dia, em porcentagem."""

    last_price: Optional[float] = FieldInfo(alias="lastPrice", default=None)
    """Último preço."""

    market_cap: Optional[float] = FieldInfo(alias="marketCap", default=None)
    """Valor de mercado, em reais. Pode ser nulo."""

    volume: Optional[float] = None
    """Volume negociado no dia."""


class Result(BaseModel):
    asset_type: Optional[Literal["stock", "fund", "bdr"]] = FieldInfo(alias="assetType", default=None)
    """Tipo do ativo."""

    currency: Literal["BRL"]
    """Moeda."""

    exchange: Literal["B3"]
    """Bolsa."""

    is_active: bool = FieldInfo(alias="isActive")
    """`true` quando o ativo está em negociação."""

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)
    """URL do logo."""

    long_name: Optional[str] = FieldInfo(alias="longName", default=None)
    """Nome longo. Pode ser nulo."""

    name: str
    """Nome da empresa ou do fundo."""

    quote: ResultQuote

    sector: Optional[str] = None
    """Setor. Pode ser nulo."""

    subsector: Optional[str] = None
    """Subsetor. Pode ser nulo."""

    sub_type: Optional[Literal["stock", "unit", "fii", "etf", "fi-infra", "fi-agro", "fip", "fidc", "bdr"]] = FieldInfo(
        alias="subType", default=None
    )
    """Subtipo do ativo: stock, unit, fii, etf, fi-infra, fi-agro, fip, fidc ou bdr."""

    symbol: str
    """Ticker do ativo."""


class TickerListResponse(BaseModel):
    facets: Facets

    indexes: List[Index]

    pagination: Pagination

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    results: List[Result]

    took: int
    """Tempo de processamento, em milissegundos."""
