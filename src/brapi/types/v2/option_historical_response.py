# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .option_series import OptionSeries

__all__ = ["OptionHistoricalResponse", "Option", "OptionHistory"]


class OptionHistory(BaseModel):
    ask: Optional[float] = None
    """Melhor oferta de venda no fechamento."""

    average: Optional[float] = None
    """Preço médio."""

    bid: Optional[float] = None
    """Melhor oferta de compra no fechamento."""

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

    reference_price: Optional[float] = FieldInfo(alias="referencePrice", default=None)
    """Preço de referência do pregão."""

    trades: Optional[float] = None
    """Número de negócios."""

    volume: Optional[float] = None
    """Número de contratos negociados."""


class Option(OptionSeries):
    """Dados da série e `history`, com um ponto por pregão no intervalo pedido."""

    history: List[OptionHistory]
    """Um ponto por pregão no intervalo pedido."""


class OptionHistoricalResponse(BaseModel):
    option: Option
    """Dados da série e `history`, com um ponto por pregão no intervalo pedido."""

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
