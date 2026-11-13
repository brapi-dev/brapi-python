# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["StockOwnershipNetworkParams"]


class StockOwnershipNetworkParams(TypedDict, total=False):
    depth: int
    """Passos a partir do ticker, para cima e para baixo."""

    include_persons: Annotated[Literal["true", "false"], PropertyInfo(alias="includePersons")]
    """Inclui pessoas físicas. Padrão: true com ticker, false na rede do mercado."""

    limit: int
    """Máximo de participantes (com ticker) ou de ligações (mercado)."""

    min_percent: Annotated[Optional[float], PropertyInfo(alias="minPercent")]
    """Participação mínima, em % do total ou do voto.

    Com ticker, controladores entram sempre.
    """

    symbol: str
    """Ticker do centro da rede. Sem ticker, a resposta traz a rede do mercado."""
