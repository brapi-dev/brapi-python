# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["QuoteRetrieveParams"]


class QuoteRetrieveParams(TypedDict, total=False):
    token: str
    """Token de acesso. Use no lugar do header `Authorization`."""

    dividends: Literal["true", "false"]
    """Inclui `dividendsData` com dividendos, JCP e eventos em ações."""

    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """Data final da série de preços no formato YYYY-MM-DD."""

    include_raw: Annotated[Literal["true", "false"], PropertyInfo(alias="includeRaw")]
    """
    Inclui os preços originais sem ajuste (`rawOpen`, `rawHigh`, `rawLow`,
    `rawClose`) em intervalos diários. Exige o plano Pro.
    """

    interval: Literal["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
    """Intervalo entre os pontos da série de preços."""

    modules: str
    """Módulos extras separados por vírgula."""

    range: Literal["1d", "2d", "5d", "7d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]
    """Janela relativa da série de preços."""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """Data inicial da série de preços no formato YYYY-MM-DD."""
