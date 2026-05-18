# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["InflationRetrieveResponse", "Inflation"]


class Inflation(BaseModel):
    date: str

    epoch_date: float = FieldInfo(alias="epochDate")

    value: str
    """Variação percentual do IPCA no mês"""


class InflationRetrieveResponse(BaseModel):
    inflation: List[Inflation]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em formato ISO 8601"""

    took: int
    """Tempo de processamento em milissegundos"""
