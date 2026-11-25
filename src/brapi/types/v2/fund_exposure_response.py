# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "FundExposureResponse",
    "AssetClass",
    "Company",
    "CompanyPath",
    "CompanyPathVia",
    "Country",
    "Coverage",
    "CoverageOtherUnresolved",
    "CoverageUnresolved",
    "Input",
    "Pagination",
    "Sector",
    "Totals",
]


class AssetClass(BaseModel):
    asset_class: Literal["equity", "fixedIncome", "cash", "commodity", "crypto", "fund", "other"] = FieldInfo(
        alias="assetClass"
    )
    """
    `equity` (ações e BDRs), `fixedIncome` (renda fixa), `cash` (caixa e valores a
    pagar e receber), `commodity`, `crypto`, `fund` (fundos que não abrem) ou
    `other`.
    """

    value: Optional[float] = None

    weight_percent: float = FieldInfo(alias="weightPercent")
    """Peso na cesta, em %."""


class CompanyPathVia(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None

    symbol: Optional[str] = None


class CompanyPath(BaseModel):
    input: str
    """Item da cesta."""

    via: List[CompanyPathVia]
    """Fundos entre o item e a empresa, no caminho de maior peso.

    Vazio quando o item é a própria ação.
    """

    weight_percent: float = FieldInfo(alias="weightPercent")
    """Peso que vem por este item, em % da cesta."""


class Company(BaseModel):
    id: str
    """Chave da empresa: junta classes de ações e BDRs da mesma empresa."""

    b3_symbols: List[str] = FieldInfo(alias="b3Symbols")
    """Tickers da empresa na B3 (ações, units, BDRs)."""

    country: Optional[str] = None

    isin: Optional[str] = None

    name: Optional[str] = None

    paths: List[CompanyPath]
    """Até 10 itens da cesta que levam à empresa, do maior para o menor."""

    paths_count: int = FieldInfo(alias="pathsCount")
    """Quantos itens da cesta levam à empresa."""

    rank: int

    sector: Optional[str] = None

    symbol: Optional[str] = None
    """Ticker na bolsa de origem, quando conhecido."""

    value: Optional[float] = None

    weight_percent: float = FieldInfo(alias="weightPercent")
    """Peso na cesta, em %."""


class Country(BaseModel):
    country: str
    """Código ISO do país."""

    country_name: Optional[str] = FieldInfo(alias="countryName", default=None)

    weight_percent: float = FieldInfo(alias="weightPercent")
    """Peso no patrimônio, em %."""


class CoverageOtherUnresolved(BaseModel):
    """Soma das partes que não abrem além das 50 listadas."""

    count: int

    weight_percent: float = FieldInfo(alias="weightPercent")
    """Peso das partes fora de `unresolved`, em % da cesta."""


class CoverageUnresolved(BaseModel):
    id: Optional[str] = None

    kind: Optional[Literal["localFund", "foreignFund", "etfBdr", "singleAsset"]] = None
    """
    `localFund` (fundo brasileiro), `foreignFund` (fundo do exterior), `etfBdr` (BDR
    de ETF) ou `singleAsset` (um ativo só, como ouro ou bitcoin).
    """

    name: Optional[str] = None

    reason: Literal[
        "confidential",
        "noReport",
        "staleReport",
        "belowThreshold",
        "depthLimit",
        "cycle",
        "noComposition",
        "inconsistentReport",
        "notFound",
    ]
    """
    Por que o fundo não abre: `confidential` (posição confidencial), `noReport` (sem
    carteira), `staleReport` (carteira longe do mês), `belowThreshold` (peso
    pequeno), `depthLimit` (muitos níveis), `cycle` (o fundo já está acima),
    `noComposition` (sem carteira pública), `inconsistentReport` (as posições não
    batem com o patrimônio) ou `notFound` (item da cesta que não é ticker, fundo ou
    BDR de ETF conhecido).
    """

    symbol: Optional[str] = None

    via: List[str]
    """Até 10 itens da cesta por onde chega esta parte."""

    via_count: int = FieldInfo(alias="viaCount")
    """Quantos itens da cesta chegam a esta parte."""

    weight_percent: float = FieldInfo(alias="weightPercent")
    """Peso no fundo pedido, em %."""


class Coverage(BaseModel):
    oldest_reference_date: Optional[str] = FieldInfo(alias="oldestReferenceDate", default=None)

    other_unresolved: CoverageOtherUnresolved = FieldInfo(alias="otherUnresolved")
    """Soma das partes que não abrem além das 50 listadas."""

    resolved_percent: float = FieldInfo(alias="resolvedPercent")
    """Parte da cesta que chega a um ativo final, em %."""

    unresolved: List[CoverageUnresolved]
    """As 50 maiores partes que não abrem, da maior para a menor."""


class Input(BaseModel):
    id: Optional[str] = None

    cnpj: Optional[str] = None

    kind: Literal["localFund", "etfBdr", "singleAsset", "stock", "bdr", "fund", "unknown"]
    """
    Como o item foi lido: fundo brasileiro, BDR de ETF, ativo único (ouro, bitcoin),
    ação ou unit, BDR de empresa, fundo listado sem carteira mensal, ou
    desconhecido.
    """

    name: Optional[str] = None

    reason: Optional[
        Literal[
            "confidential",
            "noReport",
            "staleReport",
            "belowThreshold",
            "depthLimit",
            "cycle",
            "noComposition",
            "inconsistentReport",
            "notFound",
        ]
    ] = None
    """
    Por que o fundo não abre: `confidential` (posição confidencial), `noReport` (sem
    carteira), `staleReport` (carteira longe do mês), `belowThreshold` (peso
    pequeno), `depthLimit` (muitos níveis), `cycle` (o fundo já está acima),
    `noComposition` (sem carteira pública), `inconsistentReport` (as posições não
    batem com o patrimônio) ou `notFound` (item da cesta que não é ticker, fundo ou
    BDR de ETF conhecido).
    """

    reference_date: Optional[str] = FieldInfo(alias="referenceDate", default=None)
    """Data da carteira do item."""

    resolved_percent: float = FieldInfo(alias="resolvedPercent")
    """Parte do item que chega a um ativo final, em %."""

    symbol: Optional[str] = None

    value: Optional[float] = None

    weight_percent: float = FieldInfo(alias="weightPercent")
    """Peso do item na cesta, em %."""


class Pagination(BaseModel):
    has_next_page: bool = FieldInfo(alias="hasNextPage")

    limit: int

    page: int

    total_items: int = FieldInfo(alias="totalItems")

    total_pages: int = FieldInfo(alias="totalPages")


class Sector(BaseModel):
    sector: str

    weight_percent: float = FieldInfo(alias="weightPercent")
    """Peso no patrimônio, em %."""


class Totals(BaseModel):
    companies_count: int = FieldInfo(alias="companiesCount")

    companies_weight_percent: float = FieldInfo(alias="companiesWeightPercent")
    """Peso de todas as empresas, em %."""

    listed_weight_percent: float = FieldInfo(alias="listedWeightPercent")
    """Peso das empresas desta página."""

    not_companies_weight_percent: float = FieldInfo(alias="notCompaniesWeightPercent")
    """
    Peso do que não é ação: renda fixa, caixa, ouro, criptoativos, fundos sem
    carteira.
    """

    other_companies_weight_percent: float = FieldInfo(alias="otherCompaniesWeightPercent")
    """Peso das empresas fora desta página."""


class FundExposureResponse(BaseModel):
    asset_classes: List[AssetClass] = FieldInfo(alias="assetClasses")

    companies: List[Company]

    countries: List[Country]

    country_coverage_percent: Optional[float] = FieldInfo(alias="countryCoveragePercent", default=None)

    coverage: Coverage

    inputs: List[Input]

    pagination: Pagination

    reference_date: Optional[str] = FieldInfo(alias="referenceDate", default=None)

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    sector_coverage_percent: Optional[float] = FieldInfo(alias="sectorCoveragePercent", default=None)
    """Parte do peso das empresas que tem setor, em %."""

    sectors: List[Sector]

    took: int
    """Tempo de processamento, em milissegundos."""

    totals: Totals

    total_value: Optional[float] = FieldInfo(alias="totalValue", default=None)
    """Soma dos valores informados. `null` com pesos."""
