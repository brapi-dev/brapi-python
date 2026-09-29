# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["StockHistoricalParams"]


class StockHistoricalParams(TypedDict, total=False):
    symbols: Required[str]
    """Tickers separados por vírgula.

    Ex.: PETR4,VALE3. Um ticker antigo é trocado pelo ticker atual.
    """

    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """Data final no formato YYYY-MM-DD."""

    include_raw: Annotated[Literal["true", "false"], PropertyInfo(alias="includeRaw")]
    """
    Inclui os preços originais sem ajuste (`rawOpen`, `rawHigh`, `rawLow`,
    `rawClose`) em intervalos diários. Exige o plano Pro.
    """

    interval: Literal["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
    """Intervalo entre os pontos. Padrão: 1d."""

    range: Literal["1d", "2d", "5d", "7d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]
    """Janela relativa. Padrão: 1mo."""

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """Ordem dos pontos por data."""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """Data inicial no formato YYYY-MM-DD."""
