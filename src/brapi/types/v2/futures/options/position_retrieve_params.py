# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["PositionRetrieveParams"]


class PositionRetrieveParams(TypedDict, total=False):
    expiration_date: Required[Annotated[str, PropertyInfo(alias="expirationDate")]]
    """Data de vencimento, no formato YYYY-MM-DD.

    Veja os vencimentos em `/expirations`.
    """

    underlying: Required[str]
    """Código do ativo do futuro. Ex.: `BGI`."""

    date: str
    """Data do pregão, no formato YYYY-MM-DD. Padrão: último pregão disponível."""

    max_strike: Annotated[Optional[float], PropertyInfo(alias="maxStrike")]
    """Strike máximo."""

    min_strike: Annotated[Optional[float], PropertyInfo(alias="minStrike")]
    """Strike mínimo."""

    side: Literal["call", "put"]
    """Filtra por `call` ou `put`. Sem o filtro, retorna os dois."""
