# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v2 import prime_rate_retrieve_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v2.prime_rate_retrieve_response import PrimeRateRetrieveResponse
from ...types.v2.prime_rate_list_available_response import PrimeRateListAvailableResponse

__all__ = ["PrimeRateResource", "AsyncPrimeRateResource"]


class PrimeRateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PrimeRateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return PrimeRateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrimeRateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return PrimeRateResourceWithStreamingResponse(self)

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
    ) -> PrimeRateRetrieveResponse:
        """
        Retorna dados históricos da **Taxa SELIC (Sistema Especial de Liquidação e de
        Custódia)**, a taxa básica de juros da economia brasileira, definida pelo COPOM
        (Comitê de Política Monetária) do Banco Central.

        ### Funcionalidades

        - **Dados Diários:** Taxa SELIC diária (meta anualizada, % a.a.)
        - **Histórico Completo:** Dados desde janeiro/2000 até a data atual
        - **Filtros de Período:** Use `start` e `end` (formato DD/MM/YYYY)
        - **Ordenação:** Por data ou valor, crescente ou decrescente

        ### Autenticação

        Bearer token ou query param `token`. Requer plano Startup.

        ### Exemplos de Uso

        ```bash
        # Padrão (últimos 12 meses)
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/prime-rate"

        # Histórico completo
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/prime-rate?historical=true"

        # Período específico
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/prime-rate?start=01/01/2023&end=31/12/2023"

        # Ordenado por valor (decrescente)
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/prime-rate?historical=true&sortBy=value&sortOrder=desc"
        ```

        ### Parâmetros de Ordenação

        - `sortBy`: `date` (padrão) ou `value`
        - `sortOrder`: `desc` (padrão) ou `asc`

        ### Campos da Resposta

        - `date` — Data no formato DD/MM/YYYY
        - `value` — Taxa SELIC meta anualizada (% a.a.)
        - `epochDate` — Data em timestamp Unix (milissegundos)

        ### Sobre a SELIC

        A SELIC é a taxa básica de juros da economia brasileira e influencia todas as
        demais taxas de juros do país (empréstimos, financiamentos, aplicações
        financeiras). Ela é definida pelo COPOM a cada 45 dias e serve como referência
        para o CDI.

        ### Fonte dos Dados

        Banco Central do Brasil (BCB) — meta SELIC publicada como série temporal oficial

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
            "/api/v2/prime-rate",
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
                    prime_rate_retrieve_params.PrimeRateRetrieveParams,
                ),
            ),
            cast_to=PrimeRateRetrieveResponse,
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
    ) -> PrimeRateListAvailableResponse:
        """
        Retorna a lista de países disponíveis para consulta de dados de taxa de juros.

        ### Países Disponíveis

        - **brazil** — Taxa SELIC (Banco Central)

        Use o valor retornado como referência para futuras expansões do endpoint.

        ### Exemplo de Uso

        ```bash
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/prime-rate/available"
        ```

        **Plano Mínimo:** Startup | **Autenticação:** Necessária
        """
        return self._get(
            "/api/v2/prime-rate/available",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrimeRateListAvailableResponse,
        )


class AsyncPrimeRateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPrimeRateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPrimeRateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrimeRateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncPrimeRateResourceWithStreamingResponse(self)

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
    ) -> PrimeRateRetrieveResponse:
        """
        Retorna dados históricos da **Taxa SELIC (Sistema Especial de Liquidação e de
        Custódia)**, a taxa básica de juros da economia brasileira, definida pelo COPOM
        (Comitê de Política Monetária) do Banco Central.

        ### Funcionalidades

        - **Dados Diários:** Taxa SELIC diária (meta anualizada, % a.a.)
        - **Histórico Completo:** Dados desde janeiro/2000 até a data atual
        - **Filtros de Período:** Use `start` e `end` (formato DD/MM/YYYY)
        - **Ordenação:** Por data ou valor, crescente ou decrescente

        ### Autenticação

        Bearer token ou query param `token`. Requer plano Startup.

        ### Exemplos de Uso

        ```bash
        # Padrão (últimos 12 meses)
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/prime-rate"

        # Histórico completo
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/prime-rate?historical=true"

        # Período específico
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/prime-rate?start=01/01/2023&end=31/12/2023"

        # Ordenado por valor (decrescente)
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/prime-rate?historical=true&sortBy=value&sortOrder=desc"
        ```

        ### Parâmetros de Ordenação

        - `sortBy`: `date` (padrão) ou `value`
        - `sortOrder`: `desc` (padrão) ou `asc`

        ### Campos da Resposta

        - `date` — Data no formato DD/MM/YYYY
        - `value` — Taxa SELIC meta anualizada (% a.a.)
        - `epochDate` — Data em timestamp Unix (milissegundos)

        ### Sobre a SELIC

        A SELIC é a taxa básica de juros da economia brasileira e influencia todas as
        demais taxas de juros do país (empréstimos, financiamentos, aplicações
        financeiras). Ela é definida pelo COPOM a cada 45 dias e serve como referência
        para o CDI.

        ### Fonte dos Dados

        Banco Central do Brasil (BCB) — meta SELIC publicada como série temporal oficial

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
            "/api/v2/prime-rate",
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
                    prime_rate_retrieve_params.PrimeRateRetrieveParams,
                ),
            ),
            cast_to=PrimeRateRetrieveResponse,
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
    ) -> PrimeRateListAvailableResponse:
        """
        Retorna a lista de países disponíveis para consulta de dados de taxa de juros.

        ### Países Disponíveis

        - **brazil** — Taxa SELIC (Banco Central)

        Use o valor retornado como referência para futuras expansões do endpoint.

        ### Exemplo de Uso

        ```bash
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/prime-rate/available"
        ```

        **Plano Mínimo:** Startup | **Autenticação:** Necessária
        """
        return await self._get(
            "/api/v2/prime-rate/available",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrimeRateListAvailableResponse,
        )


class PrimeRateResourceWithRawResponse:
    def __init__(self, prime_rate: PrimeRateResource) -> None:
        self._prime_rate = prime_rate

        self.retrieve = to_raw_response_wrapper(
            prime_rate.retrieve,
        )
        self.list_available = to_raw_response_wrapper(
            prime_rate.list_available,
        )


class AsyncPrimeRateResourceWithRawResponse:
    def __init__(self, prime_rate: AsyncPrimeRateResource) -> None:
        self._prime_rate = prime_rate

        self.retrieve = async_to_raw_response_wrapper(
            prime_rate.retrieve,
        )
        self.list_available = async_to_raw_response_wrapper(
            prime_rate.list_available,
        )


class PrimeRateResourceWithStreamingResponse:
    def __init__(self, prime_rate: PrimeRateResource) -> None:
        self._prime_rate = prime_rate

        self.retrieve = to_streamed_response_wrapper(
            prime_rate.retrieve,
        )
        self.list_available = to_streamed_response_wrapper(
            prime_rate.list_available,
        )


class AsyncPrimeRateResourceWithStreamingResponse:
    def __init__(self, prime_rate: AsyncPrimeRateResource) -> None:
        self._prime_rate = prime_rate

        self.retrieve = async_to_streamed_response_wrapper(
            prime_rate.retrieve,
        )
        self.list_available = async_to_streamed_response_wrapper(
            prime_rate.list_available,
        )
