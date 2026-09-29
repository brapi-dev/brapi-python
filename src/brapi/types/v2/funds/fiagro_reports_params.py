# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["FiagroReportsParams"]


class FiagroReportsParams(TypedDict, total=False):
    all_versions: Annotated[Optional[bool], PropertyInfo(alias="allVersions")]
    """Se `true`, traz todas as versões enviadas à CVM para cada mês."""

    cnpjs: str
    """CNPJs separados por vírgula, até 20, com ou sem pontuação."""

    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """Data final no formato YYYY-MM-DD."""

    limit: int
    """Itens por página."""

    page: int
    """Número da página, a partir de 1."""

    sort_by: Annotated[str, PropertyInfo(alias="sortBy")]
    """Campo usado na ordenação."""

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """Ordem crescente (`asc`) ou decrescente (`desc`)."""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """Data inicial no formato YYYY-MM-DD."""

    symbols: str
    """Tickers separados por vírgula, até 20. Ex.: JURO11,XPCA11."""
