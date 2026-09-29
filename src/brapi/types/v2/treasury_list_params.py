# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TreasuryListParams"]


class TreasuryListParams(TypedDict, total=False):
    coupon_type: Annotated[Literal["zero", "semestral"], PropertyInfo(alias="couponType")]
    """Tipo de cupom do título."""

    indexer: Literal["selic", "prefixado", "ipca", "igpm"]
    """Indexador do título."""

    limit: int
    """Itens por página."""

    page: int
    """Número da página, a partir de 1."""

    search: str
    """Busca por parte do código ou do nome do título. Ex.: tesouro-selic-01032031."""

    sort_by: Annotated[
        Literal[
            "symbol",
            "bondType",
            "maturityDate",
            "durationDays",
            "baseDate",
            "buyRate",
            "sellRate",
            "buyPrice",
            "sellPrice",
            "basePrice",
        ],
        PropertyInfo(alias="sortBy"),
    ]
    """Campo usado na ordenação."""

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """Direção da ordenação."""
