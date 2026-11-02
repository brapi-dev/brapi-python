# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v2 import revenue_source_compare_params, revenue_source_retrieve_params, revenue_source_activities_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v2.revenue_source_compare_response import RevenueSourceCompareResponse
from ...types.v2.revenue_source_retrieve_response import RevenueSourceRetrieveResponse
from ...types.v2.revenue_source_activities_response import RevenueSourceActivitiesResponse

__all__ = ["RevenueSourcesResource", "AsyncRevenueSourcesResource"]


class RevenueSourcesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RevenueSourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return RevenueSourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RevenueSourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return RevenueSourcesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        cnpjs: str | Omit = omit,
        end_year: int | Omit = omit,
        start_year: int | Omit = omit,
        symbols: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RevenueSourceRetrieveResponse:
        """
        Receita por segmento de empresas da B3, BDRs, FIIs e Fiagros, por exercício
        social, a partir das demonstrações anuais. Cada segmento tem uma atividade
        padrão, para comparar empresas.

        `segments` traz os segmentos como a empresa publica, com o crescimento sobre o
        ano anterior e o link do documento. `activities` soma os segmentos por
        atividade, com a parte de cada uma na soma dos segmentos.

        Para ETFs e outros fundos, `lookThrough` mostra a exposição às atividades pela
        carteira mais recente: o peso de cada ação, BDR ou FII na carteira vezes a parte
        de cada atividade na receita da empresa.

        Concessões de energia, saneamento, gás e rodovias registram o investimento na
        rede como receita de construção. Use `growthExConstruction` para comparar o
        crescimento sem ela.

        Planos Startup e Pro. FIIs, Fiagros e fundos só no plano Pro. PETR4, MGLU3,
        VALE3 e ITUB4 permitem testes gratuitos, sem token.

        Args:
          cnpjs: CNPJs de fundos separados por vírgula, com ou sem pontuação. Use para fundos sem
              ticker.

          end_year: Último exercício social. Padrão: o mais recente disponível.

          start_year: Primeiro exercício social. Padrão: o mais antigo disponível.

          symbols: Tickers separados por vírgula: ações, BDRs, FIIs, Fiagros ou ETFs. Máximo de 20.
              PETR3 e PETR4 retornam a mesma empresa.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/revenue-sources",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cnpjs": cnpjs,
                        "end_year": end_year,
                        "start_year": start_year,
                        "symbols": symbols,
                    },
                    revenue_source_retrieve_params.RevenueSourceRetrieveParams,
                ),
            ),
            cast_to=RevenueSourceRetrieveResponse,
        )

    def activities(
        self,
        *,
        activity: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RevenueSourceActivitiesResponse:
        """Lista das atividades usadas nas fontes de receita.

        Os códigos têm níveis
        separados por ponto: uma atividade inclui as atividades filhas.

        Não precisa de token.

        Args:
          activity: Código de uma atividade. Retorna só ela e as atividades filhas. Padrão: todas.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/revenue-sources/activities",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"activity": activity}, revenue_source_activities_params.RevenueSourceActivitiesParams
                ),
            ),
            cast_to=RevenueSourceActivitiesResponse,
        )

    def compare(
        self,
        *,
        activity: str,
        end_year: int | Omit = omit,
        start_year: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RevenueSourceCompareResponse:
        """
        Todos os emissores com receita em uma atividade e nas atividades filhas, com o
        crescimento por exercício. A receita de vários segmentos do mesmo emissor é
        somada.

        Para concessões, o crescimento não usa a receita de construção (`basis` =
        `exConstruction`) quando ela é conhecida em todos os segmentos. Nos demais
        casos, `flags` traz `includes-construction`.

        Os valores ficam na moeda de cada emissor. Compare o crescimento, não os
        valores. Receitas que já aparecem em uma controlada listada ficam de fora.

        Bancos e seguradoras não entram: suas receitas não se comparam. Pedir essas
        atividades retorna erro 400.

        Planos Startup e Pro. FIIs, Fiagros e fundos só no plano Pro. PETR4, MGLU3,
        VALE3 e ITUB4 permitem testes gratuitos, sem token.

        Args:
          activity: Código da atividade. Inclui as atividades filhas. Veja os códigos em
              `/api/v2/revenue-sources/activities`.

          end_year: Último exercício social. Padrão: o mais recente disponível.

          start_year: Primeiro exercício social. Padrão: o mais antigo disponível.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/revenue-sources/compare",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "activity": activity,
                        "end_year": end_year,
                        "start_year": start_year,
                    },
                    revenue_source_compare_params.RevenueSourceCompareParams,
                ),
            ),
            cast_to=RevenueSourceCompareResponse,
        )


class AsyncRevenueSourcesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRevenueSourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRevenueSourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRevenueSourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncRevenueSourcesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        cnpjs: str | Omit = omit,
        end_year: int | Omit = omit,
        start_year: int | Omit = omit,
        symbols: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RevenueSourceRetrieveResponse:
        """
        Receita por segmento de empresas da B3, BDRs, FIIs e Fiagros, por exercício
        social, a partir das demonstrações anuais. Cada segmento tem uma atividade
        padrão, para comparar empresas.

        `segments` traz os segmentos como a empresa publica, com o crescimento sobre o
        ano anterior e o link do documento. `activities` soma os segmentos por
        atividade, com a parte de cada uma na soma dos segmentos.

        Para ETFs e outros fundos, `lookThrough` mostra a exposição às atividades pela
        carteira mais recente: o peso de cada ação, BDR ou FII na carteira vezes a parte
        de cada atividade na receita da empresa.

        Concessões de energia, saneamento, gás e rodovias registram o investimento na
        rede como receita de construção. Use `growthExConstruction` para comparar o
        crescimento sem ela.

        Planos Startup e Pro. FIIs, Fiagros e fundos só no plano Pro. PETR4, MGLU3,
        VALE3 e ITUB4 permitem testes gratuitos, sem token.

        Args:
          cnpjs: CNPJs de fundos separados por vírgula, com ou sem pontuação. Use para fundos sem
              ticker.

          end_year: Último exercício social. Padrão: o mais recente disponível.

          start_year: Primeiro exercício social. Padrão: o mais antigo disponível.

          symbols: Tickers separados por vírgula: ações, BDRs, FIIs, Fiagros ou ETFs. Máximo de 20.
              PETR3 e PETR4 retornam a mesma empresa.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/revenue-sources",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cnpjs": cnpjs,
                        "end_year": end_year,
                        "start_year": start_year,
                        "symbols": symbols,
                    },
                    revenue_source_retrieve_params.RevenueSourceRetrieveParams,
                ),
            ),
            cast_to=RevenueSourceRetrieveResponse,
        )

    async def activities(
        self,
        *,
        activity: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RevenueSourceActivitiesResponse:
        """Lista das atividades usadas nas fontes de receita.

        Os códigos têm níveis
        separados por ponto: uma atividade inclui as atividades filhas.

        Não precisa de token.

        Args:
          activity: Código de uma atividade. Retorna só ela e as atividades filhas. Padrão: todas.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/revenue-sources/activities",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"activity": activity}, revenue_source_activities_params.RevenueSourceActivitiesParams
                ),
            ),
            cast_to=RevenueSourceActivitiesResponse,
        )

    async def compare(
        self,
        *,
        activity: str,
        end_year: int | Omit = omit,
        start_year: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RevenueSourceCompareResponse:
        """
        Todos os emissores com receita em uma atividade e nas atividades filhas, com o
        crescimento por exercício. A receita de vários segmentos do mesmo emissor é
        somada.

        Para concessões, o crescimento não usa a receita de construção (`basis` =
        `exConstruction`) quando ela é conhecida em todos os segmentos. Nos demais
        casos, `flags` traz `includes-construction`.

        Os valores ficam na moeda de cada emissor. Compare o crescimento, não os
        valores. Receitas que já aparecem em uma controlada listada ficam de fora.

        Bancos e seguradoras não entram: suas receitas não se comparam. Pedir essas
        atividades retorna erro 400.

        Planos Startup e Pro. FIIs, Fiagros e fundos só no plano Pro. PETR4, MGLU3,
        VALE3 e ITUB4 permitem testes gratuitos, sem token.

        Args:
          activity: Código da atividade. Inclui as atividades filhas. Veja os códigos em
              `/api/v2/revenue-sources/activities`.

          end_year: Último exercício social. Padrão: o mais recente disponível.

          start_year: Primeiro exercício social. Padrão: o mais antigo disponível.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/revenue-sources/compare",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "activity": activity,
                        "end_year": end_year,
                        "start_year": start_year,
                    },
                    revenue_source_compare_params.RevenueSourceCompareParams,
                ),
            ),
            cast_to=RevenueSourceCompareResponse,
        )


class RevenueSourcesResourceWithRawResponse:
    def __init__(self, revenue_sources: RevenueSourcesResource) -> None:
        self._revenue_sources = revenue_sources

        self.retrieve = to_raw_response_wrapper(
            revenue_sources.retrieve,
        )
        self.activities = to_raw_response_wrapper(
            revenue_sources.activities,
        )
        self.compare = to_raw_response_wrapper(
            revenue_sources.compare,
        )


class AsyncRevenueSourcesResourceWithRawResponse:
    def __init__(self, revenue_sources: AsyncRevenueSourcesResource) -> None:
        self._revenue_sources = revenue_sources

        self.retrieve = async_to_raw_response_wrapper(
            revenue_sources.retrieve,
        )
        self.activities = async_to_raw_response_wrapper(
            revenue_sources.activities,
        )
        self.compare = async_to_raw_response_wrapper(
            revenue_sources.compare,
        )


class RevenueSourcesResourceWithStreamingResponse:
    def __init__(self, revenue_sources: RevenueSourcesResource) -> None:
        self._revenue_sources = revenue_sources

        self.retrieve = to_streamed_response_wrapper(
            revenue_sources.retrieve,
        )
        self.activities = to_streamed_response_wrapper(
            revenue_sources.activities,
        )
        self.compare = to_streamed_response_wrapper(
            revenue_sources.compare,
        )


class AsyncRevenueSourcesResourceWithStreamingResponse:
    def __init__(self, revenue_sources: AsyncRevenueSourcesResource) -> None:
        self._revenue_sources = revenue_sources

        self.retrieve = async_to_streamed_response_wrapper(
            revenue_sources.retrieve,
        )
        self.activities = async_to_streamed_response_wrapper(
            revenue_sources.activities,
        )
        self.compare = async_to_streamed_response_wrapper(
            revenue_sources.compare,
        )
