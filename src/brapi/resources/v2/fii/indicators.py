# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v2.fii import indicator_history_params, indicator_retrieve_params
from ....types.v2.fii.indicator_history_response import IndicatorHistoryResponse
from ....types.v2.fii.indicator_retrieve_response import IndicatorRetrieveResponse

__all__ = ["IndicatorsResource", "AsyncIndicatorsResource"]


class IndicatorsResource(SyncAPIResource):
    """
    Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
    """

    @cached_property
    def with_raw_response(self) -> IndicatorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return IndicatorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IndicatorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return IndicatorsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        symbols: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IndicatorRetrieveResponse:
        """
        Indicadores mais recentes de um ou mais FIIs: preço, valor patrimonial por cota,
        P/VP, dividend yield de 1 e 12 meses, retorno mensal, cotistas, cotas emitidas,
        patrimônio líquido, ativo total, segmento e dados do administrador.

        Use para comparar FIIs, mostrar o P/VP e o yield de uma cota, ou montar a ficha
        de um fundo.

        `priceToNav` abaixo de 1 indica que a cota negocia abaixo do valor patrimonial.

        Para a série mensal, use o
        [histórico de indicadores](https://brapi.dev/docs/fiis/indicadores-historico).

        Plano Pro. Sem token, aceita só `symbols` com MXRF11 e HGLG11.

        Args:
          symbols: Tickers de FIIs separados por vírgula, até 20. Ex.: HGLG11,MXRF11.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/fii/indicators",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"symbols": symbols}, indicator_retrieve_params.IndicatorRetrieveParams),
            ),
            cast_to=IndicatorRetrieveResponse,
        )

    def history(
        self,
        *,
        symbols: str,
        end_date: str | Omit = omit,
        sort_by: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IndicatorHistoryResponse:
        """
        Série mensal dos [indicadores de FIIs](https://brapi.dev/docs/fiis/indicadores):
        um ponto por mês, com `referenceDate` no último dia do mês. O histórico começa
        em setembro de 2016.

        Use para gráficos de P/VP e dividend yield, e para comparar um fundo com o
        próprio passado.

        Sem `startDate` e `endDate`, retorna os últimos 12 meses. `sortBy` aceita
        `referenceDate` (padrão), `symbol`, `price`, `navPerShare`, `priceToNav`,
        `dividendYield12m`, `dividendYield1m`, `monthlyReturn` e `totalInvestors`.

        Plano Pro. Sem token, aceita só `symbols` com MXRF11 e HGLG11.

        Args:
          symbols: Tickers de FIIs separados por vírgula, até 20. Ex.: HGLG11,MXRF11.

          end_date: Data final no formato YYYY-MM-DD.

          sort_by: Campo de ordenação.

          sort_order: Direção da ordenação.

          start_date: Data inicial no formato YYYY-MM-DD.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/fii/indicators/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "symbols": symbols,
                        "end_date": end_date,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "start_date": start_date,
                    },
                    indicator_history_params.IndicatorHistoryParams,
                ),
            ),
            cast_to=IndicatorHistoryResponse,
        )


class AsyncIndicatorsResource(AsyncAPIResource):
    """
    Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
    """

    @cached_property
    def with_raw_response(self) -> AsyncIndicatorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIndicatorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIndicatorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncIndicatorsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        symbols: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IndicatorRetrieveResponse:
        """
        Indicadores mais recentes de um ou mais FIIs: preço, valor patrimonial por cota,
        P/VP, dividend yield de 1 e 12 meses, retorno mensal, cotistas, cotas emitidas,
        patrimônio líquido, ativo total, segmento e dados do administrador.

        Use para comparar FIIs, mostrar o P/VP e o yield de uma cota, ou montar a ficha
        de um fundo.

        `priceToNav` abaixo de 1 indica que a cota negocia abaixo do valor patrimonial.

        Para a série mensal, use o
        [histórico de indicadores](https://brapi.dev/docs/fiis/indicadores-historico).

        Plano Pro. Sem token, aceita só `symbols` com MXRF11 e HGLG11.

        Args:
          symbols: Tickers de FIIs separados por vírgula, até 20. Ex.: HGLG11,MXRF11.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/fii/indicators",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"symbols": symbols}, indicator_retrieve_params.IndicatorRetrieveParams
                ),
            ),
            cast_to=IndicatorRetrieveResponse,
        )

    async def history(
        self,
        *,
        symbols: str,
        end_date: str | Omit = omit,
        sort_by: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IndicatorHistoryResponse:
        """
        Série mensal dos [indicadores de FIIs](https://brapi.dev/docs/fiis/indicadores):
        um ponto por mês, com `referenceDate` no último dia do mês. O histórico começa
        em setembro de 2016.

        Use para gráficos de P/VP e dividend yield, e para comparar um fundo com o
        próprio passado.

        Sem `startDate` e `endDate`, retorna os últimos 12 meses. `sortBy` aceita
        `referenceDate` (padrão), `symbol`, `price`, `navPerShare`, `priceToNav`,
        `dividendYield12m`, `dividendYield1m`, `monthlyReturn` e `totalInvestors`.

        Plano Pro. Sem token, aceita só `symbols` com MXRF11 e HGLG11.

        Args:
          symbols: Tickers de FIIs separados por vírgula, até 20. Ex.: HGLG11,MXRF11.

          end_date: Data final no formato YYYY-MM-DD.

          sort_by: Campo de ordenação.

          sort_order: Direção da ordenação.

          start_date: Data inicial no formato YYYY-MM-DD.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/fii/indicators/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "symbols": symbols,
                        "end_date": end_date,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "start_date": start_date,
                    },
                    indicator_history_params.IndicatorHistoryParams,
                ),
            ),
            cast_to=IndicatorHistoryResponse,
        )


class IndicatorsResourceWithRawResponse:
    def __init__(self, indicators: IndicatorsResource) -> None:
        self._indicators = indicators

        self.retrieve = to_raw_response_wrapper(
            indicators.retrieve,
        )
        self.history = to_raw_response_wrapper(
            indicators.history,
        )


class AsyncIndicatorsResourceWithRawResponse:
    def __init__(self, indicators: AsyncIndicatorsResource) -> None:
        self._indicators = indicators

        self.retrieve = async_to_raw_response_wrapper(
            indicators.retrieve,
        )
        self.history = async_to_raw_response_wrapper(
            indicators.history,
        )


class IndicatorsResourceWithStreamingResponse:
    def __init__(self, indicators: IndicatorsResource) -> None:
        self._indicators = indicators

        self.retrieve = to_streamed_response_wrapper(
            indicators.retrieve,
        )
        self.history = to_streamed_response_wrapper(
            indicators.history,
        )


class AsyncIndicatorsResourceWithStreamingResponse:
    def __init__(self, indicators: AsyncIndicatorsResource) -> None:
        self._indicators = indicators

        self.retrieve = async_to_streamed_response_wrapper(
            indicators.retrieve,
        )
        self.history = async_to_streamed_response_wrapper(
            indicators.history,
        )
