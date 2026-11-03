# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DebentureProfileParams"]


class DebentureProfileParams(TypedDict, total=False):
    symbols: Required[str]
    """Códigos das debêntures separados por vírgula. Máximo de 20."""
