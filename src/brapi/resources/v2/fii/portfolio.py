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
from ....types.v2.fii import portfolio_history_params, portfolio_retrieve_params
from ....types.v2.fii.portfolio_history_response import PortfolioHistoryResponse
from ....types.v2.fii.portfolio_retrieve_response import PortfolioRetrieveResponse

__all__ = ["PortfolioResource", "AsyncPortfolioResource"]


class PortfolioResource(SyncAPIResource):
    """
    Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
    """

    @cached_property
    def with_raw_response(self) -> PortfolioResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return PortfolioResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PortfolioResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return PortfolioResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        symbols: str,
        all_versions: Literal["true", "false"] | Omit = omit,
        include: str | Omit = omit,
        reference_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortfolioRetrieveResponse:
        """
        Composição da carteira de FIIs pelo informe trimestral da CVM: imóveis, CRIs e
        outros ativos financeiros, cotas de outros FIIs, terrenos e direitos, com totais
        em `summary`.

        Use para analisar FIIs de papel e fundos de fundos, ver os CRIs de um fundo ou
        somar a exposição por classe de ativo.

        `include` escolhe as listas. Sem `include`, retorna todas. `summary` sempre vem.

        Em fundos de fundos, `fundHoldings` lista as cotas de outros FIIs. Em FIIs de
        papel, `financialAssets` lista os CRIs com emissor e valor. `allocations` resume
        a carteira por classe de ativo.

        Sem `referenceDate`, retorna o trimestre mais recente de cada fundo. Informes
        podem ser retificados. O padrão retorna a versão mais recente, e
        `allVersions=true` retorna todas.

        Para imóveis e vacância, use
        [imóveis de FIIs](https://brapi.dev/docs/fiis/imoveis). Para a série no tempo,
        use o [histórico da carteira](https://brapi.dev/docs/fiis/carteira-historico).

        Plano Pro. Sem token, aceita só `symbols` com MXRF11 e HGLG11.

        Args:
          symbols: Tickers de FIIs separados por vírgula, até 20. Ex.: HGLG11,MXRF11.

          all_versions: true inclui todas as versões do trimestre. false retorna só a mais recente.

          include: Listas a retornar, separadas por vírgula: allocations, properties,
              financialAssets, fundHoldings, lands, rights. summary sempre vem. Sem valor,
              retorna todas.

          reference_date: Fim do trimestre no formato YYYY-MM-DD. Sem valor, retorna o trimestre mais
              recente de cada FII.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/fii/portfolio",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "symbols": symbols,
                        "all_versions": all_versions,
                        "include": include,
                        "reference_date": reference_date,
                    },
                    portfolio_retrieve_params.PortfolioRetrieveParams,
                ),
            ),
            cast_to=PortfolioRetrieveResponse,
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
    ) -> PortfolioHistoryResponse:
        """
        Série trimestral da carteira de FIIs: um ponto por fundo, trimestre e versão do
        informe, com `summary` e `allocations` por classe de ativo.

        Use para ver como a alocação de um fundo mudou no tempo, por exemplo entre
        imóveis, CRIs e cotas de outros FIIs.

        A resposta não traz as listas item a item. Para o detalhe de um trimestre, use a
        [carteira de FIIs](https://brapi.dev/docs/fiis/carteira) com `referenceDate`.

        Sem `startDate` e `endDate`, retorna os últimos 12 meses. `sortBy` aceita
        `referenceDate` (padrão), `symbol`, `version`, `totalItems`, `declaredValue` e
        `financialAssetsDeclaredValue`. `allVersions=true` inclui as versões
        retificadas.

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
            "/api/v2/fii/portfolio/history",
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
                    portfolio_history_params.PortfolioHistoryParams,
                ),
            ),
            cast_to=PortfolioHistoryResponse,
        )


class AsyncPortfolioResource(AsyncAPIResource):
    """
    Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
    """

    @cached_property
    def with_raw_response(self) -> AsyncPortfolioResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPortfolioResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPortfolioResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncPortfolioResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        symbols: str,
        all_versions: Literal["true", "false"] | Omit = omit,
        include: str | Omit = omit,
        reference_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortfolioRetrieveResponse:
        """
        Composição da carteira de FIIs pelo informe trimestral da CVM: imóveis, CRIs e
        outros ativos financeiros, cotas de outros FIIs, terrenos e direitos, com totais
        em `summary`.

        Use para analisar FIIs de papel e fundos de fundos, ver os CRIs de um fundo ou
        somar a exposição por classe de ativo.

        `include` escolhe as listas. Sem `include`, retorna todas. `summary` sempre vem.

        Em fundos de fundos, `fundHoldings` lista as cotas de outros FIIs. Em FIIs de
        papel, `financialAssets` lista os CRIs com emissor e valor. `allocations` resume
        a carteira por classe de ativo.

        Sem `referenceDate`, retorna o trimestre mais recente de cada fundo. Informes
        podem ser retificados. O padrão retorna a versão mais recente, e
        `allVersions=true` retorna todas.

        Para imóveis e vacância, use
        [imóveis de FIIs](https://brapi.dev/docs/fiis/imoveis). Para a série no tempo,
        use o [histórico da carteira](https://brapi.dev/docs/fiis/carteira-historico).

        Plano Pro. Sem token, aceita só `symbols` com MXRF11 e HGLG11.

        Args:
          symbols: Tickers de FIIs separados por vírgula, até 20. Ex.: HGLG11,MXRF11.

          all_versions: true inclui todas as versões do trimestre. false retorna só a mais recente.

          include: Listas a retornar, separadas por vírgula: allocations, properties,
              financialAssets, fundHoldings, lands, rights. summary sempre vem. Sem valor,
              retorna todas.

          reference_date: Fim do trimestre no formato YYYY-MM-DD. Sem valor, retorna o trimestre mais
              recente de cada FII.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/fii/portfolio",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "symbols": symbols,
                        "all_versions": all_versions,
                        "include": include,
                        "reference_date": reference_date,
                    },
                    portfolio_retrieve_params.PortfolioRetrieveParams,
                ),
            ),
            cast_to=PortfolioRetrieveResponse,
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
    ) -> PortfolioHistoryResponse:
        """
        Série trimestral da carteira de FIIs: um ponto por fundo, trimestre e versão do
        informe, com `summary` e `allocations` por classe de ativo.

        Use para ver como a alocação de um fundo mudou no tempo, por exemplo entre
        imóveis, CRIs e cotas de outros FIIs.

        A resposta não traz as listas item a item. Para o detalhe de um trimestre, use a
        [carteira de FIIs](https://brapi.dev/docs/fiis/carteira) com `referenceDate`.

        Sem `startDate` e `endDate`, retorna os últimos 12 meses. `sortBy` aceita
        `referenceDate` (padrão), `symbol`, `version`, `totalItems`, `declaredValue` e
        `financialAssetsDeclaredValue`. `allVersions=true` inclui as versões
        retificadas.

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
            "/api/v2/fii/portfolio/history",
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
                    portfolio_history_params.PortfolioHistoryParams,
                ),
            ),
            cast_to=PortfolioHistoryResponse,
        )


class PortfolioResourceWithRawResponse:
    def __init__(self, portfolio: PortfolioResource) -> None:
        self._portfolio = portfolio

        self.retrieve = to_raw_response_wrapper(
            portfolio.retrieve,
        )
        self.history = to_raw_response_wrapper(
            portfolio.history,
        )


class AsyncPortfolioResourceWithRawResponse:
    def __init__(self, portfolio: AsyncPortfolioResource) -> None:
        self._portfolio = portfolio

        self.retrieve = async_to_raw_response_wrapper(
            portfolio.retrieve,
        )
        self.history = async_to_raw_response_wrapper(
            portfolio.history,
        )


class PortfolioResourceWithStreamingResponse:
    def __init__(self, portfolio: PortfolioResource) -> None:
        self._portfolio = portfolio

        self.retrieve = to_streamed_response_wrapper(
            portfolio.retrieve,
        )
        self.history = to_streamed_response_wrapper(
            portfolio.history,
        )


class AsyncPortfolioResourceWithStreamingResponse:
    def __init__(self, portfolio: AsyncPortfolioResource) -> None:
        self._portfolio = portfolio

        self.retrieve = async_to_streamed_response_wrapper(
            portfolio.retrieve,
        )
        self.history = async_to_streamed_response_wrapper(
            portfolio.history,
        )
