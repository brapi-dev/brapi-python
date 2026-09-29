# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from .analytics import (
    AnalyticsResource,
    AsyncAnalyticsResource,
    AnalyticsResourceWithRawResponse,
    AsyncAnalyticsResourceWithRawResponse,
    AnalyticsResourceWithStreamingResponse,
    AsyncAnalyticsResourceWithStreamingResponse,
)
from .positions import (
    PositionsResource,
    AsyncPositionsResource,
    PositionsResourceWithRawResponse,
    AsyncPositionsResourceWithRawResponse,
    PositionsResourceWithStreamingResponse,
    AsyncPositionsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ....types.v2 import option_chain_params, option_strikes_params, option_historical_params, option_expirations_params
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v2.option_chain_response import OptionChainResponse
from ....types.v2.option_strikes_response import OptionStrikesResponse
from ....types.v2.option_historical_response import OptionHistoricalResponse
from ....types.v2.option_expirations_response import OptionExpirationsResponse

__all__ = ["OptionsResource", "AsyncOptionsResource"]


class OptionsResource(SyncAPIResource):
    """Consulte contratos, cadeias EOD negociadas e histórico de opções."""

    @cached_property
    def positions(self) -> PositionsResource:
        """Consulte contratos, cadeias EOD negociadas e histórico de opções."""
        return PositionsResource(self._client)

    @cached_property
    def analytics(self) -> AnalyticsResource:
        """Consulte contratos, cadeias EOD negociadas e histórico de opções."""
        return AnalyticsResource(self._client)

    @cached_property
    def with_raw_response(self) -> OptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return OptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return OptionsResourceWithStreamingResponse(self)

    def chain(
        self,
        *,
        expiration_date: str,
        underlying: str,
        date: str | Omit = omit,
        max_strike: Optional[float] | Omit = omit,
        min_strike: Optional[float] | Omit = omit,
        side: Literal["call", "put"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OptionChainResponse:
        """
        Retorna as séries de opções de um vencimento, com dados do contrato (`symbol`,
        `side`, `strike`, `optionStyle`) e a cotação do último pregão até `date`: OHLC,
        bid, ask, volume e contratos em aberto.

        Use para montar uma tela de opções por vencimento, comparar calls e puts por
        strike e filtrar séries por faixa de strike.

        A lista traz só séries com cotação nos 10 dias até `date`. Cada série traz a
        cotação do seu último pregão nessa janela, que pode ser anterior a `date`.
        Confira o campo `date` de cada série antes de usar o preço como atual.

        Nas séries de `DOL` e `WDO`, `referencePrice` pode vir preenchido com `close`,
        `high` e `low` nulos, porque muitas séries não negociam no dia.

        Disponível no plano Pro. Sem token, aceita só `underlying=PETR4`.

        Args:
          expiration_date: Data de vencimento, no formato YYYY-MM-DD. Veja os vencimentos em
              `/expirations`.

          underlying: Ticker do ativo subjacente: ação, ETF, índice, `DOL` ou `WDO`.

          date: Data do pregão, no formato YYYY-MM-DD. Padrão: último pregão disponível.

          max_strike: Strike máximo.

          min_strike: Strike mínimo.

          side: Filtra por `call` ou `put`. Sem o filtro, retorna os dois.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/options/chain",
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
                        "max_strike": max_strike,
                        "min_strike": min_strike,
                        "side": side,
                    },
                    option_chain_params.OptionChainParams,
                ),
            ),
            cast_to=OptionChainResponse,
        )

    def expirations(
        self,
        *,
        underlying: str,
        include_expired: Literal["true", "false"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OptionExpirationsResponse:
        """
        Retorna as datas de vencimento de opções de um ativo subjacente: ação, ETF,
        índice, `DOL` ou `WDO`. Por padrão, só vencimentos futuros.

        Use para montar um seletor de vencimento, listar vencimentos passados em um
        backtest e escolher a data antes de consultar a
        [cadeia de opções](https://brapi.dev/docs/opcoes/series).

        Passe `includeExpired=true` para incluir vencimentos passados.

        Disponível no plano Pro. Sem token, aceita só `underlying=PETR4`.

        Args:
          underlying: Ticker do ativo subjacente: ação, ETF, índice, `DOL` ou `WDO`.

          include_expired: `true` inclui vencimentos passados. Padrão: `false`, só vencimentos futuros.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/options/expirations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "underlying": underlying,
                        "include_expired": include_expired,
                    },
                    option_expirations_params.OptionExpirationsParams,
                ),
            ),
            cast_to=OptionExpirationsResponse,
        )

    def historical(
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
    ) -> OptionHistoricalResponse:
        """
        Retorna o histórico diário de uma série de opção, identificada por `symbol` e
        `expirationDate`: OHLC, bid, ask, negócios e volume por pregão.

        Use para montar gráficos de prêmio, fazer backtests e analisar a liquidez de uma
        série.

        Se o mesmo `symbol` aparece duas vezes no vencimento, passe também `strike`.
        Encontre a série na [cadeia de opções](https://brapi.dev/docs/opcoes/series).

        Séries fora do dinheiro passam dias sem negócio. Um pregão sem negócio não
        aparece no histórico.

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
            "/api/v2/options/historical",
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
                    option_historical_params.OptionHistoricalParams,
                ),
            ),
            cast_to=OptionHistoricalResponse,
        )

    def strikes(
        self,
        *,
        expiration_date: str,
        underlying: str,
        side: Literal["call", "put"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OptionStrikesResponse:
        """
        Retorna os preços de exercício das séries negociadas de um vencimento, em ordem
        crescente. Filtre por `call` ou `put` com `side`.

        Use para montar um seletor de strike sem baixar a cadeia inteira.

        Este passo é opcional: a
        [cadeia de opções](https://brapi.dev/docs/opcoes/series) também aceita
        `minStrike` e `maxStrike`.

        Disponível no plano Pro. Sem token, aceita só `underlying=PETR4`.

        Args:
          expiration_date: Data de vencimento, no formato YYYY-MM-DD. Veja os vencimentos em
              `/expirations`.

          underlying: Ticker do ativo subjacente: ação, ETF, índice, `DOL` ou `WDO`.

          side: Filtra por `call` ou `put`. Sem o filtro, retorna os dois.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/options/strikes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "expiration_date": expiration_date,
                        "underlying": underlying,
                        "side": side,
                    },
                    option_strikes_params.OptionStrikesParams,
                ),
            ),
            cast_to=OptionStrikesResponse,
        )


class AsyncOptionsResource(AsyncAPIResource):
    """Consulte contratos, cadeias EOD negociadas e histórico de opções."""

    @cached_property
    def positions(self) -> AsyncPositionsResource:
        """Consulte contratos, cadeias EOD negociadas e histórico de opções."""
        return AsyncPositionsResource(self._client)

    @cached_property
    def analytics(self) -> AsyncAnalyticsResource:
        """Consulte contratos, cadeias EOD negociadas e histórico de opções."""
        return AsyncAnalyticsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncOptionsResourceWithStreamingResponse(self)

    async def chain(
        self,
        *,
        expiration_date: str,
        underlying: str,
        date: str | Omit = omit,
        max_strike: Optional[float] | Omit = omit,
        min_strike: Optional[float] | Omit = omit,
        side: Literal["call", "put"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OptionChainResponse:
        """
        Retorna as séries de opções de um vencimento, com dados do contrato (`symbol`,
        `side`, `strike`, `optionStyle`) e a cotação do último pregão até `date`: OHLC,
        bid, ask, volume e contratos em aberto.

        Use para montar uma tela de opções por vencimento, comparar calls e puts por
        strike e filtrar séries por faixa de strike.

        A lista traz só séries com cotação nos 10 dias até `date`. Cada série traz a
        cotação do seu último pregão nessa janela, que pode ser anterior a `date`.
        Confira o campo `date` de cada série antes de usar o preço como atual.

        Nas séries de `DOL` e `WDO`, `referencePrice` pode vir preenchido com `close`,
        `high` e `low` nulos, porque muitas séries não negociam no dia.

        Disponível no plano Pro. Sem token, aceita só `underlying=PETR4`.

        Args:
          expiration_date: Data de vencimento, no formato YYYY-MM-DD. Veja os vencimentos em
              `/expirations`.

          underlying: Ticker do ativo subjacente: ação, ETF, índice, `DOL` ou `WDO`.

          date: Data do pregão, no formato YYYY-MM-DD. Padrão: último pregão disponível.

          max_strike: Strike máximo.

          min_strike: Strike mínimo.

          side: Filtra por `call` ou `put`. Sem o filtro, retorna os dois.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/options/chain",
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
                        "max_strike": max_strike,
                        "min_strike": min_strike,
                        "side": side,
                    },
                    option_chain_params.OptionChainParams,
                ),
            ),
            cast_to=OptionChainResponse,
        )

    async def expirations(
        self,
        *,
        underlying: str,
        include_expired: Literal["true", "false"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OptionExpirationsResponse:
        """
        Retorna as datas de vencimento de opções de um ativo subjacente: ação, ETF,
        índice, `DOL` ou `WDO`. Por padrão, só vencimentos futuros.

        Use para montar um seletor de vencimento, listar vencimentos passados em um
        backtest e escolher a data antes de consultar a
        [cadeia de opções](https://brapi.dev/docs/opcoes/series).

        Passe `includeExpired=true` para incluir vencimentos passados.

        Disponível no plano Pro. Sem token, aceita só `underlying=PETR4`.

        Args:
          underlying: Ticker do ativo subjacente: ação, ETF, índice, `DOL` ou `WDO`.

          include_expired: `true` inclui vencimentos passados. Padrão: `false`, só vencimentos futuros.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/options/expirations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "underlying": underlying,
                        "include_expired": include_expired,
                    },
                    option_expirations_params.OptionExpirationsParams,
                ),
            ),
            cast_to=OptionExpirationsResponse,
        )

    async def historical(
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
    ) -> OptionHistoricalResponse:
        """
        Retorna o histórico diário de uma série de opção, identificada por `symbol` e
        `expirationDate`: OHLC, bid, ask, negócios e volume por pregão.

        Use para montar gráficos de prêmio, fazer backtests e analisar a liquidez de uma
        série.

        Se o mesmo `symbol` aparece duas vezes no vencimento, passe também `strike`.
        Encontre a série na [cadeia de opções](https://brapi.dev/docs/opcoes/series).

        Séries fora do dinheiro passam dias sem negócio. Um pregão sem negócio não
        aparece no histórico.

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
            "/api/v2/options/historical",
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
                    option_historical_params.OptionHistoricalParams,
                ),
            ),
            cast_to=OptionHistoricalResponse,
        )

    async def strikes(
        self,
        *,
        expiration_date: str,
        underlying: str,
        side: Literal["call", "put"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OptionStrikesResponse:
        """
        Retorna os preços de exercício das séries negociadas de um vencimento, em ordem
        crescente. Filtre por `call` ou `put` com `side`.

        Use para montar um seletor de strike sem baixar a cadeia inteira.

        Este passo é opcional: a
        [cadeia de opções](https://brapi.dev/docs/opcoes/series) também aceita
        `minStrike` e `maxStrike`.

        Disponível no plano Pro. Sem token, aceita só `underlying=PETR4`.

        Args:
          expiration_date: Data de vencimento, no formato YYYY-MM-DD. Veja os vencimentos em
              `/expirations`.

          underlying: Ticker do ativo subjacente: ação, ETF, índice, `DOL` ou `WDO`.

          side: Filtra por `call` ou `put`. Sem o filtro, retorna os dois.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/options/strikes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "expiration_date": expiration_date,
                        "underlying": underlying,
                        "side": side,
                    },
                    option_strikes_params.OptionStrikesParams,
                ),
            ),
            cast_to=OptionStrikesResponse,
        )


class OptionsResourceWithRawResponse:
    def __init__(self, options: OptionsResource) -> None:
        self._options = options

        self.chain = to_raw_response_wrapper(
            options.chain,
        )
        self.expirations = to_raw_response_wrapper(
            options.expirations,
        )
        self.historical = to_raw_response_wrapper(
            options.historical,
        )
        self.strikes = to_raw_response_wrapper(
            options.strikes,
        )

    @cached_property
    def positions(self) -> PositionsResourceWithRawResponse:
        """Consulte contratos, cadeias EOD negociadas e histórico de opções."""
        return PositionsResourceWithRawResponse(self._options.positions)

    @cached_property
    def analytics(self) -> AnalyticsResourceWithRawResponse:
        """Consulte contratos, cadeias EOD negociadas e histórico de opções."""
        return AnalyticsResourceWithRawResponse(self._options.analytics)


class AsyncOptionsResourceWithRawResponse:
    def __init__(self, options: AsyncOptionsResource) -> None:
        self._options = options

        self.chain = async_to_raw_response_wrapper(
            options.chain,
        )
        self.expirations = async_to_raw_response_wrapper(
            options.expirations,
        )
        self.historical = async_to_raw_response_wrapper(
            options.historical,
        )
        self.strikes = async_to_raw_response_wrapper(
            options.strikes,
        )

    @cached_property
    def positions(self) -> AsyncPositionsResourceWithRawResponse:
        """Consulte contratos, cadeias EOD negociadas e histórico de opções."""
        return AsyncPositionsResourceWithRawResponse(self._options.positions)

    @cached_property
    def analytics(self) -> AsyncAnalyticsResourceWithRawResponse:
        """Consulte contratos, cadeias EOD negociadas e histórico de opções."""
        return AsyncAnalyticsResourceWithRawResponse(self._options.analytics)


class OptionsResourceWithStreamingResponse:
    def __init__(self, options: OptionsResource) -> None:
        self._options = options

        self.chain = to_streamed_response_wrapper(
            options.chain,
        )
        self.expirations = to_streamed_response_wrapper(
            options.expirations,
        )
        self.historical = to_streamed_response_wrapper(
            options.historical,
        )
        self.strikes = to_streamed_response_wrapper(
            options.strikes,
        )

    @cached_property
    def positions(self) -> PositionsResourceWithStreamingResponse:
        """Consulte contratos, cadeias EOD negociadas e histórico de opções."""
        return PositionsResourceWithStreamingResponse(self._options.positions)

    @cached_property
    def analytics(self) -> AnalyticsResourceWithStreamingResponse:
        """Consulte contratos, cadeias EOD negociadas e histórico de opções."""
        return AnalyticsResourceWithStreamingResponse(self._options.analytics)


class AsyncOptionsResourceWithStreamingResponse:
    def __init__(self, options: AsyncOptionsResource) -> None:
        self._options = options

        self.chain = async_to_streamed_response_wrapper(
            options.chain,
        )
        self.expirations = async_to_streamed_response_wrapper(
            options.expirations,
        )
        self.historical = async_to_streamed_response_wrapper(
            options.historical,
        )
        self.strikes = async_to_streamed_response_wrapper(
            options.strikes,
        )

    @cached_property
    def positions(self) -> AsyncPositionsResourceWithStreamingResponse:
        """Consulte contratos, cadeias EOD negociadas e histórico de opções."""
        return AsyncPositionsResourceWithStreamingResponse(self._options.positions)

    @cached_property
    def analytics(self) -> AsyncAnalyticsResourceWithStreamingResponse:
        """Consulte contratos, cadeias EOD negociadas e histórico de opções."""
        return AsyncAnalyticsResourceWithStreamingResponse(self._options.analytics)
