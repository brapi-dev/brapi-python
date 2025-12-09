# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["CryptoListAvailableResponse"]


class CryptoListAvailableResponse(BaseModel):
    """Resposta do endpoint que lista todas as criptomoedas disponíveis."""

    coins: Optional[List[str]] = None
    """
    Lista de siglas (tickers) das criptomoedas disponíveis (ex: `BTC`, `ETH`,
    `LTC`).
    """
