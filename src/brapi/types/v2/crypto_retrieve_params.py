# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CryptoRetrieveParams"]


class CryptoRetrieveParams(TypedDict, total=False):
    coin: str
    """Sigla(s) das criptomoedas separadas por vírgula"""

    currency: str
    """Moeda para cotação (padrão: BRL)"""

    interval: str
    """Intervalo dos dados históricos"""

    range: str
    """Período para dados históricos"""
