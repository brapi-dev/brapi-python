# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v2 import inflation_retrieve_params
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
    """
    Acompanhe os principais indicadores econômicos do Brasil, incluindo inflação (IPCA, IGP-M) e Taxa Selic.
    """

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
        Retorna dados históricos do **IPCA (Índice Nacional de Preços ao Consumidor
        Amplo)**, o índice oficial de inflação do Brasil, medido pelo IBGE.

        ### Funcionalidades

        - **Dados Mensais:** Variação percentual mensal do IPCA
        - **Histórico Completo:** Dados desde janeiro/2000 até o mês atual
        - **Filtros de Período:** Use `start` e `end` para definir período específico
          (formato DD/MM/YYYY)
        - **Ordenação:** Ordene por data ou valor, crescente ou decrescente

        ### Autenticação

        Bearer token ou query param `token`. Requer plano Startup.

        ### Exemplos de Uso

        ```bash
        # Padrão (últimos 12 meses)
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/inflation"

        # Histórico completo
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/inflation?historical=true"

        # Período específico
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/inflation?start=01/01/2023&end=31/12/2023"

        # Ordenado por valor (decrescente)
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/inflation?historical=true&sortBy=value&sortOrder=desc"
        ```

        ### Parâmetros de Ordenação

        - `sortBy`: `date` (padrão) ou `value`
        - `sortOrder`: `desc` (padrão) ou `asc`

        ### Campos da Resposta

        - `date` — Data no formato DD/MM/YYYY
        - `value` — Variação percentual do IPCA no mês
        - `epochDate` — Data em timestamp Unix (milissegundos)

        ### Sobre o IPCA

        O IPCA é o índice oficial de inflação do Brasil, calculado mensalmente pelo
        IBGE. Ele mede a variação de preços de uma cesta de produtos e serviços
        consumidos pelas famílias brasileiras.

        ### Fonte dos Dados

        Banco Central do Brasil (BCB) — Série temporal 13522 do Sistema Gerador de
        Séries Temporais (SGS)

        **Plano Mínimo:** Startup | **Autenticação:** Necessária

        Args:
          end: Data de fim (DD/MM/YYYY)

          historical: Incluir dados históricos (true/false)

          sort_by: Campo para ordenação (date ou value)

          sort_order: Ordem de classificação (asc ou desc)

          start: Data de início (DD/MM/YYYY)

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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InflationListAvailableResponse:
        """
        Retorna a lista de países disponíveis para consulta de dados de inflação.

        ### Países Disponíveis

        - **brazil** — Dados do IPCA (IBGE)

        Use o valor retornado como referência para futuras expansões do endpoint.

        ### Exemplo de Uso

        ```bash
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/inflation/available"
        ```

        **Plano Mínimo:** Startup | **Autenticação:** Necessária
        """
        return self._get(
            "/api/v2/inflation/available",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InflationListAvailableResponse,
        )


class AsyncInflationResource(AsyncAPIResource):
    """
    Acompanhe os principais indicadores econômicos do Brasil, incluindo inflação (IPCA, IGP-M) e Taxa Selic.
    """

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
        Retorna dados históricos do **IPCA (Índice Nacional de Preços ao Consumidor
        Amplo)**, o índice oficial de inflação do Brasil, medido pelo IBGE.

        ### Funcionalidades

        - **Dados Mensais:** Variação percentual mensal do IPCA
        - **Histórico Completo:** Dados desde janeiro/2000 até o mês atual
        - **Filtros de Período:** Use `start` e `end` para definir período específico
          (formato DD/MM/YYYY)
        - **Ordenação:** Ordene por data ou valor, crescente ou decrescente

        ### Autenticação

        Bearer token ou query param `token`. Requer plano Startup.

        ### Exemplos de Uso

        ```bash
        # Padrão (últimos 12 meses)
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/inflation"

        # Histórico completo
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/inflation?historical=true"

        # Período específico
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/inflation?start=01/01/2023&end=31/12/2023"

        # Ordenado por valor (decrescente)
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/inflation?historical=true&sortBy=value&sortOrder=desc"
        ```

        ### Parâmetros de Ordenação

        - `sortBy`: `date` (padrão) ou `value`
        - `sortOrder`: `desc` (padrão) ou `asc`

        ### Campos da Resposta

        - `date` — Data no formato DD/MM/YYYY
        - `value` — Variação percentual do IPCA no mês
        - `epochDate` — Data em timestamp Unix (milissegundos)

        ### Sobre o IPCA

        O IPCA é o índice oficial de inflação do Brasil, calculado mensalmente pelo
        IBGE. Ele mede a variação de preços de uma cesta de produtos e serviços
        consumidos pelas famílias brasileiras.

        ### Fonte dos Dados

        Banco Central do Brasil (BCB) — Série temporal 13522 do Sistema Gerador de
        Séries Temporais (SGS)

        **Plano Mínimo:** Startup | **Autenticação:** Necessária

        Args:
          end: Data de fim (DD/MM/YYYY)

          historical: Incluir dados históricos (true/false)

          sort_by: Campo para ordenação (date ou value)

          sort_order: Ordem de classificação (asc ou desc)

          start: Data de início (DD/MM/YYYY)

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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InflationListAvailableResponse:
        """
        Retorna a lista de países disponíveis para consulta de dados de inflação.

        ### Países Disponíveis

        - **brazil** — Dados do IPCA (IBGE)

        Use o valor retornado como referência para futuras expansões do endpoint.

        ### Exemplo de Uso

        ```bash
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/inflation/available"
        ```

        **Plano Mínimo:** Startup | **Autenticação:** Necessária
        """
        return await self._get(
            "/api/v2/inflation/available",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
