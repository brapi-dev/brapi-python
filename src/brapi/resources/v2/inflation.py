# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v2 import inflation_retrieve_params, inflation_list_available_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v2.inflation_retrieve_response import InflationRetrieveResponse
from ...types.v2.inflation_list_available_response import InflationListAvailableResponse

__all__ = ["InflationResource", "AsyncInflationResource"]


class InflationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InflationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return InflationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InflationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return InflationResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        end: str | Omit = omit,
        historical: str | Omit = omit,
        sort_by: str | Omit = omit,
        sort_order: str | Omit = omit,
        start: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InflationRetrieveResponse:
        """
        Série mensal do IPCA acumulado em 12 meses, o índice oficial de inflação do
        Brasil. Cada ponto é o acumulado dos 12 meses até aquela data.

        Endpoint descontinuado. Use as
        [séries macroeconômicas](https://brapi.dev/docs/macro) com `symbols=ipca12m`
        para o acumulado ou `symbols=ipca` para a variação do mês.

        Sem filtros, devolve os últimos 12 meses. Filtre com `start` e `end` no formato
        `DD/MM/YYYY`. O IPCA de um mês sai no mês seguinte.

        Planos Startup e Pro.

        Args:
          end: Data final no formato DD/MM/YYYY. Padrão: hoje.

          historical: true devolve a série desde 01/01/2000. Sem datas e sem este parâmetro, devolve
              os últimos 12 meses.

          sort_by: Campo de ordenação: date ou value. Padrão: date.

          sort_order: Ordem: asc ou desc. Padrão: desc.

          start: Data inicial no formato DD/MM/YYYY.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/inflation",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "historical": historical,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "start": start,
                    },
                    inflation_retrieve_params.InflationRetrieveParams,
                ),
            ),
            cast_to=InflationRetrieveResponse,
        )

    def list_available(
        self,
        *,
        format: Literal["json"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InflationListAvailableResponse:
        """Lista os países que o endpoint de inflação aceita.

        Hoje só `brazil`.

        Endpoint descontinuado. Use as
        [séries macroeconômicas](https://brapi.dev/docs/macro). Planos Startup e Pro.

        Args:
          format: Formato da resposta. Só aceita json.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/inflation/available",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"format": format}, inflation_list_available_params.InflationListAvailableParams),
            ),
            cast_to=InflationListAvailableResponse,
        )


class AsyncInflationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInflationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInflationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInflationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncInflationResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        end: str | Omit = omit,
        historical: str | Omit = omit,
        sort_by: str | Omit = omit,
        sort_order: str | Omit = omit,
        start: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InflationRetrieveResponse:
        """
        Série mensal do IPCA acumulado em 12 meses, o índice oficial de inflação do
        Brasil. Cada ponto é o acumulado dos 12 meses até aquela data.

        Endpoint descontinuado. Use as
        [séries macroeconômicas](https://brapi.dev/docs/macro) com `symbols=ipca12m`
        para o acumulado ou `symbols=ipca` para a variação do mês.

        Sem filtros, devolve os últimos 12 meses. Filtre com `start` e `end` no formato
        `DD/MM/YYYY`. O IPCA de um mês sai no mês seguinte.

        Planos Startup e Pro.

        Args:
          end: Data final no formato DD/MM/YYYY. Padrão: hoje.

          historical: true devolve a série desde 01/01/2000. Sem datas e sem este parâmetro, devolve
              os últimos 12 meses.

          sort_by: Campo de ordenação: date ou value. Padrão: date.

          sort_order: Ordem: asc ou desc. Padrão: desc.

          start: Data inicial no formato DD/MM/YYYY.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/inflation",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end": end,
                        "historical": historical,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "start": start,
                    },
                    inflation_retrieve_params.InflationRetrieveParams,
                ),
            ),
            cast_to=InflationRetrieveResponse,
        )

    async def list_available(
        self,
        *,
        format: Literal["json"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InflationListAvailableResponse:
        """Lista os países que o endpoint de inflação aceita.

        Hoje só `brazil`.

        Endpoint descontinuado. Use as
        [séries macroeconômicas](https://brapi.dev/docs/macro). Planos Startup e Pro.

        Args:
          format: Formato da resposta. Só aceita json.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/inflation/available",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"format": format}, inflation_list_available_params.InflationListAvailableParams
                ),
            ),
            cast_to=InflationListAvailableResponse,
        )


class InflationResourceWithRawResponse:
    def __init__(self, inflation: InflationResource) -> None:
        self._inflation = inflation

        self.retrieve = to_raw_response_wrapper(
            inflation.retrieve,
        )
        self.list_available = to_raw_response_wrapper(
            inflation.list_available,
        )


class AsyncInflationResourceWithRawResponse:
    def __init__(self, inflation: AsyncInflationResource) -> None:
        self._inflation = inflation

        self.retrieve = async_to_raw_response_wrapper(
            inflation.retrieve,
        )
        self.list_available = async_to_raw_response_wrapper(
            inflation.list_available,
        )


class InflationResourceWithStreamingResponse:
    def __init__(self, inflation: InflationResource) -> None:
        self._inflation = inflation

        self.retrieve = to_streamed_response_wrapper(
            inflation.retrieve,
        )
        self.list_available = to_streamed_response_wrapper(
            inflation.list_available,
        )


class AsyncInflationResourceWithStreamingResponse:
    def __init__(self, inflation: AsyncInflationResource) -> None:
        self._inflation = inflation

        self.retrieve = async_to_streamed_response_wrapper(
            inflation.retrieve,
        )
        self.list_available = async_to_streamed_response_wrapper(
            inflation.list_available,
        )
