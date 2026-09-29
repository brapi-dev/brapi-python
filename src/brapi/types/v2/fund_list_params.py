# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FundListParams"]


class FundListParams(TypedDict, total=False):
    asset_type: Annotated[
        Literal["fii", "fiagro", "fiinfra", "fif", "fidc", "fip", "etf", "other"], PropertyInfo(alias="assetType")
    ]
    """Tipo do fundo."""

    cnpjs: str
    """CNPJs separados por vírgula, até 20, com ou sem pontuação."""

    limit: int
    """Itens por página."""

    page: int
    """Número da página, a partir de 1."""

    search: str
    """Texto buscado no ticker, nome, razão social, ISIN ou CNPJ."""

    sort_by: Annotated[str, PropertyInfo(alias="sortBy")]
    """Campo usado na ordenação."""

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """Ordem crescente (`asc`) ou decrescente (`desc`)."""

    status: str
    """Situação do fundo no cadastro."""

    symbols: str
    """Tickers separados por vírgula, até 20. Ex.: JURO11,XPCA11."""
