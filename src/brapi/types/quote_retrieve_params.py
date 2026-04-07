# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["QuoteRetrieveParams"]


class QuoteRetrieveParams(TypedDict, total=False):
    token: str
    """Token de autenticação (alternativa ao header Authorization)"""

    dividends: Literal["true", "false"]
    """Incluir histórico de dividendos e JCP"""

    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """Data final para dados históricos (formato YYYY-MM-DD)"""

    interval: Literal["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
    """Intervalo/granularidade dos dados históricos"""

    modules: str
    """Módulos de dados adicionais separados por vírgula"""

    range: Literal["1d", "2d", "5d", "7d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]
    """Período para dados históricos de preço"""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """Data inicial para dados históricos (formato YYYY-MM-DD)"""
