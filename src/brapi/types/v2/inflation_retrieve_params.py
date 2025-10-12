# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InflationRetrieveParams"]


class InflationRetrieveParams(TypedDict, total=False):
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

    country: str
    """**Opcional.** Nome do país para o qual buscar os dados de inflação.

    Use nomes em minúsculas. O padrão é `brazil`. Consulte
    `/api/v2/inflation/available` para a lista de países suportados.
    """

    end: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    **Opcional.** Data final do período desejado para os dados históricos, no
    formato `DD/MM/YYYY`. Requerido se `start` for especificado.
    """

    historical: bool
    """**Opcional.** Booleano (`true` ou `false`).

    Define se dados históricos devem ser incluídos. O comportamento exato em
    conjunto com `start`/`end` deve ser verificado. Padrão: `false`.
    """

    sort_by: Annotated[Literal["date", "value"], PropertyInfo(alias="sortBy")]
    """**Opcional.** Campo pelo qual os resultados da inflação serão ordenados."""

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """**Opcional.** Direção da ordenação: `asc` (ascendente) ou `desc` (descendente).

    Padrão: `desc`. Requer que `sortBy` seja especificado.
    """

    start: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    **Opcional.** Data de início do período desejado para os dados históricos, no
    formato `DD/MM/YYYY`. Requerido se `end` for especificado.
    """
