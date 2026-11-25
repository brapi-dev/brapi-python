# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["CrowdingTimelineResponse", "Company"]


class Company(BaseModel):
    b3_symbols: List[str] = FieldInfo(alias="b3Symbols")

    buyers_counts: List[Optional[float]] = FieldInfo(alias="buyersCounts")
    """Fundos que compraram em cada mês."""

    country: Optional[str] = None

    flow_values: List[Optional[float]] = FieldInfo(alias="flowValues")
    """Saldo de cada mês."""

    funds_counts: List[Optional[float]] = FieldInfo(alias="fundsCounts")
    """Fundos com posição direta em cada mês."""

    name: Optional[str] = None

    sector: Optional[str] = None

    sellers_counts: List[Optional[float]] = FieldInfo(alias="sellersCounts")
    """Fundos que venderam em cada mês."""

    symbol: Optional[str] = None

    values: List[Optional[float]]
    """Dinheiro dos fundos em cada mês de `months`.

    `null` quando a empresa não aparece no mês.
    """


class CrowdingTimelineResponse(BaseModel):
    companies: List[Company]

    months: List[str]
    """Meses, do mais antigo ao mais recente."""

    region: Literal["all", "brazil", "foreign"]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
