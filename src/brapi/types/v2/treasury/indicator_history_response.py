# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["IndicatorHistoryResponse", "Result", "ResultHistory", "ResultRateInfo"]


class ResultHistory(BaseModel):
    base_date: str = FieldInfo(alias="baseDate")
    """Data da taxa e do preço, no formato YYYY-MM-DD."""

    base_price: Optional[float] = FieldInfo(alias="basePrice", default=None)
    """Preço unitário base, em reais."""

    buy_price: Optional[float] = FieldInfo(alias="buyPrice", default=None)
    """Preço unitário indicativo de compra, em reais."""

    buy_rate: Optional[float] = FieldInfo(alias="buyRate", default=None)
    """Taxa indicativa de compra, em % a.a.

    O sentido muda por indexador. Veja `rateInfo`.
    """

    sell_price: Optional[float] = FieldInfo(alias="sellPrice", default=None)
    """Preço unitário indicativo de venda, em reais."""

    sell_rate: Optional[float] = FieldInfo(alias="sellRate", default=None)
    """Taxa indicativa de venda, em % a.a.

    O sentido muda por indexador. Veja `rateInfo`.
    """


class ResultRateInfo(BaseModel):
    """Como ler `buyRate` e `sellRate`. O sentido muda por indexador."""

    description: str
    """Texto que explica como ler `buyRate` e `sellRate` neste título."""

    rate_type: Literal["spreadOverSelic", "nominalAnnualRate", "realAnnualRateOverIpca", "realAnnualRateOverIgpm"] = (
        FieldInfo(alias="rateType")
    )
    """O que `buyRate` e `sellRate` medem."""

    rate_unit: str = FieldInfo(alias="rateUnit")
    """Unidade de `buyRate` e `sellRate`."""


class Result(BaseModel):
    bond_type: str = FieldInfo(alias="bondType")
    """Nome do título no Tesouro Direto."""

    coupon_type: Literal["zero", "semestral"] = FieldInfo(alias="couponType")
    """`semestral` para títulos com juros semestrais, `zero` para os demais."""

    history: List[ResultHistory]

    indexer: Literal["selic", "prefixado", "ipca", "igpm"]
    """Indexador do título. Renda+ e Educa+ usam `ipca`."""

    maturity_date: Optional[str] = FieldInfo(alias="maturityDate", default=None)
    """Data de vencimento, no formato YYYY-MM-DD."""

    rate_info: ResultRateInfo = FieldInfo(alias="rateInfo")
    """Como ler `buyRate` e `sellRate`. O sentido muda por indexador."""

    symbol: str


class IndicatorHistoryResponse(BaseModel):
    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    results: List[Result]

    took: int
    """Tempo de processamento, em milissegundos."""
