# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FutureQuoteParams"]


class FutureQuoteParams(TypedDict, total=False):
    symbols: Required[str]
    """Contratos separados por vírgula, até 20. Ex.: WINM26,DI1F27."""
