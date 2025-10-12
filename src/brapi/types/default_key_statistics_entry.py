# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DefaultKeyStatisticsEntry"]


class DefaultKeyStatisticsEntry(BaseModel):
    api_52_week_change: Optional[float] = FieldInfo(alias="52WeekChange", default=None)
    """Variação percentual do preço da ação nas últimas 52 semanas."""

    beta: Optional[float] = None
    """Beta da ação (sensibilidade em relação ao mercado)."""

    book_value: Optional[float] = FieldInfo(alias="bookValue", default=None)
    """Valor Patrimonial por Ação (VPA): Patrimônio Líquido / Ações em Circulação."""

    dividend_yield: Optional[float] = FieldInfo(alias="dividendYield", default=None)
    """Dividend Yield (provento anualizado sobre o preço atual)."""

    earnings_annual_growth: Optional[float] = FieldInfo(alias="earningsAnnualGrowth", default=None)
    """
    Crescimento percentual do lucro líquido no último ano fiscal completo em relação
    ao ano anterior.
    """

    earnings_quarterly_growth: Optional[float] = FieldInfo(alias="earningsQuarterlyGrowth", default=None)
    """
    Crescimento percentual do lucro líquido no último trimestre em relação ao mesmo
    trimestre do ano anterior (YoY).
    """

    enterprise_to_ebitda: Optional[float] = FieldInfo(alias="enterpriseToEbitda", default=None)
    """Múltiplo EV/EBITDA (Enterprise Value / EBITDA TTM)."""

    enterprise_to_revenue: Optional[float] = FieldInfo(alias="enterpriseToRevenue", default=None)
    """Múltiplo EV/Receita (Enterprise Value / Receita Líquida TTM)."""

    enterprise_value: Optional[float] = FieldInfo(alias="enterpriseValue", default=None)
    """Valor da Firma (Enterprise Value - EV): Market Cap + Dívida Total - Caixa."""

    float_shares: Optional[float] = FieldInfo(alias="floatShares", default=None)
    """Ações em livre circulação (free float)."""

    forward_eps: Optional[float] = FieldInfo(alias="forwardEps", default=None)
    """Lucro Por Ação projetado (próximo período)."""

    forward_pe: Optional[float] = FieldInfo(alias="forwardPE", default=None)
    """
    Preço / Lucro Projetado (Forward P/E): Preço da Ação / LPA estimado para o
    próximo período.
    """

    held_percent_insiders: Optional[float] = FieldInfo(alias="heldPercentInsiders", default=None)
    """Percentual de ações detidas por insiders (administradores, controladores)."""

    held_percent_institutions: Optional[float] = FieldInfo(alias="heldPercentInstitutions", default=None)
    """
    Percentual de ações detidas por instituições (fundos, investidores
    institucionais).
    """

    implied_shares_outstanding: Optional[float] = FieldInfo(alias="impliedSharesOutstanding", default=None)
    """Ações implícitas em circulação (considerando diluição/derivativos)."""

    last_dividend_date: Optional[date] = FieldInfo(alias="lastDividendDate", default=None)
    """Data de pagamento (ou 'Data Com') do último dividendo/JCP (YYYY-MM-DD)."""

    last_dividend_value: Optional[float] = FieldInfo(alias="lastDividendValue", default=None)
    """Valor do último dividendo ou JCP pago por ação."""

    last_fiscal_year_end: Optional[date] = FieldInfo(alias="lastFiscalYearEnd", default=None)
    """Data de encerramento do último ano fiscal (YYYY-MM-DD)."""

    last_split_date: Optional[float] = FieldInfo(alias="lastSplitDate", default=None)
    """Data do último desdobramento/grupamento (timestamp UNIX em segundos)."""

    last_split_factor: Optional[str] = FieldInfo(alias="lastSplitFactor", default=None)
    """Fator do último desdobramento/grupamento (ex.: 2:1, 1:10)."""

    most_recent_quarter: Optional[date] = FieldInfo(alias="mostRecentQuarter", default=None)
    """
    Data de término do trimestre mais recente considerado nos cálculos (YYYY-MM-DD).
    """

    net_income_to_common: Optional[float] = FieldInfo(alias="netIncomeToCommon", default=None)
    """Lucro Líquido atribuível aos acionistas ordinários (controladores)."""

    next_fiscal_year_end: Optional[date] = FieldInfo(alias="nextFiscalYearEnd", default=None)
    """Data de encerramento do próximo ano fiscal (YYYY-MM-DD)."""

    peg_ratio: Optional[float] = FieldInfo(alias="pegRatio", default=None)
    """Índice PEG (P/E dividido pelo crescimento esperado dos lucros)."""

    price_to_book: Optional[float] = FieldInfo(alias="priceToBook", default=None)
    """Preço sobre Valor Patrimonial (P/VP): Preço da Ação / VPA."""

    profit_margins: Optional[float] = FieldInfo(alias="profitMargins", default=None)
    """Margem de Lucro Líquida (Lucro Líquido / Receita Líquida).

    Geralmente em base TTM ou anual.
    """

    sand_p52_week_change: Optional[float] = FieldInfo(alias="SandP52WeekChange", default=None)
    """Variação percentual do índice S&P 500 nas últimas 52 semanas (para referência)."""

    shares_outstanding: Optional[float] = FieldInfo(alias="sharesOutstanding", default=None)
    """Número total de ações ordinárias em circulação."""

    symbol: Optional[str] = None
    """Ticker do ativo ao qual as estatísticas se referem."""

    total_assets: Optional[float] = FieldInfo(alias="totalAssets", default=None)
    """Valor total dos ativos registrado no último balanço (anual ou trimestral)."""

    trailing_eps: Optional[float] = FieldInfo(alias="trailingEps", default=None)
    """Lucro Por Ação (LPA) dos Últimos 12 Meses (TTM)."""

    type: Optional[Literal["yearly", "quarterly", "ttm"]] = None
    """
    Periodicidade dos dados: `yearly` (anual), `quarterly` (trimestral), `ttm`
    (Trailing Twelve Months - últimos 12 meses).
    """

    updated_at: Optional[date] = FieldInfo(alias="updatedAt", default=None)
    """
    Data da última atualização deste registro específico na fonte de dados
    (YYYY-MM-DD).
    """

    ytd_return: Optional[float] = FieldInfo(alias="ytdReturn", default=None)
    """Retorno percentual do preço da ação desde o início do ano atual (Year-to-Date)."""
