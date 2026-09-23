# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["QuoteListParams"]


class QuoteListParams(TypedDict, total=False):
    token: str
    """Token de acesso. Use no lugar do header `Authorization`."""

    limit: str
    """Itens por página.

    Máximo: 2000. Sem este parâmetro, a resposta traz até 2000 itens e não traz
    paginação.
    """

    page: str
    """Número da página. Começa em 1."""

    search: str
    """Parte do ticker ou do nome da empresa."""

    sector: str
    """Setor."""

    sort_by: Annotated[
        Literal["name", "close", "change", "change_abs", "volume", "market_cap_basic"], PropertyInfo(alias="sortBy")
    ]
    """Campo de ordenação. Padrão: volume."""

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """Ordem. Padrão: desc."""

    subsector: str
    """Subsetor."""

    sub_type: Annotated[
        Literal["stock", "unit", "fii", "etf", "fi-infra", "fi-agro", "fip", "fidc", "bdr"],
        PropertyInfo(alias="subType"),
    ]
    """Subtipo do ativo: stock, unit, fii, etf, fi-infra, fi-agro, fip, fidc ou bdr."""

    type: Literal["stock", "fund", "bdr"]
    """Tipo do ativo."""
