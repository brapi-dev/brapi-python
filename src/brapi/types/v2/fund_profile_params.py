# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FundProfileParams"]


class FundProfileParams(TypedDict, total=False):
    cnpjs: str
    """CNPJs separados por vírgula, até 20, com ou sem pontuação."""

    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """Data final no formato YYYY-MM-DD."""

    include: str

    reference_date: Annotated[str, PropertyInfo(alias="referenceDate")]
    """Mês de referência no formato YYYY-MM-DD."""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """Data inicial no formato YYYY-MM-DD."""

    symbols: str
    """Tickers separados por vírgula, até 20. Ex.: JURO11,XPCA11."""
