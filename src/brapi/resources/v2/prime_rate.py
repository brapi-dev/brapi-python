# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v2 import prime_rate_retrieve_params, prime_rate_list_available_params
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

        For more information, see https://www.github.com/stainless-sdks/brapi-python#accessing-raw-response-data-eg-headers
        """
        return PrimeRateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrimeRateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/brapi-python#with_streaming_response
        """
        return PrimeRateResourceWithStreamingResponse(self)

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
    ) -> PrimeRateRetrieveResponse:
        """
        Obtenha informações atualizadas sobre a taxa básica de juros (SELIC) de um país
        por um período determinado.

        ### Funcionalidades:

        - **Seleção por País:** Especifique o país desejado usando o parâmetro `country`
          (padrão: brazil).
        - **Período Customizado:** Defina datas de início e fim com `start` e `end` para
          consultar um intervalo específico.
        - **Ordenação:** Ordene os resultados por data ou valor com os parâmetros
          `sortBy` e `sortOrder`.
        - **Dados Históricos:** Solicite o histórico completo ou apenas o valor mais
          recente com o parâmetro `historical`.

        ### Autenticação:

        Requer token de autenticação via `token` (query) ou `Authorization` (header).

        ### Exemplo de Requisição:

        **Taxa de juros do Brasil entre dezembro/2021 e janeiro/2022:**

        ```bash
        curl -X GET "https://brapi.dev/api/v2/prime-rate?country=brazil&start=01/12/2021&end=01/01/2022&sortBy=date&sortOrder=desc&token=SEU_TOKEN"
        ```

        Args:
          token: **Obrigatório caso não esteja adicionado como header "Authorization".** Seu
              token de autenticação pessoal da API Brapi.

              **Formas de Envio:**

              1.  **Query Parameter:** Adicione `?token=SEU_TOKEN` ao final da URL.
              2.  **HTTP Header:** Inclua o header `Authorization: Bearer SEU_TOKEN` na sua
                  requisição.

              Ambos os métodos são aceitos, mas pelo menos um deles deve ser utilizado.
              Obtenha seu token em [brapi.dev/dashboard](https://brapi.dev/dashboard).

          country: **Opcional.** O país do qual você deseja obter informações sobre a taxa básica
              de juros. Por padrão, o país é definido como brazil. Você pode consultar a lista
              de países disponíveis através do endpoint `/api/v2/prime-rate/available`.

          end: **Opcional.** Data final do período para busca no formato DD/MM/YYYY. Por padrão
              é a data atual. Útil quando `historical=true` para restringir o período da série
              histórica.

          historical: **Opcional.** Define se os dados históricos serão retornados. Se definido como
              `true`, retorna a série histórica completa. Se `false` (padrão) ou omitido,
              retorna apenas o valor mais recente.

          sort_by: **Opcional.** Campo pelo qual os resultados serão ordenados. Por padrão, ordena
              por `date` (data).

          sort_order: **Opcional.** Define se a ordenação será crescente (`asc`) ou decrescente
              (`desc`). Por padrão, é `desc` (decrescente).

          start: **Opcional.** Data inicial do período para busca no formato DD/MM/YYYY. Útil
              quando `historical=true` para restringir o período da série histórica.

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
                        "token": token,
                        "country": country,
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
        token: str | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrimeRateListAvailableResponse:
        """
        Liste todos os países disponíveis com dados de taxa básica de juros (SELIC) na
        API brapi. Este endpoint facilita a descoberta de quais países possuem dados
        disponíveis para consulta através do endpoint principal `/api/v2/prime-rate`.

        ### Funcionalidades:

        - **Busca Filtrada:** Utilize o parâmetro `search` para filtrar países por nome
          ou parte do nome.
        - **Ideal para Autocomplete:** Perfeito para implementar campos de busca com
          autocompletar em interfaces de usuário.

        ### Autenticação:

        Requer token de autenticação via `token` (query) ou `Authorization` (header).

        ### Exemplo de Requisição:

        **Listar países que contenham "BR" no nome:**

        ```bash
        curl -X GET "https://brapi.dev/api/v2/prime-rate/available?search=BR&token=SEU_TOKEN"
        ```

        Args:
          token: **Obrigatório caso não esteja adicionado como header "Authorization".** Seu
              token de autenticação pessoal da API Brapi.

              **Formas de Envio:**

              1.  **Query Parameter:** Adicione `?token=SEU_TOKEN` ao final da URL.
              2.  **HTTP Header:** Inclua o header `Authorization: Bearer SEU_TOKEN` na sua
                  requisição.

              Ambos os métodos são aceitos, mas pelo menos um deles deve ser utilizado.
              Obtenha seu token em [brapi.dev/dashboard](https://brapi.dev/dashboard).

          search: **Opcional.** Termo para filtrar a lista de países por nome. Retorna países
              cujos nomes contenham o termo especificado (case insensitive).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/prime-rate/available",
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
                    prime_rate_list_available_params.PrimeRateListAvailableParams,
                ),
            ),
            cast_to=PrimeRateListAvailableResponse,
        )


class AsyncPrimeRateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPrimeRateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPrimeRateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrimeRateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/brapi-python#with_streaming_response
        """
        return AsyncPrimeRateResourceWithStreamingResponse(self)

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
    ) -> PrimeRateRetrieveResponse:
        """
        Obtenha informações atualizadas sobre a taxa básica de juros (SELIC) de um país
        por um período determinado.

        ### Funcionalidades:

        - **Seleção por País:** Especifique o país desejado usando o parâmetro `country`
          (padrão: brazil).
        - **Período Customizado:** Defina datas de início e fim com `start` e `end` para
          consultar um intervalo específico.
        - **Ordenação:** Ordene os resultados por data ou valor com os parâmetros
          `sortBy` e `sortOrder`.
        - **Dados Históricos:** Solicite o histórico completo ou apenas o valor mais
          recente com o parâmetro `historical`.

        ### Autenticação:

        Requer token de autenticação via `token` (query) ou `Authorization` (header).

        ### Exemplo de Requisição:

        **Taxa de juros do Brasil entre dezembro/2021 e janeiro/2022:**

        ```bash
        curl -X GET "https://brapi.dev/api/v2/prime-rate?country=brazil&start=01/12/2021&end=01/01/2022&sortBy=date&sortOrder=desc&token=SEU_TOKEN"
        ```

        Args:
          token: **Obrigatório caso não esteja adicionado como header "Authorization".** Seu
              token de autenticação pessoal da API Brapi.

              **Formas de Envio:**

              1.  **Query Parameter:** Adicione `?token=SEU_TOKEN` ao final da URL.
              2.  **HTTP Header:** Inclua o header `Authorization: Bearer SEU_TOKEN` na sua
                  requisição.

              Ambos os métodos são aceitos, mas pelo menos um deles deve ser utilizado.
              Obtenha seu token em [brapi.dev/dashboard](https://brapi.dev/dashboard).

          country: **Opcional.** O país do qual você deseja obter informações sobre a taxa básica
              de juros. Por padrão, o país é definido como brazil. Você pode consultar a lista
              de países disponíveis através do endpoint `/api/v2/prime-rate/available`.

          end: **Opcional.** Data final do período para busca no formato DD/MM/YYYY. Por padrão
              é a data atual. Útil quando `historical=true` para restringir o período da série
              histórica.

          historical: **Opcional.** Define se os dados históricos serão retornados. Se definido como
              `true`, retorna a série histórica completa. Se `false` (padrão) ou omitido,
              retorna apenas o valor mais recente.

          sort_by: **Opcional.** Campo pelo qual os resultados serão ordenados. Por padrão, ordena
              por `date` (data).

          sort_order: **Opcional.** Define se a ordenação será crescente (`asc`) ou decrescente
              (`desc`). Por padrão, é `desc` (decrescente).

          start: **Opcional.** Data inicial do período para busca no formato DD/MM/YYYY. Útil
              quando `historical=true` para restringir o período da série histórica.

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
                        "token": token,
                        "country": country,
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
        token: str | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PrimeRateListAvailableResponse:
        """
        Liste todos os países disponíveis com dados de taxa básica de juros (SELIC) na
        API brapi. Este endpoint facilita a descoberta de quais países possuem dados
        disponíveis para consulta através do endpoint principal `/api/v2/prime-rate`.

        ### Funcionalidades:

        - **Busca Filtrada:** Utilize o parâmetro `search` para filtrar países por nome
          ou parte do nome.
        - **Ideal para Autocomplete:** Perfeito para implementar campos de busca com
          autocompletar em interfaces de usuário.

        ### Autenticação:

        Requer token de autenticação via `token` (query) ou `Authorization` (header).

        ### Exemplo de Requisição:

        **Listar países que contenham "BR" no nome:**

        ```bash
        curl -X GET "https://brapi.dev/api/v2/prime-rate/available?search=BR&token=SEU_TOKEN"
        ```

        Args:
          token: **Obrigatório caso não esteja adicionado como header "Authorization".** Seu
              token de autenticação pessoal da API Brapi.

              **Formas de Envio:**

              1.  **Query Parameter:** Adicione `?token=SEU_TOKEN` ao final da URL.
              2.  **HTTP Header:** Inclua o header `Authorization: Bearer SEU_TOKEN` na sua
                  requisição.

              Ambos os métodos são aceitos, mas pelo menos um deles deve ser utilizado.
              Obtenha seu token em [brapi.dev/dashboard](https://brapi.dev/dashboard).

          search: **Opcional.** Termo para filtrar a lista de países por nome. Retorna países
              cujos nomes contenham o termo especificado (case insensitive).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/prime-rate/available",
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
                    prime_rate_list_available_params.PrimeRateListAvailableParams,
                ),
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
