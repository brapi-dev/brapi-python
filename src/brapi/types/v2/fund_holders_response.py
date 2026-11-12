# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FundHoldersResponse", "Asset", "Fund", "FundPosition", "Pagination", "Summary"]


class Asset(BaseModel):
    cnpj: Optional[str] = None

    name: Optional[str] = None

    symbol: Optional[str] = None

    symbols: List[str]
    """Tickers buscados na bolsa."""

    type: Literal["fund", "company", "security"]
    """
    `fund` (cotas de um fundo e, se listado, o ticker dele), `company` (ações e
    dívida de uma empresa) ou `security` (um ticker).
    """


class FundPosition(BaseModel):
    asset_class: Literal[
        "equity",
        "bdr",
        "fund",
        "governmentBond",
        "repo",
        "privateCredit",
        "bankSecurity",
        "foreign",
        "derivative",
        "cash",
        "receivable",
        "payable",
        "other",
    ] = FieldInfo(alias="assetClass")
    """
    Classe do ativo: `equity` (ações), `bdr`, `fund` (cotas de fundos),
    `governmentBond` (títulos públicos), `repo` (compromissadas), `privateCredit`
    (crédito privado), `bankSecurity` (títulos de bancos), `foreign` (exterior),
    `derivative`, `cash` (caixa), `receivable` (valores a receber), `payable`
    (valores a pagar) ou `other`.
    """

    market_value: float = FieldInfo(alias="marketValue")
    """Valor em reais."""

    quantity: Optional[float] = None
    """Quantidade.

    `null` para títulos sem código de uma empresa: podem ser mais de um.
    """

    symbol: Optional[str] = None
    """Ticker ou código do ativo. `null` para cotas de fundo e títulos sem código."""

    weight_percent: Optional[float] = FieldInfo(alias="weightPercent", default=None)
    """Peso no patrimônio do fundo, em %."""


class Fund(BaseModel):
    asset_type: Optional[Literal["fii", "fiagro", "fiinfra", "fif", "fidc", "fip", "etf", "other"]] = FieldInfo(
        alias="assetType", default=None
    )

    cnpj: str

    market_value: float = FieldInfo(alias="marketValue")
    """Valor da posição em reais, com ações emprestadas."""

    name: Optional[str] = None

    net_assets: Optional[float] = FieldInfo(alias="netAssets", default=None)
    """Patrimônio líquido do fundo, em reais."""

    positions: List[FundPosition]
    """Cada ativo que forma a posição, do maior valor ao menor.

    Mostra, por exemplo, quanto o fundo tem em cada ação e em cada debênture da
    empresa.
    """

    quantity: Optional[float] = None
    """Quantidade.

    Vendas a descoberto ficam negativas. `null` quando a posição junta mais de um
    ativo da empresa, ou títulos sem código.
    """

    symbol: Optional[str] = None

    weight_percent: Optional[float] = FieldInfo(alias="weightPercent", default=None)
    """Peso do ativo no patrimônio do fundo, em %."""


class Pagination(BaseModel):
    has_next_page: bool = FieldInfo(alias="hasNextPage")

    limit: int

    page: int

    total_items: int = FieldInfo(alias="totalItems")

    total_pages: int = FieldInfo(alias="totalPages")


class Summary(BaseModel):
    funds_count: int = FieldInfo(alias="fundsCount")

    total_market_value: float = FieldInfo(alias="totalMarketValue")

    total_quantity: Optional[float] = FieldInfo(alias="totalQuantity", default=None)
    """Soma das quantidades.

    `null` quando a resposta junta mais de um ativo da empresa, ou títulos sem
    código.
    """


class FundHoldersResponse(BaseModel):
    asset: Asset

    funds: List[Fund]

    pagination: Pagination

    reference_date: Optional[str] = FieldInfo(alias="referenceDate", default=None)

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    summary: Summary

    took: int
    """Tempo de processamento, em milissegundos."""
