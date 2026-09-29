# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FiiFinancialsParams"]


class FiiFinancialsParams(TypedDict, total=False):
    cnpjs: str
    """CNPJs de FIIs separados por vírgula, até 20. Aceita com ou sem pontuação."""

    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """Data de referência final no formato YYYY-MM-DD."""

    limit: int

    page: int

    sort_by: Annotated[str, PropertyInfo(alias="sortBy")]
    """Campo de ordenação: referenceDate, symbol, cnpj ou year."""

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """Data de referência inicial no formato YYYY-MM-DD."""

    symbols: str
    """Tickers de FIIs separados por vírgula, até 20."""

    year: Optional[int]
    """Ano do exercício do documento."""
