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
from ....types.v2.funds import nav_history_params
from ....types.v2.funds.nav_history_response import NavHistoryResponse

__all__ = ["NavResource", "AsyncNavResource"]


class NavResource(SyncAPIResource):
    """
    Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
    """

    @cached_property
    def with_raw_response(self) -> NavResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return NavResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NavResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return NavResourceWithStreamingResponse(self)

    def history(
        self,
        *,
        cnpjs: str | Omit = omit,
        end_date: str | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        symbols: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NavHistoryResponse:
        """
        Série do valor patrimonial por cota, com patrimônio, ativos, cotistas,
        aplicações e resgates. FI e FIF podem ter pontos diários. A cobertura varia por
        CNPJ. Alguns fundos não têm histórico disponível. FIDC tem pontos mensais por
        classe ou série, com a rentabilidade do mês em `monthlyReturn`.

        Use para gráficos de valor da cota, cálculo de rentabilidade e acompanhamento do
        patrimônio.

        Informe `symbols` ou `cnpjs`. Os filtros de data usam o campo `date`.

        Este é o valor patrimonial, não o preço negociado em bolsa. Para comparar um FI
        com um FIDC, alinhe os pontos por mês.

        Plano Pro.

        Args:
          cnpjs: CNPJs separados por vírgula, até 20, com ou sem pontuação.

          end_date: Data final no formato YYYY-MM-DD.

          limit: Itens por página.

          page: Número da página, a partir de 1.

          sort_order: Ordem crescente (`asc`) ou decrescente (`desc`).

          start_date: Data inicial no formato YYYY-MM-DD.

          symbols: Tickers separados por vírgula, até 20. Ex.: JURO11,XPCA11.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/funds/nav/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cnpjs": cnpjs,
                        "end_date": end_date,
                        "limit": limit,
                        "page": page,
                        "sort_order": sort_order,
                        "start_date": start_date,
                        "symbols": symbols,
                    },
                    nav_history_params.NavHistoryParams,
                ),
            ),
            cast_to=NavHistoryResponse,
        )


class AsyncNavResource(AsyncAPIResource):
    """
    Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
    """

    @cached_property
    def with_raw_response(self) -> AsyncNavResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNavResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNavResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncNavResourceWithStreamingResponse(self)

    async def history(
        self,
        *,
        cnpjs: str | Omit = omit,
        end_date: str | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        symbols: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NavHistoryResponse:
        """
        Série do valor patrimonial por cota, com patrimônio, ativos, cotistas,
        aplicações e resgates. FI e FIF podem ter pontos diários. A cobertura varia por
        CNPJ. Alguns fundos não têm histórico disponível. FIDC tem pontos mensais por
        classe ou série, com a rentabilidade do mês em `monthlyReturn`.

        Use para gráficos de valor da cota, cálculo de rentabilidade e acompanhamento do
        patrimônio.

        Informe `symbols` ou `cnpjs`. Os filtros de data usam o campo `date`.

        Este é o valor patrimonial, não o preço negociado em bolsa. Para comparar um FI
        com um FIDC, alinhe os pontos por mês.

        Plano Pro.

        Args:
          cnpjs: CNPJs separados por vírgula, até 20, com ou sem pontuação.

          end_date: Data final no formato YYYY-MM-DD.

          limit: Itens por página.

          page: Número da página, a partir de 1.

          sort_order: Ordem crescente (`asc`) ou decrescente (`desc`).

          start_date: Data inicial no formato YYYY-MM-DD.

          symbols: Tickers separados por vírgula, até 20. Ex.: JURO11,XPCA11.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/funds/nav/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cnpjs": cnpjs,
                        "end_date": end_date,
                        "limit": limit,
                        "page": page,
                        "sort_order": sort_order,
                        "start_date": start_date,
                        "symbols": symbols,
                    },
                    nav_history_params.NavHistoryParams,
                ),
            ),
            cast_to=NavHistoryResponse,
        )


class NavResourceWithRawResponse:
    def __init__(self, nav: NavResource) -> None:
        self._nav = nav

        self.history = to_raw_response_wrapper(
            nav.history,
        )


class AsyncNavResourceWithRawResponse:
    def __init__(self, nav: AsyncNavResource) -> None:
        self._nav = nav

        self.history = async_to_raw_response_wrapper(
            nav.history,
        )


class NavResourceWithStreamingResponse:
    def __init__(self, nav: NavResource) -> None:
        self._nav = nav

        self.history = to_streamed_response_wrapper(
            nav.history,
        )


class AsyncNavResourceWithStreamingResponse:
    def __init__(self, nav: AsyncNavResource) -> None:
        self._nav = nav

        self.history = async_to_streamed_response_wrapper(
            nav.history,
        )
