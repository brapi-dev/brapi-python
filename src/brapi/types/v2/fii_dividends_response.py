# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FiiDividendsResponse", "Dividend"]


class Dividend(BaseModel):
    approved_on: Optional[str] = FieldInfo(alias="approvedOn", default=None)

    ex_date: Optional[str] = FieldInfo(alias="exDate", default=None)

    isin_code: Optional[str] = FieldInfo(alias="isinCode", default=None)

    label: str

    last_date_prior: str = FieldInfo(alias="lastDatePrior")

    payment_date: str = FieldInfo(alias="paymentDate")

    rate: float

    related_to: Optional[str] = FieldInfo(alias="relatedTo", default=None)

    remarks: Optional[str] = None

    symbol: str

    verified: bool
    """
    `true` quando o provento foi conferido em um documento publicado pela empresa ou
    pelo fundo. `false` quando vem de dados históricos que ainda não têm esse
    documento.
    """


class FiiDividendsResponse(BaseModel):
    dividends: List[Dividend]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
