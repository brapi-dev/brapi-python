# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["HoldingHistoryParams"]


class HoldingHistoryParams(TypedDict, total=False):
    asset: str
    """Ticker do ativo na bolsa. Ex.: PETR4."""

    asset_cnpj: Annotated[str, PropertyInfo(alias="assetCnpj")]
    """
    CNPJ de um fundo, para as cotas dele, ou de uma empresa, para as ações e a
    dívida dela. Use `asset` ou `assetCnpj`, não os dois.
    """

    cnpj: str
    """CNPJ do fundo, com ou sem pontuação. Use `symbol` ou `cnpj`, não os dois."""

    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """Data final no formato YYYY-MM-DD. Padrão: hoje."""

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """Do mês mais antigo (`asc`) ou do mais recente (`desc`, padrão)."""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """Data inicial no formato YYYY-MM-DD. Padrão: 24 meses antes de `endDate`."""

    symbol: str
    """Ticker do fundo. Ex.: BOVA11."""
