# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["AnalyticsRetrieveResponse", "Analytics"]


class Analytics(BaseModel):
    allocation_round_lot: Optional[int] = FieldInfo(alias="allocationRoundLot", default=None)
    """Lote padrão de negociação."""

    automatic_exercise: Optional[bool] = FieldInfo(alias="automaticExercise", default=None)
    """`true` quando a opção é exercida automaticamente no vencimento."""

    cfic_code: Optional[str] = FieldInfo(alias="cficCode", default=None)
    """Código CFI."""

    confidence: Literal["high", "medium", "low", "none"]
    """Confiança do cálculo.

    `none` indica IV e gregas nulas, com o motivo em `nullReason`. `low` indica
    cálculo sobre `referencePrice`.
    """

    contract_multiplier: Optional[float] = FieldInfo(alias="contractMultiplier", default=None)
    """Multiplicador do contrato, herdado do futuro. Ex.: 330 arrobas no boi gordo."""

    date: str
    """Data do pregão, no formato YYYY-MM-DD."""

    delta: Optional[float] = None
    """Variação do prêmio para 1 unidade de variação no ativo subjacente."""

    dividend_yield: Optional[float] = FieldInfo(alias="dividendYield", default=None)
    """Sempre `0` em opções sobre futuros."""

    exercise_type: Optional[str] = FieldInfo(alias="exerciseType", default=None)
    """Tipo de exercício."""

    expiration_date: str = FieldInfo(alias="expirationDate")
    """Data de vencimento, no formato YYYY-MM-DD."""

    first_trade_date: Optional[str] = FieldInfo(alias="firstTradeDate", default=None)
    """Data do primeiro pregão da série, no formato YYYY-MM-DD."""

    gamma: Optional[float] = None
    """Variação do delta para 1 unidade de variação no ativo subjacente."""

    implied_volatility: Optional[float] = FieldInfo(alias="impliedVolatility", default=None)
    """Volatilidade implícita anual, em decimal."""

    isin: Optional[str] = None
    """Código ISIN da série de opção."""

    last_trade_date: Optional[str] = FieldInfo(alias="lastTradeDate", default=None)
    """Data do último pregão da série, no formato YYYY-MM-DD."""

    model: Literal["black-76", "cox-ross-rubinstein-futures", "unsupported"]
    """Modelo de cálculo.

    Séries americanas usam árvore binomial sobre o futuro
    (`cox-ross-rubinstein-futures`). Séries europeias usam `black-76`. `unsupported`
    quando o estilo da opção é desconhecido.
    """

    null_reason: Optional[str] = FieldInfo(alias="nullReason", default=None)
    """Motivo dos campos calculados nulos.

    Ex.: `no_trades`, `missing_underlying_price`, `iv_not_converged`.
    """

    open_interest: Optional[float] = FieldInfo(alias="openInterest", default=None)
    """Contratos em aberto na série, na última apuração até a data pedida."""

    open_interest_change: Optional[float] = FieldInfo(alias="openInterestChange", default=None)
    """Variação de contratos em aberto desde a apuração anterior."""

    open_interest_date: Optional[str] = FieldInfo(alias="openInterestDate", default=None)
    """Data da apuração usada, no formato YYYY-MM-DD.

    Pode ser anterior à data do pregão.
    """

    option_price: Optional[float] = FieldInfo(alias="optionPrice", default=None)
    """Preço da opção usado para calcular a volatilidade implícita."""

    option_style: Optional[Literal["american", "european"]] = FieldInfo(alias="optionStyle", default=None)
    """`american` permite exercício até o vencimento.

    `european` permite exercício só no vencimento.
    """

    option_type: Literal["call", "put"] = FieldInfo(alias="optionType")
    """`call` (opção de compra) ou `put` (opção de venda)."""

    premium_upfront: Optional[bool] = FieldInfo(alias="premiumUpfront", default=None)
    """`true` se o prêmio é pago à vista, `false` se é diferido."""

    price_source: Literal["close", "referencePrice", "none"] = FieldInfo(alias="priceSource")
    """Preço usado para calcular a IV.

    `close` é o fechamento negociado. Sem negócio, o cálculo usa `referencePrice`,
    com `confidence` igual a `low`.
    """

    rho: Optional[float] = None
    """Variação do prêmio para 1,00 de variação na taxa de juro.

    Divida por 100 para 1 ponto percentual.
    """

    risk_free_rate: Optional[float] = FieldInfo(alias="riskFreeRate", default=None)
    """Taxa livre de risco anual, em decimal. Ex.: 0.105 para 10,5%."""

    segment: Literal["financial", "agribusiness"]
    """Segmento do contrato: `financial` ou `agribusiness`."""

    strike: float
    """Preço de exercício da opção, na unidade de cotação do futuro."""

    symbol: str
    """Código da série de opção. Ex.: `BGIH27C028550`."""

    theta: Optional[float] = None
    """Variação do prêmio com a passagem do tempo, por ano."""

    time_to_expiration_years: Optional[float] = FieldInfo(alias="timeToExpirationYears", default=None)
    """Tempo até o vencimento, em anos."""

    underlying_asset: str = FieldInfo(alias="underlyingAsset")
    """Código do ativo do futuro. Ex.: `BGI`."""

    underlying_future: Optional[str] = FieldInfo(alias="underlyingFuture", default=None)
    """Contrato futuro de base, quando informado."""

    underlying_price: Optional[float] = FieldInfo(alias="underlyingPrice", default=None)
    """Preço do futuro subjacente usado no cálculo."""

    vega: Optional[float] = None
    """Variação do prêmio para 1,00 de variação na volatilidade.

    Divida por 100 para 1 ponto percentual.
    """


class AnalyticsRetrieveResponse(BaseModel):
    analytics: List[Analytics]

    date: str

    expiration_date: str = FieldInfo(alias="expirationDate")

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""

    underlying: str
