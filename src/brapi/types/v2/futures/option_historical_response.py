# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .future_option_specs import FutureOptionSpecs

__all__ = ["OptionHistoricalResponse", "Option", "OptionHistory"]


class OptionHistory(BaseModel):
    average: Optional[float] = None
    """Preço médio."""

    close: Optional[float] = None
    """Preço de fechamento."""

    date: int
    """Data do pregão, em timestamp Unix (segundos)."""

    financial_volume: Optional[float] = FieldInfo(alias="financialVolume", default=None)
    """Volume financeiro, em reais."""

    high: Optional[float] = None
    """Preço máximo."""

    low: Optional[float] = None
    """Preço mínimo."""

    open: Optional[float] = None
    """Preço de abertura."""

    oscillation_pct: Optional[float] = FieldInfo(alias="oscillationPct", default=None)
    """Variação percentual em relação ao pregão anterior."""

    reference_price: Optional[float] = FieldInfo(alias="referencePrice", default=None)
    """Preço de referência do pregão. Costuma vir preenchido mesmo sem negócio."""

    trades: Optional[float] = None
    """Número de negócios."""

    volume: Optional[float] = None
    """Número de contratos negociados."""


class Option(FutureOptionSpecs):
    history: List[OptionHistory]


class OptionHistoricalResponse(BaseModel):
    option: Option

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
