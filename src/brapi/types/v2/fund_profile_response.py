# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FundProfileResponse", "Profile"]


class Profile(BaseModel):
    cnpj: str

    concentration: Optional[Dict[str, Optional[object]]] = None

    investor_breakdown: Optional[Dict[str, Optional[object]]] = FieldInfo(alias="investorBreakdown", default=None)

    liquidity: Optional[Dict[str, Optional[object]]] = None

    private_credit: Optional[Dict[str, Optional[object]]] = FieldInfo(alias="privateCredit", default=None)

    reference_date: str = FieldInfo(alias="referenceDate")

    risk: Optional[Dict[str, Optional[object]]] = None

    symbol: Optional[str] = None


class FundProfileResponse(BaseModel):
    profiles: List[Profile]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
