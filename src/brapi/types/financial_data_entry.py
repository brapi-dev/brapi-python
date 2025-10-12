# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FinancialDataEntry"]


class FinancialDataEntry(BaseModel):
    current_price: Optional[float] = FieldInfo(alias="currentPrice", default=None)
    """Preço atual da ação (pode ser ligeiramente defasado)."""

    current_ratio: Optional[float] = FieldInfo(alias="currentRatio", default=None)
    """Índice de Liquidez Corrente (Ativo Circulante / Passivo Circulante)."""

    debt_to_equity: Optional[float] = FieldInfo(alias="debtToEquity", default=None)
    """Índice Dívida Líquida / Patrimônio Líquido."""

    earnings_growth: Optional[float] = FieldInfo(alias="earningsGrowth", default=None)
    """
    Crescimento do Lucro Líquido (geralmente trimestral YoY, como
    `earningsQuarterlyGrowth`).
    """

    ebitda: Optional[float] = None
    """Lucro Antes de Juros, Impostos, Depreciação e Amortização (LAJIDA ou EBITDA).

    Geralmente TTM.
    """

    ebitda_margins: Optional[float] = FieldInfo(alias="ebitdaMargins", default=None)
    """Margem EBITDA (EBITDA TTM / Receita Líquida TTM)."""

    financial_currency: Optional[str] = FieldInfo(alias="financialCurrency", default=None)
    """Moeda na qual os dados financeiros são reportados (ex: `BRL`, `USD`)."""

    free_cashflow: Optional[float] = FieldInfo(alias="freeCashflow", default=None)
    """Fluxo de Caixa Livre (FCO - CAPEX) - (geralmente TTM)."""

    gross_margins: Optional[float] = FieldInfo(alias="grossMargins", default=None)
    """Margem Bruta (Lucro Bruto TTM / Receita Líquida TTM)."""

    gross_profits: Optional[float] = FieldInfo(alias="grossProfits", default=None)
    """Lucro Bruto (geralmente TTM)."""

    number_of_analyst_opinions: Optional[float] = FieldInfo(alias="numberOfAnalystOpinions", default=None)
    """Número de opiniões de analistas consideradas."""

    operating_cashflow: Optional[float] = FieldInfo(alias="operatingCashflow", default=None)
    """Fluxo de Caixa das Operações (FCO) - (geralmente TTM)."""

    operating_margins: Optional[float] = FieldInfo(alias="operatingMargins", default=None)
    """Margem Operacional (EBIT TTM / Receita Líquida TTM)."""

    profit_margins: Optional[float] = FieldInfo(alias="profitMargins", default=None)
    """Margem Líquida (Lucro Líquido TTM / Receita Líquida TTM).

    Sinônimo do campo de mesmo nome em `DefaultKeyStatisticsEntry`.
    """

    quick_ratio: Optional[float] = FieldInfo(alias="quickRatio", default=None)
    """Índice de Liquidez Seca ((Ativo Circulante - Estoques) / Passivo Circulante)."""

    recommendation_key: Optional[str] = FieldInfo(alias="recommendationKey", default=None)
    """Resumo da recomendação (ex.: strong_buy, buy, hold, sell, strong_sell)."""

    recommendation_mean: Optional[float] = FieldInfo(alias="recommendationMean", default=None)
    """Média de recomendações dos analistas (1=Compra Forte, 5=Venda Forte)."""

    return_on_assets: Optional[float] = FieldInfo(alias="returnOnAssets", default=None)
    """Retorno sobre Ativos (ROA): Lucro Líquido TTM / Ativo Total Médio."""

    return_on_equity: Optional[float] = FieldInfo(alias="returnOnEquity", default=None)
    """
    Retorno sobre Patrimônio Líquido (ROE): Lucro Líquido TTM / Patrimônio Líquido
    Médio.
    """

    revenue_growth: Optional[float] = FieldInfo(alias="revenueGrowth", default=None)
    """Crescimento da Receita Líquida (geralmente trimestral YoY)."""

    revenue_per_share: Optional[float] = FieldInfo(alias="revenuePerShare", default=None)
    """Receita Líquida por Ação (Receita Líquida TTM / Ações em Circulação)."""

    symbol: Optional[str] = None
    """Ticker do ativo ao qual os dados se referem."""

    target_high_price: Optional[float] = FieldInfo(alias="targetHighPrice", default=None)
    """Preço-alvo mais alto estimado por analistas."""

    target_low_price: Optional[float] = FieldInfo(alias="targetLowPrice", default=None)
    """Preço-alvo mais baixo estimado por analistas."""

    target_mean_price: Optional[float] = FieldInfo(alias="targetMeanPrice", default=None)
    """Preço-alvo médio estimado por analistas."""

    target_median_price: Optional[float] = FieldInfo(alias="targetMedianPrice", default=None)
    """Preço-alvo mediano estimado por analistas."""

    total_cash: Optional[float] = FieldInfo(alias="totalCash", default=None)
    """
    Caixa e Equivalentes de Caixa + Aplicações Financeiras de Curto Prazo (último
    balanço).
    """

    total_cash_per_share: Optional[float] = FieldInfo(alias="totalCashPerShare", default=None)
    """Caixa Total por Ação (Caixa Total / Ações em Circulação)."""

    total_debt: Optional[float] = FieldInfo(alias="totalDebt", default=None)
    """
    Dívida Bruta Total (Dívida de Curto Prazo + Dívida de Longo Prazo - último
    balanço).
    """

    total_revenue: Optional[float] = FieldInfo(alias="totalRevenue", default=None)
    """Receita Líquida Total (geralmente TTM)."""

    type: Optional[Literal["yearly", "quarterly", "ttm"]] = None
    """
    Periodicidade dos dados: `yearly` (anual), `quarterly` (trimestral), `ttm`
    (Trailing Twelve Months).
    """

    updated_at: Optional[date] = FieldInfo(alias="updatedAt", default=None)
    """
    Data da última atualização deste registro específico na fonte de dados
    (YYYY-MM-DD).
    """
