# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .debenture_profile import DebentureProfile

__all__ = ["DebentureProfileResponse"]


class DebentureProfileResponse(BaseModel):
    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    results: List[DebentureProfile]

    took: int
    """Tempo de processamento, em milissegundos."""
