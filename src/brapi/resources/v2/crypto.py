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
        Cotação de uma ou mais criptomoedas, com preço, variação, máxima, mínima e
        volume de 24 horas. O preço vem na moeda de `currency`, com BRL como padrão.

        Use para mostrar preços de cripto, montar carteiras e gerar gráficos.

        Peça várias moedas em `coin`, como `coin=BTC,ETH,SOL`. Para o histórico, passe
        `range` ou `interval`, como `range=1mo&interval=1d`. A resposta traz os pontos
        em `historicalDataPrice` e o período aplicado em `usedRange` e `usedInterval`.
        Intervalos curtos limitam o período.

        Cripto negocia 24 horas por dia. A variação é uma janela móvel de 24 horas.
        `marketCap` vem sempre como 0.

        Veja as siglas em
        [listar criptomoedas](https://brapi.dev/docs/criptomoedas/available). Planos
        Startup e Pro. Os períodos e intervalos aceitos dependem do plano.

        Args:
          coin: Siglas das criptomoedas, separadas por vírgula. Ex.: BTC,ETH.

          currency: Moeda da cotação, como BRL, USD ou EUR. Padrão: BRL.

          interval: Intervalo entre os pontos do histórico, como 1h ou 1d. Padrão: 1d.

          range: Período do histórico, como 5d, 1mo ou 1y. Padrão: 1mo quando há histórico.

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
        Lista as siglas de criptomoedas que a
        [cotação de criptomoedas](https://brapi.dev/docs/criptomoedas) aceita.

        Use para montar seletores e validar siglas antes da chamada.

        `coins` é uma lista de siglas. Passe cada sigla no parâmetro `coin` da cotação.
        Filtre com `search`. Planos Startup e Pro.

        Args:
          search: Texto buscado na sigla da criptomoeda.

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
        Cotação de uma ou mais criptomoedas, com preço, variação, máxima, mínima e
        volume de 24 horas. O preço vem na moeda de `currency`, com BRL como padrão.

        Use para mostrar preços de cripto, montar carteiras e gerar gráficos.

        Peça várias moedas em `coin`, como `coin=BTC,ETH,SOL`. Para o histórico, passe
        `range` ou `interval`, como `range=1mo&interval=1d`. A resposta traz os pontos
        em `historicalDataPrice` e o período aplicado em `usedRange` e `usedInterval`.
        Intervalos curtos limitam o período.

        Cripto negocia 24 horas por dia. A variação é uma janela móvel de 24 horas.
        `marketCap` vem sempre como 0.

        Veja as siglas em
        [listar criptomoedas](https://brapi.dev/docs/criptomoedas/available). Planos
        Startup e Pro. Os períodos e intervalos aceitos dependem do plano.

        Args:
          coin: Siglas das criptomoedas, separadas por vírgula. Ex.: BTC,ETH.

          currency: Moeda da cotação, como BRL, USD ou EUR. Padrão: BRL.

          interval: Intervalo entre os pontos do histórico, como 1h ou 1d. Padrão: 1d.

          range: Período do histórico, como 5d, 1mo ou 1y. Padrão: 1mo quando há histórico.

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
        Lista as siglas de criptomoedas que a
        [cotação de criptomoedas](https://brapi.dev/docs/criptomoedas) aceita.

        Use para montar seletores e validar siglas antes da chamada.

        `coins` é uma lista de siglas. Passe cada sigla no parâmetro `coin` da cotação.
        Filtre com `search`. Planos Startup e Pro.

        Args:
          search: Texto buscado na sigla da criptomoeda.

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
