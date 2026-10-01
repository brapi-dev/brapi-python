# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v2 import (
    stock_quote_params,
    stock_profile_params,
    stock_cash_flow_params,
    stock_dividends_params,
    stock_historical_params,
    stock_statistics_params,
    stock_value_added_params,
    stock_balance_sheet_params,
    stock_financial_data_params,
    stock_income_statement_params,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v2.stock_quote_response import StockQuoteResponse
from ...types.v2.stock_profile_response import StockProfileResponse
from ...types.v2.stock_cash_flow_response import StockCashFlowResponse
from ...types.v2.stock_dividends_response import StockDividendsResponse
from ...types.v2.stock_historical_response import StockHistoricalResponse
from ...types.v2.stock_statistics_response import StockStatisticsResponse
from ...types.v2.stock_value_added_response import StockValueAddedResponse
from ...types.v2.stock_balance_sheet_response import StockBalanceSheetResponse
from ...types.v2.stock_financial_data_response import StockFinancialDataResponse
from ...types.v2.stock_income_statement_response import StockIncomeStatementResponse

__all__ = ["StocksResource", "AsyncStocksResource"]


class StocksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StocksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return StocksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StocksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return StocksResourceWithStreamingResponse(self)

    def balance_sheet(
        self,
        *,
        symbols: str,
        end_date: str | Omit = omit,
        period: Literal["annual", "quarterly"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockBalanceSheetResponse:
        """
        Ativo, passivo e patrimônio líquido de empresas listadas, com base nos
        demonstrativos entregues à CVM. Uma linha por período, do mais recente para o
        mais antigo.

        Use para analisar endividamento, liquidez e estrutura de capital.

        O padrão é `period=annual`. Use `period=quarterly` para trimestres. `startDate`
        e `endDate` filtram pela data de encerramento do período.

        Bancos e seguradoras usam outro plano de contas. Campos que não se aplicam ao
        setor vêm como `null`.

        Args:
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. Um ticker antigo é trocado pelo
              ticker atual.

          end_date: Data final no formato YYYY-MM-DD. Filtra pela data de encerramento do período.

          period: Período de cada linha: anual ou trimestral.

          start_date: Data inicial no formato YYYY-MM-DD. Filtra pela data de encerramento do período.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/stocks/balance-sheet",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "symbols": symbols,
                        "end_date": end_date,
                        "period": period,
                        "start_date": start_date,
                    },
                    stock_balance_sheet_params.StockBalanceSheetParams,
                ),
            ),
            cast_to=StockBalanceSheetResponse,
        )

    def cash_flow(
        self,
        *,
        symbols: str,
        end_date: str | Omit = omit,
        period: Literal["annual", "quarterly"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockCashFlowResponse:
        """
        Demonstração do fluxo de caixa de empresas listadas: caixa das atividades
        operacionais, de investimento e de financiamento, com os saldos de caixa no
        início e no fim do período.

        Use para comparar a geração de caixa com o lucro e calcular o fluxo de caixa
        livre.

        O padrão é `period=annual`. Use `period=quarterly` para trimestres. `startDate`
        e `endDate` filtram pela data de encerramento do período.

        `freeCashFlow` soma o caixa operacional e o caixa de investimento. Ele é `null`
        quando um dos dois falta.

        Os trimestres usam a mesma base, consolidada ou individual, do relatório anual
        do mesmo ano. Sem relatório anual, a base é a que tem o trimestre mais recente.
        Em empate, a consolidada vale. Lacunas não são preenchidas com a outra base. Um
        período sem os dados necessários para o cálculo retorna `null`.

        Args:
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. Um ticker antigo é trocado pelo
              ticker atual.

          end_date: Data final no formato YYYY-MM-DD. Filtra pela data de encerramento do período.

          period: Período de cada linha: anual ou trimestral.

          start_date: Data inicial no formato YYYY-MM-DD. Filtra pela data de encerramento do período.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/stocks/cash-flow",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "symbols": symbols,
                        "end_date": end_date,
                        "period": period,
                        "start_date": start_date,
                    },
                    stock_cash_flow_params.StockCashFlowParams,
                ),
            ),
            cast_to=StockCashFlowResponse,
        )

    def dividends(
        self,
        *,
        symbols: str,
        end_date: str | Omit = omit,
        include_raw: Literal["true", "false"] | Omit = omit,
        sort_by: Literal["paymentDate", "lastDatePrior", "approvedOn", "rate"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockDividendsResponse:
        """
        Proventos de ações brasileiras: dividendos, JCP, bonificações, desdobramentos,
        grupamentos e subscrições, com valor por ação, data-com, data ex e data de
        pagamento.

        Use para calcular dividend yield, montar calendários de proventos e registrar
        proventos em carteiras.

        Em conversões de ações, os proventos de cada classe permanecem separados. Uma
        consulta por AXIA6 retorna os proventos de AXIA6 e ELET6.

        `lastDatePrior` é a data-com, o último dia para comprar a ação e ter direito ao
        provento. `exDate` é a data ex, o primeiro dia sem esse direito. `exDate` pode
        ser nulo.

        `startDate` e `endDate` filtram proventos em dinheiro por `paymentDate` e
        eventos em ações por `lastDatePrior`.

        `includeRaw=true` exige o plano Pro. Ele adiciona `rawRate`, o valor por ação na
        escala dos preços sem ajuste.

        FIIs não entram aqui. Um ticker de FII retorna erro 400. Use
        [dividendos de FIIs](https://brapi.dev/docs/fiis/dividendos).

        Args:
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. Um ticker antigo é trocado pelo
              ticker atual.

          end_date: Data final no formato YYYY-MM-DD. Filtra proventos em dinheiro por `paymentDate`
              e eventos em ações por `lastDatePrior`.

          include_raw: Inclui `rawRate`, o valor por ação na escala dos preços sem ajuste. Exige o
              plano Pro.

          sort_by: Campo de ordenação dos eventos.

          sort_order: Ordem dos eventos.

          start_date: Data inicial no formato YYYY-MM-DD. Filtra proventos em dinheiro por
              `paymentDate` e eventos em ações por `lastDatePrior`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/stocks/dividends",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "symbols": symbols,
                        "end_date": end_date,
                        "include_raw": include_raw,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "start_date": start_date,
                    },
                    stock_dividends_params.StockDividendsParams,
                ),
            ),
            cast_to=StockDividendsResponse,
        )

    def financial_data(
        self,
        *,
        symbols: str,
        end_date: str | Omit = omit,
        mode: Literal["current", "history"] | Omit = omit,
        period: Literal["annual", "quarterly"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockFinancialDataResponse:
        """
        Receita, lucro, EBITDA, margens, dívida, caixa e fluxo de caixa livre de uma
        empresa, em um único objeto.

        Use para ver o resumo financeiro sem ler cada demonstração.

        O padrão `mode=current` traz os últimos 12 meses. `mode=history` traz a série
        anual ou trimestral, conforme `period`, filtrada por `startDate` e `endDate`.

        Para as linhas completas, use
        [balanço patrimonial](https://brapi.dev/docs/acoes/balanco-patrimonial),
        [DRE](https://brapi.dev/docs/acoes/dre) e
        [fluxo de caixa](https://brapi.dev/docs/acoes/fluxo-de-caixa).

        Args:
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. Um ticker antigo é trocado pelo
              ticker atual.

          end_date: Data final no formato YYYY-MM-DD. Filtra pela data de encerramento do período.

          mode: `current` traz o valor atual. `history` traz a série definida por `period`.

          period: Período de cada linha: anual ou trimestral.

          start_date: Data inicial no formato YYYY-MM-DD. Filtra pela data de encerramento do período.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/stocks/financial-data",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "symbols": symbols,
                        "end_date": end_date,
                        "mode": mode,
                        "period": period,
                        "start_date": start_date,
                    },
                    stock_financial_data_params.StockFinancialDataParams,
                ),
            ),
            cast_to=StockFinancialDataResponse,
        )

    def historical(
        self,
        *,
        symbols: str,
        end_date: str | Omit = omit,
        include_raw: Literal["true", "false"] | Omit = omit,
        interval: Literal["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
        | Omit = omit,
        range: Literal["1d", "2d", "5d", "7d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]
        | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockHistoricalResponse:
        """
        Série de preços por pregão com abertura, máxima, mínima, fechamento, fechamento
        ajustado e volume. Serve para ações, FIIs, BDRs, ETFs, units e índices com
        histórico.

        Use para gráficos, backtests e cálculo de retorno.

        Em conversões de ações, use o ticker original para consultar o histórico daquela
        classe. Por exemplo, AXIA6 mantém seu próprio histórico.

        Defina a janela com `range` e `interval`, por exemplo `range=1y&interval=1d`, ou
        com `startDate` e `endDate`. O padrão é `range=1mo` e `interval=1d`.

        O plano define os valores aceitos em `range` e `interval` e o tamanho máximo da
        janela por data. Um pedido acima do limite do plano retorna erro 400.

        Em intervalos diários, `open`, `high`, `low` e `close` podem vir ajustados.
        Nesses pontos, `close` coincide com `adjustedClose`. Outros pontos podem trazer
        `close` sem ajuste ou `adjustedClose` nulo. Os campos `raw*`, quando
        disponíveis, trazem os preços originais.

        Use `adjustedClose` para calcular retorno diário. Ele considera proventos,
        desdobramentos e grupamentos.

        `includeRaw=true` exige o plano Pro. Em intervalos diários, ele adiciona
        `rawOpen`, `rawHigh`, `rawLow` e `rawClose`, os preços originais sem ajuste.
        Esses campos podem ser nulos. Intervalos intradiários não trazem campos `raw*`.

        Args:
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. Um ticker antigo é trocado pelo
              ticker atual.

          end_date: Data final no formato YYYY-MM-DD.

          include_raw: Inclui os preços originais sem ajuste (`rawOpen`, `rawHigh`, `rawLow`,
              `rawClose`) em intervalos diários. Exige o plano Pro.

          interval: Intervalo entre os pontos. Padrão: 1d.

          range: Janela relativa. Padrão: 1mo.

          sort_order: Ordem dos pontos por data.

          start_date: Data inicial no formato YYYY-MM-DD.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/stocks/historical",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "symbols": symbols,
                        "end_date": end_date,
                        "include_raw": include_raw,
                        "interval": interval,
                        "range": range,
                        "sort_order": sort_order,
                        "start_date": start_date,
                    },
                    stock_historical_params.StockHistoricalParams,
                ),
            ),
            cast_to=StockHistoricalResponse,
        )

    def income_statement(
        self,
        *,
        symbols: str,
        end_date: str | Omit = omit,
        period: Literal["annual", "quarterly"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockIncomeStatementResponse:
        """
        Demonstração de resultado de empresas listadas: receita, custos, lucro bruto,
        despesas operacionais, resultado financeiro, impostos e lucro líquido. Uma linha
        por período, do mais recente para o mais antigo.

        Use para acompanhar resultados, margens e crescimento de lucro.

        O padrão é `period=annual`. Use `period=quarterly` para trimestres. `startDate`
        e `endDate` filtram pela data de encerramento do período.

        Cada trimestre traz o valor do trimestre isolado, sem somar os trimestres
        anteriores do ano.

        Os trimestres usam a mesma base, consolidada ou individual, do relatório anual
        do mesmo ano. Sem relatório anual, a base é a que tem o trimestre mais recente.
        Em empate, a consolidada vale. Lacunas não são preenchidas com a outra base. Um
        período sem os dados necessários para o cálculo retorna `null`.

        Args:
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. Um ticker antigo é trocado pelo
              ticker atual.

          end_date: Data final no formato YYYY-MM-DD. Filtra pela data de encerramento do período.

          period: Período de cada linha: anual ou trimestral.

          start_date: Data inicial no formato YYYY-MM-DD. Filtra pela data de encerramento do período.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/stocks/income-statement",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "symbols": symbols,
                        "end_date": end_date,
                        "period": period,
                        "start_date": start_date,
                    },
                    stock_income_statement_params.StockIncomeStatementParams,
                ),
            ),
            cast_to=StockIncomeStatementResponse,
        )

    def profile(
        self,
        *,
        symbols: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockProfileResponse:
        """
        Dados cadastrais da empresa por trás do ticker: razão social, CNPJ, setor,
        indústria, endereço, site, telefone, número de funcionários e descrição da
        atividade.

        Use para páginas de empresa, filtros por setor e cadastro de ativos em
        carteiras.

        Esses dados quase não mudam. Guarde a resposta e consulte de novo poucas vezes.

        Args:
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. Um ticker antigo é trocado pelo
              ticker atual.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/stocks/profile",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"symbols": symbols}, stock_profile_params.StockProfileParams),
            ),
            cast_to=StockProfileResponse,
        )

    def quote(
        self,
        *,
        symbols: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockQuoteResponse:
        """
        Preço, variação, volume, market cap, máxima e mínima do dia, faixa de 52 semanas
        e logo de ações, FIIs, BDRs, ETFs, units e índices brasileiros.

        Use para telas de cotação, carteiras, alertas de preço e widgets.

        Envie vários tickers em `symbols`, separados por vírgula. O número máximo de
        tickers por chamada depende do plano.

        Quando alguns tickers não existem, eles ficam fora de `results`. Se nenhum
        ticker tem cotação, a resposta retorna 404.

        Um ticker antigo é trocado pelo ticker atual. Nesse caso, `changed` é `true` e
        `requestedSymbol` guarda o ticker enviado.

        AXIA5 e AXIA6 retornam a cotação de uma ação AXIA3. Consulte a resolução de
        tickers para ver a proporção de conversão.

        Para a série de preços, use o
        [histórico de preços](https://brapi.dev/docs/acoes/historico). Para achar
        tickers válidos, use a [lista de tickers](https://brapi.dev/docs/tickers).

        Args:
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. Um ticker antigo é trocado pelo
              ticker atual.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/stocks/quote",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"symbols": symbols}, stock_quote_params.StockQuoteParams),
            ),
            cast_to=StockQuoteResponse,
        )

    def statistics(
        self,
        *,
        symbols: str,
        end_date: str | Omit = omit,
        mode: Literal["current", "history"] | Omit = omit,
        period: Literal["annual", "quarterly"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockStatisticsResponse:
        """
        Múltiplos e indicadores por ação: P/L, P/VP, beta, dividend yield, lucro por
        ação, valor patrimonial por ação e market cap.

        Use para comparar empresas, montar screeners e acompanhar valuation.

        O padrão `mode=current` traz o valor atual. `mode=history` traz a série anual ou
        trimestral, conforme `period`, filtrada por `startDate` e `endDate`.

        Múltiplos que usam o preço mudam a cada pregão. Múltiplos que usam só o balanço
        mudam quando a empresa publica um novo resultado.

        Args:
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. Um ticker antigo é trocado pelo
              ticker atual.

          end_date: Data final no formato YYYY-MM-DD. Filtra pela data de encerramento do período.

          mode: `current` traz o valor atual. `history` traz a série definida por `period`.

          period: Período de cada linha: anual ou trimestral.

          start_date: Data inicial no formato YYYY-MM-DD. Filtra pela data de encerramento do período.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/stocks/statistics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "symbols": symbols,
                        "end_date": end_date,
                        "mode": mode,
                        "period": period,
                        "start_date": start_date,
                    },
                    stock_statistics_params.StockStatisticsParams,
                ),
            ),
            cast_to=StockStatisticsResponse,
        )

    def value_added(
        self,
        *,
        symbols: str,
        end_date: str | Omit = omit,
        period: Literal["annual", "quarterly"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockValueAddedResponse:
        """
        Demonstração do valor adicionado de empresas listadas: a riqueza que a empresa
        gerou e como ela se divide entre pessoal, governo, credores e acionistas.

        Use para ver quanto a empresa paga de salários, impostos e juros, e quanto fica
        com os acionistas.

        O padrão é `period=annual`. Use `period=quarterly` para trimestres. `startDate`
        e `endDate` filtram pela data de encerramento do período.

        Os trimestres usam a mesma base, consolidada ou individual, do relatório anual
        do mesmo ano. Sem relatório anual, a base é a que tem o trimestre mais recente.
        Em empate, a consolidada vale. Lacunas não são preenchidas com a outra base. Um
        período sem os dados necessários para o cálculo retorna `null`.

        Args:
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. Um ticker antigo é trocado pelo
              ticker atual.

          end_date: Data final no formato YYYY-MM-DD. Filtra pela data de encerramento do período.

          period: Período de cada linha: anual ou trimestral.

          start_date: Data inicial no formato YYYY-MM-DD. Filtra pela data de encerramento do período.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/stocks/value-added",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "symbols": symbols,
                        "end_date": end_date,
                        "period": period,
                        "start_date": start_date,
                    },
                    stock_value_added_params.StockValueAddedParams,
                ),
            ),
            cast_to=StockValueAddedResponse,
        )


class AsyncStocksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStocksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStocksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStocksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncStocksResourceWithStreamingResponse(self)

    async def balance_sheet(
        self,
        *,
        symbols: str,
        end_date: str | Omit = omit,
        period: Literal["annual", "quarterly"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockBalanceSheetResponse:
        """
        Ativo, passivo e patrimônio líquido de empresas listadas, com base nos
        demonstrativos entregues à CVM. Uma linha por período, do mais recente para o
        mais antigo.

        Use para analisar endividamento, liquidez e estrutura de capital.

        O padrão é `period=annual`. Use `period=quarterly` para trimestres. `startDate`
        e `endDate` filtram pela data de encerramento do período.

        Bancos e seguradoras usam outro plano de contas. Campos que não se aplicam ao
        setor vêm como `null`.

        Args:
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. Um ticker antigo é trocado pelo
              ticker atual.

          end_date: Data final no formato YYYY-MM-DD. Filtra pela data de encerramento do período.

          period: Período de cada linha: anual ou trimestral.

          start_date: Data inicial no formato YYYY-MM-DD. Filtra pela data de encerramento do período.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/stocks/balance-sheet",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "symbols": symbols,
                        "end_date": end_date,
                        "period": period,
                        "start_date": start_date,
                    },
                    stock_balance_sheet_params.StockBalanceSheetParams,
                ),
            ),
            cast_to=StockBalanceSheetResponse,
        )

    async def cash_flow(
        self,
        *,
        symbols: str,
        end_date: str | Omit = omit,
        period: Literal["annual", "quarterly"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockCashFlowResponse:
        """
        Demonstração do fluxo de caixa de empresas listadas: caixa das atividades
        operacionais, de investimento e de financiamento, com os saldos de caixa no
        início e no fim do período.

        Use para comparar a geração de caixa com o lucro e calcular o fluxo de caixa
        livre.

        O padrão é `period=annual`. Use `period=quarterly` para trimestres. `startDate`
        e `endDate` filtram pela data de encerramento do período.

        `freeCashFlow` soma o caixa operacional e o caixa de investimento. Ele é `null`
        quando um dos dois falta.

        Os trimestres usam a mesma base, consolidada ou individual, do relatório anual
        do mesmo ano. Sem relatório anual, a base é a que tem o trimestre mais recente.
        Em empate, a consolidada vale. Lacunas não são preenchidas com a outra base. Um
        período sem os dados necessários para o cálculo retorna `null`.

        Args:
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. Um ticker antigo é trocado pelo
              ticker atual.

          end_date: Data final no formato YYYY-MM-DD. Filtra pela data de encerramento do período.

          period: Período de cada linha: anual ou trimestral.

          start_date: Data inicial no formato YYYY-MM-DD. Filtra pela data de encerramento do período.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/stocks/cash-flow",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "symbols": symbols,
                        "end_date": end_date,
                        "period": period,
                        "start_date": start_date,
                    },
                    stock_cash_flow_params.StockCashFlowParams,
                ),
            ),
            cast_to=StockCashFlowResponse,
        )

    async def dividends(
        self,
        *,
        symbols: str,
        end_date: str | Omit = omit,
        include_raw: Literal["true", "false"] | Omit = omit,
        sort_by: Literal["paymentDate", "lastDatePrior", "approvedOn", "rate"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockDividendsResponse:
        """
        Proventos de ações brasileiras: dividendos, JCP, bonificações, desdobramentos,
        grupamentos e subscrições, com valor por ação, data-com, data ex e data de
        pagamento.

        Use para calcular dividend yield, montar calendários de proventos e registrar
        proventos em carteiras.

        Em conversões de ações, os proventos de cada classe permanecem separados. Uma
        consulta por AXIA6 retorna os proventos de AXIA6 e ELET6.

        `lastDatePrior` é a data-com, o último dia para comprar a ação e ter direito ao
        provento. `exDate` é a data ex, o primeiro dia sem esse direito. `exDate` pode
        ser nulo.

        `startDate` e `endDate` filtram proventos em dinheiro por `paymentDate` e
        eventos em ações por `lastDatePrior`.

        `includeRaw=true` exige o plano Pro. Ele adiciona `rawRate`, o valor por ação na
        escala dos preços sem ajuste.

        FIIs não entram aqui. Um ticker de FII retorna erro 400. Use
        [dividendos de FIIs](https://brapi.dev/docs/fiis/dividendos).

        Args:
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. Um ticker antigo é trocado pelo
              ticker atual.

          end_date: Data final no formato YYYY-MM-DD. Filtra proventos em dinheiro por `paymentDate`
              e eventos em ações por `lastDatePrior`.

          include_raw: Inclui `rawRate`, o valor por ação na escala dos preços sem ajuste. Exige o
              plano Pro.

          sort_by: Campo de ordenação dos eventos.

          sort_order: Ordem dos eventos.

          start_date: Data inicial no formato YYYY-MM-DD. Filtra proventos em dinheiro por
              `paymentDate` e eventos em ações por `lastDatePrior`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/stocks/dividends",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "symbols": symbols,
                        "end_date": end_date,
                        "include_raw": include_raw,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "start_date": start_date,
                    },
                    stock_dividends_params.StockDividendsParams,
                ),
            ),
            cast_to=StockDividendsResponse,
        )

    async def financial_data(
        self,
        *,
        symbols: str,
        end_date: str | Omit = omit,
        mode: Literal["current", "history"] | Omit = omit,
        period: Literal["annual", "quarterly"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockFinancialDataResponse:
        """
        Receita, lucro, EBITDA, margens, dívida, caixa e fluxo de caixa livre de uma
        empresa, em um único objeto.

        Use para ver o resumo financeiro sem ler cada demonstração.

        O padrão `mode=current` traz os últimos 12 meses. `mode=history` traz a série
        anual ou trimestral, conforme `period`, filtrada por `startDate` e `endDate`.

        Para as linhas completas, use
        [balanço patrimonial](https://brapi.dev/docs/acoes/balanco-patrimonial),
        [DRE](https://brapi.dev/docs/acoes/dre) e
        [fluxo de caixa](https://brapi.dev/docs/acoes/fluxo-de-caixa).

        Args:
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. Um ticker antigo é trocado pelo
              ticker atual.

          end_date: Data final no formato YYYY-MM-DD. Filtra pela data de encerramento do período.

          mode: `current` traz o valor atual. `history` traz a série definida por `period`.

          period: Período de cada linha: anual ou trimestral.

          start_date: Data inicial no formato YYYY-MM-DD. Filtra pela data de encerramento do período.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/stocks/financial-data",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "symbols": symbols,
                        "end_date": end_date,
                        "mode": mode,
                        "period": period,
                        "start_date": start_date,
                    },
                    stock_financial_data_params.StockFinancialDataParams,
                ),
            ),
            cast_to=StockFinancialDataResponse,
        )

    async def historical(
        self,
        *,
        symbols: str,
        end_date: str | Omit = omit,
        include_raw: Literal["true", "false"] | Omit = omit,
        interval: Literal["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
        | Omit = omit,
        range: Literal["1d", "2d", "5d", "7d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]
        | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockHistoricalResponse:
        """
        Série de preços por pregão com abertura, máxima, mínima, fechamento, fechamento
        ajustado e volume. Serve para ações, FIIs, BDRs, ETFs, units e índices com
        histórico.

        Use para gráficos, backtests e cálculo de retorno.

        Em conversões de ações, use o ticker original para consultar o histórico daquela
        classe. Por exemplo, AXIA6 mantém seu próprio histórico.

        Defina a janela com `range` e `interval`, por exemplo `range=1y&interval=1d`, ou
        com `startDate` e `endDate`. O padrão é `range=1mo` e `interval=1d`.

        O plano define os valores aceitos em `range` e `interval` e o tamanho máximo da
        janela por data. Um pedido acima do limite do plano retorna erro 400.

        Em intervalos diários, `open`, `high`, `low` e `close` podem vir ajustados.
        Nesses pontos, `close` coincide com `adjustedClose`. Outros pontos podem trazer
        `close` sem ajuste ou `adjustedClose` nulo. Os campos `raw*`, quando
        disponíveis, trazem os preços originais.

        Use `adjustedClose` para calcular retorno diário. Ele considera proventos,
        desdobramentos e grupamentos.

        `includeRaw=true` exige o plano Pro. Em intervalos diários, ele adiciona
        `rawOpen`, `rawHigh`, `rawLow` e `rawClose`, os preços originais sem ajuste.
        Esses campos podem ser nulos. Intervalos intradiários não trazem campos `raw*`.

        Args:
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. Um ticker antigo é trocado pelo
              ticker atual.

          end_date: Data final no formato YYYY-MM-DD.

          include_raw: Inclui os preços originais sem ajuste (`rawOpen`, `rawHigh`, `rawLow`,
              `rawClose`) em intervalos diários. Exige o plano Pro.

          interval: Intervalo entre os pontos. Padrão: 1d.

          range: Janela relativa. Padrão: 1mo.

          sort_order: Ordem dos pontos por data.

          start_date: Data inicial no formato YYYY-MM-DD.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/stocks/historical",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "symbols": symbols,
                        "end_date": end_date,
                        "include_raw": include_raw,
                        "interval": interval,
                        "range": range,
                        "sort_order": sort_order,
                        "start_date": start_date,
                    },
                    stock_historical_params.StockHistoricalParams,
                ),
            ),
            cast_to=StockHistoricalResponse,
        )

    async def income_statement(
        self,
        *,
        symbols: str,
        end_date: str | Omit = omit,
        period: Literal["annual", "quarterly"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockIncomeStatementResponse:
        """
        Demonstração de resultado de empresas listadas: receita, custos, lucro bruto,
        despesas operacionais, resultado financeiro, impostos e lucro líquido. Uma linha
        por período, do mais recente para o mais antigo.

        Use para acompanhar resultados, margens e crescimento de lucro.

        O padrão é `period=annual`. Use `period=quarterly` para trimestres. `startDate`
        e `endDate` filtram pela data de encerramento do período.

        Cada trimestre traz o valor do trimestre isolado, sem somar os trimestres
        anteriores do ano.

        Os trimestres usam a mesma base, consolidada ou individual, do relatório anual
        do mesmo ano. Sem relatório anual, a base é a que tem o trimestre mais recente.
        Em empate, a consolidada vale. Lacunas não são preenchidas com a outra base. Um
        período sem os dados necessários para o cálculo retorna `null`.

        Args:
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. Um ticker antigo é trocado pelo
              ticker atual.

          end_date: Data final no formato YYYY-MM-DD. Filtra pela data de encerramento do período.

          period: Período de cada linha: anual ou trimestral.

          start_date: Data inicial no formato YYYY-MM-DD. Filtra pela data de encerramento do período.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/stocks/income-statement",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "symbols": symbols,
                        "end_date": end_date,
                        "period": period,
                        "start_date": start_date,
                    },
                    stock_income_statement_params.StockIncomeStatementParams,
                ),
            ),
            cast_to=StockIncomeStatementResponse,
        )

    async def profile(
        self,
        *,
        symbols: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockProfileResponse:
        """
        Dados cadastrais da empresa por trás do ticker: razão social, CNPJ, setor,
        indústria, endereço, site, telefone, número de funcionários e descrição da
        atividade.

        Use para páginas de empresa, filtros por setor e cadastro de ativos em
        carteiras.

        Esses dados quase não mudam. Guarde a resposta e consulte de novo poucas vezes.

        Args:
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. Um ticker antigo é trocado pelo
              ticker atual.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/stocks/profile",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"symbols": symbols}, stock_profile_params.StockProfileParams),
            ),
            cast_to=StockProfileResponse,
        )

    async def quote(
        self,
        *,
        symbols: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockQuoteResponse:
        """
        Preço, variação, volume, market cap, máxima e mínima do dia, faixa de 52 semanas
        e logo de ações, FIIs, BDRs, ETFs, units e índices brasileiros.

        Use para telas de cotação, carteiras, alertas de preço e widgets.

        Envie vários tickers em `symbols`, separados por vírgula. O número máximo de
        tickers por chamada depende do plano.

        Quando alguns tickers não existem, eles ficam fora de `results`. Se nenhum
        ticker tem cotação, a resposta retorna 404.

        Um ticker antigo é trocado pelo ticker atual. Nesse caso, `changed` é `true` e
        `requestedSymbol` guarda o ticker enviado.

        AXIA5 e AXIA6 retornam a cotação de uma ação AXIA3. Consulte a resolução de
        tickers para ver a proporção de conversão.

        Para a série de preços, use o
        [histórico de preços](https://brapi.dev/docs/acoes/historico). Para achar
        tickers válidos, use a [lista de tickers](https://brapi.dev/docs/tickers).

        Args:
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. Um ticker antigo é trocado pelo
              ticker atual.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/stocks/quote",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"symbols": symbols}, stock_quote_params.StockQuoteParams),
            ),
            cast_to=StockQuoteResponse,
        )

    async def statistics(
        self,
        *,
        symbols: str,
        end_date: str | Omit = omit,
        mode: Literal["current", "history"] | Omit = omit,
        period: Literal["annual", "quarterly"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockStatisticsResponse:
        """
        Múltiplos e indicadores por ação: P/L, P/VP, beta, dividend yield, lucro por
        ação, valor patrimonial por ação e market cap.

        Use para comparar empresas, montar screeners e acompanhar valuation.

        O padrão `mode=current` traz o valor atual. `mode=history` traz a série anual ou
        trimestral, conforme `period`, filtrada por `startDate` e `endDate`.

        Múltiplos que usam o preço mudam a cada pregão. Múltiplos que usam só o balanço
        mudam quando a empresa publica um novo resultado.

        Args:
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. Um ticker antigo é trocado pelo
              ticker atual.

          end_date: Data final no formato YYYY-MM-DD. Filtra pela data de encerramento do período.

          mode: `current` traz o valor atual. `history` traz a série definida por `period`.

          period: Período de cada linha: anual ou trimestral.

          start_date: Data inicial no formato YYYY-MM-DD. Filtra pela data de encerramento do período.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/stocks/statistics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "symbols": symbols,
                        "end_date": end_date,
                        "mode": mode,
                        "period": period,
                        "start_date": start_date,
                    },
                    stock_statistics_params.StockStatisticsParams,
                ),
            ),
            cast_to=StockStatisticsResponse,
        )

    async def value_added(
        self,
        *,
        symbols: str,
        end_date: str | Omit = omit,
        period: Literal["annual", "quarterly"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockValueAddedResponse:
        """
        Demonstração do valor adicionado de empresas listadas: a riqueza que a empresa
        gerou e como ela se divide entre pessoal, governo, credores e acionistas.

        Use para ver quanto a empresa paga de salários, impostos e juros, e quanto fica
        com os acionistas.

        O padrão é `period=annual`. Use `period=quarterly` para trimestres. `startDate`
        e `endDate` filtram pela data de encerramento do período.

        Os trimestres usam a mesma base, consolidada ou individual, do relatório anual
        do mesmo ano. Sem relatório anual, a base é a que tem o trimestre mais recente.
        Em empate, a consolidada vale. Lacunas não são preenchidas com a outra base. Um
        período sem os dados necessários para o cálculo retorna `null`.

        Args:
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. Um ticker antigo é trocado pelo
              ticker atual.

          end_date: Data final no formato YYYY-MM-DD. Filtra pela data de encerramento do período.

          period: Período de cada linha: anual ou trimestral.

          start_date: Data inicial no formato YYYY-MM-DD. Filtra pela data de encerramento do período.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/stocks/value-added",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "symbols": symbols,
                        "end_date": end_date,
                        "period": period,
                        "start_date": start_date,
                    },
                    stock_value_added_params.StockValueAddedParams,
                ),
            ),
            cast_to=StockValueAddedResponse,
        )


class StocksResourceWithRawResponse:
    def __init__(self, stocks: StocksResource) -> None:
        self._stocks = stocks

        self.balance_sheet = to_raw_response_wrapper(
            stocks.balance_sheet,
        )
        self.cash_flow = to_raw_response_wrapper(
            stocks.cash_flow,
        )
        self.dividends = to_raw_response_wrapper(
            stocks.dividends,
        )
        self.financial_data = to_raw_response_wrapper(
            stocks.financial_data,
        )
        self.historical = to_raw_response_wrapper(
            stocks.historical,
        )
        self.income_statement = to_raw_response_wrapper(
            stocks.income_statement,
        )
        self.profile = to_raw_response_wrapper(
            stocks.profile,
        )
        self.quote = to_raw_response_wrapper(
            stocks.quote,
        )
        self.statistics = to_raw_response_wrapper(
            stocks.statistics,
        )
        self.value_added = to_raw_response_wrapper(
            stocks.value_added,
        )


class AsyncStocksResourceWithRawResponse:
    def __init__(self, stocks: AsyncStocksResource) -> None:
        self._stocks = stocks

        self.balance_sheet = async_to_raw_response_wrapper(
            stocks.balance_sheet,
        )
        self.cash_flow = async_to_raw_response_wrapper(
            stocks.cash_flow,
        )
        self.dividends = async_to_raw_response_wrapper(
            stocks.dividends,
        )
        self.financial_data = async_to_raw_response_wrapper(
            stocks.financial_data,
        )
        self.historical = async_to_raw_response_wrapper(
            stocks.historical,
        )
        self.income_statement = async_to_raw_response_wrapper(
            stocks.income_statement,
        )
        self.profile = async_to_raw_response_wrapper(
            stocks.profile,
        )
        self.quote = async_to_raw_response_wrapper(
            stocks.quote,
        )
        self.statistics = async_to_raw_response_wrapper(
            stocks.statistics,
        )
        self.value_added = async_to_raw_response_wrapper(
            stocks.value_added,
        )


class StocksResourceWithStreamingResponse:
    def __init__(self, stocks: StocksResource) -> None:
        self._stocks = stocks

        self.balance_sheet = to_streamed_response_wrapper(
            stocks.balance_sheet,
        )
        self.cash_flow = to_streamed_response_wrapper(
            stocks.cash_flow,
        )
        self.dividends = to_streamed_response_wrapper(
            stocks.dividends,
        )
        self.financial_data = to_streamed_response_wrapper(
            stocks.financial_data,
        )
        self.historical = to_streamed_response_wrapper(
            stocks.historical,
        )
        self.income_statement = to_streamed_response_wrapper(
            stocks.income_statement,
        )
        self.profile = to_streamed_response_wrapper(
            stocks.profile,
        )
        self.quote = to_streamed_response_wrapper(
            stocks.quote,
        )
        self.statistics = to_streamed_response_wrapper(
            stocks.statistics,
        )
        self.value_added = to_streamed_response_wrapper(
            stocks.value_added,
        )


class AsyncStocksResourceWithStreamingResponse:
    def __init__(self, stocks: AsyncStocksResource) -> None:
        self._stocks = stocks

        self.balance_sheet = async_to_streamed_response_wrapper(
            stocks.balance_sheet,
        )
        self.cash_flow = async_to_streamed_response_wrapper(
            stocks.cash_flow,
        )
        self.dividends = async_to_streamed_response_wrapper(
            stocks.dividends,
        )
        self.financial_data = async_to_streamed_response_wrapper(
            stocks.financial_data,
        )
        self.historical = async_to_streamed_response_wrapper(
            stocks.historical,
        )
        self.income_statement = async_to_streamed_response_wrapper(
            stocks.income_statement,
        )
        self.profile = async_to_streamed_response_wrapper(
            stocks.profile,
        )
        self.quote = async_to_streamed_response_wrapper(
            stocks.quote,
        )
        self.statistics = async_to_streamed_response_wrapper(
            stocks.statistics,
        )
        self.value_added = async_to_streamed_response_wrapper(
            stocks.value_added,
        )
