# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .dividends_data import DividendsData
from .balance_sheet_entry import BalanceSheetEntry
from .financial_data_entry import FinancialDataEntry

__all__ = [
    "QuoteRetrieveResponse",
    "Result",
    "ResultHistoricalDataPrice",
    "ResultSummaryProfile",
    "Guidance",
    "GuidanceDetails",
]


class ResultHistoricalDataPrice(BaseModel):
    adjusted_close: float = FieldInfo(alias="adjustedClose")
    """Fechamento ajustado por proventos, desdobramentos e grupamentos.

    Use para calcular retorno.
    """

    close: float
    """Preço de fechamento no intervalo."""

    date: int
    """Data do ponto em Unix timestamp, em segundos."""

    high: float
    """Preço máximo no intervalo."""

    low: float
    """Preço mínimo no intervalo."""

    open: float
    """Preço de abertura no intervalo."""

    volume: int
    """Volume negociado no intervalo."""

    raw_close: Optional[float] = FieldInfo(alias="rawClose", default=None)
    """Preço de fechamento original, sem ajuste.

    Vem com `includeRaw=true` em intervalos diários. Pode ser nulo.
    """

    raw_high: Optional[float] = FieldInfo(alias="rawHigh", default=None)
    """Preço máximo original, sem ajuste.

    Vem com `includeRaw=true` em intervalos diários. Pode ser nulo.
    """

    raw_low: Optional[float] = FieldInfo(alias="rawLow", default=None)
    """Preço mínimo original, sem ajuste.

    Vem com `includeRaw=true` em intervalos diários. Pode ser nulo.
    """

    raw_open: Optional[float] = FieldInfo(alias="rawOpen", default=None)
    """Preço de abertura original, sem ajuste.

    Vem com `includeRaw=true` em intervalos diários. Pode ser nulo.
    """


class ResultSummaryProfile(BaseModel):
    """Cadastro da empresa. Vem com o módulo `summaryProfile`."""

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
    """Volume médio diário dos últimos 10 dias."""

    average_daily_volume3_month: Optional[float] = FieldInfo(alias="averageDailyVolume3Month", default=None)
    """Volume médio diário dos últimos 3 meses."""

    currency: str
    """Moeda dos valores. Em geral, BRL."""

    earnings_per_share: Optional[float] = FieldInfo(alias="earningsPerShare", default=None)
    """Lucro por ação (LPA) dos últimos 12 meses."""

    fifty_two_week_high: Optional[float] = FieldInfo(alias="fiftyTwoWeekHigh", default=None)
    """Preço máximo das últimas 52 semanas."""

    fifty_two_week_high_change: Optional[float] = FieldInfo(alias="fiftyTwoWeekHighChange", default=None)
    """Diferença entre o preço atual e o máximo de 52 semanas."""

    fifty_two_week_high_change_percent: Optional[float] = FieldInfo(alias="fiftyTwoWeekHighChangePercent", default=None)
    """Diferença entre o preço atual e o máximo de 52 semanas, em porcentagem."""

    fifty_two_week_low: Optional[float] = FieldInfo(alias="fiftyTwoWeekLow", default=None)
    """Preço mínimo das últimas 52 semanas."""

    fifty_two_week_low_change: Optional[float] = FieldInfo(alias="fiftyTwoWeekLowChange", default=None)
    """Diferença entre o preço atual e o mínimo de 52 semanas."""

    fifty_two_week_range: Optional[str] = FieldInfo(alias="fiftyTwoWeekRange", default=None)
    """Faixa de preço das últimas 52 semanas no formato mínimo - máximo."""

    logourl: Optional[str] = None
    """URL do logo do ativo."""

    long_name: Optional[str] = FieldInfo(alias="longName", default=None)
    """Nome completo da empresa."""

    market_cap: Optional[float] = FieldInfo(alias="marketCap", default=None)
    """Valor de mercado, em reais."""

    price_earnings: Optional[float] = FieldInfo(alias="priceEarnings", default=None)
    """Preço sobre lucro (P/L)."""

    regular_market_change: Optional[float] = FieldInfo(alias="regularMarketChange", default=None)
    """Variação do preço no dia em relação ao fechamento anterior, em reais."""

    regular_market_change_percent: Optional[float] = FieldInfo(alias="regularMarketChangePercent", default=None)
    """Variação do preço no dia, em porcentagem."""

    regular_market_day_high: Optional[float] = FieldInfo(alias="regularMarketDayHigh", default=None)
    """Preço máximo do dia."""

    regular_market_day_low: Optional[float] = FieldInfo(alias="regularMarketDayLow", default=None)
    """Preço mínimo do dia."""

    regular_market_day_range: Optional[str] = FieldInfo(alias="regularMarketDayRange", default=None)
    """Faixa de preço do dia no formato mínimo - máximo."""

    regular_market_open: Optional[float] = FieldInfo(alias="regularMarketOpen", default=None)
    """Preço de abertura do dia."""

    regular_market_previous_close: Optional[float] = FieldInfo(alias="regularMarketPreviousClose", default=None)
    """Fechamento do pregão anterior."""

    regular_market_price: Optional[float] = FieldInfo(alias="regularMarketPrice", default=None)
    """Preço do último negócio."""

    regular_market_time: Optional[str] = FieldInfo(alias="regularMarketTime", default=None)
    """Horário da cotação em ISO 8601."""

    regular_market_volume: Optional[float] = FieldInfo(alias="regularMarketVolume", default=None)
    """Volume negociado no dia."""

    short_name: Optional[str] = FieldInfo(alias="shortName", default=None)
    """Nome curto do ativo."""

    symbol: str
    """Ticker do ativo. Ex.: PETR4, ^BVSP."""

    two_hundred_day_average: Optional[float] = FieldInfo(alias="twoHundredDayAverage", default=None)
    """Média móvel de 200 dias."""

    two_hundred_day_average_change: Optional[float] = FieldInfo(alias="twoHundredDayAverageChange", default=None)
    """Diferença entre o preço atual e a média de 200 dias."""

    two_hundred_day_average_change_percent: Optional[float] = FieldInfo(
        alias="twoHundredDayAverageChangePercent", default=None
    )
    """Diferença entre o preço atual e a média de 200 dias, em porcentagem."""

    used_interval: Optional[str] = FieldInfo(alias="usedInterval", default=None)
    """Intervalo usado na série de preços."""

    used_range: Optional[str] = FieldInfo(alias="usedRange", default=None)
    """Janela usada na série de preços."""

    balance_sheet_history: Optional[List[BalanceSheetEntry]] = FieldInfo(alias="balanceSheetHistory", default=None)
    """Balanço patrimonial anual."""

    balance_sheet_history_quarterly: Optional[List[BalanceSheetEntry]] = FieldInfo(
        alias="balanceSheetHistoryQuarterly", default=None
    )
    """Balanço patrimonial trimestral."""

    dividends_data: Optional[DividendsData] = FieldInfo(alias="dividendsData", default=None)
    """Proventos.

    Na rota `/api/quote/{tickers}`, vem com `dividends=true`. Na rota
    `/api/v2/stocks/dividends`, não exige esse parâmetro.
    """

    dividends_symbol: Optional[str] = FieldInfo(alias="dividendsSymbol", default=None)
    """Ticker do histórico de proventos quando ele difere do ticker da cotação."""

    financial_data: Optional[FinancialDataEntry] = FieldInfo(alias="financialData", default=None)
    """Dados financeiros dos últimos 12 meses."""

    financial_data_history: Optional[List[FinancialDataEntry]] = FieldInfo(alias="financialDataHistory", default=None)
    """Dados financeiros anuais."""

    financial_data_history_quarterly: Optional[List[FinancialDataEntry]] = FieldInfo(
        alias="financialDataHistoryQuarterly", default=None
    )
    """Dados financeiros trimestrais."""

    historical_data_price: Optional[List[ResultHistoricalDataPrice]] = FieldInfo(
        alias="historicalDataPrice", default=None
    )
    """Série de preços. Vem quando a requisição define a janela."""

    historical_symbol: Optional[str] = FieldInfo(alias="historicalSymbol", default=None)
    """Ticker do histórico de preços quando ele difere do ticker da cotação."""

    requested_symbol: Optional[str] = FieldInfo(alias="requestedSymbol", default=None)
    """Ticker enviado quando a cotação pertence a outro ticker."""

    summary_profile: Optional[ResultSummaryProfile] = FieldInfo(alias="summaryProfile", default=None)
    """Cadastro da empresa. Vem com o módulo `summaryProfile`."""

    valid_intervals: Optional[List[str]] = FieldInfo(alias="validIntervals", default=None)
    """Valores aceitos em `interval`."""

    valid_ranges: Optional[List[str]] = FieldInfo(alias="validRanges", default=None)
    """Valores aceitos em `range`."""


class GuidanceDetails(BaseModel):
    reason: str

    suggested_endpoint: str = FieldInfo(alias="suggestedEndpoint")


class Guidance(BaseModel):
    code: str

    details: GuidanceDetails

    message: str


class QuoteRetrieveResponse(BaseModel):
    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    results: List[Result]

    took: int
    """Tempo de processamento, em milissegundos."""

    guidance: Optional[List[Guidance]] = None
    """Dicas que apontam um endpoint mais adequado para o pedido.

    A requisição funciona mesmo assim.
    """
