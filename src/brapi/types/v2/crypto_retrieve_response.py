# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CryptoRetrieveResponse", "Coin", "CoinHistoricalDataPrice"]


class CoinHistoricalDataPrice(BaseModel):
    adjusted_close: Optional[float] = FieldInfo(alias="adjustedClose", default=None)

    close: Optional[float] = None

    date: int

    high: Optional[float] = None

    low: Optional[float] = None

    open: Optional[float] = None

    volume: Optional[float] = None


class Coin(BaseModel):
    coin: str

    coin_name: str = FieldInfo(alias="coinName")

    currency: str

    currency_rate_from_usd: float = FieldInfo(alias="currencyRateFromUSD")

    market_cap: float = FieldInfo(alias="marketCap")

    regular_market_change: float = FieldInfo(alias="regularMarketChange")

    regular_market_change_percent: float = FieldInfo(alias="regularMarketChangePercent")

    regular_market_day_high: float = FieldInfo(alias="regularMarketDayHigh")

    regular_market_day_low: float = FieldInfo(alias="regularMarketDayLow")

    regular_market_day_range: str = FieldInfo(alias="regularMarketDayRange")

    regular_market_price: float = FieldInfo(alias="regularMarketPrice")

    regular_market_time: str = FieldInfo(alias="regularMarketTime")

    regular_market_volume: float = FieldInfo(alias="regularMarketVolume")

    coin_image_url: Optional[str] = FieldInfo(alias="coinImageUrl", default=None)

    historical_data_price: Optional[List[CoinHistoricalDataPrice]] = FieldInfo(
        alias="historicalDataPrice", default=None
    )

    used_interval: Optional[str] = FieldInfo(alias="usedInterval", default=None)

    used_range: Optional[str] = FieldInfo(alias="usedRange", default=None)

    valid_intervals: Optional[List[str]] = FieldInfo(alias="validIntervals", default=None)

    valid_ranges: Optional[List[str]] = FieldInfo(alias="validRanges", default=None)


class CryptoRetrieveResponse(BaseModel):
    coins: List[Coin]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em formato ISO 8601"""

    took: int
    """Tempo de processamento em milissegundos"""
