# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CurrencyHistoricalResponse", "Result", "ResultObservation", "Error"]


class ResultObservation(BaseModel):
    date: str

    value: float


class Result(BaseModel):
    from_currency: str = FieldInfo(alias="fromCurrency")

    observations: List[ResultObservation]

    pair: str

    to_currency: str = FieldInfo(alias="toCurrency")


class Error(BaseModel):
    code: str

    message: str

    pair: str

    details: Optional[Dict[str, Optional[object]]] = None


class CurrencyHistoricalResponse(BaseModel):
    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    results: List[Result]

    took: int
    """Tempo de processamento, em milissegundos."""

    errors: Optional[List[Error]] = None
