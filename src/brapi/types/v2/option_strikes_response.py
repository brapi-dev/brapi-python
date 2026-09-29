# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OptionStrikesResponse"]


class OptionStrikesResponse(BaseModel):
    expiration_date: str = FieldInfo(alias="expirationDate")
    """Vencimento consultado, no formato YYYY-MM-DD."""

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    side: Optional[Literal["call", "put"]] = None
    """Lado filtrado: `call`, `put` ou `null` sem filtro."""

    strikes: List[float]
    """Preços de exercício em ordem crescente."""

    took: int
    """Tempo de processamento, em milissegundos."""

    traded_only: Literal[True] = FieldInfo(alias="tradedOnly")
    """Sempre `true`: os strikes vêm das séries negociadas."""

    underlying: str
    """Ativo subjacente consultado, em maiúsculas."""
