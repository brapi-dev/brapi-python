# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["FiiFinancialsResponse", "Financial"]


class Financial(BaseModel):
    cnpj: str

    document_type: str = FieldInfo(alias="documentType")

    fields: Optional[Dict[str, Optional[object]]] = None

    reference_date: str = FieldInfo(alias="referenceDate")

    symbol: Optional[str] = None

    year: float


class FiiFinancialsResponse(BaseModel):
    financials: List[Financial]

    pagination: PaginationMeta

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
