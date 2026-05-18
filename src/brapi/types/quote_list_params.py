# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["QuoteListParams"]


class QuoteListParams(TypedDict, total=False):
    token: str
    """Token de autenticação (alternativa ao header Authorization)"""

    limit: str
    """Número máximo de resultados"""

    page: str
    """Número da página (paginação)"""

    search: str
    """Termo de busca para filtrar ativos"""

    sector: str
    """Filtrar por setor"""

    sort_by: Annotated[
        Literal["name", "close", "change", "change_abs", "volume", "market_cap_basic"], PropertyInfo(alias="sortBy")
    ]
    """Campo para ordenação"""

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """Ordem de classificação"""

    type: Literal["stock", "fund", "bdr"]
    """Filtrar por tipo de ativo"""
