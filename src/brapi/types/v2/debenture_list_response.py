# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .debenture import Debenture

__all__ = ["DebentureListResponse", "Pagination"]


class Pagination(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")

    limit: int

    page: int

    total: int


class DebentureListResponse(BaseModel):
    pagination: Pagination

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    results: List[Debenture]

    took: int
    """Tempo de processamento, em milissegundos."""
