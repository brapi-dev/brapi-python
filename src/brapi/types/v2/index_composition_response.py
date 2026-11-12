# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "IndexCompositionResponse",
    "Index",
    "IndexHolding",
    "IndexPagination",
    "IndexSummary",
    "IndexSummaryCountry",
    "IndexSummarySector",
    "IndexTrackingFund",
]


class IndexHolding(BaseModel):
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

    country: Optional[str] = None

    isin: Optional[str] = None

    name: Optional[str] = None

    rank: int

    sector: Optional[str] = None

    symbol: Optional[str] = None

    weight_percent: float = FieldInfo(alias="weightPercent")
    """Peso na parte investida do ETF, em % (4.52 = 4,52%)."""


class IndexPagination(BaseModel):
    has_next_page: bool = FieldInfo(alias="hasNextPage")

    limit: int

    page: int

    total_items: int = FieldInfo(alias="totalItems")

    total_pages: int = FieldInfo(alias="totalPages")


class IndexSummaryCountry(BaseModel):
    country: str
    """Código ISO do país."""

    country_name: Optional[str] = FieldInfo(alias="countryName", default=None)

    weight_percent: float = FieldInfo(alias="weightPercent")
    """Peso no patrimônio, em %."""


class IndexSummarySector(BaseModel):
    sector: str

    weight_percent: float = FieldInfo(alias="weightPercent")
    """Peso no patrimônio, em %."""


class IndexSummary(BaseModel):
    countries: List[IndexSummaryCountry]

    sector_coverage_percent: Optional[float] = FieldInfo(alias="sectorCoveragePercent", default=None)
    """Parte do peso em ações e BDRs que tem setor, em %. `null` sem ações."""

    sectors: List[IndexSummarySector]


class IndexTrackingFund(BaseModel):
    cnpj: str

    name: Optional[str] = None

    symbol: str


class Index(BaseModel):
    approximated: Literal[True]
    """
    Sempre `true`: a composição é a carteira do ETF que segue o índice, não a
    carteira oficial.
    """

    holdings: List[IndexHolding]

    holdings_count: int = FieldInfo(alias="holdingsCount")

    name: str

    pagination: IndexPagination

    reference_date: str = FieldInfo(alias="referenceDate")
    """Fim do mês da carteira do ETF."""

    summary: IndexSummary

    symbol: str

    tracking_fund: IndexTrackingFund = FieldInfo(alias="trackingFund")


class IndexCompositionResponse(BaseModel):
    indexes: List[Index]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
