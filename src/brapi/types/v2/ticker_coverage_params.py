# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TickerCoverageParams"]


class TickerCoverageParams(TypedDict, total=False):
    symbols: Required[str]
    """Tickers separados por vírgula, até 20."""
