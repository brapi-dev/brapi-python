# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PrimeRateRetrieveResponse", "PrimeRate"]


class PrimeRate(BaseModel):
    date: str

    epoch_date: float = FieldInfo(alias="epochDate")

    value: str
    """Taxa SELIC meta anualizada (% a.a.)"""


class PrimeRateRetrieveResponse(BaseModel):
    prime_rate: List[PrimeRate] = FieldInfo(alias="prime-rate")

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em formato ISO 8601"""

    took: int
    """Tempo de processamento em milissegundos"""
