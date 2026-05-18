# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .balance_sheet_entry import BalanceSheetEntry
from .financial_data_entry import FinancialDataEntry

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
    approved_on: Optional[str] = FieldInfo(alias="approvedOn", default=None)
    """Data de aprovação"""

    asset_issued: str = FieldInfo(alias="assetIssued")
    """Código ISIN do ativo emissor"""

    isin_code: str = FieldInfo(alias="isinCode")
    """Código ISIN"""

    label: str
    """Tipo (DIVIDENDO, JCP)"""

    last_date_prior: Optional[str] = FieldInfo(alias="lastDatePrior", default=None)
    """Data-com (último dia antes da data ex)"""

    payment_date: Optional[str] = FieldInfo(alias="paymentDate", default=None)
    """Data de pagamento"""

    rate: float
    """Valor por ação"""

    related_to: str = FieldInfo(alias="relatedTo")
    """Período de referência"""

    remarks: str
    """Observações"""


class ResultDividendsDataStockDividend(BaseModel):
    approved_on: Optional[str] = FieldInfo(alias="approvedOn", default=None)
    """Data de aprovação"""

    asset_issued: str = FieldInfo(alias="assetIssued")
    """Código ISIN do ativo emissor"""

    complete_factor: str = FieldInfo(alias="completeFactor")
    """Fator completo (ex: 2 para 1)"""

    factor: float
    """Fator do desdobramento/grupamento"""

    isin_code: str = FieldInfo(alias="isinCode")
    """Código ISIN"""

    label: str
    """Tipo (DESDOBRAMENTO, GRUPAMENTO)"""

    last_date_prior: Optional[str] = FieldInfo(alias="lastDatePrior", default=None)
    """Data de corte"""

    remarks: str
    """Observações"""


class ResultDividendsData(BaseModel):
    """Dados de dividendos (quando dividends=true)"""

    cash_dividends: List[ResultDividendsDataCashDividend] = FieldInfo(alias="cashDividends")
    """Histórico de dividendos e JCP em dinheiro"""

    stock_dividends: List[ResultDividendsDataStockDividend] = FieldInfo(alias="stockDividends")
    """Histórico de bonificações e desdobramentos"""

    subscriptions: List[Optional[object]]
    """Histórico de subscrições"""


class ResultHistoricalDataPrice(BaseModel):
    adjusted_close: float = FieldInfo(alias="adjustedClose")
    """
    Preço de fechamento ajustado para proventos (dividendos, JCP, bonificações,
    etc.) e desdobramentos/grupamentos.
    """

    close: float
    """Preço de fechamento do ativo no intervalo."""

    date: int
    """
    Data do pregão ou do ponto de dados, representada como um timestamp UNIX (número
    de segundos desde 1970-01-01 UTC).
    """

    high: float
    """Preço máximo atingido pelo ativo no intervalo."""

    low: float
    """Preço mínimo atingido pelo ativo no intervalo."""

    open: float
    """Preço de abertura do ativo no intervalo (dia, semana, mês, etc.)."""

    volume: int
    """Volume financeiro negociado no intervalo."""


class ResultSummaryProfile(BaseModel):
    """Perfil da empresa (quando modules inclui summaryProfile)"""

    address1: Optional[str] = None
    """Endereço linha 1"""

    address2: Optional[str] = None
    """Endereço linha 2"""

    address3: Optional[str] = None
    """Endereço linha 3"""

    city: Optional[str] = None
    """Cidade"""

    cnpj: Optional[str] = None
    """CNPJ da empresa"""

    company_officers: List[Optional[object]] = FieldInfo(alias="companyOfficers")
    """Diretoria"""

    country: Optional[str] = None
    """País"""

    fax: Optional[str] = None
    """Fax"""

    full_time_employees: Optional[float] = FieldInfo(alias="fullTimeEmployees", default=None)
    """Número de funcionários"""

    industry: Optional[str] = None
    """Setor"""

    industry_disp: Optional[str] = FieldInfo(alias="industryDisp", default=None)
    """Nome do setor"""

    industry_key: Optional[str] = FieldInfo(alias="industryKey", default=None)
    """Chave do setor"""

    long_business_summary: Optional[str] = FieldInfo(alias="longBusinessSummary", default=None)
    """Descrição da empresa"""

    phone: Optional[str] = None
    """Telefone"""

    sector: Optional[str] = None
    """Segmento"""

    sector_disp: Optional[str] = FieldInfo(alias="sectorDisp", default=None)
    """Nome do segmento"""

    sector_key: Optional[str] = FieldInfo(alias="sectorKey", default=None)
    """Chave do segmento"""

    state: Optional[str] = None
    """Estado"""

    symbol: str
    """Ticker do ativo"""

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)
    """Data de atualização"""

    website: Optional[str] = None
    """Website"""

    zip: Optional[str] = None
    """CEP"""


class Result(BaseModel):
    average_daily_volume10_day: Optional[float] = FieldInfo(alias="averageDailyVolume10Day", default=None)
    """Média do volume diário nos últimos 10 dias"""

    average_daily_volume3_month: Optional[float] = FieldInfo(alias="averageDailyVolume3Month", default=None)
    """Média do volume diário nos últimos 3 meses"""

    currency: str
    """Moeda na qual os valores são expressos (geralmente BRL)"""

    earnings_per_share: Optional[float] = FieldInfo(alias="earningsPerShare", default=None)
    """Lucro Por Ação (LPA) TTM"""

    fifty_two_week_high: Optional[float] = FieldInfo(alias="fiftyTwoWeekHigh", default=None)
    """Preço máximo nas últimas 52 semanas"""

    fifty_two_week_high_change: Optional[float] = FieldInfo(alias="fiftyTwoWeekHighChange", default=None)
    """Variação entre preço atual e máximo de 52 semanas"""

    fifty_two_week_high_change_percent: Optional[float] = FieldInfo(alias="fiftyTwoWeekHighChangePercent", default=None)
    """Variação percentual entre preço atual e máximo de 52 semanas"""

    fifty_two_week_low: Optional[float] = FieldInfo(alias="fiftyTwoWeekLow", default=None)
    """Preço mínimo nas últimas 52 semanas"""

    fifty_two_week_low_change: Optional[float] = FieldInfo(alias="fiftyTwoWeekLowChange", default=None)
    """Variação entre preço atual e mínimo de 52 semanas"""

    fifty_two_week_range: Optional[str] = FieldInfo(alias="fiftyTwoWeekRange", default=None)
    """Intervalo de preço das últimas 52 semanas"""

    logourl: Optional[str] = None
    """URL do logo do ativo"""

    long_name: Optional[str] = FieldInfo(alias="longName", default=None)
    """Nome completo da empresa"""

    market_cap: Optional[float] = FieldInfo(alias="marketCap", default=None)
    """Capitalização de mercado total"""

    price_earnings: Optional[float] = FieldInfo(alias="priceEarnings", default=None)
    """Indicador Preço/Lucro (P/L)"""

    regular_market_change: Optional[float] = FieldInfo(alias="regularMarketChange", default=None)
    """Variação absoluta do preço no dia em relação ao fechamento anterior"""

    regular_market_change_percent: Optional[float] = FieldInfo(alias="regularMarketChangePercent", default=None)
    """Variação percentual do preço no dia"""

    regular_market_day_high: Optional[float] = FieldInfo(alias="regularMarketDayHigh", default=None)
    """Preço máximo atingido no dia"""

    regular_market_day_low: Optional[float] = FieldInfo(alias="regularMarketDayLow", default=None)
    """Preço mínimo atingido no dia"""

    regular_market_day_range: Optional[str] = FieldInfo(alias="regularMarketDayRange", default=None)
    """Intervalo de preço do dia (Mínimo - Máximo)"""

    regular_market_open: Optional[float] = FieldInfo(alias="regularMarketOpen", default=None)
    """Preço de abertura no dia"""

    regular_market_previous_close: Optional[float] = FieldInfo(alias="regularMarketPreviousClose", default=None)
    """Preço de fechamento do pregão anterior"""

    regular_market_price: Optional[float] = FieldInfo(alias="regularMarketPrice", default=None)
    """Preço atual ou do último negócio registrado"""

    regular_market_time: Optional[str] = FieldInfo(alias="regularMarketTime", default=None)
    """Data/hora da última atualização da cotação (ISO 8601)"""

    regular_market_volume: Optional[float] = FieldInfo(alias="regularMarketVolume", default=None)
    """Volume financeiro negociado no dia"""

    short_name: Optional[str] = FieldInfo(alias="shortName", default=None)
    """Nome curto ou abreviado da empresa"""

    symbol: str
    """Ticker (símbolo) do ativo (ex: PETR4, ^BVSP)"""

    two_hundred_day_average: Optional[float] = FieldInfo(alias="twoHundredDayAverage", default=None)
    """Média móvel de 200 dias"""

    two_hundred_day_average_change: Optional[float] = FieldInfo(alias="twoHundredDayAverageChange", default=None)
    """Variação entre preço atual e média de 200 dias"""

    two_hundred_day_average_change_percent: Optional[float] = FieldInfo(
        alias="twoHundredDayAverageChangePercent", default=None
    )
    """Variação percentual entre preço atual e média de 200 dias"""

    used_interval: Optional[str] = FieldInfo(alias="usedInterval", default=None)
    """Intervalo efetivamente utilizado para dados históricos"""

    used_range: Optional[str] = FieldInfo(alias="usedRange", default=None)
    """Período efetivamente utilizado para dados históricos"""

    balance_sheet_history: Optional[List[BalanceSheetEntry]] = FieldInfo(alias="balanceSheetHistory", default=None)
    """Histórico anual do Balanço Patrimonial"""

    balance_sheet_history_quarterly: Optional[List[BalanceSheetEntry]] = FieldInfo(
        alias="balanceSheetHistoryQuarterly", default=None
    )
    """Histórico trimestral do Balanço Patrimonial"""

    dividends_data: Optional[ResultDividendsData] = FieldInfo(alias="dividendsData", default=None)
    """Dados de dividendos (quando dividends=true)"""

    financial_data: Optional[FinancialDataEntry] = FieldInfo(alias="financialData", default=None)
    """Dados financeiros e indicadores TTM"""

    financial_data_history: Optional[List[FinancialDataEntry]] = FieldInfo(alias="financialDataHistory", default=None)
    """Histórico anual de dados financeiros"""

    financial_data_history_quarterly: Optional[List[FinancialDataEntry]] = FieldInfo(
        alias="financialDataHistoryQuarterly", default=None
    )
    """Histórico trimestral de dados financeiros"""

    historical_data_price: Optional[List[ResultHistoricalDataPrice]] = FieldInfo(
        alias="historicalDataPrice", default=None
    )
    """Série histórica de preços (quando range/interval fornecidos)"""

    summary_profile: Optional[ResultSummaryProfile] = FieldInfo(alias="summaryProfile", default=None)
    """Perfil da empresa (quando modules inclui summaryProfile)"""

    valid_intervals: Optional[List[str]] = FieldInfo(alias="validIntervals", default=None)
    """Valores válidos para o parâmetro interval"""

    valid_ranges: Optional[List[str]] = FieldInfo(alias="validRanges", default=None)
    """Valores válidos para o parâmetro range"""


class QuoteRetrieveResponse(BaseModel):
    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em formato ISO 8601"""

    results: List[Result]

    took: int
    """Tempo de processamento em milissegundos"""
