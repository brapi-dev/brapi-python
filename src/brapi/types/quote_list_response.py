# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["QuoteListResponse", "Index", "Stock"]


class Index(BaseModel):
    name: Optional[str] = None
    """Nome do índice (ex: `IBOVESPA`)."""

    stock: Optional[str] = None
    """Ticker do índice (ex: `^BVSP`)."""


class Stock(BaseModel):
    change: Optional[float] = None
    """Variação percentual do preço em relação ao fechamento anterior."""

    close: Optional[float] = None
    """Preço de fechamento mais recente ou último preço negociado."""

    logo: Optional[str] = None
    """URL para a imagem do logo da empresa/ativo."""

    market_cap: Optional[float] = None
    """Capitalização de mercado (Preço x Quantidade de Ações).

    Pode ser nulo para FIIs ou outros tipos.
    """

    name: Optional[str] = None
    """Nome do ativo ou empresa (ex: `PETROBRAS PN`)."""

    sector: Optional[str] = None
    """Setor de atuação da empresa (ex: `Energy Minerals`, `Finance`).

    Pode ser nulo ou variar para FIIs.
    """

    stock: Optional[str] = None
    """Ticker do ativo (ex: `PETR4`, `MXRF11`)."""

    type: Optional[Literal["stock", "fund", "bdr"]] = None
    """
    Tipo do ativo: `stock` (Ação), `fund` (Fundo Imobiliário/FII), `bdr` (Brazilian
    Depositary Receipt).
    """

    volume: Optional[int] = None
    """Volume financeiro negociado no último pregão ou dia atual."""


class QuoteListResponse(BaseModel):
    available_sectors: Optional[List[str]] = FieldInfo(alias="availableSectors", default=None)
    """
    Lista de todos os setores disponíveis que podem ser usados no parâmetro de
    filtro `sector`.
    """

    available_stock_types: Optional[List[Literal["stock", "fund", "bdr"]]] = FieldInfo(
        alias="availableStockTypes", default=None
    )
    """
    Lista dos tipos de ativos (`stock`, `fund`, `bdr`) disponíveis que podem ser
    usados no parâmetro de filtro `type`.
    """

    current_page: Optional[int] = FieldInfo(alias="currentPage", default=None)
    """Número da página atual retornada nos resultados."""

    has_next_page: Optional[bool] = FieldInfo(alias="hasNextPage", default=None)
    """
    Indica se existe uma próxima página de resultados (`true`) ou se esta é a última
    página (`false`).
    """

    indexes: Optional[List[Index]] = None
    """Lista resumida de índices relevantes (geralmente inclui IBOVESPA)."""

    items_per_page: Optional[int] = FieldInfo(alias="itemsPerPage", default=None)
    """Número de itens (ativos) retornados por página (conforme `limit` ou padrão)."""

    stocks: Optional[List[Stock]] = None
    """Lista paginada e filtrada dos ativos solicitados."""

    total_count: Optional[int] = FieldInfo(alias="totalCount", default=None)
    """
    Número total de ativos encontrados que correspondem aos filtros aplicados (sem
    considerar a paginação).
    """

    total_pages: Optional[int] = FieldInfo(alias="totalPages", default=None)
    """Número total de páginas existentes para a consulta/filtros aplicados."""
