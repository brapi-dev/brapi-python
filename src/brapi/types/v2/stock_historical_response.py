# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["StockHistoricalResponse", "Result", "ResultData", "ResultDataHistoricalDataPrice"]


class ResultDataHistoricalDataPrice(BaseModel):
    adjusted_close: Optional[float] = FieldInfo(alias="adjustedClose", default=None)

    close: Optional[float] = None

    date: int
    """Data do pregão em Unix timestamp, em segundos."""

    high: Optional[float] = None

    low: Optional[float] = None

    open: Optional[float] = None

    volume: Optional[float] = None

    raw_close: Optional[float] = FieldInfo(alias="rawClose", default=None)
    """Preço de fechamento original, sem ajuste.

    Vem com `includeRaw=true` em intervalos diários. Pode ser nulo.
    """

    raw_high: Optional[float] = FieldInfo(alias="rawHigh", default=None)
    """Preço máximo original, sem ajuste.

    Vem com `includeRaw=true` em intervalos diários. Pode ser nulo.
    """

    raw_low: Optional[float] = FieldInfo(alias="rawLow", default=None)
    """Preço mínimo original, sem ajuste.

    Vem com `includeRaw=true` em intervalos diários. Pode ser nulo.
    """

    raw_open: Optional[float] = FieldInfo(alias="rawOpen", default=None)
    """Preço de abertura original, sem ajuste.

    Vem com `includeRaw=true` em intervalos diários. Pode ser nulo.
    """


class ResultData(BaseModel):
    historical_data_price: List[ResultDataHistoricalDataPrice] = FieldInfo(alias="historicalDataPrice")

    used_interval: str = FieldInfo(alias="usedInterval")

    used_range: str = FieldInfo(alias="usedRange")


class Result(BaseModel):
    changed: bool
    """`true` quando o ticker enviado foi trocado pelo ticker atual."""

    data: ResultData

    requested_symbol: str = FieldInfo(alias="requestedSymbol")
    """Ticker enviado na requisição."""

    symbol: str
    """Ticker atual, depois de resolver renomes."""


class StockHistoricalResponse(BaseModel):
    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    results: List[Result]

    took: int
    """Tempo de processamento, em milissegundos."""
