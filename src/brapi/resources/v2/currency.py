# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v2 import currency_retrieve_params, currency_list_available_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v2.currency_retrieve_response import CurrencyRetrieveResponse
from ...types.v2.currency_list_available_response import CurrencyListAvailableResponse

__all__ = ["CurrencyResource", "AsyncCurrencyResource"]


class CurrencyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CurrencyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/brapi-python#accessing-raw-response-data-eg-headers
        """
        return CurrencyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CurrencyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/brapi-python#with_streaming_response
        """
        return CurrencyResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        currency: str,
        token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencyRetrieveResponse:
        """
        Obtenha cotações atualizadas para um ou mais pares de moedas fiduciárias (ex:
        USD-BRL, EUR-USD).

        ### Funcionalidades:

        - **Cotação Múltipla:** Consulte vários pares de moedas em uma única requisição
          usando o parâmetro `currency`.
        - **Dados Retornados:** Inclui nome do par, preços de compra (bid) e venda
          (ask), variação, máximas e mínimas, e timestamp da atualização.

        ### Parâmetros:

        - **`currency` (Obrigatório):** Uma lista de pares de moedas separados por
          vírgula, no formato `MOEDA_ORIGEM-MOEDA_DESTINO` (ex: `USD-BRL`, `EUR-USD`).
          Consulte os pares disponíveis em
          [`/api/v2/currency/available`](#/Moedas/getAvailableCurrencies).
        - **`token` (Obrigatório):** Seu token de autenticação.

        ### Autenticação:

        Requer token de autenticação válido via `token` (query) ou `Authorization`
        (header).

        Args:
          currency: **Obrigatório.** Uma lista de um ou mais pares de moedas a serem consultados,
              separados por vírgula (`,`).

              - **Formato:** `MOEDA_ORIGEM-MOEDA_DESTINO` (ex: `USD-BRL`).
              - **Disponibilidade:** Consulte os pares válidos usando o endpoint
                [`/api/v2/currency/available`](#/Moedas/getAvailableCurrencies).
              - **Exemplo:** `USD-BRL,EUR-BRL,BTC-BRL`

          token: **Obrigatório caso não esteja adicionado como header "Authorization".** Seu
              token de autenticação pessoal da API Brapi.

              **Formas de Envio:**

              1.  **Query Parameter:** Adicione `?token=SEU_TOKEN` ao final da URL.
              2.  **HTTP Header:** Inclua o header `Authorization: Bearer SEU_TOKEN` na sua
                  requisição.

              Ambos os métodos são aceitos, mas pelo menos um deles deve ser utilizado.
              Obtenha seu token em [brapi.dev/dashboard](https://brapi.dev/dashboard).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/currency",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "currency": currency,
                        "token": token,
                    },
                    currency_retrieve_params.CurrencyRetrieveParams,
                ),
            ),
            cast_to=CurrencyRetrieveResponse,
        )

    def list_available(
        self,
        *,
        token: str | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencyListAvailableResponse:
        """
        Obtenha a lista completa de todas as moedas fiduciárias suportadas pela API,
        geralmente utilizadas no parâmetro `currency` de outros endpoints (como o de
        criptomoedas) ou para futuras funcionalidades de conversão.

        ### Funcionalidade:

        - Retorna um array `currencies` com os nomes das moedas.
        - Pode ser filtrado usando o parâmetro `search`.

        ### Autenticação:

        Requer token de autenticação via `token` (query) ou `Authorization` (header).

        ### Exemplo de Requisição:

        **Listar todas as moedas disponíveis:**

        ```bash
        curl -X GET "https://brapi.dev/api/v2/currency/available?token=SEU_TOKEN"
        ```

        **Buscar moedas cujo nome contenha 'Euro':**

        ```bash
        curl -X GET "https://brapi.dev/api/v2/currency/available?search=Euro&token=SEU_TOKEN"
        ```

        ### Resposta:

        A resposta é um objeto JSON com a chave `currencies`, contendo um array de
        objetos. Cada objeto possui uma chave `currency` com o nome completo da moeda
        (ex: `"Dólar Americano/Real Brasileiro"`). **Nota:** O formato do nome pode
        indicar um par de moedas, dependendo do contexto interno da API.

        Args:
          token: **Obrigatório caso não esteja adicionado como header "Authorization".** Seu
              token de autenticação pessoal da API Brapi.

              **Formas de Envio:**

              1.  **Query Parameter:** Adicione `?token=SEU_TOKEN` ao final da URL.
              2.  **HTTP Header:** Inclua o header `Authorization: Bearer SEU_TOKEN` na sua
                  requisição.

              Ambos os métodos são aceitos, mas pelo menos um deles deve ser utilizado.
              Obtenha seu token em [brapi.dev/dashboard](https://brapi.dev/dashboard).

          search: **Opcional.** Termo para filtrar a lista pelo nome da moeda (correspondência
              parcial, case-insensitive).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/currency/available",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "token": token,
                        "search": search,
                    },
                    currency_list_available_params.CurrencyListAvailableParams,
                ),
            ),
            cast_to=CurrencyListAvailableResponse,
        )


class AsyncCurrencyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCurrencyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCurrencyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCurrencyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/brapi-python#with_streaming_response
        """
        return AsyncCurrencyResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        currency: str,
        token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencyRetrieveResponse:
        """
        Obtenha cotações atualizadas para um ou mais pares de moedas fiduciárias (ex:
        USD-BRL, EUR-USD).

        ### Funcionalidades:

        - **Cotação Múltipla:** Consulte vários pares de moedas em uma única requisição
          usando o parâmetro `currency`.
        - **Dados Retornados:** Inclui nome do par, preços de compra (bid) e venda
          (ask), variação, máximas e mínimas, e timestamp da atualização.

        ### Parâmetros:

        - **`currency` (Obrigatório):** Uma lista de pares de moedas separados por
          vírgula, no formato `MOEDA_ORIGEM-MOEDA_DESTINO` (ex: `USD-BRL`, `EUR-USD`).
          Consulte os pares disponíveis em
          [`/api/v2/currency/available`](#/Moedas/getAvailableCurrencies).
        - **`token` (Obrigatório):** Seu token de autenticação.

        ### Autenticação:

        Requer token de autenticação válido via `token` (query) ou `Authorization`
        (header).

        Args:
          currency: **Obrigatório.** Uma lista de um ou mais pares de moedas a serem consultados,
              separados por vírgula (`,`).

              - **Formato:** `MOEDA_ORIGEM-MOEDA_DESTINO` (ex: `USD-BRL`).
              - **Disponibilidade:** Consulte os pares válidos usando o endpoint
                [`/api/v2/currency/available`](#/Moedas/getAvailableCurrencies).
              - **Exemplo:** `USD-BRL,EUR-BRL,BTC-BRL`

          token: **Obrigatório caso não esteja adicionado como header "Authorization".** Seu
              token de autenticação pessoal da API Brapi.

              **Formas de Envio:**

              1.  **Query Parameter:** Adicione `?token=SEU_TOKEN` ao final da URL.
              2.  **HTTP Header:** Inclua o header `Authorization: Bearer SEU_TOKEN` na sua
                  requisição.

              Ambos os métodos são aceitos, mas pelo menos um deles deve ser utilizado.
              Obtenha seu token em [brapi.dev/dashboard](https://brapi.dev/dashboard).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/currency",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "currency": currency,
                        "token": token,
                    },
                    currency_retrieve_params.CurrencyRetrieveParams,
                ),
            ),
            cast_to=CurrencyRetrieveResponse,
        )

    async def list_available(
        self,
        *,
        token: str | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencyListAvailableResponse:
        """
        Obtenha a lista completa de todas as moedas fiduciárias suportadas pela API,
        geralmente utilizadas no parâmetro `currency` de outros endpoints (como o de
        criptomoedas) ou para futuras funcionalidades de conversão.

        ### Funcionalidade:

        - Retorna um array `currencies` com os nomes das moedas.
        - Pode ser filtrado usando o parâmetro `search`.

        ### Autenticação:

        Requer token de autenticação via `token` (query) ou `Authorization` (header).

        ### Exemplo de Requisição:

        **Listar todas as moedas disponíveis:**

        ```bash
        curl -X GET "https://brapi.dev/api/v2/currency/available?token=SEU_TOKEN"
        ```

        **Buscar moedas cujo nome contenha 'Euro':**

        ```bash
        curl -X GET "https://brapi.dev/api/v2/currency/available?search=Euro&token=SEU_TOKEN"
        ```

        ### Resposta:

        A resposta é um objeto JSON com a chave `currencies`, contendo um array de
        objetos. Cada objeto possui uma chave `currency` com o nome completo da moeda
        (ex: `"Dólar Americano/Real Brasileiro"`). **Nota:** O formato do nome pode
        indicar um par de moedas, dependendo do contexto interno da API.

        Args:
          token: **Obrigatório caso não esteja adicionado como header "Authorization".** Seu
              token de autenticação pessoal da API Brapi.

              **Formas de Envio:**

              1.  **Query Parameter:** Adicione `?token=SEU_TOKEN` ao final da URL.
              2.  **HTTP Header:** Inclua o header `Authorization: Bearer SEU_TOKEN` na sua
                  requisição.

              Ambos os métodos são aceitos, mas pelo menos um deles deve ser utilizado.
              Obtenha seu token em [brapi.dev/dashboard](https://brapi.dev/dashboard).

          search: **Opcional.** Termo para filtrar a lista pelo nome da moeda (correspondência
              parcial, case-insensitive).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/currency/available",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "token": token,
                        "search": search,
                    },
                    currency_list_available_params.CurrencyListAvailableParams,
                ),
            ),
            cast_to=CurrencyListAvailableResponse,
        )


class CurrencyResourceWithRawResponse:
    def __init__(self, currency: CurrencyResource) -> None:
        self._currency = currency

        self.retrieve = to_raw_response_wrapper(
            currency.retrieve,
        )
        self.list_available = to_raw_response_wrapper(
            currency.list_available,
        )


class AsyncCurrencyResourceWithRawResponse:
    def __init__(self, currency: AsyncCurrencyResource) -> None:
        self._currency = currency

        self.retrieve = async_to_raw_response_wrapper(
            currency.retrieve,
        )
        self.list_available = async_to_raw_response_wrapper(
            currency.list_available,
        )


class CurrencyResourceWithStreamingResponse:
    def __init__(self, currency: CurrencyResource) -> None:
        self._currency = currency

        self.retrieve = to_streamed_response_wrapper(
            currency.retrieve,
        )
        self.list_available = to_streamed_response_wrapper(
            currency.list_available,
        )


class AsyncCurrencyResourceWithStreamingResponse:
    def __init__(self, currency: AsyncCurrencyResource) -> None:
        self._currency = currency

        self.retrieve = async_to_streamed_response_wrapper(
            currency.retrieve,
        )
        self.list_available = async_to_streamed_response_wrapper(
            currency.list_available,
        )
