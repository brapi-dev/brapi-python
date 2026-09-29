# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .future_quote import FutureQuote

__all__ = ["FutureTermStructureResponse"]


class FutureTermStructureResponse(BaseModel):
    asset: str

    contracts: List[FutureQuote]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
