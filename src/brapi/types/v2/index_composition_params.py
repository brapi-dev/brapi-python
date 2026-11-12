# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IndexCompositionParams"]


class IndexCompositionParams(TypedDict, total=False):
    symbols: Required[str]
    """Índices separados por vírgula, até 20.

    Veja os aceitos em `/api/v2/indexes/list`. Ex.: IBOV,SMLL.
    """

    limit: int
    """Ativos por índice e por página. Padrão 10, máximo 500."""

    page: int
    """Página, a partir de 1."""
