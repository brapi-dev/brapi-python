# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FundIndicatorsResponse", "Fund"]


class Fund(BaseModel):
    as_of_date: Optional[str] = FieldInfo(alias="asOfDate", default=None)
    """Data do informe com a cota e o patrimônio. Pode ser anterior a `priceDate`."""

    asset_type: Literal["fii", "fiagro", "fiinfra", "fif", "fidc", "fip", "etf", "other"] = FieldInfo(alias="assetType")

    cnpj: str

    daily_applications: Optional[float] = FieldInfo(alias="dailyApplications", default=None)

    daily_redemptions: Optional[float] = FieldInfo(alias="dailyRedemptions", default=None)

    dividend_yield_monthly: Optional[float] = FieldInfo(alias="dividendYieldMonthly", default=None)
    """Rendimento distribuído no mês sobre o valor patrimonial da cota, em %."""

    equity: Optional[float] = None

    monthly_return: Optional[float] = FieldInfo(alias="monthlyReturn", default=None)
    """Rentabilidade da cota no mês do informe, em %."""

    name: Optional[str] = None

    nav_per_share: Optional[float] = FieldInfo(alias="navPerShare", default=None)
    """
    Valor patrimonial por cota na base de cotas dos preços: desdobramentos e
    grupamentos depois da data do informe já estão aplicados, como em `close`.
    """

    patrimonial_monthly_return: Optional[float] = FieldInfo(alias="patrimonialMonthlyReturn", default=None)
    """Rentabilidade patrimonial no mês do informe, em %."""

    price: Optional[float] = None

    price_date: Optional[str] = FieldInfo(alias="priceDate", default=None)
    """Data do preço de fechamento usado em `price`."""

    price_to_nav: Optional[float] = FieldInfo(alias="priceToNav", default=None)
    """Fechamento na data da cota dividido por `navPerShare`.

    Usa o último pregão até 7 dias antes dessa data. Sem fechamento nesse intervalo,
    é `null`.
    """

    raw_nav_per_share: Optional[float] = FieldInfo(alias="rawNavPerShare", default=None)
    """
    Valor patrimonial por cota como o informe declara, sem desdobramentos e
    grupamentos posteriores.
    """

    shares_outstanding: Optional[float] = FieldInfo(alias="sharesOutstanding", default=None)

    symbol: Optional[str] = None

    total_assets: Optional[float] = FieldInfo(alias="totalAssets", default=None)

    total_investors: Optional[float] = FieldInfo(alias="totalInvestors", default=None)


class FundIndicatorsResponse(BaseModel):
    funds: List[Fund]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
