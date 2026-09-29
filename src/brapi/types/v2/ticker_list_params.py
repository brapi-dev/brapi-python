# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TickerListParams"]


class TickerListParams(TypedDict, total=False):
    limit: int
    """Itens por página. Máximo: 2000."""

    page: int
    """Número da página. Começa em 1."""

    search: str
    """Parte do ticker, do nome da empresa ou de um ticker antigo."""

    sector: str
    """Setor."""

    sort_by: Annotated[
        Literal["symbol", "name", "close", "change", "volume", "marketCap"], PropertyInfo(alias="sortBy")
    ]
    """Campo de ordenação."""

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """Ordem."""

    subsector: str
    """Subsetor."""

    sub_type: Annotated[
        Literal["stock", "unit", "fii", "etf", "fi-infra", "fi-agro", "fip", "fidc", "bdr"],
        PropertyInfo(alias="subType"),
    ]
    """Subtipo do ativo: stock, unit, fii, etf, fi-infra, fi-agro, fip, fidc ou bdr."""

    type: Literal["stock", "fund", "bdr"]
    """Tipo do ativo. Índices não entram neste filtro."""
