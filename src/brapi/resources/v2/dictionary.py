# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v2 import dictionary_retrieve_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v2.dictionary_retrieve_response import DictionaryRetrieveResponse

__all__ = ["DictionaryResource", "AsyncDictionaryResource"]


class DictionaryResource(SyncAPIResource):
    """
    Ferramentas auxiliares para descobrir ativos disponíveis e verificar a saúde da API.
    """

    @cached_property
    def with_raw_response(self) -> DictionaryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return DictionaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DictionaryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return DictionaryResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        category: str | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DictionaryRetrieveResponse:
        """
        Lista os campos da API com nome em português, descrição, fórmula de cálculo,
        tipo, unidade, categoria e os endpoints onde cada campo aparece.

        Use para gerar rótulos e tooltips, formatar valores pela unidade e entender um
        campo antes de usar.

        `category` filtra por área, como `fii`, `treasury` ou `balance-sheet`. `search`
        busca em chave, nome, descrição, categoria e endpoints. Os dois funcionam
        juntos. Endpoint público, sem token.

        Args:
          category: Categoria exata do campo. Ex.: fii, treasury, quote, balance-sheet.

          search: Texto buscado em key, label, description, category e endpoints. Ignora
              maiúsculas.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/dictionary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "category": category,
                        "search": search,
                    },
                    dictionary_retrieve_params.DictionaryRetrieveParams,
                ),
            ),
            cast_to=DictionaryRetrieveResponse,
        )


class AsyncDictionaryResource(AsyncAPIResource):
    """
    Ferramentas auxiliares para descobrir ativos disponíveis e verificar a saúde da API.
    """

    @cached_property
    def with_raw_response(self) -> AsyncDictionaryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDictionaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDictionaryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncDictionaryResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        category: str | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DictionaryRetrieveResponse:
        """
        Lista os campos da API com nome em português, descrição, fórmula de cálculo,
        tipo, unidade, categoria e os endpoints onde cada campo aparece.

        Use para gerar rótulos e tooltips, formatar valores pela unidade e entender um
        campo antes de usar.

        `category` filtra por área, como `fii`, `treasury` ou `balance-sheet`. `search`
        busca em chave, nome, descrição, categoria e endpoints. Os dois funcionam
        juntos. Endpoint público, sem token.

        Args:
          category: Categoria exata do campo. Ex.: fii, treasury, quote, balance-sheet.

          search: Texto buscado em key, label, description, category e endpoints. Ignora
              maiúsculas.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/dictionary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "category": category,
                        "search": search,
                    },
                    dictionary_retrieve_params.DictionaryRetrieveParams,
                ),
            ),
            cast_to=DictionaryRetrieveResponse,
        )


class DictionaryResourceWithRawResponse:
    def __init__(self, dictionary: DictionaryResource) -> None:
        self._dictionary = dictionary

        self.retrieve = to_raw_response_wrapper(
            dictionary.retrieve,
        )


class AsyncDictionaryResourceWithRawResponse:
    def __init__(self, dictionary: AsyncDictionaryResource) -> None:
        self._dictionary = dictionary

        self.retrieve = async_to_raw_response_wrapper(
            dictionary.retrieve,
        )


class DictionaryResourceWithStreamingResponse:
    def __init__(self, dictionary: DictionaryResource) -> None:
        self._dictionary = dictionary

        self.retrieve = to_streamed_response_wrapper(
            dictionary.retrieve,
        )


class AsyncDictionaryResourceWithStreamingResponse:
    def __init__(self, dictionary: AsyncDictionaryResource) -> None:
        self._dictionary = dictionary

        self.retrieve = async_to_streamed_response_wrapper(
            dictionary.retrieve,
        )
