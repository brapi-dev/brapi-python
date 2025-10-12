# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
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
        token: str | Omit = omit,
        country: str | Omit = omit,
        end: Union[str, date] | Omit = omit,
        historical: bool | Omit = omit,
        sort_by: Literal["date", "value"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InflationRetrieveResponse:
        """
        Obtenha dados históricos sobre índices de inflação para um país específico.

        ### Funcionalidades:

        - **Seleção de País:** Especifique o país desejado com o parâmetro `country`
          (padrão: `brazil`).
        - **Filtragem por Período:** Defina um intervalo de datas com `start` e `end`
          (formato DD/MM/YYYY).
        - **Inclusão de Histórico:** O parâmetro `historical` (booleano) parece
          controlar a inclusão de dados históricos (verificar comportamento exato, pode
          ser redundante com `start`/`end`).
        - **Ordenação:** Ordene os resultados por data (`date`) ou valor (`value`)
          usando `sortBy` e `sortOrder`.

        ### Autenticação:

        Requer token de autenticação via `token` (query) ou `Authorization` (header).

        ### Exemplo de Requisição:

        **Buscar dados de inflação do Brasil para o ano de 2022, ordenados por valor
        ascendente:**

        ```bash
        curl -X GET "https://brapi.dev/api/v2/inflation?country=brazil&start=01/01/2022&end=31/12/2022&sortBy=value&sortOrder=asc&token=SEU_TOKEN"
        ```

        **Buscar os dados mais recentes de inflação (sem período definido, ordenação
        padrão):**

        ```bash
        curl -X GET "https://brapi.dev/api/v2/inflation?country=brazil&token=SEU_TOKEN"
        ```

        ### Resposta:

        A resposta contém um array `inflation`, onde cada objeto representa um ponto de
        dado de inflação com sua `date` (DD/MM/YYYY), `value` (o índice de inflação como
        string) e `epochDate` (timestamp UNIX).

        Args:
          token: **Obrigatório caso não esteja adicionado como header "Authorization".** Seu
              token de autenticação pessoal da API Brapi.

              **Formas de Envio:**

              1.  **Query Parameter:** Adicione `?token=SEU_TOKEN` ao final da URL.
              2.  **HTTP Header:** Inclua o header `Authorization: Bearer SEU_TOKEN` na sua
                  requisição.

              Ambos os métodos são aceitos, mas pelo menos um deles deve ser utilizado.
              Obtenha seu token em [brapi.dev/dashboard](https://brapi.dev/dashboard).

          country: **Opcional.** Nome do país para o qual buscar os dados de inflação. Use nomes em
              minúsculas. O padrão é `brazil`. Consulte `/api/v2/inflation/available` para a
              lista de países suportados.

          end: **Opcional.** Data final do período desejado para os dados históricos, no
              formato `DD/MM/YYYY`. Requerido se `start` for especificado.

          historical: **Opcional.** Booleano (`true` ou `false`). Define se dados históricos devem ser
              incluídos. O comportamento exato em conjunto com `start`/`end` deve ser
              verificado. Padrão: `false`.

          sort_by: **Opcional.** Campo pelo qual os resultados da inflação serão ordenados.

          sort_order: **Opcional.** Direção da ordenação: `asc` (ascendente) ou `desc` (descendente).
              Padrão: `desc`. Requer que `sortBy` seja especificado.

          start: **Opcional.** Data de início do período desejado para os dados históricos, no
              formato `DD/MM/YYYY`. Requerido se `end` for especificado.

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
                        "token": token,
                        "country": country,
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
        token: str | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InflationListAvailableResponse:
        """
        Obtenha a lista completa de todos os países para os quais a API Brapi possui
        dados de inflação disponíveis para consulta no endpoint `/api/v2/inflation`.

        ### Funcionalidade:

        - Retorna um array `countries` com os nomes dos países (em minúsculas).
        - Pode ser filtrado usando o parâmetro `search`.

        ### Autenticação:

        Requer token de autenticação via `token` (query) ou `Authorization` (header).

        ### Exemplo de Requisição:

        **Listar todos os países com dados de inflação:**

        ```bash
        curl -X GET "https://brapi.dev/api/v2/inflation/available?token=SEU_TOKEN"
        ```

        **Buscar países cujo nome contenha 'arg':**

        ```bash
        curl -X GET "https://brapi.dev/api/v2/inflation/available?search=arg&token=SEU_TOKEN"
        ```

        ### Resposta:

        A resposta é um objeto JSON com a chave `countries`, contendo um array de
        strings com os nomes dos países (ex: `["brazil", "argentina", "usa"]`).

        Args:
          token: **Obrigatório caso não esteja adicionado como header "Authorization".** Seu
              token de autenticação pessoal da API Brapi.

              **Formas de Envio:**

              1.  **Query Parameter:** Adicione `?token=SEU_TOKEN` ao final da URL.
              2.  **HTTP Header:** Inclua o header `Authorization: Bearer SEU_TOKEN` na sua
                  requisição.

              Ambos os métodos são aceitos, mas pelo menos um deles deve ser utilizado.
              Obtenha seu token em [brapi.dev/dashboard](https://brapi.dev/dashboard).

          search: **Opcional.** Termo para filtrar a lista pelo nome do país (correspondência
              parcial, case-insensitive). Se omitido, retorna todos os países.

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
                query=maybe_transform(
                    {
                        "token": token,
                        "search": search,
                    },
                    inflation_list_available_params.InflationListAvailableParams,
                ),
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
        token: str | Omit = omit,
        country: str | Omit = omit,
        end: Union[str, date] | Omit = omit,
        historical: bool | Omit = omit,
        sort_by: Literal["date", "value"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InflationRetrieveResponse:
        """
        Obtenha dados históricos sobre índices de inflação para um país específico.

        ### Funcionalidades:

        - **Seleção de País:** Especifique o país desejado com o parâmetro `country`
          (padrão: `brazil`).
        - **Filtragem por Período:** Defina um intervalo de datas com `start` e `end`
          (formato DD/MM/YYYY).
        - **Inclusão de Histórico:** O parâmetro `historical` (booleano) parece
          controlar a inclusão de dados históricos (verificar comportamento exato, pode
          ser redundante com `start`/`end`).
        - **Ordenação:** Ordene os resultados por data (`date`) ou valor (`value`)
          usando `sortBy` e `sortOrder`.

        ### Autenticação:

        Requer token de autenticação via `token` (query) ou `Authorization` (header).

        ### Exemplo de Requisição:

        **Buscar dados de inflação do Brasil para o ano de 2022, ordenados por valor
        ascendente:**

        ```bash
        curl -X GET "https://brapi.dev/api/v2/inflation?country=brazil&start=01/01/2022&end=31/12/2022&sortBy=value&sortOrder=asc&token=SEU_TOKEN"
        ```

        **Buscar os dados mais recentes de inflação (sem período definido, ordenação
        padrão):**

        ```bash
        curl -X GET "https://brapi.dev/api/v2/inflation?country=brazil&token=SEU_TOKEN"
        ```

        ### Resposta:

        A resposta contém um array `inflation`, onde cada objeto representa um ponto de
        dado de inflação com sua `date` (DD/MM/YYYY), `value` (o índice de inflação como
        string) e `epochDate` (timestamp UNIX).

        Args:
          token: **Obrigatório caso não esteja adicionado como header "Authorization".** Seu
              token de autenticação pessoal da API Brapi.

              **Formas de Envio:**

              1.  **Query Parameter:** Adicione `?token=SEU_TOKEN` ao final da URL.
              2.  **HTTP Header:** Inclua o header `Authorization: Bearer SEU_TOKEN` na sua
                  requisição.

              Ambos os métodos são aceitos, mas pelo menos um deles deve ser utilizado.
              Obtenha seu token em [brapi.dev/dashboard](https://brapi.dev/dashboard).

          country: **Opcional.** Nome do país para o qual buscar os dados de inflação. Use nomes em
              minúsculas. O padrão é `brazil`. Consulte `/api/v2/inflation/available` para a
              lista de países suportados.

          end: **Opcional.** Data final do período desejado para os dados históricos, no
              formato `DD/MM/YYYY`. Requerido se `start` for especificado.

          historical: **Opcional.** Booleano (`true` ou `false`). Define se dados históricos devem ser
              incluídos. O comportamento exato em conjunto com `start`/`end` deve ser
              verificado. Padrão: `false`.

          sort_by: **Opcional.** Campo pelo qual os resultados da inflação serão ordenados.

          sort_order: **Opcional.** Direção da ordenação: `asc` (ascendente) ou `desc` (descendente).
              Padrão: `desc`. Requer que `sortBy` seja especificado.

          start: **Opcional.** Data de início do período desejado para os dados históricos, no
              formato `DD/MM/YYYY`. Requerido se `end` for especificado.

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
                        "token": token,
                        "country": country,
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
        token: str | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InflationListAvailableResponse:
        """
        Obtenha a lista completa de todos os países para os quais a API Brapi possui
        dados de inflação disponíveis para consulta no endpoint `/api/v2/inflation`.

        ### Funcionalidade:

        - Retorna um array `countries` com os nomes dos países (em minúsculas).
        - Pode ser filtrado usando o parâmetro `search`.

        ### Autenticação:

        Requer token de autenticação via `token` (query) ou `Authorization` (header).

        ### Exemplo de Requisição:

        **Listar todos os países com dados de inflação:**

        ```bash
        curl -X GET "https://brapi.dev/api/v2/inflation/available?token=SEU_TOKEN"
        ```

        **Buscar países cujo nome contenha 'arg':**

        ```bash
        curl -X GET "https://brapi.dev/api/v2/inflation/available?search=arg&token=SEU_TOKEN"
        ```

        ### Resposta:

        A resposta é um objeto JSON com a chave `countries`, contendo um array de
        strings com os nomes dos países (ex: `["brazil", "argentina", "usa"]`).

        Args:
          token: **Obrigatório caso não esteja adicionado como header "Authorization".** Seu
              token de autenticação pessoal da API Brapi.

              **Formas de Envio:**

              1.  **Query Parameter:** Adicione `?token=SEU_TOKEN` ao final da URL.
              2.  **HTTP Header:** Inclua o header `Authorization: Bearer SEU_TOKEN` na sua
                  requisição.

              Ambos os métodos são aceitos, mas pelo menos um deles deve ser utilizado.
              Obtenha seu token em [brapi.dev/dashboard](https://brapi.dev/dashboard).

          search: **Opcional.** Termo para filtrar a lista pelo nome do país (correspondência
              parcial, case-insensitive). Se omitido, retorna todos os países.

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
                    {
                        "token": token,
                        "search": search,
                    },
                    inflation_list_available_params.InflationListAvailableParams,
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
