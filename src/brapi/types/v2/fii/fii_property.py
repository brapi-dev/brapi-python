# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["FiiProperty"]


class FiiProperty(BaseModel):
    address: Optional[str] = None

    area: Optional[float] = None

    confidential: bool

    construction_cost_actual: Optional[float] = FieldInfo(alias="constructionCostActual", default=None)

    construction_cost_expected: Optional[float] = FieldInfo(alias="constructionCostExpected", default=None)

    construction_progress_actual: Optional[float] = FieldInfo(alias="constructionProgressActual", default=None)

    construction_progress_expected: Optional[float] = FieldInfo(alias="constructionProgressExpected", default=None)

    delinquency_rate: Optional[float] = FieldInfo(alias="delinquencyRate", default=None)

    identifier: Optional[str] = None

    invested_share: Optional[float] = FieldInfo(alias="investedShare", default=None)

    leased_rate: Optional[float] = FieldInfo(alias="leasedRate", default=None)

    name: str

    property_class: Optional[str] = FieldInfo(alias="propertyClass", default=None)

    revenue_share: Optional[float] = FieldInfo(alias="revenueShare", default=None)

    sold_rate: Optional[float] = FieldInfo(alias="soldRate", default=None)

    unit_count: Optional[float] = FieldInfo(alias="unitCount", default=None)

    vacancy_rate: Optional[float] = FieldInfo(alias="vacancyRate", default=None)
