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
        """Cotação de um ou mais ativos brasileiros.

        A mesma resposta pode trazer histórico
        de preços, proventos e dados das demonstrações financeiras.

        Use para integrações que já usam este formato. Para integrações novas, use os
        endpoints `/api/v2/stocks/*`, que trazem um tipo de dado por chamada. Veja o
        [guia de migração](https://brapi.dev/docs/acoes/migracao-v2).

        Este é o endpoint original da brapi. Ele continua ativo e não tem data de
        remoção.

        A resposta sempre traz a cotação: preço, variação, volume, máxima e mínima do
        dia, faixa de 52 semanas e `marketCap`. Estes parâmetros adicionam outros dados:

        - `range` e `interval`, ou `startDate` e `endDate`: `historicalDataPrice`, a
          série de preços.
        - `includeRaw=true`: os preços originais sem ajuste `rawOpen`, `rawHigh`,
          `rawLow` e `rawClose`, só em intervalos diários. Exige o plano Pro.
        - `dividends=true`: `dividendsData`, com dividendos, JCP e eventos em ações.
        - `modules`: um objeto para cada módulo pedido.

        Módulos aceitos em `modules`, separados por vírgula:

        - `summaryProfile`: cadastro da empresa.
        - `defaultKeyStatistics`: múltiplos dos últimos 12 meses, como P/L, P/VP e
          dividend yield.
        - `financialData`: receita, EBITDA, margens e dívida dos últimos 12 meses.
        - `balanceSheetHistory`: balanço patrimonial anual.
        - `incomeStatementHistory`: DRE anual.
        - `cashflowHistory`: fluxo de caixa anual.
        - `valueAddedHistory`: DVA anual.

        Cada módulo de demonstração tem uma versão trimestral com o sufixo `Quarterly`,
        como `balanceSheetHistoryQuarterly`. `defaultKeyStatistics` e `financialData`
        também aceitam os sufixos `History` e `HistoryQuarterly`. Os dados trimestrais
        seguem as mesmas regras dos endpoints v2 de
        [DRE](https://brapi.dev/docs/acoes/dre),
        [fluxo de caixa](https://brapi.dev/docs/acoes/fluxo-de-caixa) e
        [DVA](https://brapi.dev/docs/acoes/valor-adicionado).

        O plano define os valores aceitos em `range`, `interval` e `modules`. Um valor
        fora do plano retorna erro.

        PETR4, MGLU3, VALE3 e ITUB4 respondem sem token. Se a chamada juntar um deles
        com outro ticker, ela exige token.

        Args:
          tickers: Tickers separados por vírgula. Ex.: PETR4,VALE3.

          token: Token de acesso. Use no lugar do header `Authorization`.

          dividends: Inclui `dividendsData` com dividendos, JCP e eventos em ações.

          end_date: Data final da série de preços no formato YYYY-MM-DD.

          include_raw: Inclui os preços originais sem ajuste (`rawOpen`, `rawHigh`, `rawLow`,
              `rawClose`) em intervalos diários. Exige o plano Pro.

          interval: Intervalo entre os pontos da série de preços.

          modules: Módulos extras separados por vírgula.

          range: Janela relativa da série de preços.

          start_date: Data inicial da série de preços no formato YYYY-MM-DD.

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
        """
        Lista de ações, FIIs, BDRs e ETFs com preço de fechamento, variação, volume,
        market cap, setor e logo de cada um. A resposta também traz os índices
        disponíveis.

        Use para screeners, tabelas de mercado e busca de ativos com cotação.

        `search` busca por parte do ticker ou do nome da empresa. Filtre por `type`,
        `subType`, `sector` e `subsector`. A ordem padrão é por volume, decrescente.

        Sem `limit`, a resposta traz até 2.000 ativos e não traz os campos de paginação.
        Com `limit`, ela traz `currentPage`, `totalPages`, `itemsPerPage`, `totalCount`
        e `hasNextPage`.

        `availableSectors`, `availableSubsectors`, `availableStockTypes` e
        `availableSubTypeTypes` listam os valores aceitos nos filtros.

        Este endpoint não exige token. Para buscar e validar tickers, a
        [lista de tickers](https://brapi.dev/docs/tickers) traz uma resposta menor.

        Args:
          token: Token de acesso. Use no lugar do header `Authorization`.

          limit: Itens por página. Máximo: 2000. Sem este parâmetro, a resposta traz até 2000
              itens e não traz paginação.

          page: Número da página. Começa em 1.

          search: Parte do ticker ou do nome da empresa.

          sector: Setor.

          sort_by: Campo de ordenação. Padrão: volume.

          sort_order: Ordem. Padrão: desc.

          subsector: Subsetor.

          sub_type: Subtipo do ativo: stock, unit, fii, etf, fi-infra, fi-agro, fip, fidc ou bdr.

          type: Tipo do ativo.

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
        """Cotação de um ou mais ativos brasileiros.

        A mesma resposta pode trazer histórico
        de preços, proventos e dados das demonstrações financeiras.

        Use para integrações que já usam este formato. Para integrações novas, use os
        endpoints `/api/v2/stocks/*`, que trazem um tipo de dado por chamada. Veja o
        [guia de migração](https://brapi.dev/docs/acoes/migracao-v2).

        Este é o endpoint original da brapi. Ele continua ativo e não tem data de
        remoção.

        A resposta sempre traz a cotação: preço, variação, volume, máxima e mínima do
        dia, faixa de 52 semanas e `marketCap`. Estes parâmetros adicionam outros dados:

        - `range` e `interval`, ou `startDate` e `endDate`: `historicalDataPrice`, a
          série de preços.
        - `includeRaw=true`: os preços originais sem ajuste `rawOpen`, `rawHigh`,
          `rawLow` e `rawClose`, só em intervalos diários. Exige o plano Pro.
        - `dividends=true`: `dividendsData`, com dividendos, JCP e eventos em ações.
        - `modules`: um objeto para cada módulo pedido.

        Módulos aceitos em `modules`, separados por vírgula:

        - `summaryProfile`: cadastro da empresa.
        - `defaultKeyStatistics`: múltiplos dos últimos 12 meses, como P/L, P/VP e
          dividend yield.
        - `financialData`: receita, EBITDA, margens e dívida dos últimos 12 meses.
        - `balanceSheetHistory`: balanço patrimonial anual.
        - `incomeStatementHistory`: DRE anual.
        - `cashflowHistory`: fluxo de caixa anual.
        - `valueAddedHistory`: DVA anual.

        Cada módulo de demonstração tem uma versão trimestral com o sufixo `Quarterly`,
        como `balanceSheetHistoryQuarterly`. `defaultKeyStatistics` e `financialData`
        também aceitam os sufixos `History` e `HistoryQuarterly`. Os dados trimestrais
        seguem as mesmas regras dos endpoints v2 de
        [DRE](https://brapi.dev/docs/acoes/dre),
        [fluxo de caixa](https://brapi.dev/docs/acoes/fluxo-de-caixa) e
        [DVA](https://brapi.dev/docs/acoes/valor-adicionado).

        O plano define os valores aceitos em `range`, `interval` e `modules`. Um valor
        fora do plano retorna erro.

        PETR4, MGLU3, VALE3 e ITUB4 respondem sem token. Se a chamada juntar um deles
        com outro ticker, ela exige token.

        Args:
          tickers: Tickers separados por vírgula. Ex.: PETR4,VALE3.

          token: Token de acesso. Use no lugar do header `Authorization`.

          dividends: Inclui `dividendsData` com dividendos, JCP e eventos em ações.

          end_date: Data final da série de preços no formato YYYY-MM-DD.

          include_raw: Inclui os preços originais sem ajuste (`rawOpen`, `rawHigh`, `rawLow`,
              `rawClose`) em intervalos diários. Exige o plano Pro.

          interval: Intervalo entre os pontos da série de preços.

          modules: Módulos extras separados por vírgula.

          range: Janela relativa da série de preços.

          start_date: Data inicial da série de preços no formato YYYY-MM-DD.

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
        """
        Lista de ações, FIIs, BDRs e ETFs com preço de fechamento, variação, volume,
        market cap, setor e logo de cada um. A resposta também traz os índices
        disponíveis.

        Use para screeners, tabelas de mercado e busca de ativos com cotação.

        `search` busca por parte do ticker ou do nome da empresa. Filtre por `type`,
        `subType`, `sector` e `subsector`. A ordem padrão é por volume, decrescente.

        Sem `limit`, a resposta traz até 2.000 ativos e não traz os campos de paginação.
        Com `limit`, ela traz `currentPage`, `totalPages`, `itemsPerPage`, `totalCount`
        e `hasNextPage`.

        `availableSectors`, `availableSubsectors`, `availableStockTypes` e
        `availableSubTypeTypes` listam os valores aceitos nos filtros.

        Este endpoint não exige token. Para buscar e validar tickers, a
        [lista de tickers](https://brapi.dev/docs/tickers) traz uma resposta menor.

        Args:
          token: Token de acesso. Use no lugar do header `Authorization`.

          limit: Itens por página. Máximo: 2000. Sem este parâmetro, a resposta traz até 2000
              itens e não traz paginação.

          page: Número da página. Começa em 1.

          search: Parte do ticker ou do nome da empresa.

          sector: Setor.

          sort_by: Campo de ordenação. Padrão: volume.

          sort_order: Ordem. Padrão: desc.

          subsector: Subsetor.

          sub_type: Subtipo do ativo: stock, unit, fii, etf, fi-infra, fi-agro, fip, fidc ou bdr.

          type: Tipo do ativo.

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
