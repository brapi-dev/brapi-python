# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v2 import currency_retrieve_params, currency_historical_params, currency_list_available_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v2.currency_retrieve_response import CurrencyRetrieveResponse
from ...types.v2.currency_historical_response import CurrencyHistoricalResponse
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
        Cotação atual de pares de moedas, com preço de compra, preço de venda, máxima,
        mínima e variação do dia. Os pares cobertos pelo Banco Central usam a PTAX.

        Use para converter valores, mostrar o dólar do dia e atualizar planilhas.

        Informe os pares em `currency` no formato `ORIGEM-DESTINO`, como
        `USD-BRL,EUR-BRL`. Os números vêm como texto.

        A diferença entre `bidPrice` e `askPrice` é o spread de referência. Bancos e
        casas de câmbio cobram um spread maior.

        Veja os pares em [listar pares](https://brapi.dev/docs/moedas/available) e a
        série diária em [histórico de câmbio](https://brapi.dev/docs/moedas/historico).
        Planos Startup e Pro.

        Args:
          currency: Pares no formato ORIGEM-DESTINO, separados por vírgula. Ex.: USD-BRL,EUR-BRL.

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

    def historical(
        self,
        *,
        currency: str,
        end_date: str | Omit = omit,
        limit: int | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencyHistoricalResponse:
        """Série diária de câmbio pela PTAX de fechamento do Banco Central.

        Cobre USD, EUR,
        GBP, JPY, CHF, CAD, AUD, DKK, NOK e SEK contra o real e entre si.

        Use para backtests, conversão de valores em datas passadas e gráficos de câmbio.

        Há três tipos de par:

        - Direto, como `USD-BRL`: planos Startup e Pro.
        - Inverso, como `BRL-USD`: calculado como `1 / USD-BRL`. Só no plano Pro.
        - Cruzado, como `EUR-USD`: calculado como `EUR-BRL / USD-BRL` nas datas em que
          as duas séries têm valor. Só no plano Pro.

        Peça até 20 pares por chamada. Sem datas, a janela é dos últimos 12 meses. A
        PTAX sai uma vez por dia útil, então não há pontos em fins de semana e feriados.

        Um par não aceito ou fora do plano gera um item em `errors` e não derruba os
        outros pares. Para cripto, use a
        [cotação de criptomoedas](https://brapi.dev/docs/criptomoedas).

        Args:
          currency:
              Pares no formato ORIGEM-DESTINO, separados por vírgula, até 20. Ex.:
              USD-BRL,EUR-BRL.

          end_date: Data final no formato YYYY-MM-DD. Padrão: hoje.

          limit: Máximo de pontos por par. Padrão: 365.

          sort_order: Ordem por data. Padrão: desc.

          start_date: Data inicial no formato YYYY-MM-DD. Padrão: 12 meses atrás.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/currency/historical",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "currency": currency,
                        "end_date": end_date,
                        "limit": limit,
                        "sort_order": sort_order,
                        "start_date": start_date,
                    },
                    currency_historical_params.CurrencyHistoricalParams,
                ),
            ),
            cast_to=CurrencyHistoricalResponse,
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
        Lista os pares de moedas que a
        [cotação de câmbio](https://brapi.dev/docs/moedas) aceita, no formato
        `ORIGEM-DESTINO`, com o nome de cada par.

        Use para montar seletores de moeda e validar pares antes da chamada.

        Filtre com `search`. Planos Startup e Pro.

        Args:
          search: Texto buscado no par e no nome das moedas.

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
        Cotação atual de pares de moedas, com preço de compra, preço de venda, máxima,
        mínima e variação do dia. Os pares cobertos pelo Banco Central usam a PTAX.

        Use para converter valores, mostrar o dólar do dia e atualizar planilhas.

        Informe os pares em `currency` no formato `ORIGEM-DESTINO`, como
        `USD-BRL,EUR-BRL`. Os números vêm como texto.

        A diferença entre `bidPrice` e `askPrice` é o spread de referência. Bancos e
        casas de câmbio cobram um spread maior.

        Veja os pares em [listar pares](https://brapi.dev/docs/moedas/available) e a
        série diária em [histórico de câmbio](https://brapi.dev/docs/moedas/historico).
        Planos Startup e Pro.

        Args:
          currency: Pares no formato ORIGEM-DESTINO, separados por vírgula. Ex.: USD-BRL,EUR-BRL.

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

    async def historical(
        self,
        *,
        currency: str,
        end_date: str | Omit = omit,
        limit: int | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CurrencyHistoricalResponse:
        """Série diária de câmbio pela PTAX de fechamento do Banco Central.

        Cobre USD, EUR,
        GBP, JPY, CHF, CAD, AUD, DKK, NOK e SEK contra o real e entre si.

        Use para backtests, conversão de valores em datas passadas e gráficos de câmbio.

        Há três tipos de par:

        - Direto, como `USD-BRL`: planos Startup e Pro.
        - Inverso, como `BRL-USD`: calculado como `1 / USD-BRL`. Só no plano Pro.
        - Cruzado, como `EUR-USD`: calculado como `EUR-BRL / USD-BRL` nas datas em que
          as duas séries têm valor. Só no plano Pro.

        Peça até 20 pares por chamada. Sem datas, a janela é dos últimos 12 meses. A
        PTAX sai uma vez por dia útil, então não há pontos em fins de semana e feriados.

        Um par não aceito ou fora do plano gera um item em `errors` e não derruba os
        outros pares. Para cripto, use a
        [cotação de criptomoedas](https://brapi.dev/docs/criptomoedas).

        Args:
          currency:
              Pares no formato ORIGEM-DESTINO, separados por vírgula, até 20. Ex.:
              USD-BRL,EUR-BRL.

          end_date: Data final no formato YYYY-MM-DD. Padrão: hoje.

          limit: Máximo de pontos por par. Padrão: 365.

          sort_order: Ordem por data. Padrão: desc.

          start_date: Data inicial no formato YYYY-MM-DD. Padrão: 12 meses atrás.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/currency/historical",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "currency": currency,
                        "end_date": end_date,
                        "limit": limit,
                        "sort_order": sort_order,
                        "start_date": start_date,
                    },
                    currency_historical_params.CurrencyHistoricalParams,
                ),
            ),
            cast_to=CurrencyHistoricalResponse,
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
        Lista os pares de moedas que a
        [cotação de câmbio](https://brapi.dev/docs/moedas) aceita, no formato
        `ORIGEM-DESTINO`, com o nome de cada par.

        Use para montar seletores de moeda e validar pares antes da chamada.

        Filtre com `search`. Planos Startup e Pro.

        Args:
          search: Texto buscado no par e no nome das moedas.

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
        self.historical = to_raw_response_wrapper(
            currency.historical,
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
        self.historical = async_to_raw_response_wrapper(
            currency.historical,
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
        self.historical = to_streamed_response_wrapper(
            currency.historical,
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
        self.historical = async_to_streamed_response_wrapper(
            currency.historical,
        )
        self.list_available = async_to_streamed_response_wrapper(
            currency.list_available,
        )
