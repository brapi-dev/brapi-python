# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CurrencyHistoricalParams"]


class CurrencyHistoricalParams(TypedDict, total=False):
    currency: Required[str]
    """Pares no formato ORIGEM-DESTINO, separados por vírgula, até 20.

    Ex.: USD-BRL,EUR-BRL.
    """

    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """Data final no formato YYYY-MM-DD. Padrão: hoje."""

    limit: int
    """Máximo de pontos por par. Padrão: 365."""

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """Ordem por data. Padrão: desc."""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """Data inicial no formato YYYY-MM-DD. Padrão: 12 meses atrás."""
