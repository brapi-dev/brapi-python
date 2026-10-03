# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["StockQuoteResponse", "Result", "ResultData"]


class ResultData(BaseModel):
    currency: str

    fifty_two_week_high: float = FieldInfo(alias="fiftyTwoWeekHigh")

    fifty_two_week_low: float = FieldInfo(alias="fiftyTwoWeekLow")

    fifty_two_week_range: str = FieldInfo(alias="fiftyTwoWeekRange")

    logourl: str

    long_name: str = FieldInfo(alias="longName")

    market_cap: Optional[float] = FieldInfo(alias="marketCap", default=None)

    regular_market_change: float = FieldInfo(alias="regularMarketChange")

    regular_market_change_percent: float = FieldInfo(alias="regularMarketChangePercent")

    regular_market_day_high: float = FieldInfo(alias="regularMarketDayHigh")

    regular_market_day_low: float = FieldInfo(alias="regularMarketDayLow")

    regular_market_day_range: str = FieldInfo(alias="regularMarketDayRange")

    regular_market_open: float = FieldInfo(alias="regularMarketOpen")

    regular_market_previous_close: float = FieldInfo(alias="regularMarketPreviousClose")

    regular_market_price: float = FieldInfo(alias="regularMarketPrice")

    regular_market_time: str = FieldInfo(alias="regularMarketTime")
    """Horário da cotação em ISO 8601."""

    regular_market_volume: float = FieldInfo(alias="regularMarketVolume")

    short_name: str = FieldInfo(alias="shortName")


class Result(BaseModel):
    changed: bool
    """`true` quando `symbol` difere de `requestedSymbol`."""

    data: ResultData

    requested_symbol: str = FieldInfo(alias="requestedSymbol")
    """Ticker enviado na requisição."""

    symbol: str
    """Ticker usado para os dados retornados."""


class StockQuoteResponse(BaseModel):
    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    results: List[Result]

    took: int
    """Tempo de processamento, em milissegundos."""
