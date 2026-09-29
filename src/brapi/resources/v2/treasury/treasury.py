# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from .indicators import (
    IndicatorsResource,
    AsyncIndicatorsResource,
    IndicatorsResourceWithRawResponse,
    AsyncIndicatorsResourceWithRawResponse,
    IndicatorsResourceWithStreamingResponse,
    AsyncIndicatorsResourceWithStreamingResponse,
)
from ....types.v2 import treasury_list_params
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v2.treasury_list_response import TreasuryListResponse

__all__ = ["TreasuryResource", "AsyncTreasuryResource"]


class TreasuryResource(SyncAPIResource):
    """
    Consulte dados de títulos públicos e outros instrumentos de renda fixa brasileira.
    """

    @cached_property
    def indicators(self) -> IndicatorsResource:
        """
        Consulte dados de títulos públicos e outros instrumentos de renda fixa brasileira.
        """
        return IndicatorsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TreasuryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return TreasuryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TreasuryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return TreasuryResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        coupon_type: Literal["zero", "semestral"] | Omit = omit,
        indexer: Literal["selic", "prefixado", "ipca", "igpm"] | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        search: str | Omit = omit,
        sort_by: Literal[
            "symbol",
            "bondType",
            "maturityDate",
            "durationDays",
            "baseDate",
            "buyRate",
            "sellRate",
            "buyPrice",
            "sellPrice",
            "basePrice",
        ]
        | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TreasuryListResponse:
        """
        Títulos do Tesouro Direto da data-base mais recente, com taxa e preço
        indicativos de compra e venda. Filtre por indexador, tipo de cupom ou nome.

        Use para achar o `symbol` de cada título, montar uma tabela de títulos ou
        comparar taxas entre vencimentos.

        Cada item traz `rateInfo`, que diz como ler `buyRate` e `sellRate` para aquele
        indexador.

        Plano Pro. Sem token, `search` precisa ser um destes códigos:
        `tesouro-selic-01032031`, `tesouro-prefixado-com-juros-semestrais-01012037` ou
        `tesouro-ipca-com-juros-semestrais-15082060`.

        Args:
          coupon_type: Tipo de cupom do título.

          indexer: Indexador do título.

          limit: Itens por página.

          page: Número da página, a partir de 1.

          search: Busca por parte do código ou do nome do título. Ex.: tesouro-selic-01032031.

          sort_by: Campo usado na ordenação.

          sort_order: Direção da ordenação.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/treasury/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "coupon_type": coupon_type,
                        "indexer": indexer,
                        "limit": limit,
                        "page": page,
                        "search": search,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                    },
                    treasury_list_params.TreasuryListParams,
                ),
            ),
            cast_to=TreasuryListResponse,
        )


class AsyncTreasuryResource(AsyncAPIResource):
    """
    Consulte dados de títulos públicos e outros instrumentos de renda fixa brasileira.
    """

    @cached_property
    def indicators(self) -> AsyncIndicatorsResource:
        """
        Consulte dados de títulos públicos e outros instrumentos de renda fixa brasileira.
        """
        return AsyncIndicatorsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTreasuryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTreasuryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTreasuryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncTreasuryResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        coupon_type: Literal["zero", "semestral"] | Omit = omit,
        indexer: Literal["selic", "prefixado", "ipca", "igpm"] | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        search: str | Omit = omit,
        sort_by: Literal[
            "symbol",
            "bondType",
            "maturityDate",
            "durationDays",
            "baseDate",
            "buyRate",
            "sellRate",
            "buyPrice",
            "sellPrice",
            "basePrice",
        ]
        | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TreasuryListResponse:
        """
        Títulos do Tesouro Direto da data-base mais recente, com taxa e preço
        indicativos de compra e venda. Filtre por indexador, tipo de cupom ou nome.

        Use para achar o `symbol` de cada título, montar uma tabela de títulos ou
        comparar taxas entre vencimentos.

        Cada item traz `rateInfo`, que diz como ler `buyRate` e `sellRate` para aquele
        indexador.

        Plano Pro. Sem token, `search` precisa ser um destes códigos:
        `tesouro-selic-01032031`, `tesouro-prefixado-com-juros-semestrais-01012037` ou
        `tesouro-ipca-com-juros-semestrais-15082060`.

        Args:
          coupon_type: Tipo de cupom do título.

          indexer: Indexador do título.

          limit: Itens por página.

          page: Número da página, a partir de 1.

          search: Busca por parte do código ou do nome do título. Ex.: tesouro-selic-01032031.

          sort_by: Campo usado na ordenação.

          sort_order: Direção da ordenação.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/treasury/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "coupon_type": coupon_type,
                        "indexer": indexer,
                        "limit": limit,
                        "page": page,
                        "search": search,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                    },
                    treasury_list_params.TreasuryListParams,
                ),
            ),
            cast_to=TreasuryListResponse,
        )


class TreasuryResourceWithRawResponse:
    def __init__(self, treasury: TreasuryResource) -> None:
        self._treasury = treasury

        self.list = to_raw_response_wrapper(
            treasury.list,
        )

    @cached_property
    def indicators(self) -> IndicatorsResourceWithRawResponse:
        """
        Consulte dados de títulos públicos e outros instrumentos de renda fixa brasileira.
        """
        return IndicatorsResourceWithRawResponse(self._treasury.indicators)


class AsyncTreasuryResourceWithRawResponse:
    def __init__(self, treasury: AsyncTreasuryResource) -> None:
        self._treasury = treasury

        self.list = async_to_raw_response_wrapper(
            treasury.list,
        )

    @cached_property
    def indicators(self) -> AsyncIndicatorsResourceWithRawResponse:
        """
        Consulte dados de títulos públicos e outros instrumentos de renda fixa brasileira.
        """
        return AsyncIndicatorsResourceWithRawResponse(self._treasury.indicators)


class TreasuryResourceWithStreamingResponse:
    def __init__(self, treasury: TreasuryResource) -> None:
        self._treasury = treasury

        self.list = to_streamed_response_wrapper(
            treasury.list,
        )

    @cached_property
    def indicators(self) -> IndicatorsResourceWithStreamingResponse:
        """
        Consulte dados de títulos públicos e outros instrumentos de renda fixa brasileira.
        """
        return IndicatorsResourceWithStreamingResponse(self._treasury.indicators)


class AsyncTreasuryResourceWithStreamingResponse:
    def __init__(self, treasury: AsyncTreasuryResource) -> None:
        self._treasury = treasury

        self.list = async_to_streamed_response_wrapper(
            treasury.list,
        )

    @cached_property
    def indicators(self) -> AsyncIndicatorsResourceWithStreamingResponse:
        """
        Consulte dados de títulos públicos e outros instrumentos de renda fixa brasileira.
        """
        return AsyncIndicatorsResourceWithStreamingResponse(self._treasury.indicators)
