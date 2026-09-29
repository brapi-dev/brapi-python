# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .fip import (
    FipResource,
    AsyncFipResource,
    FipResourceWithRawResponse,
    AsyncFipResourceWithRawResponse,
    FipResourceWithStreamingResponse,
    AsyncFipResourceWithStreamingResponse,
)
from .nav import (
    NavResource,
    AsyncNavResource,
    NavResourceWithRawResponse,
    AsyncNavResourceWithRawResponse,
    NavResourceWithStreamingResponse,
    AsyncNavResourceWithStreamingResponse,
)
from .fidc import (
    FidcResource,
    AsyncFidcResource,
    FidcResourceWithRawResponse,
    AsyncFidcResourceWithRawResponse,
    FidcResourceWithStreamingResponse,
    AsyncFidcResourceWithStreamingResponse,
)
from .fiagro import (
    FiagroResource,
    AsyncFiagroResource,
    FiagroResourceWithRawResponse,
    AsyncFiagroResourceWithRawResponse,
    FiagroResourceWithStreamingResponse,
    AsyncFiagroResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.v2 import (
    fund_list_params,
    fund_profile_params,
    fund_dividends_params,
    fund_portfolio_params,
    fund_indicators_params,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v2.fund_list_response import FundListResponse
from ....types.v2.fund_profile_response import FundProfileResponse
from ....types.v2.fund_dividends_response import FundDividendsResponse
from ....types.v2.fund_portfolio_response import FundPortfolioResponse
from ....types.v2.fund_indicators_response import FundIndicatorsResponse

__all__ = ["FundsResource", "AsyncFundsResource"]


class FundsResource(SyncAPIResource):
    """
    Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
    """

    @cached_property
    def nav(self) -> NavResource:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return NavResource(self._client)

    @cached_property
    def fiagro(self) -> FiagroResource:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return FiagroResource(self._client)

    @cached_property
    def fidc(self) -> FidcResource:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return FidcResource(self._client)

    @cached_property
    def fip(self) -> FipResource:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return FipResource(self._client)

    @cached_property
    def with_raw_response(self) -> FundsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return FundsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FundsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return FundsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        asset_type: Literal["fii", "fiagro", "fiinfra", "fif", "fidc", "fip", "etf", "other"] | Omit = omit,
        cnpjs: str | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        search: str | Omit = omit,
        sort_by: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        status: str | Omit = omit,
        symbols: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FundListResponse:
        """
        Lista fundos brasileiros: FII, FIAGRO, FI-Infra, FIF, FIDC, FIP, ETF e outros.
        Cada item traz ticker, CNPJ, tipo, classificações, administrador, gestor e
        indicadores atuais.

        Use para descobrir o tipo de um fundo, achar um CNPJ ou filtrar fundos por tipo.

        Busque por `symbols`, `cnpjs` ou `search`. O `search` procura no ticker, no
        nome, na razão social, no ISIN e no CNPJ.

        Nem todo ticker terminado em 11 é FII. `JURO11` é FI-Infra e não responde nos
        [endpoints de FIIs](https://brapi.dev/docs/fiis).

        `sortBy` aceita `symbol`, `name`, `assetType`, `price`, `navPerShare`,
        `priceToNav`, `totalInvestors` e `updatedAt`. O padrão é `updatedAt`.

        Plano Pro.

        Args:
          asset_type: Tipo do fundo.

          cnpjs: CNPJs separados por vírgula, até 20, com ou sem pontuação.

          limit: Itens por página.

          page: Número da página, a partir de 1.

          search: Texto buscado no ticker, nome, razão social, ISIN ou CNPJ.

          sort_by: Campo usado na ordenação.

          sort_order: Ordem crescente (`asc`) ou decrescente (`desc`).

          status: Situação do fundo no cadastro.

          symbols: Tickers separados por vírgula, até 20. Ex.: JURO11,XPCA11.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/funds/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asset_type": asset_type,
                        "cnpjs": cnpjs,
                        "limit": limit,
                        "page": page,
                        "search": search,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "status": status,
                        "symbols": symbols,
                    },
                    fund_list_params.FundListParams,
                ),
            ),
            cast_to=FundListResponse,
        )

    def dividends(
        self,
        *,
        asset_type: Literal["fiagro", "fiinfra", "fif", "fidc", "fip", "other"] | Omit = omit,
        cnpjs: str | Omit = omit,
        end_date: str | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        sort_by: Literal["lastDatePrior", "paymentDate", "declaredDate", "symbol", "rate"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        symbols: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FundDividendsResponse:
        """Dividendos e rendimentos de FIAGRO, FI-Infra, FIF, FIDC e FIP listados.

        Cada
        evento traz data de declaração, data-com (`lastDatePrior`), data ex quando
        existe, data de pagamento, valor por cota e rótulo.

        Use para calcular renda, montar calendários de pagamento e comparar rendimentos.

        Os filtros `startDate` e `endDate` usam `paymentDate`. Sem `symbols` e `cnpjs`,
        a resposta traz todos os fundos.

        FIIs ficam em [dividendos de FIIs](https://brapi.dev/docs/fiis/dividendos). Um
        ticker de FII neste endpoint retorna erro 400.

        O histórico começa no primeiro evento verificável de cada fundo. Não há data
        inicial única. As fontes são documentos da CVM e comunicados de administradores
        e gestores. Eventos de tickers antigos continuam depois de um renome. A brapi
        não estima datas de pagamento. A revisão é mensal.

        Plano Pro.

        Args:
          asset_type: Tipo do fundo.

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
            "/api/v2/funds/dividends",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asset_type": asset_type,
                        "cnpjs": cnpjs,
                        "end_date": end_date,
                        "limit": limit,
                        "page": page,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "start_date": start_date,
                        "symbols": symbols,
                    },
                    fund_dividends_params.FundDividendsParams,
                ),
            ),
            cast_to=FundDividendsResponse,
        )

    def indicators(
        self,
        *,
        asset_type: Literal["fii", "fiagro", "fiinfra", "fif", "fidc", "fip", "etf", "other"] | Omit = omit,
        cnpjs: str | Omit = omit,
        symbols: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FundIndicatorsResponse:
        """
        Indicadores mais recentes de um ou mais fundos: preço de mercado, valor
        patrimonial por cota (`navPerShare`), a razão entre os dois, patrimônio, ativos
        e número de cotistas.

        Use para comparar preço e valor patrimonial, medir ágio ou deságio e ver o
        tamanho do fundo.

        Informe `symbols` ou `cnpjs`. Se você não tem o identificador, use a
        [lista de fundos](https://brapi.dev/docs/fundos/listagem).

        Plano Pro.

        Args:
          asset_type: Tipo do fundo.

          cnpjs: CNPJs separados por vírgula, até 20, com ou sem pontuação.

          symbols: Tickers separados por vírgula, até 20. Ex.: JURO11,XPCA11.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/funds/indicators",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asset_type": asset_type,
                        "cnpjs": cnpjs,
                        "symbols": symbols,
                    },
                    fund_indicators_params.FundIndicatorsParams,
                ),
            ),
            cast_to=FundIndicatorsResponse,
        )

    def portfolio(
        self,
        *,
        cnpjs: str | Omit = omit,
        include: str | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        reference_date: str | Omit = omit,
        symbols: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FundPortfolioResponse:
        """Carteira de fundos FI e FIF, do arquivo CDA da CVM.

        As posições vêm agrupadas em
        títulos públicos, cotas de fundos, crédito privado, ativos listados, recebíveis
        e valores a pagar.

        Use para ver onde o fundo investe e qual o peso de cada grupo de ativos.

        Informe `symbols` ou `cnpjs`. Sem `referenceDate`, a resposta traz a carteira
        mais recente.

        Filtre os grupos com `include`: `publicBonds`, `fundHoldings`, `creditAssets`,
        `listedSecurities`, `receivables` e `payables`.

        Posições confidenciais aparecem só no total, em `confidentialSummary`.

        A CVM publica o CDA com meses de atraso. Mostre `referenceDate` junto do dado.

        Plano Pro.

        Args:
          cnpjs: CNPJs separados por vírgula, até 20, com ou sem pontuação.

          include: Grupos de ativos separados por vírgula. Ex.: publicBonds,creditAssets.

          limit: Itens por página.

          page: Número da página, a partir de 1.

          reference_date: Mês de referência no formato YYYY-MM-DD.

          symbols: Tickers separados por vírgula, até 20. Ex.: JURO11,XPCA11.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/funds/portfolio",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cnpjs": cnpjs,
                        "include": include,
                        "limit": limit,
                        "page": page,
                        "reference_date": reference_date,
                        "symbols": symbols,
                    },
                    fund_portfolio_params.FundPortfolioParams,
                ),
            ),
            cast_to=FundPortfolioResponse,
        )

    def profile(
        self,
        *,
        cnpjs: str | Omit = omit,
        end_date: str | Omit = omit,
        include: str | Omit = omit,
        reference_date: str | Omit = omit,
        start_date: str | Omit = omit,
        symbols: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FundProfileResponse:
        """
        Perfil mensal de fundos FI e FIF, conforme a CVM: distribuição de cotistas,
        medidas de risco, liquidez, concentração e exposição a crédito privado.

        Use para ver se o fundo é de varejo ou institucional e quanto do patrimônio está
        em ativos de baixa liquidez.

        Informe `symbols` ou `cnpjs`. Sem filtro de data, a resposta traz o perfil mais
        recente de cada fundo.

        Plano Pro.

        Args:
          cnpjs: CNPJs separados por vírgula, até 20, com ou sem pontuação.

          end_date: Data final no formato YYYY-MM-DD.

          reference_date: Mês de referência no formato YYYY-MM-DD.

          start_date: Data inicial no formato YYYY-MM-DD.

          symbols: Tickers separados por vírgula, até 20. Ex.: JURO11,XPCA11.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/funds/profile",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cnpjs": cnpjs,
                        "end_date": end_date,
                        "include": include,
                        "reference_date": reference_date,
                        "start_date": start_date,
                        "symbols": symbols,
                    },
                    fund_profile_params.FundProfileParams,
                ),
            ),
            cast_to=FundProfileResponse,
        )


class AsyncFundsResource(AsyncAPIResource):
    """
    Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
    """

    @cached_property
    def nav(self) -> AsyncNavResource:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return AsyncNavResource(self._client)

    @cached_property
    def fiagro(self) -> AsyncFiagroResource:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return AsyncFiagroResource(self._client)

    @cached_property
    def fidc(self) -> AsyncFidcResource:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return AsyncFidcResource(self._client)

    @cached_property
    def fip(self) -> AsyncFipResource:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return AsyncFipResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFundsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFundsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFundsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncFundsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        asset_type: Literal["fii", "fiagro", "fiinfra", "fif", "fidc", "fip", "etf", "other"] | Omit = omit,
        cnpjs: str | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        search: str | Omit = omit,
        sort_by: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        status: str | Omit = omit,
        symbols: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FundListResponse:
        """
        Lista fundos brasileiros: FII, FIAGRO, FI-Infra, FIF, FIDC, FIP, ETF e outros.
        Cada item traz ticker, CNPJ, tipo, classificações, administrador, gestor e
        indicadores atuais.

        Use para descobrir o tipo de um fundo, achar um CNPJ ou filtrar fundos por tipo.

        Busque por `symbols`, `cnpjs` ou `search`. O `search` procura no ticker, no
        nome, na razão social, no ISIN e no CNPJ.

        Nem todo ticker terminado em 11 é FII. `JURO11` é FI-Infra e não responde nos
        [endpoints de FIIs](https://brapi.dev/docs/fiis).

        `sortBy` aceita `symbol`, `name`, `assetType`, `price`, `navPerShare`,
        `priceToNav`, `totalInvestors` e `updatedAt`. O padrão é `updatedAt`.

        Plano Pro.

        Args:
          asset_type: Tipo do fundo.

          cnpjs: CNPJs separados por vírgula, até 20, com ou sem pontuação.

          limit: Itens por página.

          page: Número da página, a partir de 1.

          search: Texto buscado no ticker, nome, razão social, ISIN ou CNPJ.

          sort_by: Campo usado na ordenação.

          sort_order: Ordem crescente (`asc`) ou decrescente (`desc`).

          status: Situação do fundo no cadastro.

          symbols: Tickers separados por vírgula, até 20. Ex.: JURO11,XPCA11.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/funds/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asset_type": asset_type,
                        "cnpjs": cnpjs,
                        "limit": limit,
                        "page": page,
                        "search": search,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "status": status,
                        "symbols": symbols,
                    },
                    fund_list_params.FundListParams,
                ),
            ),
            cast_to=FundListResponse,
        )

    async def dividends(
        self,
        *,
        asset_type: Literal["fiagro", "fiinfra", "fif", "fidc", "fip", "other"] | Omit = omit,
        cnpjs: str | Omit = omit,
        end_date: str | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        sort_by: Literal["lastDatePrior", "paymentDate", "declaredDate", "symbol", "rate"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        symbols: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FundDividendsResponse:
        """Dividendos e rendimentos de FIAGRO, FI-Infra, FIF, FIDC e FIP listados.

        Cada
        evento traz data de declaração, data-com (`lastDatePrior`), data ex quando
        existe, data de pagamento, valor por cota e rótulo.

        Use para calcular renda, montar calendários de pagamento e comparar rendimentos.

        Os filtros `startDate` e `endDate` usam `paymentDate`. Sem `symbols` e `cnpjs`,
        a resposta traz todos os fundos.

        FIIs ficam em [dividendos de FIIs](https://brapi.dev/docs/fiis/dividendos). Um
        ticker de FII neste endpoint retorna erro 400.

        O histórico começa no primeiro evento verificável de cada fundo. Não há data
        inicial única. As fontes são documentos da CVM e comunicados de administradores
        e gestores. Eventos de tickers antigos continuam depois de um renome. A brapi
        não estima datas de pagamento. A revisão é mensal.

        Plano Pro.

        Args:
          asset_type: Tipo do fundo.

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
            "/api/v2/funds/dividends",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asset_type": asset_type,
                        "cnpjs": cnpjs,
                        "end_date": end_date,
                        "limit": limit,
                        "page": page,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "start_date": start_date,
                        "symbols": symbols,
                    },
                    fund_dividends_params.FundDividendsParams,
                ),
            ),
            cast_to=FundDividendsResponse,
        )

    async def indicators(
        self,
        *,
        asset_type: Literal["fii", "fiagro", "fiinfra", "fif", "fidc", "fip", "etf", "other"] | Omit = omit,
        cnpjs: str | Omit = omit,
        symbols: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FundIndicatorsResponse:
        """
        Indicadores mais recentes de um ou mais fundos: preço de mercado, valor
        patrimonial por cota (`navPerShare`), a razão entre os dois, patrimônio, ativos
        e número de cotistas.

        Use para comparar preço e valor patrimonial, medir ágio ou deságio e ver o
        tamanho do fundo.

        Informe `symbols` ou `cnpjs`. Se você não tem o identificador, use a
        [lista de fundos](https://brapi.dev/docs/fundos/listagem).

        Plano Pro.

        Args:
          asset_type: Tipo do fundo.

          cnpjs: CNPJs separados por vírgula, até 20, com ou sem pontuação.

          symbols: Tickers separados por vírgula, até 20. Ex.: JURO11,XPCA11.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/funds/indicators",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asset_type": asset_type,
                        "cnpjs": cnpjs,
                        "symbols": symbols,
                    },
                    fund_indicators_params.FundIndicatorsParams,
                ),
            ),
            cast_to=FundIndicatorsResponse,
        )

    async def portfolio(
        self,
        *,
        cnpjs: str | Omit = omit,
        include: str | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        reference_date: str | Omit = omit,
        symbols: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FundPortfolioResponse:
        """Carteira de fundos FI e FIF, do arquivo CDA da CVM.

        As posições vêm agrupadas em
        títulos públicos, cotas de fundos, crédito privado, ativos listados, recebíveis
        e valores a pagar.

        Use para ver onde o fundo investe e qual o peso de cada grupo de ativos.

        Informe `symbols` ou `cnpjs`. Sem `referenceDate`, a resposta traz a carteira
        mais recente.

        Filtre os grupos com `include`: `publicBonds`, `fundHoldings`, `creditAssets`,
        `listedSecurities`, `receivables` e `payables`.

        Posições confidenciais aparecem só no total, em `confidentialSummary`.

        A CVM publica o CDA com meses de atraso. Mostre `referenceDate` junto do dado.

        Plano Pro.

        Args:
          cnpjs: CNPJs separados por vírgula, até 20, com ou sem pontuação.

          include: Grupos de ativos separados por vírgula. Ex.: publicBonds,creditAssets.

          limit: Itens por página.

          page: Número da página, a partir de 1.

          reference_date: Mês de referência no formato YYYY-MM-DD.

          symbols: Tickers separados por vírgula, até 20. Ex.: JURO11,XPCA11.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/funds/portfolio",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cnpjs": cnpjs,
                        "include": include,
                        "limit": limit,
                        "page": page,
                        "reference_date": reference_date,
                        "symbols": symbols,
                    },
                    fund_portfolio_params.FundPortfolioParams,
                ),
            ),
            cast_to=FundPortfolioResponse,
        )

    async def profile(
        self,
        *,
        cnpjs: str | Omit = omit,
        end_date: str | Omit = omit,
        include: str | Omit = omit,
        reference_date: str | Omit = omit,
        start_date: str | Omit = omit,
        symbols: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FundProfileResponse:
        """
        Perfil mensal de fundos FI e FIF, conforme a CVM: distribuição de cotistas,
        medidas de risco, liquidez, concentração e exposição a crédito privado.

        Use para ver se o fundo é de varejo ou institucional e quanto do patrimônio está
        em ativos de baixa liquidez.

        Informe `symbols` ou `cnpjs`. Sem filtro de data, a resposta traz o perfil mais
        recente de cada fundo.

        Plano Pro.

        Args:
          cnpjs: CNPJs separados por vírgula, até 20, com ou sem pontuação.

          end_date: Data final no formato YYYY-MM-DD.

          reference_date: Mês de referência no formato YYYY-MM-DD.

          start_date: Data inicial no formato YYYY-MM-DD.

          symbols: Tickers separados por vírgula, até 20. Ex.: JURO11,XPCA11.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/funds/profile",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cnpjs": cnpjs,
                        "end_date": end_date,
                        "include": include,
                        "reference_date": reference_date,
                        "start_date": start_date,
                        "symbols": symbols,
                    },
                    fund_profile_params.FundProfileParams,
                ),
            ),
            cast_to=FundProfileResponse,
        )


class FundsResourceWithRawResponse:
    def __init__(self, funds: FundsResource) -> None:
        self._funds = funds

        self.list = to_raw_response_wrapper(
            funds.list,
        )
        self.dividends = to_raw_response_wrapper(
            funds.dividends,
        )
        self.indicators = to_raw_response_wrapper(
            funds.indicators,
        )
        self.portfolio = to_raw_response_wrapper(
            funds.portfolio,
        )
        self.profile = to_raw_response_wrapper(
            funds.profile,
        )

    @cached_property
    def nav(self) -> NavResourceWithRawResponse:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return NavResourceWithRawResponse(self._funds.nav)

    @cached_property
    def fiagro(self) -> FiagroResourceWithRawResponse:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return FiagroResourceWithRawResponse(self._funds.fiagro)

    @cached_property
    def fidc(self) -> FidcResourceWithRawResponse:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return FidcResourceWithRawResponse(self._funds.fidc)

    @cached_property
    def fip(self) -> FipResourceWithRawResponse:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return FipResourceWithRawResponse(self._funds.fip)


class AsyncFundsResourceWithRawResponse:
    def __init__(self, funds: AsyncFundsResource) -> None:
        self._funds = funds

        self.list = async_to_raw_response_wrapper(
            funds.list,
        )
        self.dividends = async_to_raw_response_wrapper(
            funds.dividends,
        )
        self.indicators = async_to_raw_response_wrapper(
            funds.indicators,
        )
        self.portfolio = async_to_raw_response_wrapper(
            funds.portfolio,
        )
        self.profile = async_to_raw_response_wrapper(
            funds.profile,
        )

    @cached_property
    def nav(self) -> AsyncNavResourceWithRawResponse:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return AsyncNavResourceWithRawResponse(self._funds.nav)

    @cached_property
    def fiagro(self) -> AsyncFiagroResourceWithRawResponse:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return AsyncFiagroResourceWithRawResponse(self._funds.fiagro)

    @cached_property
    def fidc(self) -> AsyncFidcResourceWithRawResponse:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return AsyncFidcResourceWithRawResponse(self._funds.fidc)

    @cached_property
    def fip(self) -> AsyncFipResourceWithRawResponse:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return AsyncFipResourceWithRawResponse(self._funds.fip)


class FundsResourceWithStreamingResponse:
    def __init__(self, funds: FundsResource) -> None:
        self._funds = funds

        self.list = to_streamed_response_wrapper(
            funds.list,
        )
        self.dividends = to_streamed_response_wrapper(
            funds.dividends,
        )
        self.indicators = to_streamed_response_wrapper(
            funds.indicators,
        )
        self.portfolio = to_streamed_response_wrapper(
            funds.portfolio,
        )
        self.profile = to_streamed_response_wrapper(
            funds.profile,
        )

    @cached_property
    def nav(self) -> NavResourceWithStreamingResponse:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return NavResourceWithStreamingResponse(self._funds.nav)

    @cached_property
    def fiagro(self) -> FiagroResourceWithStreamingResponse:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return FiagroResourceWithStreamingResponse(self._funds.fiagro)

    @cached_property
    def fidc(self) -> FidcResourceWithStreamingResponse:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return FidcResourceWithStreamingResponse(self._funds.fidc)

    @cached_property
    def fip(self) -> FipResourceWithStreamingResponse:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return FipResourceWithStreamingResponse(self._funds.fip)


class AsyncFundsResourceWithStreamingResponse:
    def __init__(self, funds: AsyncFundsResource) -> None:
        self._funds = funds

        self.list = async_to_streamed_response_wrapper(
            funds.list,
        )
        self.dividends = async_to_streamed_response_wrapper(
            funds.dividends,
        )
        self.indicators = async_to_streamed_response_wrapper(
            funds.indicators,
        )
        self.portfolio = async_to_streamed_response_wrapper(
            funds.portfolio,
        )
        self.profile = async_to_streamed_response_wrapper(
            funds.profile,
        )

    @cached_property
    def nav(self) -> AsyncNavResourceWithStreamingResponse:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return AsyncNavResourceWithStreamingResponse(self._funds.nav)

    @cached_property
    def fiagro(self) -> AsyncFiagroResourceWithStreamingResponse:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return AsyncFiagroResourceWithStreamingResponse(self._funds.fiagro)

    @cached_property
    def fidc(self) -> AsyncFidcResourceWithStreamingResponse:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return AsyncFidcResourceWithStreamingResponse(self._funds.fidc)

    @cached_property
    def fip(self) -> AsyncFipResourceWithStreamingResponse:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return AsyncFipResourceWithStreamingResponse(self._funds.fip)
