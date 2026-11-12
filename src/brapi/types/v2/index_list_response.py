# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["IndexListResponse", "Index", "IndexTrackingFund"]


class IndexTrackingFund(BaseModel):
    name: Optional[str] = None

    symbol: str


class Index(BaseModel):
    name: str

    reference_date: Optional[str] = FieldInfo(alias="referenceDate", default=None)
    """Mês da carteira mais recente do ETF."""

    symbol: str

    tracking_fund: IndexTrackingFund = FieldInfo(alias="trackingFund")


class IndexListResponse(BaseModel):
    indexes: List[Index]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
