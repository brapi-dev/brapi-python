# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FinancialDataEntry"]


class FinancialDataEntry(BaseModel):
    """Dados financeiros e indicadores TTM"""

    current_price: Optional[float] = FieldInfo(alias="currentPrice", default=None)
    """Preço atual"""

    current_ratio: Optional[float] = FieldInfo(alias="currentRatio", default=None)
    """Liquidez corrente"""

    debt_to_equity: Optional[float] = FieldInfo(alias="debtToEquity", default=None)
    """Dívida/PL"""

    earnings_growth: Optional[float] = FieldInfo(alias="earningsGrowth", default=None)
    """
    Crescimento do lucro do controlador (TTM) — variação dos últimos 4 trimestres em
    relação aos 4 trimestres imediatamente anteriores, usando Lucro Líquido
    Atribuível aos Controladores. Para crescimento anual (DRE de exercício vs.
    exercício anterior), use earningsGrowthAnnual.
    """

    earnings_growth_annual: Optional[float] = FieldInfo(alias="earningsGrowthAnnual", default=None)
    """
    Crescimento anual do lucro do controlador — variação do Lucro Líquido Atribuível
    aos Controladores do último exercício social completo em relação ao exercício
    anterior.
    """

    ebitda: Optional[float] = None
    """EBITDA"""

    ebitda_margins: Optional[float] = FieldInfo(alias="ebitdaMargins", default=None)
    """Margem EBITDA"""

    financial_currency: Optional[str] = FieldInfo(alias="financialCurrency", default=None)
    """Moeda"""

    free_cashflow: Optional[float] = FieldInfo(alias="freeCashflow", default=None)
    """Fluxo de caixa livre"""

    gross_margins: Optional[float] = FieldInfo(alias="grossMargins", default=None)
    """Margem bruta"""

    gross_profits: Optional[float] = FieldInfo(alias="grossProfits", default=None)
    """Lucro bruto"""

    operating_cashflow: Optional[float] = FieldInfo(alias="operatingCashflow", default=None)
    """Fluxo de caixa operacional"""

    operating_margins: Optional[float] = FieldInfo(alias="operatingMargins", default=None)
    """Margem operacional"""

    profit_margins: Optional[float] = FieldInfo(alias="profitMargins", default=None)
    """Margem de lucro"""

    quick_ratio: Optional[float] = FieldInfo(alias="quickRatio", default=None)
    """Liquidez seca"""

    return_on_assets: Optional[float] = FieldInfo(alias="returnOnAssets", default=None)
    """ROA"""

    return_on_equity: Optional[float] = FieldInfo(alias="returnOnEquity", default=None)
    """ROE"""

    revenue_growth: Optional[float] = FieldInfo(alias="revenueGrowth", default=None)
    """
    Crescimento da receita (TTM) — variação da receita dos últimos 4 trimestres em
    relação aos 4 trimestres imediatamente anteriores. Para crescimento anual (DRE
    de exercício vs. exercício anterior), use revenueGrowthAnnual.
    """

    revenue_growth_annual: Optional[float] = FieldInfo(alias="revenueGrowthAnnual", default=None)
    """
    Crescimento anual da receita — variação da Receita Líquida do último exercício
    social completo em relação ao exercício anterior.
    """

    revenue_per_share: Optional[float] = FieldInfo(alias="revenuePerShare", default=None)
    """Receita por ação"""

    symbol: str
    """Ticker do ativo"""

    total_cash: Optional[float] = FieldInfo(alias="totalCash", default=None)
    """Caixa total"""

    total_cash_per_share: Optional[float] = FieldInfo(alias="totalCashPerShare", default=None)
    """Caixa por ação"""

    total_debt: Optional[float] = FieldInfo(alias="totalDebt", default=None)
    """Dívida total"""

    total_revenue: Optional[float] = FieldInfo(alias="totalRevenue", default=None)
    """Receita total"""

    type: Optional[str] = None
    """Tipo (ttm, yearly, quarterly)"""

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)
    """Data de atualização"""
