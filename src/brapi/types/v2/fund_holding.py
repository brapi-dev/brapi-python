# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FundHolding", "Details"]


class Details(BaseModel):
    application_type: Optional[str] = FieldInfo(alias="applicationType", default=None)

    asset_code: Optional[str] = FieldInfo(alias="assetCode", default=None)

    confidential_until: Optional[str] = FieldInfo(alias="confidentialUntil", default=None)

    fund_class_type: Optional[str] = FieldInfo(alias="fundClassType", default=None)

    issue_date: Optional[str] = FieldInfo(alias="issueDate", default=None)

    issuer_type: Optional[str] = FieldInfo(alias="issuerType", default=None)

    negotiation_type: Optional[str] = FieldInfo(alias="negotiationType", default=None)

    purchased_quantity: Optional[float] = FieldInfo(alias="purchasedQuantity", default=None)

    purchase_value: Optional[float] = FieldInfo(alias="purchaseValue", default=None)

    related_issuer: Optional[bool] = FieldInfo(alias="relatedIssuer", default=None)

    sale_value: Optional[float] = FieldInfo(alias="saleValue", default=None)

    sold_quantity: Optional[float] = FieldInfo(alias="soldQuantity", default=None)

    subclass_id: Optional[str] = FieldInfo(alias="subclassId", default=None)


class FundHolding(BaseModel):
    asset_name: Optional[str] = FieldInfo(alias="assetName", default=None)

    asset_type: Optional[str] = FieldInfo(alias="assetType", default=None)

    bucket: str

    confidential: bool

    cost_value: Optional[float] = FieldInfo(alias="costValue", default=None)

    details: Optional[Details] = None

    isin: Optional[str] = None

    issuer_cnpj: Optional[str] = FieldInfo(alias="issuerCnpj", default=None)

    issuer_name: Optional[str] = FieldInfo(alias="issuerName", default=None)

    market_value: Optional[float] = FieldInfo(alias="marketValue", default=None)

    maturity_date: Optional[str] = FieldInfo(alias="maturityDate", default=None)

    quantity: Optional[float] = None

    selic_code: Optional[str] = FieldInfo(alias="selicCode", default=None)
