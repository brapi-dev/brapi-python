# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CurrencyRetrieveParams"]


class CurrencyRetrieveParams(TypedDict, total=False):
    currency: Required[str]
    """
    **Obrigatório.** Uma lista de um ou mais pares de moedas a serem consultados,
    separados por vírgula (`,`).

    - **Formato:** `MOEDA_ORIGEM-MOEDA_DESTINO` (ex: `USD-BRL`).
    - **Disponibilidade:** Consulte os pares válidos usando o endpoint
      [`/api/v2/currency/available`](#/Moedas/getAvailableCurrencies).
    - **Exemplo:** `USD-BRL,EUR-BRL,BTC-BRL`
    """

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
