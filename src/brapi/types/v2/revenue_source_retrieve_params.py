# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RevenueSourceRetrieveParams"]


class RevenueSourceRetrieveParams(TypedDict, total=False):
    cnpjs: str
    """CNPJs de fundos separados por vírgula, com ou sem pontuação.

    Use para fundos sem ticker.
    """

    end_year: Annotated[int, PropertyInfo(alias="endYear")]
    """Último exercício social. Padrão: o mais recente disponível."""

    period: Literal["annual", "quarterly"]
    """`annual` (padrão): exercícios em `years`.

    `quarterly`: trimestres em `quarters`, com a receita acumulada no ano e a
    receita dos 3 meses. Só para empresas da B3 com exercício de janeiro a dezembro.
    """

    start_year: Annotated[int, PropertyInfo(alias="startYear")]
    """Primeiro exercício social. Padrão: o mais antigo disponível."""

    symbols: str
    """Tickers separados por vírgula: ações, BDRs, FIIs, Fiagros ou ETFs.

    Máximo de 20. PETR3 e PETR4 retornam a mesma empresa.
    """
