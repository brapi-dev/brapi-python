# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import quote_list_params, quote_retrieve_params
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
from ..types.quote_list_response import QuoteListResponse
from ..types.quote_retrieve_response import QuoteRetrieveResponse

__all__ = ["QuoteResource", "AsyncQuoteResource"]


class QuoteResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QuoteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/brapi-python#accessing-raw-response-data-eg-headers
        """
        return QuoteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QuoteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/brapi-python#with_streaming_response
        """
        return QuoteResourceWithStreamingResponse(self)

    def retrieve(
        self,
        tickers: str,
        *,
        token: str | Omit = omit,
        dividends: bool | Omit = omit,
        fundamental: bool | Omit = omit,
        interval: Literal["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
        | Omit = omit,
        modules: List[
            Literal[
                "summaryProfile",
                "balanceSheetHistory",
                "defaultKeyStatistics",
                "balanceSheetHistoryQuarterly",
                "incomeStatementHistory",
                "incomeStatementHistoryQuarterly",
                "financialData",
                "financialDataHistory",
                "financialDataHistoryQuarterly",
                "defaultKeyStatisticsHistory",
                "defaultKeyStatisticsHistoryQuarterly",
                "valueAddedHistory",
                "valueAddedHistoryQuarterly",
                "cashflowHistory",
                "cashflowHistoryQuarterly",
            ]
        ]
        | Omit = omit,
        range: Literal["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QuoteRetrieveResponse:
        """
        Este endpoint é a principal forma de obter informações detalhadas sobre um ou
        mais ativos financeiros (ações, FIIs, ETFs, BDRs, índices) listados na B3,
        identificados pelos seus respectivos **tickers**.

        ### Funcionalidades Principais:

        - **Cotação Atual:** Retorna o preço mais recente, variação diária, máximas,
          mínimas, volume, etc.
        - **Dados Históricos:** Permite solicitar séries históricas de preços usando os
          parâmetros `range` e `interval`.
        - **Dados Fundamentalistas:** Opcionalmente, inclui dados fundamentalistas
          básicos (P/L, LPA) com o parâmetro `fundamental=true`.
        - **Dividendos:** Opcionalmente, inclui histórico de dividendos e JCP com
          `dividends=true`.
        - **Módulos Adicionais:** Permite requisitar conjuntos de dados financeiros mais
          aprofundados através do parâmetro `modules` (veja detalhes abaixo).

        ### 🧪 Ações de Teste (Sem Autenticação):

        Para facilitar o desenvolvimento e teste, as seguintes **4 ações têm acesso
        irrestrito** e **não requerem autenticação**:

        - **PETR4** (Petrobras PN)
        - **MGLU3** (Magazine Luiza ON)
        - **VALE3** (Vale ON)
        - **ITUB4** (Itaú Unibanco PN)

        **Importante:** Você pode consultar essas ações sem token e com acesso a todos
        os recursos (históricos, módulos, dividendos). Porém, se misturar essas ações
        com outras na mesma requisição, a autenticação será obrigatória.

        ### Autenticação:

        Para **outras ações** (além das 4 de teste), é **obrigatório** fornecer um token
        de autenticação válido, seja via query parameter `token` ou via header
        `Authorization: Bearer seu_token`.

        ### Exemplos de Requisição:

        **1. Cotação simples de PETR4 e VALE3 (ações de teste - sem token):**

        ```bash
        curl -X GET "https://brapi.dev/api/quote/PETR4,VALE3"
        ```

        **2. Cotação de MGLU3 com dados históricos do último mês (ação de teste - sem
        token):**

        ```bash
        curl -X GET "https://brapi.dev/api/quote/MGLU3?range=1mo&interval=1d"
        ```

        **3. Cotação de ITUB4 incluindo dividendos e dados fundamentalistas (ação de
        teste - sem token):**

        ```bash
        curl -X GET "https://brapi.dev/api/quote/ITUB4?fundamental=true&dividends=true"
        ```

        **4. Cotação de WEGE3 com Resumo da Empresa e Balanço Patrimonial Anual (via
        módulos - requer token):**

        ```bash
        curl -X GET "https://brapi.dev/api/quote/WEGE3?modules=summaryProfile,balanceSheetHistory&token=SEU_TOKEN"
        ```

        **5. Exemplo de requisição mista (requer token):**

        ```bash
        curl -X GET "https://brapi.dev/api/quote/PETR4,BBAS3?token=SEU_TOKEN"
        ```

        _Nota: Como BBAS3 não é uma ação de teste, toda a requisição requer
        autenticação, mesmo contendo PETR4._

        ### Parâmetro `modules` (Detalhado):

        O parâmetro `modules` é extremamente poderoso para enriquecer a resposta com
        dados financeiros detalhados. Você pode solicitar um ou mais módulos, separados
        por vírgula.

        **Módulos Disponíveis:**

        - `summaryProfile`: Informações cadastrais da empresa (endereço, setor,
          descrição do negócio, website, número de funcionários).
        - `balanceSheetHistory`: Histórico **anual** do Balanço Patrimonial.
        - `balanceSheetHistoryQuarterly`: Histórico **trimestral** do Balanço
          Patrimonial.
        - `defaultKeyStatistics`: Principais estatísticas da empresa (Valor de Mercado,
          P/L, ROE, Dividend Yield, etc.) - **TTM (Trailing Twelve Months)**.
        - `defaultKeyStatisticsHistory`: Histórico **anual** das Principais
          Estatísticas.
        - `defaultKeyStatisticsHistoryQuarterly`: Histórico **trimestral** das
          Principais Estatísticas.
        - `incomeStatementHistory`: Histórico **anual** da Demonstração do Resultado do
          Exercício (DRE).
        - `incomeStatementHistoryQuarterly`: Histórico **trimestral** da Demonstração do
          Resultado do Exercício (DRE).
        - `financialData`: Dados financeiros selecionados (Receita, Lucro Bruto, EBITDA,
          Dívida Líquida, Fluxo de Caixa Livre, Margens) - **TTM (Trailing Twelve
          Months)**.
        - `financialDataHistory`: Histórico **anual** dos Dados Financeiros.
        - `financialDataHistoryQuarterly`: Histórico **trimestral** dos Dados
          Financeiros.
        - `valueAddedHistory`: Histórico **anual** da Demonstração do Valor Adicionado
          (DVA).
        - `valueAddedHistoryQuarterly`: Histórico **trimestral** da Demonstração do
          Valor Adicionado (DVA).
        - `cashflowHistory`: Histórico **anual** da Demonstração do Fluxo de Caixa
          (DFC).
        - `cashflowHistoryQuarterly`: Histórico **trimestral** da Demonstração do Fluxo
          de Caixa (DFC).

        **Exemplo de Uso do `modules`:**

        Para obter a cotação de BBDC4 junto com seu DRE trimestral e Fluxo de Caixa
        anual:

        ```bash
        curl -X GET "https://brapi.dev/api/quote/BBDC4?modules=incomeStatementHistoryQuarterly,cashflowHistory&token=SEU_TOKEN"
        ```

        ### Resposta:

        A resposta é um objeto JSON contendo a chave `results`, que é um array. Cada
        elemento do array corresponde a um ticker solicitado e contém os dados da
        cotação e os módulos adicionais requisitados.

        - **Sucesso (200 OK):** Retorna os dados conforme solicitado.
        - **Bad Request (400 Bad Request):** Ocorre se um parâmetro for inválido (ex:
          `range=invalid`) ou se a formatação estiver incorreta.
        - **Unauthorized (401 Unauthorized):** Token inválido ou ausente.
        - **Payment Required (402 Payment Required):** Limite de requisições do plano
          atual excedido.
        - **Not Found (404 Not Found):** Um ou mais tickers solicitados não foram
          encontrados.

        Args:
          token: **Obrigatório caso não esteja adicionado como header "Authorization".** Seu
              token de autenticação pessoal da API Brapi.

              **Formas de Envio:**

              1.  **Query Parameter:** Adicione `?token=SEU_TOKEN` ao final da URL.
              2.  **HTTP Header:** Inclua o header `Authorization: Bearer SEU_TOKEN` na sua
                  requisição.

              Ambos os métodos são aceitos, mas pelo menos um deles deve ser utilizado.
              Obtenha seu token em [brapi.dev/dashboard](https://brapi.dev/dashboard).

          dividends: **Opcional.** Booleano (`true` ou `false`). Se `true`, inclui informações sobre
              dividendos e JCP (Juros sobre Capital Próprio) pagos historicamente pelo ativo
              na chave `dividendsData`.

          fundamental: **Opcional.** Booleano (`true` ou `false`). Se `true`, inclui dados
              fundamentalistas básicos na resposta, como Preço/Lucro (P/L) e Lucro Por Ação
              (LPA).

              **Nota:** Para dados fundamentalistas mais completos, utilize o parâmetro
              `modules`.

          interval: **Opcional.** Define a granularidade (intervalo) dos dados históricos de preço
              (`historicalDataPrice`). Requer que `range` também seja especificado.

              **Valores Possíveis:**

              - `1m`, `2m`, `5m`, `15m`, `30m`, `60m`, `90m`, `1h`: Intervalos intraday
                (minutos/horas). **Atenção:** Disponibilidade pode variar conforme o `range` e
                o ativo.
              - `1d`: Diário (padrão se `range` for especificado e `interval` omitido).
              - `5d`: 5 dias.
              - `1wk`: Semanal.
              - `1mo`: Mensal.
              - `3mo`: Trimestral.

          modules: **Opcional.** Uma lista de módulos de dados adicionais, separados por vírgula
              (`,`), para incluir na resposta. Permite buscar dados financeiros detalhados.

              **Exemplos:**

              - `modules=summaryProfile` (retorna perfil da empresa)
              - `modules=balanceSheetHistory,incomeStatementHistory` (retorna histórico anual
                do BP e DRE)

              Veja a descrição principal do endpoint para a lista completa de módulos e seus
              conteúdos.

          range: **Opcional.** Define o período para os dados históricos de preço
              (`historicalDataPrice`). Se omitido, apenas a cotação mais recente é retornada
              (a menos que `interval` seja usado).

              **Valores Possíveis:**

              - `1d`: Último dia de pregão (intraday se `interval` for minutos/horas).
              - `5d`: Últimos 5 dias.
              - `1mo`: Último mês.
              - `3mo`: Últimos 3 meses.
              - `6mo`: Últimos 6 meses.
              - `1y`: Último ano.
              - `2y`: Últimos 2 anos.
              - `5y`: Últimos 5 anos.
              - `10y`: Últimos 10 anos.
              - `ytd`: Desde o início do ano atual (Year-to-Date).
              - `max`: Todo o período histórico disponível.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tickers:
            raise ValueError(f"Expected a non-empty value for `tickers` but received {tickers!r}")
        return self._get(
            f"/api/quote/{tickers}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "token": token,
                        "dividends": dividends,
                        "fundamental": fundamental,
                        "interval": interval,
                        "modules": modules,
                        "range": range,
                    },
                    quote_retrieve_params.QuoteRetrieveParams,
                ),
            ),
            cast_to=QuoteRetrieveResponse,
        )

    def list(
        self,
        *,
        token: str | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        search: str | Omit = omit,
        sector: Literal[
            "Retail Trade",
            "Energy Minerals",
            "Health Services",
            "Utilities",
            "Finance",
            "Consumer Services",
            "Consumer Non-Durables",
            "Non-Energy Minerals",
            "Commercial Services",
            "Distribution Services",
            "Transportation",
            "Technology Services",
            "Process Industries",
            "Communications",
            "Producer Manufacturing",
            "Miscellaneous",
            "Electronic Technology",
            "Industrial Services",
            "Health Technology",
            "Consumer Durables",
        ]
        | Omit = omit,
        sort_by: Literal["name", "close", "change", "change_abs", "volume", "market_cap_basic", "sector"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        type: Literal["stock", "fund", "bdr"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QuoteListResponse:
        """
        Obtenha uma lista paginada de cotações de diversos ativos (ações, FIIs, BDRs)
        negociados na B3, com opções avançadas de busca, filtragem e ordenação.

        ### Funcionalidades:

        - **Busca por Ticker:** Filtre por parte do ticker usando `search`.
        - **Filtragem por Tipo:** Restrinja a lista a `stock`, `fund` (FII) ou `bdr` com
          o parâmetro `type`.
        - **Filtragem por Setor:** Selecione ativos de um setor específico usando
          `sector`.
        - **Ordenação:** Ordene os resultados por diversos campos (preço, variação,
          volume, etc.) usando `sortBy` e `sortOrder`.
        - **Paginação:** Controle o número de resultados por página (`limit`) e a página
          desejada (`page`).

        ### Autenticação:

        Requer token de autenticação via `token` (query) ou `Authorization` (header).

        ### Exemplo de Requisição:

        **Listar as 10 ações do setor Financeiro com maior volume, ordenadas de forma
        decrescente:**

        ```bash
        curl -X GET "https://brapi.dev/api/quote/list?sector=Finance&sortBy=volume&sortOrder=desc&limit=10&page=1&token=SEU_TOKEN"
        ```

        **Buscar por ativos cujo ticker contenha 'ITUB' e ordenar por nome ascendente:**

        ```bash
        curl -X GET "https://brapi.dev/api/quote/list?search=ITUB&sortBy=name&sortOrder=asc&token=SEU_TOKEN"
        ```

        ### Resposta:

        A resposta contém a lista de `stocks` (e `indexes` relevantes), informações
        sobre os filtros aplicados, detalhes da paginação (`currentPage`, `totalPages`,
        `itemsPerPage`, `totalCount`, `hasNextPage`) e listas de setores
        (`availableSectors`) e tipos (`availableStockTypes`) disponíveis para filtragem.

        Args:
          token: **Obrigatório caso não esteja adicionado como header "Authorization".** Seu
              token de autenticação pessoal da API Brapi.

              **Formas de Envio:**

              1.  **Query Parameter:** Adicione `?token=SEU_TOKEN` ao final da URL.
              2.  **HTTP Header:** Inclua o header `Authorization: Bearer SEU_TOKEN` na sua
                  requisição.

              Ambos os métodos são aceitos, mas pelo menos um deles deve ser utilizado.
              Obtenha seu token em [brapi.dev/dashboard](https://brapi.dev/dashboard).

          limit: **Opcional.** Número máximo de ativos a serem retornados por página. O valor
              padrão pode variar.

          page: **Opcional.** Número da página dos resultados a ser retornada, considerando o
              `limit` especificado. Começa em 1.

          search:
              **Opcional.** Termo para buscar ativos por ticker (correspondência parcial). Ex:
              `PETR` encontrará `PETR4`, `PETR3`.

          sector: **Opcional.** Filtra os resultados por setor de atuação da empresa. Utilize um
              dos valores retornados em `availableSectors`.

          sort_by: **Opcional.** Campo pelo qual os resultados serão ordenados.

          sort_order: **Opcional.** Direção da ordenação: `asc` (ascendente) ou `desc` (descendente).
              Requer que `sortBy` seja especificado.

          type: **Opcional.** Filtra os resultados por tipo de ativo.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/quote/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "token": token,
                        "limit": limit,
                        "page": page,
                        "search": search,
                        "sector": sector,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "type": type,
                    },
                    quote_list_params.QuoteListParams,
                ),
            ),
            cast_to=QuoteListResponse,
        )


class AsyncQuoteResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQuoteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQuoteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQuoteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/brapi-python#with_streaming_response
        """
        return AsyncQuoteResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        tickers: str,
        *,
        token: str | Omit = omit,
        dividends: bool | Omit = omit,
        fundamental: bool | Omit = omit,
        interval: Literal["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
        | Omit = omit,
        modules: List[
            Literal[
                "summaryProfile",
                "balanceSheetHistory",
                "defaultKeyStatistics",
                "balanceSheetHistoryQuarterly",
                "incomeStatementHistory",
                "incomeStatementHistoryQuarterly",
                "financialData",
                "financialDataHistory",
                "financialDataHistoryQuarterly",
                "defaultKeyStatisticsHistory",
                "defaultKeyStatisticsHistoryQuarterly",
                "valueAddedHistory",
                "valueAddedHistoryQuarterly",
                "cashflowHistory",
                "cashflowHistoryQuarterly",
            ]
        ]
        | Omit = omit,
        range: Literal["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QuoteRetrieveResponse:
        """
        Este endpoint é a principal forma de obter informações detalhadas sobre um ou
        mais ativos financeiros (ações, FIIs, ETFs, BDRs, índices) listados na B3,
        identificados pelos seus respectivos **tickers**.

        ### Funcionalidades Principais:

        - **Cotação Atual:** Retorna o preço mais recente, variação diária, máximas,
          mínimas, volume, etc.
        - **Dados Históricos:** Permite solicitar séries históricas de preços usando os
          parâmetros `range` e `interval`.
        - **Dados Fundamentalistas:** Opcionalmente, inclui dados fundamentalistas
          básicos (P/L, LPA) com o parâmetro `fundamental=true`.
        - **Dividendos:** Opcionalmente, inclui histórico de dividendos e JCP com
          `dividends=true`.
        - **Módulos Adicionais:** Permite requisitar conjuntos de dados financeiros mais
          aprofundados através do parâmetro `modules` (veja detalhes abaixo).

        ### 🧪 Ações de Teste (Sem Autenticação):

        Para facilitar o desenvolvimento e teste, as seguintes **4 ações têm acesso
        irrestrito** e **não requerem autenticação**:

        - **PETR4** (Petrobras PN)
        - **MGLU3** (Magazine Luiza ON)
        - **VALE3** (Vale ON)
        - **ITUB4** (Itaú Unibanco PN)

        **Importante:** Você pode consultar essas ações sem token e com acesso a todos
        os recursos (históricos, módulos, dividendos). Porém, se misturar essas ações
        com outras na mesma requisição, a autenticação será obrigatória.

        ### Autenticação:

        Para **outras ações** (além das 4 de teste), é **obrigatório** fornecer um token
        de autenticação válido, seja via query parameter `token` ou via header
        `Authorization: Bearer seu_token`.

        ### Exemplos de Requisição:

        **1. Cotação simples de PETR4 e VALE3 (ações de teste - sem token):**

        ```bash
        curl -X GET "https://brapi.dev/api/quote/PETR4,VALE3"
        ```

        **2. Cotação de MGLU3 com dados históricos do último mês (ação de teste - sem
        token):**

        ```bash
        curl -X GET "https://brapi.dev/api/quote/MGLU3?range=1mo&interval=1d"
        ```

        **3. Cotação de ITUB4 incluindo dividendos e dados fundamentalistas (ação de
        teste - sem token):**

        ```bash
        curl -X GET "https://brapi.dev/api/quote/ITUB4?fundamental=true&dividends=true"
        ```

        **4. Cotação de WEGE3 com Resumo da Empresa e Balanço Patrimonial Anual (via
        módulos - requer token):**

        ```bash
        curl -X GET "https://brapi.dev/api/quote/WEGE3?modules=summaryProfile,balanceSheetHistory&token=SEU_TOKEN"
        ```

        **5. Exemplo de requisição mista (requer token):**

        ```bash
        curl -X GET "https://brapi.dev/api/quote/PETR4,BBAS3?token=SEU_TOKEN"
        ```

        _Nota: Como BBAS3 não é uma ação de teste, toda a requisição requer
        autenticação, mesmo contendo PETR4._

        ### Parâmetro `modules` (Detalhado):

        O parâmetro `modules` é extremamente poderoso para enriquecer a resposta com
        dados financeiros detalhados. Você pode solicitar um ou mais módulos, separados
        por vírgula.

        **Módulos Disponíveis:**

        - `summaryProfile`: Informações cadastrais da empresa (endereço, setor,
          descrição do negócio, website, número de funcionários).
        - `balanceSheetHistory`: Histórico **anual** do Balanço Patrimonial.
        - `balanceSheetHistoryQuarterly`: Histórico **trimestral** do Balanço
          Patrimonial.
        - `defaultKeyStatistics`: Principais estatísticas da empresa (Valor de Mercado,
          P/L, ROE, Dividend Yield, etc.) - **TTM (Trailing Twelve Months)**.
        - `defaultKeyStatisticsHistory`: Histórico **anual** das Principais
          Estatísticas.
        - `defaultKeyStatisticsHistoryQuarterly`: Histórico **trimestral** das
          Principais Estatísticas.
        - `incomeStatementHistory`: Histórico **anual** da Demonstração do Resultado do
          Exercício (DRE).
        - `incomeStatementHistoryQuarterly`: Histórico **trimestral** da Demonstração do
          Resultado do Exercício (DRE).
        - `financialData`: Dados financeiros selecionados (Receita, Lucro Bruto, EBITDA,
          Dívida Líquida, Fluxo de Caixa Livre, Margens) - **TTM (Trailing Twelve
          Months)**.
        - `financialDataHistory`: Histórico **anual** dos Dados Financeiros.
        - `financialDataHistoryQuarterly`: Histórico **trimestral** dos Dados
          Financeiros.
        - `valueAddedHistory`: Histórico **anual** da Demonstração do Valor Adicionado
          (DVA).
        - `valueAddedHistoryQuarterly`: Histórico **trimestral** da Demonstração do
          Valor Adicionado (DVA).
        - `cashflowHistory`: Histórico **anual** da Demonstração do Fluxo de Caixa
          (DFC).
        - `cashflowHistoryQuarterly`: Histórico **trimestral** da Demonstração do Fluxo
          de Caixa (DFC).

        **Exemplo de Uso do `modules`:**

        Para obter a cotação de BBDC4 junto com seu DRE trimestral e Fluxo de Caixa
        anual:

        ```bash
        curl -X GET "https://brapi.dev/api/quote/BBDC4?modules=incomeStatementHistoryQuarterly,cashflowHistory&token=SEU_TOKEN"
        ```

        ### Resposta:

        A resposta é um objeto JSON contendo a chave `results`, que é um array. Cada
        elemento do array corresponde a um ticker solicitado e contém os dados da
        cotação e os módulos adicionais requisitados.

        - **Sucesso (200 OK):** Retorna os dados conforme solicitado.
        - **Bad Request (400 Bad Request):** Ocorre se um parâmetro for inválido (ex:
          `range=invalid`) ou se a formatação estiver incorreta.
        - **Unauthorized (401 Unauthorized):** Token inválido ou ausente.
        - **Payment Required (402 Payment Required):** Limite de requisições do plano
          atual excedido.
        - **Not Found (404 Not Found):** Um ou mais tickers solicitados não foram
          encontrados.

        Args:
          token: **Obrigatório caso não esteja adicionado como header "Authorization".** Seu
              token de autenticação pessoal da API Brapi.

              **Formas de Envio:**

              1.  **Query Parameter:** Adicione `?token=SEU_TOKEN` ao final da URL.
              2.  **HTTP Header:** Inclua o header `Authorization: Bearer SEU_TOKEN` na sua
                  requisição.

              Ambos os métodos são aceitos, mas pelo menos um deles deve ser utilizado.
              Obtenha seu token em [brapi.dev/dashboard](https://brapi.dev/dashboard).

          dividends: **Opcional.** Booleano (`true` ou `false`). Se `true`, inclui informações sobre
              dividendos e JCP (Juros sobre Capital Próprio) pagos historicamente pelo ativo
              na chave `dividendsData`.

          fundamental: **Opcional.** Booleano (`true` ou `false`). Se `true`, inclui dados
              fundamentalistas básicos na resposta, como Preço/Lucro (P/L) e Lucro Por Ação
              (LPA).

              **Nota:** Para dados fundamentalistas mais completos, utilize o parâmetro
              `modules`.

          interval: **Opcional.** Define a granularidade (intervalo) dos dados históricos de preço
              (`historicalDataPrice`). Requer que `range` também seja especificado.

              **Valores Possíveis:**

              - `1m`, `2m`, `5m`, `15m`, `30m`, `60m`, `90m`, `1h`: Intervalos intraday
                (minutos/horas). **Atenção:** Disponibilidade pode variar conforme o `range` e
                o ativo.
              - `1d`: Diário (padrão se `range` for especificado e `interval` omitido).
              - `5d`: 5 dias.
              - `1wk`: Semanal.
              - `1mo`: Mensal.
              - `3mo`: Trimestral.

          modules: **Opcional.** Uma lista de módulos de dados adicionais, separados por vírgula
              (`,`), para incluir na resposta. Permite buscar dados financeiros detalhados.

              **Exemplos:**

              - `modules=summaryProfile` (retorna perfil da empresa)
              - `modules=balanceSheetHistory,incomeStatementHistory` (retorna histórico anual
                do BP e DRE)

              Veja a descrição principal do endpoint para a lista completa de módulos e seus
              conteúdos.

          range: **Opcional.** Define o período para os dados históricos de preço
              (`historicalDataPrice`). Se omitido, apenas a cotação mais recente é retornada
              (a menos que `interval` seja usado).

              **Valores Possíveis:**

              - `1d`: Último dia de pregão (intraday se `interval` for minutos/horas).
              - `5d`: Últimos 5 dias.
              - `1mo`: Último mês.
              - `3mo`: Últimos 3 meses.
              - `6mo`: Últimos 6 meses.
              - `1y`: Último ano.
              - `2y`: Últimos 2 anos.
              - `5y`: Últimos 5 anos.
              - `10y`: Últimos 10 anos.
              - `ytd`: Desde o início do ano atual (Year-to-Date).
              - `max`: Todo o período histórico disponível.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tickers:
            raise ValueError(f"Expected a non-empty value for `tickers` but received {tickers!r}")
        return await self._get(
            f"/api/quote/{tickers}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "token": token,
                        "dividends": dividends,
                        "fundamental": fundamental,
                        "interval": interval,
                        "modules": modules,
                        "range": range,
                    },
                    quote_retrieve_params.QuoteRetrieveParams,
                ),
            ),
            cast_to=QuoteRetrieveResponse,
        )

    async def list(
        self,
        *,
        token: str | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        search: str | Omit = omit,
        sector: Literal[
            "Retail Trade",
            "Energy Minerals",
            "Health Services",
            "Utilities",
            "Finance",
            "Consumer Services",
            "Consumer Non-Durables",
            "Non-Energy Minerals",
            "Commercial Services",
            "Distribution Services",
            "Transportation",
            "Technology Services",
            "Process Industries",
            "Communications",
            "Producer Manufacturing",
            "Miscellaneous",
            "Electronic Technology",
            "Industrial Services",
            "Health Technology",
            "Consumer Durables",
        ]
        | Omit = omit,
        sort_by: Literal["name", "close", "change", "change_abs", "volume", "market_cap_basic", "sector"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        type: Literal["stock", "fund", "bdr"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QuoteListResponse:
        """
        Obtenha uma lista paginada de cotações de diversos ativos (ações, FIIs, BDRs)
        negociados na B3, com opções avançadas de busca, filtragem e ordenação.

        ### Funcionalidades:

        - **Busca por Ticker:** Filtre por parte do ticker usando `search`.
        - **Filtragem por Tipo:** Restrinja a lista a `stock`, `fund` (FII) ou `bdr` com
          o parâmetro `type`.
        - **Filtragem por Setor:** Selecione ativos de um setor específico usando
          `sector`.
        - **Ordenação:** Ordene os resultados por diversos campos (preço, variação,
          volume, etc.) usando `sortBy` e `sortOrder`.
        - **Paginação:** Controle o número de resultados por página (`limit`) e a página
          desejada (`page`).

        ### Autenticação:

        Requer token de autenticação via `token` (query) ou `Authorization` (header).

        ### Exemplo de Requisição:

        **Listar as 10 ações do setor Financeiro com maior volume, ordenadas de forma
        decrescente:**

        ```bash
        curl -X GET "https://brapi.dev/api/quote/list?sector=Finance&sortBy=volume&sortOrder=desc&limit=10&page=1&token=SEU_TOKEN"
        ```

        **Buscar por ativos cujo ticker contenha 'ITUB' e ordenar por nome ascendente:**

        ```bash
        curl -X GET "https://brapi.dev/api/quote/list?search=ITUB&sortBy=name&sortOrder=asc&token=SEU_TOKEN"
        ```

        ### Resposta:

        A resposta contém a lista de `stocks` (e `indexes` relevantes), informações
        sobre os filtros aplicados, detalhes da paginação (`currentPage`, `totalPages`,
        `itemsPerPage`, `totalCount`, `hasNextPage`) e listas de setores
        (`availableSectors`) e tipos (`availableStockTypes`) disponíveis para filtragem.

        Args:
          token: **Obrigatório caso não esteja adicionado como header "Authorization".** Seu
              token de autenticação pessoal da API Brapi.

              **Formas de Envio:**

              1.  **Query Parameter:** Adicione `?token=SEU_TOKEN` ao final da URL.
              2.  **HTTP Header:** Inclua o header `Authorization: Bearer SEU_TOKEN` na sua
                  requisição.

              Ambos os métodos são aceitos, mas pelo menos um deles deve ser utilizado.
              Obtenha seu token em [brapi.dev/dashboard](https://brapi.dev/dashboard).

          limit: **Opcional.** Número máximo de ativos a serem retornados por página. O valor
              padrão pode variar.

          page: **Opcional.** Número da página dos resultados a ser retornada, considerando o
              `limit` especificado. Começa em 1.

          search:
              **Opcional.** Termo para buscar ativos por ticker (correspondência parcial). Ex:
              `PETR` encontrará `PETR4`, `PETR3`.

          sector: **Opcional.** Filtra os resultados por setor de atuação da empresa. Utilize um
              dos valores retornados em `availableSectors`.

          sort_by: **Opcional.** Campo pelo qual os resultados serão ordenados.

          sort_order: **Opcional.** Direção da ordenação: `asc` (ascendente) ou `desc` (descendente).
              Requer que `sortBy` seja especificado.

          type: **Opcional.** Filtra os resultados por tipo de ativo.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/quote/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "token": token,
                        "limit": limit,
                        "page": page,
                        "search": search,
                        "sector": sector,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "type": type,
                    },
                    quote_list_params.QuoteListParams,
                ),
            ),
            cast_to=QuoteListResponse,
        )


class QuoteResourceWithRawResponse:
    def __init__(self, quote: QuoteResource) -> None:
        self._quote = quote

        self.retrieve = to_raw_response_wrapper(
            quote.retrieve,
        )
        self.list = to_raw_response_wrapper(
            quote.list,
        )


class AsyncQuoteResourceWithRawResponse:
    def __init__(self, quote: AsyncQuoteResource) -> None:
        self._quote = quote

        self.retrieve = async_to_raw_response_wrapper(
            quote.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            quote.list,
        )


class QuoteResourceWithStreamingResponse:
    def __init__(self, quote: QuoteResource) -> None:
        self._quote = quote

        self.retrieve = to_streamed_response_wrapper(
            quote.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            quote.list,
        )


class AsyncQuoteResourceWithStreamingResponse:
    def __init__(self, quote: AsyncQuoteResource) -> None:
        self._quote = quote

        self.retrieve = async_to_streamed_response_wrapper(
            quote.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            quote.list,
        )
