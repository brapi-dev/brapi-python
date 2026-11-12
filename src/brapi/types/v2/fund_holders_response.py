# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FundHoldersResponse", "Asset", "Fund", "Pagination", "Summary"]


class Asset(BaseModel):
    cnpj: Optional[str] = None

    name: Optional[str] = None

    symbol: Optional[str] = None


class Fund(BaseModel):
    asset_type: Optional[Literal["fii", "fiagro", "fiinfra", "fif", "fidc", "fip", "etf", "other"]] = FieldInfo(
        alias="assetType", default=None
    )

    cnpj: str

    market_value: float = FieldInfo(alias="marketValue")
    """Valor da posição em reais, com ações emprestadas."""

    name: Optional[str] = None

    net_assets: Optional[float] = FieldInfo(alias="netAssets", default=None)
    """Patrimônio líquido do fundo, em reais."""

    quantity: Optional[float] = None

    symbol: Optional[str] = None

    weight_percent: Optional[float] = FieldInfo(alias="weightPercent", default=None)
    """Peso do ativo no patrimônio do fundo, em %."""


class Pagination(BaseModel):
    has_next_page: bool = FieldInfo(alias="hasNextPage")

    limit: int

    page: int

    total_items: int = FieldInfo(alias="totalItems")

    total_pages: int = FieldInfo(alias="totalPages")


class Summary(BaseModel):
    funds_count: int = FieldInfo(alias="fundsCount")

    total_market_value: float = FieldInfo(alias="totalMarketValue")

    total_quantity: float = FieldInfo(alias="totalQuantity")


class FundHoldersResponse(BaseModel):
    asset: Asset

    funds: List[Fund]

    pagination: Pagination

    reference_date: Optional[str] = FieldInfo(alias="referenceDate", default=None)

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    summary: Summary

    took: int
    """Tempo de processamento, em milissegundos."""
