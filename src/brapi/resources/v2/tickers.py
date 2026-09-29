# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v2 import ticker_list_params, ticker_renames_params, ticker_resolve_params, ticker_coverage_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v2.ticker_list_response import TickerListResponse
from ...types.v2.ticker_renames_response import TickerRenamesResponse
from ...types.v2.ticker_resolve_response import TickerResolveResponse
from ...types.v2.ticker_coverage_response import TickerCoverageResponse

__all__ = ["TickersResource", "AsyncTickersResource"]


class TickersResource(SyncAPIResource):
    """Descubra, filtre e valide tickers B3 disponíveis na brapi.

    Use como camada de identidade antes dos endpoints de dados de mercado.
    """

    @cached_property
    def with_raw_response(self) -> TickersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return TickersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TickersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return TickersResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        search: str | Omit = omit,
        sector: str | Omit = omit,
        sort_by: Literal["symbol", "name", "close", "change", "volume", "marketCap"] | Omit = omit,
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
    ) -> TickerListResponse:
        """
        Lista de tickers brasileiros com nome, tipo, setor, logo e um resumo da cotação:
        ações, FIIs, ETFs, BDRs e units. Os índices vêm em `indexes`.

        Use para busca, autocomplete, validação de tickers e screeners.

        `search` busca por parte do ticker, do nome da empresa ou de um ticker antigo. O
        filtro `type` aceita `stock`, `fund` e `bdr`. `facets` lista os valores aceitos
        nos filtros.

        A lista não tem opções, futuros, Tesouro Direto, criptomoedas, câmbio nem
        indicadores econômicos. Esses dados têm endpoints próprios.

        Não exige token. Para cotação completa, use a
        [cotação de ações](https://brapi.dev/docs/acoes/cotacao).

        Args:
          limit: Itens por página. Máximo: 2000.

          page: Número da página. Começa em 1.

          search: Parte do ticker, do nome da empresa ou de um ticker antigo.

          sector: Setor.

          sort_by: Campo de ordenação.

          sort_order: Ordem.

          subsector: Subsetor.

          sub_type: Subtipo do ativo: stock, unit, fii, etf, fi-infra, fi-agro, fip, fidc ou bdr.

          type: Tipo do ativo. Índices não entram neste filtro.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/tickers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
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
                    ticker_list_params.TickerListParams,
                ),
            ),
            cast_to=TickerListResponse,
        )

    def coverage(
        self,
        *,
        symbols: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TickerCoverageResponse:
        """
        Mostra quais dados a brapi tem para cada ticker e quais endpoints usar em
        seguida: cotação, histórico, dividendos, fundamentos ou dados de FII.

        Use antes de montar uma integração, para saber quais endpoints servem para cada
        ativo.

        Envie até 20 tickers em `symbols`. Um ticker antigo é trocado pelo atual e vem
        com `status` igual a `renamed`. Um ticker desconhecido não gera erro. Ele vem
        com `status` igual a `unknown` e links de busca. Um ticker de opção vem com
        `wrong_endpoint` e links para os endpoints de opções.

        Este endpoint não traz dados de mercado. Não exige token.

        Args:
          symbols: Tickers separados por vírgula, até 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/tickers/coverage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"symbols": symbols}, ticker_coverage_params.TickerCoverageParams),
            ),
            cast_to=TickerCoverageResponse,
        )

    def renames(
        self,
        *,
        end_date: str | Omit = omit,
        search: str | Omit = omit,
        start_date: str | Omit = omit,
        symbols: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TickerRenamesResponse:
        """
        Mudanças de ticker, com o ticker antigo, o novo, o atual e a data efetiva.

        Use para explicar por que um ticker antigo leva a outro e para corrigir séries
        salvas com o ticker antigo.

        Se um ativo mudou de ticker mais de uma vez, `canonicalSymbol` traz o último.
        `startDate` e `endDate` filtram pela data efetiva. A lista vem da data mais
        recente para a mais antiga.

        Não exige token. Para trocar uma lista de tickers pelos atuais, use
        [resolver ticker antigo](https://brapi.dev/docs/tickers/resolver).

        Args:
          end_date: Data efetiva final no formato YYYY-MM-DD.

          search: Parte do ticker antigo, do novo ou do atual.

          start_date: Data efetiva inicial no formato YYYY-MM-DD.

          symbols: Tickers separados por vírgula, até 20. Traz renomes em que algum deles é o
              ticker antigo, o novo ou o atual.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/tickers/renames",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "search": search,
                        "start_date": start_date,
                        "symbols": symbols,
                    },
                    ticker_renames_params.TickerRenamesParams,
                ),
            ),
            cast_to=TickerRenamesResponse,
        )

    def resolve(
        self,
        *,
        symbols: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TickerResolveResponse:
        """Troca tickers antigos pelo ticker atual.

        Um ticker sem renome conhecido volta
        igual.

        Use antes de consultar dados de mercado quando os tickers vêm de usuários,
        planilhas antigas ou carteiras importadas.

        Envie até 20 tickers em `symbols`. A resposta segue a ordem enviada, sem
        repetidos. `status` é `renamed` quando o ticker mudou e `active` quando não há
        renome conhecido.

        Este endpoint não confirma se o ticker existe. Para isso, use a
        [cobertura por ticker](https://brapi.dev/docs/tickers/cobertura).

        Não exige token.

        Args:
          symbols: Tickers separados por vírgula, até 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/tickers/resolve",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"symbols": symbols}, ticker_resolve_params.TickerResolveParams),
            ),
            cast_to=TickerResolveResponse,
        )


class AsyncTickersResource(AsyncAPIResource):
    """Descubra, filtre e valide tickers B3 disponíveis na brapi.

    Use como camada de identidade antes dos endpoints de dados de mercado.
    """

    @cached_property
    def with_raw_response(self) -> AsyncTickersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTickersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTickersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncTickersResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        search: str | Omit = omit,
        sector: str | Omit = omit,
        sort_by: Literal["symbol", "name", "close", "change", "volume", "marketCap"] | Omit = omit,
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
    ) -> TickerListResponse:
        """
        Lista de tickers brasileiros com nome, tipo, setor, logo e um resumo da cotação:
        ações, FIIs, ETFs, BDRs e units. Os índices vêm em `indexes`.

        Use para busca, autocomplete, validação de tickers e screeners.

        `search` busca por parte do ticker, do nome da empresa ou de um ticker antigo. O
        filtro `type` aceita `stock`, `fund` e `bdr`. `facets` lista os valores aceitos
        nos filtros.

        A lista não tem opções, futuros, Tesouro Direto, criptomoedas, câmbio nem
        indicadores econômicos. Esses dados têm endpoints próprios.

        Não exige token. Para cotação completa, use a
        [cotação de ações](https://brapi.dev/docs/acoes/cotacao).

        Args:
          limit: Itens por página. Máximo: 2000.

          page: Número da página. Começa em 1.

          search: Parte do ticker, do nome da empresa ou de um ticker antigo.

          sector: Setor.

          sort_by: Campo de ordenação.

          sort_order: Ordem.

          subsector: Subsetor.

          sub_type: Subtipo do ativo: stock, unit, fii, etf, fi-infra, fi-agro, fip, fidc ou bdr.

          type: Tipo do ativo. Índices não entram neste filtro.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/tickers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
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
                    ticker_list_params.TickerListParams,
                ),
            ),
            cast_to=TickerListResponse,
        )

    async def coverage(
        self,
        *,
        symbols: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TickerCoverageResponse:
        """
        Mostra quais dados a brapi tem para cada ticker e quais endpoints usar em
        seguida: cotação, histórico, dividendos, fundamentos ou dados de FII.

        Use antes de montar uma integração, para saber quais endpoints servem para cada
        ativo.

        Envie até 20 tickers em `symbols`. Um ticker antigo é trocado pelo atual e vem
        com `status` igual a `renamed`. Um ticker desconhecido não gera erro. Ele vem
        com `status` igual a `unknown` e links de busca. Um ticker de opção vem com
        `wrong_endpoint` e links para os endpoints de opções.

        Este endpoint não traz dados de mercado. Não exige token.

        Args:
          symbols: Tickers separados por vírgula, até 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/tickers/coverage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"symbols": symbols}, ticker_coverage_params.TickerCoverageParams),
            ),
            cast_to=TickerCoverageResponse,
        )

    async def renames(
        self,
        *,
        end_date: str | Omit = omit,
        search: str | Omit = omit,
        start_date: str | Omit = omit,
        symbols: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TickerRenamesResponse:
        """
        Mudanças de ticker, com o ticker antigo, o novo, o atual e a data efetiva.

        Use para explicar por que um ticker antigo leva a outro e para corrigir séries
        salvas com o ticker antigo.

        Se um ativo mudou de ticker mais de uma vez, `canonicalSymbol` traz o último.
        `startDate` e `endDate` filtram pela data efetiva. A lista vem da data mais
        recente para a mais antiga.

        Não exige token. Para trocar uma lista de tickers pelos atuais, use
        [resolver ticker antigo](https://brapi.dev/docs/tickers/resolver).

        Args:
          end_date: Data efetiva final no formato YYYY-MM-DD.

          search: Parte do ticker antigo, do novo ou do atual.

          start_date: Data efetiva inicial no formato YYYY-MM-DD.

          symbols: Tickers separados por vírgula, até 20. Traz renomes em que algum deles é o
              ticker antigo, o novo ou o atual.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/tickers/renames",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "search": search,
                        "start_date": start_date,
                        "symbols": symbols,
                    },
                    ticker_renames_params.TickerRenamesParams,
                ),
            ),
            cast_to=TickerRenamesResponse,
        )

    async def resolve(
        self,
        *,
        symbols: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TickerResolveResponse:
        """Troca tickers antigos pelo ticker atual.

        Um ticker sem renome conhecido volta
        igual.

        Use antes de consultar dados de mercado quando os tickers vêm de usuários,
        planilhas antigas ou carteiras importadas.

        Envie até 20 tickers em `symbols`. A resposta segue a ordem enviada, sem
        repetidos. `status` é `renamed` quando o ticker mudou e `active` quando não há
        renome conhecido.

        Este endpoint não confirma se o ticker existe. Para isso, use a
        [cobertura por ticker](https://brapi.dev/docs/tickers/cobertura).

        Não exige token.

        Args:
          symbols: Tickers separados por vírgula, até 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/tickers/resolve",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"symbols": symbols}, ticker_resolve_params.TickerResolveParams),
            ),
            cast_to=TickerResolveResponse,
        )


class TickersResourceWithRawResponse:
    def __init__(self, tickers: TickersResource) -> None:
        self._tickers = tickers

        self.list = to_raw_response_wrapper(
            tickers.list,
        )
        self.coverage = to_raw_response_wrapper(
            tickers.coverage,
        )
        self.renames = to_raw_response_wrapper(
            tickers.renames,
        )
        self.resolve = to_raw_response_wrapper(
            tickers.resolve,
        )


class AsyncTickersResourceWithRawResponse:
    def __init__(self, tickers: AsyncTickersResource) -> None:
        self._tickers = tickers

        self.list = async_to_raw_response_wrapper(
            tickers.list,
        )
        self.coverage = async_to_raw_response_wrapper(
            tickers.coverage,
        )
        self.renames = async_to_raw_response_wrapper(
            tickers.renames,
        )
        self.resolve = async_to_raw_response_wrapper(
            tickers.resolve,
        )


class TickersResourceWithStreamingResponse:
    def __init__(self, tickers: TickersResource) -> None:
        self._tickers = tickers

        self.list = to_streamed_response_wrapper(
            tickers.list,
        )
        self.coverage = to_streamed_response_wrapper(
            tickers.coverage,
        )
        self.renames = to_streamed_response_wrapper(
            tickers.renames,
        )
        self.resolve = to_streamed_response_wrapper(
            tickers.resolve,
        )


class AsyncTickersResourceWithStreamingResponse:
    def __init__(self, tickers: AsyncTickersResource) -> None:
        self._tickers = tickers

        self.list = async_to_streamed_response_wrapper(
            tickers.list,
        )
        self.coverage = async_to_streamed_response_wrapper(
            tickers.coverage,
        )
        self.renames = async_to_streamed_response_wrapper(
            tickers.renames,
        )
        self.resolve = async_to_streamed_response_wrapper(
            tickers.resolve,
        )
