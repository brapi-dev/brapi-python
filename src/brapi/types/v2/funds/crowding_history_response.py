# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["CrowdingHistoryResponse", "Month"]


class Month(BaseModel):
    companies_count: int = FieldInfo(alias="companiesCount")

    confidential_equity_value: float = FieldInfo(alias="confidentialEquityValue")
    """Ações e BDRs em posições confidenciais, que não entram."""

    effective_companies: Optional[float] = FieldInfo(alias="effectiveCompanies", default=None)

    flow_value: Optional[float] = FieldInfo(alias="flowValue", default=None)
    """Saldo do mês. `null` no primeiro mês."""

    funds_count: int = FieldInfo(alias="fundsCount")
    """Fundos com carteira no mês."""

    reference_date: str = FieldInfo(alias="referenceDate")

    top10_weight_percent: Optional[float] = FieldInfo(alias="top10WeightPercent", default=None)

    top5_weight_percent: Optional[float] = FieldInfo(alias="top5WeightPercent", default=None)

    total_value: float = FieldInfo(alias="totalValue")
    """Dinheiro dos fundos em todas as empresas."""


class CrowdingHistoryResponse(BaseModel):
    months: List[Month]

    region: Literal["all", "brazil", "foreign"]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
