# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["StockShareholdersParams"]


class StockShareholdersParams(TypedDict, total=False):
    symbols: Required[str]
    """Tickers separados por vírgula. Máximo de 20."""
