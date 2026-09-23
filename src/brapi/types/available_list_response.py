# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["AvailableListResponse"]


class AvailableListResponse(BaseModel):
    indexes: List[str]
    """Tickers de índices."""

    stocks: List[str]
    """Tickers de ativos."""
