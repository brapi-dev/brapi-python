# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["IndicatorHistoryParams"]


class IndicatorHistoryParams(TypedDict, total=False):
    symbols: Required[str]
    """Códigos dos títulos separados por vírgula, até 20.

    Ex.: tesouro-selic-01032031,tesouro-ipca-15052035.
    """

    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """Data final no formato YYYY-MM-DD. Padrão: hoje."""

    sort_by: Annotated[
        Literal["baseDate", "buyRate", "sellRate", "buyPrice", "sellPrice", "basePrice"], PropertyInfo(alias="sortBy")
    ]
    """Campo usado na ordenação da série."""

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """Direção da ordenação."""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """Data inicial no formato YYYY-MM-DD. Padrão: 12 meses antes de hoje."""
