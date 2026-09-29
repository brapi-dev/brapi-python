# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ..fund_pagination_meta import FundPaginationMeta

__all__ = ["FidcReportsResponse", "Report"]


class Report(BaseModel):
    administrator_name: Optional[str] = FieldInfo(alias="administratorName", default=None)

    assets: Optional[float] = None

    average_net_equity: Optional[float] = FieldInfo(alias="averageNetEquity", default=None)

    class_: Optional[str] = FieldInfo(alias="class", default=None)

    cnpj: str

    condominium_type: Optional[str] = FieldInfo(alias="condominiumType", default=None)

    liabilities: Optional[float] = None

    name: Optional[str] = None

    net_equity: Optional[float] = FieldInfo(alias="netEquity", default=None)

    portfolio_value: Optional[float] = FieldInfo(alias="portfolioValue", default=None)

    reference_date: str = FieldInfo(alias="referenceDate")

    symbol: Optional[str] = None


class FidcReportsResponse(BaseModel):
    pagination: FundPaginationMeta

    reports: List[Report]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
