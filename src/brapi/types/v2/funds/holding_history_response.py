# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["HoldingHistoryResponse", "Asset", "Fund", "History"]


class Asset(BaseModel):
    cnpj: Optional[str] = None

    name: Optional[str] = None

    symbol: Optional[str] = None


class Fund(BaseModel):
    asset_type: Optional[Literal["fii", "fiagro", "fiinfra", "fif", "fidc", "fip", "etf", "other"]] = FieldInfo(
        alias="assetType", default=None
    )

    cnpj: str

    name: Optional[str] = None

    symbol: Optional[str] = None


class History(BaseModel):
    market_value: float = FieldInfo(alias="marketValue")
    """Valor em reais."""

    net_assets: float = FieldInfo(alias="netAssets")
    """Patrimônio líquido do fundo, em reais."""

    quantity: Optional[float] = None
    """Quantidade.

    Vendas a descoberto ficam negativas. `null` quando o fundo tem mais de um ativo
    da empresa no mês, ou títulos sem código.
    """

    reference_date: str = FieldInfo(alias="referenceDate")
    """Fim do mês da carteira."""

    weight_percent: float = FieldInfo(alias="weightPercent")
    """Peso do ativo no patrimônio do fundo, em %.

    Zero quando o fundo não tem o ativo no mês.
    """


class HoldingHistoryResponse(BaseModel):
    asset: Asset

    fund: Fund

    history: List[History]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
