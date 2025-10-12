# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PrimeRateRetrieveParams"]


class PrimeRateRetrieveParams(TypedDict, total=False):
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
    """
    **Opcional.** O país do qual você deseja obter informações sobre a taxa básica
    de juros. Por padrão, o país é definido como brazil. Você pode consultar a lista
    de países disponíveis através do endpoint `/api/v2/prime-rate/available`.
    """

    end: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """**Opcional.** Data final do período para busca no formato DD/MM/YYYY.

    Por padrão é a data atual. Útil quando `historical=true` para restringir o
    período da série histórica.
    """

    historical: bool
    """**Opcional.** Define se os dados históricos serão retornados.

    Se definido como `true`, retorna a série histórica completa. Se `false` (padrão)
    ou omitido, retorna apenas o valor mais recente.
    """

    sort_by: Annotated[Literal["date", "value"], PropertyInfo(alias="sortBy")]
    """**Opcional.** Campo pelo qual os resultados serão ordenados.

    Por padrão, ordena por `date` (data).
    """

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """
    **Opcional.** Define se a ordenação será crescente (`asc`) ou decrescente
    (`desc`). Por padrão, é `desc` (decrescente).
    """

    start: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """**Opcional.** Data inicial do período para busca no formato DD/MM/YYYY.

    Útil quando `historical=true` para restringir o período da série histórica.
    """
