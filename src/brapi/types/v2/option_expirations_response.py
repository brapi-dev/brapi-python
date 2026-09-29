# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OptionExpirationsResponse"]


class OptionExpirationsResponse(BaseModel):
    expirations: List[str]
    """Datas de vencimento em ordem crescente, no formato YYYY-MM-DD."""

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""

    traded_only: Literal[True] = FieldInfo(alias="tradedOnly")
    """Sempre `true`: a lista vem das séries negociadas."""

    underlying: str
    """Ativo subjacente consultado, em maiúsculas."""
