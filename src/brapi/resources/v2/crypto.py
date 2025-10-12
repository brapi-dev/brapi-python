# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v2 import crypto_retrieve_params, crypto_list_available_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v2.crypto_retrieve_response import CryptoRetrieveResponse
from ...types.v2.crypto_list_available_response import CryptoListAvailableResponse

__all__ = ["CryptoResource", "AsyncCryptoResource"]


class CryptoResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CryptoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return CryptoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CryptoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return CryptoResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        coin: str,
        token: str | Omit = omit,
        currency: str | Omit = omit,
        interval: Literal["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
        | Omit = omit,
        range: Literal["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CryptoRetrieveResponse:
        """
        Obtenha cotações atualizadas e dados históricos para uma ou mais criptomoedas.

        ### Funcionalidades:

        - **Cotação Múltipla:** Consulte várias criptomoedas em uma única requisição
          usando o parâmetro `coin`.
        - **Moeda de Referência:** Especifique a moeda fiduciária para a cotação com
          `currency` (padrão: BRL).
        - **Dados Históricos:** Solicite séries históricas usando `range` e `interval`
          (similar ao endpoint de ações).

        ### Autenticação:

        Requer token de autenticação via `token` (query) ou `Authorization` (header).

        ### Exemplo de Requisição:

        **Cotação de Bitcoin (BTC) e Ethereum (ETH) em Dólar Americano (USD):**

        ```bash
        curl -X GET "https://brapi.dev/api/v2/crypto?coin=BTC,ETH&currency=USD&token=SEU_TOKEN"
        ```

        **Cotação de Cardano (ADA) em Real (BRL) com histórico do último mês (intervalo
        diário):**

        ```bash
        curl -X GET "https://brapi.dev/api/v2/crypto?coin=ADA&currency=BRL&range=1mo&interval=1d&token=SEU_TOKEN"
        ```

        ### Resposta:

        A resposta contém um array `coins`, onde cada objeto representa uma criptomoeda
        solicitada, incluindo sua cotação atual, dados de mercado e, opcionalmente, a
        série histórica (`historicalDataPrice`).

        Args:
          coin: **Obrigatório.** Uma ou mais siglas (tickers) de criptomoedas que você deseja
              consultar. Separe múltiplas siglas por vírgula (`,`).

              - **Exemplos:** `BTC`, `ETH,ADA`, `SOL`.

          token: **Obrigatório caso não esteja adicionado como header "Authorization".** Seu
              token de autenticação pessoal da API Brapi.

              **Formas de Envio:**

              1.  **Query Parameter:** Adicione `?token=SEU_TOKEN` ao final da URL.
              2.  **HTTP Header:** Inclua o header `Authorization: Bearer SEU_TOKEN` na sua
                  requisição.

              Ambos os métodos são aceitos, mas pelo menos um deles deve ser utilizado.
              Obtenha seu token em [brapi.dev/dashboard](https://brapi.dev/dashboard).

          currency: **Opcional.** A sigla da moeda fiduciária na qual a cotação da(s) criptomoeda(s)
              deve ser retornada. Se omitido, o padrão é `BRL` (Real Brasileiro).

          interval: **Opcional.** Define a granularidade (intervalo) dos dados históricos de preço
              (`historicalDataPrice`). Requer que `range` também seja especificado. Funciona
              de forma análoga ao endpoint de ações.

              - Valores: `1m`, `2m`, `5m`, `15m`, `30m`, `60m`, `90m`, `1h`, `1d`, `5d`,
                `1wk`, `1mo`, `3mo`.

          range: **Opcional.** Define o período para os dados históricos de preço
              (`historicalDataPrice`). Funciona de forma análoga ao endpoint de ações. Se
              omitido, apenas a cotação mais recente é retornada (a menos que `interval` seja
              usado).

              - Valores: `1d`, `5d`, `1mo`, `3mo`, `6mo`, `1y`, `2y`, `5y`, `10y`, `ytd`,
                `max`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/crypto",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "coin": coin,
                        "token": token,
                        "currency": currency,
                        "interval": interval,
                        "range": range,
                    },
                    crypto_retrieve_params.CryptoRetrieveParams,
                ),
            ),
            cast_to=CryptoRetrieveResponse,
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
    ) -> CryptoListAvailableResponse:
        """
        Obtenha a lista completa de todas as siglas (tickers) de criptomoedas que a API
        Brapi suporta para consulta no endpoint `/api/v2/crypto`.

        ### Funcionalidade:

        - Retorna um array `coins` com as siglas.
        - Pode ser filtrado usando o parâmetro `search`.

        ### Autenticação:

        Requer token de autenticação via `token` (query) ou `Authorization` (header).

        ### Exemplo de Requisição:

        **Listar todas as criptomoedas disponíveis:**

        ```bash
        curl -X GET "https://brapi.dev/api/v2/crypto/available?token=SEU_TOKEN"
        ```

        **Buscar criptomoedas cujo ticker contenha 'DOGE':**

        ```bash
        curl -X GET "https://brapi.dev/api/v2/crypto/available?search=DOGE&token=SEU_TOKEN"
        ```

        ### Resposta:

        A resposta é um objeto JSON com a chave `coins`, contendo um array de strings
        com as siglas das criptomoedas (ex: `["BTC", "ETH", "LTC", "XRP"]`).

        Args:
          token: **Obrigatório caso não esteja adicionado como header "Authorization".** Seu
              token de autenticação pessoal da API Brapi.

              **Formas de Envio:**

              1.  **Query Parameter:** Adicione `?token=SEU_TOKEN` ao final da URL.
              2.  **HTTP Header:** Inclua o header `Authorization: Bearer SEU_TOKEN` na sua
                  requisição.

              Ambos os métodos são aceitos, mas pelo menos um deles deve ser utilizado.
              Obtenha seu token em [brapi.dev/dashboard](https://brapi.dev/dashboard).

          search: **Opcional.** Termo para filtrar a lista de siglas de criptomoedas
              (correspondência parcial, case-insensitive). Se omitido, retorna todas as
              siglas.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/crypto/available",
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
                    crypto_list_available_params.CryptoListAvailableParams,
                ),
            ),
            cast_to=CryptoListAvailableResponse,
        )


class AsyncCryptoResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCryptoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCryptoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCryptoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncCryptoResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        coin: str,
        token: str | Omit = omit,
        currency: str | Omit = omit,
        interval: Literal["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
        | Omit = omit,
        range: Literal["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CryptoRetrieveResponse:
        """
        Obtenha cotações atualizadas e dados históricos para uma ou mais criptomoedas.

        ### Funcionalidades:

        - **Cotação Múltipla:** Consulte várias criptomoedas em uma única requisição
          usando o parâmetro `coin`.
        - **Moeda de Referência:** Especifique a moeda fiduciária para a cotação com
          `currency` (padrão: BRL).
        - **Dados Históricos:** Solicite séries históricas usando `range` e `interval`
          (similar ao endpoint de ações).

        ### Autenticação:

        Requer token de autenticação via `token` (query) ou `Authorization` (header).

        ### Exemplo de Requisição:

        **Cotação de Bitcoin (BTC) e Ethereum (ETH) em Dólar Americano (USD):**

        ```bash
        curl -X GET "https://brapi.dev/api/v2/crypto?coin=BTC,ETH&currency=USD&token=SEU_TOKEN"
        ```

        **Cotação de Cardano (ADA) em Real (BRL) com histórico do último mês (intervalo
        diário):**

        ```bash
        curl -X GET "https://brapi.dev/api/v2/crypto?coin=ADA&currency=BRL&range=1mo&interval=1d&token=SEU_TOKEN"
        ```

        ### Resposta:

        A resposta contém um array `coins`, onde cada objeto representa uma criptomoeda
        solicitada, incluindo sua cotação atual, dados de mercado e, opcionalmente, a
        série histórica (`historicalDataPrice`).

        Args:
          coin: **Obrigatório.** Uma ou mais siglas (tickers) de criptomoedas que você deseja
              consultar. Separe múltiplas siglas por vírgula (`,`).

              - **Exemplos:** `BTC`, `ETH,ADA`, `SOL`.

          token: **Obrigatório caso não esteja adicionado como header "Authorization".** Seu
              token de autenticação pessoal da API Brapi.

              **Formas de Envio:**

              1.  **Query Parameter:** Adicione `?token=SEU_TOKEN` ao final da URL.
              2.  **HTTP Header:** Inclua o header `Authorization: Bearer SEU_TOKEN` na sua
                  requisição.

              Ambos os métodos são aceitos, mas pelo menos um deles deve ser utilizado.
              Obtenha seu token em [brapi.dev/dashboard](https://brapi.dev/dashboard).

          currency: **Opcional.** A sigla da moeda fiduciária na qual a cotação da(s) criptomoeda(s)
              deve ser retornada. Se omitido, o padrão é `BRL` (Real Brasileiro).

          interval: **Opcional.** Define a granularidade (intervalo) dos dados históricos de preço
              (`historicalDataPrice`). Requer que `range` também seja especificado. Funciona
              de forma análoga ao endpoint de ações.

              - Valores: `1m`, `2m`, `5m`, `15m`, `30m`, `60m`, `90m`, `1h`, `1d`, `5d`,
                `1wk`, `1mo`, `3mo`.

          range: **Opcional.** Define o período para os dados históricos de preço
              (`historicalDataPrice`). Funciona de forma análoga ao endpoint de ações. Se
              omitido, apenas a cotação mais recente é retornada (a menos que `interval` seja
              usado).

              - Valores: `1d`, `5d`, `1mo`, `3mo`, `6mo`, `1y`, `2y`, `5y`, `10y`, `ytd`,
                `max`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/crypto",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "coin": coin,
                        "token": token,
                        "currency": currency,
                        "interval": interval,
                        "range": range,
                    },
                    crypto_retrieve_params.CryptoRetrieveParams,
                ),
            ),
            cast_to=CryptoRetrieveResponse,
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
    ) -> CryptoListAvailableResponse:
        """
        Obtenha a lista completa de todas as siglas (tickers) de criptomoedas que a API
        Brapi suporta para consulta no endpoint `/api/v2/crypto`.

        ### Funcionalidade:

        - Retorna um array `coins` com as siglas.
        - Pode ser filtrado usando o parâmetro `search`.

        ### Autenticação:

        Requer token de autenticação via `token` (query) ou `Authorization` (header).

        ### Exemplo de Requisição:

        **Listar todas as criptomoedas disponíveis:**

        ```bash
        curl -X GET "https://brapi.dev/api/v2/crypto/available?token=SEU_TOKEN"
        ```

        **Buscar criptomoedas cujo ticker contenha 'DOGE':**

        ```bash
        curl -X GET "https://brapi.dev/api/v2/crypto/available?search=DOGE&token=SEU_TOKEN"
        ```

        ### Resposta:

        A resposta é um objeto JSON com a chave `coins`, contendo um array de strings
        com as siglas das criptomoedas (ex: `["BTC", "ETH", "LTC", "XRP"]`).

        Args:
          token: **Obrigatório caso não esteja adicionado como header "Authorization".** Seu
              token de autenticação pessoal da API Brapi.

              **Formas de Envio:**

              1.  **Query Parameter:** Adicione `?token=SEU_TOKEN` ao final da URL.
              2.  **HTTP Header:** Inclua o header `Authorization: Bearer SEU_TOKEN` na sua
                  requisição.

              Ambos os métodos são aceitos, mas pelo menos um deles deve ser utilizado.
              Obtenha seu token em [brapi.dev/dashboard](https://brapi.dev/dashboard).

          search: **Opcional.** Termo para filtrar a lista de siglas de criptomoedas
              (correspondência parcial, case-insensitive). Se omitido, retorna todas as
              siglas.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/crypto/available",
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
                    crypto_list_available_params.CryptoListAvailableParams,
                ),
            ),
            cast_to=CryptoListAvailableResponse,
        )


class CryptoResourceWithRawResponse:
    def __init__(self, crypto: CryptoResource) -> None:
        self._crypto = crypto

        self.retrieve = to_raw_response_wrapper(
            crypto.retrieve,
        )
        self.list_available = to_raw_response_wrapper(
            crypto.list_available,
        )


class AsyncCryptoResourceWithRawResponse:
    def __init__(self, crypto: AsyncCryptoResource) -> None:
        self._crypto = crypto

        self.retrieve = async_to_raw_response_wrapper(
            crypto.retrieve,
        )
        self.list_available = async_to_raw_response_wrapper(
            crypto.list_available,
        )


class CryptoResourceWithStreamingResponse:
    def __init__(self, crypto: CryptoResource) -> None:
        self._crypto = crypto

        self.retrieve = to_streamed_response_wrapper(
            crypto.retrieve,
        )
        self.list_available = to_streamed_response_wrapper(
            crypto.list_available,
        )


class AsyncCryptoResourceWithStreamingResponse:
    def __init__(self, crypto: AsyncCryptoResource) -> None:
        self._crypto = crypto

        self.retrieve = async_to_streamed_response_wrapper(
            crypto.retrieve,
        )
        self.list_available = async_to_streamed_response_wrapper(
            crypto.list_available,
        )
