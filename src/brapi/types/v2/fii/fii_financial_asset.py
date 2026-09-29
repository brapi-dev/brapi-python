# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["FiiFinancialAsset"]


class FiiFinancialAsset(BaseModel):
    asset_class: str = FieldInfo(alias="assetClass")

    confidential: bool

    identifier: Optional[str] = None

    issue: Optional[str] = None

    issuer: Optional[str] = None

    issuer_cnpj: Optional[str] = FieldInfo(alias="issuerCnpj", default=None)

    maturity_date: Optional[str] = FieldInfo(alias="maturityDate", default=None)

    name: str

    quantity: Optional[float] = None

    series: Optional[str] = None

    ticker: Optional[str] = None

    value: Optional[float] = None
