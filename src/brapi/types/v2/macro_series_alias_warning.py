# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MacroSeriesAliasWarning"]


class MacroSeriesAliasWarning(BaseModel):
    canonical_slug: str = FieldInfo(alias="canonicalSlug")
    """Código oficial da série. Use este valor em integrações."""

    message: str

    provided: str
    """Nome alternativo enviado em `symbols`."""
