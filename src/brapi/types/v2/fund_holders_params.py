# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FundHoldersParams"]


class FundHoldersParams(TypedDict, total=False):
    asset_class: Annotated[str, PropertyInfo(alias="assetClass")]
    """Só posições destas classes de ativo, separadas por vírgula.

    Ex.: `equity` para só ações de uma empresa.
    """

    asset_type: Annotated[
        Literal["fii", "fiagro", "fiinfra", "fif", "fidc", "fip", "etf", "other"], PropertyInfo(alias="assetType")
    ]
    """Só fundos deste tipo. Ex.: `etf`."""

    cnpj: str
    """
    CNPJ de um fundo, para ver quais fundos têm cotas dele, ou de uma empresa, para
    ver quais fundos têm ações ou dívida dela. Use `symbol` ou `cnpj`, não os dois.
    """

    include: Literal["movers"]
    """
    `movers` traz também `topBuyers` e `topSellers`: os maiores compradores e
    vendedores do mês, até `limit` de cada, na mesma resposta.
    """

    issuer: Literal["true", "false"]
    """
    `true` troca o ticker de `symbol` por todos os ativos da empresa: ações, units,
    debêntures e outros títulos de dívida. Padrão `false`.
    """

    limit: int
    """Fundos por página. Padrão 20, máximo 100."""

    page: int
    """Página, a partir de 1."""

    reference_date: Annotated[str, PropertyInfo(alias="referenceDate")]
    """Data no formato YYYY-MM-DD.

    Traz o mês mais recente até esta data. Sem ela, traz o mês mais recente que a
    maioria dos fundos já entregou.
    """

    sort_by: Annotated[Literal["marketValue", "weightPercent", "bought", "sold"], PropertyInfo(alias="sortBy")]
    """`marketValue` (padrão) ou `weightPercent` listam os fundos que têm o ativo.

    `bought` lista só os fundos que compraram no mês, pelo valor comprado
    (`change.changeValue`). `sold` lista só os que venderam, inclusive os que
    zeraram a posição, pelo valor vendido.
    """

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """Ordem crescente (`asc`) ou decrescente (`desc`, padrão).

    Com `bought` e `sold`, `desc` traz primeiro as maiores compras ou vendas.
    """

    symbol: str
    """Ticker do ativo na bolsa. Ex.: PETR4."""
