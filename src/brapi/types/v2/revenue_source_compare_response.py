# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RevenueSourceCompareResponse", "Activity", "Issuer", "IssuerYear", "IssuerYearSource"]


class Activity(BaseModel):
    cnae: Optional[str] = None
    """Classe ou divisão CNAE mais próxima. É uma referência."""

    code: str

    comparable: bool
    """false para bancos e seguradoras, cujas receitas não se comparam.

    `compare` recusa essas atividades.
    """

    construction_revenue: bool = FieldInfo(alias="constructionRevenue")
    """
    true para concessões que registram o investimento na rede como receita de
    construção. O crescimento em `compare` não usa essa receita.
    """

    label: str

    parent: Optional[str] = None
    """Código da atividade mãe. null no primeiro nível."""


class IssuerYearSource(BaseModel):
    document_id: str = FieldInfo(alias="documentId")
    """Protocolo ou número do documento na origem."""

    form: str
    """
    Documento de origem: `dfp` (demonstrações anuais na CVM), `10-K`, `20-F` ou
    `40-F` (relatório anual na SEC) ou `fii-quarterly` (informes trimestrais de FIIs
    na CVM).
    """

    page: Optional[int] = None
    """Página do valor no documento, quando conhecida."""

    url: Optional[str] = None
    """Link do documento."""


class IssuerYear(BaseModel):
    basis: Literal["reported", "exConstruction"]
    """`exConstruction` quando o crescimento não usa a receita de construção.

    `reported` nos demais casos.
    """

    fiscal_year: int = FieldInfo(alias="fiscalYear")

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

    prior_value: Optional[float] = FieldInfo(alias="priorValue", default=None)
    """Receita do ano anterior, na mesma base de `growth`."""

    segments: List[str]
    """Segmentos somados, como a empresa publica."""

    source: IssuerYearSource

    value: float
    """Receita da atividade no exercício, na moeda do emissor."""

    value_ex_construction: Optional[float] = FieldInfo(alias="valueExConstruction", default=None)
    """Receita sem a receita de construção.

    Preenchido quando `basis` é `exConstruction`.
    """


class Issuer(BaseModel):
    currency: str

    issuer_code: str = FieldInfo(alias="issuerCode")

    latest_growth: Optional[float] = FieldInfo(alias="latestGrowth", default=None)

    latest_value: float = FieldInfo(alias="latestValue")

    latest_year: int = FieldInfo(alias="latestYear")

    name: str

    type: Literal["company", "bdr", "fii", "fiagro"]

    years: List[IssuerYear]
    """Exercícios do mais recente para o mais antigo."""


class RevenueSourceCompareResponse(BaseModel):
    activity: Activity

    issuers: List[Issuer]
    """
    Emissores com receita na atividade, do maior para o menor crescimento no último
    exercício. Compare o crescimento: os valores podem estar em moedas diferentes.
    """

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
