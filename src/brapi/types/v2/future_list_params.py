# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FutureListParams"]


class FutureListParams(TypedDict, total=False):
    asset: str
    """Código do ativo. Ex.: `WIN`, `BGI`, `DI1`."""

    include_expired: Annotated[Literal["true", "false"], PropertyInfo(alias="includeExpired")]
    """`true` inclui contratos vencidos."""

    limit: int
    """Itens por página. Máximo: 100."""

    page: int
    """Número da página, a partir de 1."""

    segment: Literal["financial", "agribusiness"]
    """Segmento do contrato."""

    sort_by: Annotated[Literal["symbol", "expirationDate", "underlyingAsset"], PropertyInfo(alias="sortBy")]
    """Campo usado na ordenação."""

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """Direção da ordenação."""
