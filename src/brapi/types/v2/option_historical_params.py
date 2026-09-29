# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["OptionHistoricalParams"]


class OptionHistoricalParams(TypedDict, total=False):
    expiration_date: Required[Annotated[str, PropertyInfo(alias="expirationDate")]]
    """Data de vencimento da série, no formato YYYY-MM-DD."""

    symbol: Required[str]
    """Código da série de opção."""

    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """Data final, no formato YYYY-MM-DD. Padrão: hoje."""

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """
    Ordem por data: `asc` do mais antigo ao mais recente, `desc` do mais recente ao
    mais antigo.
    """

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """Data inicial, no formato YYYY-MM-DD. Padrão: 12 meses atrás."""

    strike: Optional[float]
    """Preço de exercício.

    Use quando o mesmo `symbol` aparece mais de uma vez no vencimento.
    """
