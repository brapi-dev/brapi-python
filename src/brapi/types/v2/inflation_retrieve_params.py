# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InflationRetrieveParams"]


class InflationRetrieveParams(TypedDict, total=False):
    end: str
    """Data de fim (DD/MM/YYYY)"""

    historical: str
    """Incluir dados históricos (true/false)"""

    sort_by: Annotated[str, PropertyInfo(alias="sortBy")]
    """Campo para ordenação (date ou value)"""

    sort_order: Annotated[str, PropertyInfo(alias="sortOrder")]
    """Ordem de classificação (asc ou desc)"""

    start: str
    """Data de início (DD/MM/YYYY)"""
