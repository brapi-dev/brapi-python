# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["PositionRetrieveResponse", "Position"]


class Position(BaseModel):
    allocation_round_lot: Optional[int] = FieldInfo(alias="allocationRoundLot", default=None)
    """Lote padrão de negociação. Em geral, 100 nas opções sobre ações."""

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

    expiration_date: str = FieldInfo(alias="expirationDate")
    """Data de vencimento, no formato YYYY-MM-DD."""

    first_trade_date: str = FieldInfo(alias="firstTradeDate")
    """Data do primeiro pregão da série, no formato YYYY-MM-DD."""

    forward_price: Optional[float] = FieldInfo(alias="forwardPrice", default=None)
    """Preço a termo. Preenchido só em alguns segmentos."""

    isin: Optional[str] = None
    """Código ISIN da série de opção, não do ativo objeto."""

    last_trade_date: str = FieldInfo(alias="lastTradeDate")
    """Data do último pregão da série, no formato YYYY-MM-DD."""

    lender_quantity: Optional[float] = FieldInfo(alias="lenderQuantity", default=None)
    """Quantidade doadora em empréstimo de ativos."""

    market: Literal["equity", "index", "currency"]
    """
    Mercado da opção: `equity` para ação ou ETF, `index` para índice, `currency`
    para DOL e WDO.
    """

    open_interest: Optional[float] = FieldInfo(alias="openInterest", default=None)
    """Contratos em aberto na série, na última apuração até a data pedida."""

    open_interest_change: Optional[float] = FieldInfo(alias="openInterestChange", default=None)
    """Variação de contratos em aberto desde a apuração anterior."""

    open_interest_date: Optional[str] = FieldInfo(alias="openInterestDate", default=None)
    """Data da apuração usada, no formato YYYY-MM-DD.

    Pode ser anterior à data do pregão.
    """

    option_style: Optional[Literal["american", "european"]] = FieldInfo(alias="optionStyle", default=None)
    """`american` permite exercício até o vencimento.

    `european` permite exercício só no vencimento. Nulo quando o cadastro da série
    não informa o estilo.
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

    side: Literal["call", "put"]
    """`call` (opção de compra) ou `put` (opção de venda)."""

    strike: Optional[float] = None
    """Preço de exercício da opção."""

    symbol: str
    """Código da série de opção. Ex.: PETRF783."""

    total_position_quantity: Optional[float] = FieldInfo(alias="totalPositionQuantity", default=None)
    """Total de contratos em posição.

    É a origem de `openInterest` nas opções sobre ações.
    """

    uncovered_quantity: Optional[float] = FieldInfo(alias="uncoveredQuantity", default=None)
    """Contratos em posição descoberta."""

    underlying_symbol: Optional[str] = FieldInfo(alias="underlyingSymbol", default=None)
    """Ativo subjacente da opção. Ex.: PETR4."""


class PositionRetrieveResponse(BaseModel):
    date: str

    expiration_date: str = FieldInfo(alias="expirationDate")

    positions: List[Position]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""

    underlying: str
