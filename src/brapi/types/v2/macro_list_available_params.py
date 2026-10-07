# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MacroListAvailableParams"]


class MacroListAvailableParams(TypedDict, total=False):
    category: str
    """
    Categoria da série: `interestRate`, `inflation`, `monetary`, `activity`,
    `labor`, `external`.
    """

    q: str
    """Texto buscado no código, nome alternativo, nome e descrição.

    Ignora maiúsculas e aceita parte da palavra.
    """
