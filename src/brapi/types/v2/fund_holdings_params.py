# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FundHoldingsParams"]


class FundHoldingsParams(TypedDict, total=False):
    asset_class: Annotated[str, PropertyInfo(alias="assetClass")]
    """Classes de ativo separadas por vírgula.

    Filtra só a lista `holdings`; o resumo usa a carteira toda. Ex.: equity,bdr.
    """

    cnpjs: str
    """CNPJs separados por vírgula, até 20, com ou sem pontuação."""

    limit: int
    """Posições por fundo e por página. Padrão 10, máximo 500."""

    look_through: Annotated[Literal["true", "false"], PropertyInfo(alias="lookThrough")]
    """`true` (padrão) abre as cotas de outros fundos e mostra os ativos deles.

    `false` mostra só as posições diretas.
    """

    page: int
    """Página, a partir de 1."""

    reference_date: Annotated[str, PropertyInfo(alias="referenceDate")]
    """Data no formato YYYY-MM-DD.

    Traz o mês mais recente até esta data. Sem ela, traz o mês mais recente.
    """

    symbols: str
    """Tickers separados por vírgula, até 20. Ex.: BOVA11,WRLD11."""
