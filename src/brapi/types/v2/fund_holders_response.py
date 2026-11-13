# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "FundHoldersResponse",
    "Asset",
    "Fund",
    "FundChange",
    "FundPosition",
    "FundPath",
    "FundPathVia",
    "Pagination",
    "Summary",
    "TopBuyer",
    "TopBuyerChange",
    "TopBuyerPosition",
    "TopBuyerPath",
    "TopBuyerPathVia",
    "TopDirect",
    "TopDirectChange",
    "TopDirectPosition",
    "TopDirectPath",
    "TopDirectPathVia",
    "TopSeller",
    "TopSellerChange",
    "TopSellerPosition",
    "TopSellerPath",
    "TopSellerPathVia",
]


class Asset(BaseModel):
    cnpj: Optional[str] = None

    name: Optional[str] = None

    symbol: Optional[str] = None

    symbols: List[str]
    """Tickers buscados na bolsa."""

    type: Literal["fund", "company", "security"]
    """
    `fund` (cotas de um fundo e, se listado, o ticker dele), `company` (ações e
    dívida de uma empresa) ou `security` (um ticker).
    """


class FundChange(BaseModel):
    """Mudança contra o mês anterior com carteiras (`previousReferenceDate`).

    `null` sem mês anterior, ou quando um evento muda a quantidade de ações sem fator conhecido (incorporação, redução de capital, ou mudança de quantidade sem evento registrado).
    """

    change_value: Optional[float] = FieldInfo(alias="changeValue", default=None)
    """
    Valor estimado comprado (positivo) ou vendido (negativo) no mês, em reais: a
    diferença de quantidade vezes o preço do mês (valor dividido pela quantidade).
    Assim a alta ou a queda do preço não conta como compra ou venda. Uma posição
    nova soma o valor dela; uma posição zerada, o valor do mês anterior. Um título
    sem quantidade que o fundo tem nos dois meses soma 0. `null` para `unknown`.
    """

    previous_market_value: Optional[float] = FieldInfo(alias="previousMarketValue", default=None)
    """Valor da posição no mês anterior, em reais.

    0 para `new`. `null` para `unknown` sem carteira do mês anterior.
    """

    previous_quantity: Optional[float] = FieldInfo(alias="previousQuantity", default=None)
    """
    Quantidade no mês anterior, já ajustada por desdobramentos, grupamentos e
    bonificações. `null` como em `quantity`.
    """

    status: Literal["new", "increased", "decreased", "unchanged", "exited", "unknown"]
    """
    `new` (o fundo entregou a carteira do mês anterior sem o ativo), `increased`,
    `decreased`, `unchanged`, `exited` (tinha o ativo no mês anterior e entregou a
    carteira deste mês sem ele) ou `unknown` (sem carteira do mês anterior, ou com
    posições confidenciais da mesma classe do ativo em um dos dois meses). Uma linha
    com quantidade e valor zerados conta como sem posição.
    """


class FundPosition(BaseModel):
    asset_class: Literal[
        "equity",
        "bdr",
        "fund",
        "governmentBond",
        "repo",
        "privateCredit",
        "bankSecurity",
        "foreign",
        "derivative",
        "cash",
        "receivable",
        "payable",
        "commodity",
        "crypto",
        "other",
    ] = FieldInfo(alias="assetClass")
    """
    Classe do ativo: `equity` (ações), `bdr`, `fund` (cotas de fundos),
    `governmentBond` (títulos públicos), `repo` (compromissadas), `privateCredit`
    (crédito privado), `bankSecurity` (títulos de bancos), `foreign` (exterior),
    `derivative`, `cash` (caixa), `receivable` (valores a receber), `payable`
    (valores a pagar), `commodity` (ouro, prata), `crypto` (criptoativos) ou
    `other`.
    """

    market_value: float = FieldInfo(alias="marketValue")
    """Valor em reais."""

    quantity: Optional[float] = None
    """Quantidade.

    `null` para títulos sem código de uma empresa: podem ser mais de um.
    """

    symbol: Optional[str] = None
    """Ticker ou código do ativo. `null` para cotas de fundo e títulos sem código."""

    weight_percent: Optional[float] = FieldInfo(alias="weightPercent", default=None)
    """Peso no patrimônio do fundo, em %."""


class FundPathVia(BaseModel):
    id: str
    """
    CNPJ do fundo, `sec:<série>` de um fundo do exterior ou `bdr:<ticker>` de um BDR
    de ETF.
    """

    name: Optional[str] = None

    symbol: Optional[str] = None


class FundPath(BaseModel):
    value: float
    """Valor em reais."""

    via: List[FundPathVia]
    """Fundos no caminho, do primeiro ao que tem o ativo. Vazio para a posição direta."""

    weight_percent: Optional[float] = FieldInfo(alias="weightPercent", default=None)
    """Peso deste caminho no patrimônio do fundo, em %."""


class Fund(BaseModel):
    asset_type: Optional[Literal["fii", "fiagro", "fiinfra", "fif", "fidc", "fip", "etf", "other"]] = FieldInfo(
        alias="assetType", default=None
    )

    change: Optional[FundChange] = None
    """Mudança contra o mês anterior com carteiras (`previousReferenceDate`).

    `null` sem mês anterior, ou quando um evento muda a quantidade de ações sem
    fator conhecido (incorporação, redução de capital, ou mudança de quantidade sem
    evento registrado).
    """

    cnpj: str

    market_value: float = FieldInfo(alias="marketValue")
    """Valor da posição em reais, com ações emprestadas."""

    name: Optional[str] = None

    net_assets: Optional[float] = FieldInfo(alias="netAssets", default=None)
    """Patrimônio líquido do fundo, em reais."""

    positions: List[FundPosition]
    """Cada ativo que forma a posição, do maior valor ao menor.

    Mostra, por exemplo, quanto o fundo tem em cada ação e em cada debênture da
    empresa.
    """

    quantity: Optional[float] = None
    """Quantidade.

    Vendas a descoberto ficam negativas. `null` quando a posição junta mais de um
    ativo (classes da empresa, ou o BDR e a ação no exterior com
    `scope=indirect|all`), ou títulos sem código.
    """

    return12m_percent: Optional[float] = FieldInfo(alias="return12mPercent", default=None)
    """
    Variação do valor da cota do fundo nos 12 meses até `referenceDate`, em % (12.5
    = 12,5%), ajustada por desdobramentos da cota. Não soma os rendimentos
    distribuídos, então fica abaixo do retorno total de um fundo que distribui.
    `null` sem o valor da cota nas duas datas.
    """

    symbol: Optional[str] = None

    weight_percent: Optional[float] = FieldInfo(alias="weightPercent", default=None)
    """Peso do ativo no patrimônio do fundo, em %."""

    direct_value: Optional[float] = FieldInfo(alias="directValue", default=None)
    """
    Com `scope=indirect` ou `all`: valor da posição na própria carteira do fundo, em
    reais.
    """

    direct_weight_percent: Optional[float] = FieldInfo(alias="directWeightPercent", default=None)
    """
    Com `scope=indirect` ou `all`: peso da posição direta no patrimônio do fundo, em
    %.
    """

    indirect_value: Optional[float] = FieldInfo(alias="indirectValue", default=None)
    """
    Com `scope=indirect` ou `all`: valor que o fundo tem no ativo por meio de outros
    fundos, em reais: patrimônio do fundo × peso do caminho × peso do ativo no fundo
    que o tem.
    """

    paths: Optional[List[FundPath]] = None
    """Com `scope=indirect` ou `all`: os 3 caminhos de maior valor."""

    paths_count: Optional[int] = FieldInfo(alias="pathsCount", default=None)
    """
    Com `scope=indirect` ou `all`: quantos caminhos levam ao ativo, com a posição
    direta.
    """

    previous_indirect_value: Optional[float] = FieldInfo(alias="previousIndirectValue", default=None)
    """
    Com `scope=indirect` ou `all`: `indirectValue` no mês anterior
    (`previousReferenceDate`). Não indica compra nem venda: o valor muda quando um
    fundo no meio do caminho negocia. `null` sem dados do mês anterior.
    """

    value: Optional[float] = None
    """
    Com `scope=indirect` ou `all`: exposição do fundo ao ativo em reais, direta mais
    indireta. Igual a `marketValue`.
    """


class Pagination(BaseModel):
    has_next_page: bool = FieldInfo(alias="hasNextPage")

    limit: int

    page: int

    total_items: int = FieldInfo(alias="totalItems")

    total_pages: int = FieldInfo(alias="totalPages")


class Summary(BaseModel):
    buyers_count: Optional[int] = FieldInfo(alias="buyersCount", default=None)
    """Fundos que compraram no mês (`change.changeValue` positivo).

    `null` quando `change` é `null`.
    """

    change_value: Optional[float] = FieldInfo(alias="changeValue", default=None)
    """Saldo estimado do mês, em reais: compras menos vendas de todos os fundos.

    Fundos com `unknown` não entram.
    """

    funds_count: int = FieldInfo(alias="fundsCount")

    sellers_count: Optional[int] = FieldInfo(alias="sellersCount", default=None)
    """Fundos que venderam no mês, inclusive os que zeraram a posição.

    `null` quando `change` é `null`.
    """

    total_market_value: float = FieldInfo(alias="totalMarketValue")
    """Valor das posições diretas.

    Com `scope=indirect` ou `all`, inclui as linhas da mesma ação no exterior nas
    carteiras dos fundos locais (NVDA para NVDC34).
    """

    total_quantity: Optional[float] = FieldInfo(alias="totalQuantity", default=None)
    """Soma das quantidades.

    `null` quando a resposta junta mais de um ativo (classes da empresa, ou o BDR e
    a ação no exterior com `scope=indirect|all`), ou títulos sem código.
    """

    both_count: Optional[int] = FieldInfo(alias="bothCount", default=None)
    """Com `scope=indirect` ou `all`: fundos que têm o ativo das duas formas."""

    direct_only_count: Optional[int] = FieldInfo(alias="directOnlyCount", default=None)
    """Com `scope=indirect` ou `all`: fundos que têm o ativo só na própria carteira."""

    foreign_funds_value: Optional[float] = FieldInfo(alias="foreignFundsValue", default=None)
    """
    Com `scope=indirect` ou `all`: parte de `totalValue` que os fundos têm por meio
    de fundos do exterior e BDRs de ETF.
    """

    indirect_available: Optional[bool] = FieldInfo(alias="indirectAvailable", default=None)
    """
    Com `scope=indirect` ou `all`: `false` quando o mês não tem os caminhos entre
    fundos. Então só as posições diretas entram.
    """

    indirect_only_count: Optional[int] = FieldInfo(alias="indirectOnlyCount", default=None)
    """
    Com `scope=indirect` ou `all`: fundos que têm o ativo só por meio de outros
    fundos.
    """

    oldest_reference_date: Optional[str] = FieldInfo(alias="oldestReferenceDate", default=None)
    """Com `scope=indirect` ou `all`: data da carteira mais antiga usada.

    Os fundos do exterior publicam a carteira a cada trimestre, com atraso.
    """

    total_value: Optional[float] = FieldInfo(alias="totalValue", default=None)
    """
    Com `scope=indirect` ou `all`: valor total no ativo, com cada posição contada
    uma vez: as posições diretas (`totalMarketValue`) mais a parte dos fundos do
    exterior que os fundos têm (`foreignFundsValue`). A soma de `value` dos fundos é
    maior: a mesma posição aparece em cada fundo acima dela.
    """


class TopBuyerChange(BaseModel):
    """Mudança contra o mês anterior com carteiras (`previousReferenceDate`).

    `null` sem mês anterior, ou quando um evento muda a quantidade de ações sem fator conhecido (incorporação, redução de capital, ou mudança de quantidade sem evento registrado).
    """

    change_value: Optional[float] = FieldInfo(alias="changeValue", default=None)
    """
    Valor estimado comprado (positivo) ou vendido (negativo) no mês, em reais: a
    diferença de quantidade vezes o preço do mês (valor dividido pela quantidade).
    Assim a alta ou a queda do preço não conta como compra ou venda. Uma posição
    nova soma o valor dela; uma posição zerada, o valor do mês anterior. Um título
    sem quantidade que o fundo tem nos dois meses soma 0. `null` para `unknown`.
    """

    previous_market_value: Optional[float] = FieldInfo(alias="previousMarketValue", default=None)
    """Valor da posição no mês anterior, em reais.

    0 para `new`. `null` para `unknown` sem carteira do mês anterior.
    """

    previous_quantity: Optional[float] = FieldInfo(alias="previousQuantity", default=None)
    """
    Quantidade no mês anterior, já ajustada por desdobramentos, grupamentos e
    bonificações. `null` como em `quantity`.
    """

    status: Literal["new", "increased", "decreased", "unchanged", "exited", "unknown"]
    """
    `new` (o fundo entregou a carteira do mês anterior sem o ativo), `increased`,
    `decreased`, `unchanged`, `exited` (tinha o ativo no mês anterior e entregou a
    carteira deste mês sem ele) ou `unknown` (sem carteira do mês anterior, ou com
    posições confidenciais da mesma classe do ativo em um dos dois meses). Uma linha
    com quantidade e valor zerados conta como sem posição.
    """


class TopBuyerPosition(BaseModel):
    asset_class: Literal[
        "equity",
        "bdr",
        "fund",
        "governmentBond",
        "repo",
        "privateCredit",
        "bankSecurity",
        "foreign",
        "derivative",
        "cash",
        "receivable",
        "payable",
        "commodity",
        "crypto",
        "other",
    ] = FieldInfo(alias="assetClass")
    """
    Classe do ativo: `equity` (ações), `bdr`, `fund` (cotas de fundos),
    `governmentBond` (títulos públicos), `repo` (compromissadas), `privateCredit`
    (crédito privado), `bankSecurity` (títulos de bancos), `foreign` (exterior),
    `derivative`, `cash` (caixa), `receivable` (valores a receber), `payable`
    (valores a pagar), `commodity` (ouro, prata), `crypto` (criptoativos) ou
    `other`.
    """

    market_value: float = FieldInfo(alias="marketValue")
    """Valor em reais."""

    quantity: Optional[float] = None
    """Quantidade.

    `null` para títulos sem código de uma empresa: podem ser mais de um.
    """

    symbol: Optional[str] = None
    """Ticker ou código do ativo. `null` para cotas de fundo e títulos sem código."""

    weight_percent: Optional[float] = FieldInfo(alias="weightPercent", default=None)
    """Peso no patrimônio do fundo, em %."""


class TopBuyerPathVia(BaseModel):
    id: str
    """
    CNPJ do fundo, `sec:<série>` de um fundo do exterior ou `bdr:<ticker>` de um BDR
    de ETF.
    """

    name: Optional[str] = None

    symbol: Optional[str] = None


class TopBuyerPath(BaseModel):
    value: float
    """Valor em reais."""

    via: List[TopBuyerPathVia]
    """Fundos no caminho, do primeiro ao que tem o ativo. Vazio para a posição direta."""

    weight_percent: Optional[float] = FieldInfo(alias="weightPercent", default=None)
    """Peso deste caminho no patrimônio do fundo, em %."""


class TopBuyer(BaseModel):
    asset_type: Optional[Literal["fii", "fiagro", "fiinfra", "fif", "fidc", "fip", "etf", "other"]] = FieldInfo(
        alias="assetType", default=None
    )

    change: Optional[TopBuyerChange] = None
    """Mudança contra o mês anterior com carteiras (`previousReferenceDate`).

    `null` sem mês anterior, ou quando um evento muda a quantidade de ações sem
    fator conhecido (incorporação, redução de capital, ou mudança de quantidade sem
    evento registrado).
    """

    cnpj: str

    market_value: float = FieldInfo(alias="marketValue")
    """Valor da posição em reais, com ações emprestadas."""

    name: Optional[str] = None

    net_assets: Optional[float] = FieldInfo(alias="netAssets", default=None)
    """Patrimônio líquido do fundo, em reais."""

    positions: List[TopBuyerPosition]
    """Cada ativo que forma a posição, do maior valor ao menor.

    Mostra, por exemplo, quanto o fundo tem em cada ação e em cada debênture da
    empresa.
    """

    quantity: Optional[float] = None
    """Quantidade.

    Vendas a descoberto ficam negativas. `null` quando a posição junta mais de um
    ativo (classes da empresa, ou o BDR e a ação no exterior com
    `scope=indirect|all`), ou títulos sem código.
    """

    return12m_percent: Optional[float] = FieldInfo(alias="return12mPercent", default=None)
    """
    Variação do valor da cota do fundo nos 12 meses até `referenceDate`, em % (12.5
    = 12,5%), ajustada por desdobramentos da cota. Não soma os rendimentos
    distribuídos, então fica abaixo do retorno total de um fundo que distribui.
    `null` sem o valor da cota nas duas datas.
    """

    symbol: Optional[str] = None

    weight_percent: Optional[float] = FieldInfo(alias="weightPercent", default=None)
    """Peso do ativo no patrimônio do fundo, em %."""

    direct_value: Optional[float] = FieldInfo(alias="directValue", default=None)
    """
    Com `scope=indirect` ou `all`: valor da posição na própria carteira do fundo, em
    reais.
    """

    direct_weight_percent: Optional[float] = FieldInfo(alias="directWeightPercent", default=None)
    """
    Com `scope=indirect` ou `all`: peso da posição direta no patrimônio do fundo, em
    %.
    """

    indirect_value: Optional[float] = FieldInfo(alias="indirectValue", default=None)
    """
    Com `scope=indirect` ou `all`: valor que o fundo tem no ativo por meio de outros
    fundos, em reais: patrimônio do fundo × peso do caminho × peso do ativo no fundo
    que o tem.
    """

    paths: Optional[List[TopBuyerPath]] = None
    """Com `scope=indirect` ou `all`: os 3 caminhos de maior valor."""

    paths_count: Optional[int] = FieldInfo(alias="pathsCount", default=None)
    """
    Com `scope=indirect` ou `all`: quantos caminhos levam ao ativo, com a posição
    direta.
    """

    previous_indirect_value: Optional[float] = FieldInfo(alias="previousIndirectValue", default=None)
    """
    Com `scope=indirect` ou `all`: `indirectValue` no mês anterior
    (`previousReferenceDate`). Não indica compra nem venda: o valor muda quando um
    fundo no meio do caminho negocia. `null` sem dados do mês anterior.
    """

    value: Optional[float] = None
    """
    Com `scope=indirect` ou `all`: exposição do fundo ao ativo em reais, direta mais
    indireta. Igual a `marketValue`.
    """


class TopDirectChange(BaseModel):
    """Mudança contra o mês anterior com carteiras (`previousReferenceDate`).

    `null` sem mês anterior, ou quando um evento muda a quantidade de ações sem fator conhecido (incorporação, redução de capital, ou mudança de quantidade sem evento registrado).
    """

    change_value: Optional[float] = FieldInfo(alias="changeValue", default=None)
    """
    Valor estimado comprado (positivo) ou vendido (negativo) no mês, em reais: a
    diferença de quantidade vezes o preço do mês (valor dividido pela quantidade).
    Assim a alta ou a queda do preço não conta como compra ou venda. Uma posição
    nova soma o valor dela; uma posição zerada, o valor do mês anterior. Um título
    sem quantidade que o fundo tem nos dois meses soma 0. `null` para `unknown`.
    """

    previous_market_value: Optional[float] = FieldInfo(alias="previousMarketValue", default=None)
    """Valor da posição no mês anterior, em reais.

    0 para `new`. `null` para `unknown` sem carteira do mês anterior.
    """

    previous_quantity: Optional[float] = FieldInfo(alias="previousQuantity", default=None)
    """
    Quantidade no mês anterior, já ajustada por desdobramentos, grupamentos e
    bonificações. `null` como em `quantity`.
    """

    status: Literal["new", "increased", "decreased", "unchanged", "exited", "unknown"]
    """
    `new` (o fundo entregou a carteira do mês anterior sem o ativo), `increased`,
    `decreased`, `unchanged`, `exited` (tinha o ativo no mês anterior e entregou a
    carteira deste mês sem ele) ou `unknown` (sem carteira do mês anterior, ou com
    posições confidenciais da mesma classe do ativo em um dos dois meses). Uma linha
    com quantidade e valor zerados conta como sem posição.
    """


class TopDirectPosition(BaseModel):
    asset_class: Literal[
        "equity",
        "bdr",
        "fund",
        "governmentBond",
        "repo",
        "privateCredit",
        "bankSecurity",
        "foreign",
        "derivative",
        "cash",
        "receivable",
        "payable",
        "commodity",
        "crypto",
        "other",
    ] = FieldInfo(alias="assetClass")
    """
    Classe do ativo: `equity` (ações), `bdr`, `fund` (cotas de fundos),
    `governmentBond` (títulos públicos), `repo` (compromissadas), `privateCredit`
    (crédito privado), `bankSecurity` (títulos de bancos), `foreign` (exterior),
    `derivative`, `cash` (caixa), `receivable` (valores a receber), `payable`
    (valores a pagar), `commodity` (ouro, prata), `crypto` (criptoativos) ou
    `other`.
    """

    market_value: float = FieldInfo(alias="marketValue")
    """Valor em reais."""

    quantity: Optional[float] = None
    """Quantidade.

    `null` para títulos sem código de uma empresa: podem ser mais de um.
    """

    symbol: Optional[str] = None
    """Ticker ou código do ativo. `null` para cotas de fundo e títulos sem código."""

    weight_percent: Optional[float] = FieldInfo(alias="weightPercent", default=None)
    """Peso no patrimônio do fundo, em %."""


class TopDirectPathVia(BaseModel):
    id: str
    """
    CNPJ do fundo, `sec:<série>` de um fundo do exterior ou `bdr:<ticker>` de um BDR
    de ETF.
    """

    name: Optional[str] = None

    symbol: Optional[str] = None


class TopDirectPath(BaseModel):
    value: float
    """Valor em reais."""

    via: List[TopDirectPathVia]
    """Fundos no caminho, do primeiro ao que tem o ativo. Vazio para a posição direta."""

    weight_percent: Optional[float] = FieldInfo(alias="weightPercent", default=None)
    """Peso deste caminho no patrimônio do fundo, em %."""


class TopDirect(BaseModel):
    asset_type: Optional[Literal["fii", "fiagro", "fiinfra", "fif", "fidc", "fip", "etf", "other"]] = FieldInfo(
        alias="assetType", default=None
    )

    change: Optional[TopDirectChange] = None
    """Mudança contra o mês anterior com carteiras (`previousReferenceDate`).

    `null` sem mês anterior, ou quando um evento muda a quantidade de ações sem
    fator conhecido (incorporação, redução de capital, ou mudança de quantidade sem
    evento registrado).
    """

    cnpj: str

    market_value: float = FieldInfo(alias="marketValue")
    """Valor da posição em reais, com ações emprestadas."""

    name: Optional[str] = None

    net_assets: Optional[float] = FieldInfo(alias="netAssets", default=None)
    """Patrimônio líquido do fundo, em reais."""

    positions: List[TopDirectPosition]
    """Cada ativo que forma a posição, do maior valor ao menor.

    Mostra, por exemplo, quanto o fundo tem em cada ação e em cada debênture da
    empresa.
    """

    quantity: Optional[float] = None
    """Quantidade.

    Vendas a descoberto ficam negativas. `null` quando a posição junta mais de um
    ativo (classes da empresa, ou o BDR e a ação no exterior com
    `scope=indirect|all`), ou títulos sem código.
    """

    return12m_percent: Optional[float] = FieldInfo(alias="return12mPercent", default=None)
    """
    Variação do valor da cota do fundo nos 12 meses até `referenceDate`, em % (12.5
    = 12,5%), ajustada por desdobramentos da cota. Não soma os rendimentos
    distribuídos, então fica abaixo do retorno total de um fundo que distribui.
    `null` sem o valor da cota nas duas datas.
    """

    symbol: Optional[str] = None

    weight_percent: Optional[float] = FieldInfo(alias="weightPercent", default=None)
    """Peso do ativo no patrimônio do fundo, em %."""

    direct_value: Optional[float] = FieldInfo(alias="directValue", default=None)
    """
    Com `scope=indirect` ou `all`: valor da posição na própria carteira do fundo, em
    reais.
    """

    direct_weight_percent: Optional[float] = FieldInfo(alias="directWeightPercent", default=None)
    """
    Com `scope=indirect` ou `all`: peso da posição direta no patrimônio do fundo, em
    %.
    """

    indirect_value: Optional[float] = FieldInfo(alias="indirectValue", default=None)
    """
    Com `scope=indirect` ou `all`: valor que o fundo tem no ativo por meio de outros
    fundos, em reais: patrimônio do fundo × peso do caminho × peso do ativo no fundo
    que o tem.
    """

    paths: Optional[List[TopDirectPath]] = None
    """Com `scope=indirect` ou `all`: os 3 caminhos de maior valor."""

    paths_count: Optional[int] = FieldInfo(alias="pathsCount", default=None)
    """
    Com `scope=indirect` ou `all`: quantos caminhos levam ao ativo, com a posição
    direta.
    """

    previous_indirect_value: Optional[float] = FieldInfo(alias="previousIndirectValue", default=None)
    """
    Com `scope=indirect` ou `all`: `indirectValue` no mês anterior
    (`previousReferenceDate`). Não indica compra nem venda: o valor muda quando um
    fundo no meio do caminho negocia. `null` sem dados do mês anterior.
    """

    value: Optional[float] = None
    """
    Com `scope=indirect` ou `all`: exposição do fundo ao ativo em reais, direta mais
    indireta. Igual a `marketValue`.
    """


class TopSellerChange(BaseModel):
    """Mudança contra o mês anterior com carteiras (`previousReferenceDate`).

    `null` sem mês anterior, ou quando um evento muda a quantidade de ações sem fator conhecido (incorporação, redução de capital, ou mudança de quantidade sem evento registrado).
    """

    change_value: Optional[float] = FieldInfo(alias="changeValue", default=None)
    """
    Valor estimado comprado (positivo) ou vendido (negativo) no mês, em reais: a
    diferença de quantidade vezes o preço do mês (valor dividido pela quantidade).
    Assim a alta ou a queda do preço não conta como compra ou venda. Uma posição
    nova soma o valor dela; uma posição zerada, o valor do mês anterior. Um título
    sem quantidade que o fundo tem nos dois meses soma 0. `null` para `unknown`.
    """

    previous_market_value: Optional[float] = FieldInfo(alias="previousMarketValue", default=None)
    """Valor da posição no mês anterior, em reais.

    0 para `new`. `null` para `unknown` sem carteira do mês anterior.
    """

    previous_quantity: Optional[float] = FieldInfo(alias="previousQuantity", default=None)
    """
    Quantidade no mês anterior, já ajustada por desdobramentos, grupamentos e
    bonificações. `null` como em `quantity`.
    """

    status: Literal["new", "increased", "decreased", "unchanged", "exited", "unknown"]
    """
    `new` (o fundo entregou a carteira do mês anterior sem o ativo), `increased`,
    `decreased`, `unchanged`, `exited` (tinha o ativo no mês anterior e entregou a
    carteira deste mês sem ele) ou `unknown` (sem carteira do mês anterior, ou com
    posições confidenciais da mesma classe do ativo em um dos dois meses). Uma linha
    com quantidade e valor zerados conta como sem posição.
    """


class TopSellerPosition(BaseModel):
    asset_class: Literal[
        "equity",
        "bdr",
        "fund",
        "governmentBond",
        "repo",
        "privateCredit",
        "bankSecurity",
        "foreign",
        "derivative",
        "cash",
        "receivable",
        "payable",
        "commodity",
        "crypto",
        "other",
    ] = FieldInfo(alias="assetClass")
    """
    Classe do ativo: `equity` (ações), `bdr`, `fund` (cotas de fundos),
    `governmentBond` (títulos públicos), `repo` (compromissadas), `privateCredit`
    (crédito privado), `bankSecurity` (títulos de bancos), `foreign` (exterior),
    `derivative`, `cash` (caixa), `receivable` (valores a receber), `payable`
    (valores a pagar), `commodity` (ouro, prata), `crypto` (criptoativos) ou
    `other`.
    """

    market_value: float = FieldInfo(alias="marketValue")
    """Valor em reais."""

    quantity: Optional[float] = None
    """Quantidade.

    `null` para títulos sem código de uma empresa: podem ser mais de um.
    """

    symbol: Optional[str] = None
    """Ticker ou código do ativo. `null` para cotas de fundo e títulos sem código."""

    weight_percent: Optional[float] = FieldInfo(alias="weightPercent", default=None)
    """Peso no patrimônio do fundo, em %."""


class TopSellerPathVia(BaseModel):
    id: str
    """
    CNPJ do fundo, `sec:<série>` de um fundo do exterior ou `bdr:<ticker>` de um BDR
    de ETF.
    """

    name: Optional[str] = None

    symbol: Optional[str] = None


class TopSellerPath(BaseModel):
    value: float
    """Valor em reais."""

    via: List[TopSellerPathVia]
    """Fundos no caminho, do primeiro ao que tem o ativo. Vazio para a posição direta."""

    weight_percent: Optional[float] = FieldInfo(alias="weightPercent", default=None)
    """Peso deste caminho no patrimônio do fundo, em %."""


class TopSeller(BaseModel):
    asset_type: Optional[Literal["fii", "fiagro", "fiinfra", "fif", "fidc", "fip", "etf", "other"]] = FieldInfo(
        alias="assetType", default=None
    )

    change: Optional[TopSellerChange] = None
    """Mudança contra o mês anterior com carteiras (`previousReferenceDate`).

    `null` sem mês anterior, ou quando um evento muda a quantidade de ações sem
    fator conhecido (incorporação, redução de capital, ou mudança de quantidade sem
    evento registrado).
    """

    cnpj: str

    market_value: float = FieldInfo(alias="marketValue")
    """Valor da posição em reais, com ações emprestadas."""

    name: Optional[str] = None

    net_assets: Optional[float] = FieldInfo(alias="netAssets", default=None)
    """Patrimônio líquido do fundo, em reais."""

    positions: List[TopSellerPosition]
    """Cada ativo que forma a posição, do maior valor ao menor.

    Mostra, por exemplo, quanto o fundo tem em cada ação e em cada debênture da
    empresa.
    """

    quantity: Optional[float] = None
    """Quantidade.

    Vendas a descoberto ficam negativas. `null` quando a posição junta mais de um
    ativo (classes da empresa, ou o BDR e a ação no exterior com
    `scope=indirect|all`), ou títulos sem código.
    """

    return12m_percent: Optional[float] = FieldInfo(alias="return12mPercent", default=None)
    """
    Variação do valor da cota do fundo nos 12 meses até `referenceDate`, em % (12.5
    = 12,5%), ajustada por desdobramentos da cota. Não soma os rendimentos
    distribuídos, então fica abaixo do retorno total de um fundo que distribui.
    `null` sem o valor da cota nas duas datas.
    """

    symbol: Optional[str] = None

    weight_percent: Optional[float] = FieldInfo(alias="weightPercent", default=None)
    """Peso do ativo no patrimônio do fundo, em %."""

    direct_value: Optional[float] = FieldInfo(alias="directValue", default=None)
    """
    Com `scope=indirect` ou `all`: valor da posição na própria carteira do fundo, em
    reais.
    """

    direct_weight_percent: Optional[float] = FieldInfo(alias="directWeightPercent", default=None)
    """
    Com `scope=indirect` ou `all`: peso da posição direta no patrimônio do fundo, em
    %.
    """

    indirect_value: Optional[float] = FieldInfo(alias="indirectValue", default=None)
    """
    Com `scope=indirect` ou `all`: valor que o fundo tem no ativo por meio de outros
    fundos, em reais: patrimônio do fundo × peso do caminho × peso do ativo no fundo
    que o tem.
    """

    paths: Optional[List[TopSellerPath]] = None
    """Com `scope=indirect` ou `all`: os 3 caminhos de maior valor."""

    paths_count: Optional[int] = FieldInfo(alias="pathsCount", default=None)
    """
    Com `scope=indirect` ou `all`: quantos caminhos levam ao ativo, com a posição
    direta.
    """

    previous_indirect_value: Optional[float] = FieldInfo(alias="previousIndirectValue", default=None)
    """
    Com `scope=indirect` ou `all`: `indirectValue` no mês anterior
    (`previousReferenceDate`). Não indica compra nem venda: o valor muda quando um
    fundo no meio do caminho negocia. `null` sem dados do mês anterior.
    """

    value: Optional[float] = None
    """
    Com `scope=indirect` ou `all`: exposição do fundo ao ativo em reais, direta mais
    indireta. Igual a `marketValue`.
    """


class FundHoldersResponse(BaseModel):
    asset: Asset

    funds: List[Fund]

    pagination: Pagination

    previous_reference_date: Optional[str] = FieldInfo(alias="previousReferenceDate", default=None)
    """Mês anterior com carteiras, base de `change` e dos totais de compra e venda.

    `null` quando `change` é `null`.
    """

    reference_date: Optional[str] = FieldInfo(alias="referenceDate", default=None)

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    summary: Summary

    took: int
    """Tempo de processamento, em milissegundos."""

    scope: Optional[Literal["direct", "indirect", "all"]] = None
    """Com `scope=indirect` ou `all`: o escopo pedido."""

    top_buyers: Optional[List[TopBuyer]] = FieldInfo(alias="topBuyers", default=None)
    """
    Com `include=movers`: os fundos que mais compraram no mês, como em
    `sortBy=bought`, até `limit`. Vazio quando `change` é `null`.
    """

    top_direct: Optional[List[TopDirect]] = FieldInfo(alias="topDirect", default=None)
    """
    Com `include=direct` e `scope=indirect` ou `all`: os fundos com as maiores
    posições diretas, por `directValue`, até `limit`.
    """

    top_sellers: Optional[List[TopSeller]] = FieldInfo(alias="topSellers", default=None)
    """
    Com `include=movers`: os fundos que mais venderam no mês, como em `sortBy=sold`,
    até `limit`. Vazio quando `change` é `null`.
    """
