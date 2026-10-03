# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["StockProfileParams"]


class StockProfileParams(TypedDict, total=False):
    symbols: Required[str]
    """Tickers separados por vírgula.

    Ex.: PETR4,VALE3. `requestedSymbol` identifica o ticker enviado e `symbol`
    identifica os dados retornados.
    """
