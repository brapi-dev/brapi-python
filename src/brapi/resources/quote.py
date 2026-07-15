# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import quote_list_params, quote_retrieve_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
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
    """Consulte informações detalhadas sobre ações, BDRs, ETFs e índices brasileiros.

    Obtenha preços em tempo real, dados fundamentalistas, históricos e dividendos.
    """

    @cached_property
    def with_raw_response(self) -> QuoteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return QuoteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QuoteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return QuoteResourceWithStreamingResponse(self)

    def retrieve(
        self,
        tickers: str,
        *,
        token: str | Omit = omit,
        dividends: Literal["true", "false"] | Omit = omit,
        end_date: str | Omit = omit,
        interval: Literal["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
        | Omit = omit,
        modules: str | Omit = omit,
        range: Literal["1d", "2d", "5d", "7d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]
        | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QuoteRetrieveResponse:
        """
        **O ENDPOINT MAIS IMPORTANTE DA API.** Obtém dados detalhados e abrangentes de
        um ou múltiplos ativos (ações, FIIs, BDRs) em uma única requisição. Combine
        cotações em tempo real, dados históricos, fundamentos e dividendos conforme
        necessário.

        ### Funcionalidades:

        - **Cotação em Tempo Real:** Preço atual, variação absoluta e percentual,
          volume, máxima/mínima do dia, range de 52 semanas.
        - **Dados Históricos:** Preços OHLCV (Open, High, Low, Close, Volume) com
          intervalos flexíveis (1d, 5d, 1wk, 1mo, 3mo) e períodos (1d até max).
        - **Fundamentos:** Balanço Patrimonial, DRE, Fluxo de Caixa, DVA,
          Indicadores-chave (P/L, P/VP, ROE, etc) via parâmetro `modules`.
        - **Dividendos:** Histórico completo de proventos em dinheiro (dividendos, JCP)
          e bonificações.

        ### Autenticação:

        Requer token Bearer no header ou como query param. Tickers de teste **PETR4** e
        **VALE3** funcionam sem autenticação.

        ```bash
        # Via header (recomendado)
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/quote/PETR4"

        # Via query param
        curl "https://brapi.dev/api/quote/PETR4?token=SEU_TOKEN"
        ```

        ### Exemplos de Requisição:

        ```bash
        # Simples: apenas cotação atual
        curl "https://brapi.dev/api/quote/PETR4?token=SEU_TOKEN"

        # Múltiplos tickers em uma requisição
        curl "https://brapi.dev/api/quote/PETR4,VALE3,ITUB4?token=SEU_TOKEN"

        # Com dados históricos (últimos 12 meses, diário)
        curl "https://brapi.dev/api/quote/PETR4?range=1y&interval=1d&token=SEU_TOKEN"

        # Com módulos de fundamentos (balanço e DRE)
        curl "https://brapi.dev/api/quote/PETR4?modules=balanceSheetHistory,incomeStatementHistory&token=SEU_TOKEN"

        # Completo: histórico + dividendos + estatísticas-chave
        curl "https://brapi.dev/api/quote/PETR4?range=6mo&interval=1d&dividends=true&modules=balanceSheetHistory,defaultKeyStatistics&token=SEU_TOKEN"
        ```

        ### Módulos Disponíveis:

        - `summaryProfile` — Perfil da empresa (CNPJ, setor, descrição, website,
          funcionários)
        - `balanceSheetHistory` — Balanço Patrimonial anual
        - `balanceSheetHistoryQuarterly` — Balanço Patrimonial trimestral
        - `incomeStatementHistory` — DRE anual (Demonstração de Resultado do Exercício)
        - `incomeStatementHistoryQuarterly` — DRE trimestral
        - `financialData` — Indicadores financeiros atuais (TTM - Trailing Twelve
          Months)
        - `financialDataHistory` — Histórico anual de indicadores financeiros
        - `financialDataHistoryQuarterly` — Histórico trimestral de indicadores
          financeiros
        - `defaultKeyStatistics` — Estatísticas-chave (P/L, P/VP, ROE, Dividend Yield,
          etc)
        - `defaultKeyStatisticsHistory` — Histórico anual de estatísticas-chave
        - `defaultKeyStatisticsHistoryQuarterly` — Histórico trimestral de
          estatísticas-chave
        - `cashflowHistory` — Fluxo de Caixa anual
        - `cashflowHistoryQuarterly` — Fluxo de Caixa trimestral
        - `valueAddedHistory` — DVA anual (Demonstração de Valor Adicionado)
        - `valueAddedHistoryQuarterly` — DVA trimestral

        ### Intervalos Válidos (histórico):

        - `1d` — Diário
        - `5d` — 5 dias
        - `1wk` — Semanal
        - `1mo` — Mensal
        - `3mo` — Trimestral

        ### Períodos Válidos (range):

        - `1d` — Último dia
        - `5d` — Últimos 5 dias
        - `1mo` — Último mês
        - `3mo` — Últimos 3 meses
        - `6mo` — Últimos 6 meses
        - `1y` — Último ano
        - `2y` — Últimos 2 anos
        - `5y` — Últimos 5 anos
        - `10y` — Últimos 10 anos
        - `ytd` — Ano até hoje
        - `max` — Máximo disponível

        ### Campos Principais da Resposta:

        - `symbol` — Ticker do ativo (ex: PETR4)
        - `shortName` — Nome curto da empresa
        - `currency` — Moeda (BRL)
        - `regularMarketPrice` — Preço atual em BRL
        - `regularMarketChange` — Variação absoluta
        - `regularMarketChangePercent` — Variação percentual (%)
        - `regularMarketVolume` — Volume de negociação do dia
        - `regularMarketDayHigh` — Máxima do dia
        - `regularMarketDayLow` — Mínima do dia
        - `fiftyTwoWeekHigh` — Máxima de 52 semanas
        - `fiftyTwoWeekLow` — Mínima de 52 semanas
        - `marketCap` — Capitalização de mercado
        - `historicalDataPrice` — Array de dados OHLCV (quando `range`/`interval`
          fornecidos)
        - `dividendsData` — Histórico de dividendos (quando `dividends=true`)

        ### Tickers Populares (Teste):

        - `PETR4` — Petrobras (Energia)
        - `VALE3` — Vale (Mineração)
        - `ITUB4` — Itaú Unibanco (Financeiro)
        - `BBDC4` — Bradesco (Financeiro)
        - `ABEV3` — Ambev (Consumo)
        - `WEGE3` — WEG (Indústria)
        - `RENT3` — Localiza (Transporte)
        - `BBAS3` — Banco do Brasil (Financeiro)
        - `MGLU3` — Magazine Luiza (Varejo)

        ### Fonte dos Dados:

        CVM (Comissão de Valores Mobiliários)

        **Plano Mínimo:** Gratuito (limitado a 1 ticker/requisição e módulos básicos)
        **Autenticação:** Necessária para produção (tickers de teste PETR4 e VALE3
        funcionam sem token)

        Args:
          tickers: Ticker(s) de ativos separados por vírgula (ex: PETR4 ou PETR4,VALE3,ITUB4)

          token: Token de autenticação (alternativa ao header Authorization)

          dividends: Incluir histórico de dividendos e JCP

          end_date: Data final para dados históricos (formato YYYY-MM-DD)

          interval: Intervalo/granularidade dos dados históricos

          modules: Módulos de dados adicionais separados por vírgula

          range: Período para dados históricos de preço

          start_date: Data inicial para dados históricos (formato YYYY-MM-DD)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tickers:
            raise ValueError(f"Expected a non-empty value for `tickers` but received {tickers!r}")
        return self._get(
            path_template("/api/quote/{tickers}", tickers=tickers),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "token": token,
                        "dividends": dividends,
                        "end_date": end_date,
                        "interval": interval,
                        "modules": modules,
                        "range": range,
                        "start_date": start_date,
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
        limit: str | Omit = omit,
        page: str | Omit = omit,
        search: str | Omit = omit,
        sector: str | Omit = omit,
        sort_by: Literal["name", "close", "change", "change_abs", "volume", "market_cap_basic"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        subsector: str | Omit = omit,
        sub_type: Literal["stock", "unit", "fii", "etf", "fi-infra", "fi-agro", "fip", "fidc", "bdr"] | Omit = omit,
        type: Literal["stock", "fund", "bdr"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QuoteListResponse:
        """
        Retorna uma lista paginada de todos os ativos disponíveis na API (Ações, FIIs,
        BDRs, ETFs, Índices). Use este endpoint para construir screeners, exploradores
        de ações ou para descobrir novos ativos.

        ### Funcionalidades:

        - **Busca por Nome ou Ticker:** Encontre ativos digitando "Petrobras", "PETR4"
          ou qualquer termo.
        - **Filtros por Tipo:** Ações (stock), Fundos Imobiliários (fund), BDRs (bdr).
        - **Filtros por Subtipo:** Units, FIIs, ETFs, FI-Infra, FI-Agro, FIPs, FIDCs e
          BDRs via `subType`.
        - **Filtros por Setor:** Energia, Financeiro, Tecnologia, Saúde, etc.
        - **Ordenação Flexível:** Ordene por volume, preço, market cap ou nome.
        - **Paginação:** Controle o número de resultados com `limit` e `page`.

        ### Autenticação:

        Requer token Bearer. Obtenha seu token em
        [brapi.dev/dashboard](https://brapi.dev/dashboard).

        ### Exemplos de Requisição:

        ```bash
        # Listar todos os ativos (primeiros 100)
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/quote/list"

        # Buscar por nome ou ticker
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/quote/list?search=petrobras"

        # Filtrar por tipo e ordenar por volume
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/quote/list?type=stock&sortBy=volume&sortOrder=desc&limit=10"

        # Filtrar por subtipo
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/quote/list?subType=fi-agro&limit=10"

        # Listar apenas FIIs de um setor específico
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/quote/list?type=fund&sector=Logística&limit=20"
        ```

        ### Parâmetros de Ordenação:

        - `volume` — Volume de negociação do dia
        - `close` — Preço de fechamento
        - `market_cap_basic` — Capitalização de mercado
        - `name` — Nome da empresa (alfabético)

        ### Tipos de Ativo:

        - `stock` — Ações (Ações ordinárias e preferenciais)
        - `fund` — Fundos Imobiliários (FIIs) e ETFs
        - `bdr` — BDRs (Brazilian Depositary Receipts)

        **Plano Mínimo:** Gratuito **Autenticação:** Necessária (Bearer Token)

        Args:
          token: Token de autenticação (alternativa ao header Authorization)

          limit: Número máximo de resultados

          page: Número da página (paginação)

          search: Termo de busca para filtrar ativos

          sector: Filtrar por setor

          sort_by: Campo para ordenação

          sort_order: Ordem de classificação

          subsector: Filtrar pelo subsetor B3

          sub_type: Filtrar por classificação aditiva: stock, unit, fii, etf, fi-infra, fi-agro,
              fip, fidc ou bdr

          type: Filtrar por tipo de ativo

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
                        "subsector": subsector,
                        "sub_type": sub_type,
                        "type": type,
                    },
                    quote_list_params.QuoteListParams,
                ),
            ),
            cast_to=QuoteListResponse,
        )


class AsyncQuoteResource(AsyncAPIResource):
    """Consulte informações detalhadas sobre ações, BDRs, ETFs e índices brasileiros.

    Obtenha preços em tempo real, dados fundamentalistas, históricos e dividendos.
    """

    @cached_property
    def with_raw_response(self) -> AsyncQuoteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQuoteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQuoteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncQuoteResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        tickers: str,
        *,
        token: str | Omit = omit,
        dividends: Literal["true", "false"] | Omit = omit,
        end_date: str | Omit = omit,
        interval: Literal["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
        | Omit = omit,
        modules: str | Omit = omit,
        range: Literal["1d", "2d", "5d", "7d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]
        | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QuoteRetrieveResponse:
        """
        **O ENDPOINT MAIS IMPORTANTE DA API.** Obtém dados detalhados e abrangentes de
        um ou múltiplos ativos (ações, FIIs, BDRs) em uma única requisição. Combine
        cotações em tempo real, dados históricos, fundamentos e dividendos conforme
        necessário.

        ### Funcionalidades:

        - **Cotação em Tempo Real:** Preço atual, variação absoluta e percentual,
          volume, máxima/mínima do dia, range de 52 semanas.
        - **Dados Históricos:** Preços OHLCV (Open, High, Low, Close, Volume) com
          intervalos flexíveis (1d, 5d, 1wk, 1mo, 3mo) e períodos (1d até max).
        - **Fundamentos:** Balanço Patrimonial, DRE, Fluxo de Caixa, DVA,
          Indicadores-chave (P/L, P/VP, ROE, etc) via parâmetro `modules`.
        - **Dividendos:** Histórico completo de proventos em dinheiro (dividendos, JCP)
          e bonificações.

        ### Autenticação:

        Requer token Bearer no header ou como query param. Tickers de teste **PETR4** e
        **VALE3** funcionam sem autenticação.

        ```bash
        # Via header (recomendado)
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/quote/PETR4"

        # Via query param
        curl "https://brapi.dev/api/quote/PETR4?token=SEU_TOKEN"
        ```

        ### Exemplos de Requisição:

        ```bash
        # Simples: apenas cotação atual
        curl "https://brapi.dev/api/quote/PETR4?token=SEU_TOKEN"

        # Múltiplos tickers em uma requisição
        curl "https://brapi.dev/api/quote/PETR4,VALE3,ITUB4?token=SEU_TOKEN"

        # Com dados históricos (últimos 12 meses, diário)
        curl "https://brapi.dev/api/quote/PETR4?range=1y&interval=1d&token=SEU_TOKEN"

        # Com módulos de fundamentos (balanço e DRE)
        curl "https://brapi.dev/api/quote/PETR4?modules=balanceSheetHistory,incomeStatementHistory&token=SEU_TOKEN"

        # Completo: histórico + dividendos + estatísticas-chave
        curl "https://brapi.dev/api/quote/PETR4?range=6mo&interval=1d&dividends=true&modules=balanceSheetHistory,defaultKeyStatistics&token=SEU_TOKEN"
        ```

        ### Módulos Disponíveis:

        - `summaryProfile` — Perfil da empresa (CNPJ, setor, descrição, website,
          funcionários)
        - `balanceSheetHistory` — Balanço Patrimonial anual
        - `balanceSheetHistoryQuarterly` — Balanço Patrimonial trimestral
        - `incomeStatementHistory` — DRE anual (Demonstração de Resultado do Exercício)
        - `incomeStatementHistoryQuarterly` — DRE trimestral
        - `financialData` — Indicadores financeiros atuais (TTM - Trailing Twelve
          Months)
        - `financialDataHistory` — Histórico anual de indicadores financeiros
        - `financialDataHistoryQuarterly` — Histórico trimestral de indicadores
          financeiros
        - `defaultKeyStatistics` — Estatísticas-chave (P/L, P/VP, ROE, Dividend Yield,
          etc)
        - `defaultKeyStatisticsHistory` — Histórico anual de estatísticas-chave
        - `defaultKeyStatisticsHistoryQuarterly` — Histórico trimestral de
          estatísticas-chave
        - `cashflowHistory` — Fluxo de Caixa anual
        - `cashflowHistoryQuarterly` — Fluxo de Caixa trimestral
        - `valueAddedHistory` — DVA anual (Demonstração de Valor Adicionado)
        - `valueAddedHistoryQuarterly` — DVA trimestral

        ### Intervalos Válidos (histórico):

        - `1d` — Diário
        - `5d` — 5 dias
        - `1wk` — Semanal
        - `1mo` — Mensal
        - `3mo` — Trimestral

        ### Períodos Válidos (range):

        - `1d` — Último dia
        - `5d` — Últimos 5 dias
        - `1mo` — Último mês
        - `3mo` — Últimos 3 meses
        - `6mo` — Últimos 6 meses
        - `1y` — Último ano
        - `2y` — Últimos 2 anos
        - `5y` — Últimos 5 anos
        - `10y` — Últimos 10 anos
        - `ytd` — Ano até hoje
        - `max` — Máximo disponível

        ### Campos Principais da Resposta:

        - `symbol` — Ticker do ativo (ex: PETR4)
        - `shortName` — Nome curto da empresa
        - `currency` — Moeda (BRL)
        - `regularMarketPrice` — Preço atual em BRL
        - `regularMarketChange` — Variação absoluta
        - `regularMarketChangePercent` — Variação percentual (%)
        - `regularMarketVolume` — Volume de negociação do dia
        - `regularMarketDayHigh` — Máxima do dia
        - `regularMarketDayLow` — Mínima do dia
        - `fiftyTwoWeekHigh` — Máxima de 52 semanas
        - `fiftyTwoWeekLow` — Mínima de 52 semanas
        - `marketCap` — Capitalização de mercado
        - `historicalDataPrice` — Array de dados OHLCV (quando `range`/`interval`
          fornecidos)
        - `dividendsData` — Histórico de dividendos (quando `dividends=true`)

        ### Tickers Populares (Teste):

        - `PETR4` — Petrobras (Energia)
        - `VALE3` — Vale (Mineração)
        - `ITUB4` — Itaú Unibanco (Financeiro)
        - `BBDC4` — Bradesco (Financeiro)
        - `ABEV3` — Ambev (Consumo)
        - `WEGE3` — WEG (Indústria)
        - `RENT3` — Localiza (Transporte)
        - `BBAS3` — Banco do Brasil (Financeiro)
        - `MGLU3` — Magazine Luiza (Varejo)

        ### Fonte dos Dados:

        CVM (Comissão de Valores Mobiliários)

        **Plano Mínimo:** Gratuito (limitado a 1 ticker/requisição e módulos básicos)
        **Autenticação:** Necessária para produção (tickers de teste PETR4 e VALE3
        funcionam sem token)

        Args:
          tickers: Ticker(s) de ativos separados por vírgula (ex: PETR4 ou PETR4,VALE3,ITUB4)

          token: Token de autenticação (alternativa ao header Authorization)

          dividends: Incluir histórico de dividendos e JCP

          end_date: Data final para dados históricos (formato YYYY-MM-DD)

          interval: Intervalo/granularidade dos dados históricos

          modules: Módulos de dados adicionais separados por vírgula

          range: Período para dados históricos de preço

          start_date: Data inicial para dados históricos (formato YYYY-MM-DD)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tickers:
            raise ValueError(f"Expected a non-empty value for `tickers` but received {tickers!r}")
        return await self._get(
            path_template("/api/quote/{tickers}", tickers=tickers),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "token": token,
                        "dividends": dividends,
                        "end_date": end_date,
                        "interval": interval,
                        "modules": modules,
                        "range": range,
                        "start_date": start_date,
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
        limit: str | Omit = omit,
        page: str | Omit = omit,
        search: str | Omit = omit,
        sector: str | Omit = omit,
        sort_by: Literal["name", "close", "change", "change_abs", "volume", "market_cap_basic"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        subsector: str | Omit = omit,
        sub_type: Literal["stock", "unit", "fii", "etf", "fi-infra", "fi-agro", "fip", "fidc", "bdr"] | Omit = omit,
        type: Literal["stock", "fund", "bdr"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QuoteListResponse:
        """
        Retorna uma lista paginada de todos os ativos disponíveis na API (Ações, FIIs,
        BDRs, ETFs, Índices). Use este endpoint para construir screeners, exploradores
        de ações ou para descobrir novos ativos.

        ### Funcionalidades:

        - **Busca por Nome ou Ticker:** Encontre ativos digitando "Petrobras", "PETR4"
          ou qualquer termo.
        - **Filtros por Tipo:** Ações (stock), Fundos Imobiliários (fund), BDRs (bdr).
        - **Filtros por Subtipo:** Units, FIIs, ETFs, FI-Infra, FI-Agro, FIPs, FIDCs e
          BDRs via `subType`.
        - **Filtros por Setor:** Energia, Financeiro, Tecnologia, Saúde, etc.
        - **Ordenação Flexível:** Ordene por volume, preço, market cap ou nome.
        - **Paginação:** Controle o número de resultados com `limit` e `page`.

        ### Autenticação:

        Requer token Bearer. Obtenha seu token em
        [brapi.dev/dashboard](https://brapi.dev/dashboard).

        ### Exemplos de Requisição:

        ```bash
        # Listar todos os ativos (primeiros 100)
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/quote/list"

        # Buscar por nome ou ticker
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/quote/list?search=petrobras"

        # Filtrar por tipo e ordenar por volume
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/quote/list?type=stock&sortBy=volume&sortOrder=desc&limit=10"

        # Filtrar por subtipo
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/quote/list?subType=fi-agro&limit=10"

        # Listar apenas FIIs de um setor específico
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/quote/list?type=fund&sector=Logística&limit=20"
        ```

        ### Parâmetros de Ordenação:

        - `volume` — Volume de negociação do dia
        - `close` — Preço de fechamento
        - `market_cap_basic` — Capitalização de mercado
        - `name` — Nome da empresa (alfabético)

        ### Tipos de Ativo:

        - `stock` — Ações (Ações ordinárias e preferenciais)
        - `fund` — Fundos Imobiliários (FIIs) e ETFs
        - `bdr` — BDRs (Brazilian Depositary Receipts)

        **Plano Mínimo:** Gratuito **Autenticação:** Necessária (Bearer Token)

        Args:
          token: Token de autenticação (alternativa ao header Authorization)

          limit: Número máximo de resultados

          page: Número da página (paginação)

          search: Termo de busca para filtrar ativos

          sector: Filtrar por setor

          sort_by: Campo para ordenação

          sort_order: Ordem de classificação

          subsector: Filtrar pelo subsetor B3

          sub_type: Filtrar por classificação aditiva: stock, unit, fii, etf, fi-infra, fi-agro,
              fip, fidc ou bdr

          type: Filtrar por tipo de ativo

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
                        "subsector": subsector,
                        "sub_type": sub_type,
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
