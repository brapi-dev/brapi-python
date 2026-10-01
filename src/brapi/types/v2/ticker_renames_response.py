# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TickerRenamesResponse", "Result"]


class Result(BaseModel):
    canonical_symbol: str = FieldInfo(alias="canonicalSymbol")
    """Ticker atual. Se o ativo mudou de ticker mais de uma vez, é o último."""

    effective_date: str = FieldInfo(alias="effectiveDate")
    """Data de início da negociação do novo ticker no formato YYYY-MM-DD."""

    new_symbol: str = FieldInfo(alias="newSymbol")
    """Ticker novo divulgado no evento."""

    old_symbol: str = FieldInfo(alias="oldSymbol")
    """Ticker antigo."""

    conversion_ratio: Optional[float] = FieldInfo(alias="conversionRatio", default=None)
    """Quantidade de ações novas por ação antiga.

    Presente quando houve conversão de ações.
    """


class TickerRenamesResponse(BaseModel):
    count: float

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    results: List[Result]

    took: int
    """Tempo de processamento, em milissegundos."""
