# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["PropertyRetrieveParams"]


class PropertyRetrieveParams(TypedDict, total=False):
    symbols: Required[str]
    """Tickers de FIIs separados por vírgula, até 20. Ex.: HGLG11,MXRF11."""

    all_versions: Annotated[Literal["true", "false"], PropertyInfo(alias="allVersions")]
    """true inclui todas as versões do trimestre. false retorna só a mais recente."""

    reference_date: Annotated[str, PropertyInfo(alias="referenceDate")]
    """Fim do trimestre no formato YYYY-MM-DD.

    Sem valor, retorna o trimestre mais recente de cada FII.
    """

    sort_by: Annotated[Literal["revenueShare", "area", "vacancyRate", "name"], PropertyInfo(alias="sortBy")]
    """Campo de ordenação dos imóveis."""

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """Direção da ordenação dos imóveis."""
