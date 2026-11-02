# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RevenueSourceCompareParams"]


class RevenueSourceCompareParams(TypedDict, total=False):
    activity: Required[str]
    """Código da atividade.

    Inclui as atividades filhas. Veja os códigos em
    `/api/v2/revenue-sources/activities`.
    """

    end_year: Annotated[int, PropertyInfo(alias="endYear")]
    """Último exercício social. Padrão: o mais recente disponível."""

    start_year: Annotated[int, PropertyInfo(alias="startYear")]
    """Primeiro exercício social. Padrão: o mais antigo disponível."""
