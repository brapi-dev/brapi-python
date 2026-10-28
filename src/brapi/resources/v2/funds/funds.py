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
    fund_screener_params,
    fund_dividends_params,
    fund_portfolio_params,
    fund_indicators_params,
    fund_screener_cnpj_params,
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
from ....types.v2.fund_screener_response import FundScreenerResponse
from ....types.v2.fund_dividends_response import FundDividendsResponse
from ....types.v2.fund_portfolio_response import FundPortfolioResponse
from ....types.v2.fund_indicators_response import FundIndicatorsResponse
from ....types.v2.fund_screener_cnpj_response import FundScreenerCnpjResponse

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
        etf_category: Literal["fixed-income", "equity", "crypto", "real-estate"] | Omit = omit,
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
        Lista fundos brasileiros com dados disponíveis: FII, FIAGRO, FI-Infra, FIF,
        FIDC, FIP e outros. Cada item traz ticker, CNPJ, tipo, classificações,
        administrador, gestor e os últimos indicadores disponíveis.

        Para ETFs, `etfCategory` separa renda fixa, renda variável, criptoativos e
        imobiliário. Consulte cotações e preços históricos nos endpoints de ações. A
        presença no catálogo de tickers não garante indicadores de fundos.

        `updatedAt` informa a atualização do cadastro. `priceDate` informa a data do
        preço. Consulte `asOfDate` em `/api/v2/funds/indicators` para a data da cota e
        do patrimônio. Os indicadores não têm a mesma frequência das cotações.

        Use para descobrir o tipo de um fundo, achar um CNPJ ou filtrar fundos por tipo.

        Busque por `symbols`, `cnpjs` ou `search`. O `search` procura no ticker, no
        nome, na razão social, no ISIN e no CNPJ.

        Os tipos `fiinfra` e `fiagro` equivalem a `fi-infra` e `fi-agro` no catálogo de
        tickers.

        Nem todo ticker terminado em 11 é FII. `JURO11` é FI-Infra e não responde nos
        [endpoints de FIIs](https://brapi.dev/docs/fiis).

        `sortBy` aceita `symbol`, `name`, `assetType`, `price`, `navPerShare`,
        `priceToNav`, `totalInvestors` e `updatedAt`. O padrão é `updatedAt`.

        Plano Pro.

        Args:
          asset_type: Tipo do fundo.

          cnpjs: CNPJs separados por vírgula, até 20, com ou sem pontuação.

          etf_category: Categoria do ETF. Só traz ETFs.

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
                        "etf_category": etf_category,
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

        `priceDate` é a data do último fechamento. `asOfDate` é a data do informe com a
        cota e o patrimônio, que costuma chegar dias depois do pregão.

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

    def screener(
        self,
        *,
        asset_type: Literal["fii", "fiagro", "fiinfra", "etf", "fidc", "fip", "fif"] | Omit = omit,
        average_daily_traded_value_max: float | Omit = omit,
        average_daily_traded_value_min: float | Omit = omit,
        change_percent_max: float | Omit = omit,
        change_percent_min: float | Omit = omit,
        dividend_yield_max: float | Omit = omit,
        dividend_yield_min: float | Omit = omit,
        equity_max: float | Omit = omit,
        equity_min: float | Omit = omit,
        etf_category: Literal["fixed-income", "equity", "crypto", "real-estate"] | Omit = omit,
        income_months12m_max: float | Omit = omit,
        income_months12m_min: float | Omit = omit,
        last_dividend_max: float | Omit = omit,
        last_dividend_min: float | Omit = omit,
        last_dividend_yield_max: float | Omit = omit,
        last_dividend_yield_min: float | Omit = omit,
        last_price_max: float | Omit = omit,
        last_price_min: float | Omit = omit,
        limit: int | Omit = omit,
        market_cap_max: float | Omit = omit,
        market_cap_min: float | Omit = omit,
        nav_per_share_max: float | Omit = omit,
        nav_per_share_min: float | Omit = omit,
        page: int | Omit = omit,
        price_change12m_max: float | Omit = omit,
        price_change12m_min: float | Omit = omit,
        price_to_nav_max: float | Omit = omit,
        price_to_nav_min: float | Omit = omit,
        search: str | Omit = omit,
        segment: str | Omit = omit,
        segment_type: Literal["tijolo", "papel", "hibrido", "fof"] | Omit = omit,
        sort_by: Literal[
            "symbol",
            "name",
            "lastPrice",
            "changePercent",
            "volume",
            "averageDailyTradedValue",
            "marketCap",
            "dividendYield",
            "lastDividend",
            "lastDividendYield",
            "incomeMonths12m",
            "navPerShare",
            "priceToNav",
            "equity",
            "totalInvestors",
            "priceChange12m",
            "totalFeePercent",
        ]
        | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        total_fee_percent_max: float | Omit = omit,
        total_fee_percent_min: float | Omit = omit,
        total_investors_max: float | Omit = omit,
        total_investors_min: float | Omit = omit,
        volume_max: float | Omit = omit,
        volume_min: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FundScreenerResponse:
        """
        Filtra e ordena os fundos negociados na B3 (FIIs, Fiagros, FI-Infra, ETFs, FIDCs
        e FIPs) por preço, rendimentos, P/VP, liquidez, patrimônio e cotistas. Uma
        chamada percorre todos os fundos.

        `assetType` escolhe o tipo de fundo. Para FIIs, `segmentType` separa tijolo,
        papel, fundos de fundos e híbridos, e `segment` usa o segmento do cadastro da
        CVM. Para ETFs, `etfCategory` separa renda fixa, renda variável, cripto e
        imobiliário.

        Cada indicador aceita `{chave}Min` e `{chave}Max`. Os limites são inclusivos e
        usam a mesma unidade da resposta: 10% é `0.1`. Um filtro remove os fundos sem o
        dado. Na ordenação, os nulos ficam no fim.

        Exemplos:

        - FIIs de papel com dividend yield de pelo menos 12% e P/VP até 0,95:
          `?assetType=fii&segmentType=papel&dividendYieldMin=0.12&priceToNavMax=0.95&sortBy=dividendYield`
        - ETFs de renda fixa pela menor taxa:
          `?assetType=etf&etfCategory=fixed-income&sortBy=totalFeePercent&sortOrder=asc`

        `dividendYield` soma só os rendimentos dos últimos 12 meses pela data-com, sem
        amortizações, e divide pelo último preço. `priceToNav` usa o último preço e o
        valor patrimonial por cota do último informe. `averageDailyTradedValue` divide o
        valor negociado nos últimos 30 dias pelos pregões do período.

        Plano Pro.

        | Indicador                  | Chave                     | Unidade                    |
        | -------------------------- | ------------------------- | -------------------------- |
        | Preço                      | `lastPrice`               | reais                      |
        | Variação no dia            | `changePercent`           | porcentagem (2.81 = 2,81%) |
        | Volume                     | `volume`                  | quantidade                 |
        | Liquidez diária            | `averageDailyTradedValue` | reais                      |
        | Valor de mercado           | `marketCap`               | reais                      |
        | Dividend yield 12m         | `dividendYield`           | fração (0.06 = 6%)         |
        | Último rendimento          | `lastDividend`            | reais                      |
        | Yield do último rendimento | `lastDividendYield`       | fração (0.06 = 6%)         |
        | Meses com rendimento       | `incomeMonths12m`         | quantidade                 |
        | Valor patrimonial/cota     | `navPerShare`             | reais                      |
        | P/VP                       | `priceToNav`              | múltiplo                   |
        | Patrimônio líquido         | `equity`                  | reais                      |
        | Cotistas                   | `totalInvestors`          | quantidade                 |
        | Variação em 12 meses       | `priceChange12m`          | fração (0.06 = 6%)         |
        | Taxa total                 | `totalFeePercent`         | porcentagem (2.81 = 2,81%) |

        Args:
          asset_type: Tipo do fundo: fii, fiagro, fiinfra, etf, fidc, fip ou fif. Sem ele, todos os
              fundos listados.

          average_daily_traded_value_max: Liquidez diária: valor máximo, inclusive. Unidade: reais.

          average_daily_traded_value_min: Liquidez diária: valor mínimo, inclusive. Unidade: reais.

          change_percent_max: Variação no dia: valor máximo, inclusive. Unidade: porcentagem (2.81 = 2,81%).

          change_percent_min: Variação no dia: valor mínimo, inclusive. Unidade: porcentagem (2.81 = 2,81%).

          dividend_yield_max: Dividend yield 12m: valor máximo, inclusive. Unidade: fração (0.06 = 6%).

          dividend_yield_min: Dividend yield 12m: valor mínimo, inclusive. Unidade: fração (0.06 = 6%).

          equity_max: Patrimônio líquido: valor máximo, inclusive. Unidade: reais.

          equity_min: Patrimônio líquido: valor mínimo, inclusive. Unidade: reais.

          etf_category: Categoria do ETF pela lista da bolsa: fixed-income, equity, crypto ou
              real-estate.

          income_months12m_max: Meses com rendimento: valor máximo, inclusive. Unidade: quantidade.

          income_months12m_min: Meses com rendimento: valor mínimo, inclusive. Unidade: quantidade.

          last_dividend_max: Último rendimento: valor máximo, inclusive. Unidade: reais.

          last_dividend_min: Último rendimento: valor mínimo, inclusive. Unidade: reais.

          last_dividend_yield_max: Yield do último rendimento: valor máximo, inclusive. Unidade: fração (0.06 =
              6%).

          last_dividend_yield_min: Yield do último rendimento: valor mínimo, inclusive. Unidade: fração (0.06 =
              6%).

          last_price_max: Preço: valor máximo, inclusive. Unidade: reais.

          last_price_min: Preço: valor mínimo, inclusive. Unidade: reais.

          limit: Itens por página. Máximo: 200.

          market_cap_max: Valor de mercado: valor máximo, inclusive. Unidade: reais.

          market_cap_min: Valor de mercado: valor mínimo, inclusive. Unidade: reais.

          nav_per_share_max: Valor patrimonial/cota: valor máximo, inclusive. Unidade: reais.

          nav_per_share_min: Valor patrimonial/cota: valor mínimo, inclusive. Unidade: reais.

          page: Número da página. Começa em 1.

          price_change12m_max: Variação em 12 meses: valor máximo, inclusive. Unidade: fração (0.06 = 6%).

          price_change12m_min: Variação em 12 meses: valor mínimo, inclusive. Unidade: fração (0.06 = 6%).

          price_to_nav_max: P/VP: valor máximo, inclusive. Unidade: múltiplo.

          price_to_nav_min: P/VP: valor mínimo, inclusive. Unidade: múltiplo.

          search: Parte do ticker ou do nome do fundo.

          segment: Segmento do FII no cadastro da CVM, como Logística, Shoppings, Escritórios ou
              Títulos e Val. Mob. Nome exato, sem diferença de maiúsculas.

          segment_type: Tipo do FII pelo último informe: tijolo (imóveis), papel (CRI, LCI e títulos),
              fof (cotas de outros FIIs) ou hibrido.

          sort_by:
              Campo de ordenação: uma chave de métrica, `symbol` ou `name`. Padrão:
              `averageDailyTradedValue`. Valores nulos ficam no fim.

          sort_order: Ordem. Padrão: `desc`.

          total_fee_percent_max: Taxa total: valor máximo, inclusive. Unidade: porcentagem (2.81 = 2,81%).

          total_fee_percent_min: Taxa total: valor mínimo, inclusive. Unidade: porcentagem (2.81 = 2,81%).

          total_investors_max: Cotistas: valor máximo, inclusive. Unidade: quantidade.

          total_investors_min: Cotistas: valor mínimo, inclusive. Unidade: quantidade.

          volume_max: Volume: valor máximo, inclusive. Unidade: quantidade.

          volume_min: Volume: valor mínimo, inclusive. Unidade: quantidade.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/funds/screener",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asset_type": asset_type,
                        "average_daily_traded_value_max": average_daily_traded_value_max,
                        "average_daily_traded_value_min": average_daily_traded_value_min,
                        "change_percent_max": change_percent_max,
                        "change_percent_min": change_percent_min,
                        "dividend_yield_max": dividend_yield_max,
                        "dividend_yield_min": dividend_yield_min,
                        "equity_max": equity_max,
                        "equity_min": equity_min,
                        "etf_category": etf_category,
                        "income_months12m_max": income_months12m_max,
                        "income_months12m_min": income_months12m_min,
                        "last_dividend_max": last_dividend_max,
                        "last_dividend_min": last_dividend_min,
                        "last_dividend_yield_max": last_dividend_yield_max,
                        "last_dividend_yield_min": last_dividend_yield_min,
                        "last_price_max": last_price_max,
                        "last_price_min": last_price_min,
                        "limit": limit,
                        "market_cap_max": market_cap_max,
                        "market_cap_min": market_cap_min,
                        "nav_per_share_max": nav_per_share_max,
                        "nav_per_share_min": nav_per_share_min,
                        "page": page,
                        "price_change12m_max": price_change12m_max,
                        "price_change12m_min": price_change12m_min,
                        "price_to_nav_max": price_to_nav_max,
                        "price_to_nav_min": price_to_nav_min,
                        "search": search,
                        "segment": segment,
                        "segment_type": segment_type,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "total_fee_percent_max": total_fee_percent_max,
                        "total_fee_percent_min": total_fee_percent_min,
                        "total_investors_max": total_investors_max,
                        "total_investors_min": total_investors_min,
                        "volume_max": volume_max,
                        "volume_min": volume_min,
                    },
                    fund_screener_params.FundScreenerParams,
                ),
            ),
            cast_to=FundScreenerResponse,
        )

    def screener_cnpj(
        self,
        *,
        anbima_classification: str | Omit = omit,
        classification: Literal["renda-fixa", "multimercado", "acoes", "cambial", "fmp-fgts"] | Omit = omit,
        equity_max: float | Omit = omit,
        equity_min: float | Omit = omit,
        limit: int | Omit = omit,
        manager: str | Omit = omit,
        nav_per_share_max: float | Omit = omit,
        nav_per_share_min: float | Omit = omit,
        net_flow1m_max: float | Omit = omit,
        net_flow1m_min: float | Omit = omit,
        page: int | Omit = omit,
        return12m_max: float | Omit = omit,
        return12m_min: float | Omit = omit,
        return1m_max: float | Omit = omit,
        return1m_min: float | Omit = omit,
        return36m_max: float | Omit = omit,
        return36m_min: float | Omit = omit,
        return_day_max: float | Omit = omit,
        return_day_min: float | Omit = omit,
        return_ytd_max: float | Omit = omit,
        return_ytd_min: float | Omit = omit,
        search: str | Omit = omit,
        sort_by: Literal[
            "name",
            "cnpj",
            "navPerShare",
            "returnDay",
            "return1m",
            "returnYtd",
            "return12m",
            "return36m",
            "equity",
            "totalInvestors",
            "netFlow1m",
        ]
        | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        total_investors_max: float | Omit = omit,
        total_investors_min: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FundScreenerCnpjResponse:
        """
        Filtra e ordena os fundos de investimento sem ticker na B3, identificados pelo
        CNPJ, por rentabilidade, patrimônio, cotistas e captação. Uma chamada percorre
        todos os fundos.

        Entram só os fundos sem ticker na B3, com situação "Em Funcionamento Normal" na
        CVM, que enviaram o informe diário nos últimos 20 dias. Para os fundos
        negociados na bolsa, use `/api/v2/funds/screener`.

        Os dados vêm do informe diário que os fundos enviam à CVM. Ele costuma chegar
        com 1 a 3 dias úteis de atraso: `navDate` mostra a data do último informe de
        cada fundo.

        As rentabilidades são a variação da cota: brutas de imposto de renda e líquidas
        de taxas. Uma rentabilidade é nula quando falta a cota inicial ou quando a cota
        muda mais de 10 vezes no período, o que indica desdobramento ou grupamento de
        cotas.

        `search` busca no nome e na razão social. Números, com ou sem pontuação, buscam
        o início do CNPJ. `classification` usa a classe da CVM, `anbimaClassification`
        busca parte da classificação ANBIMA e `manager` busca parte do nome do gestor.

        Cada indicador aceita `{chave}Min` e `{chave}Max`. Os limites são inclusivos e
        usam a mesma unidade da resposta: 10% é `0.1`. Um filtro remove os fundos sem o
        dado. Na ordenação, os nulos ficam no fim.

        Exemplos:

        - Fundos de previdência de renda fixa pela maior rentabilidade em 12 meses:
          `?classification=renda-fixa&anbimaClassification=Previdência&sortBy=return12m`
        - Multimercados com pelo menos R$ 100 milhões e 1.000 cotistas:
          `?classification=multimercado&equityMin=100000000&totalInvestorsMin=1000`
        - Fundos cujo CNPJ começa com 12.345.678: `?search=12.345.678`

        Plano Pro.

        | Indicador                 | Chave            | Unidade            |
        | ------------------------- | ---------------- | ------------------ |
        | Valor da cota             | `navPerShare`    | reais              |
        | Variação no dia           | `returnDay`      | fração (0.06 = 6%) |
        | Rentabilidade em 1 mês    | `return1m`       | fração (0.06 = 6%) |
        | Rentabilidade no ano      | `returnYtd`      | fração (0.06 = 6%) |
        | Rentabilidade em 12 meses | `return12m`      | fração (0.06 = 6%) |
        | Rentabilidade em 36 meses | `return36m`      | fração (0.06 = 6%) |
        | Patrimônio líquido        | `equity`         | reais              |
        | Cotistas                  | `totalInvestors` | quantidade         |
        | Captação líquida em 1 mês | `netFlow1m`      | reais              |

        Args:
          anbima_classification:
              Parte da classificação ANBIMA, sem diferença de maiúsculas e acentos. Exemplos:
              Previdência, Exterior, Crédito Livre.

          classification: Classe do fundo na CVM: renda-fixa, multimercado, acoes, cambial ou fmp-fgts.

          equity_max: Patrimônio líquido: valor máximo, inclusive. Unidade: reais.

          equity_min: Patrimônio líquido: valor mínimo, inclusive. Unidade: reais.

          limit: Itens por página. Máximo: 200.

          manager: Parte do nome do gestor, sem diferença de maiúsculas e acentos.

          nav_per_share_max: Valor da cota: valor máximo, inclusive. Unidade: reais.

          nav_per_share_min: Valor da cota: valor mínimo, inclusive. Unidade: reais.

          net_flow1m_max: Captação líquida em 1 mês: valor máximo, inclusive. Unidade: reais.

          net_flow1m_min: Captação líquida em 1 mês: valor mínimo, inclusive. Unidade: reais.

          page: Número da página. Começa em 1.

          return12m_max: Rentabilidade em 12 meses: valor máximo, inclusive. Unidade: fração (0.06 = 6%).

          return12m_min: Rentabilidade em 12 meses: valor mínimo, inclusive. Unidade: fração (0.06 = 6%).

          return1m_max: Rentabilidade em 1 mês: valor máximo, inclusive. Unidade: fração (0.06 = 6%).

          return1m_min: Rentabilidade em 1 mês: valor mínimo, inclusive. Unidade: fração (0.06 = 6%).

          return36m_max: Rentabilidade em 36 meses: valor máximo, inclusive. Unidade: fração (0.06 = 6%).

          return36m_min: Rentabilidade em 36 meses: valor mínimo, inclusive. Unidade: fração (0.06 = 6%).

          return_day_max: Variação no dia: valor máximo, inclusive. Unidade: fração (0.06 = 6%).

          return_day_min: Variação no dia: valor mínimo, inclusive. Unidade: fração (0.06 = 6%).

          return_ytd_max: Rentabilidade no ano: valor máximo, inclusive. Unidade: fração (0.06 = 6%).

          return_ytd_min: Rentabilidade no ano: valor mínimo, inclusive. Unidade: fração (0.06 = 6%).

          search: Parte do nome ou da razão social do fundo, sem diferença de maiúsculas e
              acentos. Números, com ou sem pontuação, buscam o início do CNPJ.

          sort_by: Campo de ordenação: uma chave de indicador, `name` ou `cnpj`. Padrão: `equity`.
              Valores nulos ficam no fim.

          sort_order: Ordem. Padrão: `desc`.

          total_investors_max: Cotistas: valor máximo, inclusive. Unidade: quantidade.

          total_investors_min: Cotistas: valor mínimo, inclusive. Unidade: quantidade.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/funds/screener/cnpj",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "anbima_classification": anbima_classification,
                        "classification": classification,
                        "equity_max": equity_max,
                        "equity_min": equity_min,
                        "limit": limit,
                        "manager": manager,
                        "nav_per_share_max": nav_per_share_max,
                        "nav_per_share_min": nav_per_share_min,
                        "net_flow1m_max": net_flow1m_max,
                        "net_flow1m_min": net_flow1m_min,
                        "page": page,
                        "return12m_max": return12m_max,
                        "return12m_min": return12m_min,
                        "return1m_max": return1m_max,
                        "return1m_min": return1m_min,
                        "return36m_max": return36m_max,
                        "return36m_min": return36m_min,
                        "return_day_max": return_day_max,
                        "return_day_min": return_day_min,
                        "return_ytd_max": return_ytd_max,
                        "return_ytd_min": return_ytd_min,
                        "search": search,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "total_investors_max": total_investors_max,
                        "total_investors_min": total_investors_min,
                    },
                    fund_screener_cnpj_params.FundScreenerCnpjParams,
                ),
            ),
            cast_to=FundScreenerCnpjResponse,
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
        etf_category: Literal["fixed-income", "equity", "crypto", "real-estate"] | Omit = omit,
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
        Lista fundos brasileiros com dados disponíveis: FII, FIAGRO, FI-Infra, FIF,
        FIDC, FIP e outros. Cada item traz ticker, CNPJ, tipo, classificações,
        administrador, gestor e os últimos indicadores disponíveis.

        Para ETFs, `etfCategory` separa renda fixa, renda variável, criptoativos e
        imobiliário. Consulte cotações e preços históricos nos endpoints de ações. A
        presença no catálogo de tickers não garante indicadores de fundos.

        `updatedAt` informa a atualização do cadastro. `priceDate` informa a data do
        preço. Consulte `asOfDate` em `/api/v2/funds/indicators` para a data da cota e
        do patrimônio. Os indicadores não têm a mesma frequência das cotações.

        Use para descobrir o tipo de um fundo, achar um CNPJ ou filtrar fundos por tipo.

        Busque por `symbols`, `cnpjs` ou `search`. O `search` procura no ticker, no
        nome, na razão social, no ISIN e no CNPJ.

        Os tipos `fiinfra` e `fiagro` equivalem a `fi-infra` e `fi-agro` no catálogo de
        tickers.

        Nem todo ticker terminado em 11 é FII. `JURO11` é FI-Infra e não responde nos
        [endpoints de FIIs](https://brapi.dev/docs/fiis).

        `sortBy` aceita `symbol`, `name`, `assetType`, `price`, `navPerShare`,
        `priceToNav`, `totalInvestors` e `updatedAt`. O padrão é `updatedAt`.

        Plano Pro.

        Args:
          asset_type: Tipo do fundo.

          cnpjs: CNPJs separados por vírgula, até 20, com ou sem pontuação.

          etf_category: Categoria do ETF. Só traz ETFs.

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
                        "etf_category": etf_category,
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

        `priceDate` é a data do último fechamento. `asOfDate` é a data do informe com a
        cota e o patrimônio, que costuma chegar dias depois do pregão.

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

    async def screener(
        self,
        *,
        asset_type: Literal["fii", "fiagro", "fiinfra", "etf", "fidc", "fip", "fif"] | Omit = omit,
        average_daily_traded_value_max: float | Omit = omit,
        average_daily_traded_value_min: float | Omit = omit,
        change_percent_max: float | Omit = omit,
        change_percent_min: float | Omit = omit,
        dividend_yield_max: float | Omit = omit,
        dividend_yield_min: float | Omit = omit,
        equity_max: float | Omit = omit,
        equity_min: float | Omit = omit,
        etf_category: Literal["fixed-income", "equity", "crypto", "real-estate"] | Omit = omit,
        income_months12m_max: float | Omit = omit,
        income_months12m_min: float | Omit = omit,
        last_dividend_max: float | Omit = omit,
        last_dividend_min: float | Omit = omit,
        last_dividend_yield_max: float | Omit = omit,
        last_dividend_yield_min: float | Omit = omit,
        last_price_max: float | Omit = omit,
        last_price_min: float | Omit = omit,
        limit: int | Omit = omit,
        market_cap_max: float | Omit = omit,
        market_cap_min: float | Omit = omit,
        nav_per_share_max: float | Omit = omit,
        nav_per_share_min: float | Omit = omit,
        page: int | Omit = omit,
        price_change12m_max: float | Omit = omit,
        price_change12m_min: float | Omit = omit,
        price_to_nav_max: float | Omit = omit,
        price_to_nav_min: float | Omit = omit,
        search: str | Omit = omit,
        segment: str | Omit = omit,
        segment_type: Literal["tijolo", "papel", "hibrido", "fof"] | Omit = omit,
        sort_by: Literal[
            "symbol",
            "name",
            "lastPrice",
            "changePercent",
            "volume",
            "averageDailyTradedValue",
            "marketCap",
            "dividendYield",
            "lastDividend",
            "lastDividendYield",
            "incomeMonths12m",
            "navPerShare",
            "priceToNav",
            "equity",
            "totalInvestors",
            "priceChange12m",
            "totalFeePercent",
        ]
        | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        total_fee_percent_max: float | Omit = omit,
        total_fee_percent_min: float | Omit = omit,
        total_investors_max: float | Omit = omit,
        total_investors_min: float | Omit = omit,
        volume_max: float | Omit = omit,
        volume_min: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FundScreenerResponse:
        """
        Filtra e ordena os fundos negociados na B3 (FIIs, Fiagros, FI-Infra, ETFs, FIDCs
        e FIPs) por preço, rendimentos, P/VP, liquidez, patrimônio e cotistas. Uma
        chamada percorre todos os fundos.

        `assetType` escolhe o tipo de fundo. Para FIIs, `segmentType` separa tijolo,
        papel, fundos de fundos e híbridos, e `segment` usa o segmento do cadastro da
        CVM. Para ETFs, `etfCategory` separa renda fixa, renda variável, cripto e
        imobiliário.

        Cada indicador aceita `{chave}Min` e `{chave}Max`. Os limites são inclusivos e
        usam a mesma unidade da resposta: 10% é `0.1`. Um filtro remove os fundos sem o
        dado. Na ordenação, os nulos ficam no fim.

        Exemplos:

        - FIIs de papel com dividend yield de pelo menos 12% e P/VP até 0,95:
          `?assetType=fii&segmentType=papel&dividendYieldMin=0.12&priceToNavMax=0.95&sortBy=dividendYield`
        - ETFs de renda fixa pela menor taxa:
          `?assetType=etf&etfCategory=fixed-income&sortBy=totalFeePercent&sortOrder=asc`

        `dividendYield` soma só os rendimentos dos últimos 12 meses pela data-com, sem
        amortizações, e divide pelo último preço. `priceToNav` usa o último preço e o
        valor patrimonial por cota do último informe. `averageDailyTradedValue` divide o
        valor negociado nos últimos 30 dias pelos pregões do período.

        Plano Pro.

        | Indicador                  | Chave                     | Unidade                    |
        | -------------------------- | ------------------------- | -------------------------- |
        | Preço                      | `lastPrice`               | reais                      |
        | Variação no dia            | `changePercent`           | porcentagem (2.81 = 2,81%) |
        | Volume                     | `volume`                  | quantidade                 |
        | Liquidez diária            | `averageDailyTradedValue` | reais                      |
        | Valor de mercado           | `marketCap`               | reais                      |
        | Dividend yield 12m         | `dividendYield`           | fração (0.06 = 6%)         |
        | Último rendimento          | `lastDividend`            | reais                      |
        | Yield do último rendimento | `lastDividendYield`       | fração (0.06 = 6%)         |
        | Meses com rendimento       | `incomeMonths12m`         | quantidade                 |
        | Valor patrimonial/cota     | `navPerShare`             | reais                      |
        | P/VP                       | `priceToNav`              | múltiplo                   |
        | Patrimônio líquido         | `equity`                  | reais                      |
        | Cotistas                   | `totalInvestors`          | quantidade                 |
        | Variação em 12 meses       | `priceChange12m`          | fração (0.06 = 6%)         |
        | Taxa total                 | `totalFeePercent`         | porcentagem (2.81 = 2,81%) |

        Args:
          asset_type: Tipo do fundo: fii, fiagro, fiinfra, etf, fidc, fip ou fif. Sem ele, todos os
              fundos listados.

          average_daily_traded_value_max: Liquidez diária: valor máximo, inclusive. Unidade: reais.

          average_daily_traded_value_min: Liquidez diária: valor mínimo, inclusive. Unidade: reais.

          change_percent_max: Variação no dia: valor máximo, inclusive. Unidade: porcentagem (2.81 = 2,81%).

          change_percent_min: Variação no dia: valor mínimo, inclusive. Unidade: porcentagem (2.81 = 2,81%).

          dividend_yield_max: Dividend yield 12m: valor máximo, inclusive. Unidade: fração (0.06 = 6%).

          dividend_yield_min: Dividend yield 12m: valor mínimo, inclusive. Unidade: fração (0.06 = 6%).

          equity_max: Patrimônio líquido: valor máximo, inclusive. Unidade: reais.

          equity_min: Patrimônio líquido: valor mínimo, inclusive. Unidade: reais.

          etf_category: Categoria do ETF pela lista da bolsa: fixed-income, equity, crypto ou
              real-estate.

          income_months12m_max: Meses com rendimento: valor máximo, inclusive. Unidade: quantidade.

          income_months12m_min: Meses com rendimento: valor mínimo, inclusive. Unidade: quantidade.

          last_dividend_max: Último rendimento: valor máximo, inclusive. Unidade: reais.

          last_dividend_min: Último rendimento: valor mínimo, inclusive. Unidade: reais.

          last_dividend_yield_max: Yield do último rendimento: valor máximo, inclusive. Unidade: fração (0.06 =
              6%).

          last_dividend_yield_min: Yield do último rendimento: valor mínimo, inclusive. Unidade: fração (0.06 =
              6%).

          last_price_max: Preço: valor máximo, inclusive. Unidade: reais.

          last_price_min: Preço: valor mínimo, inclusive. Unidade: reais.

          limit: Itens por página. Máximo: 200.

          market_cap_max: Valor de mercado: valor máximo, inclusive. Unidade: reais.

          market_cap_min: Valor de mercado: valor mínimo, inclusive. Unidade: reais.

          nav_per_share_max: Valor patrimonial/cota: valor máximo, inclusive. Unidade: reais.

          nav_per_share_min: Valor patrimonial/cota: valor mínimo, inclusive. Unidade: reais.

          page: Número da página. Começa em 1.

          price_change12m_max: Variação em 12 meses: valor máximo, inclusive. Unidade: fração (0.06 = 6%).

          price_change12m_min: Variação em 12 meses: valor mínimo, inclusive. Unidade: fração (0.06 = 6%).

          price_to_nav_max: P/VP: valor máximo, inclusive. Unidade: múltiplo.

          price_to_nav_min: P/VP: valor mínimo, inclusive. Unidade: múltiplo.

          search: Parte do ticker ou do nome do fundo.

          segment: Segmento do FII no cadastro da CVM, como Logística, Shoppings, Escritórios ou
              Títulos e Val. Mob. Nome exato, sem diferença de maiúsculas.

          segment_type: Tipo do FII pelo último informe: tijolo (imóveis), papel (CRI, LCI e títulos),
              fof (cotas de outros FIIs) ou hibrido.

          sort_by:
              Campo de ordenação: uma chave de métrica, `symbol` ou `name`. Padrão:
              `averageDailyTradedValue`. Valores nulos ficam no fim.

          sort_order: Ordem. Padrão: `desc`.

          total_fee_percent_max: Taxa total: valor máximo, inclusive. Unidade: porcentagem (2.81 = 2,81%).

          total_fee_percent_min: Taxa total: valor mínimo, inclusive. Unidade: porcentagem (2.81 = 2,81%).

          total_investors_max: Cotistas: valor máximo, inclusive. Unidade: quantidade.

          total_investors_min: Cotistas: valor mínimo, inclusive. Unidade: quantidade.

          volume_max: Volume: valor máximo, inclusive. Unidade: quantidade.

          volume_min: Volume: valor mínimo, inclusive. Unidade: quantidade.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/funds/screener",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asset_type": asset_type,
                        "average_daily_traded_value_max": average_daily_traded_value_max,
                        "average_daily_traded_value_min": average_daily_traded_value_min,
                        "change_percent_max": change_percent_max,
                        "change_percent_min": change_percent_min,
                        "dividend_yield_max": dividend_yield_max,
                        "dividend_yield_min": dividend_yield_min,
                        "equity_max": equity_max,
                        "equity_min": equity_min,
                        "etf_category": etf_category,
                        "income_months12m_max": income_months12m_max,
                        "income_months12m_min": income_months12m_min,
                        "last_dividend_max": last_dividend_max,
                        "last_dividend_min": last_dividend_min,
                        "last_dividend_yield_max": last_dividend_yield_max,
                        "last_dividend_yield_min": last_dividend_yield_min,
                        "last_price_max": last_price_max,
                        "last_price_min": last_price_min,
                        "limit": limit,
                        "market_cap_max": market_cap_max,
                        "market_cap_min": market_cap_min,
                        "nav_per_share_max": nav_per_share_max,
                        "nav_per_share_min": nav_per_share_min,
                        "page": page,
                        "price_change12m_max": price_change12m_max,
                        "price_change12m_min": price_change12m_min,
                        "price_to_nav_max": price_to_nav_max,
                        "price_to_nav_min": price_to_nav_min,
                        "search": search,
                        "segment": segment,
                        "segment_type": segment_type,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "total_fee_percent_max": total_fee_percent_max,
                        "total_fee_percent_min": total_fee_percent_min,
                        "total_investors_max": total_investors_max,
                        "total_investors_min": total_investors_min,
                        "volume_max": volume_max,
                        "volume_min": volume_min,
                    },
                    fund_screener_params.FundScreenerParams,
                ),
            ),
            cast_to=FundScreenerResponse,
        )

    async def screener_cnpj(
        self,
        *,
        anbima_classification: str | Omit = omit,
        classification: Literal["renda-fixa", "multimercado", "acoes", "cambial", "fmp-fgts"] | Omit = omit,
        equity_max: float | Omit = omit,
        equity_min: float | Omit = omit,
        limit: int | Omit = omit,
        manager: str | Omit = omit,
        nav_per_share_max: float | Omit = omit,
        nav_per_share_min: float | Omit = omit,
        net_flow1m_max: float | Omit = omit,
        net_flow1m_min: float | Omit = omit,
        page: int | Omit = omit,
        return12m_max: float | Omit = omit,
        return12m_min: float | Omit = omit,
        return1m_max: float | Omit = omit,
        return1m_min: float | Omit = omit,
        return36m_max: float | Omit = omit,
        return36m_min: float | Omit = omit,
        return_day_max: float | Omit = omit,
        return_day_min: float | Omit = omit,
        return_ytd_max: float | Omit = omit,
        return_ytd_min: float | Omit = omit,
        search: str | Omit = omit,
        sort_by: Literal[
            "name",
            "cnpj",
            "navPerShare",
            "returnDay",
            "return1m",
            "returnYtd",
            "return12m",
            "return36m",
            "equity",
            "totalInvestors",
            "netFlow1m",
        ]
        | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        total_investors_max: float | Omit = omit,
        total_investors_min: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FundScreenerCnpjResponse:
        """
        Filtra e ordena os fundos de investimento sem ticker na B3, identificados pelo
        CNPJ, por rentabilidade, patrimônio, cotistas e captação. Uma chamada percorre
        todos os fundos.

        Entram só os fundos sem ticker na B3, com situação "Em Funcionamento Normal" na
        CVM, que enviaram o informe diário nos últimos 20 dias. Para os fundos
        negociados na bolsa, use `/api/v2/funds/screener`.

        Os dados vêm do informe diário que os fundos enviam à CVM. Ele costuma chegar
        com 1 a 3 dias úteis de atraso: `navDate` mostra a data do último informe de
        cada fundo.

        As rentabilidades são a variação da cota: brutas de imposto de renda e líquidas
        de taxas. Uma rentabilidade é nula quando falta a cota inicial ou quando a cota
        muda mais de 10 vezes no período, o que indica desdobramento ou grupamento de
        cotas.

        `search` busca no nome e na razão social. Números, com ou sem pontuação, buscam
        o início do CNPJ. `classification` usa a classe da CVM, `anbimaClassification`
        busca parte da classificação ANBIMA e `manager` busca parte do nome do gestor.

        Cada indicador aceita `{chave}Min` e `{chave}Max`. Os limites são inclusivos e
        usam a mesma unidade da resposta: 10% é `0.1`. Um filtro remove os fundos sem o
        dado. Na ordenação, os nulos ficam no fim.

        Exemplos:

        - Fundos de previdência de renda fixa pela maior rentabilidade em 12 meses:
          `?classification=renda-fixa&anbimaClassification=Previdência&sortBy=return12m`
        - Multimercados com pelo menos R$ 100 milhões e 1.000 cotistas:
          `?classification=multimercado&equityMin=100000000&totalInvestorsMin=1000`
        - Fundos cujo CNPJ começa com 12.345.678: `?search=12.345.678`

        Plano Pro.

        | Indicador                 | Chave            | Unidade            |
        | ------------------------- | ---------------- | ------------------ |
        | Valor da cota             | `navPerShare`    | reais              |
        | Variação no dia           | `returnDay`      | fração (0.06 = 6%) |
        | Rentabilidade em 1 mês    | `return1m`       | fração (0.06 = 6%) |
        | Rentabilidade no ano      | `returnYtd`      | fração (0.06 = 6%) |
        | Rentabilidade em 12 meses | `return12m`      | fração (0.06 = 6%) |
        | Rentabilidade em 36 meses | `return36m`      | fração (0.06 = 6%) |
        | Patrimônio líquido        | `equity`         | reais              |
        | Cotistas                  | `totalInvestors` | quantidade         |
        | Captação líquida em 1 mês | `netFlow1m`      | reais              |

        Args:
          anbima_classification:
              Parte da classificação ANBIMA, sem diferença de maiúsculas e acentos. Exemplos:
              Previdência, Exterior, Crédito Livre.

          classification: Classe do fundo na CVM: renda-fixa, multimercado, acoes, cambial ou fmp-fgts.

          equity_max: Patrimônio líquido: valor máximo, inclusive. Unidade: reais.

          equity_min: Patrimônio líquido: valor mínimo, inclusive. Unidade: reais.

          limit: Itens por página. Máximo: 200.

          manager: Parte do nome do gestor, sem diferença de maiúsculas e acentos.

          nav_per_share_max: Valor da cota: valor máximo, inclusive. Unidade: reais.

          nav_per_share_min: Valor da cota: valor mínimo, inclusive. Unidade: reais.

          net_flow1m_max: Captação líquida em 1 mês: valor máximo, inclusive. Unidade: reais.

          net_flow1m_min: Captação líquida em 1 mês: valor mínimo, inclusive. Unidade: reais.

          page: Número da página. Começa em 1.

          return12m_max: Rentabilidade em 12 meses: valor máximo, inclusive. Unidade: fração (0.06 = 6%).

          return12m_min: Rentabilidade em 12 meses: valor mínimo, inclusive. Unidade: fração (0.06 = 6%).

          return1m_max: Rentabilidade em 1 mês: valor máximo, inclusive. Unidade: fração (0.06 = 6%).

          return1m_min: Rentabilidade em 1 mês: valor mínimo, inclusive. Unidade: fração (0.06 = 6%).

          return36m_max: Rentabilidade em 36 meses: valor máximo, inclusive. Unidade: fração (0.06 = 6%).

          return36m_min: Rentabilidade em 36 meses: valor mínimo, inclusive. Unidade: fração (0.06 = 6%).

          return_day_max: Variação no dia: valor máximo, inclusive. Unidade: fração (0.06 = 6%).

          return_day_min: Variação no dia: valor mínimo, inclusive. Unidade: fração (0.06 = 6%).

          return_ytd_max: Rentabilidade no ano: valor máximo, inclusive. Unidade: fração (0.06 = 6%).

          return_ytd_min: Rentabilidade no ano: valor mínimo, inclusive. Unidade: fração (0.06 = 6%).

          search: Parte do nome ou da razão social do fundo, sem diferença de maiúsculas e
              acentos. Números, com ou sem pontuação, buscam o início do CNPJ.

          sort_by: Campo de ordenação: uma chave de indicador, `name` ou `cnpj`. Padrão: `equity`.
              Valores nulos ficam no fim.

          sort_order: Ordem. Padrão: `desc`.

          total_investors_max: Cotistas: valor máximo, inclusive. Unidade: quantidade.

          total_investors_min: Cotistas: valor mínimo, inclusive. Unidade: quantidade.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/funds/screener/cnpj",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "anbima_classification": anbima_classification,
                        "classification": classification,
                        "equity_max": equity_max,
                        "equity_min": equity_min,
                        "limit": limit,
                        "manager": manager,
                        "nav_per_share_max": nav_per_share_max,
                        "nav_per_share_min": nav_per_share_min,
                        "net_flow1m_max": net_flow1m_max,
                        "net_flow1m_min": net_flow1m_min,
                        "page": page,
                        "return12m_max": return12m_max,
                        "return12m_min": return12m_min,
                        "return1m_max": return1m_max,
                        "return1m_min": return1m_min,
                        "return36m_max": return36m_max,
                        "return36m_min": return36m_min,
                        "return_day_max": return_day_max,
                        "return_day_min": return_day_min,
                        "return_ytd_max": return_ytd_max,
                        "return_ytd_min": return_ytd_min,
                        "search": search,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "total_investors_max": total_investors_max,
                        "total_investors_min": total_investors_min,
                    },
                    fund_screener_cnpj_params.FundScreenerCnpjParams,
                ),
            ),
            cast_to=FundScreenerCnpjResponse,
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
        self.screener = to_raw_response_wrapper(
            funds.screener,
        )
        self.screener_cnpj = to_raw_response_wrapper(
            funds.screener_cnpj,
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
        self.screener = async_to_raw_response_wrapper(
            funds.screener,
        )
        self.screener_cnpj = async_to_raw_response_wrapper(
            funds.screener_cnpj,
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
        self.screener = to_streamed_response_wrapper(
            funds.screener,
        )
        self.screener_cnpj = to_streamed_response_wrapper(
            funds.screener_cnpj,
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
        self.screener = async_to_streamed_response_wrapper(
            funds.screener,
        )
        self.screener_cnpj = async_to_streamed_response_wrapper(
            funds.screener_cnpj,
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
