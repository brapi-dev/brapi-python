# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CryptoRetrieveResponse", "Coin", "CoinHistoricalDataPrice"]


class CoinHistoricalDataPrice(BaseModel):
    """Representa um ponto na série histórica de preços de uma criptomoeda."""

    adjusted_close: Optional[float] = FieldInfo(alias="adjustedClose", default=None)
    """Preço de fechamento ajustado (geralmente igual ao `close` para cripto)."""

    close: Optional[float] = None
    """Preço de fechamento da criptomoeda no intervalo."""

    date: Optional[int] = None
    """Data do ponto de dados, representada como um timestamp UNIX."""

    high: Optional[float] = None
    """Preço máximo atingido no intervalo."""

    low: Optional[float] = None
    """Preço mínimo atingido no intervalo."""

    open: Optional[float] = None
    """Preço de abertura da criptomoeda no intervalo."""

    volume: Optional[int] = None
    """
    Volume negociado no intervalo (na criptomoeda ou na moeda de referência,
    verificar contexto).
    """


class Coin(BaseModel):
    """
    Contém os dados detalhados de uma criptomoeda específica retornada pelo endpoint `/api/v2/crypto`.
    """

    coin: Optional[str] = None
    """Sigla (ticker) da criptomoeda (ex: `BTC`, `ETH`)."""

    coin_image_url: Optional[str] = FieldInfo(alias="coinImageUrl", default=None)
    """URL da imagem do logo da criptomoeda."""

    coin_name: Optional[str] = FieldInfo(alias="coinName", default=None)
    """Nome completo da criptomoeda (ex: `Bitcoin`, `Ethereum`)."""

    currency: Optional[str] = None
    """Sigla da moeda fiduciária na qual os preços estão cotados (ex: `BRL`, `USD`)."""

    currency_rate_from_usd: Optional[float] = FieldInfo(alias="currencyRateFromUSD", default=None)
    """Taxa de câmbio da `currency` em relação ao USD (Dólar Americano).

    `1 USD = X currency`.
    """

    historical_data_price: Optional[List[CoinHistoricalDataPrice]] = FieldInfo(
        alias="historicalDataPrice", default=None
    )
    """
    Array contendo a série histórica de preços, retornado se `range` ou `interval`
    forem especificados.
    """

    market_cap: Optional[int] = FieldInfo(alias="marketCap", default=None)
    """Capitalização de mercado da criptomoeda na `currency` especificada."""

    regular_market_change: Optional[float] = FieldInfo(alias="regularMarketChange", default=None)
    """Variação absoluta do preço nas últimas 24 horas (ou período relevante)."""

    regular_market_change_percent: Optional[float] = FieldInfo(alias="regularMarketChangePercent", default=None)
    """Variação percentual do preço nas últimas 24 horas (ou período relevante)."""

    regular_market_day_high: Optional[float] = FieldInfo(alias="regularMarketDayHigh", default=None)
    """Preço máximo nas últimas 24 horas (ou período relevante)."""

    regular_market_day_low: Optional[float] = FieldInfo(alias="regularMarketDayLow", default=None)
    """Preço mínimo nas últimas 24 horas (ou período relevante)."""

    regular_market_day_range: Optional[str] = FieldInfo(alias="regularMarketDayRange", default=None)
    """
    String formatada mostrando o intervalo de preço das últimas 24h (Mínimo -
    Máximo).
    """

    regular_market_price: Optional[float] = FieldInfo(alias="regularMarketPrice", default=None)
    """Preço atual da criptomoeda na `currency` especificada."""

    regular_market_time: Optional[datetime] = FieldInfo(alias="regularMarketTime", default=None)
    """Timestamp da última atualização da cotação. Formato ISO 8601."""

    regular_market_volume: Optional[int] = FieldInfo(alias="regularMarketVolume", default=None)
    """Volume negociado nas últimas 24 horas (na `currency` especificada)."""

    used_interval: Optional[str] = FieldInfo(alias="usedInterval", default=None)
    """
    O intervalo (`interval`) efetivamente utilizado para os dados históricos, se
    solicitado.
    """

    used_range: Optional[str] = FieldInfo(alias="usedRange", default=None)
    """
    O período (`range`) efetivamente utilizado para os dados históricos, se
    solicitado.
    """

    valid_intervals: Optional[List[str]] = FieldInfo(alias="validIntervals", default=None)
    """Lista dos valores válidos para o parâmetro `interval` nesta criptomoeda."""

    valid_ranges: Optional[List[str]] = FieldInfo(alias="validRanges", default=None)
    """Lista dos valores válidos para o parâmetro `range` nesta criptomoeda."""


class CryptoRetrieveResponse(BaseModel):
    """Resposta principal do endpoint `/api/v2/crypto`."""

    coins: Optional[List[Coin]] = None
    """Array contendo os resultados detalhados para cada criptomoeda solicitada."""
