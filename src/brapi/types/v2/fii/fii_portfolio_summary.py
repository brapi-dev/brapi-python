# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .fii_property_summary import FiiPropertySummary

__all__ = ["FiiPortfolioSummary", "FinancialAssets", "Lands", "Rights"]


class FinancialAssets(BaseModel):
    count: float

    declared_value: Optional[float] = FieldInfo(alias="declaredValue", default=None)


class Lands(BaseModel):
    count: float

    total_area: Optional[float] = FieldInfo(alias="totalArea", default=None)


class Rights(BaseModel):
    count: float

    declared_value: Optional[float] = FieldInfo(alias="declaredValue", default=None)


class FiiPortfolioSummary(BaseModel):
    declared_value: Optional[float] = FieldInfo(alias="declaredValue", default=None)

    financial_assets: FinancialAssets = FieldInfo(alias="financialAssets")

    lands: Lands

    properties: FiiPropertySummary

    rights: Rights

    total_items: float = FieldInfo(alias="totalItems")
