# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["FiagroPortfolioParams"]


class FiagroPortfolioParams(TypedDict, total=False):
    all_versions: Annotated[Optional[bool], PropertyInfo(alias="allVersions")]
    """Se `true`, traz todas as versões enviadas à CVM para cada mês."""

    cnpjs: str
    """CNPJs separados por vírgula, até 20, com ou sem pontuação."""

    include: str

    reference_date: Annotated[str, PropertyInfo(alias="referenceDate")]
    """Mês de referência no formato YYYY-MM-DD."""

    symbols: str
    """Tickers separados por vírgula, até 20. Ex.: JURO11,XPCA11."""
