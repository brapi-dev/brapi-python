# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .fund_holding import FundHolding

__all__ = ["FundPortfolioResponse", "Fund"]


class Fund(BaseModel):
    cnpj: str

    confidential_summary: Optional[Dict[str, Optional[object]]] = FieldInfo(alias="confidentialSummary", default=None)

    credit_assets: List[FundHolding] = FieldInfo(alias="creditAssets")

    fund_holdings: List[FundHolding] = FieldInfo(alias="fundHoldings")

    listed_securities: List[FundHolding] = FieldInfo(alias="listedSecurities")

    name: Optional[str] = None

    payables: List[FundHolding]

    public_bonds: List[FundHolding] = FieldInfo(alias="publicBonds")

    receivables: List[FundHolding]

    reference_date: str = FieldInfo(alias="referenceDate")

    summary: Dict[str, Optional[object]]

    symbol: Optional[str] = None


class FundPortfolioResponse(BaseModel):
    funds: List[Fund]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
