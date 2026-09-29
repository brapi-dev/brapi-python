# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FundPortfolioParams"]


class FundPortfolioParams(TypedDict, total=False):
    cnpjs: str
    """CNPJs separados por vírgula, até 20, com ou sem pontuação."""

    include: str
    """Grupos de ativos separados por vírgula. Ex.: publicBonds,creditAssets."""

    limit: int
    """Itens por página."""

    page: int
    """Número da página, a partir de 1."""

    reference_date: Annotated[str, PropertyInfo(alias="referenceDate")]
    """Mês de referência no formato YYYY-MM-DD."""

    symbols: str
    """Tickers separados por vírgula, até 20. Ex.: JURO11,XPCA11."""
