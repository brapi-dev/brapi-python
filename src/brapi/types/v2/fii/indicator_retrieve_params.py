# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IndicatorRetrieveParams"]


class IndicatorRetrieveParams(TypedDict, total=False):
    symbols: Required[str]
    """Tickers de FIIs separados por vírgula, até 20. Ex.: HGLG11,MXRF11."""
