# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
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
from ....types.v2.funds import fiagro_reports_params, fiagro_portfolio_params
from ....types.v2.funds.fiagro_reports_response import FiagroReportsResponse
from ....types.v2.funds.fiagro_portfolio_response import FiagroPortfolioResponse

__all__ = ["FiagroResource", "AsyncFiagroResource"]


class FiagroResource(SyncAPIResource):
    """
    Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
    """

    @cached_property
    def with_raw_response(self) -> FiagroResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return FiagroResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FiagroResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return FiagroResourceWithStreamingResponse(self)

    def portfolio(
        self,
        *,
        all_versions: Optional[bool] | Omit = omit,
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
    ) -> FiagroPortfolioResponse:
        """
        Carteira de FIAGRO em um mês: resumo, alocações por classe de ativo, passivos e
        investidores.

        Use para ver quanto do fundo está em CRA, direitos creditórios, imóveis rurais
        ou participações.

        Informe `symbols` ou `cnpjs`. Sem `referenceDate`, a resposta traz o mês mais
        recente.

        Plano Pro.

        Args:
          all_versions: Se `true`, traz todas as versões enviadas à CVM para cada mês.

          cnpjs: CNPJs separados por vírgula, até 20, com ou sem pontuação.

          reference_date: Mês de referência no formato YYYY-MM-DD.

          symbols: Tickers separados por vírgula, até 20. Ex.: JURO11,XPCA11.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/funds/fiagro/portfolio",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "all_versions": all_versions,
                        "cnpjs": cnpjs,
                        "include": include,
                        "reference_date": reference_date,
                        "symbols": symbols,
                    },
                    fiagro_portfolio_params.FiagroPortfolioParams,
                ),
            ),
            cast_to=FiagroPortfolioResponse,
        )

    def reports(
        self,
        *,
        all_versions: Optional[bool] | Omit = omit,
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
    ) -> FiagroReportsResponse:
        """
        Relatório mensal de FIAGRO na CVM: patrimônio, valor patrimonial por cota,
        cotistas, rentabilidade do mês, dividend yield mensal e valores a distribuir.

        Use para acompanhar a evolução de um FIAGRO mês a mês.

        Informe `symbols` ou `cnpjs`. Por padrão, a resposta traz só a versão mais
        recente de cada mês. Use `allVersions=true` para ver as reapresentações.

        `sortBy` aceita `referenceDate`, `symbol`, `cnpj`, `netEquity`, `totalInvestors`
        e `dividendYieldMonthly`. O padrão é `referenceDate`.

        Plano Pro.

        Args:
          all_versions: Se `true`, traz todas as versões enviadas à CVM para cada mês.

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
            "/api/v2/funds/fiagro/reports",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "all_versions": all_versions,
                        "cnpjs": cnpjs,
                        "end_date": end_date,
                        "limit": limit,
                        "page": page,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "start_date": start_date,
                        "symbols": symbols,
                    },
                    fiagro_reports_params.FiagroReportsParams,
                ),
            ),
            cast_to=FiagroReportsResponse,
        )


class AsyncFiagroResource(AsyncAPIResource):
    """
    Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
    """

    @cached_property
    def with_raw_response(self) -> AsyncFiagroResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFiagroResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFiagroResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncFiagroResourceWithStreamingResponse(self)

    async def portfolio(
        self,
        *,
        all_versions: Optional[bool] | Omit = omit,
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
    ) -> FiagroPortfolioResponse:
        """
        Carteira de FIAGRO em um mês: resumo, alocações por classe de ativo, passivos e
        investidores.

        Use para ver quanto do fundo está em CRA, direitos creditórios, imóveis rurais
        ou participações.

        Informe `symbols` ou `cnpjs`. Sem `referenceDate`, a resposta traz o mês mais
        recente.

        Plano Pro.

        Args:
          all_versions: Se `true`, traz todas as versões enviadas à CVM para cada mês.

          cnpjs: CNPJs separados por vírgula, até 20, com ou sem pontuação.

          reference_date: Mês de referência no formato YYYY-MM-DD.

          symbols: Tickers separados por vírgula, até 20. Ex.: JURO11,XPCA11.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/funds/fiagro/portfolio",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "all_versions": all_versions,
                        "cnpjs": cnpjs,
                        "include": include,
                        "reference_date": reference_date,
                        "symbols": symbols,
                    },
                    fiagro_portfolio_params.FiagroPortfolioParams,
                ),
            ),
            cast_to=FiagroPortfolioResponse,
        )

    async def reports(
        self,
        *,
        all_versions: Optional[bool] | Omit = omit,
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
    ) -> FiagroReportsResponse:
        """
        Relatório mensal de FIAGRO na CVM: patrimônio, valor patrimonial por cota,
        cotistas, rentabilidade do mês, dividend yield mensal e valores a distribuir.

        Use para acompanhar a evolução de um FIAGRO mês a mês.

        Informe `symbols` ou `cnpjs`. Por padrão, a resposta traz só a versão mais
        recente de cada mês. Use `allVersions=true` para ver as reapresentações.

        `sortBy` aceita `referenceDate`, `symbol`, `cnpj`, `netEquity`, `totalInvestors`
        e `dividendYieldMonthly`. O padrão é `referenceDate`.

        Plano Pro.

        Args:
          all_versions: Se `true`, traz todas as versões enviadas à CVM para cada mês.

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
            "/api/v2/funds/fiagro/reports",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "all_versions": all_versions,
                        "cnpjs": cnpjs,
                        "end_date": end_date,
                        "limit": limit,
                        "page": page,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "start_date": start_date,
                        "symbols": symbols,
                    },
                    fiagro_reports_params.FiagroReportsParams,
                ),
            ),
            cast_to=FiagroReportsResponse,
        )


class FiagroResourceWithRawResponse:
    def __init__(self, fiagro: FiagroResource) -> None:
        self._fiagro = fiagro

        self.portfolio = to_raw_response_wrapper(
            fiagro.portfolio,
        )
        self.reports = to_raw_response_wrapper(
            fiagro.reports,
        )


class AsyncFiagroResourceWithRawResponse:
    def __init__(self, fiagro: AsyncFiagroResource) -> None:
        self._fiagro = fiagro

        self.portfolio = async_to_raw_response_wrapper(
            fiagro.portfolio,
        )
        self.reports = async_to_raw_response_wrapper(
            fiagro.reports,
        )


class FiagroResourceWithStreamingResponse:
    def __init__(self, fiagro: FiagroResource) -> None:
        self._fiagro = fiagro

        self.portfolio = to_streamed_response_wrapper(
            fiagro.portfolio,
        )
        self.reports = to_streamed_response_wrapper(
            fiagro.reports,
        )


class AsyncFiagroResourceWithStreamingResponse:
    def __init__(self, fiagro: AsyncFiagroResource) -> None:
        self._fiagro = fiagro

        self.portfolio = async_to_streamed_response_wrapper(
            fiagro.portfolio,
        )
        self.reports = async_to_streamed_response_wrapper(
            fiagro.reports,
        )
