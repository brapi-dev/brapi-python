# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["FiiPortfolioAllocation"]


class FiiPortfolioAllocation(BaseModel):
    asset_class: str = FieldInfo(alias="assetClass")

    count: float

    value: Optional[float] = None
