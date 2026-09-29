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
from ....types.v2.funds import fidc_reports_params, fidc_portfolio_params
from ....types.v2.funds.fidc_reports_response import FidcReportsResponse
from ....types.v2.funds.fidc_portfolio_response import FidcPortfolioResponse

__all__ = ["FidcResource", "AsyncFidcResource"]


class FidcResource(SyncAPIResource):
    """
    Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
    """

    @cached_property
    def with_raw_response(self) -> FidcResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return FidcResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FidcResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return FidcResourceWithStreamingResponse(self)

    def portfolio(
        self,
        *,
        cnpjs: str | Omit = omit,
        include: str | Omit = omit,
        reference_date: str | Omit = omit,
        symbols: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FidcPortfolioResponse:
        """
        Carteira de FIDC em um mês: setores, vencimentos, inadimplência, faixas de
        risco, classes de cota, cotistas e cedentes.

        Use para avaliar o risco de crédito de um FIDC e a concentração por cedente.

        Informe `cnpjs`, ou `symbols` quando o fundo tem ticker. Sem `referenceDate`, a
        resposta traz o mês mais recente.

        Plano Pro.

        Args:
          cnpjs: CNPJs separados por vírgula, até 20, com ou sem pontuação.

          reference_date: Mês de referência no formato YYYY-MM-DD.

          symbols: Tickers separados por vírgula, até 20. Ex.: JURO11,XPCA11.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/funds/fidc/portfolio",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cnpjs": cnpjs,
                        "include": include,
                        "reference_date": reference_date,
                        "symbols": symbols,
                    },
                    fidc_portfolio_params.FidcPortfolioParams,
                ),
            ),
            cast_to=FidcPortfolioResponse,
        )

    def reports(
        self,
        *,
        cnpjs: str | Omit = omit,
        end_date: str | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        sort_by: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        symbols: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FidcReportsResponse:
        """
        Relatório mensal de FIDC na CVM: ativos, valor da carteira, patrimônio líquido,
        patrimônio médio, passivos, classe de cota e tipo de condomínio.

        Use para acompanhar o tamanho e a evolução de um FIDC mês a mês.

        A maioria dos FIDCs não tem ticker em bolsa. Use `cnpjs`. `symbols` funciona só
        quando o fundo tem ticker.

        `sortBy` aceita `referenceDate`, `cnpj`, `netEquity`, `assets` e
        `portfolioValue`. O padrão é `referenceDate`.

        Plano Pro.

        Args:
          cnpjs: CNPJs separados por vírgula, até 20, com ou sem pontuação.

          end_date: Data final no formato YYYY-MM-DD.

          limit: Itens por página.

          page: Número da página, a partir de 1.

          sort_by: Campo usado na ordenação.

          sort_order: Ordem crescente (`asc`) ou decrescente (`desc`).

          start_date: Data inicial no formato YYYY-MM-DD.

          symbols: Tickers separados por vírgula, até 20. Ex.: JURO11,XPCA11.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/funds/fidc/reports",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cnpjs": cnpjs,
                        "end_date": end_date,
                        "limit": limit,
                        "page": page,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "start_date": start_date,
                        "symbols": symbols,
                    },
                    fidc_reports_params.FidcReportsParams,
                ),
            ),
            cast_to=FidcReportsResponse,
        )


class AsyncFidcResource(AsyncAPIResource):
    """
    Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
    """

    @cached_property
    def with_raw_response(self) -> AsyncFidcResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFidcResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFidcResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncFidcResourceWithStreamingResponse(self)

    async def portfolio(
        self,
        *,
        cnpjs: str | Omit = omit,
        include: str | Omit = omit,
        reference_date: str | Omit = omit,
        symbols: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FidcPortfolioResponse:
        """
        Carteira de FIDC em um mês: setores, vencimentos, inadimplência, faixas de
        risco, classes de cota, cotistas e cedentes.

        Use para avaliar o risco de crédito de um FIDC e a concentração por cedente.

        Informe `cnpjs`, ou `symbols` quando o fundo tem ticker. Sem `referenceDate`, a
        resposta traz o mês mais recente.

        Plano Pro.

        Args:
          cnpjs: CNPJs separados por vírgula, até 20, com ou sem pontuação.

          reference_date: Mês de referência no formato YYYY-MM-DD.

          symbols: Tickers separados por vírgula, até 20. Ex.: JURO11,XPCA11.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/funds/fidc/portfolio",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cnpjs": cnpjs,
                        "include": include,
                        "reference_date": reference_date,
                        "symbols": symbols,
                    },
                    fidc_portfolio_params.FidcPortfolioParams,
                ),
            ),
            cast_to=FidcPortfolioResponse,
        )

    async def reports(
        self,
        *,
        cnpjs: str | Omit = omit,
        end_date: str | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        sort_by: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        symbols: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FidcReportsResponse:
        """
        Relatório mensal de FIDC na CVM: ativos, valor da carteira, patrimônio líquido,
        patrimônio médio, passivos, classe de cota e tipo de condomínio.

        Use para acompanhar o tamanho e a evolução de um FIDC mês a mês.

        A maioria dos FIDCs não tem ticker em bolsa. Use `cnpjs`. `symbols` funciona só
        quando o fundo tem ticker.

        `sortBy` aceita `referenceDate`, `cnpj`, `netEquity`, `assets` e
        `portfolioValue`. O padrão é `referenceDate`.

        Plano Pro.

        Args:
          cnpjs: CNPJs separados por vírgula, até 20, com ou sem pontuação.

          end_date: Data final no formato YYYY-MM-DD.

          limit: Itens por página.

          page: Número da página, a partir de 1.

          sort_by: Campo usado na ordenação.

          sort_order: Ordem crescente (`asc`) ou decrescente (`desc`).

          start_date: Data inicial no formato YYYY-MM-DD.

          symbols: Tickers separados por vírgula, até 20. Ex.: JURO11,XPCA11.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/funds/fidc/reports",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cnpjs": cnpjs,
                        "end_date": end_date,
                        "limit": limit,
                        "page": page,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "start_date": start_date,
                        "symbols": symbols,
                    },
                    fidc_reports_params.FidcReportsParams,
                ),
            ),
            cast_to=FidcReportsResponse,
        )


class FidcResourceWithRawResponse:
    def __init__(self, fidc: FidcResource) -> None:
        self._fidc = fidc

        self.portfolio = to_raw_response_wrapper(
            fidc.portfolio,
        )
        self.reports = to_raw_response_wrapper(
            fidc.reports,
        )


class AsyncFidcResourceWithRawResponse:
    def __init__(self, fidc: AsyncFidcResource) -> None:
        self._fidc = fidc

        self.portfolio = async_to_raw_response_wrapper(
            fidc.portfolio,
        )
        self.reports = async_to_raw_response_wrapper(
            fidc.reports,
        )


class FidcResourceWithStreamingResponse:
    def __init__(self, fidc: FidcResource) -> None:
        self._fidc = fidc

        self.portfolio = to_streamed_response_wrapper(
            fidc.portfolio,
        )
        self.reports = to_streamed_response_wrapper(
            fidc.reports,
        )


class AsyncFidcResourceWithStreamingResponse:
    def __init__(self, fidc: AsyncFidcResource) -> None:
        self._fidc = fidc

        self.portfolio = async_to_streamed_response_wrapper(
            fidc.portfolio,
        )
        self.reports = async_to_streamed_response_wrapper(
            fidc.reports,
        )
