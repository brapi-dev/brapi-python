# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ..option_series import OptionSeries

__all__ = ["PositionHistoryResponse", "Option", "OptionPosition"]


class OptionPosition(BaseModel):
    asset: Optional[str] = None
    """Código raiz do ativo objeto, sem o dígito da classe. Ex.: PETR."""

    blocked_quantity: Optional[float] = FieldInfo(alias="blockedQuantity", default=None)
    """Contratos em posição bloqueada."""

    borrower_quantity: Optional[float] = FieldInfo(alias="borrowerQuantity", default=None)
    """Quantidade tomadora em empréstimo de ativos."""

    covered_quantity: Optional[float] = FieldInfo(alias="coveredQuantity", default=None)
    """Contratos em posição coberta."""

    current_quantity: Optional[float] = FieldInfo(alias="currentQuantity", default=None)
    """Quantidade corrente. Preenchida só em alguns segmentos."""

    distribution_id: Optional[str] = FieldInfo(alias="distributionId", default=None)
    """Número de distribuição do ativo objeto."""

    expiration_code: Optional[str] = FieldInfo(alias="expirationCode", default=None)
    """Código de vencimento da apuração. Vem vazio nas opções sobre ações."""

    forward_price: Optional[float] = FieldInfo(alias="forwardPrice", default=None)
    """Preço a termo. Preenchido só em alguns segmentos."""

    isin: Optional[str] = None
    """Código ISIN da série de opção, não do ativo objeto."""

    lender_quantity: Optional[float] = FieldInfo(alias="lenderQuantity", default=None)
    """Quantidade doadora em empréstimo de ativos."""

    open_interest: Optional[float] = FieldInfo(alias="openInterest", default=None)
    """Contratos em aberto na série, na última apuração até a data pedida."""

    open_interest_change: Optional[float] = FieldInfo(alias="openInterestChange", default=None)
    """Variação de contratos em aberto desde a apuração anterior."""

    open_interest_date: Optional[str] = FieldInfo(alias="openInterestDate", default=None)
    """Data da apuração usada, no formato YYYY-MM-DD.

    Pode ser anterior à data do pregão.
    """

    report_date: str = FieldInfo(alias="reportDate")
    """Data da apuração, no formato YYYY-MM-DD."""

    reported_open_interest: Optional[float] = FieldInfo(alias="reportedOpenInterest", default=None)
    """Contratos em aberto na apuração do pregão.

    Vem vazio nas opções sobre ações. Use `openInterest`.
    """

    reported_open_interest_change: Optional[float] = FieldInfo(alias="reportedOpenInterestChange", default=None)
    """Variação de contratos em aberto na apuração do pregão.

    Vem vazia nas opções sobre ações. Use `openInterestChange`.
    """

    segment: str
    """Segmento da apuração. Ex.: EQUITY CALL."""

    total_position_quantity: Optional[float] = FieldInfo(alias="totalPositionQuantity", default=None)
    """Total de contratos em posição.

    É a origem de `openInterest` nas opções sobre ações.
    """

    uncovered_quantity: Optional[float] = FieldInfo(alias="uncoveredQuantity", default=None)
    """Contratos em posição descoberta."""


class Option(OptionSeries):
    positions: List[OptionPosition]


class PositionHistoryResponse(BaseModel):
    option: Option

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
