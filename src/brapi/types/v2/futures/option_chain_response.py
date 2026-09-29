# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["OptionChainResponse", "Series"]


class Series(BaseModel):
    allocation_round_lot: Optional[int] = FieldInfo(alias="allocationRoundLot", default=None)
    """Lote padrão de negociação."""

    automatic_exercise: Optional[bool] = FieldInfo(alias="automaticExercise", default=None)
    """`true` quando a opção é exercida automaticamente no vencimento."""

    average: Optional[float] = None
    """Preço médio."""

    cfic_code: Optional[str] = FieldInfo(alias="cficCode", default=None)
    """Código CFI."""

    close: Optional[float] = None
    """Preço de fechamento."""

    contract_multiplier: Optional[float] = FieldInfo(alias="contractMultiplier", default=None)
    """Multiplicador do contrato, herdado do futuro. Ex.: 330 arrobas no boi gordo."""

    date: int
    """Data do pregão, em timestamp Unix (segundos)."""

    exercise_type: Optional[str] = FieldInfo(alias="exerciseType", default=None)
    """Tipo de exercício."""

    expiration_date: str = FieldInfo(alias="expirationDate")
    """Data de vencimento, no formato YYYY-MM-DD."""

    financial_volume: Optional[float] = FieldInfo(alias="financialVolume", default=None)
    """Volume financeiro, em reais."""

    first_trade_date: Optional[str] = FieldInfo(alias="firstTradeDate", default=None)
    """Data do primeiro pregão da série, no formato YYYY-MM-DD."""

    high: Optional[float] = None
    """Preço máximo."""

    isin: Optional[str] = None
    """Código ISIN da série de opção."""

    last_trade_date: Optional[str] = FieldInfo(alias="lastTradeDate", default=None)
    """Data do último pregão da série, no formato YYYY-MM-DD."""

    low: Optional[float] = None
    """Preço mínimo."""

    open: Optional[float] = None
    """Preço de abertura."""

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

    oscillation_pct: Optional[float] = FieldInfo(alias="oscillationPct", default=None)
    """Variação percentual em relação ao pregão anterior."""

    premium_upfront: Optional[bool] = FieldInfo(alias="premiumUpfront", default=None)
    """`true` se o prêmio é pago à vista, `false` se é diferido."""

    reference_price: Optional[float] = FieldInfo(alias="referencePrice", default=None)
    """Preço de referência do pregão. Costuma vir preenchido mesmo sem negócio."""

    segment: Literal["financial", "agribusiness"]
    """Segmento do contrato: `financial` ou `agribusiness`."""

    strike: float
    """Preço de exercício da opção, na unidade de cotação do futuro."""

    symbol: str
    """Código da série de opção. Ex.: `BGIH27C028550`."""

    trades: Optional[float] = None
    """Número de negócios."""

    underlying_asset: str = FieldInfo(alias="underlyingAsset")
    """Código do ativo do futuro. Ex.: `BGI`."""

    underlying_future: Optional[str] = FieldInfo(alias="underlyingFuture", default=None)
    """Contrato futuro de base, quando informado."""

    volume: Optional[float] = None
    """Número de contratos negociados."""


class OptionChainResponse(BaseModel):
    date: str

    expiration_date: str = FieldInfo(alias="expirationDate")

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    series: List[Series]

    took: int
    """Tempo de processamento, em milissegundos."""

    underlying: str
