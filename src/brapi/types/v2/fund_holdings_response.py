# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "FundHoldingsResponse",
    "Fund",
    "FundHolding",
    "FundHoldingVia",
    "FundLookThrough",
    "FundLookThroughFund",
    "FundLookThroughFundSource",
    "FundPagination",
    "FundSource",
    "FundSummary",
    "FundSummaryAssetClass",
    "FundSummaryCountry",
    "FundSummarySector",
]


class FundHoldingVia(BaseModel):
    """Fundo pelo qual a posição é detida, quando ela vem de outro fundo.

    `null` para posição direta. Se a posição vem de mais de um caminho, mostra o de maior peso.
    """

    name: Optional[str] = None

    symbol: Optional[str] = None


class FundHolding(BaseModel):
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

    asset_type: Optional[str] = FieldInfo(alias="assetType", default=None)
    """Tipo do ativo como a fonte informa."""

    country: Optional[str] = None
    """Código ISO do país. Ativos locais sem país são `BR`."""

    isin: Optional[str] = None

    market_value: Optional[float] = FieldInfo(alias="marketValue", default=None)
    """Valor em reais.

    Para ativos de outro fundo, é o valor da cota vezes o peso do ativo nele.
    """

    maturity_date: Optional[str] = FieldInfo(alias="maturityDate", default=None)

    name: Optional[str] = None

    quantity: Optional[float] = None
    """Quantidade. `null` para ativos de outro fundo."""

    rank: int
    """Posição no ranking por peso, sem o filtro `assetClass`."""

    sector: Optional[str] = None
    """Setor da ação ou BDR, o mesmo de `/api/quote/list`.

    `null` para outros ativos e para ativos do exterior.
    """

    symbol: Optional[str] = None
    """Ticker na bolsa ou código no exterior."""

    via: Optional[FundHoldingVia] = None
    """Fundo pelo qual a posição é detida, quando ela vem de outro fundo.

    `null` para posição direta. Se a posição vem de mais de um caminho, mostra o de
    maior peso.
    """

    weight_percent: float = FieldInfo(alias="weightPercent")
    """Peso no patrimônio do fundo, em % (4.52 = 4,52%).

    Negativo para valores a pagar e posições vendidas.
    """


class FundLookThroughFundSource(BaseModel):
    name: Literal["SEC", "CVM"]

    url: Optional[str] = None


class FundLookThroughFund(BaseModel):
    cnpj: Optional[str] = None

    holdings_count: int = FieldInfo(alias="holdingsCount")

    name: Optional[str] = None

    reference_date: str = FieldInfo(alias="referenceDate")
    """Data da carteira do fundo aberto.

    Pode ser diferente da data do fundo pedido: fundos do exterior divulgam a
    carteira a cada trimestre.
    """

    source: FundLookThroughFundSource

    symbol: Optional[str] = None

    weight_percent: float = FieldInfo(alias="weightPercent")
    """Peso do fundo aberto no patrimônio, em %."""


class FundLookThrough(BaseModel):
    applied: bool

    funds: List[FundLookThroughFund]


class FundPagination(BaseModel):
    has_next_page: bool = FieldInfo(alias="hasNextPage")

    limit: int

    page: int

    total_items: int = FieldInfo(alias="totalItems")

    total_pages: int = FieldInfo(alias="totalPages")


class FundSource(BaseModel):
    document_id: Optional[float] = FieldInfo(alias="documentId", default=None)

    name: Literal["CVM"]

    url: Optional[str] = None


class FundSummaryAssetClass(BaseModel):
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

    weight_percent: float = FieldInfo(alias="weightPercent")
    """Peso no patrimônio, em %."""


class FundSummaryCountry(BaseModel):
    country: str
    """Código ISO do país."""

    country_name: Optional[str] = FieldInfo(alias="countryName", default=None)

    weight_percent: float = FieldInfo(alias="weightPercent")
    """Peso no patrimônio, em %."""


class FundSummarySector(BaseModel):
    sector: str

    weight_percent: float = FieldInfo(alias="weightPercent")
    """Peso no patrimônio, em %."""


class FundSummary(BaseModel):
    asset_classes: List[FundSummaryAssetClass] = FieldInfo(alias="assetClasses")

    confidential_until: Optional[str] = FieldInfo(alias="confidentialUntil", default=None)
    """Última data em que uma posição confidencial do mês fica pública."""

    confidential_weight_percent: float = FieldInfo(alias="confidentialWeightPercent")
    """Peso das posições confidenciais, em %. Elas não aparecem em `holdings`."""

    countries: List[FundSummaryCountry]
    """Peso por país. Sem valores a receber e a pagar."""

    holdings_count: int = FieldInfo(alias="holdingsCount")
    """Posições depois de juntar repetidas e abrir fundos."""

    sector_coverage_percent: Optional[float] = FieldInfo(alias="sectorCoveragePercent", default=None)
    """Parte do peso em ações e BDRs que tem setor, em %. `null` sem ações."""

    sectors: List[FundSummarySector]
    """Peso por setor das ações e BDRs com setor."""

    top10_weight_percent: float = FieldInfo(alias="top10WeightPercent")
    """Peso das 10 maiores posições, em %."""


class Fund(BaseModel):
    asset_type: Optional[Literal["fii", "fiagro", "fiinfra", "fif", "fidc", "fip", "etf", "other"]] = FieldInfo(
        alias="assetType", default=None
    )

    available_dates: List[str] = FieldInfo(alias="availableDates")
    """Meses com carteira, do mais recente ao mais antigo. Até 24."""

    cnpj: str

    holdings: List[FundHolding]

    look_through: FundLookThrough = FieldInfo(alias="lookThrough")

    name: Optional[str] = None

    net_assets: float = FieldInfo(alias="netAssets")
    """Patrimônio líquido, em reais."""

    pagination: FundPagination

    reference_date: str = FieldInfo(alias="referenceDate")
    """Fim do mês da carteira."""

    source: FundSource

    summary: FundSummary

    symbol: Optional[str] = None


class FundHoldingsResponse(BaseModel):
    funds: List[Fund]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
