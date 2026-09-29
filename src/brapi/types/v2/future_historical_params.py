# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FutureHistoricalParams"]


class FutureHistoricalParams(TypedDict, total=False):
    symbol: Required[str]
    """Código do contrato. Ex.: `WINM26`."""

    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """Data final no formato YYYY-MM-DD. Padrão: hoje."""

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """Ordem das datas. `desc` traz o pregão mais recente primeiro."""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """Data inicial no formato YYYY-MM-DD. Padrão: 12 meses antes de hoje."""
