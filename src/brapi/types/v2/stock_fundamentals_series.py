# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["StockFundamentalsSeries"]


class StockFundamentalsSeries(BaseModel):
    changed: bool

    requested_symbol: str = FieldInfo(alias="requestedSymbol")

    symbol: str

    data: Optional[object] = None
    """Dados do endpoint. Pode ser objeto, array ou null."""
