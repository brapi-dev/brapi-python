# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["StockCashFlowParams"]


class StockCashFlowParams(TypedDict, total=False):
    symbols: Required[str]
    """Tickers separados por vírgula.

    Ex.: PETR4,VALE3. Um ticker antigo é trocado pelo ticker atual.
    """

    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """Data final no formato YYYY-MM-DD. Filtra pela data de encerramento do período."""

    period: Literal["annual", "quarterly"]
    """Período de cada linha: anual ou trimestral."""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """Data inicial no formato YYYY-MM-DD.

    Filtra pela data de encerramento do período.
    """
