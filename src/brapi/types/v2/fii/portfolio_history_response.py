# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .fii_portfolio_summary import FiiPortfolioSummary
from .fii_portfolio_allocation import FiiPortfolioAllocation

__all__ = ["PortfolioHistoryResponse", "History"]


class History(BaseModel):
    allocations: List[FiiPortfolioAllocation]

    cnpj: str

    reference_date: str = FieldInfo(alias="referenceDate")

    summary: FiiPortfolioSummary

    symbol: Optional[str] = None

    version: float


class PortfolioHistoryResponse(BaseModel):
    history: List[History]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
