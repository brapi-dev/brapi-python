# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["FidcPortfolioResponse", "Fund"]


class Fund(BaseModel):
    cedentes: Optional[Dict[str, Optional[object]]] = None

    cnpj: str

    delinquency_buckets: Optional[Dict[str, Optional[object]]] = FieldInfo(alias="delinquencyBuckets", default=None)

    investors: Optional[Dict[str, Optional[object]]] = None

    maturity_buckets: Optional[Dict[str, Optional[object]]] = FieldInfo(alias="maturityBuckets", default=None)

    quota_classes: Optional[List[Dict[str, Optional[object]]]] = FieldInfo(alias="quotaClasses", default=None)

    reference_date: str = FieldInfo(alias="referenceDate")

    risk_buckets: Optional[Dict[str, Optional[object]]] = FieldInfo(alias="riskBuckets", default=None)

    sectors: Optional[Dict[str, Optional[object]]] = None

    symbol: Optional[str] = None


class FidcPortfolioResponse(BaseModel):
    funds: List[Fund]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
