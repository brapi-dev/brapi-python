# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TickerRenamesParams"]


class TickerRenamesParams(TypedDict, total=False):
    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """Data efetiva final no formato YYYY-MM-DD."""

    search: str
    """Parte do ticker antigo, do novo ou do atual."""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """Data efetiva inicial no formato YYYY-MM-DD."""

    symbols: str
    """Tickers separados por vírgula, até 20.

    Traz renomes em que algum deles é o ticker antigo, o novo ou o atual.
    """
