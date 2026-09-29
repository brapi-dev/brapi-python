# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .fii_property import FiiProperty
from .fii_property_summary import FiiPropertySummary

__all__ = ["PropertyRetrieveResponse", "Fii"]


class Fii(BaseModel):
    cnpj: str

    properties: List[FiiProperty]

    reference_date: str = FieldInfo(alias="referenceDate")

    summary: FiiPropertySummary

    symbol: Optional[str] = None

    version: float


class PropertyRetrieveResponse(BaseModel):
    fiis: List[Fii]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
