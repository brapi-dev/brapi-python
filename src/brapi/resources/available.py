# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import available_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.available_list_response import AvailableListResponse

__all__ = ["AvailableResource", "AsyncAvailableResource"]


class AvailableResource(SyncAPIResource):
    """
    Ferramentas auxiliares para descobrir ativos disponíveis e verificar a saúde da API.
    """

    @cached_property
    def with_raw_response(self) -> AvailableResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AvailableResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AvailableResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AvailableResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AvailableListResponse:
        """
        Lista todos os ativos que a API aceita: ações, FIIs, BDRs e ETFs da B3, mais os
        índices com cotação disponível.

        Filtre por código ou nome com `search`.

        ```bash
        curl "https://brapi.dev/api/available?search=PETR"
        ```

        Endpoint público, sem token. A resposta fica em cache por 15 minutos e é
        atualizada conforme novos ativos entram na bolsa.

        Para busca com filtros por setor e tipo, `/api/v2/tickers` é mais completo.

        Args:
          search: Filtrar ações e índices por nome ou código

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/available",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"search": search}, available_list_params.AvailableListParams),
            ),
            cast_to=AvailableListResponse,
        )


class AsyncAvailableResource(AsyncAPIResource):
    """
    Ferramentas auxiliares para descobrir ativos disponíveis e verificar a saúde da API.
    """

    @cached_property
    def with_raw_response(self) -> AsyncAvailableResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAvailableResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAvailableResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncAvailableResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AvailableListResponse:
        """
        Lista todos os ativos que a API aceita: ações, FIIs, BDRs e ETFs da B3, mais os
        índices com cotação disponível.

        Filtre por código ou nome com `search`.

        ```bash
        curl "https://brapi.dev/api/available?search=PETR"
        ```

        Endpoint público, sem token. A resposta fica em cache por 15 minutos e é
        atualizada conforme novos ativos entram na bolsa.

        Para busca com filtros por setor e tipo, `/api/v2/tickers` é mais completo.

        Args:
          search: Filtrar ações e índices por nome ou código

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/available",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"search": search}, available_list_params.AvailableListParams),
            ),
            cast_to=AvailableListResponse,
        )


class AvailableResourceWithRawResponse:
    def __init__(self, available: AvailableResource) -> None:
        self._available = available

        self.list = to_raw_response_wrapper(
            available.list,
        )


class AsyncAvailableResourceWithRawResponse:
    def __init__(self, available: AsyncAvailableResource) -> None:
        self._available = available

        self.list = async_to_raw_response_wrapper(
            available.list,
        )


class AvailableResourceWithStreamingResponse:
    def __init__(self, available: AvailableResource) -> None:
        self._available = available

        self.list = to_streamed_response_wrapper(
            available.list,
        )


class AsyncAvailableResourceWithStreamingResponse:
    def __init__(self, available: AsyncAvailableResource) -> None:
        self._available = available

        self.list = async_to_streamed_response_wrapper(
            available.list,
        )
