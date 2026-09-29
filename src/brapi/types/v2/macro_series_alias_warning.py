# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MacroSeriesAliasWarning"]


class MacroSeriesAliasWarning(BaseModel):
    canonical_slug: str = FieldInfo(alias="canonicalSlug")

    message: str

    provided: str
