# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ..fund_pagination_meta import FundPaginationMeta

__all__ = ["FiagroReportsResponse", "Report"]


class Report(BaseModel):
    admin_fee_expense_percent: Optional[float] = FieldInfo(alias="adminFeeExpensePercent", default=None)
    """Despesa com taxa de administração no mês, em % do patrimônio líquido."""

    administrator_name: Optional[str] = FieldInfo(alias="administratorName", default=None)

    amortization_rate_monthly: Optional[float] = FieldInfo(alias="amortizationRateMonthly", default=None)

    cnpj: str

    distribution_fee_expense_percent: Optional[float] = FieldInfo(alias="distributionFeeExpensePercent", default=None)
    """Despesa com taxa de distribuição no mês, em % do patrimônio líquido."""

    dividend_yield_monthly: Optional[float] = FieldInfo(alias="dividendYieldMonthly", default=None)

    income_to_distribute: Optional[float] = FieldInfo(alias="incomeToDistribute", default=None)

    isin: Optional[str] = None

    liquidity_needs: Optional[float] = FieldInfo(alias="liquidityNeeds", default=None)

    management_fee_expense_percent: Optional[float] = FieldInfo(alias="managementFeeExpensePercent", default=None)
    """Despesa com taxa de gestão no mês, em % do patrimônio líquido."""

    manager_name: Optional[str] = FieldInfo(alias="managerName", default=None)

    market: Optional[str] = None

    monthly_return: Optional[float] = FieldInfo(alias="monthlyReturn", default=None)

    name: Optional[str] = None

    nav_per_share: Optional[float] = FieldInfo(alias="navPerShare", default=None)
    """
    Valor patrimonial por cota na base de cotas dos preços: desdobramentos e
    grupamentos depois da data do informe já estão aplicados, como em `close`.
    """

    net_equity: Optional[float] = FieldInfo(alias="netEquity", default=None)

    patrimonial_monthly_return: Optional[float] = FieldInfo(alias="patrimonialMonthlyReturn", default=None)

    raw_nav_per_share: Optional[float] = FieldInfo(alias="rawNavPerShare", default=None)
    """
    Valor patrimonial por cota como o informe declara, sem desdobramentos e
    grupamentos posteriores.
    """

    reference_date: str = FieldInfo(alias="referenceDate")

    shares_outstanding: Optional[float] = FieldInfo(alias="sharesOutstanding", default=None)

    symbol: Optional[str] = None

    total_assets: Optional[float] = FieldInfo(alias="totalAssets", default=None)

    total_investors: Optional[float] = FieldInfo(alias="totalInvestors", default=None)

    total_liabilities: Optional[float] = FieldInfo(alias="totalLiabilities", default=None)

    version: float


class FiagroReportsResponse(BaseModel):
    pagination: FundPaginationMeta

    reports: List[Report]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
