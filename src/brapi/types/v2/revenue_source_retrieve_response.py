# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "RevenueSourceRetrieveResponse",
    "Result",
    "ResultLookThrough",
    "ResultLookThroughActivity",
    "ResultLookThroughActivityHolding",
    "ResultYear",
    "ResultYearActivity",
    "ResultYearSegment",
    "ResultYearSegmentSource",
    "ResultYearTotalCheck",
    "ResultQuarter",
    "ResultQuarterSegment",
    "ResultQuarterSegmentSource",
    "ResultQuarterTotalCheck",
]


class ResultLookThroughActivityHolding(BaseModel):
    fiscal_year: int = FieldInfo(alias="fiscalYear")
    """Exercício das receitas usadas para esta posição."""

    issuer_code: str = FieldInfo(alias="issuerCode")

    portfolio_weight: float = FieldInfo(alias="portfolioWeight")
    """Peso da posição na carteira, em fração (0.06 = 6%)."""

    symbol: str

    weight: float
    """Peso da atividade que vem desta posição, em fração da carteira."""


class ResultLookThroughActivity(BaseModel):
    activity: str

    activity_label: str = FieldInfo(alias="activityLabel")

    holdings: List[ResultLookThroughActivityHolding]
    """Até 5 posições que mais pesam na atividade."""

    weight: float
    """Exposição da carteira à atividade, em fração (0.06 = 6%)."""


class ResultLookThrough(BaseModel):
    """
    Só para fundos com carteira mensal na CVM: exposição da carteira às atividades das empresas, FIIs e BDRs que o fundo tem. `null` para ETFs.
    """

    activities: List[ResultLookThroughActivity]
    """Atividades da maior para a menor."""

    coverage: float
    """Parte da carteira com fontes de receita, em fração (0.06 = 6%).

    A soma de `weight` das atividades é igual a `coverage`.
    """

    covered_value: float = FieldInfo(alias="coveredValue")
    """Valor das posições com fontes de receita, em reais."""

    portfolio_value: float = FieldInfo(alias="portfolioValue")
    """Valor das posições da carteira, em reais."""

    reference_date: str = FieldInfo(alias="referenceDate")
    """Data da carteira usada."""


class ResultYearActivity(BaseModel):
    activity: str

    activity_label: str = FieldInfo(alias="activityLabel")

    growth: Optional[float] = None
    """Crescimento da atividade, em fração.

    null quando falta o valor anterior de algum segmento.
    """

    segments: int
    """Número de segmentos somados."""

    share: float
    """Parte da soma de todos os segmentos, em fração (0.06 = 6%)."""

    value: float
    """Soma dos segmentos desta atividade."""


class ResultYearSegmentSource(BaseModel):
    document_id: str = FieldInfo(alias="documentId")
    """Protocolo ou número do documento na origem."""

    form: str
    """
    Documento de origem: `dfp` (demonstrações anuais na CVM), `itr` (demonstrações
    trimestrais na CVM), `10-K`, `20-F` ou `40-F` (relatório anual na SEC) ou
    `fii-quarterly` (informes trimestrais de FIIs na CVM).
    """

    page: Optional[int] = None
    """Página do valor no documento, quando conhecida."""

    prior_page: Optional[int] = FieldInfo(alias="priorPage", default=None)
    """Página do valor do ano anterior, quando conhecida."""

    url: Optional[str] = None
    """Link do documento."""


class ResultYearSegment(BaseModel):
    activity: str
    """Código da atividade do segmento."""

    activity_label: str = FieldInfo(alias="activityLabel")

    axis: str
    """
    Tipo de divisão: `business` (segmento de negócio), `product` (linha de produto
    ou serviço), `whole` (empresa sem segmentos: receita líquida total) ou
    `fii-income` (receitas de FIIs e Fiagros).
    """

    currency: str

    flags: List[str]
    """Alertas sobre o valor.

    `unchecked`: a soma dos segmentos não confere com a receita total. `relabeled`:
    uma conferência moveu o valor para outro segmento. `reviewed`: uma pessoa
    conferiu o segmento. `label-disputed`: duas leituras deram nomes diferentes ao
    segmento. `reviewed-by-model`: duas leituras discordaram e uma terceira leitura
    automática confirmou o segmento. `duplicate`: a mesma receita aparece em uma
    controlada listada. `includes-construction`: o valor inclui receita de
    construção. `gross`: o valor é receita bruta, antes de impostos e devoluções.
    """

    growth: Optional[float] = None
    """Crescimento sobre o ano anterior, em fração (0.06 = 6%)."""

    growth_ex_construction: Optional[float] = FieldInfo(alias="growthExConstruction", default=None)
    """Crescimento sem a receita de construção, em fração (0.06 = 6%)."""

    member: str
    """Nome do segmento como a empresa publica."""

    prior_ex_construction: Optional[float] = FieldInfo(alias="priorExConstruction", default=None)
    """Receita do ano anterior sem a receita de construção."""

    prior_from: Optional[Literal["same-filing", "previous-filing"]] = FieldInfo(alias="priorFrom", default=None)
    """`same-filing` quando o valor anterior vem do mesmo documento.

    `previous-filing` quando vem do documento do ano anterior.
    """

    prior_value: Optional[float] = FieldInfo(alias="priorValue", default=None)
    """Receita do exercício anterior."""

    scope: Literal["exact", "mixed"]
    """`exact` quando o segmento tem só esta atividade.

    `mixed` quando ele junta atividades e esta é a principal.
    """

    source: ResultYearSegmentSource

    value: float
    """Receita do exercício, na moeda `currency`."""

    value_ex_construction: Optional[float] = FieldInfo(alias="valueExConstruction", default=None)
    """
    Receita sem a receita de construção de concessões, quando a atividade tem essa
    receita.
    """


class ResultYearTotalCheck(BaseModel):
    """Conferência dos segmentos com a receita total."""

    diff: Optional[float] = None
    """Diferença entre `sum` e `total`, ou `grossTotal` quando existe."""

    sum: float
    """Soma dos segmentos lidos, com as eliminações entre segmentos."""

    total: Optional[float] = None
    """Receita total publicada."""

    verified: bool
    """true quando a soma confere com a receita total, ou com `grossTotal`."""

    gross_total: Optional[float] = FieldInfo(alias="grossTotal", default=None)
    """Receita bruta publicada, quando os segmentos são de receita bruta."""


class ResultYear(BaseModel):
    activities: List[ResultYearActivity]
    """Soma por atividade, da maior para a menor."""

    currency: str

    fiscal_year: int = FieldInfo(alias="fiscalYear")
    """Exercício social.

    Empresas com exercício fora do ano civil usam o ano em que o exercício termina.
    """

    period_end: str = FieldInfo(alias="periodEnd")

    segments: List[ResultYearSegment]
    """Segmentos do maior para o menor."""

    segments_total: float = FieldInfo(alias="segmentsTotal")
    """Soma dos segmentos.

    Pode passar da receita total quando os segmentos vendem entre si ou são de
    receita bruta.
    """

    status: Literal["ok", "no-segments", "review"]
    """`ok`: segmentos lidos.

    `no-segments`: a empresa não divulga segmentos, e a lista traz a receita total.
    `review`: há segmentos com alerta de leitura.
    """

    total_check: Optional[ResultYearTotalCheck] = FieldInfo(alias="totalCheck", default=None)
    """Conferência dos segmentos com a receita total."""


class ResultQuarterSegmentSource(BaseModel):
    document_id: str = FieldInfo(alias="documentId")
    """Protocolo ou número do documento na origem."""

    form: str
    """
    Documento de origem: `dfp` (demonstrações anuais na CVM), `itr` (demonstrações
    trimestrais na CVM), `10-K`, `20-F` ou `40-F` (relatório anual na SEC) ou
    `fii-quarterly` (informes trimestrais de FIIs na CVM).
    """

    page: Optional[int] = None
    """Página do valor no documento, quando conhecida."""

    prior_page: Optional[int] = FieldInfo(alias="priorPage", default=None)
    """Página do valor do ano anterior, quando conhecida."""

    url: Optional[str] = None
    """Link do documento."""


class ResultQuarterSegment(BaseModel):
    activity: str
    """Código da atividade do segmento."""

    activity_label: str = FieldInfo(alias="activityLabel")

    axis: str
    """
    Tipo de divisão: `business` (segmento de negócio), `product` (linha de produto
    ou serviço), `whole` (empresa sem segmentos: receita líquida total) ou
    `fii-income` (receitas de FIIs e Fiagros).
    """

    currency: str

    flags: List[str]
    """Alertas sobre o valor.

    `unchecked`: a soma dos segmentos não confere com a receita total. `relabeled`:
    uma conferência moveu o valor para outro segmento. `reviewed`: uma pessoa
    conferiu o segmento. `label-disputed`: duas leituras deram nomes diferentes ao
    segmento. `reviewed-by-model`: duas leituras discordaram e uma terceira leitura
    automática confirmou o segmento. `duplicate`: a mesma receita aparece em uma
    controlada listada. `includes-construction`: o valor inclui receita de
    construção. `gross`: o valor é receita bruta, antes de impostos e devoluções.
    """

    growth: Optional[float] = None
    """
    Crescimento do acumulado sobre o mesmo período do ano anterior, em fração (0.06
    = 6%).
    """

    growth_ex_construction: Optional[float] = FieldInfo(alias="growthExConstruction", default=None)
    """Crescimento sem a receita de construção, em fração (0.06 = 6%)."""

    member: str
    """Nome do segmento como a empresa publica."""

    prior_ex_construction: Optional[float] = FieldInfo(alias="priorExConstruction", default=None)
    """Receita do ano anterior sem a receita de construção."""

    prior_from: Optional[Literal["same-filing", "previous-filing"]] = FieldInfo(alias="priorFrom", default=None)
    """`same-filing` quando o valor anterior vem do mesmo documento.

    `previous-filing` quando vem do documento do ano anterior.
    """

    prior_value: Optional[float] = FieldInfo(alias="priorValue", default=None)
    """Receita acumulada no mesmo período do ano anterior."""

    quarter_value: Optional[float] = FieldInfo(alias="quarterValue", default=None)
    """
    Receita dos 3 meses do trimestre: o acumulado menos o acumulado do trimestre
    anterior. null quando os segmentos mudam entre os dois trimestres ou falta o
    trimestre anterior. Um segmento que só mudou de nome mantém o valor.
    """

    scope: Literal["exact", "mixed"]
    """`exact` quando o segmento tem só esta atividade.

    `mixed` quando ele junta atividades e esta é a principal.
    """

    source: ResultQuarterSegmentSource

    value: float
    """Receita acumulada no ano até `periodEnd`, na moeda `currency`."""

    value_ex_construction: Optional[float] = FieldInfo(alias="valueExConstruction", default=None)
    """
    Receita sem a receita de construção de concessões, quando a atividade tem essa
    receita.
    """


class ResultQuarterTotalCheck(BaseModel):
    """Conferência dos segmentos com a receita total acumulada no ano."""

    diff: Optional[float] = None
    """Diferença entre `sum` e `total`, ou `grossTotal` quando existe."""

    sum: float
    """Soma dos segmentos lidos, com as eliminações entre segmentos."""

    total: Optional[float] = None
    """Receita total publicada."""

    verified: bool
    """true quando a soma confere com a receita total, ou com `grossTotal`."""

    gross_total: Optional[float] = FieldInfo(alias="grossTotal", default=None)
    """Receita bruta publicada, quando os segmentos são de receita bruta."""


class ResultQuarter(BaseModel):
    currency: str

    fiscal_year: int = FieldInfo(alias="fiscalYear")

    months: int
    """Meses acumulados de 1º de janeiro até `periodEnd`: 3, 6, 9 ou 12.

    O 4º trimestre vem das demonstrações anuais.
    """

    period_end: str = FieldInfo(alias="periodEnd")

    quarter: int

    segments: List[ResultQuarterSegment]
    """Segmentos do maior para o menor."""

    segments_total: float = FieldInfo(alias="segmentsTotal")
    """Soma dos segmentos, acumulada no ano."""

    status: Literal["ok", "no-segments", "review"]
    """`ok`: segmentos lidos.

    `no-segments`: a empresa não divulga segmentos, e a lista traz a receita total.
    `review`: há segmentos com alerta de leitura.
    """

    total_check: Optional[ResultQuarterTotalCheck] = FieldInfo(alias="totalCheck", default=None)
    """Conferência dos segmentos com a receita total acumulada no ano."""


class Result(BaseModel):
    changed: bool
    """true quando o ticker pedido mudou de nome."""

    cnpj: Optional[str] = None
    """CNPJ do fundo. null para empresas."""

    issuer_code: Optional[str] = FieldInfo(alias="issuerCode", default=None)
    """Código do emissor na B3."""

    look_through: Optional[ResultLookThrough] = FieldInfo(alias="lookThrough", default=None)
    """
    Só para fundos com carteira mensal na CVM: exposição da carteira às atividades
    das empresas, FIIs e BDRs que o fundo tem. `null` para ETFs.
    """

    name: Optional[str] = None

    requested_symbol: str = FieldInfo(alias="requestedSymbol")

    symbol: str
    """Ticker atual, ou o CNPJ quando o fundo não tem ticker."""

    type: Optional[Literal["company", "bdr", "fii", "fiagro", "fund"]] = None
    """
    `company` (empresa da B3), `bdr`, `fii`, `fiagro` ou `fund` (ETF ou outro fundo,
    com a exposição pela carteira). null quando não há dados.
    """

    years: List[ResultYear]
    """Exercícios do mais recente para o mais antigo.

    Vazio para fundos e com `period=quarterly`.
    """

    quarters: Optional[List[ResultQuarter]] = None
    """Só com `period=quarterly`: trimestres do mais recente para o mais antigo."""


class RevenueSourceRetrieveResponse(BaseModel):
    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    results: List[Result]

    took: int
    """Tempo de processamento, em milissegundos."""
