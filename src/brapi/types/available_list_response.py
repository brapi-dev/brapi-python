# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["AvailableListResponse"]


class AvailableListResponse(BaseModel):
    """Resposta do endpoint que lista todos os tickers disponíveis."""

    indexes: List[str]
    """Lista de tickers de **índices** disponíveis (ex: `^BVSP`, `^IFIX`)."""

    stocks: List[str]
    """
    Lista de tickers de **ações, FIIs, BDRs e ETFs** disponíveis (ex: `PETR4`,
    `VALE3`, `MXRF11`).
    """
