# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .cashflow_entry import CashflowEntry
from .value_added_entry import ValueAddedEntry
from .balance_sheet_entry import BalanceSheetEntry
from .financial_data_entry import FinancialDataEntry
from .income_statement_entry import IncomeStatementEntry
from .default_key_statistics_entry import DefaultKeyStatisticsEntry

__all__ = [
    "QuoteRetrieveResponse",
    "Result",
    "ResultDividendsData",
    "ResultDividendsDataCashDividend",
    "ResultDividendsDataStockDividend",
    "ResultHistoricalDataPrice",
    "ResultSummaryProfile",
]


class ResultDividendsDataCashDividend(BaseModel):
    approved_on: Optional[datetime] = FieldInfo(alias="approvedOn", default=None)
    """Data em que o pagamento do provento foi aprovado pela empresa.

    Pode ser uma estimativa em alguns casos. Formato ISO 8601.
    """

    asset_issued: Optional[str] = FieldInfo(alias="assetIssued", default=None)
    """Ticker do ativo que pagou o provento (ex: `ITSA4`).

    Pode incluir sufixos específicos relacionados ao evento.
    """

    isin_code: Optional[str] = FieldInfo(alias="isinCode", default=None)
    """
    Código ISIN (International Securities Identification Number) do ativo
    relacionado ao provento.
    """

    label: Optional[str] = None
    """Tipo do provento em dinheiro.

    Geralmente `DIVIDENDO` ou `JCP` (Juros sobre Capital Próprio).
    """

    last_date_prior: Optional[datetime] = FieldInfo(alias="lastDatePrior", default=None)
    """Data Com (Ex-Date).

    Último dia em que era necessário possuir o ativo para ter direito a receber este
    provento. Pode ser uma estimativa. Formato ISO 8601.
    """

    payment_date: Optional[datetime] = FieldInfo(alias="paymentDate", default=None)
    """Data efetiva em que o pagamento foi realizado (ou está previsto).

    Formato ISO 8601.
    """

    rate: Optional[float] = None
    """Valor bruto do provento pago por unidade do ativo (por ação, por cota)."""

    related_to: Optional[str] = FieldInfo(alias="relatedTo", default=None)
    """
    Descrição do período ou evento ao qual o provento se refere (ex:
    `1º Trimestre/2023`, `Resultado 2022`).
    """

    remarks: Optional[str] = None
    """Observações adicionais ou informações relevantes sobre o provento."""


class ResultDividendsDataStockDividend(BaseModel):
    approved_on: Optional[datetime] = FieldInfo(alias="approvedOn", default=None)
    """Data em que o evento foi aprovado. Formato ISO 8601."""

    asset_issued: Optional[str] = FieldInfo(alias="assetIssued", default=None)
    """Ticker do ativo afetado pelo evento."""

    complete_factor: Optional[str] = FieldInfo(alias="completeFactor", default=None)
    """Descrição textual do fator (ex: `1 / 10`, `10 / 1`)."""

    factor: Optional[float] = None
    """Fator numérico do evento.

    - **Bonificação:** Percentual (ex: 0.1 para 10%).
    - **Desdobramento/Grupamento:** Fator multiplicativo ou divisor.
    """

    isin_code: Optional[str] = FieldInfo(alias="isinCode", default=None)
    """Código ISIN do ativo."""

    label: Optional[str] = None
    """Tipo do evento: `DESDOBRAMENTO`, `GRUPAMENTO`, `BONIFICACAO`."""

    last_date_prior: Optional[datetime] = FieldInfo(alias="lastDatePrior", default=None)
    """Data Com (Ex-Date).

    Último dia para possuir o ativo nas condições antigas. Formato ISO 8601.
    """

    remarks: Optional[str] = None
    """Observações adicionais sobre o evento."""


class ResultDividendsData(BaseModel):
    cash_dividends: Optional[List[ResultDividendsDataCashDividend]] = FieldInfo(alias="cashDividends", default=None)
    """Lista de proventos pagos em dinheiro (Dividendos e JCP)."""

    stock_dividends: Optional[List[ResultDividendsDataStockDividend]] = FieldInfo(alias="stockDividends", default=None)
    """Lista de eventos corporativos (Desdobramento, Grupamento, Bonificação)."""

    subscriptions: Optional[List[object]] = None
    """Lista de eventos de subscrição de ações (estrutura não detalhada aqui)."""


class ResultHistoricalDataPrice(BaseModel):
    adjusted_close: Optional[float] = FieldInfo(alias="adjustedClose", default=None)
    """
    Preço de fechamento ajustado para proventos (dividendos, JCP, bonificações,
    etc.) e desdobramentos/grupamentos.
    """

    close: Optional[float] = None
    """Preço de fechamento do ativo no intervalo."""

    date: Optional[int] = None
    """
    Data do pregão ou do ponto de dados, representada como um timestamp UNIX (número
    de segundos desde 1970-01-01 UTC).
    """

    high: Optional[float] = None
    """Preço máximo atingido pelo ativo no intervalo."""

    low: Optional[float] = None
    """Preço mínimo atingido pelo ativo no intervalo."""

    open: Optional[float] = None
    """Preço de abertura do ativo no intervalo (dia, semana, mês, etc.)."""

    volume: Optional[int] = None
    """Volume financeiro negociado no intervalo."""


class ResultSummaryProfile(BaseModel):
    address1: Optional[str] = None
    """Linha 1 do endereço da sede da empresa."""

    address2: Optional[str] = None
    """Linha 2 do endereço da sede da empresa (complemento)."""

    city: Optional[str] = None
    """Cidade da sede da empresa."""

    company_officers: Optional[List[object]] = FieldInfo(alias="companyOfficers", default=None)
    """
    Lista de diretores e executivos principais da empresa (estrutura interna do
    objeto não detalhada aqui).
    """

    country: Optional[str] = None
    """País da sede da empresa."""

    full_time_employees: Optional[int] = FieldInfo(alias="fullTimeEmployees", default=None)
    """Número estimado de funcionários em tempo integral."""

    industry: Optional[str] = None
    """Nome da indústria em que a empresa atua."""

    industry_disp: Optional[str] = FieldInfo(alias="industryDisp", default=None)
    """Nome de exibição formatado para a indústria."""

    industry_key: Optional[str] = FieldInfo(alias="industryKey", default=None)
    """Chave interna ou código para a indústria."""

    long_business_summary: Optional[str] = FieldInfo(alias="longBusinessSummary", default=None)
    """Descrição longa e detalhada sobre as atividades e o negócio da empresa."""

    phone: Optional[str] = None
    """Número de telefone principal da empresa."""

    sector: Optional[str] = None
    """Nome do setor de atuação da empresa."""

    sector_disp: Optional[str] = FieldInfo(alias="sectorDisp", default=None)
    """Nome de exibição formatado para o setor."""

    sector_key: Optional[str] = FieldInfo(alias="sectorKey", default=None)
    """Chave interna ou código para o setor."""

    state: Optional[str] = None
    """Estado ou província da sede da empresa."""

    website: Optional[str] = None
    """URL do website oficial da empresa."""

    zip: Optional[str] = None
    """Código Postal (CEP) da sede da empresa."""


class Result(BaseModel):
    average_daily_volume10_day: Optional[float] = FieldInfo(alias="averageDailyVolume10Day", default=None)
    """Média do volume financeiro diário negociado nos últimos 10 dias."""

    average_daily_volume3_month: Optional[float] = FieldInfo(alias="averageDailyVolume3Month", default=None)
    """Média do volume financeiro diário negociado nos últimos 3 meses."""

    balance_sheet_history: Optional[List[BalanceSheetEntry]] = FieldInfo(alias="balanceSheetHistory", default=None)
    """Histórico **anual** do Balanço Patrimonial.

    Retornado apenas se `modules` incluir `balanceSheetHistory`.
    """

    balance_sheet_history_quarterly: Optional[List[BalanceSheetEntry]] = FieldInfo(
        alias="balanceSheetHistoryQuarterly", default=None
    )
    """Histórico **trimestral** do Balanço Patrimonial.

    Retornado apenas se `modules` incluir `balanceSheetHistoryQuarterly`.
    """

    cashflow_history: Optional[List[CashflowEntry]] = FieldInfo(alias="cashflowHistory", default=None)
    """Histórico **anual** da Demonstração do Fluxo de Caixa (DFC).

    Retornado apenas se `modules` incluir `cashflowHistory`.
    """

    cashflow_history_quarterly: Optional[List[CashflowEntry]] = FieldInfo(
        alias="cashflowHistoryQuarterly", default=None
    )
    """Histórico **trimestral** da Demonstração do Fluxo de Caixa (DFC).

    Retornado apenas se `modules` incluir `cashflowHistoryQuarterly`.
    """

    currency: Optional[str] = None
    """Moeda na qual os valores monetários são expressos (geralmente `BRL`)."""

    default_key_statistics: Optional[DefaultKeyStatisticsEntry] = FieldInfo(alias="defaultKeyStatistics", default=None)
    """Principais estatísticas financeiras atuais/TTM.

    Retornado apenas se `modules` incluir `defaultKeyStatistics`.
    """

    default_key_statistics_history: Optional[List[DefaultKeyStatisticsEntry]] = FieldInfo(
        alias="defaultKeyStatisticsHistory", default=None
    )
    """Histórico **anual** das principais estatísticas.

    Retornado apenas se `modules` incluir `defaultKeyStatisticsHistory`.
    """

    default_key_statistics_history_quarterly: Optional[List[DefaultKeyStatisticsEntry]] = FieldInfo(
        alias="defaultKeyStatisticsHistoryQuarterly", default=None
    )
    """Histórico **trimestral** das principais estatísticas.

    Retornado apenas se `modules` incluir `defaultKeyStatisticsHistoryQuarterly`.
    """

    dividends_data: Optional[ResultDividendsData] = FieldInfo(alias="dividendsData", default=None)
    """Objeto contendo informações sobre dividendos, JCP e outros eventos corporativos.

    Retornado apenas se `dividends=true` for especificado na requisição.
    """

    earnings_per_share: Optional[float] = FieldInfo(alias="earningsPerShare", default=None)
    """Lucro Por Ação (LPA) dos últimos 12 meses (TTM).

    Retornado se `fundamental=true`.
    """

    fifty_two_week_high: Optional[float] = FieldInfo(alias="fiftyTwoWeekHigh", default=None)
    """Preço máximo atingido nas últimas 52 semanas."""

    fifty_two_week_high_change: Optional[float] = FieldInfo(alias="fiftyTwoWeekHighChange", default=None)
    """Variação absoluta entre o preço atual e o preço máximo das últimas 52 semanas."""

    fifty_two_week_high_change_percent: Optional[float] = FieldInfo(alias="fiftyTwoWeekHighChangePercent", default=None)
    """
    Variação percentual entre o preço atual e o preço máximo das últimas 52 semanas.
    """

    fifty_two_week_low: Optional[float] = FieldInfo(alias="fiftyTwoWeekLow", default=None)
    """Preço mínimo atingido nas últimas 52 semanas."""

    fifty_two_week_low_change: Optional[float] = FieldInfo(alias="fiftyTwoWeekLowChange", default=None)
    """Variação absoluta entre o preço atual e o preço mínimo das últimas 52 semanas."""

    fifty_two_week_range: Optional[str] = FieldInfo(alias="fiftyTwoWeekRange", default=None)
    """
    String formatada mostrando o intervalo de preço das últimas 52 semanas (Mínimo -
    Máximo).
    """

    financial_data: Optional[FinancialDataEntry] = FieldInfo(alias="financialData", default=None)
    """Dados financeiros e indicadores TTM.

    Retornado apenas se `modules` incluir `financialData`.
    """

    financial_data_history: Optional[List[FinancialDataEntry]] = FieldInfo(alias="financialDataHistory", default=None)
    """Histórico **anual** de dados financeiros e indicadores.

    Retornado apenas se `modules` incluir `financialDataHistory`.
    """

    financial_data_history_quarterly: Optional[List[FinancialDataEntry]] = FieldInfo(
        alias="financialDataHistoryQuarterly", default=None
    )
    """Histórico **trimestral** de dados financeiros e indicadores.

    Retornado apenas se `modules` incluir `financialDataHistoryQuarterly`.
    """

    historical_data_price: Optional[List[ResultHistoricalDataPrice]] = FieldInfo(
        alias="historicalDataPrice", default=None
    )
    """
    Array contendo a série histórica de preços, retornado apenas se os parâmetros
    `range` e/ou `interval` forem especificados na requisição.
    """

    income_statement_history: Optional[List[IncomeStatementEntry]] = FieldInfo(
        alias="incomeStatementHistory", default=None
    )
    """Histórico **anual** da Demonstração do Resultado (DRE).

    Retornado apenas se `modules` incluir `incomeStatementHistory`.
    """

    income_statement_history_quarterly: Optional[List[IncomeStatementEntry]] = FieldInfo(
        alias="incomeStatementHistoryQuarterly", default=None
    )
    """Histórico **trimestral** da Demonstração do Resultado (DRE).

    Retornado apenas se `modules` incluir `incomeStatementHistoryQuarterly`.
    """

    logourl: Optional[str] = None
    """URL da imagem do logo do ativo/empresa."""

    long_name: Optional[str] = FieldInfo(alias="longName", default=None)
    """Nome longo ou completo da empresa ou ativo."""

    market_cap: Optional[float] = FieldInfo(alias="marketCap", default=None)
    """Capitalização de mercado total do ativo (Preço Atual x Ações em Circulação)."""

    price_earnings: Optional[float] = FieldInfo(alias="priceEarnings", default=None)
    """Indicador Preço/Lucro (P/L): Preço Atual / Lucro Por Ação (LPA) TTM.

    Retornado se `fundamental=true`.
    """

    regular_market_change: Optional[float] = FieldInfo(alias="regularMarketChange", default=None)
    """Variação absoluta do preço no dia atual em relação ao fechamento anterior."""

    regular_market_change_percent: Optional[float] = FieldInfo(alias="regularMarketChangePercent", default=None)
    """Variação percentual do preço no dia atual em relação ao fechamento anterior."""

    regular_market_day_high: Optional[float] = FieldInfo(alias="regularMarketDayHigh", default=None)
    """Preço máximo atingido no dia de negociação atual."""

    regular_market_day_low: Optional[float] = FieldInfo(alias="regularMarketDayLow", default=None)
    """Preço mínimo atingido no dia de negociação atual."""

    regular_market_day_range: Optional[str] = FieldInfo(alias="regularMarketDayRange", default=None)
    """String formatada mostrando o intervalo de preço do dia (Mínimo - Máximo)."""

    regular_market_open: Optional[float] = FieldInfo(alias="regularMarketOpen", default=None)
    """Preço de abertura no dia de negociação atual."""

    regular_market_previous_close: Optional[float] = FieldInfo(alias="regularMarketPreviousClose", default=None)
    """Preço de fechamento do pregão anterior."""

    regular_market_price: Optional[float] = FieldInfo(alias="regularMarketPrice", default=None)
    """Preço atual ou do último negócio registrado."""

    regular_market_time: Optional[datetime] = FieldInfo(alias="regularMarketTime", default=None)
    """Data e hora da última atualização da cotação (último negócio registrado).

    Formato ISO 8601.
    """

    regular_market_volume: Optional[float] = FieldInfo(alias="regularMarketVolume", default=None)
    """Volume financeiro negociado no dia atual."""

    short_name: Optional[str] = FieldInfo(alias="shortName", default=None)
    """Nome curto ou abreviado da empresa ou ativo."""

    summary_profile: Optional[ResultSummaryProfile] = FieldInfo(alias="summaryProfile", default=None)
    """Resumo do perfil da empresa.

    Retornado apenas se `modules` incluir `summaryProfile`.
    """

    symbol: Optional[str] = None
    """Ticker (símbolo) do ativo (ex: `PETR4`, `^BVSP`)."""

    two_hundred_day_average: Optional[float] = FieldInfo(alias="twoHundredDayAverage", default=None)
    """Média móvel simples dos preços de fechamento dos últimos 200 dias."""

    two_hundred_day_average_change: Optional[float] = FieldInfo(alias="twoHundredDayAverageChange", default=None)
    """Variação absoluta entre o preço atual e a média de 200 dias."""

    two_hundred_day_average_change_percent: Optional[float] = FieldInfo(
        alias="twoHundredDayAverageChangePercent", default=None
    )
    """Variação percentual entre o preço atual e a média de 200 dias."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """
    Timestamp da última atualização dos dados do índice na fonte (aplicável
    principalmente a índices, como `^BVSP`). Formato ISO 8601.
    """

    used_interval: Optional[str] = FieldInfo(alias="usedInterval", default=None)
    """
    O intervalo (`interval`) efetivamente utilizado pela API para retornar os dados
    históricos, caso solicitado.
    """

    used_range: Optional[str] = FieldInfo(alias="usedRange", default=None)
    """
    O período (`range`) efetivamente utilizado pela API para retornar os dados
    históricos, caso solicitado.
    """

    valid_intervals: Optional[List[str]] = FieldInfo(alias="validIntervals", default=None)
    """
    Lista dos valores válidos que podem ser utilizados no parâmetro `interval` para
    este ativo específico.
    """

    valid_ranges: Optional[List[str]] = FieldInfo(alias="validRanges", default=None)
    """
    Lista dos valores válidos que podem ser utilizados no parâmetro `range` para
    este ativo específico.
    """

    value_added_history: Optional[List[ValueAddedEntry]] = FieldInfo(alias="valueAddedHistory", default=None)
    """Histórico **anual** da Demonstração do Valor Adicionado (DVA).

    Retornado apenas se `modules` incluir `valueAddedHistory`.
    """

    value_added_history_quarterly: Optional[List[ValueAddedEntry]] = FieldInfo(
        alias="valueAddedHistoryQuarterly", default=None
    )
    """Histórico **trimestral** da Demonstração do Valor Adicionado (DVA).

    Retornado apenas se `modules` incluir `valueAddedHistoryQuarterly`.
    """


class QuoteRetrieveResponse(BaseModel):
    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """Timestamp indicando quando a requisição foi recebida pelo servidor.

    Formato ISO 8601.
    """

    results: Optional[List[Result]] = None
    """Array contendo os resultados detalhados para cada ticker solicitado."""

    took: Optional[str] = None
    """
    Tempo aproximado que o servidor levou para processar a requisição, em formato de
    string (ex: `746ms`).
    """
