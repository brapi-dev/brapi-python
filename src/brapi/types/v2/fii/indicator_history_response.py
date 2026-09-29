# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["IndicatorHistoryResponse", "History"]


class History(BaseModel):
    dividend_yield12m: Optional[float] = FieldInfo(alias="dividendYield12m", default=None)

    dividend_yield1m: Optional[float] = FieldInfo(alias="dividendYield1m", default=None)

    equity: Optional[float] = None

    monthly_return: Optional[float] = FieldInfo(alias="monthlyReturn", default=None)

    nav_per_share: Optional[float] = FieldInfo(alias="navPerShare", default=None)

    price: Optional[float] = None

    price_to_nav: Optional[float] = FieldInfo(alias="priceToNav", default=None)

    reference_date: str = FieldInfo(alias="referenceDate")

    segment_type: Optional[str] = FieldInfo(alias="segmentType", default=None)

    shares_outstanding: Optional[float] = FieldInfo(alias="sharesOutstanding", default=None)

    symbol: str

    total_assets: Optional[float] = FieldInfo(alias="totalAssets", default=None)

    total_investors: Optional[float] = FieldInfo(alias="totalInvestors", default=None)


class IndicatorHistoryResponse(BaseModel):
    history: List[History]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
