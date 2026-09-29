# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OptionChainResponse", "Series"]


class Series(BaseModel):
    allocation_round_lot: Optional[int] = FieldInfo(alias="allocationRoundLot", default=None)
    """Lote padrão de negociação. Em geral, 100 nas opções sobre ações."""

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

    expiration_date: str = FieldInfo(alias="expirationDate")
    """Data de vencimento, no formato YYYY-MM-DD."""

    financial_volume: Optional[float] = FieldInfo(alias="financialVolume", default=None)
    """Volume financeiro, em reais."""

    first_trade_date: str = FieldInfo(alias="firstTradeDate")
    """Data do primeiro pregão da série, no formato YYYY-MM-DD."""

    high: Optional[float] = None
    """Preço máximo."""

    last_trade_date: str = FieldInfo(alias="lastTradeDate")
    """Data do último pregão da série, no formato YYYY-MM-DD."""

    low: Optional[float] = None
    """Preço mínimo."""

    market: Literal["equity", "index", "currency"]
    """
    Mercado da opção: `equity` para ação ou ETF, `index` para índice, `currency`
    para DOL e WDO.
    """

    open: Optional[float] = None
    """Preço de abertura."""

    open_interest: Optional[float] = FieldInfo(alias="openInterest", default=None)
    """Contratos em aberto na série, na última apuração até a data pedida."""

    open_interest_change: Optional[float] = FieldInfo(alias="openInterestChange", default=None)
    """Variação de contratos em aberto desde a apuração anterior."""

    open_interest_date: Optional[str] = FieldInfo(alias="openInterestDate", default=None)
    """Data da apuração usada, no formato YYYY-MM-DD.

    Pode ser anterior à data do pregão.
    """

    option_style: Optional[Literal["american", "european"]] = FieldInfo(alias="optionStyle", default=None)
    """`american` permite exercício até o vencimento.

    `european` permite exercício só no vencimento. Nulo quando o cadastro da série
    não informa o estilo.
    """

    reference_price: Optional[float] = FieldInfo(alias="referencePrice", default=None)
    """Preço de referência do pregão."""

    side: Literal["call", "put"]
    """`call` (opção de compra) ou `put` (opção de venda)."""

    strike: Optional[float] = None
    """Preço de exercício da opção."""

    symbol: str
    """Código da série de opção. Ex.: PETRF783."""

    trades: Optional[float] = None
    """Número de negócios."""

    underlying_symbol: Optional[str] = FieldInfo(alias="underlyingSymbol", default=None)
    """Ativo subjacente da opção. Ex.: PETR4."""

    volume: Optional[float] = None
    """Número de contratos negociados."""


class OptionChainResponse(BaseModel):
    date: str
    """Último pregão com dados até a data pedida, no formato YYYY-MM-DD."""

    expiration_date: str = FieldInfo(alias="expirationDate")
    """Vencimento consultado, no formato YYYY-MM-DD."""

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    series: List[Series]
    """Séries do vencimento. Cada uma traz a cotação do seu último pregão até `date`."""

    took: int
    """Tempo de processamento, em milissegundos."""

    traded_only: Literal[True] = FieldInfo(alias="tradedOnly")
    """Sempre `true`: a lista traz só séries com cotação nos 10 dias até `date`."""

    underlying: str
    """Ativo subjacente consultado, em maiúsculas."""
