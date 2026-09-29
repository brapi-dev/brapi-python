# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DictionaryRetrieveResponse", "Field"]


class Field(BaseModel):
    calculation: Optional[str] = None

    category: str

    description: str

    endpoints: List[str]

    key: str

    label: str

    type: Literal["number", "string", "boolean", "date", "object", "array"]

    unit: Optional[str] = None


class DictionaryRetrieveResponse(BaseModel):
    fields: List[Field]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
