# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AvailableListParams"]


class AvailableListParams(TypedDict, total=False):
    search: str
    """Filtrar ações e índices por nome ou código"""
