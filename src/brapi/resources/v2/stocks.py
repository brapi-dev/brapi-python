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
    stock_screener_params,
    stock_cash_flow_params,
    stock_dividends_params,
    stock_historical_params,
    stock_statistics_params,
    stock_value_added_params,
    stock_balance_sheet_params,
    stock_financial_data_params,
    stock_income_statement_params,
    stock_insider_transactions_params,
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
from ...types.v2.stock_screener_response import StockScreenerResponse
from ...types.v2.stock_cash_flow_response import StockCashFlowResponse
from ...types.v2.stock_dividends_response import StockDividendsResponse
from ...types.v2.stock_historical_response import StockHistoricalResponse
from ...types.v2.stock_statistics_response import StockStatisticsResponse
from ...types.v2.stock_value_added_response import StockValueAddedResponse
from ...types.v2.stock_balance_sheet_response import StockBalanceSheetResponse
from ...types.v2.stock_financial_data_response import StockFinancialDataResponse
from ...types.v2.stock_income_statement_response import StockIncomeStatementResponse
from ...types.v2.stock_insider_transactions_response import StockInsiderTransactionsResponse

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
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. `requestedSymbol` identifica o
              ticker enviado e `symbol` identifica os dados retornados.

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
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. `requestedSymbol` identifica o
              ticker enviado e `symbol` identifica os dados retornados.

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

        Os proventos de LCAM3 e BRFS3 permanecem separados de RENT3 e MBRF3. PRGA3 usa
        BRFS3. MRFG3 usa MBRF3.

        Os proventos disponíveis podem ser consultados mesmo quando o ticker não tem
        cotação atual.

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
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. `requestedSymbol` identifica o
              ticker enviado e `symbol` identifica os dados retornados.

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
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. `requestedSymbol` identifica o
              ticker enviado e `symbol` identifica os dados retornados.

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

        LCAM3 e BRFS3 também mantêm históricos próprios, separados de RENT3 e MBRF3.
        PRGA3 usa a série de BRFS3. MRFG3 usa MBRF3.

        O histórico disponível pode ser consultado mesmo quando o ticker não tem cotação
        atual.

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
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. `requestedSymbol` identifica o
              ticker enviado e `symbol` identifica os dados retornados.

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
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. `requestedSymbol` identifica o
              ticker enviado e `symbol` identifica os dados retornados.

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

    def insider_transactions(
        self,
        *,
        symbols: str,
        all_versions: Literal["true", "false"] | Omit = omit,
        company_relation: Literal["company", "parent", "subsidiary", "all"] | Omit = omit,
        direction: Literal["credit", "debit"] | Omit = omit,
        end_date: str | Omit = omit,
        limit: int | Omit = omit,
        movement_type: str | Omit = omit,
        page: int | Omit = omit,
        role_group: Literal["controller", "board", "director", "fiscalCouncil", "statutoryBody"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockInsiderTransactionsResponse:
        """
        Movimentações de valores mobiliários por administradores, controladores e
        pessoas vinculadas, por empresa e período. Os relatórios são mensais. A
        atualização ocorre semanalmente.

        O ticker identifica a empresa do relatório. PETR3 e PETR4 retornam os mesmos
        dados. Os registros agrupam pessoas por cargo, sem identificar cada pessoa ou o
        ticker negociado.

        `direction` indica entrada ou saída da posição, inclusive transferências. Use
        `movementType` para identificar compras e vendas.

        A resposta traz as movimentações mais recentes primeiro e a última versão de
        cada relatório. Use `allVersions=true` para incluir versões anteriores. Não some
        essas versões, pois elas podem repetir movimentações. Saldos iniciais não entram
        na lista.

        Plano Pro. PETR4, MGLU3, VALE3 e ITUB4 permitem testes gratuitos, sem token.

        Args:
          symbols: Tickers separados por vírgula. Máximo de 20. Cada ticker identifica a empresa
              que apresenta o relatório.

          all_versions: Inclui versões anteriores dos relatórios. Padrão: false. Versões anteriores
              podem repetir movimentações.

          company_relation: Empresa que emite o valor mobiliário: a própria empresa, sua controladora ou sua
              controlada.

          direction: Entrada ou saída da posição. Inclui transferências e outras movimentações.

          end_date: Data final da movimentação. Padrão: hoje.

          limit: Máximo de movimentações por empresa e página.

          movement_type: Tipo de movimentação, com o texto exato do relatório.

          page: Página de cada empresa.

          role_group: Grupo de cargos. Cada grupo inclui pessoas vinculadas.

          start_date: Data inicial da movimentação. Padrão: 365 dias antes de endDate.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/stocks/insider-transactions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "symbols": symbols,
                        "all_versions": all_versions,
                        "company_relation": company_relation,
                        "direction": direction,
                        "end_date": end_date,
                        "limit": limit,
                        "movement_type": movement_type,
                        "page": page,
                        "role_group": role_group,
                        "start_date": start_date,
                    },
                    stock_insider_transactions_params.StockInsiderTransactionsParams,
                ),
            ),
            cast_to=StockInsiderTransactionsResponse,
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
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. `requestedSymbol` identifica o
              ticker enviado e `symbol` identifica os dados retornados.

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
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. `requestedSymbol` identifica o
              ticker enviado e `symbol` identifica os dados retornados.

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

    def screener(
        self,
        *,
        book_value_per_share_max: float | Omit = omit,
        book_value_per_share_min: float | Omit = omit,
        change_percent_max: float | Omit = omit,
        change_percent_min: float | Omit = omit,
        current_ratio_max: float | Omit = omit,
        current_ratio_min: float | Omit = omit,
        debt_to_equity_max: float | Omit = omit,
        debt_to_equity_min: float | Omit = omit,
        dividend_yield_max: float | Omit = omit,
        dividend_yield_min: float | Omit = omit,
        earnings_growth_annual_max: float | Omit = omit,
        earnings_growth_annual_min: float | Omit = omit,
        earnings_growth_max: float | Omit = omit,
        earnings_growth_min: float | Omit = omit,
        earnings_per_share_max: float | Omit = omit,
        earnings_per_share_min: float | Omit = omit,
        ebitda_margin_max: float | Omit = omit,
        ebitda_margin_min: float | Omit = omit,
        ebitda_max: float | Omit = omit,
        ebitda_min: float | Omit = omit,
        enterprise_to_ebitda_max: float | Omit = omit,
        enterprise_to_ebitda_min: float | Omit = omit,
        enterprise_to_revenue_max: float | Omit = omit,
        enterprise_to_revenue_min: float | Omit = omit,
        enterprise_value_max: float | Omit = omit,
        enterprise_value_min: float | Omit = omit,
        fifty_two_week_change_max: float | Omit = omit,
        fifty_two_week_change_min: float | Omit = omit,
        free_cashflow_max: float | Omit = omit,
        free_cashflow_min: float | Omit = omit,
        gross_margin_max: float | Omit = omit,
        gross_margin_min: float | Omit = omit,
        last_price_max: float | Omit = omit,
        last_price_min: float | Omit = omit,
        limit: int | Omit = omit,
        market_cap_max: float | Omit = omit,
        market_cap_min: float | Omit = omit,
        net_debt_to_ebitda_max: float | Omit = omit,
        net_debt_to_ebitda_min: float | Omit = omit,
        net_margin_max: float | Omit = omit,
        net_margin_min: float | Omit = omit,
        operating_margin_max: float | Omit = omit,
        operating_margin_min: float | Omit = omit,
        page: int | Omit = omit,
        peg_ratio_max: float | Omit = omit,
        peg_ratio_min: float | Omit = omit,
        price_to_book_max: float | Omit = omit,
        price_to_book_min: float | Omit = omit,
        quick_ratio_max: float | Omit = omit,
        quick_ratio_min: float | Omit = omit,
        return_on_assets_max: float | Omit = omit,
        return_on_assets_min: float | Omit = omit,
        return_on_equity_max: float | Omit = omit,
        return_on_equity_min: float | Omit = omit,
        revenue_growth_annual_max: float | Omit = omit,
        revenue_growth_annual_min: float | Omit = omit,
        revenue_growth_max: float | Omit = omit,
        revenue_growth_min: float | Omit = omit,
        search: str | Omit = omit,
        sector: str | Omit = omit,
        sort_by: Literal[
            "symbol",
            "name",
            "lastPrice",
            "changePercent",
            "volume",
            "marketCap",
            "trailingPE",
            "priceToBook",
            "enterpriseToEbitda",
            "enterpriseToRevenue",
            "pegRatio",
            "earningsPerShare",
            "bookValuePerShare",
            "netMargin",
            "enterpriseValue",
            "fiftyTwoWeekChange",
            "dividendYield",
            "returnOnEquity",
            "returnOnAssets",
            "grossMargin",
            "ebitdaMargin",
            "operatingMargin",
            "debtToEquity",
            "netDebtToEbitda",
            "currentRatio",
            "quickRatio",
            "revenueGrowth",
            "earningsGrowth",
            "revenueGrowthAnnual",
            "earningsGrowthAnnual",
            "totalRevenue",
            "ebitda",
            "freeCashflow",
            "totalDebt",
            "totalCash",
        ]
        | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        subsector: str | Omit = omit,
        sub_type: Literal["stock", "unit", "fii", "etf", "fi-infra", "fi-agro", "fip", "fidc", "bdr"] | Omit = omit,
        total_cash_max: float | Omit = omit,
        total_cash_min: float | Omit = omit,
        total_debt_max: float | Omit = omit,
        total_debt_min: float | Omit = omit,
        total_revenue_max: float | Omit = omit,
        total_revenue_min: float | Omit = omit,
        trailing_pe_max: float | Omit = omit,
        trailing_pe_min: float | Omit = omit,
        type: Literal["stock", "fund", "bdr"] | Omit = omit,
        volume_max: float | Omit = omit,
        volume_min: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockScreenerResponse:
        """
        Filtra e ordena ações da B3 por preço e indicadores fundamentalistas, como P/L,
        P/VP, dividend yield e ROE. Uma chamada percorre todas as ações.

        Cada indicador aceita `{chave}Min` e `{chave}Max`. Os limites são inclusivos e
        usam a mesma unidade da resposta. Frações seguem `/api/v2/stocks/statistics` e
        `/api/v2/stocks/financial-data`: 6% é `0.06`. Um filtro remove os ativos sem o
        dado. Na ordenação, os nulos ficam no fim.

        Exemplos:

        - P/L entre 0 e 8 e dividend yield de pelo menos 6%:
          `?trailingPEMin=0&trailingPEMax=8&dividendYieldMin=0.06&sortBy=dividendYield`
        - ROE de pelo menos 15%, do maior para o menor:
          `?returnOnEquityMin=0.15&sortBy=returnOnEquity`

        Empresas com prejuízo têm P/L negativo. Para excluí-las, envie `trailingPEMin=0`
        junto com `trailingPEMax`.

        `quote` e `dividendYield` usam o último preço. P/L, P/VP e os outros indicadores
        usam o preço da atualização diária dos fundamentos. Em units, P/L e P/VP usam o
        último preço da unit. `dividendYield` soma os proventos em dinheiro dos últimos
        12 meses.

        Planos Startup e Pro. Os indicadores do plano Pro não vêm em `metrics` no plano
        Startup. Um filtro ou uma ordenação com esses indicadores no plano Startup
        retorna 403.

        | Indicador                    | Chave                  | Unidade                    | Plano         |
        | ---------------------------- | ---------------------- | -------------------------- | ------------- |
        | Preço                        | `lastPrice`            | reais                      | Startup e Pro |
        | Variação no dia              | `changePercent`        | porcentagem (2.81 = 2,81%) | Startup e Pro |
        | Volume                       | `volume`               | ações                      | Startup e Pro |
        | Valor de mercado             | `marketCap`            | reais                      | Startup e Pro |
        | P/L                          | `trailingPE`           | múltiplo                   | Startup e Pro |
        | P/VP                         | `priceToBook`          | múltiplo                   | Startup e Pro |
        | EV/EBITDA                    | `enterpriseToEbitda`   | múltiplo                   | Startup e Pro |
        | EV/Receita                   | `enterpriseToRevenue`  | múltiplo                   | Startup e Pro |
        | PEG                          | `pegRatio`             | múltiplo                   | Startup e Pro |
        | LPA                          | `earningsPerShare`     | reais                      | Startup e Pro |
        | VPA                          | `bookValuePerShare`    | reais                      | Startup e Pro |
        | Margem líquida               | `netMargin`            | fração (0.06 = 6%)         | Startup e Pro |
        | Valor da firma               | `enterpriseValue`      | reais                      | Startup e Pro |
        | Variação 52 semanas          | `fiftyTwoWeekChange`   | fração (0.06 = 6%)         | Startup e Pro |
        | Dividend yield               | `dividendYield`        | fração (0.06 = 6%)         | Startup e Pro |
        | ROE                          | `returnOnEquity`       | fração (0.06 = 6%)         | Pro           |
        | ROA                          | `returnOnAssets`       | fração (0.06 = 6%)         | Pro           |
        | Margem bruta                 | `grossMargin`          | fração (0.06 = 6%)         | Pro           |
        | Margem EBITDA                | `ebitdaMargin`         | fração (0.06 = 6%)         | Pro           |
        | Margem operacional           | `operatingMargin`      | fração (0.06 = 6%)         | Pro           |
        | Dívida/PL                    | `debtToEquity`         | múltiplo                   | Pro           |
        | Dívida líquida/EBITDA        | `netDebtToEbitda`      | múltiplo                   | Pro           |
        | Liquidez corrente            | `currentRatio`         | múltiplo                   | Pro           |
        | Liquidez seca                | `quickRatio`           | múltiplo                   | Pro           |
        | Crescimento da receita       | `revenueGrowth`        | fração (0.06 = 6%)         | Pro           |
        | Crescimento do lucro         | `earningsGrowth`       | fração (0.06 = 6%)         | Pro           |
        | Crescimento anual da receita | `revenueGrowthAnnual`  | fração (0.06 = 6%)         | Pro           |
        | Crescimento anual do lucro   | `earningsGrowthAnnual` | fração (0.06 = 6%)         | Pro           |
        | Receita                      | `totalRevenue`         | reais                      | Pro           |
        | EBITDA                       | `ebitda`               | reais                      | Pro           |
        | Fluxo de caixa livre         | `freeCashflow`         | reais                      | Pro           |
        | Dívida bruta                 | `totalDebt`            | reais                      | Pro           |
        | Caixa                        | `totalCash`            | reais                      | Pro           |

        Args:
          book_value_per_share_max: VPA: valor máximo, inclusive. Unidade: reais. Plano Startup e Pro.

          book_value_per_share_min: VPA: valor mínimo, inclusive. Unidade: reais. Plano Startup e Pro.

          change_percent_max: Variação no dia: valor máximo, inclusive. Unidade: porcentagem (2.81 = 2,81%).
              Plano Startup e Pro.

          change_percent_min: Variação no dia: valor mínimo, inclusive. Unidade: porcentagem (2.81 = 2,81%).
              Plano Startup e Pro.

          current_ratio_max: Liquidez corrente: valor máximo, inclusive. Unidade: múltiplo. Plano Pro.

          current_ratio_min: Liquidez corrente: valor mínimo, inclusive. Unidade: múltiplo. Plano Pro.

          debt_to_equity_max: Dívida/PL: valor máximo, inclusive. Unidade: múltiplo. Plano Pro.

          debt_to_equity_min: Dívida/PL: valor mínimo, inclusive. Unidade: múltiplo. Plano Pro.

          dividend_yield_max: Dividend yield: valor máximo, inclusive. Unidade: fração (0.06 = 6%). Plano
              Startup e Pro.

          dividend_yield_min: Dividend yield: valor mínimo, inclusive. Unidade: fração (0.06 = 6%). Plano
              Startup e Pro.

          earnings_growth_annual_max: Crescimento anual do lucro: valor máximo, inclusive. Unidade: fração (0.06 =
              6%). Plano Pro.

          earnings_growth_annual_min: Crescimento anual do lucro: valor mínimo, inclusive. Unidade: fração (0.06 =
              6%). Plano Pro.

          earnings_growth_max: Crescimento do lucro: valor máximo, inclusive. Unidade: fração (0.06 = 6%).
              Plano Pro.

          earnings_growth_min: Crescimento do lucro: valor mínimo, inclusive. Unidade: fração (0.06 = 6%).
              Plano Pro.

          earnings_per_share_max: LPA: valor máximo, inclusive. Unidade: reais. Plano Startup e Pro.

          earnings_per_share_min: LPA: valor mínimo, inclusive. Unidade: reais. Plano Startup e Pro.

          ebitda_margin_max: Margem EBITDA: valor máximo, inclusive. Unidade: fração (0.06 = 6%). Plano Pro.

          ebitda_margin_min: Margem EBITDA: valor mínimo, inclusive. Unidade: fração (0.06 = 6%). Plano Pro.

          ebitda_max: EBITDA: valor máximo, inclusive. Unidade: reais. Plano Pro.

          ebitda_min: EBITDA: valor mínimo, inclusive. Unidade: reais. Plano Pro.

          enterprise_to_ebitda_max: EV/EBITDA: valor máximo, inclusive. Unidade: múltiplo. Plano Startup e Pro.

          enterprise_to_ebitda_min: EV/EBITDA: valor mínimo, inclusive. Unidade: múltiplo. Plano Startup e Pro.

          enterprise_to_revenue_max: EV/Receita: valor máximo, inclusive. Unidade: múltiplo. Plano Startup e Pro.

          enterprise_to_revenue_min: EV/Receita: valor mínimo, inclusive. Unidade: múltiplo. Plano Startup e Pro.

          enterprise_value_max: Valor da firma: valor máximo, inclusive. Unidade: reais. Plano Startup e Pro.

          enterprise_value_min: Valor da firma: valor mínimo, inclusive. Unidade: reais. Plano Startup e Pro.

          fifty_two_week_change_max: Variação 52 semanas: valor máximo, inclusive. Unidade: fração (0.06 = 6%). Plano
              Startup e Pro.

          fifty_two_week_change_min: Variação 52 semanas: valor mínimo, inclusive. Unidade: fração (0.06 = 6%). Plano
              Startup e Pro.

          free_cashflow_max: Fluxo de caixa livre: valor máximo, inclusive. Unidade: reais. Plano Pro.

          free_cashflow_min: Fluxo de caixa livre: valor mínimo, inclusive. Unidade: reais. Plano Pro.

          gross_margin_max: Margem bruta: valor máximo, inclusive. Unidade: fração (0.06 = 6%). Plano Pro.

          gross_margin_min: Margem bruta: valor mínimo, inclusive. Unidade: fração (0.06 = 6%). Plano Pro.

          last_price_max: Preço: valor máximo, inclusive. Unidade: reais. Plano Startup e Pro.

          last_price_min: Preço: valor mínimo, inclusive. Unidade: reais. Plano Startup e Pro.

          limit: Itens por página. Máximo: 200.

          market_cap_max: Valor de mercado: valor máximo, inclusive. Unidade: reais. Plano Startup e Pro.

          market_cap_min: Valor de mercado: valor mínimo, inclusive. Unidade: reais. Plano Startup e Pro.

          net_debt_to_ebitda_max: Dívida líquida/EBITDA: valor máximo, inclusive. Unidade: múltiplo. Plano Pro.

          net_debt_to_ebitda_min: Dívida líquida/EBITDA: valor mínimo, inclusive. Unidade: múltiplo. Plano Pro.

          net_margin_max: Margem líquida: valor máximo, inclusive. Unidade: fração (0.06 = 6%). Plano
              Startup e Pro.

          net_margin_min: Margem líquida: valor mínimo, inclusive. Unidade: fração (0.06 = 6%). Plano
              Startup e Pro.

          operating_margin_max: Margem operacional: valor máximo, inclusive. Unidade: fração (0.06 = 6%). Plano
              Pro.

          operating_margin_min: Margem operacional: valor mínimo, inclusive. Unidade: fração (0.06 = 6%). Plano
              Pro.

          page: Número da página. Começa em 1.

          peg_ratio_max: PEG: valor máximo, inclusive. Unidade: múltiplo. Plano Startup e Pro.

          peg_ratio_min: PEG: valor mínimo, inclusive. Unidade: múltiplo. Plano Startup e Pro.

          price_to_book_max: P/VP: valor máximo, inclusive. Unidade: múltiplo. Plano Startup e Pro.

          price_to_book_min: P/VP: valor mínimo, inclusive. Unidade: múltiplo. Plano Startup e Pro.

          quick_ratio_max: Liquidez seca: valor máximo, inclusive. Unidade: múltiplo. Plano Pro.

          quick_ratio_min: Liquidez seca: valor mínimo, inclusive. Unidade: múltiplo. Plano Pro.

          return_on_assets_max: ROA: valor máximo, inclusive. Unidade: fração (0.06 = 6%). Plano Pro.

          return_on_assets_min: ROA: valor mínimo, inclusive. Unidade: fração (0.06 = 6%). Plano Pro.

          return_on_equity_max: ROE: valor máximo, inclusive. Unidade: fração (0.06 = 6%). Plano Pro.

          return_on_equity_min: ROE: valor mínimo, inclusive. Unidade: fração (0.06 = 6%). Plano Pro.

          revenue_growth_annual_max: Crescimento anual da receita: valor máximo, inclusive. Unidade: fração (0.06 =
              6%). Plano Pro.

          revenue_growth_annual_min: Crescimento anual da receita: valor mínimo, inclusive. Unidade: fração (0.06 =
              6%). Plano Pro.

          revenue_growth_max: Crescimento da receita: valor máximo, inclusive. Unidade: fração (0.06 = 6%).
              Plano Pro.

          revenue_growth_min: Crescimento da receita: valor mínimo, inclusive. Unidade: fração (0.06 = 6%).
              Plano Pro.

          search: Parte do ticker, do nome da empresa ou de um ticker antigo.

          sector: Setor. Aceita parte do nome.

          sort_by: Campo de ordenação: uma chave de métrica, `symbol` ou `name`. Valores nulos
              ficam no fim.

          sort_order: Ordem. Padrão: `desc`.

          subsector: Subsetor. Nome exato.

          sub_type: Subtipo do ativo: stock, unit, fii, etf, fi-infra, fi-agro, fip, fidc ou bdr.

          total_cash_max: Caixa: valor máximo, inclusive. Unidade: reais. Plano Pro.

          total_cash_min: Caixa: valor mínimo, inclusive. Unidade: reais. Plano Pro.

          total_debt_max: Dívida bruta: valor máximo, inclusive. Unidade: reais. Plano Pro.

          total_debt_min: Dívida bruta: valor mínimo, inclusive. Unidade: reais. Plano Pro.

          total_revenue_max: Receita: valor máximo, inclusive. Unidade: reais. Plano Pro.

          total_revenue_min: Receita: valor mínimo, inclusive. Unidade: reais. Plano Pro.

          trailing_pe_max: P/L: valor máximo, inclusive. Unidade: múltiplo. Plano Startup e Pro.

          trailing_pe_min: P/L: valor mínimo, inclusive. Unidade: múltiplo. Plano Startup e Pro.

          type: Tipo do ativo. Padrão: `stock`.

          volume_max: Volume: valor máximo, inclusive. Unidade: ações. Plano Startup e Pro.

          volume_min: Volume: valor mínimo, inclusive. Unidade: ações. Plano Startup e Pro.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/stocks/screener",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "book_value_per_share_max": book_value_per_share_max,
                        "book_value_per_share_min": book_value_per_share_min,
                        "change_percent_max": change_percent_max,
                        "change_percent_min": change_percent_min,
                        "current_ratio_max": current_ratio_max,
                        "current_ratio_min": current_ratio_min,
                        "debt_to_equity_max": debt_to_equity_max,
                        "debt_to_equity_min": debt_to_equity_min,
                        "dividend_yield_max": dividend_yield_max,
                        "dividend_yield_min": dividend_yield_min,
                        "earnings_growth_annual_max": earnings_growth_annual_max,
                        "earnings_growth_annual_min": earnings_growth_annual_min,
                        "earnings_growth_max": earnings_growth_max,
                        "earnings_growth_min": earnings_growth_min,
                        "earnings_per_share_max": earnings_per_share_max,
                        "earnings_per_share_min": earnings_per_share_min,
                        "ebitda_margin_max": ebitda_margin_max,
                        "ebitda_margin_min": ebitda_margin_min,
                        "ebitda_max": ebitda_max,
                        "ebitda_min": ebitda_min,
                        "enterprise_to_ebitda_max": enterprise_to_ebitda_max,
                        "enterprise_to_ebitda_min": enterprise_to_ebitda_min,
                        "enterprise_to_revenue_max": enterprise_to_revenue_max,
                        "enterprise_to_revenue_min": enterprise_to_revenue_min,
                        "enterprise_value_max": enterprise_value_max,
                        "enterprise_value_min": enterprise_value_min,
                        "fifty_two_week_change_max": fifty_two_week_change_max,
                        "fifty_two_week_change_min": fifty_two_week_change_min,
                        "free_cashflow_max": free_cashflow_max,
                        "free_cashflow_min": free_cashflow_min,
                        "gross_margin_max": gross_margin_max,
                        "gross_margin_min": gross_margin_min,
                        "last_price_max": last_price_max,
                        "last_price_min": last_price_min,
                        "limit": limit,
                        "market_cap_max": market_cap_max,
                        "market_cap_min": market_cap_min,
                        "net_debt_to_ebitda_max": net_debt_to_ebitda_max,
                        "net_debt_to_ebitda_min": net_debt_to_ebitda_min,
                        "net_margin_max": net_margin_max,
                        "net_margin_min": net_margin_min,
                        "operating_margin_max": operating_margin_max,
                        "operating_margin_min": operating_margin_min,
                        "page": page,
                        "peg_ratio_max": peg_ratio_max,
                        "peg_ratio_min": peg_ratio_min,
                        "price_to_book_max": price_to_book_max,
                        "price_to_book_min": price_to_book_min,
                        "quick_ratio_max": quick_ratio_max,
                        "quick_ratio_min": quick_ratio_min,
                        "return_on_assets_max": return_on_assets_max,
                        "return_on_assets_min": return_on_assets_min,
                        "return_on_equity_max": return_on_equity_max,
                        "return_on_equity_min": return_on_equity_min,
                        "revenue_growth_annual_max": revenue_growth_annual_max,
                        "revenue_growth_annual_min": revenue_growth_annual_min,
                        "revenue_growth_max": revenue_growth_max,
                        "revenue_growth_min": revenue_growth_min,
                        "search": search,
                        "sector": sector,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "subsector": subsector,
                        "sub_type": sub_type,
                        "total_cash_max": total_cash_max,
                        "total_cash_min": total_cash_min,
                        "total_debt_max": total_debt_max,
                        "total_debt_min": total_debt_min,
                        "total_revenue_max": total_revenue_max,
                        "total_revenue_min": total_revenue_min,
                        "trailing_pe_max": trailing_pe_max,
                        "trailing_pe_min": trailing_pe_min,
                        "type": type,
                        "volume_max": volume_max,
                        "volume_min": volume_min,
                    },
                    stock_screener_params.StockScreenerParams,
                ),
            ),
            cast_to=StockScreenerResponse,
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
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. `requestedSymbol` identifica o
              ticker enviado e `symbol` identifica os dados retornados.

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
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. `requestedSymbol` identifica o
              ticker enviado e `symbol` identifica os dados retornados.

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
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. `requestedSymbol` identifica o
              ticker enviado e `symbol` identifica os dados retornados.

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
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. `requestedSymbol` identifica o
              ticker enviado e `symbol` identifica os dados retornados.

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

        Os proventos de LCAM3 e BRFS3 permanecem separados de RENT3 e MBRF3. PRGA3 usa
        BRFS3. MRFG3 usa MBRF3.

        Os proventos disponíveis podem ser consultados mesmo quando o ticker não tem
        cotação atual.

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
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. `requestedSymbol` identifica o
              ticker enviado e `symbol` identifica os dados retornados.

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
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. `requestedSymbol` identifica o
              ticker enviado e `symbol` identifica os dados retornados.

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

        LCAM3 e BRFS3 também mantêm históricos próprios, separados de RENT3 e MBRF3.
        PRGA3 usa a série de BRFS3. MRFG3 usa MBRF3.

        O histórico disponível pode ser consultado mesmo quando o ticker não tem cotação
        atual.

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
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. `requestedSymbol` identifica o
              ticker enviado e `symbol` identifica os dados retornados.

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
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. `requestedSymbol` identifica o
              ticker enviado e `symbol` identifica os dados retornados.

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

    async def insider_transactions(
        self,
        *,
        symbols: str,
        all_versions: Literal["true", "false"] | Omit = omit,
        company_relation: Literal["company", "parent", "subsidiary", "all"] | Omit = omit,
        direction: Literal["credit", "debit"] | Omit = omit,
        end_date: str | Omit = omit,
        limit: int | Omit = omit,
        movement_type: str | Omit = omit,
        page: int | Omit = omit,
        role_group: Literal["controller", "board", "director", "fiscalCouncil", "statutoryBody"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockInsiderTransactionsResponse:
        """
        Movimentações de valores mobiliários por administradores, controladores e
        pessoas vinculadas, por empresa e período. Os relatórios são mensais. A
        atualização ocorre semanalmente.

        O ticker identifica a empresa do relatório. PETR3 e PETR4 retornam os mesmos
        dados. Os registros agrupam pessoas por cargo, sem identificar cada pessoa ou o
        ticker negociado.

        `direction` indica entrada ou saída da posição, inclusive transferências. Use
        `movementType` para identificar compras e vendas.

        A resposta traz as movimentações mais recentes primeiro e a última versão de
        cada relatório. Use `allVersions=true` para incluir versões anteriores. Não some
        essas versões, pois elas podem repetir movimentações. Saldos iniciais não entram
        na lista.

        Plano Pro. PETR4, MGLU3, VALE3 e ITUB4 permitem testes gratuitos, sem token.

        Args:
          symbols: Tickers separados por vírgula. Máximo de 20. Cada ticker identifica a empresa
              que apresenta o relatório.

          all_versions: Inclui versões anteriores dos relatórios. Padrão: false. Versões anteriores
              podem repetir movimentações.

          company_relation: Empresa que emite o valor mobiliário: a própria empresa, sua controladora ou sua
              controlada.

          direction: Entrada ou saída da posição. Inclui transferências e outras movimentações.

          end_date: Data final da movimentação. Padrão: hoje.

          limit: Máximo de movimentações por empresa e página.

          movement_type: Tipo de movimentação, com o texto exato do relatório.

          page: Página de cada empresa.

          role_group: Grupo de cargos. Cada grupo inclui pessoas vinculadas.

          start_date: Data inicial da movimentação. Padrão: 365 dias antes de endDate.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/stocks/insider-transactions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "symbols": symbols,
                        "all_versions": all_versions,
                        "company_relation": company_relation,
                        "direction": direction,
                        "end_date": end_date,
                        "limit": limit,
                        "movement_type": movement_type,
                        "page": page,
                        "role_group": role_group,
                        "start_date": start_date,
                    },
                    stock_insider_transactions_params.StockInsiderTransactionsParams,
                ),
            ),
            cast_to=StockInsiderTransactionsResponse,
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
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. `requestedSymbol` identifica o
              ticker enviado e `symbol` identifica os dados retornados.

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
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. `requestedSymbol` identifica o
              ticker enviado e `symbol` identifica os dados retornados.

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

    async def screener(
        self,
        *,
        book_value_per_share_max: float | Omit = omit,
        book_value_per_share_min: float | Omit = omit,
        change_percent_max: float | Omit = omit,
        change_percent_min: float | Omit = omit,
        current_ratio_max: float | Omit = omit,
        current_ratio_min: float | Omit = omit,
        debt_to_equity_max: float | Omit = omit,
        debt_to_equity_min: float | Omit = omit,
        dividend_yield_max: float | Omit = omit,
        dividend_yield_min: float | Omit = omit,
        earnings_growth_annual_max: float | Omit = omit,
        earnings_growth_annual_min: float | Omit = omit,
        earnings_growth_max: float | Omit = omit,
        earnings_growth_min: float | Omit = omit,
        earnings_per_share_max: float | Omit = omit,
        earnings_per_share_min: float | Omit = omit,
        ebitda_margin_max: float | Omit = omit,
        ebitda_margin_min: float | Omit = omit,
        ebitda_max: float | Omit = omit,
        ebitda_min: float | Omit = omit,
        enterprise_to_ebitda_max: float | Omit = omit,
        enterprise_to_ebitda_min: float | Omit = omit,
        enterprise_to_revenue_max: float | Omit = omit,
        enterprise_to_revenue_min: float | Omit = omit,
        enterprise_value_max: float | Omit = omit,
        enterprise_value_min: float | Omit = omit,
        fifty_two_week_change_max: float | Omit = omit,
        fifty_two_week_change_min: float | Omit = omit,
        free_cashflow_max: float | Omit = omit,
        free_cashflow_min: float | Omit = omit,
        gross_margin_max: float | Omit = omit,
        gross_margin_min: float | Omit = omit,
        last_price_max: float | Omit = omit,
        last_price_min: float | Omit = omit,
        limit: int | Omit = omit,
        market_cap_max: float | Omit = omit,
        market_cap_min: float | Omit = omit,
        net_debt_to_ebitda_max: float | Omit = omit,
        net_debt_to_ebitda_min: float | Omit = omit,
        net_margin_max: float | Omit = omit,
        net_margin_min: float | Omit = omit,
        operating_margin_max: float | Omit = omit,
        operating_margin_min: float | Omit = omit,
        page: int | Omit = omit,
        peg_ratio_max: float | Omit = omit,
        peg_ratio_min: float | Omit = omit,
        price_to_book_max: float | Omit = omit,
        price_to_book_min: float | Omit = omit,
        quick_ratio_max: float | Omit = omit,
        quick_ratio_min: float | Omit = omit,
        return_on_assets_max: float | Omit = omit,
        return_on_assets_min: float | Omit = omit,
        return_on_equity_max: float | Omit = omit,
        return_on_equity_min: float | Omit = omit,
        revenue_growth_annual_max: float | Omit = omit,
        revenue_growth_annual_min: float | Omit = omit,
        revenue_growth_max: float | Omit = omit,
        revenue_growth_min: float | Omit = omit,
        search: str | Omit = omit,
        sector: str | Omit = omit,
        sort_by: Literal[
            "symbol",
            "name",
            "lastPrice",
            "changePercent",
            "volume",
            "marketCap",
            "trailingPE",
            "priceToBook",
            "enterpriseToEbitda",
            "enterpriseToRevenue",
            "pegRatio",
            "earningsPerShare",
            "bookValuePerShare",
            "netMargin",
            "enterpriseValue",
            "fiftyTwoWeekChange",
            "dividendYield",
            "returnOnEquity",
            "returnOnAssets",
            "grossMargin",
            "ebitdaMargin",
            "operatingMargin",
            "debtToEquity",
            "netDebtToEbitda",
            "currentRatio",
            "quickRatio",
            "revenueGrowth",
            "earningsGrowth",
            "revenueGrowthAnnual",
            "earningsGrowthAnnual",
            "totalRevenue",
            "ebitda",
            "freeCashflow",
            "totalDebt",
            "totalCash",
        ]
        | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        subsector: str | Omit = omit,
        sub_type: Literal["stock", "unit", "fii", "etf", "fi-infra", "fi-agro", "fip", "fidc", "bdr"] | Omit = omit,
        total_cash_max: float | Omit = omit,
        total_cash_min: float | Omit = omit,
        total_debt_max: float | Omit = omit,
        total_debt_min: float | Omit = omit,
        total_revenue_max: float | Omit = omit,
        total_revenue_min: float | Omit = omit,
        trailing_pe_max: float | Omit = omit,
        trailing_pe_min: float | Omit = omit,
        type: Literal["stock", "fund", "bdr"] | Omit = omit,
        volume_max: float | Omit = omit,
        volume_min: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockScreenerResponse:
        """
        Filtra e ordena ações da B3 por preço e indicadores fundamentalistas, como P/L,
        P/VP, dividend yield e ROE. Uma chamada percorre todas as ações.

        Cada indicador aceita `{chave}Min` e `{chave}Max`. Os limites são inclusivos e
        usam a mesma unidade da resposta. Frações seguem `/api/v2/stocks/statistics` e
        `/api/v2/stocks/financial-data`: 6% é `0.06`. Um filtro remove os ativos sem o
        dado. Na ordenação, os nulos ficam no fim.

        Exemplos:

        - P/L entre 0 e 8 e dividend yield de pelo menos 6%:
          `?trailingPEMin=0&trailingPEMax=8&dividendYieldMin=0.06&sortBy=dividendYield`
        - ROE de pelo menos 15%, do maior para o menor:
          `?returnOnEquityMin=0.15&sortBy=returnOnEquity`

        Empresas com prejuízo têm P/L negativo. Para excluí-las, envie `trailingPEMin=0`
        junto com `trailingPEMax`.

        `quote` e `dividendYield` usam o último preço. P/L, P/VP e os outros indicadores
        usam o preço da atualização diária dos fundamentos. Em units, P/L e P/VP usam o
        último preço da unit. `dividendYield` soma os proventos em dinheiro dos últimos
        12 meses.

        Planos Startup e Pro. Os indicadores do plano Pro não vêm em `metrics` no plano
        Startup. Um filtro ou uma ordenação com esses indicadores no plano Startup
        retorna 403.

        | Indicador                    | Chave                  | Unidade                    | Plano         |
        | ---------------------------- | ---------------------- | -------------------------- | ------------- |
        | Preço                        | `lastPrice`            | reais                      | Startup e Pro |
        | Variação no dia              | `changePercent`        | porcentagem (2.81 = 2,81%) | Startup e Pro |
        | Volume                       | `volume`               | ações                      | Startup e Pro |
        | Valor de mercado             | `marketCap`            | reais                      | Startup e Pro |
        | P/L                          | `trailingPE`           | múltiplo                   | Startup e Pro |
        | P/VP                         | `priceToBook`          | múltiplo                   | Startup e Pro |
        | EV/EBITDA                    | `enterpriseToEbitda`   | múltiplo                   | Startup e Pro |
        | EV/Receita                   | `enterpriseToRevenue`  | múltiplo                   | Startup e Pro |
        | PEG                          | `pegRatio`             | múltiplo                   | Startup e Pro |
        | LPA                          | `earningsPerShare`     | reais                      | Startup e Pro |
        | VPA                          | `bookValuePerShare`    | reais                      | Startup e Pro |
        | Margem líquida               | `netMargin`            | fração (0.06 = 6%)         | Startup e Pro |
        | Valor da firma               | `enterpriseValue`      | reais                      | Startup e Pro |
        | Variação 52 semanas          | `fiftyTwoWeekChange`   | fração (0.06 = 6%)         | Startup e Pro |
        | Dividend yield               | `dividendYield`        | fração (0.06 = 6%)         | Startup e Pro |
        | ROE                          | `returnOnEquity`       | fração (0.06 = 6%)         | Pro           |
        | ROA                          | `returnOnAssets`       | fração (0.06 = 6%)         | Pro           |
        | Margem bruta                 | `grossMargin`          | fração (0.06 = 6%)         | Pro           |
        | Margem EBITDA                | `ebitdaMargin`         | fração (0.06 = 6%)         | Pro           |
        | Margem operacional           | `operatingMargin`      | fração (0.06 = 6%)         | Pro           |
        | Dívida/PL                    | `debtToEquity`         | múltiplo                   | Pro           |
        | Dívida líquida/EBITDA        | `netDebtToEbitda`      | múltiplo                   | Pro           |
        | Liquidez corrente            | `currentRatio`         | múltiplo                   | Pro           |
        | Liquidez seca                | `quickRatio`           | múltiplo                   | Pro           |
        | Crescimento da receita       | `revenueGrowth`        | fração (0.06 = 6%)         | Pro           |
        | Crescimento do lucro         | `earningsGrowth`       | fração (0.06 = 6%)         | Pro           |
        | Crescimento anual da receita | `revenueGrowthAnnual`  | fração (0.06 = 6%)         | Pro           |
        | Crescimento anual do lucro   | `earningsGrowthAnnual` | fração (0.06 = 6%)         | Pro           |
        | Receita                      | `totalRevenue`         | reais                      | Pro           |
        | EBITDA                       | `ebitda`               | reais                      | Pro           |
        | Fluxo de caixa livre         | `freeCashflow`         | reais                      | Pro           |
        | Dívida bruta                 | `totalDebt`            | reais                      | Pro           |
        | Caixa                        | `totalCash`            | reais                      | Pro           |

        Args:
          book_value_per_share_max: VPA: valor máximo, inclusive. Unidade: reais. Plano Startup e Pro.

          book_value_per_share_min: VPA: valor mínimo, inclusive. Unidade: reais. Plano Startup e Pro.

          change_percent_max: Variação no dia: valor máximo, inclusive. Unidade: porcentagem (2.81 = 2,81%).
              Plano Startup e Pro.

          change_percent_min: Variação no dia: valor mínimo, inclusive. Unidade: porcentagem (2.81 = 2,81%).
              Plano Startup e Pro.

          current_ratio_max: Liquidez corrente: valor máximo, inclusive. Unidade: múltiplo. Plano Pro.

          current_ratio_min: Liquidez corrente: valor mínimo, inclusive. Unidade: múltiplo. Plano Pro.

          debt_to_equity_max: Dívida/PL: valor máximo, inclusive. Unidade: múltiplo. Plano Pro.

          debt_to_equity_min: Dívida/PL: valor mínimo, inclusive. Unidade: múltiplo. Plano Pro.

          dividend_yield_max: Dividend yield: valor máximo, inclusive. Unidade: fração (0.06 = 6%). Plano
              Startup e Pro.

          dividend_yield_min: Dividend yield: valor mínimo, inclusive. Unidade: fração (0.06 = 6%). Plano
              Startup e Pro.

          earnings_growth_annual_max: Crescimento anual do lucro: valor máximo, inclusive. Unidade: fração (0.06 =
              6%). Plano Pro.

          earnings_growth_annual_min: Crescimento anual do lucro: valor mínimo, inclusive. Unidade: fração (0.06 =
              6%). Plano Pro.

          earnings_growth_max: Crescimento do lucro: valor máximo, inclusive. Unidade: fração (0.06 = 6%).
              Plano Pro.

          earnings_growth_min: Crescimento do lucro: valor mínimo, inclusive. Unidade: fração (0.06 = 6%).
              Plano Pro.

          earnings_per_share_max: LPA: valor máximo, inclusive. Unidade: reais. Plano Startup e Pro.

          earnings_per_share_min: LPA: valor mínimo, inclusive. Unidade: reais. Plano Startup e Pro.

          ebitda_margin_max: Margem EBITDA: valor máximo, inclusive. Unidade: fração (0.06 = 6%). Plano Pro.

          ebitda_margin_min: Margem EBITDA: valor mínimo, inclusive. Unidade: fração (0.06 = 6%). Plano Pro.

          ebitda_max: EBITDA: valor máximo, inclusive. Unidade: reais. Plano Pro.

          ebitda_min: EBITDA: valor mínimo, inclusive. Unidade: reais. Plano Pro.

          enterprise_to_ebitda_max: EV/EBITDA: valor máximo, inclusive. Unidade: múltiplo. Plano Startup e Pro.

          enterprise_to_ebitda_min: EV/EBITDA: valor mínimo, inclusive. Unidade: múltiplo. Plano Startup e Pro.

          enterprise_to_revenue_max: EV/Receita: valor máximo, inclusive. Unidade: múltiplo. Plano Startup e Pro.

          enterprise_to_revenue_min: EV/Receita: valor mínimo, inclusive. Unidade: múltiplo. Plano Startup e Pro.

          enterprise_value_max: Valor da firma: valor máximo, inclusive. Unidade: reais. Plano Startup e Pro.

          enterprise_value_min: Valor da firma: valor mínimo, inclusive. Unidade: reais. Plano Startup e Pro.

          fifty_two_week_change_max: Variação 52 semanas: valor máximo, inclusive. Unidade: fração (0.06 = 6%). Plano
              Startup e Pro.

          fifty_two_week_change_min: Variação 52 semanas: valor mínimo, inclusive. Unidade: fração (0.06 = 6%). Plano
              Startup e Pro.

          free_cashflow_max: Fluxo de caixa livre: valor máximo, inclusive. Unidade: reais. Plano Pro.

          free_cashflow_min: Fluxo de caixa livre: valor mínimo, inclusive. Unidade: reais. Plano Pro.

          gross_margin_max: Margem bruta: valor máximo, inclusive. Unidade: fração (0.06 = 6%). Plano Pro.

          gross_margin_min: Margem bruta: valor mínimo, inclusive. Unidade: fração (0.06 = 6%). Plano Pro.

          last_price_max: Preço: valor máximo, inclusive. Unidade: reais. Plano Startup e Pro.

          last_price_min: Preço: valor mínimo, inclusive. Unidade: reais. Plano Startup e Pro.

          limit: Itens por página. Máximo: 200.

          market_cap_max: Valor de mercado: valor máximo, inclusive. Unidade: reais. Plano Startup e Pro.

          market_cap_min: Valor de mercado: valor mínimo, inclusive. Unidade: reais. Plano Startup e Pro.

          net_debt_to_ebitda_max: Dívida líquida/EBITDA: valor máximo, inclusive. Unidade: múltiplo. Plano Pro.

          net_debt_to_ebitda_min: Dívida líquida/EBITDA: valor mínimo, inclusive. Unidade: múltiplo. Plano Pro.

          net_margin_max: Margem líquida: valor máximo, inclusive. Unidade: fração (0.06 = 6%). Plano
              Startup e Pro.

          net_margin_min: Margem líquida: valor mínimo, inclusive. Unidade: fração (0.06 = 6%). Plano
              Startup e Pro.

          operating_margin_max: Margem operacional: valor máximo, inclusive. Unidade: fração (0.06 = 6%). Plano
              Pro.

          operating_margin_min: Margem operacional: valor mínimo, inclusive. Unidade: fração (0.06 = 6%). Plano
              Pro.

          page: Número da página. Começa em 1.

          peg_ratio_max: PEG: valor máximo, inclusive. Unidade: múltiplo. Plano Startup e Pro.

          peg_ratio_min: PEG: valor mínimo, inclusive. Unidade: múltiplo. Plano Startup e Pro.

          price_to_book_max: P/VP: valor máximo, inclusive. Unidade: múltiplo. Plano Startup e Pro.

          price_to_book_min: P/VP: valor mínimo, inclusive. Unidade: múltiplo. Plano Startup e Pro.

          quick_ratio_max: Liquidez seca: valor máximo, inclusive. Unidade: múltiplo. Plano Pro.

          quick_ratio_min: Liquidez seca: valor mínimo, inclusive. Unidade: múltiplo. Plano Pro.

          return_on_assets_max: ROA: valor máximo, inclusive. Unidade: fração (0.06 = 6%). Plano Pro.

          return_on_assets_min: ROA: valor mínimo, inclusive. Unidade: fração (0.06 = 6%). Plano Pro.

          return_on_equity_max: ROE: valor máximo, inclusive. Unidade: fração (0.06 = 6%). Plano Pro.

          return_on_equity_min: ROE: valor mínimo, inclusive. Unidade: fração (0.06 = 6%). Plano Pro.

          revenue_growth_annual_max: Crescimento anual da receita: valor máximo, inclusive. Unidade: fração (0.06 =
              6%). Plano Pro.

          revenue_growth_annual_min: Crescimento anual da receita: valor mínimo, inclusive. Unidade: fração (0.06 =
              6%). Plano Pro.

          revenue_growth_max: Crescimento da receita: valor máximo, inclusive. Unidade: fração (0.06 = 6%).
              Plano Pro.

          revenue_growth_min: Crescimento da receita: valor mínimo, inclusive. Unidade: fração (0.06 = 6%).
              Plano Pro.

          search: Parte do ticker, do nome da empresa ou de um ticker antigo.

          sector: Setor. Aceita parte do nome.

          sort_by: Campo de ordenação: uma chave de métrica, `symbol` ou `name`. Valores nulos
              ficam no fim.

          sort_order: Ordem. Padrão: `desc`.

          subsector: Subsetor. Nome exato.

          sub_type: Subtipo do ativo: stock, unit, fii, etf, fi-infra, fi-agro, fip, fidc ou bdr.

          total_cash_max: Caixa: valor máximo, inclusive. Unidade: reais. Plano Pro.

          total_cash_min: Caixa: valor mínimo, inclusive. Unidade: reais. Plano Pro.

          total_debt_max: Dívida bruta: valor máximo, inclusive. Unidade: reais. Plano Pro.

          total_debt_min: Dívida bruta: valor mínimo, inclusive. Unidade: reais. Plano Pro.

          total_revenue_max: Receita: valor máximo, inclusive. Unidade: reais. Plano Pro.

          total_revenue_min: Receita: valor mínimo, inclusive. Unidade: reais. Plano Pro.

          trailing_pe_max: P/L: valor máximo, inclusive. Unidade: múltiplo. Plano Startup e Pro.

          trailing_pe_min: P/L: valor mínimo, inclusive. Unidade: múltiplo. Plano Startup e Pro.

          type: Tipo do ativo. Padrão: `stock`.

          volume_max: Volume: valor máximo, inclusive. Unidade: ações. Plano Startup e Pro.

          volume_min: Volume: valor mínimo, inclusive. Unidade: ações. Plano Startup e Pro.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/stocks/screener",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "book_value_per_share_max": book_value_per_share_max,
                        "book_value_per_share_min": book_value_per_share_min,
                        "change_percent_max": change_percent_max,
                        "change_percent_min": change_percent_min,
                        "current_ratio_max": current_ratio_max,
                        "current_ratio_min": current_ratio_min,
                        "debt_to_equity_max": debt_to_equity_max,
                        "debt_to_equity_min": debt_to_equity_min,
                        "dividend_yield_max": dividend_yield_max,
                        "dividend_yield_min": dividend_yield_min,
                        "earnings_growth_annual_max": earnings_growth_annual_max,
                        "earnings_growth_annual_min": earnings_growth_annual_min,
                        "earnings_growth_max": earnings_growth_max,
                        "earnings_growth_min": earnings_growth_min,
                        "earnings_per_share_max": earnings_per_share_max,
                        "earnings_per_share_min": earnings_per_share_min,
                        "ebitda_margin_max": ebitda_margin_max,
                        "ebitda_margin_min": ebitda_margin_min,
                        "ebitda_max": ebitda_max,
                        "ebitda_min": ebitda_min,
                        "enterprise_to_ebitda_max": enterprise_to_ebitda_max,
                        "enterprise_to_ebitda_min": enterprise_to_ebitda_min,
                        "enterprise_to_revenue_max": enterprise_to_revenue_max,
                        "enterprise_to_revenue_min": enterprise_to_revenue_min,
                        "enterprise_value_max": enterprise_value_max,
                        "enterprise_value_min": enterprise_value_min,
                        "fifty_two_week_change_max": fifty_two_week_change_max,
                        "fifty_two_week_change_min": fifty_two_week_change_min,
                        "free_cashflow_max": free_cashflow_max,
                        "free_cashflow_min": free_cashflow_min,
                        "gross_margin_max": gross_margin_max,
                        "gross_margin_min": gross_margin_min,
                        "last_price_max": last_price_max,
                        "last_price_min": last_price_min,
                        "limit": limit,
                        "market_cap_max": market_cap_max,
                        "market_cap_min": market_cap_min,
                        "net_debt_to_ebitda_max": net_debt_to_ebitda_max,
                        "net_debt_to_ebitda_min": net_debt_to_ebitda_min,
                        "net_margin_max": net_margin_max,
                        "net_margin_min": net_margin_min,
                        "operating_margin_max": operating_margin_max,
                        "operating_margin_min": operating_margin_min,
                        "page": page,
                        "peg_ratio_max": peg_ratio_max,
                        "peg_ratio_min": peg_ratio_min,
                        "price_to_book_max": price_to_book_max,
                        "price_to_book_min": price_to_book_min,
                        "quick_ratio_max": quick_ratio_max,
                        "quick_ratio_min": quick_ratio_min,
                        "return_on_assets_max": return_on_assets_max,
                        "return_on_assets_min": return_on_assets_min,
                        "return_on_equity_max": return_on_equity_max,
                        "return_on_equity_min": return_on_equity_min,
                        "revenue_growth_annual_max": revenue_growth_annual_max,
                        "revenue_growth_annual_min": revenue_growth_annual_min,
                        "revenue_growth_max": revenue_growth_max,
                        "revenue_growth_min": revenue_growth_min,
                        "search": search,
                        "sector": sector,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "subsector": subsector,
                        "sub_type": sub_type,
                        "total_cash_max": total_cash_max,
                        "total_cash_min": total_cash_min,
                        "total_debt_max": total_debt_max,
                        "total_debt_min": total_debt_min,
                        "total_revenue_max": total_revenue_max,
                        "total_revenue_min": total_revenue_min,
                        "trailing_pe_max": trailing_pe_max,
                        "trailing_pe_min": trailing_pe_min,
                        "type": type,
                        "volume_max": volume_max,
                        "volume_min": volume_min,
                    },
                    stock_screener_params.StockScreenerParams,
                ),
            ),
            cast_to=StockScreenerResponse,
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
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. `requestedSymbol` identifica o
              ticker enviado e `symbol` identifica os dados retornados.

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
          symbols: Tickers separados por vírgula. Ex.: PETR4,VALE3. `requestedSymbol` identifica o
              ticker enviado e `symbol` identifica os dados retornados.

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
        self.insider_transactions = to_raw_response_wrapper(
            stocks.insider_transactions,
        )
        self.profile = to_raw_response_wrapper(
            stocks.profile,
        )
        self.quote = to_raw_response_wrapper(
            stocks.quote,
        )
        self.screener = to_raw_response_wrapper(
            stocks.screener,
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
        self.insider_transactions = async_to_raw_response_wrapper(
            stocks.insider_transactions,
        )
        self.profile = async_to_raw_response_wrapper(
            stocks.profile,
        )
        self.quote = async_to_raw_response_wrapper(
            stocks.quote,
        )
        self.screener = async_to_raw_response_wrapper(
            stocks.screener,
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
        self.insider_transactions = to_streamed_response_wrapper(
            stocks.insider_transactions,
        )
        self.profile = to_streamed_response_wrapper(
            stocks.profile,
        )
        self.quote = to_streamed_response_wrapper(
            stocks.quote,
        )
        self.screener = to_streamed_response_wrapper(
            stocks.screener,
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
        self.insider_transactions = async_to_streamed_response_wrapper(
            stocks.insider_transactions,
        )
        self.profile = async_to_streamed_response_wrapper(
            stocks.profile,
        )
        self.quote = async_to_streamed_response_wrapper(
            stocks.quote,
        )
        self.screener = async_to_streamed_response_wrapper(
            stocks.screener,
        )
        self.statistics = async_to_streamed_response_wrapper(
            stocks.statistics,
        )
        self.value_added = async_to_streamed_response_wrapper(
            stocks.value_added,
        )
