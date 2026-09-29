# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .future_specs import FutureSpecs

__all__ = ["FutureListResponse", "Pagination"]


class Pagination(BaseModel):
    limit: int

    page: int

    total: int

    total_pages: int = FieldInfo(alias="totalPages")


class FutureListResponse(BaseModel):
    futures: List[FutureSpecs]

    pagination: Pagination

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
