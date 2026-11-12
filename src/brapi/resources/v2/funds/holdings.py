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
from ....types.v2.funds import holding_history_params
from ....types.v2.funds.holding_history_response import HoldingHistoryResponse

__all__ = ["HoldingsResource", "AsyncHoldingsResource"]


class HoldingsResource(SyncAPIResource):
    """
    Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
    """

    @cached_property
    def with_raw_response(self) -> HoldingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return HoldingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HoldingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return HoldingsResourceWithStreamingResponse(self)

    def history(
        self,
        *,
        asset: str | Omit = omit,
        asset_cnpj: str | Omit = omit,
        cnpj: str | Omit = omit,
        end_date: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        symbol: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HoldingHistoryResponse:
        """
        A posição de um fundo em um ativo, mês a mês: peso no patrimônio, valor e
        quantidade. Os dados vêm da carteira mensal que os fundos entregam à CVM.

        Use para ver quando um fundo ou ETF comprou ou vendeu uma ação, ou como mudou o
        peso de um ativo na carteira.

        Informe o fundo (`symbol` ou `cnpj`) e o ativo (`asset` com o ticker, ou
        `assetCnpj` com o CNPJ de um fundo ou de uma empresa, como em
        `/api/v2/funds/holders`). Sem datas, a resposta traz os últimos 24 meses.

        Um mês em que o fundo entregou a carteira sem o ativo aparece com zeros. Um mês
        sem carteira não aparece.

        Só posições diretas: o ativo detido por meio de outro fundo não entra. Ações
        próprias e emprestadas somam uma posição. Derivativos, valores a pagar e
        posições confidenciais não entram.

        Plano Pro.

        Args:
          asset: Ticker do ativo na bolsa. Ex.: PETR4.

          asset_cnpj: CNPJ de um fundo, para as cotas dele, ou de uma empresa, para as ações e a
              dívida dela. Use `asset` ou `assetCnpj`, não os dois.

          cnpj: CNPJ do fundo, com ou sem pontuação. Use `symbol` ou `cnpj`, não os dois.

          end_date: Data final no formato YYYY-MM-DD. Padrão: hoje.

          sort_order: Do mês mais antigo (`asc`) ou do mais recente (`desc`, padrão).

          start_date: Data inicial no formato YYYY-MM-DD. Padrão: 24 meses antes de `endDate`.

          symbol: Ticker do fundo. Ex.: BOVA11.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/funds/holdings/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asset": asset,
                        "asset_cnpj": asset_cnpj,
                        "cnpj": cnpj,
                        "end_date": end_date,
                        "sort_order": sort_order,
                        "start_date": start_date,
                        "symbol": symbol,
                    },
                    holding_history_params.HoldingHistoryParams,
                ),
            ),
            cast_to=HoldingHistoryResponse,
        )


class AsyncHoldingsResource(AsyncAPIResource):
    """
    Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
    """

    @cached_property
    def with_raw_response(self) -> AsyncHoldingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHoldingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHoldingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncHoldingsResourceWithStreamingResponse(self)

    async def history(
        self,
        *,
        asset: str | Omit = omit,
        asset_cnpj: str | Omit = omit,
        cnpj: str | Omit = omit,
        end_date: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        symbol: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HoldingHistoryResponse:
        """
        A posição de um fundo em um ativo, mês a mês: peso no patrimônio, valor e
        quantidade. Os dados vêm da carteira mensal que os fundos entregam à CVM.

        Use para ver quando um fundo ou ETF comprou ou vendeu uma ação, ou como mudou o
        peso de um ativo na carteira.

        Informe o fundo (`symbol` ou `cnpj`) e o ativo (`asset` com o ticker, ou
        `assetCnpj` com o CNPJ de um fundo ou de uma empresa, como em
        `/api/v2/funds/holders`). Sem datas, a resposta traz os últimos 24 meses.

        Um mês em que o fundo entregou a carteira sem o ativo aparece com zeros. Um mês
        sem carteira não aparece.

        Só posições diretas: o ativo detido por meio de outro fundo não entra. Ações
        próprias e emprestadas somam uma posição. Derivativos, valores a pagar e
        posições confidenciais não entram.

        Plano Pro.

        Args:
          asset: Ticker do ativo na bolsa. Ex.: PETR4.

          asset_cnpj: CNPJ de um fundo, para as cotas dele, ou de uma empresa, para as ações e a
              dívida dela. Use `asset` ou `assetCnpj`, não os dois.

          cnpj: CNPJ do fundo, com ou sem pontuação. Use `symbol` ou `cnpj`, não os dois.

          end_date: Data final no formato YYYY-MM-DD. Padrão: hoje.

          sort_order: Do mês mais antigo (`asc`) ou do mais recente (`desc`, padrão).

          start_date: Data inicial no formato YYYY-MM-DD. Padrão: 24 meses antes de `endDate`.

          symbol: Ticker do fundo. Ex.: BOVA11.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/funds/holdings/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asset": asset,
                        "asset_cnpj": asset_cnpj,
                        "cnpj": cnpj,
                        "end_date": end_date,
                        "sort_order": sort_order,
                        "start_date": start_date,
                        "symbol": symbol,
                    },
                    holding_history_params.HoldingHistoryParams,
                ),
            ),
            cast_to=HoldingHistoryResponse,
        )


class HoldingsResourceWithRawResponse:
    def __init__(self, holdings: HoldingsResource) -> None:
        self._holdings = holdings

        self.history = to_raw_response_wrapper(
            holdings.history,
        )


class AsyncHoldingsResourceWithRawResponse:
    def __init__(self, holdings: AsyncHoldingsResource) -> None:
        self._holdings = holdings

        self.history = async_to_raw_response_wrapper(
            holdings.history,
        )


class HoldingsResourceWithStreamingResponse:
    def __init__(self, holdings: HoldingsResource) -> None:
        self._holdings = holdings

        self.history = to_streamed_response_wrapper(
            holdings.history,
        )


class AsyncHoldingsResourceWithStreamingResponse:
    def __init__(self, holdings: AsyncHoldingsResource) -> None:
        self._holdings = holdings

        self.history = async_to_streamed_response_wrapper(
            holdings.history,
        )
