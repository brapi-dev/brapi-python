# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["StockEarningsCalendarResponse", "Pagination", "Result", "ResultDateChange", "ResultLinks"]


class Pagination(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")

    limit: int

    page: int

    total: int


class ResultDateChange(BaseModel):
    announced_at: str = FieldInfo(alias="announcedAt")
    """Data em que a empresa informou a mudança."""

    field: Literal["date", "callDate"]
    """`date` para a data de divulgação, `callDate` para a apresentação de resultados."""

    from_: str = FieldInfo(alias="from")

    to: str


class ResultLinks(BaseModel):
    calendar: Optional[str] = None
    """Calendário de eventos de onde vem a data prevista."""

    document: Optional[str] = None
    """Documento com os resultados entregues."""


class Result(BaseModel):
    id: str
    """Identificador estável da divulgação."""

    call_date: Optional[str] = FieldInfo(alias="callDate", default=None)
    """Data da apresentação pública dos resultados."""

    cnpj: Optional[str] = None
    """CNPJ da empresa. null para empresas estrangeiras com BDRs."""

    company_name: str = FieldInfo(alias="companyName")

    date: str
    """Data de divulgação: a data real quando houver, senão a data prevista."""

    date_changes: List[ResultDateChange] = FieldInfo(alias="dateChanges")
    """Mudanças de data, da mais antiga para a mais recente."""

    date_status: Literal["confirmed", "estimated"] = FieldInfo(alias="dateStatus")
    """`confirmed` quando a empresa informou ou já divulgou a data.

    `estimated` quando a data é uma estimativa, feita com a data do mesmo período no
    ano anterior.
    """

    debentures: List[str]
    """Códigos das debêntures da empresa que ainda não venceram.

    Plano Pro; vazio nos demais planos.
    """

    filing_date: Optional[str] = FieldInfo(alias="filingDate", default=None)
    """Data de entrega das demonstrações financeiras."""

    fiscal_period: Literal["Q1", "Q2", "Q3", "H1", "FY"] = FieldInfo(alias="fiscalPeriod")
    """Período do exercício.

    `FY` é o exercício completo, que inclui o 4º trimestre. `H1` é o 1º semestre,
    para empresas que divulgam resultados semestrais.
    """

    fiscal_year: int = FieldInfo(alias="fiscalYear")
    """Exercício social.

    Empresas com exercício fora do ano civil usam o ano em que o exercício termina.
    """

    issuer_code: str = FieldInfo(alias="issuerCode")
    """Código da empresa na B3."""

    links: ResultLinks

    period_end: str = FieldInfo(alias="periodEnd")
    """Último dia do período."""

    planned_date: Optional[str] = FieldInfo(alias="plannedDate", default=None)
    """Última data prevista no calendário da empresa."""

    release_time: Optional[Literal["beforeMarket", "duringMarket", "afterMarket"]] = FieldInfo(
        alias="releaseTime", default=None
    )
    """
    Horário da divulgação em relação ao pregão de Nova York (09h30 às 16h00, horário
    local): `beforeMarket`, `duringMarket` ou `afterMarket`. Só para BDRs. null
    quando não informado.
    """

    reported_date: Optional[str] = FieldInfo(alias="reportedDate", default=None)
    """Data em que os resultados foram entregues."""

    status: Literal["scheduled", "published", "overdue"]
    """`published` quando os resultados foram entregues.

    `overdue` quando a data informada pela empresa passou há mais de 2 dias úteis
    sem entrega. Uma data estimada que passou continua `scheduled`. `scheduled` nos
    demais casos.
    """

    tickers: List[str]
    """Tickers das ações ou BDRs da empresa.

    Vazio quando a empresa não tem ações listadas.
    """

    updated_at: str = FieldInfo(alias="updatedAt")
    """Momento da última mudança nesta divulgação."""


class StockEarningsCalendarResponse(BaseModel):
    from_: str = FieldInfo(alias="from")

    pagination: Pagination

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    results: List[Result]

    to: str

    took: int
    """Tempo de processamento, em milissegundos."""
