# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["StockScreenerResponse", "Pagination", "Result", "ResultMetrics", "ResultQuote"]


class Pagination(BaseModel):
    has_next_page: bool = FieldInfo(alias="hasNextPage")

    limit: float

    page: float

    total_items: float = FieldInfo(alias="totalItems")

    total_pages: float = FieldInfo(alias="totalPages")


class ResultMetrics(BaseModel):
    """Indicadores do ativo. As chaves do plano Pro não vêm no plano Startup."""

    book_value_per_share: Optional[float] = FieldInfo(alias="bookValuePerShare", default=None)
    """VPA.

    Valor patrimonial por ação, em reais. Unidade: reais. Nulo quando não há dado.
    """

    dividend_yield: Optional[float] = FieldInfo(alias="dividendYield", default=None)
    """Dividend yield.

    Proventos em dinheiro dos últimos 12 meses sobre o último preço, em fração (0.06
    = 6%). Nulo quando não houve proventos. Unidade: fração (0.06 = 6%). Nulo quando
    não há dado.
    """

    earnings_per_share: Optional[float] = FieldInfo(alias="earningsPerShare", default=None)
    """LPA.

    Lucro por ação dos últimos 12 meses, em reais. Unidade: reais. Nulo quando não
    há dado.
    """

    enterprise_to_ebitda: Optional[float] = FieldInfo(alias="enterpriseToEbitda", default=None)
    """EV/EBITDA.

    Valor da firma sobre EBITDA. Unidade: múltiplo. Nulo quando não há dado.
    """

    enterprise_to_revenue: Optional[float] = FieldInfo(alias="enterpriseToRevenue", default=None)
    """EV/Receita.

    Valor da firma sobre receita. Unidade: múltiplo. Nulo quando não há dado.
    """

    enterprise_value: Optional[float] = FieldInfo(alias="enterpriseValue", default=None)
    """Valor da firma.

    Valor de mercado mais dívida líquida, em reais. Unidade: reais. Nulo quando não
    há dado.
    """

    fifty_two_week_change: Optional[float] = FieldInfo(alias="fiftyTwoWeekChange", default=None)
    """Variação 52 semanas.

    Variação do preço em 52 semanas, em fração (0.65 = 65%). Unidade: fração (0.06 =
    6%). Nulo quando não há dado.
    """

    net_margin: Optional[float] = FieldInfo(alias="netMargin", default=None)
    """Margem líquida.

    Lucro líquido sobre receita, em fração (0.24 = 24%). Unidade: fração (0.06 =
    6%). Nulo quando não há dado.
    """

    peg_ratio: Optional[float] = FieldInfo(alias="pegRatio", default=None)
    """PEG.

    P/L dividido pelo crescimento do lucro. Unidade: múltiplo. Nulo quando não há
    dado.
    """

    price_to_book: Optional[float] = FieldInfo(alias="priceToBook", default=None)
    """P/VP.

    Preço sobre valor patrimonial. Unidade: múltiplo. Nulo quando não há dado.
    """

    trailing_pe: Optional[float] = FieldInfo(alias="trailingPE", default=None)
    """P/L.

    Preço sobre lucro dos últimos 12 meses. É negativo quando a empresa tem
    prejuízo. Unidade: múltiplo. Nulo quando não há dado.
    """

    current_ratio: Optional[float] = FieldInfo(alias="currentRatio", default=None)
    """Liquidez corrente.

    Ativo circulante sobre passivo circulante. Unidade: múltiplo. Nulo quando não há
    dado. Só vem no plano Pro.
    """

    debt_to_equity: Optional[float] = FieldInfo(alias="debtToEquity", default=None)
    """Dívida/PL.

    Dívida bruta sobre patrimônio líquido. Unidade: múltiplo. Nulo quando não há
    dado. Só vem no plano Pro.
    """

    earnings_growth: Optional[float] = FieldInfo(alias="earningsGrowth", default=None)
    """Crescimento do lucro.

    Crescimento do lucro do último trimestre contra o mesmo trimestre do ano
    anterior, em fração. Unidade: fração (0.06 = 6%). Nulo quando não há dado. Só
    vem no plano Pro.
    """

    earnings_growth_annual: Optional[float] = FieldInfo(alias="earningsGrowthAnnual", default=None)
    """Crescimento anual do lucro.

    Crescimento do lucro no último ano fiscal, em fração. Unidade: fração (0.06 =
    6%). Nulo quando não há dado. Só vem no plano Pro.
    """

    ebitda: Optional[float] = None
    """EBITDA.

    EBITDA dos últimos 12 meses, em reais. Unidade: reais. Nulo quando não há dado.
    Só vem no plano Pro.
    """

    ebitda_margin: Optional[float] = FieldInfo(alias="ebitdaMargin", default=None)
    """Margem EBITDA.

    EBITDA sobre receita, em fração. Unidade: fração (0.06 = 6%). Nulo quando não há
    dado. Só vem no plano Pro.
    """

    free_cashflow: Optional[float] = FieldInfo(alias="freeCashflow", default=None)
    """Fluxo de caixa livre.

    Fluxo de caixa livre, em reais. Unidade: reais. Nulo quando não há dado. Só vem
    no plano Pro.
    """

    gross_margin: Optional[float] = FieldInfo(alias="grossMargin", default=None)
    """Margem bruta.

    Lucro bruto sobre receita, em fração. Unidade: fração (0.06 = 6%). Nulo quando
    não há dado. Só vem no plano Pro.
    """

    net_debt_to_ebitda: Optional[float] = FieldInfo(alias="netDebtToEbitda", default=None)
    """Dívida líquida/EBITDA.

    Dívida bruta menos caixa, sobre EBITDA. Nulo quando o EBITDA é zero ou negativo.
    Unidade: múltiplo. Nulo quando não há dado. Só vem no plano Pro.
    """

    operating_margin: Optional[float] = FieldInfo(alias="operatingMargin", default=None)
    """Margem operacional.

    Lucro operacional sobre receita, em fração. Unidade: fração (0.06 = 6%). Nulo
    quando não há dado. Só vem no plano Pro.
    """

    quick_ratio: Optional[float] = FieldInfo(alias="quickRatio", default=None)
    """Liquidez seca.

    Ativo circulante sem estoques, sobre passivo circulante. Unidade: múltiplo. Nulo
    quando não há dado. Só vem no plano Pro.
    """

    return_on_assets: Optional[float] = FieldInfo(alias="returnOnAssets", default=None)
    """ROA.

    Retorno sobre os ativos, em fração. Unidade: fração (0.06 = 6%). Nulo quando não
    há dado. Só vem no plano Pro.
    """

    return_on_equity: Optional[float] = FieldInfo(alias="returnOnEquity", default=None)
    """ROE.

    Retorno sobre o patrimônio, em fração (0.15 = 15%). Unidade: fração (0.06 = 6%).
    Nulo quando não há dado. Só vem no plano Pro.
    """

    revenue_growth: Optional[float] = FieldInfo(alias="revenueGrowth", default=None)
    """Crescimento da receita.

    Crescimento da receita do último trimestre contra o mesmo trimestre do ano
    anterior, em fração. Unidade: fração (0.06 = 6%). Nulo quando não há dado. Só
    vem no plano Pro.
    """

    revenue_growth_annual: Optional[float] = FieldInfo(alias="revenueGrowthAnnual", default=None)
    """Crescimento anual da receita.

    Crescimento da receita no último ano fiscal, em fração. Unidade: fração (0.06 =
    6%). Nulo quando não há dado. Só vem no plano Pro.
    """

    total_cash: Optional[float] = FieldInfo(alias="totalCash", default=None)
    """Caixa.

    Caixa e aplicações, em reais. Unidade: reais. Nulo quando não há dado. Só vem no
    plano Pro.
    """

    total_debt: Optional[float] = FieldInfo(alias="totalDebt", default=None)
    """Dívida bruta.

    Dívida bruta, em reais. Unidade: reais. Nulo quando não há dado. Só vem no plano
    Pro.
    """

    total_revenue: Optional[float] = FieldInfo(alias="totalRevenue", default=None)
    """Receita.

    Receita dos últimos 12 meses, em reais. Unidade: reais. Nulo quando não há dado.
    Só vem no plano Pro.
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

    fundamentals_updated_at: Optional[datetime] = FieldInfo(alias="fundamentalsUpdatedAt", default=None)
    """Data e hora da última atualização dos fundamentos usados.

    Nulo quando o ativo não tem fundamentos.
    """

    is_active: bool = FieldInfo(alias="isActive")
    """`true` quando o ativo está em negociação."""

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)
    """URL do logo."""

    long_name: Optional[str] = FieldInfo(alias="longName", default=None)
    """Nome longo. Pode ser nulo."""

    metrics: ResultMetrics
    """Indicadores do ativo. As chaves do plano Pro não vêm no plano Startup."""

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


class StockScreenerResponse(BaseModel):
    pagination: Pagination

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    results: List[Result]

    took: int
    """Tempo de processamento, em milissegundos."""
