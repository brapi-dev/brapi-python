# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .future_specs import FutureSpecs

__all__ = ["FutureHistoricalResponse", "Future", "FutureHistory"]


class FutureHistory(BaseModel):
    average: Optional[float] = None
    """Preço médio do dia. Em % a.a. nos contratos de juros."""

    close: Optional[float] = None
    """Último negócio do dia. Em % a.a. nos contratos de juros."""

    date: int
    """Data do pregão, em Unix timestamp (segundos)."""

    financial_volume: Optional[float] = FieldInfo(alias="financialVolume", default=None)
    """Volume financeiro, em reais."""

    high: Optional[float] = None
    """Máxima do dia. Em % a.a. nos contratos de juros."""

    low: Optional[float] = None
    """Mínima do dia. Em % a.a. nos contratos de juros."""

    open: Optional[float] = None
    """Preço de abertura.

    Sempre `null`, porque os dados de fim de dia não trazem abertura.
    """

    oscillation_pct: Optional[float] = FieldInfo(alias="oscillationPct", default=None)
    """Variação em relação ao pregão anterior, em %."""

    reference_price: Optional[float] = FieldInfo(alias="referencePrice", default=None)
    """Preço de referência oficial."""

    settlement: Optional[float] = None
    """Preço de ajuste oficial do dia.

    Nos contratos de juros, vem em reais, como preço unitário.
    """

    settlement_rate: Optional[float] = FieldInfo(alias="settlementRate", default=None)
    """Taxa do ajuste, em % a.a. Só vem em contratos de juros."""

    trades: Optional[float] = None
    """Número de negócios."""

    volume: Optional[float] = None
    """Contratos negociados."""


class Future(FutureSpecs):
    history: List[FutureHistory]
    """Um item por pregão no período pedido."""


class FutureHistoricalResponse(BaseModel):
    future: Future

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
