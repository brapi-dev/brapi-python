# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["InflationListAvailableParams"]


class InflationListAvailableParams(TypedDict, total=False):
    format: Literal["json"]
    """Formato da resposta. JSON é o formato suportado."""
