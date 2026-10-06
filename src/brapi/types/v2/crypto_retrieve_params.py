# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CryptoRetrieveParams"]


class CryptoRetrieveParams(TypedDict, total=False):
    coin: str
    """Siglas das criptomoedas, separadas por vírgula. Ex.: BTC,ETH."""

    currency: str
    """Moeda da cotação, como BRL, USD ou EUR. Padrão: BRL."""

    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """Data final inclusiva do histórico diário no formato YYYY-MM-DD. Padrão: hoje."""

    interval: str
    """Intervalo entre os pontos do histórico, como 1h ou 1d. Padrão: 1d."""

    range: str
    """Período do histórico, como 5d, 1mo ou 1y. Padrão: 1mo quando há histórico."""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """Data inicial do histórico diário no formato YYYY-MM-DD. Use sem range."""
