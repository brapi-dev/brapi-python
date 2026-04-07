# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CurrencyRetrieveParams"]


class CurrencyRetrieveParams(TypedDict, total=False):
    currency: str
    """Par(es) de moedas separados por vírgula (ex: USD-BRL,EUR-BRL)"""
