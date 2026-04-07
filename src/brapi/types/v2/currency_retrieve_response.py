# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CurrencyRetrieveResponse", "Currency"]


class Currency(BaseModel):
    ask_price: str = FieldInfo(alias="askPrice")

    bid_price: str = FieldInfo(alias="bidPrice")

    bid_variation: str = FieldInfo(alias="bidVariation")

    from_currency: str = FieldInfo(alias="fromCurrency")

    high: str

    low: str

    name: str

    percentage_change: str = FieldInfo(alias="percentageChange")

    to_currency: str = FieldInfo(alias="toCurrency")

    updated_at_date: str = FieldInfo(alias="updatedAtDate")

    updated_at_timestamp: str = FieldInfo(alias="updatedAtTimestamp")


class CurrencyRetrieveResponse(BaseModel):
    currency: List[Currency]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em formato ISO 8601"""

    took: int
    """Tempo de processamento em milissegundos"""
