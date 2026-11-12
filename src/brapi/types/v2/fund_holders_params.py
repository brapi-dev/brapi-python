# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FundHoldersParams"]


class FundHoldersParams(TypedDict, total=False):
    asset_type: Annotated[
        Literal["fii", "fiagro", "fiinfra", "fif", "fidc", "fip", "etf", "other"], PropertyInfo(alias="assetType")
    ]
    """Só fundos deste tipo. Ex.: `etf`."""

    cnpj: str
    """CNPJ de um fundo, para ver quais fundos têm cotas dele.

    Use `symbol` ou `cnpj`, não os dois.
    """

    limit: int
    """Fundos por página. Padrão 20, máximo 100."""

    page: int
    """Página, a partir de 1."""

    reference_date: Annotated[str, PropertyInfo(alias="referenceDate")]
    """Data no formato YYYY-MM-DD.

    Traz o mês mais recente até esta data. Sem ela, traz o mês mais recente que a
    maioria dos fundos já entregou.
    """

    sort_by: Annotated[Literal["marketValue", "weightPercent"], PropertyInfo(alias="sortBy")]
    """`marketValue` (padrão) ou `weightPercent`."""

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """Ordem crescente (`asc`) ou decrescente (`desc`, padrão)."""

    symbol: str
    """Ticker do ativo na bolsa. Ex.: PETR4."""
