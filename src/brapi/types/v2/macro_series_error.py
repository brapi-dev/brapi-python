# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["MacroSeriesError"]


class MacroSeriesError(BaseModel):
    code: str

    message: str

    slug: str
