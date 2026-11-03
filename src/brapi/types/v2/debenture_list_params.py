# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DebentureListParams"]


class DebentureListParams(TypedDict, total=False):
    cnpjs: str
    """CNPJs das empresas emissoras separados por vírgula, com ou sem pontuação.

    Máximo de 20.
    """

    incentivized: Literal["true", "false"]
    """
    `true` traz só debêntures incentivadas (Lei 12.431), com benefício de imposto de
    renda.
    """

    index: Literal["di", "ipca", "pre", "igp-m", "inpc", "tr", "usd", "eur", "none"]
    """Indexador.

    Para mais de um, separe por vírgula. `pre` é prefixado, `none` é sem indexador.
    """

    limit: int
    """Máximo de debêntures por página."""

    maturity_from: Annotated[str, PropertyInfo(alias="maturityFrom")]
    """Vencimento a partir desta data."""

    maturity_to: Annotated[str, PropertyInfo(alias="maturityTo")]
    """Vencimento até esta data."""

    page: int
    """Página."""

    search: str
    """Busca pelo código da debênture ou pelo nome da emissora.

    Cada palavra deve estar no início do código ou de uma palavra do nome.
    """

    sort_by: Annotated[Literal["symbol", "maturityDate", "issueDate"], PropertyInfo(alias="sortBy")]
    """Campo de ordenação."""

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """Ordem crescente (`asc`) ou decrescente (`desc`)."""

    status: Literal["active", "inactive"]
    """`active` (em circulação) ou `inactive` (vencida, resgatada ou cancelada).

    Padrão: `active`, ou as duas quando `symbols` é informado.
    """

    symbols: str
    """Códigos das debêntures separados por vírgula. Máximo de 20."""
