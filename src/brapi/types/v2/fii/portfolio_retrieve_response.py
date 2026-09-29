# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .fii_property import FiiProperty
from .fii_financial_asset import FiiFinancialAsset
from .fii_portfolio_summary import FiiPortfolioSummary
from .fii_portfolio_allocation import FiiPortfolioAllocation

__all__ = ["PortfolioRetrieveResponse", "Fii", "FiiLand", "FiiRight"]


class FiiLand(BaseModel):
    address: Optional[str] = None

    area: Optional[float] = None

    confidential: bool

    equity_share: Optional[float] = FieldInfo(alias="equityShare", default=None)

    identifier: Optional[str] = None

    invested_share: Optional[float] = FieldInfo(alias="investedShare", default=None)

    name: str


class FiiRight(BaseModel):
    confidential: bool

    description: Optional[str] = None

    identifier: Optional[str] = None

    name: str

    value: Optional[float] = None


class Fii(BaseModel):
    allocations: List[FiiPortfolioAllocation]

    cnpj: str

    financial_assets: List[FiiFinancialAsset] = FieldInfo(alias="financialAssets")

    fund_holdings: List[FiiFinancialAsset] = FieldInfo(alias="fundHoldings")

    lands: List[FiiLand]

    properties: List[FiiProperty]

    reference_date: str = FieldInfo(alias="referenceDate")

    rights: List[FiiRight]

    summary: FiiPortfolioSummary

    symbol: Optional[str] = None

    version: float


class PortfolioRetrieveResponse(BaseModel):
    fiis: List[Fii]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
