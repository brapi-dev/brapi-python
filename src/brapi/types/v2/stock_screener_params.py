# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["StockScreenerParams"]


class StockScreenerParams(TypedDict, total=False):
    book_value_per_share_max: Annotated[float, PropertyInfo(alias="bookValuePerShareMax")]
    """VPA: valor máximo, inclusive. Unidade: reais. Plano Startup e Pro."""

    book_value_per_share_min: Annotated[float, PropertyInfo(alias="bookValuePerShareMin")]
    """VPA: valor mínimo, inclusive. Unidade: reais. Plano Startup e Pro."""

    change_percent_max: Annotated[float, PropertyInfo(alias="changePercentMax")]
    """Variação no dia: valor máximo, inclusive.

    Unidade: porcentagem (2.81 = 2,81%). Plano Startup e Pro.
    """

    change_percent_min: Annotated[float, PropertyInfo(alias="changePercentMin")]
    """Variação no dia: valor mínimo, inclusive.

    Unidade: porcentagem (2.81 = 2,81%). Plano Startup e Pro.
    """

    current_ratio_max: Annotated[float, PropertyInfo(alias="currentRatioMax")]
    """Liquidez corrente: valor máximo, inclusive. Unidade: múltiplo. Plano Pro."""

    current_ratio_min: Annotated[float, PropertyInfo(alias="currentRatioMin")]
    """Liquidez corrente: valor mínimo, inclusive. Unidade: múltiplo. Plano Pro."""

    debt_to_equity_max: Annotated[float, PropertyInfo(alias="debtToEquityMax")]
    """Dívida/PL: valor máximo, inclusive. Unidade: múltiplo. Plano Pro."""

    debt_to_equity_min: Annotated[float, PropertyInfo(alias="debtToEquityMin")]
    """Dívida/PL: valor mínimo, inclusive. Unidade: múltiplo. Plano Pro."""

    dividend_yield_max: Annotated[float, PropertyInfo(alias="dividendYieldMax")]
    """Dividend yield: valor máximo, inclusive.

    Unidade: fração (0.06 = 6%). Plano Startup e Pro.
    """

    dividend_yield_min: Annotated[float, PropertyInfo(alias="dividendYieldMin")]
    """Dividend yield: valor mínimo, inclusive.

    Unidade: fração (0.06 = 6%). Plano Startup e Pro.
    """

    earnings_growth_annual_max: Annotated[float, PropertyInfo(alias="earningsGrowthAnnualMax")]
    """Crescimento anual do lucro: valor máximo, inclusive.

    Unidade: fração (0.06 = 6%). Plano Pro.
    """

    earnings_growth_annual_min: Annotated[float, PropertyInfo(alias="earningsGrowthAnnualMin")]
    """Crescimento anual do lucro: valor mínimo, inclusive.

    Unidade: fração (0.06 = 6%). Plano Pro.
    """

    earnings_growth_max: Annotated[float, PropertyInfo(alias="earningsGrowthMax")]
    """Crescimento do lucro: valor máximo, inclusive.

    Unidade: fração (0.06 = 6%). Plano Pro.
    """

    earnings_growth_min: Annotated[float, PropertyInfo(alias="earningsGrowthMin")]
    """Crescimento do lucro: valor mínimo, inclusive.

    Unidade: fração (0.06 = 6%). Plano Pro.
    """

    earnings_per_share_max: Annotated[float, PropertyInfo(alias="earningsPerShareMax")]
    """LPA: valor máximo, inclusive. Unidade: reais. Plano Startup e Pro."""

    earnings_per_share_min: Annotated[float, PropertyInfo(alias="earningsPerShareMin")]
    """LPA: valor mínimo, inclusive. Unidade: reais. Plano Startup e Pro."""

    ebitda_margin_max: Annotated[float, PropertyInfo(alias="ebitdaMarginMax")]
    """Margem EBITDA: valor máximo, inclusive. Unidade: fração (0.06 = 6%). Plano Pro."""

    ebitda_margin_min: Annotated[float, PropertyInfo(alias="ebitdaMarginMin")]
    """Margem EBITDA: valor mínimo, inclusive. Unidade: fração (0.06 = 6%). Plano Pro."""

    ebitda_max: Annotated[float, PropertyInfo(alias="ebitdaMax")]
    """EBITDA: valor máximo, inclusive. Unidade: reais. Plano Pro."""

    ebitda_min: Annotated[float, PropertyInfo(alias="ebitdaMin")]
    """EBITDA: valor mínimo, inclusive. Unidade: reais. Plano Pro."""

    enterprise_to_ebitda_max: Annotated[float, PropertyInfo(alias="enterpriseToEbitdaMax")]
    """EV/EBITDA: valor máximo, inclusive. Unidade: múltiplo. Plano Startup e Pro."""

    enterprise_to_ebitda_min: Annotated[float, PropertyInfo(alias="enterpriseToEbitdaMin")]
    """EV/EBITDA: valor mínimo, inclusive. Unidade: múltiplo. Plano Startup e Pro."""

    enterprise_to_revenue_max: Annotated[float, PropertyInfo(alias="enterpriseToRevenueMax")]
    """EV/Receita: valor máximo, inclusive. Unidade: múltiplo. Plano Startup e Pro."""

    enterprise_to_revenue_min: Annotated[float, PropertyInfo(alias="enterpriseToRevenueMin")]
    """EV/Receita: valor mínimo, inclusive. Unidade: múltiplo. Plano Startup e Pro."""

    enterprise_value_max: Annotated[float, PropertyInfo(alias="enterpriseValueMax")]
    """Valor da firma: valor máximo, inclusive. Unidade: reais. Plano Startup e Pro."""

    enterprise_value_min: Annotated[float, PropertyInfo(alias="enterpriseValueMin")]
    """Valor da firma: valor mínimo, inclusive. Unidade: reais. Plano Startup e Pro."""

    fifty_two_week_change_max: Annotated[float, PropertyInfo(alias="fiftyTwoWeekChangeMax")]
    """Variação 52 semanas: valor máximo, inclusive.

    Unidade: fração (0.06 = 6%). Plano Startup e Pro.
    """

    fifty_two_week_change_min: Annotated[float, PropertyInfo(alias="fiftyTwoWeekChangeMin")]
    """Variação 52 semanas: valor mínimo, inclusive.

    Unidade: fração (0.06 = 6%). Plano Startup e Pro.
    """

    free_cashflow_max: Annotated[float, PropertyInfo(alias="freeCashflowMax")]
    """Fluxo de caixa livre: valor máximo, inclusive. Unidade: reais. Plano Pro."""

    free_cashflow_min: Annotated[float, PropertyInfo(alias="freeCashflowMin")]
    """Fluxo de caixa livre: valor mínimo, inclusive. Unidade: reais. Plano Pro."""

    gross_margin_max: Annotated[float, PropertyInfo(alias="grossMarginMax")]
    """Margem bruta: valor máximo, inclusive. Unidade: fração (0.06 = 6%). Plano Pro."""

    gross_margin_min: Annotated[float, PropertyInfo(alias="grossMarginMin")]
    """Margem bruta: valor mínimo, inclusive. Unidade: fração (0.06 = 6%). Plano Pro."""

    last_price_max: Annotated[float, PropertyInfo(alias="lastPriceMax")]
    """Preço: valor máximo, inclusive. Unidade: reais. Plano Startup e Pro."""

    last_price_min: Annotated[float, PropertyInfo(alias="lastPriceMin")]
    """Preço: valor mínimo, inclusive. Unidade: reais. Plano Startup e Pro."""

    limit: int
    """Itens por página. Máximo: 200."""

    market_cap_max: Annotated[float, PropertyInfo(alias="marketCapMax")]
    """Valor de mercado: valor máximo, inclusive. Unidade: reais. Plano Startup e Pro."""

    market_cap_min: Annotated[float, PropertyInfo(alias="marketCapMin")]
    """Valor de mercado: valor mínimo, inclusive. Unidade: reais. Plano Startup e Pro."""

    net_debt_to_ebitda_max: Annotated[float, PropertyInfo(alias="netDebtToEbitdaMax")]
    """Dívida líquida/EBITDA: valor máximo, inclusive. Unidade: múltiplo. Plano Pro."""

    net_debt_to_ebitda_min: Annotated[float, PropertyInfo(alias="netDebtToEbitdaMin")]
    """Dívida líquida/EBITDA: valor mínimo, inclusive. Unidade: múltiplo. Plano Pro."""

    net_margin_max: Annotated[float, PropertyInfo(alias="netMarginMax")]
    """Margem líquida: valor máximo, inclusive.

    Unidade: fração (0.06 = 6%). Plano Startup e Pro.
    """

    net_margin_min: Annotated[float, PropertyInfo(alias="netMarginMin")]
    """Margem líquida: valor mínimo, inclusive.

    Unidade: fração (0.06 = 6%). Plano Startup e Pro.
    """

    operating_margin_max: Annotated[float, PropertyInfo(alias="operatingMarginMax")]
    """Margem operacional: valor máximo, inclusive.

    Unidade: fração (0.06 = 6%). Plano Pro.
    """

    operating_margin_min: Annotated[float, PropertyInfo(alias="operatingMarginMin")]
    """Margem operacional: valor mínimo, inclusive.

    Unidade: fração (0.06 = 6%). Plano Pro.
    """

    page: int
    """Número da página. Começa em 1."""

    peg_ratio_max: Annotated[float, PropertyInfo(alias="pegRatioMax")]
    """PEG: valor máximo, inclusive. Unidade: múltiplo. Plano Startup e Pro."""

    peg_ratio_min: Annotated[float, PropertyInfo(alias="pegRatioMin")]
    """PEG: valor mínimo, inclusive. Unidade: múltiplo. Plano Startup e Pro."""

    price_to_book_max: Annotated[float, PropertyInfo(alias="priceToBookMax")]
    """P/VP: valor máximo, inclusive. Unidade: múltiplo. Plano Startup e Pro."""

    price_to_book_min: Annotated[float, PropertyInfo(alias="priceToBookMin")]
    """P/VP: valor mínimo, inclusive. Unidade: múltiplo. Plano Startup e Pro."""

    quick_ratio_max: Annotated[float, PropertyInfo(alias="quickRatioMax")]
    """Liquidez seca: valor máximo, inclusive. Unidade: múltiplo. Plano Pro."""

    quick_ratio_min: Annotated[float, PropertyInfo(alias="quickRatioMin")]
    """Liquidez seca: valor mínimo, inclusive. Unidade: múltiplo. Plano Pro."""

    return_on_assets_max: Annotated[float, PropertyInfo(alias="returnOnAssetsMax")]
    """ROA: valor máximo, inclusive. Unidade: fração (0.06 = 6%). Plano Pro."""

    return_on_assets_min: Annotated[float, PropertyInfo(alias="returnOnAssetsMin")]
    """ROA: valor mínimo, inclusive. Unidade: fração (0.06 = 6%). Plano Pro."""

    return_on_equity_max: Annotated[float, PropertyInfo(alias="returnOnEquityMax")]
    """ROE: valor máximo, inclusive. Unidade: fração (0.06 = 6%). Plano Pro."""

    return_on_equity_min: Annotated[float, PropertyInfo(alias="returnOnEquityMin")]
    """ROE: valor mínimo, inclusive. Unidade: fração (0.06 = 6%). Plano Pro."""

    revenue_growth_annual_max: Annotated[float, PropertyInfo(alias="revenueGrowthAnnualMax")]
    """Crescimento anual da receita: valor máximo, inclusive.

    Unidade: fração (0.06 = 6%). Plano Pro.
    """

    revenue_growth_annual_min: Annotated[float, PropertyInfo(alias="revenueGrowthAnnualMin")]
    """Crescimento anual da receita: valor mínimo, inclusive.

    Unidade: fração (0.06 = 6%). Plano Pro.
    """

    revenue_growth_max: Annotated[float, PropertyInfo(alias="revenueGrowthMax")]
    """Crescimento da receita: valor máximo, inclusive.

    Unidade: fração (0.06 = 6%). Plano Pro.
    """

    revenue_growth_min: Annotated[float, PropertyInfo(alias="revenueGrowthMin")]
    """Crescimento da receita: valor mínimo, inclusive.

    Unidade: fração (0.06 = 6%). Plano Pro.
    """

    search: str
    """Parte do ticker, do nome da empresa ou de um ticker antigo."""

    sector: str
    """Setor. Aceita parte do nome."""

    sort_by: Annotated[
        Literal[
            "symbol",
            "name",
            "lastPrice",
            "changePercent",
            "volume",
            "marketCap",
            "trailingPE",
            "priceToBook",
            "enterpriseToEbitda",
            "enterpriseToRevenue",
            "pegRatio",
            "earningsPerShare",
            "bookValuePerShare",
            "netMargin",
            "enterpriseValue",
            "fiftyTwoWeekChange",
            "dividendYield",
            "returnOnEquity",
            "returnOnAssets",
            "grossMargin",
            "ebitdaMargin",
            "operatingMargin",
            "debtToEquity",
            "netDebtToEbitda",
            "currentRatio",
            "quickRatio",
            "revenueGrowth",
            "earningsGrowth",
            "revenueGrowthAnnual",
            "earningsGrowthAnnual",
            "totalRevenue",
            "ebitda",
            "freeCashflow",
            "totalDebt",
            "totalCash",
        ],
        PropertyInfo(alias="sortBy"),
    ]
    """Campo de ordenação: uma chave de métrica, `symbol` ou `name`.

    Valores nulos ficam no fim.
    """

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """Ordem. Padrão: `desc`."""

    subsector: str
    """Subsetor. Nome exato."""

    sub_type: Annotated[
        Literal["stock", "unit", "fii", "etf", "fi-infra", "fi-agro", "fip", "fidc", "bdr"],
        PropertyInfo(alias="subType"),
    ]
    """Subtipo do ativo: stock, unit, fii, etf, fi-infra, fi-agro, fip, fidc ou bdr."""

    total_cash_max: Annotated[float, PropertyInfo(alias="totalCashMax")]
    """Caixa: valor máximo, inclusive. Unidade: reais. Plano Pro."""

    total_cash_min: Annotated[float, PropertyInfo(alias="totalCashMin")]
    """Caixa: valor mínimo, inclusive. Unidade: reais. Plano Pro."""

    total_debt_max: Annotated[float, PropertyInfo(alias="totalDebtMax")]
    """Dívida bruta: valor máximo, inclusive. Unidade: reais. Plano Pro."""

    total_debt_min: Annotated[float, PropertyInfo(alias="totalDebtMin")]
    """Dívida bruta: valor mínimo, inclusive. Unidade: reais. Plano Pro."""

    total_revenue_max: Annotated[float, PropertyInfo(alias="totalRevenueMax")]
    """Receita: valor máximo, inclusive. Unidade: reais. Plano Pro."""

    total_revenue_min: Annotated[float, PropertyInfo(alias="totalRevenueMin")]
    """Receita: valor mínimo, inclusive. Unidade: reais. Plano Pro."""

    trailing_pe_max: Annotated[float, PropertyInfo(alias="trailingPEMax")]
    """P/L: valor máximo, inclusive. Unidade: múltiplo. Plano Startup e Pro."""

    trailing_pe_min: Annotated[float, PropertyInfo(alias="trailingPEMin")]
    """P/L: valor mínimo, inclusive. Unidade: múltiplo. Plano Startup e Pro."""

    type: Literal["stock", "fund", "bdr"]
    """Tipo do ativo. Padrão: `stock`."""

    volume_max: Annotated[float, PropertyInfo(alias="volumeMax")]
    """Volume: valor máximo, inclusive. Unidade: ações. Plano Startup e Pro."""

    volume_min: Annotated[float, PropertyInfo(alias="volumeMin")]
    """Volume: valor mínimo, inclusive. Unidade: ações. Plano Startup e Pro."""
