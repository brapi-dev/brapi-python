# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["StockInsiderTransactionsResponse", "Result", "ResultData", "ResultDataPagination", "ResultDataTransaction"]


class ResultDataPagination(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")

    limit: int

    page: int

    total: int


class ResultDataTransaction(BaseModel):
    id: str
    """Identificador da movimentação nesta versão do relatório."""

    company_relation: Literal["company", "parent", "subsidiary"] = FieldInfo(alias="companyRelation")

    description: Optional[str] = None

    direction: Literal["credit", "debit"]

    filing_date: str = FieldInfo(alias="filingDate")
    """Data de apresentação do relatório."""

    intermediary: Optional[str] = None

    movement_type: str = FieldInfo(alias="movementType")

    quantity: Optional[str] = None
    """Quantidade inteira exata. Pode ser negativa."""

    report_date: str = FieldInfo(alias="reportDate")
    """Primeiro dia do mês de referência. Não é a data da movimentação."""

    role_description: Optional[str] = FieldInfo(alias="roleDescription", default=None)

    role_group: Optional[Literal["controller", "board", "director", "fiscalCouncil", "statutoryBody"]] = FieldInfo(
        alias="roleGroup", default=None
    )

    security_class: Optional[str] = FieldInfo(alias="securityClass", default=None)

    security_company: str = FieldInfo(alias="securityCompany")
    """Nome da empresa que emite o valor mobiliário."""

    security_type: str = FieldInfo(alias="securityType")

    transaction_date: Optional[str] = FieldInfo(alias="transactionDate", default=None)
    """Data da movimentação em YYYY-MM-DD."""

    unit_price: Optional[str] = FieldInfo(alias="unitPrice", default=None)
    """Valor decimal exato em texto, sem ajuste por desdobramentos.

    null indica valor ausente.
    """

    version: int
    """Versão do relatório. Uma correção substitui a versão anterior."""

    volume: Optional[str] = None
    """Valor decimal exato em texto, sem ajuste por desdobramentos.

    null indica valor ausente.
    """


class ResultData(BaseModel):
    cnpj: str

    company_name: Optional[str] = FieldInfo(alias="companyName", default=None)

    disclosure_level: Literal["roleGroup"] = FieldInfo(alias="disclosureLevel")
    """Movimentações agrupadas por cargo. Os dados não identificam cada pessoa."""

    end_date: str = FieldInfo(alias="endDate")

    first_report_date: Optional[str] = FieldInfo(alias="firstReportDate", default=None)
    """Primeiro mês de relatório disponível para a empresa.

    Pode haver meses sem dados.
    """

    latest_filing_date: Optional[str] = FieldInfo(alias="latestFilingDate", default=None)
    """Data de apresentação mais recente.

    Uma correção pode se referir a um mês anterior.
    """

    latest_report_date: Optional[str] = FieldInfo(alias="latestReportDate", default=None)
    """Último mês de relatório disponível para a empresa."""

    pagination: ResultDataPagination

    start_date: str = FieldInfo(alias="startDate")

    transactions: List[ResultDataTransaction]
    """Movimentações que correspondem aos filtros.

    Uma lista vazia não indica posição igual a zero.
    """


class Result(BaseModel):
    changed: bool

    data: ResultData

    requested_symbol: str = FieldInfo(alias="requestedSymbol")

    symbol: str


class StockInsiderTransactionsResponse(BaseModel):
    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    results: List[Result]

    took: int
    """Tempo de processamento, em milissegundos."""
