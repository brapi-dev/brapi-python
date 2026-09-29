# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IndicatorRetrieveParams"]


class IndicatorRetrieveParams(TypedDict, total=False):
    symbols: Required[str]
    """Códigos dos títulos separados por vírgula, até 20.

    Ex.: tesouro-selic-01032031,tesouro-ipca-15052035.
    """
