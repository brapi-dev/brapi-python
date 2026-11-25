# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CrowdingRetrieveParams"]


class CrowdingRetrieveParams(TypedDict, total=False):
    limit: int
    """Empresas por página. Padrão 20, máximo 500."""

    page: int
    """Página, a partir de 1."""

    reference_date: Annotated[str, PropertyInfo(alias="referenceDate")]
    """Data no formato YYYY-MM-DD.

    Traz o mês mais recente até esta data. Sem ela, traz o mês mais recente que a
    maioria dos fundos já entregou.
    """

    region: Literal["all", "brazil", "foreign"]
    """`all` (padrão): todas as empresas.

    `brazil`: empresas da B3. `foreign`: empresas do exterior, por BDRs, ações no
    exterior e fundos do exterior.
    """

    sort_by: Annotated[Literal["value", "flow", "funds"], PropertyInfo(alias="sortBy")]
    """`value` (padrão): dinheiro dos fundos.

    `flow`: saldo do mês (com `sortOrder=asc`, as maiores vendas). `funds`: número
    de fundos com posição direta.
    """

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """Ordem: `desc` (padrão) ou `asc`."""
