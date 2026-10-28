# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FundScreenerCnpjParams"]


class FundScreenerCnpjParams(TypedDict, total=False):
    anbima_classification: Annotated[str, PropertyInfo(alias="anbimaClassification")]
    """Parte da classificação ANBIMA, sem diferença de maiúsculas e acentos.

    Exemplos: Previdência, Exterior, Crédito Livre.
    """

    classification: Literal["renda-fixa", "multimercado", "acoes", "cambial", "fmp-fgts"]
    """Classe do fundo na CVM: renda-fixa, multimercado, acoes, cambial ou fmp-fgts."""

    equity_max: Annotated[float, PropertyInfo(alias="equityMax")]
    """Patrimônio líquido: valor máximo, inclusive. Unidade: reais."""

    equity_min: Annotated[float, PropertyInfo(alias="equityMin")]
    """Patrimônio líquido: valor mínimo, inclusive. Unidade: reais."""

    limit: int
    """Itens por página. Máximo: 200."""

    manager: str
    """Parte do nome do gestor, sem diferença de maiúsculas e acentos."""

    nav_per_share_max: Annotated[float, PropertyInfo(alias="navPerShareMax")]
    """Valor da cota: valor máximo, inclusive. Unidade: reais."""

    nav_per_share_min: Annotated[float, PropertyInfo(alias="navPerShareMin")]
    """Valor da cota: valor mínimo, inclusive. Unidade: reais."""

    net_flow1m_max: Annotated[float, PropertyInfo(alias="netFlow1mMax")]
    """Captação líquida em 1 mês: valor máximo, inclusive. Unidade: reais."""

    net_flow1m_min: Annotated[float, PropertyInfo(alias="netFlow1mMin")]
    """Captação líquida em 1 mês: valor mínimo, inclusive. Unidade: reais."""

    page: int
    """Número da página. Começa em 1."""

    return12m_max: Annotated[float, PropertyInfo(alias="return12mMax")]
    """Rentabilidade em 12 meses: valor máximo, inclusive.

    Unidade: fração (0.06 = 6%).
    """

    return12m_min: Annotated[float, PropertyInfo(alias="return12mMin")]
    """Rentabilidade em 12 meses: valor mínimo, inclusive.

    Unidade: fração (0.06 = 6%).
    """

    return1m_max: Annotated[float, PropertyInfo(alias="return1mMax")]
    """Rentabilidade em 1 mês: valor máximo, inclusive. Unidade: fração (0.06 = 6%)."""

    return1m_min: Annotated[float, PropertyInfo(alias="return1mMin")]
    """Rentabilidade em 1 mês: valor mínimo, inclusive. Unidade: fração (0.06 = 6%)."""

    return36m_max: Annotated[float, PropertyInfo(alias="return36mMax")]
    """Rentabilidade em 36 meses: valor máximo, inclusive.

    Unidade: fração (0.06 = 6%).
    """

    return36m_min: Annotated[float, PropertyInfo(alias="return36mMin")]
    """Rentabilidade em 36 meses: valor mínimo, inclusive.

    Unidade: fração (0.06 = 6%).
    """

    return_day_max: Annotated[float, PropertyInfo(alias="returnDayMax")]
    """Variação no dia: valor máximo, inclusive. Unidade: fração (0.06 = 6%)."""

    return_day_min: Annotated[float, PropertyInfo(alias="returnDayMin")]
    """Variação no dia: valor mínimo, inclusive. Unidade: fração (0.06 = 6%)."""

    return_ytd_max: Annotated[float, PropertyInfo(alias="returnYtdMax")]
    """Rentabilidade no ano: valor máximo, inclusive. Unidade: fração (0.06 = 6%)."""

    return_ytd_min: Annotated[float, PropertyInfo(alias="returnYtdMin")]
    """Rentabilidade no ano: valor mínimo, inclusive. Unidade: fração (0.06 = 6%)."""

    search: str
    """Parte do nome ou da razão social do fundo, sem diferença de maiúsculas e
    acentos.

    Números, com ou sem pontuação, buscam o início do CNPJ.
    """

    sort_by: Annotated[
        Literal[
            "name",
            "cnpj",
            "navPerShare",
            "returnDay",
            "return1m",
            "returnYtd",
            "return12m",
            "return36m",
            "equity",
            "totalInvestors",
            "netFlow1m",
        ],
        PropertyInfo(alias="sortBy"),
    ]
    """Campo de ordenação: uma chave de indicador, `name` ou `cnpj`.

    Padrão: `equity`. Valores nulos ficam no fim.
    """

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """Ordem. Padrão: `desc`."""

    total_investors_max: Annotated[float, PropertyInfo(alias="totalInvestorsMax")]
    """Cotistas: valor máximo, inclusive. Unidade: quantidade."""

    total_investors_min: Annotated[float, PropertyInfo(alias="totalInvestorsMin")]
    """Cotistas: valor mínimo, inclusive. Unidade: quantidade."""
