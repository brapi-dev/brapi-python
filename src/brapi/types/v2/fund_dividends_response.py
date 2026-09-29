# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .fund_pagination_meta import FundPaginationMeta

__all__ = ["FundDividendsResponse", "Dividend"]


class Dividend(BaseModel):
    asset_type: Literal["fiagro", "fiinfra", "fif", "fidc", "fip", "other"] = FieldInfo(alias="assetType")

    cnpj: str

    declared_date: str = FieldInfo(alias="declaredDate")

    ex_date: Optional[str] = FieldInfo(alias="exDate", default=None)

    isin_code: Optional[str] = FieldInfo(alias="isinCode", default=None)

    label: str

    last_date_prior: str = FieldInfo(alias="lastDatePrior")

    payment_date: str = FieldInfo(alias="paymentDate")

    rate: float

    symbol: str


class FundDividendsResponse(BaseModel):
    dividends: List[Dividend]

    pagination: FundPaginationMeta

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
