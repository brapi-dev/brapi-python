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
from ....types.v2.fii import property_history_params, property_retrieve_params
from ....types.v2.fii.property_history_response import PropertyHistoryResponse
from ....types.v2.fii.property_retrieve_response import PropertyRetrieveResponse

__all__ = ["PropertiesResource", "AsyncPropertiesResource"]


class PropertiesResource(SyncAPIResource):
    """
    Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
    """

    @cached_property
    def with_raw_response(self) -> PropertiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return PropertiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PropertiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return PropertiesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        symbols: str,
        all_versions: Literal["true", "false"] | Omit = omit,
        reference_date: str | Omit = omit,
        sort_by: Literal["revenueShare", "area", "vacancyRate", "name"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PropertyRetrieveResponse:
        """
        Imóveis físicos de FIIs pelo informe trimestral da CVM, com área, endereço,
        classe, unidades, vacância, inadimplência e participação na receita de cada
        imóvel.

        Use para analisar FIIs de tijolo, medir a vacância de um fundo e ver quanto da
        receita depende de cada imóvel.

        `summary.vacancyRate` é a vacância do fundo, ponderada pela área quando o
        informe traz a área de cada imóvel. `vacancyRate`, `delinquencyRate` e
        `revenueShare` são frações decimais: `0.0328` é 3,28%.

        Leia `vacancyRate` junto com `revenueShare`. Um imóvel vago com 2% da receita
        pesa menos que um com 30%.

        Sem `referenceDate`, retorna o trimestre mais recente de cada fundo. O padrão
        retorna a versão mais recente do informe, e `allVersions=true` retorna todas.
        Para a série no tempo, use o
        [histórico de imóveis](https://brapi.dev/docs/fiis/imoveis-historico).

        Plano Pro. Sem token, aceita só `symbols` com MXRF11 e HGLG11.

        Args:
          symbols: Tickers de FIIs separados por vírgula, até 20. Ex.: HGLG11,MXRF11.

          all_versions: true inclui todas as versões do trimestre. false retorna só a mais recente.

          reference_date: Fim do trimestre no formato YYYY-MM-DD. Sem valor, retorna o trimestre mais
              recente de cada FII.

          sort_by: Campo de ordenação dos imóveis.

          sort_order: Direção da ordenação dos imóveis.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/fii/properties",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "symbols": symbols,
                        "all_versions": all_versions,
                        "reference_date": reference_date,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                    },
                    property_retrieve_params.PropertyRetrieveParams,
                ),
            ),
            cast_to=PropertyRetrieveResponse,
        )

    def history(
        self,
        *,
        symbols: str,
        all_versions: Literal["true", "false"] | Omit = omit,
        end_date: str | Omit = omit,
        sort_by: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PropertyHistoryResponse:
        """
        Série trimestral de imóveis e vacância de FIIs: um ponto por fundo, trimestre e
        versão do informe, com vacância, área total e quantidade de imóveis em
        `summary`.

        Use para gráficos de vacância e para acompanhar o tamanho da carteira física no
        tempo.

        A resposta não traz a lista de imóveis. Para os imóveis de um trimestre, use
        [imóveis de FIIs](https://brapi.dev/docs/fiis/imoveis) com `referenceDate`.

        Sem `startDate` e `endDate`, retorna os últimos 12 meses. `sortBy` aceita
        `referenceDate` (padrão), `symbol`, `version`, `count`, `totalArea`,
        `vacancyRate`, `averageVacancyRate` e `propertiesWithVacancy`.
        `allVersions=true` inclui as versões retificadas.

        Plano Pro. Sem token, aceita só `symbols` com MXRF11 e HGLG11.

        Args:
          symbols: Tickers de FIIs separados por vírgula, até 20. Ex.: HGLG11,MXRF11.

          all_versions: true inclui todas as versões de cada trimestre. false retorna só a mais recente.

          end_date: Data final no formato YYYY-MM-DD.

          sort_by: Campo de ordenação.

          sort_order: Direção da ordenação.

          start_date: Data inicial no formato YYYY-MM-DD.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/fii/properties/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "symbols": symbols,
                        "all_versions": all_versions,
                        "end_date": end_date,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "start_date": start_date,
                    },
                    property_history_params.PropertyHistoryParams,
                ),
            ),
            cast_to=PropertyHistoryResponse,
        )


class AsyncPropertiesResource(AsyncAPIResource):
    """
    Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
    """

    @cached_property
    def with_raw_response(self) -> AsyncPropertiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPropertiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPropertiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncPropertiesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        symbols: str,
        all_versions: Literal["true", "false"] | Omit = omit,
        reference_date: str | Omit = omit,
        sort_by: Literal["revenueShare", "area", "vacancyRate", "name"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PropertyRetrieveResponse:
        """
        Imóveis físicos de FIIs pelo informe trimestral da CVM, com área, endereço,
        classe, unidades, vacância, inadimplência e participação na receita de cada
        imóvel.

        Use para analisar FIIs de tijolo, medir a vacância de um fundo e ver quanto da
        receita depende de cada imóvel.

        `summary.vacancyRate` é a vacância do fundo, ponderada pela área quando o
        informe traz a área de cada imóvel. `vacancyRate`, `delinquencyRate` e
        `revenueShare` são frações decimais: `0.0328` é 3,28%.

        Leia `vacancyRate` junto com `revenueShare`. Um imóvel vago com 2% da receita
        pesa menos que um com 30%.

        Sem `referenceDate`, retorna o trimestre mais recente de cada fundo. O padrão
        retorna a versão mais recente do informe, e `allVersions=true` retorna todas.
        Para a série no tempo, use o
        [histórico de imóveis](https://brapi.dev/docs/fiis/imoveis-historico).

        Plano Pro. Sem token, aceita só `symbols` com MXRF11 e HGLG11.

        Args:
          symbols: Tickers de FIIs separados por vírgula, até 20. Ex.: HGLG11,MXRF11.

          all_versions: true inclui todas as versões do trimestre. false retorna só a mais recente.

          reference_date: Fim do trimestre no formato YYYY-MM-DD. Sem valor, retorna o trimestre mais
              recente de cada FII.

          sort_by: Campo de ordenação dos imóveis.

          sort_order: Direção da ordenação dos imóveis.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/fii/properties",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "symbols": symbols,
                        "all_versions": all_versions,
                        "reference_date": reference_date,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                    },
                    property_retrieve_params.PropertyRetrieveParams,
                ),
            ),
            cast_to=PropertyRetrieveResponse,
        )

    async def history(
        self,
        *,
        symbols: str,
        all_versions: Literal["true", "false"] | Omit = omit,
        end_date: str | Omit = omit,
        sort_by: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PropertyHistoryResponse:
        """
        Série trimestral de imóveis e vacância de FIIs: um ponto por fundo, trimestre e
        versão do informe, com vacância, área total e quantidade de imóveis em
        `summary`.

        Use para gráficos de vacância e para acompanhar o tamanho da carteira física no
        tempo.

        A resposta não traz a lista de imóveis. Para os imóveis de um trimestre, use
        [imóveis de FIIs](https://brapi.dev/docs/fiis/imoveis) com `referenceDate`.

        Sem `startDate` e `endDate`, retorna os últimos 12 meses. `sortBy` aceita
        `referenceDate` (padrão), `symbol`, `version`, `count`, `totalArea`,
        `vacancyRate`, `averageVacancyRate` e `propertiesWithVacancy`.
        `allVersions=true` inclui as versões retificadas.

        Plano Pro. Sem token, aceita só `symbols` com MXRF11 e HGLG11.

        Args:
          symbols: Tickers de FIIs separados por vírgula, até 20. Ex.: HGLG11,MXRF11.

          all_versions: true inclui todas as versões de cada trimestre. false retorna só a mais recente.

          end_date: Data final no formato YYYY-MM-DD.

          sort_by: Campo de ordenação.

          sort_order: Direção da ordenação.

          start_date: Data inicial no formato YYYY-MM-DD.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/fii/properties/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "symbols": symbols,
                        "all_versions": all_versions,
                        "end_date": end_date,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "start_date": start_date,
                    },
                    property_history_params.PropertyHistoryParams,
                ),
            ),
            cast_to=PropertyHistoryResponse,
        )


class PropertiesResourceWithRawResponse:
    def __init__(self, properties: PropertiesResource) -> None:
        self._properties = properties

        self.retrieve = to_raw_response_wrapper(
            properties.retrieve,
        )
        self.history = to_raw_response_wrapper(
            properties.history,
        )


class AsyncPropertiesResourceWithRawResponse:
    def __init__(self, properties: AsyncPropertiesResource) -> None:
        self._properties = properties

        self.retrieve = async_to_raw_response_wrapper(
            properties.retrieve,
        )
        self.history = async_to_raw_response_wrapper(
            properties.history,
        )


class PropertiesResourceWithStreamingResponse:
    def __init__(self, properties: PropertiesResource) -> None:
        self._properties = properties

        self.retrieve = to_streamed_response_wrapper(
            properties.retrieve,
        )
        self.history = to_streamed_response_wrapper(
            properties.history,
        )


class AsyncPropertiesResourceWithStreamingResponse:
    def __init__(self, properties: AsyncPropertiesResource) -> None:
        self._properties = properties

        self.retrieve = async_to_streamed_response_wrapper(
            properties.retrieve,
        )
        self.history = async_to_streamed_response_wrapper(
            properties.history,
        )
