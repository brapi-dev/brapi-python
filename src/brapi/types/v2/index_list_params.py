# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["IndexListParams"]


class IndexListParams(TypedDict, total=False):
    search: str
    """Busca por parte da sigla ou do nome do índice, ou do ticker do ETF. Ex.: ibov."""
