# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["FiagroPortfolioResponse", "Fund"]


class Fund(BaseModel):
    allocations: Optional[Dict[str, Optional[object]]] = None

    cnpj: str

    investors: Optional[Dict[str, Optional[object]]] = None

    liabilities: Optional[Dict[str, Optional[object]]] = None

    reference_date: str = FieldInfo(alias="referenceDate")

    summary: Optional[Dict[str, Optional[object]]] = None

    symbol: Optional[str] = None


class FiagroPortfolioResponse(BaseModel):
    funds: List[Fund]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
