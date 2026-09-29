# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FutureQuote"]


class FutureQuote(BaseModel):
    allocation_round_lot: Optional[int] = FieldInfo(alias="allocationRoundLot", default=None)
    """Tamanho do lote, em contratos."""

    asset_description: Optional[str] = FieldInfo(alias="assetDescription", default=None)
    """Nome do ativo em português."""

    average: Optional[float] = None
    """Preço médio do dia. Em % a.a. nos contratos de juros."""

    cfic_code: Optional[str] = FieldInfo(alias="cficCode", default=None)
    """Código CFI."""

    close: Optional[float] = None
    """Último negócio do dia. Em % a.a. nos contratos de juros."""

    contract_multiplier: Optional[float] = FieldInfo(alias="contractMultiplier", default=None)
    """Valor de um ponto, em reais. Ex.: `WIN` 0,2, `BGI` 330, `DI1` 1."""

    date: int
    """Data do pregão, em Unix timestamp (segundos)."""

    delivery_type: Optional[str] = FieldInfo(alias="deliveryType", default=None)
    """Tipo de entrega: `Financial` ou `Physical`."""

    exercise_type: Optional[str] = FieldInfo(alias="exerciseType", default=None)
    """Forma de cotação: `Price` ou `Rate`."""

    expiration_date: str = FieldInfo(alias="expirationDate")
    """Data de vencimento, no formato YYYY-MM-DD."""

    financial_volume: Optional[float] = FieldInfo(alias="financialVolume", default=None)
    """Volume financeiro, em reais."""

    first_trade_date: Optional[str] = FieldInfo(alias="firstTradeDate", default=None)
    """Data do primeiro pregão, no formato YYYY-MM-DD."""

    high: Optional[float] = None
    """Máxima do dia. Em % a.a. nos contratos de juros."""

    isin: Optional[str] = None
    """Código ISIN."""

    last_trade_date: Optional[str] = FieldInfo(alias="lastTradeDate", default=None)
    """Data do último pregão, no formato YYYY-MM-DD."""

    low: Optional[float] = None
    """Mínima do dia. Em % a.a. nos contratos de juros."""

    open: Optional[float] = None
    """Preço de abertura.

    Sempre `null`, porque os dados de fim de dia não trazem abertura.
    """

    oscillation_pct: Optional[float] = FieldInfo(alias="oscillationPct", default=None)
    """Variação em relação ao pregão anterior, em %."""

    quotation_type: Literal["price", "rate"] = FieldInfo(alias="quotationType")
    """`rate` em contratos de juros, como DI1 e DAP, com preços em % a.a.

    `price` nos demais.
    """

    reference_price: Optional[float] = FieldInfo(alias="referencePrice", default=None)
    """Preço de referência oficial."""

    segment: Literal["financial", "agribusiness"]
    """`financial` para índices, juros e moedas. `agribusiness` para commodities."""

    settlement: Optional[float] = None
    """Preço de ajuste oficial do dia.

    Nos contratos de juros, vem em reais, como preço unitário.
    """

    settlement_rate: Optional[float] = FieldInfo(alias="settlementRate", default=None)
    """Taxa do ajuste, em % a.a. Só vem em contratos de juros."""

    symbol: str
    """Código do contrato. Ex.: `WINM26`, `BGIF27`, `DI1F27`."""

    trades: Optional[float] = None
    """Número de negócios."""

    trading_currency: Optional[str] = FieldInfo(alias="tradingCurrency", default=None)
    """Moeda de negociação. Quase sempre `BRL`."""

    underlying_asset: str = FieldInfo(alias="underlyingAsset")
    """Código do ativo, sem mês e ano. Ex.: `WIN`, `BGI`, `DI1`."""

    volume: Optional[float] = None
    """Contratos negociados."""
