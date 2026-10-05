# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
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
from ....types.v2.options import analytics_history_params, analytics_retrieve_params
from ....types.v2.options.analytics_history_response import AnalyticsHistoryResponse
from ....types.v2.options.analytics_retrieve_response import AnalyticsRetrieveResponse

__all__ = ["AnalyticsResource", "AsyncAnalyticsResource"]


class AnalyticsResource(SyncAPIResource):
    """Consulte contratos, cadeias EOD negociadas e histórico de opções."""

    @cached_property
    def with_raw_response(self) -> AnalyticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalyticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AnalyticsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        expiration_date: str,
        underlying: str,
        date: str | Omit = omit,
        limit: int | Omit = omit,
        max_strike: Optional[float] | Omit = omit,
        min_strike: Optional[float] | Omit = omit,
        side: Literal["call", "put"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsRetrieveResponse:
        """
        Retorna a volatilidade implícita e as gregas (delta, gamma, theta, vega e rho)
        de cada série de um vencimento, calculadas sobre o preço de fechamento.

        Use para comparar a IV entre strikes, montar um smile de volatilidade e medir a
        exposição de uma carteira de opções.

        `timeToExpirationYears` usa dias corridos até o vencimento divididos por 365.
        Por exemplo, 17 dias correspondem a `17 / 365 = 0.04657534`.

        `impliedVolatility` é anual, em decimal. Para um dia corrido, use
        `impliedVolatility / sqrt(365)`. Para `d` dias corridos, use
        `impliedVolatility * sqrt(d / 365)`.

        A divisão por `sqrt(252)` pressupõe 252 pregões por ano. Ela expressa outra
        convenção diária e não altera o prazo usado no cálculo da opção.

        O cálculo usa só o fechamento negociado. Série sem negócio no dia não tem
        cálculo: os campos calculados vêm `null` e `nullReason` diz o motivo.

        `theta` vem por ano. `vega` e `rho` medem o efeito de uma variação de 1,00 na
        volatilidade e no juro. Divida por 100 para ter o efeito de 1 ponto percentual.

        Séries americanas usam árvore binomial. Séries europeias usam
        Black-Scholes-Merton. `dividendYield` considera só os dividendos anunciados até
        a data do cálculo.

        Disponível no plano Pro. Sem token, aceita só `underlying=PETR4`.

        Args:
          expiration_date: Data de vencimento, no formato YYYY-MM-DD. Veja os vencimentos em
              `/expirations`.

          underlying: Ticker do ativo subjacente: ação, ETF, índice, `DOL` ou `WDO`.

          date: Data do pregão, no formato YYYY-MM-DD. Padrão: último pregão disponível.

          limit: Número máximo de séries na resposta. Padrão: todas as séries do filtro.

          max_strike: Strike máximo.

          min_strike: Strike mínimo.

          side: Filtra por `call` ou `put`. Sem o filtro, retorna os dois.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/options/analytics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "expiration_date": expiration_date,
                        "underlying": underlying,
                        "date": date,
                        "limit": limit,
                        "max_strike": max_strike,
                        "min_strike": min_strike,
                        "side": side,
                    },
                    analytics_retrieve_params.AnalyticsRetrieveParams,
                ),
            ),
            cast_to=AnalyticsRetrieveResponse,
        )

    def history(
        self,
        *,
        expiration_date: str,
        symbol: str,
        end_date: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        strike: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsHistoryResponse:
        """
        Retorna o histórico diário de volatilidade implícita e gregas de uma série de
        opção, identificada por `symbol` e `expirationDate`.

        Use para ver como a IV reagiu a eventos, como balanço, decisão de juros ou o
        vencimento, e para testar estratégias com gregas.

        Os campos seguem as regras de
        [gregas e IV](https://brapi.dev/docs/opcoes/analytics). Se o mesmo `symbol`
        aparece duas vezes no vencimento, passe também `strike`.

        Disponível no plano Pro. Sem token, aceita só `symbol` com prefixo `PETR`.

        Args:
          expiration_date: Data de vencimento da série, no formato YYYY-MM-DD.

          symbol: Código da série de opção.

          end_date: Data final, no formato YYYY-MM-DD. Padrão: hoje.

          sort_order: Ordem por data: `asc` do mais antigo ao mais recente, `desc` do mais recente ao
              mais antigo.

          start_date: Data inicial, no formato YYYY-MM-DD. Padrão: 12 meses atrás.

          strike: Preço de exercício. Use quando o mesmo `symbol` aparece mais de uma vez no
              vencimento.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/options/analytics/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "expiration_date": expiration_date,
                        "symbol": symbol,
                        "end_date": end_date,
                        "sort_order": sort_order,
                        "start_date": start_date,
                        "strike": strike,
                    },
                    analytics_history_params.AnalyticsHistoryParams,
                ),
            ),
            cast_to=AnalyticsHistoryResponse,
        )


class AsyncAnalyticsResource(AsyncAPIResource):
    """Consulte contratos, cadeias EOD negociadas e histórico de opções."""

    @cached_property
    def with_raw_response(self) -> AsyncAnalyticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalyticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncAnalyticsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        expiration_date: str,
        underlying: str,
        date: str | Omit = omit,
        limit: int | Omit = omit,
        max_strike: Optional[float] | Omit = omit,
        min_strike: Optional[float] | Omit = omit,
        side: Literal["call", "put"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsRetrieveResponse:
        """
        Retorna a volatilidade implícita e as gregas (delta, gamma, theta, vega e rho)
        de cada série de um vencimento, calculadas sobre o preço de fechamento.

        Use para comparar a IV entre strikes, montar um smile de volatilidade e medir a
        exposição de uma carteira de opções.

        `timeToExpirationYears` usa dias corridos até o vencimento divididos por 365.
        Por exemplo, 17 dias correspondem a `17 / 365 = 0.04657534`.

        `impliedVolatility` é anual, em decimal. Para um dia corrido, use
        `impliedVolatility / sqrt(365)`. Para `d` dias corridos, use
        `impliedVolatility * sqrt(d / 365)`.

        A divisão por `sqrt(252)` pressupõe 252 pregões por ano. Ela expressa outra
        convenção diária e não altera o prazo usado no cálculo da opção.

        O cálculo usa só o fechamento negociado. Série sem negócio no dia não tem
        cálculo: os campos calculados vêm `null` e `nullReason` diz o motivo.

        `theta` vem por ano. `vega` e `rho` medem o efeito de uma variação de 1,00 na
        volatilidade e no juro. Divida por 100 para ter o efeito de 1 ponto percentual.

        Séries americanas usam árvore binomial. Séries europeias usam
        Black-Scholes-Merton. `dividendYield` considera só os dividendos anunciados até
        a data do cálculo.

        Disponível no plano Pro. Sem token, aceita só `underlying=PETR4`.

        Args:
          expiration_date: Data de vencimento, no formato YYYY-MM-DD. Veja os vencimentos em
              `/expirations`.

          underlying: Ticker do ativo subjacente: ação, ETF, índice, `DOL` ou `WDO`.

          date: Data do pregão, no formato YYYY-MM-DD. Padrão: último pregão disponível.

          limit: Número máximo de séries na resposta. Padrão: todas as séries do filtro.

          max_strike: Strike máximo.

          min_strike: Strike mínimo.

          side: Filtra por `call` ou `put`. Sem o filtro, retorna os dois.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/options/analytics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "expiration_date": expiration_date,
                        "underlying": underlying,
                        "date": date,
                        "limit": limit,
                        "max_strike": max_strike,
                        "min_strike": min_strike,
                        "side": side,
                    },
                    analytics_retrieve_params.AnalyticsRetrieveParams,
                ),
            ),
            cast_to=AnalyticsRetrieveResponse,
        )

    async def history(
        self,
        *,
        expiration_date: str,
        symbol: str,
        end_date: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        strike: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsHistoryResponse:
        """
        Retorna o histórico diário de volatilidade implícita e gregas de uma série de
        opção, identificada por `symbol` e `expirationDate`.

        Use para ver como a IV reagiu a eventos, como balanço, decisão de juros ou o
        vencimento, e para testar estratégias com gregas.

        Os campos seguem as regras de
        [gregas e IV](https://brapi.dev/docs/opcoes/analytics). Se o mesmo `symbol`
        aparece duas vezes no vencimento, passe também `strike`.

        Disponível no plano Pro. Sem token, aceita só `symbol` com prefixo `PETR`.

        Args:
          expiration_date: Data de vencimento da série, no formato YYYY-MM-DD.

          symbol: Código da série de opção.

          end_date: Data final, no formato YYYY-MM-DD. Padrão: hoje.

          sort_order: Ordem por data: `asc` do mais antigo ao mais recente, `desc` do mais recente ao
              mais antigo.

          start_date: Data inicial, no formato YYYY-MM-DD. Padrão: 12 meses atrás.

          strike: Preço de exercício. Use quando o mesmo `symbol` aparece mais de uma vez no
              vencimento.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/options/analytics/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "expiration_date": expiration_date,
                        "symbol": symbol,
                        "end_date": end_date,
                        "sort_order": sort_order,
                        "start_date": start_date,
                        "strike": strike,
                    },
                    analytics_history_params.AnalyticsHistoryParams,
                ),
            ),
            cast_to=AnalyticsHistoryResponse,
        )


class AnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

        self.retrieve = to_raw_response_wrapper(
            analytics.retrieve,
        )
        self.history = to_raw_response_wrapper(
            analytics.history,
        )


class AsyncAnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

        self.retrieve = async_to_raw_response_wrapper(
            analytics.retrieve,
        )
        self.history = async_to_raw_response_wrapper(
            analytics.history,
        )


class AnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

        self.retrieve = to_streamed_response_wrapper(
            analytics.retrieve,
        )
        self.history = to_streamed_response_wrapper(
            analytics.history,
        )


class AsyncAnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

        self.retrieve = async_to_streamed_response_wrapper(
            analytics.retrieve,
        )
        self.history = async_to_streamed_response_wrapper(
            analytics.history,
        )
