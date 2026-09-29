# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MacroLatestParams"]


class MacroLatestParams(TypedDict, total=False):
    symbols: str
    """Slugs separados por vírgula, até 20.

    Sem valor, devolve todas as séries. Slugs: selic, selicovernight, cdi, tr, ipca,
    ipca12m, inpc, igpm, igpdi, ibcbr, pibmensal, desemprego, m1, m4, reservas.
    """
