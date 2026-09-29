# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ..fund_pagination_meta import FundPaginationMeta

__all__ = ["FiagroReportsResponse", "Report"]


class Report(BaseModel):
    administrator_name: Optional[str] = FieldInfo(alias="administratorName", default=None)

    amortization_rate_monthly: Optional[float] = FieldInfo(alias="amortizationRateMonthly", default=None)

    cnpj: str

    dividend_yield_monthly: Optional[float] = FieldInfo(alias="dividendYieldMonthly", default=None)

    income_to_distribute: Optional[float] = FieldInfo(alias="incomeToDistribute", default=None)

    isin: Optional[str] = None

    liquidity_needs: Optional[float] = FieldInfo(alias="liquidityNeeds", default=None)

    manager_name: Optional[str] = FieldInfo(alias="managerName", default=None)

    market: Optional[str] = None

    monthly_return: Optional[float] = FieldInfo(alias="monthlyReturn", default=None)

    name: Optional[str] = None

    nav_per_share: Optional[float] = FieldInfo(alias="navPerShare", default=None)

    net_equity: Optional[float] = FieldInfo(alias="netEquity", default=None)

    patrimonial_monthly_return: Optional[float] = FieldInfo(alias="patrimonialMonthlyReturn", default=None)

    reference_date: str = FieldInfo(alias="referenceDate")

    shares_outstanding: Optional[float] = FieldInfo(alias="sharesOutstanding", default=None)

    symbol: Optional[str] = None

    total_assets: Optional[float] = FieldInfo(alias="totalAssets", default=None)

    total_investors: Optional[float] = FieldInfo(alias="totalInvestors", default=None)

    total_liabilities: Optional[float] = FieldInfo(alias="totalLiabilities", default=None)

    version: float


class FiagroReportsResponse(BaseModel):
    pagination: FundPaginationMeta

    reports: List[Report]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
