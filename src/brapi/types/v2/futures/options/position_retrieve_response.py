# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["PositionRetrieveResponse", "Position"]


class Position(BaseModel):
    allocation_round_lot: Optional[int] = FieldInfo(alias="allocationRoundLot", default=None)
    """Lote padrão de negociação."""

    asset: Optional[str] = None
    """Código raiz do ativo objeto. Ex.: BGI."""

    automatic_exercise: Optional[bool] = FieldInfo(alias="automaticExercise", default=None)
    """`true` quando a opção é exercida automaticamente no vencimento."""

    blocked_quantity: Optional[float] = FieldInfo(alias="blockedQuantity", default=None)
    """Contratos em posição bloqueada."""

    borrower_quantity: Optional[float] = FieldInfo(alias="borrowerQuantity", default=None)
    """Quantidade tomadora em empréstimo de ativos."""

    cfic_code: Optional[str] = FieldInfo(alias="cficCode", default=None)
    """Código CFI."""

    contract_multiplier: Optional[float] = FieldInfo(alias="contractMultiplier", default=None)
    """Multiplicador do contrato, herdado do futuro. Ex.: 330 arrobas no boi gordo."""

    covered_quantity: Optional[float] = FieldInfo(alias="coveredQuantity", default=None)
    """Contratos em posição coberta."""

    current_quantity: Optional[float] = FieldInfo(alias="currentQuantity", default=None)
    """Quantidade corrente. Preenchida só em alguns segmentos."""

    distribution_id: Optional[str] = FieldInfo(alias="distributionId", default=None)
    """Número de distribuição do ativo objeto. Vem vazio nas opções sobre futuros."""

    exercise_type: Optional[str] = FieldInfo(alias="exerciseType", default=None)
    """Tipo de exercício."""

    expiration_code: Optional[str] = FieldInfo(alias="expirationCode", default=None)
    """Código de vencimento da apuração. Ex.: VVNK."""

    expiration_date: str = FieldInfo(alias="expirationDate")
    """Data de vencimento, no formato YYYY-MM-DD."""

    first_trade_date: Optional[str] = FieldInfo(alias="firstTradeDate", default=None)
    """Data do primeiro pregão da série, no formato YYYY-MM-DD."""

    forward_price: Optional[float] = FieldInfo(alias="forwardPrice", default=None)
    """Preço a termo. Preenchido só em alguns segmentos."""

    isin: Optional[str] = None
    """Código ISIN da série de opção, não do contrato futuro."""

    last_trade_date: Optional[str] = FieldInfo(alias="lastTradeDate", default=None)
    """Data do último pregão da série, no formato YYYY-MM-DD."""

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

    option_style: Optional[Literal["american", "european"]] = FieldInfo(alias="optionStyle", default=None)
    """`american` permite exercício até o vencimento.

    `european` permite exercício só no vencimento.
    """

    option_type: Literal["call", "put"] = FieldInfo(alias="optionType")
    """`call` (opção de compra) ou `put` (opção de venda)."""

    premium_upfront: Optional[bool] = FieldInfo(alias="premiumUpfront", default=None)
    """`true` se o prêmio é pago à vista, `false` se é diferido."""

    report_date: str = FieldInfo(alias="reportDate")
    """Data da apuração, no formato YYYY-MM-DD."""

    reported_open_interest: Optional[float] = FieldInfo(alias="reportedOpenInterest", default=None)
    """Contratos em aberto na apuração do pregão. É a origem de `openInterest`."""

    reported_open_interest_change: Optional[float] = FieldInfo(alias="reportedOpenInterestChange", default=None)
    """Variação de contratos em aberto na apuração do pregão.

    É a origem de `openInterestChange`.
    """

    report_segment: str = FieldInfo(alias="reportSegment")
    """Segmento da apuração.

    Ex.: AGRIBUSINESS. É diferente do campo `segment` do contrato.
    """

    segment: Literal["financial", "agribusiness"]
    """Segmento do contrato: `financial` ou `agribusiness`."""

    strike: float
    """Preço de exercício da opção, na unidade de cotação do futuro."""

    symbol: str
    """Código da série de opção. Ex.: `BGIH27C028550`."""

    total_position_quantity: Optional[float] = FieldInfo(alias="totalPositionQuantity", default=None)
    """Total de contratos em posição.

    Vem vazio na maior parte dos segmentos de futuros.
    """

    uncovered_quantity: Optional[float] = FieldInfo(alias="uncoveredQuantity", default=None)
    """Contratos em posição descoberta."""

    underlying_asset: str = FieldInfo(alias="underlyingAsset")
    """Código do ativo do futuro. Ex.: `BGI`."""

    underlying_future: Optional[str] = FieldInfo(alias="underlyingFuture", default=None)
    """Contrato futuro de base, quando informado."""


class PositionRetrieveResponse(BaseModel):
    date: str

    expiration_date: str = FieldInfo(alias="expirationDate")

    positions: List[Position]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""

    underlying: str
