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
        include_raw: Literal["true", "false"] | Omit = omit,
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
        Devolve cotação, histórico, dividendos e fundamentos de um ou mais ativos em uma
        única resposta. É o endpoint original da brapi e continua funcionando sem data
        de remoção.

        Para integrações novas, prefira `/api/v2/stocks/*`. Lá cada chamada traz um tipo
        de dado e a resposta chega menor. Veja o guia em
        [brapi.dev/docs/acoes/migracao-v2](https://brapi.dev/docs/acoes/migracao-v2).

        ### O que a resposta traz

        Sempre: `symbol`, `shortName`, `currency`, `regularMarketPrice`,
        `regularMarketChange`, `regularMarketChangePercent`, `regularMarketVolume`,
        `regularMarketDayHigh`, `regularMarketDayLow`, `fiftyTwoWeekHigh`,
        `fiftyTwoWeekLow` e `marketCap`.

        Com `range` e `interval`: `historicalDataPrice` com a série OHLCV. Com
        `includeRaw=true` e intervalo diário: os campos `rawOpen`, `rawHigh`, `rawLow` e
        `rawClose` quando existirem no banco. Intervalos intradiários não retornam
        campos `raw*`. Com `dividends=true`: `dividendsData` com dividendos, JCP e
        bonificações. Com `modules`: um objeto por módulo pedido.

        ### Parâmetros de histórico

        `interval` aceita `1d`, `5d`, `1wk`, `1mo` e `3mo`. `range` aceita `1d`, `5d`,
        `1mo`, `3mo`, `6mo`, `1y`, `2y`, `5y`, `10y`, `ytd` e `max`. O quanto de
        histórico você enxerga depende do plano.

        ### Módulos

        `modules` aceita uma lista separada por vírgula:

        - `summaryProfile` - cadastro da empresa: CNPJ, setor, descrição, site,
          funcionários
        - `defaultKeyStatistics` - múltiplos nos últimos 12 meses: P/L, P/VP, ROE,
          dividend yield
        - `financialData` - receita, EBITDA, margens e dívida nos últimos 12 meses
        - `balanceSheetHistory` - balanço patrimonial anual
        - `incomeStatementHistory` - DRE anual
        - `cashflowHistory` - fluxo de caixa anual
        - `valueAddedHistory` - DVA anual

        Cada módulo de histórico tem a versão trimestral com o sufixo `Quarterly`. Os
        módulos `defaultKeyStatistics` e `financialData` também aceitam os sufixos
        `History` e `HistoryQuarterly`.

        ```bash
        curl -H "Authorization: Bearer SEU_TOKEN" \\
          "https://brapi.dev/api/quote/PETR4?range=6mo&interval=1d&dividends=true&modules=defaultKeyStatistics"
        ```

        ### Autenticação

        PETR4, MGLU3, VALE3 e ITUB4 respondem sem token, com todos os recursos. Se você
        misturar um desses com outro ticker na mesma requisição, a chamada inteira passa
        a exigir token. Envie o token no header `Authorization` sempre que a sua
        ferramenta permitir.

        Os fundamentos vêm dos documentos que as companhias entregam à CVM.

        Args:
          tickers: Ticker(s) de ativos separados por vírgula (ex: PETR4 ou PETR4,VALE3,ITUB4)

          token: Token de autenticação (alternativa ao header Authorization)

          dividends: Incluir histórico de dividendos e JCP

          end_date: Data final para dados históricos (formato YYYY-MM-DD)

          include_raw: Incluir preços OHLC originais armazenados no banco da brapi para intervalos
              diários. Use includeRaw=true. Disponível no plano Pro.

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
                        "include_raw": include_raw,
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
        """Lista paginada de ativos da B3 com a cotação de cada um.

        Serve para montar
        screener, tabela de mercado ou autocomplete de busca.

        Busque por nome ou ticker com `search`, aceitando tanto "Petrobras" quanto
        "PETR4". Filtre por `type` (`stock`, `fund`, `bdr`), por `subType` (units, FIIs,
        ETFs, FI-Infra, FI-Agro, FIPs, FIDCs, BDRs) e por `sector`.

        Ordene com `sortBy` usando `volume`, `close`, `market_cap_basic` ou `name`, mais
        `sortOrder`. Pagine com `page` e `limit`. O padrão devolve os primeiros 100
        ativos.

        A resposta também traz `availableSectors` e `availableStockTypes`, então você
        monta os filtros da sua interface sem manter uma lista fixa no código.

        ```bash
        curl -H "Authorization: Bearer SEU_TOKEN" \\
          "https://brapi.dev/api/quote/list?type=stock&sortBy=volume&sortOrder=desc&limit=10"
        ```

        Exige token, disponível em qualquer plano. Para buscar e validar símbolos sem
        carregar cotação, `/api/v2/tickers` é mais leve.

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
        include_raw: Literal["true", "false"] | Omit = omit,
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
        Devolve cotação, histórico, dividendos e fundamentos de um ou mais ativos em uma
        única resposta. É o endpoint original da brapi e continua funcionando sem data
        de remoção.

        Para integrações novas, prefira `/api/v2/stocks/*`. Lá cada chamada traz um tipo
        de dado e a resposta chega menor. Veja o guia em
        [brapi.dev/docs/acoes/migracao-v2](https://brapi.dev/docs/acoes/migracao-v2).

        ### O que a resposta traz

        Sempre: `symbol`, `shortName`, `currency`, `regularMarketPrice`,
        `regularMarketChange`, `regularMarketChangePercent`, `regularMarketVolume`,
        `regularMarketDayHigh`, `regularMarketDayLow`, `fiftyTwoWeekHigh`,
        `fiftyTwoWeekLow` e `marketCap`.

        Com `range` e `interval`: `historicalDataPrice` com a série OHLCV. Com
        `includeRaw=true` e intervalo diário: os campos `rawOpen`, `rawHigh`, `rawLow` e
        `rawClose` quando existirem no banco. Intervalos intradiários não retornam
        campos `raw*`. Com `dividends=true`: `dividendsData` com dividendos, JCP e
        bonificações. Com `modules`: um objeto por módulo pedido.

        ### Parâmetros de histórico

        `interval` aceita `1d`, `5d`, `1wk`, `1mo` e `3mo`. `range` aceita `1d`, `5d`,
        `1mo`, `3mo`, `6mo`, `1y`, `2y`, `5y`, `10y`, `ytd` e `max`. O quanto de
        histórico você enxerga depende do plano.

        ### Módulos

        `modules` aceita uma lista separada por vírgula:

        - `summaryProfile` - cadastro da empresa: CNPJ, setor, descrição, site,
          funcionários
        - `defaultKeyStatistics` - múltiplos nos últimos 12 meses: P/L, P/VP, ROE,
          dividend yield
        - `financialData` - receita, EBITDA, margens e dívida nos últimos 12 meses
        - `balanceSheetHistory` - balanço patrimonial anual
        - `incomeStatementHistory` - DRE anual
        - `cashflowHistory` - fluxo de caixa anual
        - `valueAddedHistory` - DVA anual

        Cada módulo de histórico tem a versão trimestral com o sufixo `Quarterly`. Os
        módulos `defaultKeyStatistics` e `financialData` também aceitam os sufixos
        `History` e `HistoryQuarterly`.

        ```bash
        curl -H "Authorization: Bearer SEU_TOKEN" \\
          "https://brapi.dev/api/quote/PETR4?range=6mo&interval=1d&dividends=true&modules=defaultKeyStatistics"
        ```

        ### Autenticação

        PETR4, MGLU3, VALE3 e ITUB4 respondem sem token, com todos os recursos. Se você
        misturar um desses com outro ticker na mesma requisição, a chamada inteira passa
        a exigir token. Envie o token no header `Authorization` sempre que a sua
        ferramenta permitir.

        Os fundamentos vêm dos documentos que as companhias entregam à CVM.

        Args:
          tickers: Ticker(s) de ativos separados por vírgula (ex: PETR4 ou PETR4,VALE3,ITUB4)

          token: Token de autenticação (alternativa ao header Authorization)

          dividends: Incluir histórico de dividendos e JCP

          end_date: Data final para dados históricos (formato YYYY-MM-DD)

          include_raw: Incluir preços OHLC originais armazenados no banco da brapi para intervalos
              diários. Use includeRaw=true. Disponível no plano Pro.

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
                        "include_raw": include_raw,
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
        """Lista paginada de ativos da B3 com a cotação de cada um.

        Serve para montar
        screener, tabela de mercado ou autocomplete de busca.

        Busque por nome ou ticker com `search`, aceitando tanto "Petrobras" quanto
        "PETR4". Filtre por `type` (`stock`, `fund`, `bdr`), por `subType` (units, FIIs,
        ETFs, FI-Infra, FI-Agro, FIPs, FIDCs, BDRs) e por `sector`.

        Ordene com `sortBy` usando `volume`, `close`, `market_cap_basic` ou `name`, mais
        `sortOrder`. Pagine com `page` e `limit`. O padrão devolve os primeiros 100
        ativos.

        A resposta também traz `availableSectors` e `availableStockTypes`, então você
        monta os filtros da sua interface sem manter uma lista fixa no código.

        ```bash
        curl -H "Authorization: Bearer SEU_TOKEN" \\
          "https://brapi.dev/api/quote/list?type=stock&sortBy=volume&sortOrder=desc&limit=10"
        ```

        Exige token, disponível em qualquer plano. Para buscar e validar símbolos sem
        carregar cotação, `/api/v2/tickers` é mais leve.

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
