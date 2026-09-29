# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OptionSeries"]


class OptionSeries(BaseModel):
    allocation_round_lot: Optional[int] = FieldInfo(alias="allocationRoundLot", default=None)
    """Lote padrão de negociação. Em geral, 100 nas opções sobre ações."""

    expiration_date: str = FieldInfo(alias="expirationDate")
    """Data de vencimento, no formato YYYY-MM-DD."""

    first_trade_date: str = FieldInfo(alias="firstTradeDate")
    """Data do primeiro pregão da série, no formato YYYY-MM-DD."""

    last_trade_date: str = FieldInfo(alias="lastTradeDate")
    """Data do último pregão da série, no formato YYYY-MM-DD."""

    market: Literal["equity", "index", "currency"]
    """
    Mercado da opção: `equity` para ação ou ETF, `index` para índice, `currency`
    para DOL e WDO.
    """

    option_style: Optional[Literal["american", "european"]] = FieldInfo(alias="optionStyle", default=None)
    """`american` permite exercício até o vencimento.

    `european` permite exercício só no vencimento. Nulo quando o cadastro da série
    não informa o estilo.
    """

    side: Literal["call", "put"]
    """`call` (opção de compra) ou `put` (opção de venda)."""

    strike: Optional[float] = None
    """Preço de exercício da opção."""

    symbol: str
    """Código da série de opção. Ex.: PETRF783."""

    underlying_symbol: Optional[str] = FieldInfo(alias="underlyingSymbol", default=None)
    """Ativo subjacente da opção. Ex.: PETR4."""
