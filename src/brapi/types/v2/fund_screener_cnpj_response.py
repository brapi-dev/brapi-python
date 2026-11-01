# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FundScreenerCnpjResponse", "Pagination", "Result", "ResultMetrics"]


class Pagination(BaseModel):
    has_next_page: bool = FieldInfo(alias="hasNextPage")

    limit: float

    page: float

    total_items: float = FieldInfo(alias="totalItems")

    total_pages: float = FieldInfo(alias="totalPages")


class ResultMetrics(BaseModel):
    """Indicadores do fundo pelo último informe diário."""

    equity: Optional[float] = None
    """Patrimônio líquido.

    Patrimônio líquido no último informe diário, em reais. Unidade: reais. Nulo
    quando não há dado.
    """

    nav_per_share: Optional[float] = FieldInfo(alias="navPerShare", default=None)
    """Valor da cota.

    Valor da cota no último informe diário, em reais. Unidade: reais. Nulo quando
    não há dado.
    """

    net_flow1m: Optional[float] = FieldInfo(alias="netFlow1m", default=None)
    """Captação líquida em 1 mês.

    Aplicações menos resgates em 1 mês, em reais. Negativa quando saiu mais dinheiro
    do que entrou. Unidade: reais. Nulo quando não há dado.
    """

    return12m: Optional[float] = None
    """Rentabilidade em 12 meses.

    Variação da cota em 12 meses, em fração. Unidade: fração (0.06 = 6%). Nulo
    quando não há dado.
    """

    return1m: Optional[float] = None
    """Rentabilidade em 1 mês.

    Variação da cota em 1 mês, em fração. Nula quando a cota muda mais de 10 vezes
    no período (desdobramento ou grupamento). Unidade: fração (0.06 = 6%). Nulo
    quando não há dado.
    """

    return36m: Optional[float] = None
    """Rentabilidade em 36 meses.

    Variação da cota em 36 meses, em fração. Unidade: fração (0.06 = 6%). Nulo
    quando não há dado.
    """

    return_day: Optional[float] = FieldInfo(alias="returnDay", default=None)
    """Variação no dia.

    Variação da cota desde o informe anterior, em fração (0.0074 = 0,74%). Unidade:
    fração (0.06 = 6%). Nulo quando não há dado.
    """

    return_ytd: Optional[float] = FieldInfo(alias="returnYtd", default=None)
    """Rentabilidade no ano.

    Variação da cota desde o último informe do ano anterior, em fração. Unidade:
    fração (0.06 = 6%). Nulo quando não há dado.
    """

    total_investors: Optional[float] = FieldInfo(alias="totalInvestors", default=None)
    """Cotistas.

    Número de cotistas no último informe diário. Unidade: quantidade. Nulo quando
    não há dado.
    """


class Result(BaseModel):
    administrator_name: Optional[str] = FieldInfo(alias="administratorName", default=None)

    anbima_classification: Optional[str] = FieldInfo(alias="anbimaClassification", default=None)
    """Classificação ANBIMA do fundo."""

    asset_type: str = FieldInfo(alias="assetType")
    """Tipo do fundo no cadastro, como fif (fundo de investimento financeiro) ou fidc."""

    classification: Optional[str] = None
    """Classe do fundo na CVM: Renda Fixa, Multimercado, Ações, Cambial ou FMP-FGTS."""

    cnpj: str
    """CNPJ do fundo, só os 14 dígitos."""

    formatted_cnpj: str = FieldInfo(alias="formattedCnpj")

    legal_name: Optional[str] = FieldInfo(alias="legalName", default=None)
    """Razão social do fundo no cadastro da CVM."""

    manager_name: Optional[str] = FieldInfo(alias="managerName", default=None)

    metrics: ResultMetrics
    """Indicadores do fundo pelo último informe diário."""

    name: Optional[str] = None
    """Nome do fundo."""

    nav_date: str = FieldInfo(alias="navDate")
    """Data do último informe diário, de onde vêm os indicadores (AAAA-MM-DD)."""


class FundScreenerCnpjResponse(BaseModel):
    pagination: Pagination

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    results: List[Result]

    took: int
    """Tempo de processamento, em milissegundos."""
