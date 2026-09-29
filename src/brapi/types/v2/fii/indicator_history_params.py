# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["IndicatorHistoryParams"]


class IndicatorHistoryParams(TypedDict, total=False):
    symbols: Required[str]
    """Tickers de FIIs separados por vírgula, até 20. Ex.: HGLG11,MXRF11."""

    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """Data final no formato YYYY-MM-DD."""

    sort_by: Annotated[str, PropertyInfo(alias="sortBy")]
    """Campo de ordenação."""

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """Direção da ordenação."""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """Data inicial no formato YYYY-MM-DD."""
