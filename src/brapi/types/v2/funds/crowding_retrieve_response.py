# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["CrowdingRetrieveResponse", "Company", "Pagination", "Sector", "Summary"]


class Company(BaseModel):
    all_funds_count: int = FieldInfo(alias="allFundsCount")
    """Fundos com posição direta ou por meio de outros fundos."""

    b3_symbols: List[str] = FieldInfo(alias="b3Symbols")
    """Tickers da empresa na B3: ações, units e BDRs."""

    buyers_count: Optional[int] = FieldInfo(alias="buyersCount", default=None)
    """Fundos que compraram no mês."""

    cnpj: Optional[str] = None
    """CNPJ, para uma empresa da B3."""

    country: Optional[str] = None
    """País da empresa (ISO 3166-1 alfa-2)."""

    direct_value: float = FieldInfo(alias="directValue")
    """Posições dos próprios fundos: ações, units, BDRs e ações no exterior."""

    flow_value: Optional[float] = FieldInfo(alias="flowValue", default=None)
    """Compras menos vendas dos fundos no mês, em reais, ao preço do mês.

    `null` quando um evento muda a quantidade de ações sem fator conhecido.
    """

    foreign_funds_value: float = FieldInfo(alias="foreignFundsValue")
    """
    A parte dos fundos do exterior (ETFs, BDRs de ETF) que os fundos brasileiros
    têm.
    """

    funds_count: int = FieldInfo(alias="fundsCount")
    """Fundos com posição direta."""

    late_filers_value: float = FieldInfo(alias="lateFilersValue")
    """
    A parte de `directValue` dos fundos que ainda não entregaram a carteira do mês:
    a posição da carteira do mês anterior.
    """

    name: Optional[str] = None

    rank: int

    sector: Optional[str] = None
    """Setor, como na cotação do ticker."""

    sellers_count: Optional[int] = FieldInfo(alias="sellersCount", default=None)
    """Fundos que venderam no mês, inclusive os que zeraram a posição."""

    symbol: Optional[str] = None
    """Ticker na B3 com mais dinheiro dos fundos.

    Para uma empresa do exterior sem BDR, o ticker no exterior.
    """

    value: float
    """Dinheiro dos fundos na empresa, em reais: `directValue` + `foreignFundsValue`.

    Cada posição conta uma vez.
    """

    weight_percent: Optional[float] = FieldInfo(alias="weightPercent", default=None)
    """Parte de `summary.totalValue`, em %."""


class Pagination(BaseModel):
    has_next_page: bool = FieldInfo(alias="hasNextPage")

    limit: int

    page: int

    total_items: int = FieldInfo(alias="totalItems")

    total_pages: int = FieldInfo(alias="totalPages")


class Sector(BaseModel):
    bought_value: float = FieldInfo(alias="boughtValue")
    """Soma do saldo das empresas do setor que os fundos compraram no mês."""

    companies_count: int = FieldInfo(alias="companiesCount")

    flow_value: float = FieldInfo(alias="flowValue")
    """Saldo do setor no mês."""

    sector: str

    sold_value: float = FieldInfo(alias="soldValue")
    """Soma do saldo das empresas do setor que os fundos venderam no mês (negativo)."""

    value: float
    """Dinheiro dos fundos no setor, em reais."""

    weight_percent: Optional[float] = FieldInfo(alias="weightPercent", default=None)


class Summary(BaseModel):
    bought_companies_count: Optional[int] = FieldInfo(alias="boughtCompaniesCount", default=None)
    """Empresas com saldo de compra no mês."""

    companies_count: int = FieldInfo(alias="companiesCount")

    confidential_equity_value: float = FieldInfo(alias="confidentialEquityValue")
    """Ações e BDRs em posições confidenciais de todos os fundos, em reais.

    Elas não entram nos totais.
    """

    effective_companies: Optional[float] = FieldInfo(alias="effectiveCompanies", default=None)
    """Número efetivo de empresas: 1 dividido pela soma dos quadrados das partes.

    Dez empresas do mesmo tamanho dão 10.
    """

    flow_value: Optional[float] = FieldInfo(alias="flowValue", default=None)
    """Saldo do mês de todas as empresas."""

    funds_count: int = FieldInfo(alias="fundsCount")
    """Fundos com carteira no mês."""

    late_filers_value: float = FieldInfo(alias="lateFilersValue")
    """
    A parte de `totalValue` que vem da carteira do mês anterior dos fundos que ainda
    não entregaram a do mês.
    """

    late_funds_count: int = FieldInfo(alias="lateFundsCount")
    """Fundos com carteira no mês anterior que ainda não entregaram a do mês."""

    sold_companies_count: Optional[int] = FieldInfo(alias="soldCompaniesCount", default=None)
    """Empresas com saldo de venda no mês."""

    top10_weight_percent: Optional[float] = FieldInfo(alias="top10WeightPercent", default=None)
    """Parte do dinheiro nas 10 maiores empresas, em %."""

    top5_weight_percent: Optional[float] = FieldInfo(alias="top5WeightPercent", default=None)
    """Parte do dinheiro nas 5 maiores empresas, em %."""

    total_value: float = FieldInfo(alias="totalValue")
    """Dinheiro dos fundos em todas as empresas."""


class CrowdingRetrieveResponse(BaseModel):
    available_dates: List[str] = FieldInfo(alias="availableDates")
    """Meses disponíveis, do mais recente ao mais antigo."""

    companies: List[Company]

    pagination: Pagination

    previous_reference_date: Optional[str] = FieldInfo(alias="previousReferenceDate", default=None)
    """Mês com que o saldo compara. `null` no primeiro mês."""

    reference_date: Optional[str] = FieldInfo(alias="referenceDate", default=None)
    """Fim do mês das carteiras."""

    region: Literal["all", "brazil", "foreign"]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    sectors: List[Sector]

    summary: Optional[Summary] = None

    took: int
    """Tempo de processamento, em milissegundos."""
