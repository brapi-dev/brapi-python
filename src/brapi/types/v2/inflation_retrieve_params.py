# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InflationRetrieveParams"]


class InflationRetrieveParams(TypedDict, total=False):
    end: str
    """Data final no formato DD/MM/YYYY. Padrão: hoje."""

    historical: str
    """true devolve a série desde 01/01/2000.

    Sem datas e sem este parâmetro, devolve os últimos 12 meses.
    """

    sort_by: Annotated[str, PropertyInfo(alias="sortBy")]
    """Campo de ordenação: date ou value. Padrão: date."""

    sort_order: Annotated[str, PropertyInfo(alias="sortOrder")]
    """Ordem: asc ou desc. Padrão: desc."""

    start: str
    """Data inicial no formato DD/MM/YYYY."""
