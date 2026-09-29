# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .macro_series_error import MacroSeriesError
from .macro_series_public import MacroSeriesPublic
from .macro_series_observation import MacroSeriesObservation
from .macro_series_alias_warning import MacroSeriesAliasWarning

__all__ = ["MacroRetrieveResponse", "Result"]


class Result(BaseModel):
    observations: List[MacroSeriesObservation]

    series: MacroSeriesPublic


class MacroRetrieveResponse(BaseModel):
    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    results: List[Result]

    took: int
    """Tempo de processamento, em milissegundos."""

    errors: Optional[List[MacroSeriesError]] = None

    warnings: Optional[List[MacroSeriesAliasWarning]] = None
