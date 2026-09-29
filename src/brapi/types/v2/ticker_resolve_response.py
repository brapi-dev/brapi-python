# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TickerResolveResponse", "Result"]


class Result(BaseModel):
    changed: bool
    """`true` quando o ticker enviado foi trocado pelo ticker atual."""

    effective_date: Optional[str] = FieldInfo(alias="effectiveDate", default=None)
    """Data efetiva do renome. Nulo quando não há renome."""

    requested_symbol: str = FieldInfo(alias="requestedSymbol")
    """Ticker enviado na requisição."""

    status: Literal["active", "renamed"]
    """`renamed` quando o ticker enviado mudou.

    `active` quando não há renome conhecido.
    """

    symbol: str
    """Ticker atual. Use este nas próximas consultas."""


class TickerResolveResponse(BaseModel):
    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    results: List[Result]

    took: int
    """Tempo de processamento, em milissegundos."""
