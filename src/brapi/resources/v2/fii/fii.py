# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from .portfolio import (
    PortfolioResource,
    AsyncPortfolioResource,
    PortfolioResourceWithRawResponse,
    AsyncPortfolioResourceWithRawResponse,
    PortfolioResourceWithStreamingResponse,
    AsyncPortfolioResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .indicators import (
    IndicatorsResource,
    AsyncIndicatorsResource,
    IndicatorsResourceWithRawResponse,
    AsyncIndicatorsResourceWithRawResponse,
    IndicatorsResourceWithStreamingResponse,
    AsyncIndicatorsResourceWithStreamingResponse,
)
from .properties import (
    PropertiesResource,
    AsyncPropertiesResource,
    PropertiesResourceWithRawResponse,
    AsyncPropertiesResourceWithRawResponse,
    PropertiesResourceWithStreamingResponse,
    AsyncPropertiesResourceWithStreamingResponse,
)
from ....types.v2 import (
    fii_list_params,
    fii_reports_params,
    fii_dividends_params,
    fii_financials_params,
    fii_historical_params,
    fii_annual_reports_params,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v2.fii_list_response import FiiListResponse
from ....types.v2.fii_reports_response import FiiReportsResponse
from ....types.v2.fii_dividends_response import FiiDividendsResponse
from ....types.v2.fii_financials_response import FiiFinancialsResponse
from ....types.v2.fii_historical_response import FiiHistoricalResponse
from ....types.v2.fii_annual_reports_response import FiiAnnualReportsResponse

__all__ = ["FiiResource", "AsyncFiiResource"]


class FiiResource(SyncAPIResource):
    """
    Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
    """

    @cached_property
    def indicators(self) -> IndicatorsResource:
        """
        Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
        """
        return IndicatorsResource(self._client)

    @cached_property
    def portfolio(self) -> PortfolioResource:
        """
        Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
        """
        return PortfolioResource(self._client)

    @cached_property
    def properties(self) -> PropertiesResource:
        """
        Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
        """
        return PropertiesResource(self._client)

    @cached_property
    def with_raw_response(self) -> FiiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return FiiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FiiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return FiiResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cnpjs: str | Omit = omit,
        limit: int | Omit = omit,
        mandate: str | Omit = omit,
        page: int | Omit = omit,
        search: str | Omit = omit,
        segmento_atuacao: str | Omit = omit,
        segment_type: Literal["papel", "tijolo", "hibrido", "fof"] | Omit = omit,
        sort_by: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        symbols: str | Omit = omit,
        tipo_gestao: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FiiListResponse:
        """
        Lista paginada de FIIs com dados cadastrais, dados do administrador e
        indicadores atuais: preço, valor patrimonial por cota, P/VP, dividend yield de
        12 meses e total de cotistas.

        Use para montar um screener, filtrar fundos por segmento ou achar o ticker de um
        CNPJ.

        `search` busca no nome, no ticker e no CNPJ. `segmentoAtuacao` aceita valores
        como Logística, Shoppings, Escritórios, Lajes Corporativas, Títulos e Val. Mob.,
        Residencial, Hospital, Hotel, Educacional, Híbrido, Multicategoria, Varejo e
        Outros.

        `sortBy` aceita `symbol`, `name`, `segmentoAtuacao`, `mandate`, `price`,
        `navPerShare`, `priceToNav`, `dividendYield12m` e `totalInvestors`. O padrão é
        `totalInvestors`.

        Nem todo ticker terminado em 11 é FII. FI-Infra (como JURO11), FIAGRO, FIDC e
        FIP ficam em [fundos](https://brapi.dev/docs/fundos).

        Plano Pro. Sem token, aceita só `symbols` ou `cnpjs` de MXRF11 e HGLG11.

        Args:
          cnpjs: CNPJs de FIIs separados por vírgula, até 20. Aceita com ou sem pontuação.

          limit: Itens por página. Não há limite máximo.

          mandate: Mandato do fundo. Ex.: Renda, Híbrido, Títulos e Valores Mobiliários.

          page: Número da página, a partir de 1.

          search: Texto buscado no nome, no ticker ou no CNPJ.

          segmento_atuacao: Setor de atuação. Ex.: Logística, Shoppings, Escritórios.

          segment_type: Tipo do fundo: papel, tijolo, hibrido ou fof.

          sort_by: Campo de ordenação.

          sort_order: Direção da ordenação.

          symbols: Tickers de FIIs separados por vírgula, até 20.

          tipo_gestao: Tipo de gestão: Ativa ou Definida.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/fii/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cnpjs": cnpjs,
                        "limit": limit,
                        "mandate": mandate,
                        "page": page,
                        "search": search,
                        "segmento_atuacao": segmento_atuacao,
                        "segment_type": segment_type,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "symbols": symbols,
                        "tipo_gestao": tipo_gestao,
                    },
                    fii_list_params.FiiListParams,
                ),
            ),
            cast_to=FiiListResponse,
        )

    def annual_reports(
        self,
        *,
        cnpjs: str | Omit = omit,
        end_date: str | Omit = omit,
        include: str | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        sort_by: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        symbols: str | Omit = omit,
        year: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FiiAnnualReportsResponse:
        """
        Informe anual que cada FII entrega à CVM, com os dados consolidados do exercício
        em `fields`.

        Use para consultar dados anuais oficiais de um fundo.

        Busque por `symbols` ou `cnpjs`. Filtre por `year` ou por `startDate` e
        `endDate`. FIAGRO, FI-Infra, FIDC e FIP ficam em
        [fundos](https://brapi.dev/docs/fundos).

        Plano Pro. Sem token, aceita só `symbols` com MXRF11 e HGLG11.

        Args:
          cnpjs: CNPJs de FIIs separados por vírgula, até 20. Aceita com ou sem pontuação.

          end_date: Data de referência final no formato YYYY-MM-DD.

          include: Seções opcionais conforme estrutura do informe anual

          sort_by: Campo de ordenação: referenceDate, symbol, cnpj ou year.

          start_date: Data de referência inicial no formato YYYY-MM-DD.

          symbols: Tickers de FIIs separados por vírgula, até 20.

          year: Ano do exercício do documento.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/fii/annual-reports",
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
                        "limit": limit,
                        "page": page,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "start_date": start_date,
                        "symbols": symbols,
                        "year": year,
                    },
                    fii_annual_reports_params.FiiAnnualReportsParams,
                ),
            ),
            cast_to=FiiAnnualReportsResponse,
        )

    def dividends(
        self,
        *,
        symbols: str,
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
    ) -> FiiDividendsResponse:
        """Rendimentos e amortizações pagos por FIIs.

        Cada evento traz tipo (`label`),
        valor por cota em reais (`rate`), data-com (`lastDatePrior`), data de pagamento,
        data de aprovação e ISIN.

        Use para calcular dividend yield, montar calendários de rendimentos e somar a
        renda de uma carteira.

        `label` é RENDIMENTO ou AMORTIZAÇÃO. Amortização devolve capital e reduz o valor
        patrimonial da cota. Não some as duas para calcular yield.

        Os dados vêm dos informes mensais da CVM e de comunicados dos administradores.
        Quando a fonte não tem as datas reais, `paymentDate` e `lastDatePrior` recebem a
        data de referência do informe mensal, e `remarks` indica a origem. A data
        inicial varia por fundo.

        `startDate` e `endDate` filtram por `paymentDate`. Sem datas, retorna os últimos
        12 meses. `sortBy` aceita `paymentDate` (padrão), `lastDatePrior`, `approvedOn`,
        `rate` e `symbol`.

        Plano Pro. Sem token, aceita só `symbols` com MXRF11 e HGLG11.

        Args:
          symbols: Tickers de FIIs separados por vírgula, até 20. Ex.: HGLG11,MXRF11.

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
            "/api/v2/fii/dividends",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "symbols": symbols,
                        "end_date": end_date,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "start_date": start_date,
                    },
                    fii_dividends_params.FiiDividendsParams,
                ),
            ),
            cast_to=FiiDividendsResponse,
        )

    def financials(
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
        year: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FiiFinancialsResponse:
        """
        Demonstrações financeiras auditadas de FIIs, extraídas dos documentos DFIN
        entregues à CVM. Os valores vêm em `fields`, por ano e data de referência.

        Use para analisar números auditados de um fundo e conferir os dados do
        [relatório mensal](https://brapi.dev/docs/fiis/relatorios).

        Busque por `symbols` ou `cnpjs`. Filtre por `year` ou por `startDate` e
        `endDate`. A demonstração auditada sai depois do relatório mensal e prevalece
        quando os dois divergem.

        Plano Pro. Sem token, aceita só `symbols` com MXRF11 e HGLG11.

        Args:
          cnpjs: CNPJs de FIIs separados por vírgula, até 20. Aceita com ou sem pontuação.

          end_date: Data de referência final no formato YYYY-MM-DD.

          sort_by: Campo de ordenação: referenceDate, symbol, cnpj ou year.

          start_date: Data de referência inicial no formato YYYY-MM-DD.

          symbols: Tickers de FIIs separados por vírgula, até 20.

          year: Ano do exercício do documento.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/fii/financials",
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
                        "year": year,
                    },
                    fii_financials_params.FiiFinancialsParams,
                ),
            ),
            cast_to=FiiFinancialsResponse,
        )

    def historical(
        self,
        *,
        symbols: str,
        end_date: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FiiHistoricalResponse:
        """
        Série diária de preços das cotas de FIIs: `open`, `high`, `low`, `close`,
        `volume` e `adjustedClose`, em reais. `date` é um timestamp UNIX em segundos.

        Use para gráficos de preço, cálculo de retorno e backtests.

        Use `adjustedClose` para calcular retorno. Ele considera desdobramentos e
        proventos. `close` não.

        Sem `startDate` e `endDate`, retorna os últimos 12 meses. Cada símbolo tem a
        própria série em `historicalDataPrice`.

        Plano Pro. Sem token, aceita só `symbols` com MXRF11 e HGLG11.

        Args:
          symbols: Tickers de FIIs separados por vírgula, até 20. Ex.: HGLG11,MXRF11.

          end_date: Data final no formato YYYY-MM-DD.

          sort_order: Direção da ordenação por data.

          start_date: Data inicial no formato YYYY-MM-DD.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/fii/historical",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "symbols": symbols,
                        "end_date": end_date,
                        "sort_order": sort_order,
                        "start_date": start_date,
                    },
                    fii_historical_params.FiiHistoricalParams,
                ),
            ),
            cast_to=FiiHistoricalResponse,
        )

    def reports(
        self,
        *,
        symbols: str,
        all_versions: Literal["true", "false"] | Omit = omit,
        end_date: str | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        sort_by: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FiiReportsResponse:
        """
        Informe mensal que cada FII entrega à CVM: patrimônio, cotas, valor patrimonial
        por cota, taxa de administração, retorno e yield do mês, cotistas, e a
        composição do ativo e do passivo.

        Use para ver a composição do patrimônio, acompanhar taxas e comparar o retorno
        mensal entre fundos.

        O ativo separa caixa, títulos públicos e privados, fundos de renda fixa,
        imóveis, CRI, LCI, cotas de outros FIIs e recebíveis. O passivo separa
        distribuições a pagar, taxas a pagar e obrigações imobiliárias.

        Sem `startDate` e `endDate`, retorna os últimos 12 meses. O padrão retorna a
        versão mais recente de cada mês, e `allVersions=true` inclui as versões
        retificadas. `sortBy` aceita `referenceDate` (padrão), `symbol`, `totalAssets`,
        `equity`, `navPerShare`, `monthlyReturn`, `monthlyDividendYield`,
        `totalInvestors` e `version`.

        Plano Pro. Sem token, aceita só `symbols` com MXRF11 e HGLG11.

        Args:
          symbols: Tickers de FIIs separados por vírgula, até 20. Ex.: HGLG11,MXRF11.

          all_versions: true inclui todas as versões de cada mês. false retorna só a mais recente.

          end_date: Data final no formato YYYY-MM-DD.

          limit: Itens por página. Não há limite máximo.

          page: Número da página, a partir de 1.

          sort_by: Campo de ordenação.

          sort_order: Direção da ordenação.

          start_date: Data inicial no formato YYYY-MM-DD.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/fii/reports",
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
                        "limit": limit,
                        "page": page,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "start_date": start_date,
                    },
                    fii_reports_params.FiiReportsParams,
                ),
            ),
            cast_to=FiiReportsResponse,
        )


class AsyncFiiResource(AsyncAPIResource):
    """
    Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
    """

    @cached_property
    def indicators(self) -> AsyncIndicatorsResource:
        """
        Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
        """
        return AsyncIndicatorsResource(self._client)

    @cached_property
    def portfolio(self) -> AsyncPortfolioResource:
        """
        Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
        """
        return AsyncPortfolioResource(self._client)

    @cached_property
    def properties(self) -> AsyncPropertiesResource:
        """
        Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
        """
        return AsyncPropertiesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFiiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFiiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFiiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncFiiResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        cnpjs: str | Omit = omit,
        limit: int | Omit = omit,
        mandate: str | Omit = omit,
        page: int | Omit = omit,
        search: str | Omit = omit,
        segmento_atuacao: str | Omit = omit,
        segment_type: Literal["papel", "tijolo", "hibrido", "fof"] | Omit = omit,
        sort_by: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        symbols: str | Omit = omit,
        tipo_gestao: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FiiListResponse:
        """
        Lista paginada de FIIs com dados cadastrais, dados do administrador e
        indicadores atuais: preço, valor patrimonial por cota, P/VP, dividend yield de
        12 meses e total de cotistas.

        Use para montar um screener, filtrar fundos por segmento ou achar o ticker de um
        CNPJ.

        `search` busca no nome, no ticker e no CNPJ. `segmentoAtuacao` aceita valores
        como Logística, Shoppings, Escritórios, Lajes Corporativas, Títulos e Val. Mob.,
        Residencial, Hospital, Hotel, Educacional, Híbrido, Multicategoria, Varejo e
        Outros.

        `sortBy` aceita `symbol`, `name`, `segmentoAtuacao`, `mandate`, `price`,
        `navPerShare`, `priceToNav`, `dividendYield12m` e `totalInvestors`. O padrão é
        `totalInvestors`.

        Nem todo ticker terminado em 11 é FII. FI-Infra (como JURO11), FIAGRO, FIDC e
        FIP ficam em [fundos](https://brapi.dev/docs/fundos).

        Plano Pro. Sem token, aceita só `symbols` ou `cnpjs` de MXRF11 e HGLG11.

        Args:
          cnpjs: CNPJs de FIIs separados por vírgula, até 20. Aceita com ou sem pontuação.

          limit: Itens por página. Não há limite máximo.

          mandate: Mandato do fundo. Ex.: Renda, Híbrido, Títulos e Valores Mobiliários.

          page: Número da página, a partir de 1.

          search: Texto buscado no nome, no ticker ou no CNPJ.

          segmento_atuacao: Setor de atuação. Ex.: Logística, Shoppings, Escritórios.

          segment_type: Tipo do fundo: papel, tijolo, hibrido ou fof.

          sort_by: Campo de ordenação.

          sort_order: Direção da ordenação.

          symbols: Tickers de FIIs separados por vírgula, até 20.

          tipo_gestao: Tipo de gestão: Ativa ou Definida.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/fii/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cnpjs": cnpjs,
                        "limit": limit,
                        "mandate": mandate,
                        "page": page,
                        "search": search,
                        "segmento_atuacao": segmento_atuacao,
                        "segment_type": segment_type,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "symbols": symbols,
                        "tipo_gestao": tipo_gestao,
                    },
                    fii_list_params.FiiListParams,
                ),
            ),
            cast_to=FiiListResponse,
        )

    async def annual_reports(
        self,
        *,
        cnpjs: str | Omit = omit,
        end_date: str | Omit = omit,
        include: str | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        sort_by: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        symbols: str | Omit = omit,
        year: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FiiAnnualReportsResponse:
        """
        Informe anual que cada FII entrega à CVM, com os dados consolidados do exercício
        em `fields`.

        Use para consultar dados anuais oficiais de um fundo.

        Busque por `symbols` ou `cnpjs`. Filtre por `year` ou por `startDate` e
        `endDate`. FIAGRO, FI-Infra, FIDC e FIP ficam em
        [fundos](https://brapi.dev/docs/fundos).

        Plano Pro. Sem token, aceita só `symbols` com MXRF11 e HGLG11.

        Args:
          cnpjs: CNPJs de FIIs separados por vírgula, até 20. Aceita com ou sem pontuação.

          end_date: Data de referência final no formato YYYY-MM-DD.

          include: Seções opcionais conforme estrutura do informe anual

          sort_by: Campo de ordenação: referenceDate, symbol, cnpj ou year.

          start_date: Data de referência inicial no formato YYYY-MM-DD.

          symbols: Tickers de FIIs separados por vírgula, até 20.

          year: Ano do exercício do documento.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/fii/annual-reports",
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
                        "limit": limit,
                        "page": page,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "start_date": start_date,
                        "symbols": symbols,
                        "year": year,
                    },
                    fii_annual_reports_params.FiiAnnualReportsParams,
                ),
            ),
            cast_to=FiiAnnualReportsResponse,
        )

    async def dividends(
        self,
        *,
        symbols: str,
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
    ) -> FiiDividendsResponse:
        """Rendimentos e amortizações pagos por FIIs.

        Cada evento traz tipo (`label`),
        valor por cota em reais (`rate`), data-com (`lastDatePrior`), data de pagamento,
        data de aprovação e ISIN.

        Use para calcular dividend yield, montar calendários de rendimentos e somar a
        renda de uma carteira.

        `label` é RENDIMENTO ou AMORTIZAÇÃO. Amortização devolve capital e reduz o valor
        patrimonial da cota. Não some as duas para calcular yield.

        Os dados vêm dos informes mensais da CVM e de comunicados dos administradores.
        Quando a fonte não tem as datas reais, `paymentDate` e `lastDatePrior` recebem a
        data de referência do informe mensal, e `remarks` indica a origem. A data
        inicial varia por fundo.

        `startDate` e `endDate` filtram por `paymentDate`. Sem datas, retorna os últimos
        12 meses. `sortBy` aceita `paymentDate` (padrão), `lastDatePrior`, `approvedOn`,
        `rate` e `symbol`.

        Plano Pro. Sem token, aceita só `symbols` com MXRF11 e HGLG11.

        Args:
          symbols: Tickers de FIIs separados por vírgula, até 20. Ex.: HGLG11,MXRF11.

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
            "/api/v2/fii/dividends",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "symbols": symbols,
                        "end_date": end_date,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "start_date": start_date,
                    },
                    fii_dividends_params.FiiDividendsParams,
                ),
            ),
            cast_to=FiiDividendsResponse,
        )

    async def financials(
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
        year: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FiiFinancialsResponse:
        """
        Demonstrações financeiras auditadas de FIIs, extraídas dos documentos DFIN
        entregues à CVM. Os valores vêm em `fields`, por ano e data de referência.

        Use para analisar números auditados de um fundo e conferir os dados do
        [relatório mensal](https://brapi.dev/docs/fiis/relatorios).

        Busque por `symbols` ou `cnpjs`. Filtre por `year` ou por `startDate` e
        `endDate`. A demonstração auditada sai depois do relatório mensal e prevalece
        quando os dois divergem.

        Plano Pro. Sem token, aceita só `symbols` com MXRF11 e HGLG11.

        Args:
          cnpjs: CNPJs de FIIs separados por vírgula, até 20. Aceita com ou sem pontuação.

          end_date: Data de referência final no formato YYYY-MM-DD.

          sort_by: Campo de ordenação: referenceDate, symbol, cnpj ou year.

          start_date: Data de referência inicial no formato YYYY-MM-DD.

          symbols: Tickers de FIIs separados por vírgula, até 20.

          year: Ano do exercício do documento.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/fii/financials",
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
                        "year": year,
                    },
                    fii_financials_params.FiiFinancialsParams,
                ),
            ),
            cast_to=FiiFinancialsResponse,
        )

    async def historical(
        self,
        *,
        symbols: str,
        end_date: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FiiHistoricalResponse:
        """
        Série diária de preços das cotas de FIIs: `open`, `high`, `low`, `close`,
        `volume` e `adjustedClose`, em reais. `date` é um timestamp UNIX em segundos.

        Use para gráficos de preço, cálculo de retorno e backtests.

        Use `adjustedClose` para calcular retorno. Ele considera desdobramentos e
        proventos. `close` não.

        Sem `startDate` e `endDate`, retorna os últimos 12 meses. Cada símbolo tem a
        própria série em `historicalDataPrice`.

        Plano Pro. Sem token, aceita só `symbols` com MXRF11 e HGLG11.

        Args:
          symbols: Tickers de FIIs separados por vírgula, até 20. Ex.: HGLG11,MXRF11.

          end_date: Data final no formato YYYY-MM-DD.

          sort_order: Direção da ordenação por data.

          start_date: Data inicial no formato YYYY-MM-DD.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/fii/historical",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "symbols": symbols,
                        "end_date": end_date,
                        "sort_order": sort_order,
                        "start_date": start_date,
                    },
                    fii_historical_params.FiiHistoricalParams,
                ),
            ),
            cast_to=FiiHistoricalResponse,
        )

    async def reports(
        self,
        *,
        symbols: str,
        all_versions: Literal["true", "false"] | Omit = omit,
        end_date: str | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        sort_by: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FiiReportsResponse:
        """
        Informe mensal que cada FII entrega à CVM: patrimônio, cotas, valor patrimonial
        por cota, taxa de administração, retorno e yield do mês, cotistas, e a
        composição do ativo e do passivo.

        Use para ver a composição do patrimônio, acompanhar taxas e comparar o retorno
        mensal entre fundos.

        O ativo separa caixa, títulos públicos e privados, fundos de renda fixa,
        imóveis, CRI, LCI, cotas de outros FIIs e recebíveis. O passivo separa
        distribuições a pagar, taxas a pagar e obrigações imobiliárias.

        Sem `startDate` e `endDate`, retorna os últimos 12 meses. O padrão retorna a
        versão mais recente de cada mês, e `allVersions=true` inclui as versões
        retificadas. `sortBy` aceita `referenceDate` (padrão), `symbol`, `totalAssets`,
        `equity`, `navPerShare`, `monthlyReturn`, `monthlyDividendYield`,
        `totalInvestors` e `version`.

        Plano Pro. Sem token, aceita só `symbols` com MXRF11 e HGLG11.

        Args:
          symbols: Tickers de FIIs separados por vírgula, até 20. Ex.: HGLG11,MXRF11.

          all_versions: true inclui todas as versões de cada mês. false retorna só a mais recente.

          end_date: Data final no formato YYYY-MM-DD.

          limit: Itens por página. Não há limite máximo.

          page: Número da página, a partir de 1.

          sort_by: Campo de ordenação.

          sort_order: Direção da ordenação.

          start_date: Data inicial no formato YYYY-MM-DD.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/fii/reports",
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
                        "limit": limit,
                        "page": page,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "start_date": start_date,
                    },
                    fii_reports_params.FiiReportsParams,
                ),
            ),
            cast_to=FiiReportsResponse,
        )


class FiiResourceWithRawResponse:
    def __init__(self, fii: FiiResource) -> None:
        self._fii = fii

        self.list = to_raw_response_wrapper(
            fii.list,
        )
        self.annual_reports = to_raw_response_wrapper(
            fii.annual_reports,
        )
        self.dividends = to_raw_response_wrapper(
            fii.dividends,
        )
        self.financials = to_raw_response_wrapper(
            fii.financials,
        )
        self.historical = to_raw_response_wrapper(
            fii.historical,
        )
        self.reports = to_raw_response_wrapper(
            fii.reports,
        )

    @cached_property
    def indicators(self) -> IndicatorsResourceWithRawResponse:
        """
        Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
        """
        return IndicatorsResourceWithRawResponse(self._fii.indicators)

    @cached_property
    def portfolio(self) -> PortfolioResourceWithRawResponse:
        """
        Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
        """
        return PortfolioResourceWithRawResponse(self._fii.portfolio)

    @cached_property
    def properties(self) -> PropertiesResourceWithRawResponse:
        """
        Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
        """
        return PropertiesResourceWithRawResponse(self._fii.properties)


class AsyncFiiResourceWithRawResponse:
    def __init__(self, fii: AsyncFiiResource) -> None:
        self._fii = fii

        self.list = async_to_raw_response_wrapper(
            fii.list,
        )
        self.annual_reports = async_to_raw_response_wrapper(
            fii.annual_reports,
        )
        self.dividends = async_to_raw_response_wrapper(
            fii.dividends,
        )
        self.financials = async_to_raw_response_wrapper(
            fii.financials,
        )
        self.historical = async_to_raw_response_wrapper(
            fii.historical,
        )
        self.reports = async_to_raw_response_wrapper(
            fii.reports,
        )

    @cached_property
    def indicators(self) -> AsyncIndicatorsResourceWithRawResponse:
        """
        Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
        """
        return AsyncIndicatorsResourceWithRawResponse(self._fii.indicators)

    @cached_property
    def portfolio(self) -> AsyncPortfolioResourceWithRawResponse:
        """
        Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
        """
        return AsyncPortfolioResourceWithRawResponse(self._fii.portfolio)

    @cached_property
    def properties(self) -> AsyncPropertiesResourceWithRawResponse:
        """
        Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
        """
        return AsyncPropertiesResourceWithRawResponse(self._fii.properties)


class FiiResourceWithStreamingResponse:
    def __init__(self, fii: FiiResource) -> None:
        self._fii = fii

        self.list = to_streamed_response_wrapper(
            fii.list,
        )
        self.annual_reports = to_streamed_response_wrapper(
            fii.annual_reports,
        )
        self.dividends = to_streamed_response_wrapper(
            fii.dividends,
        )
        self.financials = to_streamed_response_wrapper(
            fii.financials,
        )
        self.historical = to_streamed_response_wrapper(
            fii.historical,
        )
        self.reports = to_streamed_response_wrapper(
            fii.reports,
        )

    @cached_property
    def indicators(self) -> IndicatorsResourceWithStreamingResponse:
        """
        Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
        """
        return IndicatorsResourceWithStreamingResponse(self._fii.indicators)

    @cached_property
    def portfolio(self) -> PortfolioResourceWithStreamingResponse:
        """
        Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
        """
        return PortfolioResourceWithStreamingResponse(self._fii.portfolio)

    @cached_property
    def properties(self) -> PropertiesResourceWithStreamingResponse:
        """
        Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
        """
        return PropertiesResourceWithStreamingResponse(self._fii.properties)


class AsyncFiiResourceWithStreamingResponse:
    def __init__(self, fii: AsyncFiiResource) -> None:
        self._fii = fii

        self.list = async_to_streamed_response_wrapper(
            fii.list,
        )
        self.annual_reports = async_to_streamed_response_wrapper(
            fii.annual_reports,
        )
        self.dividends = async_to_streamed_response_wrapper(
            fii.dividends,
        )
        self.financials = async_to_streamed_response_wrapper(
            fii.financials,
        )
        self.historical = async_to_streamed_response_wrapper(
            fii.historical,
        )
        self.reports = async_to_streamed_response_wrapper(
            fii.reports,
        )

    @cached_property
    def indicators(self) -> AsyncIndicatorsResourceWithStreamingResponse:
        """
        Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
        """
        return AsyncIndicatorsResourceWithStreamingResponse(self._fii.indicators)

    @cached_property
    def portfolio(self) -> AsyncPortfolioResourceWithStreamingResponse:
        """
        Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
        """
        return AsyncPortfolioResourceWithStreamingResponse(self._fii.portfolio)

    @cached_property
    def properties(self) -> AsyncPropertiesResourceWithStreamingResponse:
        """
        Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
        """
        return AsyncPropertiesResourceWithStreamingResponse(self._fii.properties)
