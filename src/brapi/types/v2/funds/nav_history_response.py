# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ..fund_pagination_meta import FundPaginationMeta

__all__ = ["NavHistoryResponse", "History"]


class History(BaseModel):
    class_or_series: Optional[str] = FieldInfo(alias="classOrSeries", default=None)

    cnpj: str

    daily_applications: Optional[float] = FieldInfo(alias="dailyApplications", default=None)

    daily_redemptions: Optional[float] = FieldInfo(alias="dailyRedemptions", default=None)

    date: str

    equity: Optional[float] = None

    monthly_return: Optional[float] = FieldInfo(alias="monthlyReturn", default=None)

    nav_per_share: Optional[float] = FieldInfo(alias="navPerShare", default=None)

    symbol: Optional[str] = None

    total_assets: Optional[float] = FieldInfo(alias="totalAssets", default=None)

    total_investors: Optional[float] = FieldInfo(alias="totalInvestors", default=None)


class NavHistoryResponse(BaseModel):
    history: List[History]

    pagination: FundPaginationMeta

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
