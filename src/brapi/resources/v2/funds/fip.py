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
from ....types.v2.funds import fip_reports_params
from ....types.v2.funds.fip_reports_response import FipReportsResponse

__all__ = ["FipResource", "AsyncFipResource"]


class FipResource(SyncAPIResource):
    """
    Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
    """

    @cached_property
    def with_raw_response(self) -> FipResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return FipResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FipResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return FipResourceWithStreamingResponse(self)

    def reports(
        self,
        *,
        cnpjs: str | Omit = omit,
        end_date: str | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        report_type: Literal["trimestral", "quadrimestral"] | Omit = omit,
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
    ) -> FipReportsResponse:
        """
        Relatórios trimestrais e quadrimestrais de FIP na CVM: patrimônio, capital
        comprometido e integralizado, cotas, classe e composição de investidores.

        Use para acompanhar o capital e os investidores de um FIP.

        Escolha o documento com `reportType`. Informe `cnpjs`, ou `symbols` quando o
        fundo tem ticker. FIP não tem cota diária.

        `sortBy` aceita `referenceDate`, `cnpj` e `netEquity`. O padrão é
        `referenceDate`.

        Plano Pro.

        Args:
          cnpjs: CNPJs separados por vírgula, até 20, com ou sem pontuação.

          end_date: Data final no formato YYYY-MM-DD.

          limit: Itens por página.

          page: Número da página, a partir de 1.

          report_type: Tipo de relatório.

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
            "/api/v2/funds/fip/reports",
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
                        "report_type": report_type,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "start_date": start_date,
                        "symbols": symbols,
                    },
                    fip_reports_params.FipReportsParams,
                ),
            ),
            cast_to=FipReportsResponse,
        )


class AsyncFipResource(AsyncAPIResource):
    """
    Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
    """

    @cached_property
    def with_raw_response(self) -> AsyncFipResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFipResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFipResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncFipResourceWithStreamingResponse(self)

    async def reports(
        self,
        *,
        cnpjs: str | Omit = omit,
        end_date: str | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        report_type: Literal["trimestral", "quadrimestral"] | Omit = omit,
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
    ) -> FipReportsResponse:
        """
        Relatórios trimestrais e quadrimestrais de FIP na CVM: patrimônio, capital
        comprometido e integralizado, cotas, classe e composição de investidores.

        Use para acompanhar o capital e os investidores de um FIP.

        Escolha o documento com `reportType`. Informe `cnpjs`, ou `symbols` quando o
        fundo tem ticker. FIP não tem cota diária.

        `sortBy` aceita `referenceDate`, `cnpj` e `netEquity`. O padrão é
        `referenceDate`.

        Plano Pro.

        Args:
          cnpjs: CNPJs separados por vírgula, até 20, com ou sem pontuação.

          end_date: Data final no formato YYYY-MM-DD.

          limit: Itens por página.

          page: Número da página, a partir de 1.

          report_type: Tipo de relatório.

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
            "/api/v2/funds/fip/reports",
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
                        "report_type": report_type,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "start_date": start_date,
                        "symbols": symbols,
                    },
                    fip_reports_params.FipReportsParams,
                ),
            ),
            cast_to=FipReportsResponse,
        )


class FipResourceWithRawResponse:
    def __init__(self, fip: FipResource) -> None:
        self._fip = fip

        self.reports = to_raw_response_wrapper(
            fip.reports,
        )


class AsyncFipResourceWithRawResponse:
    def __init__(self, fip: AsyncFipResource) -> None:
        self._fip = fip

        self.reports = async_to_raw_response_wrapper(
            fip.reports,
        )


class FipResourceWithStreamingResponse:
    def __init__(self, fip: FipResource) -> None:
        self._fip = fip

        self.reports = to_streamed_response_wrapper(
            fip.reports,
        )


class AsyncFipResourceWithStreamingResponse:
    def __init__(self, fip: AsyncFipResource) -> None:
        self._fip = fip

        self.reports = async_to_streamed_response_wrapper(
            fip.reports,
        )
