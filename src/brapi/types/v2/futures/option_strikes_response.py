# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["OptionStrikesResponse"]


class OptionStrikesResponse(BaseModel):
    expiration_date: str = FieldInfo(alias="expirationDate")

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    side: Optional[Literal["call", "put"]] = None

    strikes: List[float]

    took: int
    """Tempo de processamento, em milissegundos."""

    underlying: str
