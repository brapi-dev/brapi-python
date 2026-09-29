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
from ....types.v2.treasury import indicator_history_params, indicator_retrieve_params
from ....types.v2.treasury.indicator_history_response import IndicatorHistoryResponse
from ....types.v2.treasury.indicator_retrieve_response import IndicatorRetrieveResponse

__all__ = ["IndicatorsResource", "AsyncIndicatorsResource"]


class IndicatorsResource(SyncAPIResource):
    """
    Consulte dados de títulos públicos e outros instrumentos de renda fixa brasileira.
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
        Taxa e preço indicativos mais recentes de até 20 títulos do Tesouro Direto, com
        vencimento, indexador, tipo de cupom e dias até o vencimento.

        Use para mostrar a taxa do dia de um título, calcular o valor de uma posição ou
        avisar quando a taxa passa de um limite.

        As taxas vêm em % a.a., mas o sentido muda por indexador. No Tesouro Selic, são
        o spread sobre a Selic. No Prefixado, a taxa nominal. No IPCA+ e no IGP-M, a
        taxa real acima da inflação. Leia `rateInfo` antes de formatar o número.

        Código desconhecido não gera erro. Ele fica fora de `results`.

        Plano Pro. Sem token, todos os `symbols` precisam estar entre os três títulos
        liberados, listados em [Tesouro Direto](https://brapi.dev/docs/tesouro-direto).

        Args:
          symbols:
              Códigos dos títulos separados por vírgula, até 20. Ex.:
              tesouro-selic-01032031,tesouro-ipca-15052035.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/treasury/indicators",
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
        sort_by: Literal["baseDate", "buyRate", "sellRate", "buyPrice", "sellPrice", "basePrice"] | Omit = omit,
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
        Série diária de taxas e preços indicativos de até 20 títulos do Tesouro Direto,
        com uma série por `symbol`.

        Use para gráficos de taxa, estudo de marcação a mercado ou backtests de renda
        fixa.

        Sem `startDate`, a série começa 12 meses antes de hoje. Sem `endDate`, termina
        hoje. O preço de um título prefixado sobe quando a taxa cai. Quem vende antes do
        vencimento recebe esse preço.

        Cada série traz `rateInfo`, que diz como ler `buyRate` e `sellRate`. Título sem
        dados no período fica fora de `results`.

        Plano Pro. Sem token, todos os `symbols` precisam estar entre os três títulos
        liberados, listados em [Tesouro Direto](https://brapi.dev/docs/tesouro-direto).

        Args:
          symbols:
              Códigos dos títulos separados por vírgula, até 20. Ex.:
              tesouro-selic-01032031,tesouro-ipca-15052035.

          end_date: Data final no formato YYYY-MM-DD. Padrão: hoje.

          sort_by: Campo usado na ordenação da série.

          sort_order: Direção da ordenação.

          start_date: Data inicial no formato YYYY-MM-DD. Padrão: 12 meses antes de hoje.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/treasury/indicators/history",
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
    Consulte dados de títulos públicos e outros instrumentos de renda fixa brasileira.
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
        Taxa e preço indicativos mais recentes de até 20 títulos do Tesouro Direto, com
        vencimento, indexador, tipo de cupom e dias até o vencimento.

        Use para mostrar a taxa do dia de um título, calcular o valor de uma posição ou
        avisar quando a taxa passa de um limite.

        As taxas vêm em % a.a., mas o sentido muda por indexador. No Tesouro Selic, são
        o spread sobre a Selic. No Prefixado, a taxa nominal. No IPCA+ e no IGP-M, a
        taxa real acima da inflação. Leia `rateInfo` antes de formatar o número.

        Código desconhecido não gera erro. Ele fica fora de `results`.

        Plano Pro. Sem token, todos os `symbols` precisam estar entre os três títulos
        liberados, listados em [Tesouro Direto](https://brapi.dev/docs/tesouro-direto).

        Args:
          symbols:
              Códigos dos títulos separados por vírgula, até 20. Ex.:
              tesouro-selic-01032031,tesouro-ipca-15052035.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/treasury/indicators",
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
        sort_by: Literal["baseDate", "buyRate", "sellRate", "buyPrice", "sellPrice", "basePrice"] | Omit = omit,
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
        Série diária de taxas e preços indicativos de até 20 títulos do Tesouro Direto,
        com uma série por `symbol`.

        Use para gráficos de taxa, estudo de marcação a mercado ou backtests de renda
        fixa.

        Sem `startDate`, a série começa 12 meses antes de hoje. Sem `endDate`, termina
        hoje. O preço de um título prefixado sobe quando a taxa cai. Quem vende antes do
        vencimento recebe esse preço.

        Cada série traz `rateInfo`, que diz como ler `buyRate` e `sellRate`. Título sem
        dados no período fica fora de `results`.

        Plano Pro. Sem token, todos os `symbols` precisam estar entre os três títulos
        liberados, listados em [Tesouro Direto](https://brapi.dev/docs/tesouro-direto).

        Args:
          symbols:
              Códigos dos títulos separados por vírgula, até 20. Ex.:
              tesouro-selic-01032031,tesouro-ipca-15052035.

          end_date: Data final no formato YYYY-MM-DD. Padrão: hoje.

          sort_by: Campo usado na ordenação da série.

          sort_order: Direção da ordenação.

          start_date: Data inicial no formato YYYY-MM-DD. Padrão: 12 meses antes de hoje.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/treasury/indicators/history",
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
