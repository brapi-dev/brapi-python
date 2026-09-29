# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CurrencyListAvailableParams"]


class CurrencyListAvailableParams(TypedDict, total=False):
    search: str
    """Texto buscado no par e no nome das moedas."""
