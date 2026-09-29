# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ..treasury_list_item import TreasuryListItem

__all__ = ["IndicatorRetrieveResponse"]


class IndicatorRetrieveResponse(BaseModel):
    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    results: List[TreasuryListItem]

    took: int
    """Tempo de processamento, em milissegundos."""
