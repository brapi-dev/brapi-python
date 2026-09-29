# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["FiiPropertySummary"]


class FiiPropertySummary(BaseModel):
    average_vacancy_rate: Optional[float] = FieldInfo(alias="averageVacancyRate", default=None)

    count: float

    properties_with_vacancy: float = FieldInfo(alias="propertiesWithVacancy")

    total_area: Optional[float] = FieldInfo(alias="totalArea", default=None)

    vacancy_rate: Optional[float] = FieldInfo(alias="vacancyRate", default=None)
