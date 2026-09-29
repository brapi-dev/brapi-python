# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MacroRetrieveParams"]


class MacroRetrieveParams(TypedDict, total=False):
    symbols: Required[str]
    """Slugs separados por vírgula, até 20.

    Slugs por categoria: interestRate: `selic`, `selicovernight`, `cdi`, `tr`;
    inflation: `ipca`, `ipca12m`, `inpc`, `igpm`, `igpdi`; activity: `ibcbr`,
    `pibmensal`; labor: `desemprego`; monetary: `m1`, `m4`; external: `reservas`.
    """

    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """Data final no formato YYYY-MM-DD. Padrão: hoje."""

    limit: int
    """Máximo de observações por série. Padrão: 20. Não há teto."""

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """Ordem por data."""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """Data inicial no formato YYYY-MM-DD. Padrão: 12 meses atrás."""
