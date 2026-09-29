# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

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
from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.v2.futures import (
    option_chain_params,
    option_strikes_params,
    option_historical_params,
    option_expirations_params,
)
from .....types.v2.futures.option_chain_response import OptionChainResponse
from .....types.v2.futures.option_strikes_response import OptionStrikesResponse
from .....types.v2.futures.option_historical_response import OptionHistoricalResponse
from .....types.v2.futures.option_expirations_response import OptionExpirationsResponse

__all__ = ["OptionsResource", "AsyncOptionsResource"]


class OptionsResource(SyncAPIResource):
    @cached_property
    def positions(self) -> PositionsResource:
        return PositionsResource(self._client)

    @cached_property
    def analytics(self) -> AnalyticsResource:
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
        Retorna as calls e puts de um vencimento de opções sobre futuro, com dados do
        contrato (`symbol`, `optionType`, `optionStyle`, `strike`, `contractMultiplier`)
        e a cotação do pregão: OHLC, `referencePrice`, volume e contratos em aberto.

        Use para montar uma tela de opções por vencimento, comparar calls e puts por
        strike e filtrar séries por faixa de strike.

        Todas as séries vêm do mesmo pregão: o último com dados até a data pedida,
        informado em `date`. Séries sem registro nesse pregão não aparecem.

        Muitas séries não negociam todo dia. Sem negócio, `close` vem `null` e
        `referencePrice` costuma vir preenchido.

        Disponível no plano Pro. Sem token, aceita só `underlying=BGI`.

        Args:
          expiration_date: Data de vencimento, no formato YYYY-MM-DD. Veja os vencimentos em
              `/expirations`.

          underlying: Código do ativo do futuro. Ex.: `BGI`.

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
            "/api/v2/futures/options/chain",
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
        Retorna as datas de vencimento de opções sobre um contrato futuro, como boi
        gordo (`BGI`), café arábica (`ICF`), milho (`CCM`) e soja (`SJC`). Por padrão,
        só vencimentos futuros.

        Use para montar um seletor de vencimento, listar vencimentos passados em um
        backtest e escolher a data antes de consultar a
        [cadeia de opções sobre futuros](https://brapi.dev/docs/futuros/opcoes/series).

        Passe `includeExpired=true` para incluir vencimentos passados. O vencimento da
        opção pode ser diferente do vencimento do futuro. Não calcule uma data a partir
        da outra.

        Disponível no plano Pro. Sem token, aceita só `underlying=BGI`.

        Args:
          underlying: Código do ativo do futuro. Ex.: `BGI`, `ICF`.

          include_expired: `true` inclui vencimentos passados. Padrão: `false`, só vencimentos futuros.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/futures/options/expirations",
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
        symbol: str,
        end_date: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OptionHistoricalResponse:
        """
        Retorna o histórico diário de uma opção sobre futuro, identificada por `symbol`:
        dados do contrato e, por pregão, OHLC, `referencePrice`, `oscillationPct`,
        negócios e volume.

        Use para montar gráficos de prêmio, fazer backtests e analisar a liquidez de uma
        série.

        Encontre a série na
        [cadeia de opções sobre futuros](https://brapi.dev/docs/futuros/opcoes/series).
        Séries longe do preço do futuro quase não negociam, e o histórico pode ter
        poucos pregões.

        Disponível no plano Pro. Sem token, aceita só `symbol` com prefixo `BGI`.

        Args:
          symbol: Código da série de opção.

          end_date: Data final, no formato YYYY-MM-DD. Padrão: hoje.

          sort_order: Ordem por data: `asc` do mais antigo ao mais recente, `desc` do mais recente ao
              mais antigo.

          start_date: Data inicial, no formato YYYY-MM-DD. Padrão: 12 meses atrás.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/futures/options/historical",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "symbol": symbol,
                        "end_date": end_date,
                        "sort_order": sort_order,
                        "start_date": start_date,
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
        Retorna os preços de exercício das séries de opções sobre futuro de um
        vencimento, em ordem crescente. Filtre por `call` ou `put` com `side`.

        Use para montar um seletor de strike sem baixar a cadeia inteira.

        Este passo é opcional: a
        [cadeia de opções sobre futuros](https://brapi.dev/docs/futuros/opcoes/series)
        também aceita `minStrike` e `maxStrike`.

        Disponível no plano Pro. Sem token, aceita só `underlying=BGI`.

        Args:
          expiration_date: Data de vencimento, no formato YYYY-MM-DD. Veja os vencimentos em
              `/expirations`.

          underlying: Código do ativo do futuro. Ex.: `BGI`.

          side: Filtra por `call` ou `put`. Sem o filtro, retorna os dois.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/futures/options/strikes",
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
    @cached_property
    def positions(self) -> AsyncPositionsResource:
        return AsyncPositionsResource(self._client)

    @cached_property
    def analytics(self) -> AsyncAnalyticsResource:
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
        Retorna as calls e puts de um vencimento de opções sobre futuro, com dados do
        contrato (`symbol`, `optionType`, `optionStyle`, `strike`, `contractMultiplier`)
        e a cotação do pregão: OHLC, `referencePrice`, volume e contratos em aberto.

        Use para montar uma tela de opções por vencimento, comparar calls e puts por
        strike e filtrar séries por faixa de strike.

        Todas as séries vêm do mesmo pregão: o último com dados até a data pedida,
        informado em `date`. Séries sem registro nesse pregão não aparecem.

        Muitas séries não negociam todo dia. Sem negócio, `close` vem `null` e
        `referencePrice` costuma vir preenchido.

        Disponível no plano Pro. Sem token, aceita só `underlying=BGI`.

        Args:
          expiration_date: Data de vencimento, no formato YYYY-MM-DD. Veja os vencimentos em
              `/expirations`.

          underlying: Código do ativo do futuro. Ex.: `BGI`.

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
            "/api/v2/futures/options/chain",
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
        Retorna as datas de vencimento de opções sobre um contrato futuro, como boi
        gordo (`BGI`), café arábica (`ICF`), milho (`CCM`) e soja (`SJC`). Por padrão,
        só vencimentos futuros.

        Use para montar um seletor de vencimento, listar vencimentos passados em um
        backtest e escolher a data antes de consultar a
        [cadeia de opções sobre futuros](https://brapi.dev/docs/futuros/opcoes/series).

        Passe `includeExpired=true` para incluir vencimentos passados. O vencimento da
        opção pode ser diferente do vencimento do futuro. Não calcule uma data a partir
        da outra.

        Disponível no plano Pro. Sem token, aceita só `underlying=BGI`.

        Args:
          underlying: Código do ativo do futuro. Ex.: `BGI`, `ICF`.

          include_expired: `true` inclui vencimentos passados. Padrão: `false`, só vencimentos futuros.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/futures/options/expirations",
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
        symbol: str,
        end_date: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OptionHistoricalResponse:
        """
        Retorna o histórico diário de uma opção sobre futuro, identificada por `symbol`:
        dados do contrato e, por pregão, OHLC, `referencePrice`, `oscillationPct`,
        negócios e volume.

        Use para montar gráficos de prêmio, fazer backtests e analisar a liquidez de uma
        série.

        Encontre a série na
        [cadeia de opções sobre futuros](https://brapi.dev/docs/futuros/opcoes/series).
        Séries longe do preço do futuro quase não negociam, e o histórico pode ter
        poucos pregões.

        Disponível no plano Pro. Sem token, aceita só `symbol` com prefixo `BGI`.

        Args:
          symbol: Código da série de opção.

          end_date: Data final, no formato YYYY-MM-DD. Padrão: hoje.

          sort_order: Ordem por data: `asc` do mais antigo ao mais recente, `desc` do mais recente ao
              mais antigo.

          start_date: Data inicial, no formato YYYY-MM-DD. Padrão: 12 meses atrás.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/futures/options/historical",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "symbol": symbol,
                        "end_date": end_date,
                        "sort_order": sort_order,
                        "start_date": start_date,
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
        Retorna os preços de exercício das séries de opções sobre futuro de um
        vencimento, em ordem crescente. Filtre por `call` ou `put` com `side`.

        Use para montar um seletor de strike sem baixar a cadeia inteira.

        Este passo é opcional: a
        [cadeia de opções sobre futuros](https://brapi.dev/docs/futuros/opcoes/series)
        também aceita `minStrike` e `maxStrike`.

        Disponível no plano Pro. Sem token, aceita só `underlying=BGI`.

        Args:
          expiration_date: Data de vencimento, no formato YYYY-MM-DD. Veja os vencimentos em
              `/expirations`.

          underlying: Código do ativo do futuro. Ex.: `BGI`.

          side: Filtra por `call` ou `put`. Sem o filtro, retorna os dois.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/futures/options/strikes",
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
        return PositionsResourceWithRawResponse(self._options.positions)

    @cached_property
    def analytics(self) -> AnalyticsResourceWithRawResponse:
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
        return AsyncPositionsResourceWithRawResponse(self._options.positions)

    @cached_property
    def analytics(self) -> AsyncAnalyticsResourceWithRawResponse:
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
        return PositionsResourceWithStreamingResponse(self._options.positions)

    @cached_property
    def analytics(self) -> AnalyticsResourceWithStreamingResponse:
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
        return AsyncPositionsResourceWithStreamingResponse(self._options.positions)

    @cached_property
    def analytics(self) -> AsyncAnalyticsResourceWithStreamingResponse:
        return AsyncAnalyticsResourceWithStreamingResponse(self._options.analytics)
