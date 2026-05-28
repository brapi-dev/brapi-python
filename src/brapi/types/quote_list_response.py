# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["QuoteListResponse", "Index", "Stock"]


class Index(BaseModel):
    name: str

    stock: str


class Stock(BaseModel):
    change: Optional[float] = None
    """Variação percentual"""

    close: Optional[float] = None
    """Preço de fechamento"""

    logo: Optional[str] = None
    """URL do logo"""

    market_cap: Optional[float] = None
    """Capitalização de mercado"""

    name: str
    """Nome da empresa"""

    sector: Optional[str] = None
    """Setor"""

    stock: str
    """Ticker do ativo"""

    sub_type: Optional[str] = FieldInfo(alias="subType", default=None)
    """
    Classificação aditiva do ativo: stock, unit, fii, etf, fi-infra, fi-agro, fip,
    fidc ou bdr
    """

    type: Optional[str] = None
    """Tipo do ativo"""

    volume: Optional[float] = None
    """Volume negociado"""


class QuoteListResponse(BaseModel):
    available_sectors: List[str] = FieldInfo(alias="availableSectors")

    available_stock_types: List[str] = FieldInfo(alias="availableStockTypes")

    available_sub_type_types: List[str] = FieldInfo(alias="availableSubTypeTypes")

    indexes: List[Index]

    stocks: List[Stock]

    current_page: Optional[float] = FieldInfo(alias="currentPage", default=None)

    has_next_page: Optional[bool] = FieldInfo(alias="hasNextPage", default=None)

    items_per_page: Optional[float] = FieldInfo(alias="itemsPerPage", default=None)

    total_count: Optional[float] = FieldInfo(alias="totalCount", default=None)

    total_pages: Optional[float] = FieldInfo(alias="totalPages", default=None)
