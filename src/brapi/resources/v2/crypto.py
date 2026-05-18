# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
    """
    Obtenha cotações em tempo real e dados históricos de criptomoedas, disponíveis em diversas moedas de referência.
    """

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
        coin: str | Omit = omit,
        currency: str | Omit = omit,
        interval: str | Omit = omit,
        range: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CryptoRetrieveResponse:
        """
        Retorna cotações atualizadas de uma ou mais criptomoedas, com conversão para
        diferentes moedas fiduciárias.

        ### Funcionalidades:

        - **Cotação Atual:** Preço, variação 24h, volume, market cap
        - **Múltiplas Moedas:** Consulte várias criptos em uma requisição (separadas por
          vírgula)
        - **Conversão de Moeda:** BRL (padrão), USD, EUR e outras
        - **Dados Históricos:** OHLCV via parâmetros `range` e `interval`

        ### Autenticação:

        Bearer token ou query param `token`. Obtenha em brapi.dev/dashboard.

        ### Exemplos de Requisição:

        ```bash
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/crypto?coin=BTC&currency=BRL"
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/crypto?coin=BTC,ETH,SOL&currency=USD"
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/crypto?coin=BTC&currency=BRL&range=1mo&interval=1d"
        ```

        ### Moedas de Conversão:

        BRL (Real), USD (Dólar), EUR (Euro), GBP (Libra) e outras

        ### Campos da Resposta:

        - `coin` — Símbolo da criptomoeda
        - `coinName` — Nome completo
        - `currency` — Moeda de cotação
        - `regularMarketPrice` — Preço atual
        - `regularMarketChange` — Variação em valor absoluto
        - `regularMarketChangePercent` — Variação percentual (%)
        - `regularMarketDayHigh` / `regularMarketDayLow` — Máxima/Mínima do dia
        - `regularMarketVolume` — Volume negociado

        **Plano Mínimo:** Startup **Autenticação:** Necessária

        Args:
          coin: Sigla(s) das criptomoedas separadas por vírgula

          currency: Moeda para cotação (padrão: BRL)

          interval: Intervalo dos dados históricos

          range: Período para dados históricos

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
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CryptoListAvailableResponse:
        """
        Retorna a lista de criptomoedas disponíveis para consulta no endpoint
        `/api/v2/crypto`.

        ### Criptomoedas Populares:

        - **BTC** — Bitcoin
        - **ETH** — Ethereum
        - **BNB** — Binance Coin
        - **SOL** — Solana
        - **ADA** — Cardano
        - **XRP** — Ripple
        - **DOGE** — Dogecoin
        - **DOT** — Polkadot
        - **MATIC** — Polygon
        - **LTC** — Litecoin
        - E centenas de outras...

        ### Uso:

        Use os símbolos retornados como valor do parâmetro `coin` no endpoint principal.

        ### Exemplos de Requisição:

        ```bash
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/crypto/available"
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/crypto/available?search=BTC"
        ```

        **Plano Mínimo:** Startup **Autenticação:** Necessária

        Args:
          search: Filtrar criptomoedas por símbolo

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
                query=maybe_transform({"search": search}, crypto_list_available_params.CryptoListAvailableParams),
            ),
            cast_to=CryptoListAvailableResponse,
        )


class AsyncCryptoResource(AsyncAPIResource):
    """
    Obtenha cotações em tempo real e dados históricos de criptomoedas, disponíveis em diversas moedas de referência.
    """

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
        coin: str | Omit = omit,
        currency: str | Omit = omit,
        interval: str | Omit = omit,
        range: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CryptoRetrieveResponse:
        """
        Retorna cotações atualizadas de uma ou mais criptomoedas, com conversão para
        diferentes moedas fiduciárias.

        ### Funcionalidades:

        - **Cotação Atual:** Preço, variação 24h, volume, market cap
        - **Múltiplas Moedas:** Consulte várias criptos em uma requisição (separadas por
          vírgula)
        - **Conversão de Moeda:** BRL (padrão), USD, EUR e outras
        - **Dados Históricos:** OHLCV via parâmetros `range` e `interval`

        ### Autenticação:

        Bearer token ou query param `token`. Obtenha em brapi.dev/dashboard.

        ### Exemplos de Requisição:

        ```bash
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/crypto?coin=BTC&currency=BRL"
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/crypto?coin=BTC,ETH,SOL&currency=USD"
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/crypto?coin=BTC&currency=BRL&range=1mo&interval=1d"
        ```

        ### Moedas de Conversão:

        BRL (Real), USD (Dólar), EUR (Euro), GBP (Libra) e outras

        ### Campos da Resposta:

        - `coin` — Símbolo da criptomoeda
        - `coinName` — Nome completo
        - `currency` — Moeda de cotação
        - `regularMarketPrice` — Preço atual
        - `regularMarketChange` — Variação em valor absoluto
        - `regularMarketChangePercent` — Variação percentual (%)
        - `regularMarketDayHigh` / `regularMarketDayLow` — Máxima/Mínima do dia
        - `regularMarketVolume` — Volume negociado

        **Plano Mínimo:** Startup **Autenticação:** Necessária

        Args:
          coin: Sigla(s) das criptomoedas separadas por vírgula

          currency: Moeda para cotação (padrão: BRL)

          interval: Intervalo dos dados históricos

          range: Período para dados históricos

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
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CryptoListAvailableResponse:
        """
        Retorna a lista de criptomoedas disponíveis para consulta no endpoint
        `/api/v2/crypto`.

        ### Criptomoedas Populares:

        - **BTC** — Bitcoin
        - **ETH** — Ethereum
        - **BNB** — Binance Coin
        - **SOL** — Solana
        - **ADA** — Cardano
        - **XRP** — Ripple
        - **DOGE** — Dogecoin
        - **DOT** — Polkadot
        - **MATIC** — Polygon
        - **LTC** — Litecoin
        - E centenas de outras...

        ### Uso:

        Use os símbolos retornados como valor do parâmetro `coin` no endpoint principal.

        ### Exemplos de Requisição:

        ```bash
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/crypto/available"
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/crypto/available?search=BTC"
        ```

        **Plano Mínimo:** Startup **Autenticação:** Necessária

        Args:
          search: Filtrar criptomoedas por símbolo

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
                    {"search": search}, crypto_list_available_params.CryptoListAvailableParams
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
