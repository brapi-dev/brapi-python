# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["OptionExpirationsParams"]


class OptionExpirationsParams(TypedDict, total=False):
    underlying: Required[str]
    """Código do ativo do futuro. Ex.: `BGI`, `ICF`."""

    include_expired: Annotated[Literal["true", "false"], PropertyInfo(alias="includeExpired")]
    """`true` inclui vencimentos passados. Padrão: `false`, só vencimentos futuros."""
