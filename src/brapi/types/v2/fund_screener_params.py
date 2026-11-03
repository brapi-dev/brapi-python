# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FundScreenerParams"]


class FundScreenerParams(TypedDict, total=False):
    anbima_classification: Annotated[str, PropertyInfo(alias="anbimaClassification")]
    """Parte da classificação ANBIMA, sem diferença de maiúsculas e acentos.

    Exemplos: Previdência, Exterior, Crédito Livre. Só com `assetType=unlisted`.
    """

    asset_type: Annotated[
        Literal["fii", "fiagro", "fiinfra", "etf", "fidc", "fip", "fif", "unlisted"], PropertyInfo(alias="assetType")
    ]
    """Tipo do fundo listado: fii, fiagro, fiinfra, etf, fidc, fip ou fif.

    Sem ele, todos os fundos listados. `unlisted` troca para os fundos sem ticker na
    bolsa, por CNPJ.
    """

    average_daily_traded_value_max: Annotated[float, PropertyInfo(alias="averageDailyTradedValueMax")]
    """Liquidez diária: valor máximo, inclusive.

    Unidade: reais. Só para fundos listados.
    """

    average_daily_traded_value_min: Annotated[float, PropertyInfo(alias="averageDailyTradedValueMin")]
    """Liquidez diária: valor mínimo, inclusive.

    Unidade: reais. Só para fundos listados.
    """

    change_percent_max: Annotated[float, PropertyInfo(alias="changePercentMax")]
    """Variação no dia: valor máximo, inclusive.

    Unidade: porcentagem (2.81 = 2,81%). Só para fundos listados.
    """

    change_percent_min: Annotated[float, PropertyInfo(alias="changePercentMin")]
    """Variação no dia: valor mínimo, inclusive.

    Unidade: porcentagem (2.81 = 2,81%). Só para fundos listados.
    """

    classification: Literal["renda-fixa", "multimercado", "acoes", "cambial", "fmp-fgts"]
    """Classe do fundo na CVM: renda-fixa, multimercado, acoes, cambial ou fmp-fgts.

    Só com `assetType=unlisted`.
    """

    dividend_yield_max: Annotated[float, PropertyInfo(alias="dividendYieldMax")]
    """Dividend yield 12m: valor máximo, inclusive.

    Unidade: fração (0.06 = 6%). Só para fundos listados.
    """

    dividend_yield_min: Annotated[float, PropertyInfo(alias="dividendYieldMin")]
    """Dividend yield 12m: valor mínimo, inclusive.

    Unidade: fração (0.06 = 6%). Só para fundos listados.
    """

    equity_max: Annotated[float, PropertyInfo(alias="equityMax")]
    """Patrimônio líquido: valor máximo, inclusive. Unidade: reais."""

    equity_min: Annotated[float, PropertyInfo(alias="equityMin")]
    """Patrimônio líquido: valor mínimo, inclusive. Unidade: reais."""

    etf_category: Annotated[
        Literal["fixed-income", "equity", "crypto", "real-estate"], PropertyInfo(alias="etfCategory")
    ]
    """
    Categoria do ETF pela lista da bolsa: fixed-income, equity, crypto ou
    real-estate. Só para fundos listados.
    """

    income_months12m_max: Annotated[float, PropertyInfo(alias="incomeMonths12mMax")]
    """Meses com rendimento: valor máximo, inclusive.

    Unidade: quantidade. Só para fundos listados.
    """

    income_months12m_min: Annotated[float, PropertyInfo(alias="incomeMonths12mMin")]
    """Meses com rendimento: valor mínimo, inclusive.

    Unidade: quantidade. Só para fundos listados.
    """

    last_dividend_max: Annotated[float, PropertyInfo(alias="lastDividendMax")]
    """Último rendimento: valor máximo, inclusive.

    Unidade: reais. Só para fundos listados.
    """

    last_dividend_min: Annotated[float, PropertyInfo(alias="lastDividendMin")]
    """Último rendimento: valor mínimo, inclusive.

    Unidade: reais. Só para fundos listados.
    """

    last_dividend_yield_max: Annotated[float, PropertyInfo(alias="lastDividendYieldMax")]
    """Yield do último rendimento: valor máximo, inclusive.

    Unidade: fração (0.06 = 6%). Só para fundos listados.
    """

    last_dividend_yield_min: Annotated[float, PropertyInfo(alias="lastDividendYieldMin")]
    """Yield do último rendimento: valor mínimo, inclusive.

    Unidade: fração (0.06 = 6%). Só para fundos listados.
    """

    last_price_max: Annotated[float, PropertyInfo(alias="lastPriceMax")]
    """Preço: valor máximo, inclusive. Unidade: reais. Só para fundos listados."""

    last_price_min: Annotated[float, PropertyInfo(alias="lastPriceMin")]
    """Preço: valor mínimo, inclusive. Unidade: reais. Só para fundos listados."""

    limit: int
    """Itens por página. Máximo: 200."""

    manager: str
    """Parte do nome do gestor, sem diferença de maiúsculas e acentos.

    Só com `assetType=unlisted`.
    """

    market_cap_max: Annotated[float, PropertyInfo(alias="marketCapMax")]
    """Valor de mercado: valor máximo, inclusive.

    Unidade: reais. Só para fundos listados.
    """

    market_cap_min: Annotated[float, PropertyInfo(alias="marketCapMin")]
    """Valor de mercado: valor mínimo, inclusive.

    Unidade: reais. Só para fundos listados.
    """

    nav_per_share_max: Annotated[float, PropertyInfo(alias="navPerShareMax")]
    """Valor patrimonial/cota: valor máximo, inclusive. Unidade: reais."""

    nav_per_share_min: Annotated[float, PropertyInfo(alias="navPerShareMin")]
    """Valor patrimonial/cota: valor mínimo, inclusive. Unidade: reais."""

    net_flow1m_max: Annotated[float, PropertyInfo(alias="netFlow1mMax")]
    """Captação líquida em 1 mês: valor máximo, inclusive.

    Unidade: reais. Só com `assetType=unlisted`.
    """

    net_flow1m_min: Annotated[float, PropertyInfo(alias="netFlow1mMin")]
    """Captação líquida em 1 mês: valor mínimo, inclusive.

    Unidade: reais. Só com `assetType=unlisted`.
    """

    page: int
    """Número da página. Começa em 1."""

    price_change12m_max: Annotated[float, PropertyInfo(alias="priceChange12mMax")]
    """Variação em 12 meses: valor máximo, inclusive.

    Unidade: fração (0.06 = 6%). Só para fundos listados.
    """

    price_change12m_min: Annotated[float, PropertyInfo(alias="priceChange12mMin")]
    """Variação em 12 meses: valor mínimo, inclusive.

    Unidade: fração (0.06 = 6%). Só para fundos listados.
    """

    price_to_nav_max: Annotated[float, PropertyInfo(alias="priceToNavMax")]
    """P/VP: valor máximo, inclusive. Unidade: múltiplo. Só para fundos listados."""

    price_to_nav_min: Annotated[float, PropertyInfo(alias="priceToNavMin")]
    """P/VP: valor mínimo, inclusive. Unidade: múltiplo. Só para fundos listados."""

    return12m_max: Annotated[float, PropertyInfo(alias="return12mMax")]
    """Rentabilidade em 12 meses: valor máximo, inclusive.

    Unidade: fração (0.06 = 6%). Só com `assetType=unlisted`.
    """

    return12m_min: Annotated[float, PropertyInfo(alias="return12mMin")]
    """Rentabilidade em 12 meses: valor mínimo, inclusive.

    Unidade: fração (0.06 = 6%). Só com `assetType=unlisted`.
    """

    return1m_max: Annotated[float, PropertyInfo(alias="return1mMax")]
    """Rentabilidade em 1 mês: valor máximo, inclusive.

    Unidade: fração (0.06 = 6%). Só com `assetType=unlisted`.
    """

    return1m_min: Annotated[float, PropertyInfo(alias="return1mMin")]
    """Rentabilidade em 1 mês: valor mínimo, inclusive.

    Unidade: fração (0.06 = 6%). Só com `assetType=unlisted`.
    """

    return36m_max: Annotated[float, PropertyInfo(alias="return36mMax")]
    """Rentabilidade em 36 meses: valor máximo, inclusive.

    Unidade: fração (0.06 = 6%). Só com `assetType=unlisted`.
    """

    return36m_min: Annotated[float, PropertyInfo(alias="return36mMin")]
    """Rentabilidade em 36 meses: valor mínimo, inclusive.

    Unidade: fração (0.06 = 6%). Só com `assetType=unlisted`.
    """

    return_day_max: Annotated[float, PropertyInfo(alias="returnDayMax")]
    """Variação no dia: valor máximo, inclusive.

    Unidade: fração (0.06 = 6%). Só com `assetType=unlisted`.
    """

    return_day_min: Annotated[float, PropertyInfo(alias="returnDayMin")]
    """Variação no dia: valor mínimo, inclusive.

    Unidade: fração (0.06 = 6%). Só com `assetType=unlisted`.
    """

    return_ytd_max: Annotated[float, PropertyInfo(alias="returnYtdMax")]
    """Rentabilidade no ano: valor máximo, inclusive.

    Unidade: fração (0.06 = 6%). Só com `assetType=unlisted`.
    """

    return_ytd_min: Annotated[float, PropertyInfo(alias="returnYtdMin")]
    """Rentabilidade no ano: valor mínimo, inclusive.

    Unidade: fração (0.06 = 6%). Só com `assetType=unlisted`.
    """

    search: str
    """Parte do ticker ou do nome do fundo.

    Com `assetType=unlisted`, parte do nome ou da razão social; números, com ou sem
    pontuação, buscam o início do CNPJ.
    """

    segment: str
    """
    Segmento do FII no cadastro da CVM, como Logística, Shoppings, Escritórios ou
    Títulos e Val. Mob. Nome exato, sem diferença de maiúsculas. Só para fundos
    listados.
    """

    segment_type: Annotated[Literal["tijolo", "papel", "hibrido", "fof"], PropertyInfo(alias="segmentType")]
    """
    Tipo do FII pelo último informe: tijolo (imóveis), papel (CRI, LCI e títulos),
    fof (cotas de outros FIIs) ou hibrido. Só para fundos listados.
    """

    sort_by: Annotated[
        Literal[
            "symbol",
            "name",
            "lastPrice",
            "changePercent",
            "volume",
            "averageDailyTradedValue",
            "marketCap",
            "dividendYield",
            "lastDividend",
            "lastDividendYield",
            "incomeMonths12m",
            "navPerShare",
            "priceToNav",
            "equity",
            "totalInvestors",
            "priceChange12m",
            "totalFeePercent",
            "cnpj",
            "returnDay",
            "return1m",
            "returnYtd",
            "return12m",
            "return36m",
            "netFlow1m",
        ],
        PropertyInfo(alias="sortBy"),
    ]
    """
    Campo de ordenação: uma chave de métrica, `symbol` ou `name`; com
    `assetType=unlisted`, uma chave de indicador, `name` ou `cnpj`. Padrão:
    `averageDailyTradedValue`; com `assetType=unlisted`, `totalInvestors`. Valores
    nulos ficam no fim.
    """

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """Ordem. Padrão: `desc`."""

    total_fee_percent_max: Annotated[float, PropertyInfo(alias="totalFeePercentMax")]
    """Taxa total: valor máximo, inclusive.

    Unidade: porcentagem (2.81 = 2,81%). Só para fundos listados.
    """

    total_fee_percent_min: Annotated[float, PropertyInfo(alias="totalFeePercentMin")]
    """Taxa total: valor mínimo, inclusive.

    Unidade: porcentagem (2.81 = 2,81%). Só para fundos listados.
    """

    total_investors_max: Annotated[float, PropertyInfo(alias="totalInvestorsMax")]
    """Cotistas: valor máximo, inclusive. Unidade: quantidade."""

    total_investors_min: Annotated[float, PropertyInfo(alias="totalInvestorsMin")]
    """Cotistas: valor mínimo, inclusive. Unidade: quantidade."""

    volume_max: Annotated[float, PropertyInfo(alias="volumeMax")]
    """Volume: valor máximo, inclusive. Unidade: quantidade. Só para fundos listados."""

    volume_min: Annotated[float, PropertyInfo(alias="volumeMin")]
    """Volume: valor mínimo, inclusive. Unidade: quantidade. Só para fundos listados."""
