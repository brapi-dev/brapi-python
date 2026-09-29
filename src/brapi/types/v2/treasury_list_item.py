# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TreasuryListItem", "RateInfo"]


class RateInfo(BaseModel):
    """Como ler `buyRate` e `sellRate`. O sentido muda por indexador."""

    description: str
    """Texto que explica como ler `buyRate` e `sellRate` neste título."""

    rate_type: Literal["spreadOverSelic", "nominalAnnualRate", "realAnnualRateOverIpca", "realAnnualRateOverIgpm"] = (
        FieldInfo(alias="rateType")
    )
    """O que `buyRate` e `sellRate` medem."""

    rate_unit: str = FieldInfo(alias="rateUnit")
    """Unidade de `buyRate` e `sellRate`."""


class TreasuryListItem(BaseModel):
    base_date: Optional[str] = FieldInfo(alias="baseDate", default=None)
    """Data da taxa e do preço, no formato YYYY-MM-DD."""

    base_price: Optional[float] = FieldInfo(alias="basePrice", default=None)
    """Preço unitário base, em reais."""

    bond_type: str = FieldInfo(alias="bondType")
    """Nome do título no Tesouro Direto."""

    buy_price: Optional[float] = FieldInfo(alias="buyPrice", default=None)
    """Preço unitário indicativo de compra, em reais."""

    buy_rate: Optional[float] = FieldInfo(alias="buyRate", default=None)
    """Taxa indicativa de compra, em % a.a.

    O sentido muda por indexador. Veja `rateInfo`.
    """

    coupon_type: Literal["zero", "semestral"] = FieldInfo(alias="couponType")
    """`semestral` para títulos com juros semestrais, `zero` para os demais."""

    duration_days: Optional[float] = FieldInfo(alias="durationDays", default=None)
    """Dias corridos da data-base até o vencimento."""

    indexer: Literal["selic", "prefixado", "ipca", "igpm"]
    """Indexador do título. Renda+ e Educa+ usam `ipca`."""

    maturity_date: Optional[str] = FieldInfo(alias="maturityDate", default=None)
    """Data de vencimento, no formato YYYY-MM-DD."""

    rate_info: RateInfo = FieldInfo(alias="rateInfo")
    """Como ler `buyRate` e `sellRate`. O sentido muda por indexador."""

    sell_price: Optional[float] = FieldInfo(alias="sellPrice", default=None)
    """Preço unitário indicativo de venda, em reais."""

    sell_rate: Optional[float] = FieldInfo(alias="sellRate", default=None)
    """Taxa indicativa de venda, em % a.a.

    O sentido muda por indexador. Veja `rateInfo`.
    """

    symbol: str
    """Código do título: nome e vencimento em DDMMAAAA."""
