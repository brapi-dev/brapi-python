# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["QuoteListParams"]


class QuoteListParams(TypedDict, total=False):
    token: str
    """
    **Obrigatório caso não esteja adicionado como header "Authorization".** Seu
    token de autenticação pessoal da API Brapi.

    **Formas de Envio:**

    1.  **Query Parameter:** Adicione `?token=SEU_TOKEN` ao final da URL.
    2.  **HTTP Header:** Inclua o header `Authorization: Bearer SEU_TOKEN` na sua
        requisição.

    Ambos os métodos são aceitos, mas pelo menos um deles deve ser utilizado.
    Obtenha seu token em [brapi.dev/dashboard](https://brapi.dev/dashboard).
    """

    limit: int
    """**Opcional.** Número máximo de ativos a serem retornados por página.

    O valor padrão pode variar.
    """

    page: int
    """
    **Opcional.** Número da página dos resultados a ser retornada, considerando o
    `limit` especificado. Começa em 1.
    """

    search: str
    """**Opcional.** Termo para buscar ativos por ticker (correspondência parcial).

    Ex: `PETR` encontrará `PETR4`, `PETR3`.
    """

    sector: Literal[
        "Retail Trade",
        "Energy Minerals",
        "Health Services",
        "Utilities",
        "Finance",
        "Consumer Services",
        "Consumer Non-Durables",
        "Non-Energy Minerals",
        "Commercial Services",
        "Distribution Services",
        "Transportation",
        "Technology Services",
        "Process Industries",
        "Communications",
        "Producer Manufacturing",
        "Miscellaneous",
        "Electronic Technology",
        "Industrial Services",
        "Health Technology",
        "Consumer Durables",
    ]
    """**Opcional.** Filtra os resultados por setor de atuação da empresa.

    Utilize um dos valores retornados em `availableSectors`.
    """

    sort_by: Annotated[
        Literal["name", "close", "change", "change_abs", "volume", "market_cap_basic", "sector"],
        PropertyInfo(alias="sortBy"),
    ]
    """**Opcional.** Campo pelo qual os resultados serão ordenados."""

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """**Opcional.** Direção da ordenação: `asc` (ascendente) ou `desc` (descendente).

    Requer que `sortBy` seja especificado.
    """

    type: Literal["stock", "fund", "bdr"]
    """**Opcional.** Filtra os resultados por tipo de ativo."""
