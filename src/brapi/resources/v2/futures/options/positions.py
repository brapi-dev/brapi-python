# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

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
from .....types.v2.futures.options import position_history_params, position_retrieve_params
from .....types.v2.futures.options.position_history_response import PositionHistoryResponse
from .....types.v2.futures.options.position_retrieve_response import PositionRetrieveResponse

__all__ = ["PositionsResource", "AsyncPositionsResource"]


class PositionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PositionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return PositionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PositionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return PositionsResourceWithStreamingResponse(self)

    def retrieve(
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
    ) -> PositionRetrieveResponse:
        """
        Retorna os contratos em aberto de cada série de opções sobre futuro de um
        vencimento.

        Use para ver onde se concentram as posições por strike, comparar calls e puts e
        acompanhar a variação diária de contratos em aberto.

        Use `openInterest` como número de contratos em aberto. Aqui ele repete
        `reportedOpenInterest`. Os campos de posição coberta, descoberta, bloqueada e de
        empréstimo vêm vazios na maior parte dos segmentos de futuros. Volume e
        contratos em aberto medem coisas diferentes: uma série pode ficar sem negócio e
        ter muitos contratos em aberto.

        Os contratos em aberto são apurados uma vez por pregão. Sem apuração na data
        pedida, a resposta traz a anterior. Confira `openInterestDate` antes de comparar
        com o preço do dia.

        Aceita os mesmos filtros da
        [cadeia de opções sobre futuros](https://brapi.dev/docs/futuros/opcoes/series):
        `side`, `minStrike` e `maxStrike`.

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
            "/api/v2/futures/options/positions",
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
                    position_retrieve_params.PositionRetrieveParams,
                ),
            ),
            cast_to=PositionRetrieveResponse,
        )

    def history(
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
    ) -> PositionHistoryResponse:
        """
        Retorna o histórico diário de contratos em aberto de uma opção sobre futuro,
        identificada por `symbol`.

        Use para ver a montagem e a desmontagem de posições ao longo do tempo e comparar
        contratos em aberto com o preço.

        Cada item é uma apuração diária. Pregão sem apuração não aparece.

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
            "/api/v2/futures/options/positions/history",
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
                    position_history_params.PositionHistoryParams,
                ),
            ),
            cast_to=PositionHistoryResponse,
        )


class AsyncPositionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPositionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPositionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPositionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncPositionsResourceWithStreamingResponse(self)

    async def retrieve(
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
    ) -> PositionRetrieveResponse:
        """
        Retorna os contratos em aberto de cada série de opções sobre futuro de um
        vencimento.

        Use para ver onde se concentram as posições por strike, comparar calls e puts e
        acompanhar a variação diária de contratos em aberto.

        Use `openInterest` como número de contratos em aberto. Aqui ele repete
        `reportedOpenInterest`. Os campos de posição coberta, descoberta, bloqueada e de
        empréstimo vêm vazios na maior parte dos segmentos de futuros. Volume e
        contratos em aberto medem coisas diferentes: uma série pode ficar sem negócio e
        ter muitos contratos em aberto.

        Os contratos em aberto são apurados uma vez por pregão. Sem apuração na data
        pedida, a resposta traz a anterior. Confira `openInterestDate` antes de comparar
        com o preço do dia.

        Aceita os mesmos filtros da
        [cadeia de opções sobre futuros](https://brapi.dev/docs/futuros/opcoes/series):
        `side`, `minStrike` e `maxStrike`.

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
            "/api/v2/futures/options/positions",
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
                    position_retrieve_params.PositionRetrieveParams,
                ),
            ),
            cast_to=PositionRetrieveResponse,
        )

    async def history(
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
    ) -> PositionHistoryResponse:
        """
        Retorna o histórico diário de contratos em aberto de uma opção sobre futuro,
        identificada por `symbol`.

        Use para ver a montagem e a desmontagem de posições ao longo do tempo e comparar
        contratos em aberto com o preço.

        Cada item é uma apuração diária. Pregão sem apuração não aparece.

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
            "/api/v2/futures/options/positions/history",
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
                    position_history_params.PositionHistoryParams,
                ),
            ),
            cast_to=PositionHistoryResponse,
        )


class PositionsResourceWithRawResponse:
    def __init__(self, positions: PositionsResource) -> None:
        self._positions = positions

        self.retrieve = to_raw_response_wrapper(
            positions.retrieve,
        )
        self.history = to_raw_response_wrapper(
            positions.history,
        )


class AsyncPositionsResourceWithRawResponse:
    def __init__(self, positions: AsyncPositionsResource) -> None:
        self._positions = positions

        self.retrieve = async_to_raw_response_wrapper(
            positions.retrieve,
        )
        self.history = async_to_raw_response_wrapper(
            positions.history,
        )


class PositionsResourceWithStreamingResponse:
    def __init__(self, positions: PositionsResource) -> None:
        self._positions = positions

        self.retrieve = to_streamed_response_wrapper(
            positions.retrieve,
        )
        self.history = to_streamed_response_wrapper(
            positions.history,
        )


class AsyncPositionsResourceWithStreamingResponse:
    def __init__(self, positions: AsyncPositionsResource) -> None:
        self._positions = positions

        self.retrieve = async_to_streamed_response_wrapper(
            positions.retrieve,
        )
        self.history = async_to_streamed_response_wrapper(
            positions.history,
        )
