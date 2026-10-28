# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FundScreenerResponse", "Pagination", "Result", "ResultFund", "ResultMetrics", "ResultQuote"]


class Pagination(BaseModel):
    has_next_page: bool = FieldInfo(alias="hasNextPage")

    limit: float

    page: float

    total_items: float = FieldInfo(alias="totalItems")

    total_pages: float = FieldInfo(alias="totalPages")


class ResultFund(BaseModel):
    administrator_name: Optional[str] = FieldInfo(alias="administratorName", default=None)

    cnpj: str

    etf_category: Optional[Literal["fixed-income", "equity", "crypto", "real-estate"]] = FieldInfo(
        alias="etfCategory", default=None
    )
    """Categoria do ETF. Nulo para os outros fundos."""

    last_dividend_date: Optional[str] = FieldInfo(alias="lastDividendDate", default=None)
    """Data-com do último rendimento dos últimos 12 meses (AAAA-MM-DD)."""

    management_type: Optional[str] = FieldInfo(alias="managementType", default=None)
    """Tipo de gestão do FII: Ativa ou Passiva."""

    manager_name: Optional[str] = FieldInfo(alias="managerName", default=None)

    mandate: Optional[str] = None
    """Mandato do FII no cadastro da CVM."""

    report_date: Optional[str] = FieldInfo(alias="reportDate", default=None)
    """
    Data do informe de onde vêm patrimônio, valor patrimonial por cota e cotistas
    (AAAA-MM-DD).
    """

    segment: Optional[str] = None
    """Segmento do FII no cadastro da CVM."""

    segment_type: Optional[str] = FieldInfo(alias="segmentType", default=None)
    """Tipo do FII: tijolo, papel, fof ou hibrido."""

    type: str
    """Tipo do fundo: fii, fiagro, fiinfra, etf, fidc, fip ou fif."""


class ResultMetrics(BaseModel):
    """Indicadores do fundo."""

    average_daily_traded_value: Optional[float] = FieldInfo(alias="averageDailyTradedValue", default=None)
    """Liquidez diária.

    Média do valor negociado por pregão nos últimos 30 dias, em reais. Dias sem
    negócio contam como zero. Unidade: reais. Nulo quando não há dado.
    """

    dividend_yield: Optional[float] = FieldInfo(alias="dividendYield", default=None)
    """Dividend yield 12m.

    Rendimentos dos últimos 12 meses, pela data-com, sobre o último preço, em fração
    (0.1 = 10%). Não soma amortizações. Nulo quando o fundo não pagou rendimentos.
    Unidade: fração (0.06 = 6%). Nulo quando não há dado.
    """

    equity: Optional[float] = None
    """Patrimônio líquido.

    Patrimônio líquido do último informe, em reais. Unidade: reais. Nulo quando não
    há dado.
    """

    income_months12m: Optional[float] = FieldInfo(alias="incomeMonths12m", default=None)
    """Meses com rendimento.

    Quantos dos últimos 12 meses tiveram rendimento, pela data-com. Mede a
    regularidade dos pagamentos. Unidade: quantidade. Nulo quando não há dado.
    """

    last_dividend: Optional[float] = FieldInfo(alias="lastDividend", default=None)
    """Último rendimento.

    Valor por cota do último rendimento, pela data-com, em reais. Unidade: reais.
    Nulo quando não há dado.
    """

    last_dividend_yield: Optional[float] = FieldInfo(alias="lastDividendYield", default=None)
    """Yield do último rendimento.

    Último rendimento sobre o último preço, em fração (0.008 = 0,8%). Unidade:
    fração (0.06 = 6%). Nulo quando não há dado.
    """

    market_cap: Optional[float] = FieldInfo(alias="marketCap", default=None)
    """Valor de mercado.

    Último preço vezes as cotas emitidas do último informe, em reais. Unidade:
    reais. Nulo quando não há dado.
    """

    nav_per_share: Optional[float] = FieldInfo(alias="navPerShare", default=None)
    """Valor patrimonial/cota.

    Valor patrimonial por cota do último informe, em reais. Unidade: reais. Nulo
    quando não há dado.
    """

    price_change12m: Optional[float] = FieldInfo(alias="priceChange12m", default=None)
    """Variação em 12 meses.

    Último preço sobre o fechamento de 12 meses atrás, em fração (0.05 = 5%). Não
    soma os rendimentos. Unidade: fração (0.06 = 6%). Nulo quando não há dado.
    """

    price_to_nav: Optional[float] = FieldInfo(alias="priceToNav", default=None)
    """P/VP.

    Último preço sobre o valor patrimonial por cota do último informe. Unidade:
    múltiplo. Nulo quando não há dado.
    """

    total_fee_percent: Optional[float] = FieldInfo(alias="totalFeePercent", default=None)
    """Taxa total.

    Taxa total ao ano do regulamento mais recente, em percentual (0.2 = 0,20% a.a.).
    Por enquanto, só ETFs. Unidade: porcentagem (2.81 = 2,81%). Nulo quando não há
    dado.
    """

    total_investors: Optional[float] = FieldInfo(alias="totalInvestors", default=None)
    """Cotistas.

    Número de cotistas do último informe. Unidade: quantidade. Nulo quando não há
    dado.
    """


class ResultQuote(BaseModel):
    change_percent: Optional[float] = FieldInfo(alias="changePercent", default=None)
    """Variação no dia, em porcentagem."""

    last_price: Optional[float] = FieldInfo(alias="lastPrice", default=None)
    """Último preço."""

    market_cap: Optional[float] = FieldInfo(alias="marketCap", default=None)
    """Valor de mercado, em reais. Pode ser nulo."""

    volume: Optional[float] = None
    """Volume negociado no dia."""


class Result(BaseModel):
    asset_type: Optional[Literal["stock", "fund", "bdr"]] = FieldInfo(alias="assetType", default=None)
    """Tipo do ativo."""

    currency: Literal["BRL"]
    """Moeda."""

    exchange: Literal["B3"]
    """Bolsa."""

    fund: ResultFund

    is_active: bool = FieldInfo(alias="isActive")
    """`true` quando o ativo está em negociação."""

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)
    """URL do logo."""

    long_name: Optional[str] = FieldInfo(alias="longName", default=None)
    """Nome longo. Pode ser nulo."""

    metrics: ResultMetrics
    """Indicadores do fundo."""

    name: str
    """Nome da empresa ou do fundo."""

    quote: ResultQuote

    sector: Optional[str] = None
    """Setor. Pode ser nulo."""

    subsector: Optional[str] = None
    """Subsetor. Pode ser nulo."""

    sub_type: Optional[Literal["stock", "unit", "fii", "etf", "fi-infra", "fi-agro", "fip", "fidc", "bdr"]] = FieldInfo(
        alias="subType", default=None
    )
    """Subtipo do ativo: stock, unit, fii, etf, fi-infra, fi-agro, fip, fidc ou bdr."""

    symbol: str
    """Ticker do ativo."""


class FundScreenerResponse(BaseModel):
    pagination: Pagination

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    results: List[Result]

    took: int
    """Tempo de processamento, em milissegundos."""
