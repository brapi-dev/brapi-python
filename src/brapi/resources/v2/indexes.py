# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v2 import index_list_params, index_composition_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v2.index_list_response import IndexListResponse
from ...types.v2.index_composition_response import IndexCompositionResponse

__all__ = ["IndexesResource", "AsyncIndexesResource"]


class IndexesResource(SyncAPIResource):
    """
    Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
    """

    @cached_property
    def with_raw_response(self) -> IndexesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return IndexesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IndexesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return IndexesResourceWithStreamingResponse(self)

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
    ) -> IndexListResponse:
        """
        Índices com composição em `/api/v2/indexes/composition`, cada um com o ETF que o
        replica e o mês da carteira mais recente.

        A bolsa não licencia a carteira oficial dos índices. A composição é a carteira
        do maior ETF que replica o índice, da carteira mensal que o ETF entrega à CVM.

        Plano Pro.

        Args:
          search: Busca por parte da sigla ou do nome do índice, ou do ticker do ETF. Ex.: ibov.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/indexes/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"search": search}, index_list_params.IndexListParams),
            ),
            cast_to=IndexListResponse,
        )

    def composition(
        self,
        *,
        symbols: str,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        reference_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IndexCompositionResponse:
        """
        Ativos de um índice e o peso de cada um, com o resumo por país e setor.

        A bolsa não licencia a carteira oficial dos índices. A composição é a carteira
        do maior ETF que replica o índice, da carteira mensal que o ETF entrega à CVM.
        Por isso, `approximated` é sempre `true` e `trackingFund` mostra o ETF.

        Os pesos são da parte investida do ETF: sem caixa, valores a receber e a pagar,
        compromissadas e derivativos, e somam 100. Quando o ETF tem cotas de um ETF do
        exterior, a resposta mostra os ativos desse ETF, pelos relatórios públicos do
        fundo no exterior (SEC).

        Sem `referenceDate`, a resposta traz o mês mais recente. Com ela, traz o mês
        mais recente até essa data. Mostre `referenceDate` junto do dado: a CVM publica
        a carteira com meses de atraso.

        Plano Pro.

        Args:
          symbols: Índices separados por vírgula, até 20. Veja os aceitos em
              `/api/v2/indexes/list`. Ex.: IBOV,SMLL.

          limit: Ativos por índice e por página. Padrão 10, máximo 500.

          page: Página, a partir de 1.

          reference_date: Data no formato YYYY-MM-DD. Traz o mês mais recente até esta data. Sem ela, traz
              o mês mais recente.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/indexes/composition",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "symbols": symbols,
                        "limit": limit,
                        "page": page,
                        "reference_date": reference_date,
                    },
                    index_composition_params.IndexCompositionParams,
                ),
            ),
            cast_to=IndexCompositionResponse,
        )


class AsyncIndexesResource(AsyncAPIResource):
    """
    Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
    """

    @cached_property
    def with_raw_response(self) -> AsyncIndexesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIndexesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIndexesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncIndexesResourceWithStreamingResponse(self)

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
    ) -> IndexListResponse:
        """
        Índices com composição em `/api/v2/indexes/composition`, cada um com o ETF que o
        replica e o mês da carteira mais recente.

        A bolsa não licencia a carteira oficial dos índices. A composição é a carteira
        do maior ETF que replica o índice, da carteira mensal que o ETF entrega à CVM.

        Plano Pro.

        Args:
          search: Busca por parte da sigla ou do nome do índice, ou do ticker do ETF. Ex.: ibov.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/indexes/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"search": search}, index_list_params.IndexListParams),
            ),
            cast_to=IndexListResponse,
        )

    async def composition(
        self,
        *,
        symbols: str,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        reference_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IndexCompositionResponse:
        """
        Ativos de um índice e o peso de cada um, com o resumo por país e setor.

        A bolsa não licencia a carteira oficial dos índices. A composição é a carteira
        do maior ETF que replica o índice, da carteira mensal que o ETF entrega à CVM.
        Por isso, `approximated` é sempre `true` e `trackingFund` mostra o ETF.

        Os pesos são da parte investida do ETF: sem caixa, valores a receber e a pagar,
        compromissadas e derivativos, e somam 100. Quando o ETF tem cotas de um ETF do
        exterior, a resposta mostra os ativos desse ETF, pelos relatórios públicos do
        fundo no exterior (SEC).

        Sem `referenceDate`, a resposta traz o mês mais recente. Com ela, traz o mês
        mais recente até essa data. Mostre `referenceDate` junto do dado: a CVM publica
        a carteira com meses de atraso.

        Plano Pro.

        Args:
          symbols: Índices separados por vírgula, até 20. Veja os aceitos em
              `/api/v2/indexes/list`. Ex.: IBOV,SMLL.

          limit: Ativos por índice e por página. Padrão 10, máximo 500.

          page: Página, a partir de 1.

          reference_date: Data no formato YYYY-MM-DD. Traz o mês mais recente até esta data. Sem ela, traz
              o mês mais recente.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/indexes/composition",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "symbols": symbols,
                        "limit": limit,
                        "page": page,
                        "reference_date": reference_date,
                    },
                    index_composition_params.IndexCompositionParams,
                ),
            ),
            cast_to=IndexCompositionResponse,
        )


class IndexesResourceWithRawResponse:
    def __init__(self, indexes: IndexesResource) -> None:
        self._indexes = indexes

        self.list = to_raw_response_wrapper(
            indexes.list,
        )
        self.composition = to_raw_response_wrapper(
            indexes.composition,
        )


class AsyncIndexesResourceWithRawResponse:
    def __init__(self, indexes: AsyncIndexesResource) -> None:
        self._indexes = indexes

        self.list = async_to_raw_response_wrapper(
            indexes.list,
        )
        self.composition = async_to_raw_response_wrapper(
            indexes.composition,
        )


class IndexesResourceWithStreamingResponse:
    def __init__(self, indexes: IndexesResource) -> None:
        self._indexes = indexes

        self.list = to_streamed_response_wrapper(
            indexes.list,
        )
        self.composition = to_streamed_response_wrapper(
            indexes.composition,
        )


class AsyncIndexesResourceWithStreamingResponse:
    def __init__(self, indexes: AsyncIndexesResource) -> None:
        self._indexes = indexes

        self.list = async_to_streamed_response_wrapper(
            indexes.list,
        )
        self.composition = async_to_streamed_response_wrapper(
            indexes.composition,
        )
