# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .stock_fundamentals_series import StockFundamentalsSeries

__all__ = ["StockStatisticsResponse"]


class StockStatisticsResponse(BaseModel):
    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    results: List[StockFundamentalsSeries]

    took: int
    """Tempo de processamento, em milissegundos."""
