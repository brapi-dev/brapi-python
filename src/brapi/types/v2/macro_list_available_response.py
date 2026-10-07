# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .macro_series_public import MacroSeriesPublic

__all__ = ["MacroListAvailableResponse"]


class MacroListAvailableResponse(BaseModel):
    categories: List[str]
    """Todas as categorias. Os filtros não mudam esta lista."""

    count: int
    """Número de séries em `results`, depois dos filtros."""

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    results: List[MacroSeriesPublic]
    """Séries encontradas.

    Com `q`, a ordem é por relevância: código, nome alternativo, nome e descrição.
    """

    took: int
    """Tempo de processamento, em milissegundos."""
