# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CryptoRetrieveParams"]


class CryptoRetrieveParams(TypedDict, total=False):
    coin: str
    """Siglas das criptomoedas, separadas por vírgula. Ex.: BTC,ETH."""

    currency: str
    """Moeda da cotação, como BRL, USD ou EUR. Padrão: BRL."""

    interval: str
    """Intervalo entre os pontos do histórico, como 1h ou 1d. Padrão: 1d."""

    range: str
    """Período do histórico, como 5d, 1mo ou 1y. Padrão: 1mo quando há histórico."""
