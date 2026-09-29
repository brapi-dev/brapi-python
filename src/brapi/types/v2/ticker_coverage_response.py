# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TickerCoverageResponse", "Result", "ResultAvailableData"]


class ResultAvailableData(BaseModel):
    fii_dividends: bool = FieldInfo(alias="fiiDividends")

    fii_indicators: bool = FieldInfo(alias="fiiIndicators")

    fii_portfolio: bool = FieldInfo(alias="fiiPortfolio")

    fii_properties: bool = FieldInfo(alias="fiiProperties")

    fii_reports: bool = FieldInfo(alias="fiiReports")

    financial_statements: bool = FieldInfo(alias="financialStatements")

    historical: bool

    profile: bool

    quote: bool

    statistics: bool

    stock_dividends: bool = FieldInfo(alias="stockDividends")

    ticker: bool


class Result(BaseModel):
    asset_type: Optional[str] = FieldInfo(alias="assetType", default=None)
    """Tipo do ativo. Pode ser nulo."""

    available_data: ResultAvailableData = FieldInfo(alias="availableData")

    changed: bool
    """`true` quando o ticker enviado foi trocado pelo ticker atual."""

    recommended_endpoints: Dict[str, str] = FieldInfo(alias="recommendedEndpoints")
    """Endpoints para consultar os dados do ticker."""

    requested_symbol: str = FieldInfo(alias="requestedSymbol")
    """Ticker enviado na requisição."""

    status: Literal["available", "renamed", "unknown", "wrong_endpoint"]
    """`available`: o ticker tem dados.

    `renamed`: o ticker mudou e tem dados. `unknown`: o ticker não foi encontrado.
    `wrong_endpoint`: o ticker é de uma opção.
    """

    sub_type: Optional[str] = FieldInfo(alias="subType", default=None)
    """Subtipo do ativo. Pode ser nulo."""

    symbol: str
    """Ticker atual usado na verificação."""


class TickerCoverageResponse(BaseModel):
    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    results: List[Result]

    took: int
    """Tempo de processamento, em milissegundos."""
