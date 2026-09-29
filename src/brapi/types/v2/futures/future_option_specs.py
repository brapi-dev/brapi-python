# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["FutureOptionSpecs"]


class FutureOptionSpecs(BaseModel):
    allocation_round_lot: Optional[int] = FieldInfo(alias="allocationRoundLot", default=None)
    """Lote padrão de negociação."""

    automatic_exercise: Optional[bool] = FieldInfo(alias="automaticExercise", default=None)
    """`true` quando a opção é exercida automaticamente no vencimento."""

    cfic_code: Optional[str] = FieldInfo(alias="cficCode", default=None)
    """Código CFI."""

    contract_multiplier: Optional[float] = FieldInfo(alias="contractMultiplier", default=None)
    """Multiplicador do contrato, herdado do futuro. Ex.: 330 arrobas no boi gordo."""

    exercise_type: Optional[str] = FieldInfo(alias="exerciseType", default=None)
    """Tipo de exercício."""

    expiration_date: str = FieldInfo(alias="expirationDate")
    """Data de vencimento, no formato YYYY-MM-DD."""

    first_trade_date: Optional[str] = FieldInfo(alias="firstTradeDate", default=None)
    """Data do primeiro pregão da série, no formato YYYY-MM-DD."""

    isin: Optional[str] = None
    """Código ISIN da série de opção."""

    last_trade_date: Optional[str] = FieldInfo(alias="lastTradeDate", default=None)
    """Data do último pregão da série, no formato YYYY-MM-DD."""

    option_style: Optional[Literal["american", "european"]] = FieldInfo(alias="optionStyle", default=None)
    """`american` permite exercício até o vencimento.

    `european` permite exercício só no vencimento.
    """

    option_type: Literal["call", "put"] = FieldInfo(alias="optionType")
    """`call` (opção de compra) ou `put` (opção de venda)."""

    premium_upfront: Optional[bool] = FieldInfo(alias="premiumUpfront", default=None)
    """`true` se o prêmio é pago à vista, `false` se é diferido."""

    segment: Literal["financial", "agribusiness"]
    """Segmento do contrato: `financial` ou `agribusiness`."""

    strike: float
    """Preço de exercício da opção, na unidade de cotação do futuro."""

    symbol: str
    """Código da série de opção. Ex.: `BGIH27C028550`."""

    underlying_asset: str = FieldInfo(alias="underlyingAsset")
    """Código do ativo do futuro. Ex.: `BGI`."""

    underlying_future: Optional[str] = FieldInfo(alias="underlyingFuture", default=None)
    """Contrato futuro de base, quando informado."""
