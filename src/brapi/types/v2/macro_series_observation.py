# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["MacroSeriesObservation"]


class MacroSeriesObservation(BaseModel):
    date: str

    value: float
