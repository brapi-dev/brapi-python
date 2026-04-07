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
    """
    Monitore taxas de câmbio entre moedas fiduciárias de todo o mundo, com atualizações frequentes e dados históricos.
    """

    @cached_property
    def with_raw_response(self) -> CurrencyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return CurrencyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CurrencyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return CurrencyResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        currency: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencyRetrieveResponse:
        """
        Retorna cotações atualizadas de pares de moedas, com preço de compra/venda,
        variação e extremos do dia.

        ### Funcionalidades:

        - **Cotação Atual:** Preço de compra (bid), venda (ask), máxima, mínima,
          variação
        - **Múltiplos Pares:** Consulte vários em uma requisição (separados por vírgula)
        - **Formato:** `ORIGEM-DESTINO` (ex: `USD-BRL`)

        ### Autenticação:

        Bearer token ou query param `token`. Obtenha em brapi.dev/dashboard.

        ### Exemplos de Requisição:

        ```bash
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/currency?currency=USD-BRL"
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/currency?currency=USD-BRL,EUR-BRL,GBP-BRL"
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/currency?currency=BTC-BRL"
        ```

        ### Pares de Moedas Populares:

        - `USD-BRL` — Dólar Americano / Real
        - `EUR-BRL` — Euro / Real
        - `GBP-BRL` — Libra Esterlina / Real
        - `ARS-BRL` — Peso Argentino / Real
        - `EUR-USD` — Euro / Dólar
        - `BTC-BRL` — Bitcoin / Real
        - `ETH-BRL` — Ethereum / Real

        ### Campos da Resposta:

        - `fromCurrency` / `toCurrency` — Par de moedas
        - `name` — Nome do par
        - `bidPrice` — Preço de compra
        - `askPrice` — Preço de venda
        - `high` / `low` — Máxima/Mínima do dia
        - `bidVariation` — Variação do preço de compra
        - `percentageChange` — Variação percentual (%)

        ### Fonte dos Dados:

        Banco Central do Brasil (PTAX) / Yahoo Finance

        **Plano Mínimo:** Startup **Autenticação:** Necessária

        Args:
          currency: Par(es) de moedas separados por vírgula (ex: USD-BRL,EUR-BRL)

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
                query=maybe_transform({"currency": currency}, currency_retrieve_params.CurrencyRetrieveParams),
            ),
            cast_to=CurrencyRetrieveResponse,
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
    ) -> CurrencyListAvailableResponse:
        """
        Retorna a lista de pares de moedas disponíveis para consulta no endpoint
        `/api/v2/currency`.

        ### Formato:

        ORIGEM-DESTINO, onde ORIGEM é o código da moeda de origem e DESTINO a moeda de
        destino

        ### Pares Disponíveis:

        - **Moedas Fiduciárias:** USD-BRL, EUR-BRL, GBP-BRL, ARS-BRL, CAD-BRL, AUD-BRL,
          JPY-BRL, CNY-BRL
        - **Cross Rates:** EUR-USD, GBP-USD
        - **Criptomoedas:** BTC-BRL, ETH-BRL

        ### Exemplos de Requisição:

        ```bash
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/currency/available"
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/currency/available?search=USD"
        ```

        **Plano Mínimo:** Startup **Autenticação:** Necessária

        Args:
          search: Filtrar pares de moedas por nome ou descrição

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
                query=maybe_transform({"search": search}, currency_list_available_params.CurrencyListAvailableParams),
            ),
            cast_to=CurrencyListAvailableResponse,
        )


class AsyncCurrencyResource(AsyncAPIResource):
    """
    Monitore taxas de câmbio entre moedas fiduciárias de todo o mundo, com atualizações frequentes e dados históricos.
    """

    @cached_property
    def with_raw_response(self) -> AsyncCurrencyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCurrencyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCurrencyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncCurrencyResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        currency: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencyRetrieveResponse:
        """
        Retorna cotações atualizadas de pares de moedas, com preço de compra/venda,
        variação e extremos do dia.

        ### Funcionalidades:

        - **Cotação Atual:** Preço de compra (bid), venda (ask), máxima, mínima,
          variação
        - **Múltiplos Pares:** Consulte vários em uma requisição (separados por vírgula)
        - **Formato:** `ORIGEM-DESTINO` (ex: `USD-BRL`)

        ### Autenticação:

        Bearer token ou query param `token`. Obtenha em brapi.dev/dashboard.

        ### Exemplos de Requisição:

        ```bash
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/currency?currency=USD-BRL"
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/currency?currency=USD-BRL,EUR-BRL,GBP-BRL"
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/currency?currency=BTC-BRL"
        ```

        ### Pares de Moedas Populares:

        - `USD-BRL` — Dólar Americano / Real
        - `EUR-BRL` — Euro / Real
        - `GBP-BRL` — Libra Esterlina / Real
        - `ARS-BRL` — Peso Argentino / Real
        - `EUR-USD` — Euro / Dólar
        - `BTC-BRL` — Bitcoin / Real
        - `ETH-BRL` — Ethereum / Real

        ### Campos da Resposta:

        - `fromCurrency` / `toCurrency` — Par de moedas
        - `name` — Nome do par
        - `bidPrice` — Preço de compra
        - `askPrice` — Preço de venda
        - `high` / `low` — Máxima/Mínima do dia
        - `bidVariation` — Variação do preço de compra
        - `percentageChange` — Variação percentual (%)

        ### Fonte dos Dados:

        Banco Central do Brasil (PTAX) / Yahoo Finance

        **Plano Mínimo:** Startup **Autenticação:** Necessária

        Args:
          currency: Par(es) de moedas separados por vírgula (ex: USD-BRL,EUR-BRL)

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
                    {"currency": currency}, currency_retrieve_params.CurrencyRetrieveParams
                ),
            ),
            cast_to=CurrencyRetrieveResponse,
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
    ) -> CurrencyListAvailableResponse:
        """
        Retorna a lista de pares de moedas disponíveis para consulta no endpoint
        `/api/v2/currency`.

        ### Formato:

        ORIGEM-DESTINO, onde ORIGEM é o código da moeda de origem e DESTINO a moeda de
        destino

        ### Pares Disponíveis:

        - **Moedas Fiduciárias:** USD-BRL, EUR-BRL, GBP-BRL, ARS-BRL, CAD-BRL, AUD-BRL,
          JPY-BRL, CNY-BRL
        - **Cross Rates:** EUR-USD, GBP-USD
        - **Criptomoedas:** BTC-BRL, ETH-BRL

        ### Exemplos de Requisição:

        ```bash
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/currency/available"
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/currency/available?search=USD"
        ```

        **Plano Mínimo:** Startup **Autenticação:** Necessária

        Args:
          search: Filtrar pares de moedas por nome ou descrição

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
                    {"search": search}, currency_list_available_params.CurrencyListAvailableParams
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
