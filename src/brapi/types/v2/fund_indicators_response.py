# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FundIndicatorsResponse", "Fund"]


class Fund(BaseModel):
    as_of_date: Optional[str] = FieldInfo(alias="asOfDate", default=None)

    asset_type: Literal["fii", "fiagro", "fiinfra", "fif", "fidc", "fip", "etf", "other"] = FieldInfo(alias="assetType")

    cnpj: str

    daily_applications: Optional[float] = FieldInfo(alias="dailyApplications", default=None)

    daily_redemptions: Optional[float] = FieldInfo(alias="dailyRedemptions", default=None)

    dividend_yield_monthly: Optional[float] = FieldInfo(alias="dividendYieldMonthly", default=None)

    equity: Optional[float] = None

    monthly_return: Optional[float] = FieldInfo(alias="monthlyReturn", default=None)

    name: Optional[str] = None

    nav_per_share: Optional[float] = FieldInfo(alias="navPerShare", default=None)

    patrimonial_monthly_return: Optional[float] = FieldInfo(alias="patrimonialMonthlyReturn", default=None)

    price: Optional[float] = None

    price_to_nav: Optional[float] = FieldInfo(alias="priceToNav", default=None)

    shares_outstanding: Optional[float] = FieldInfo(alias="sharesOutstanding", default=None)

    symbol: Optional[str] = None

    total_assets: Optional[float] = FieldInfo(alias="totalAssets", default=None)

    total_investors: Optional[float] = FieldInfo(alias="totalInvestors", default=None)


class FundIndicatorsResponse(BaseModel):
    funds: List[Fund]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
