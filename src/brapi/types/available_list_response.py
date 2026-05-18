# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["AvailableListResponse"]


class AvailableListResponse(BaseModel):
    indexes: List[str]
    """Lista de índices disponíveis"""

    stocks: List[str]
    """Lista de códigos de ações disponíveis"""
