# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FiiHistoricalResponse", "Fii", "FiiHistoricalDataPrice"]


class FiiHistoricalDataPrice(BaseModel):
    adjusted_close: Optional[float] = FieldInfo(alias="adjustedClose", default=None)

    close: Optional[float] = None

    date: int

    high: Optional[float] = None

    low: Optional[float] = None

    open: Optional[float] = None

    volume: Optional[float] = None


class Fii(BaseModel):
    historical_data_price: List[FiiHistoricalDataPrice] = FieldInfo(alias="historicalDataPrice")

    symbol: str


class FiiHistoricalResponse(BaseModel):
    fiis: List[Fii]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
