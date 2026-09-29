# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FutureTermStructureParams"]


class FutureTermStructureParams(TypedDict, total=False):
    asset: Required[str]
    """Código do ativo. Ex.: `DI1`, `WIN`, `BGI`."""

    include_expired: Annotated[Literal["true", "false"], PropertyInfo(alias="includeExpired")]
    """`true` inclui contratos vencidos."""
