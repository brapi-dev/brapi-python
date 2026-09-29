# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FutureSpecs"]


class FutureSpecs(BaseModel):
    allocation_round_lot: Optional[int] = FieldInfo(alias="allocationRoundLot", default=None)
    """Tamanho do lote, em contratos."""

    asset_description: Optional[str] = FieldInfo(alias="assetDescription", default=None)
    """Nome do ativo em português."""

    cfic_code: Optional[str] = FieldInfo(alias="cficCode", default=None)
    """Código CFI."""

    contract_multiplier: Optional[float] = FieldInfo(alias="contractMultiplier", default=None)
    """Valor de um ponto, em reais. Ex.: `WIN` 0,2, `BGI` 330, `DI1` 1."""

    delivery_type: Optional[str] = FieldInfo(alias="deliveryType", default=None)
    """Tipo de entrega: `Financial` ou `Physical`."""

    exercise_type: Optional[str] = FieldInfo(alias="exerciseType", default=None)
    """Forma de cotação: `Price` ou `Rate`."""

    expiration_date: str = FieldInfo(alias="expirationDate")
    """Data de vencimento, no formato YYYY-MM-DD."""

    first_trade_date: Optional[str] = FieldInfo(alias="firstTradeDate", default=None)
    """Data do primeiro pregão, no formato YYYY-MM-DD."""

    isin: Optional[str] = None
    """Código ISIN."""

    last_trade_date: Optional[str] = FieldInfo(alias="lastTradeDate", default=None)
    """Data do último pregão, no formato YYYY-MM-DD."""

    quotation_type: Literal["price", "rate"] = FieldInfo(alias="quotationType")
    """`rate` em contratos de juros, como DI1 e DAP, com preços em % a.a.

    `price` nos demais.
    """

    segment: Literal["financial", "agribusiness"]
    """`financial` para índices, juros e moedas. `agribusiness` para commodities."""

    symbol: str
    """Código do contrato. Ex.: `WINM26`, `BGIF27`, `DI1F27`."""

    trading_currency: Optional[str] = FieldInfo(alias="tradingCurrency", default=None)
    """Moeda de negociação. Quase sempre `BRL`."""

    underlying_asset: str = FieldInfo(alias="underlyingAsset")
    """Código do ativo, sem mês e ano. Ex.: `WIN`, `BGI`, `DI1`."""
