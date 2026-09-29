# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["StockDividendsParams"]


class StockDividendsParams(TypedDict, total=False):
    symbols: Required[str]
    """Tickers separados por vírgula.

    Ex.: PETR4,VALE3. Um ticker antigo é trocado pelo ticker atual.
    """

    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """Data final no formato YYYY-MM-DD.

    Filtra proventos em dinheiro por `paymentDate` e eventos em ações por
    `lastDatePrior`.
    """

    include_raw: Annotated[Literal["true", "false"], PropertyInfo(alias="includeRaw")]
    """Inclui `rawRate`, o valor por ação na escala dos preços sem ajuste.

    Exige o plano Pro.
    """

    sort_by: Annotated[Literal["paymentDate", "lastDatePrior", "approvedOn", "rate"], PropertyInfo(alias="sortBy")]
    """Campo de ordenação dos eventos."""

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """Ordem dos eventos."""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """Data inicial no formato YYYY-MM-DD.

    Filtra proventos em dinheiro por `paymentDate` e eventos em ações por
    `lastDatePrior`.
    """
