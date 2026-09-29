# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AnalyticsRetrieveResponse", "Analytics"]


class Analytics(BaseModel):
    allocation_round_lot: Optional[int] = FieldInfo(alias="allocationRoundLot", default=None)
    """Lote padrão de negociação. Em geral, 100 nas opções sobre ações."""

    confidence: Literal["high", "medium", "low", "none"]
    """Confiança do cálculo.

    `none` indica IV e gregas nulas, com o motivo em `nullReason`.
    """

    date: str
    """Data do pregão, no formato YYYY-MM-DD."""

    delta: Optional[float] = None
    """Variação do prêmio para 1 unidade de variação no ativo subjacente."""

    dividend_yield: Optional[float] = FieldInfo(alias="dividendYield", default=None)
    """Yield contínuo dos dividendos anunciados até a data do cálculo.

    `0` sem dividendo anunciado. Não inclui estimativas.
    """

    expiration_date: str = FieldInfo(alias="expirationDate")
    """Data de vencimento, no formato YYYY-MM-DD."""

    first_trade_date: str = FieldInfo(alias="firstTradeDate")
    """Data do primeiro pregão da série, no formato YYYY-MM-DD."""

    gamma: Optional[float] = None
    """Variação do delta para 1 unidade de variação no ativo subjacente."""

    implied_volatility: Optional[float] = FieldInfo(alias="impliedVolatility", default=None)
    """Volatilidade implícita anual, em decimal."""

    last_trade_date: str = FieldInfo(alias="lastTradeDate")
    """Data do último pregão da série, no formato YYYY-MM-DD."""

    market: Literal["equity", "index", "currency"]
    """
    Mercado da opção: `equity` para ação ou ETF, `index` para índice, `currency`
    para DOL e WDO.
    """

    model: Literal["black-scholes-merton", "barone-adesi-whaley", "cox-ross-rubinstein", "unsupported"]
    """Modelo de cálculo.

    Séries americanas usam árvore binomial (`cox-ross-rubinstein`). Séries europeias
    usam `black-scholes-merton`. `unsupported` quando o estilo da opção é
    desconhecido.
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

    `european` permite exercício só no vencimento. Nulo quando o cadastro da série
    não informa o estilo.
    """

    price_source: Literal["close", "referencePrice", "none"] = FieldInfo(alias="priceSource")
    """Preço usado para calcular a IV.

    Aqui é sempre `close` ou `none`. Sem negócio no dia, não há cálculo.
    """

    rho: Optional[float] = None
    """Variação do prêmio para 1,00 de variação na taxa de juro.

    Divida por 100 para 1 ponto percentual.
    """

    risk_free_rate: Optional[float] = FieldInfo(alias="riskFreeRate", default=None)
    """Taxa livre de risco anual, em decimal. Ex.: 0.105 para 10,5%."""

    side: Literal["call", "put"]
    """`call` (opção de compra) ou `put` (opção de venda)."""

    strike: Optional[float] = None
    """Preço de exercício da opção."""

    symbol: str
    """Código da série de opção. Ex.: PETRF783."""

    theta: Optional[float] = None
    """Variação do prêmio com a passagem do tempo, por ano."""

    time_to_expiration_years: Optional[float] = FieldInfo(alias="timeToExpirationYears", default=None)
    """Tempo até o vencimento, em anos."""

    underlying_price: Optional[float] = FieldInfo(alias="underlyingPrice", default=None)
    """Preço do ativo subjacente usado no cálculo."""

    underlying_symbol: Optional[str] = FieldInfo(alias="underlyingSymbol", default=None)
    """Ativo subjacente da opção. Ex.: PETR4."""

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
