# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["StockStatisticsParams"]


class StockStatisticsParams(TypedDict, total=False):
    symbols: Required[str]
    """Tickers separados por vírgula.

    Ex.: PETR4,VALE3. `requestedSymbol` identifica o ticker enviado e `symbol`
    identifica os dados retornados.
    """

    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """Data final no formato YYYY-MM-DD. Filtra pela data de encerramento do período."""

    mode: Literal["current", "history"]
    """`current` traz o valor atual. `history` traz a série definida por `period`."""

    period: Literal["annual", "quarterly"]
    """Período de cada linha: anual ou trimestral."""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """Data inicial no formato YYYY-MM-DD.

    Filtra pela data de encerramento do período.
    """
