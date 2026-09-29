# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DictionaryRetrieveParams"]


class DictionaryRetrieveParams(TypedDict, total=False):
    category: str
    """Categoria exata do campo. Ex.: fii, treasury, quote, balance-sheet."""

    search: str
    """Texto buscado em key, label, description, category e endpoints.

    Ignora maiúsculas.
    """
