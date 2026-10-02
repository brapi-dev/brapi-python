# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..dividends_data import DividendsData

__all__ = ["StockDividendsResponse", "Result"]


class Result(BaseModel):
    changed: bool
    """`true` quando `symbol` difere de `requestedSymbol`."""

    data: DividendsData
    """Proventos.

    Na rota `/api/quote/{tickers}`, vem com `dividends=true`. Na rota
    `/api/v2/stocks/dividends`, não exige esse parâmetro.
    """

    requested_symbol: str = FieldInfo(alias="requestedSymbol")
    """Ticker enviado na requisição."""

    symbol: str
    """Ticker usado para os dados retornados."""


class StockDividendsResponse(BaseModel):
    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    results: List[Result]

    took: int
    """Tempo de processamento, em milissegundos."""
