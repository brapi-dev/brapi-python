# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MacroSeriesPublic"]


class MacroSeriesPublic(BaseModel):
    category: str

    description: str

    frequency: str

    name: str

    slug: str
    """Código da série. Use este valor em `symbols`."""

    start_date: str = FieldInfo(alias="startDate")

    unit: str
