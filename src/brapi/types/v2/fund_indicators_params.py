# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FundIndicatorsParams"]


class FundIndicatorsParams(TypedDict, total=False):
    asset_type: Annotated[
        Literal["fii", "fiagro", "fiinfra", "fif", "fidc", "fip", "etf", "other"], PropertyInfo(alias="assetType")
    ]
    """Tipo do fundo."""

    cnpjs: str
    """CNPJs separados por vírgula, até 20, com ou sem pontuação."""

    symbols: str
    """Tickers separados por vírgula, até 20. Ex.: JURO11,XPCA11."""
