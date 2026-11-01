# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["StockEarningsCalendarParams"]


class StockEarningsCalendarParams(TypedDict, total=False):
    date_status: Annotated[Literal["confirmed", "estimated"], PropertyInfo(alias="dateStatus")]
    """`confirmed` traz datas informadas pela empresa.

    `estimated` traz datas estimadas.
    """

    from_: Annotated[str, PropertyInfo(alias="from")]
    """Data inicial de divulgação.

    Padrão: 7 dias antes de hoje, ou 97 dias antes de `to`. O intervalo máximo é de
    366 dias, ou de 10 anos com `symbols`.
    """

    limit: int
    """Máximo de divulgações por página."""

    page: int
    """Página."""

    status: Literal["scheduled", "published", "overdue"]
    """`scheduled` (prevista), `published` (divulgada) ou `overdue` (atrasada).

    Para mais de uma, separe por vírgula.
    """

    symbols: str
    """Tickers separados por vírgula, de ações ou BDRs.

    Máximo de 20. PETR3 e PETR4 retornam a mesma empresa.
    """

    to: str
    """Data final de divulgação.

    Padrão: 97 dias depois de `from` (90 dias depois de hoje).
    """

    types: Literal["quarterly", "annual"]
    """`quarterly` (trimestral) ou `annual` (anual).

    Para mais de um, separe por vírgula.
    """

    updated_since: Annotated[Union[str, datetime], PropertyInfo(alias="updatedSince", format="iso8601")]
    """Retorna só divulgações alteradas a partir deste momento, em ISO 8601.

    Use para sincronizar sua base.
    """
