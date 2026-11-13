# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "StockShareholdersResponse",
    "Result",
    "ResultData",
    "ResultDataChain",
    "ResultDataChainOwned",
    "ResultDataChainOwner",
    "ResultDataChainOwnerShareClass",
    "ResultDataFiling",
    "ResultDataFreeFloat",
    "ResultDataHolderCounts",
    "ResultDataOthers",
    "ResultDataShareholder",
    "ResultDataShareholderShareClass",
    "ResultDataStake",
    "ResultDataStakeCompany",
    "ResultDataTreasury",
    "ResultDataUltimateController",
]


class ResultDataChainOwned(BaseModel):
    id: str
    """Identificador estável do participante.

    Empresas e fundos: `cnpj:` e a raiz do CNPJ (8 dígitos). Pessoas: `person:` e o
    nome. Sem documento: `name:` e o nome.
    """

    cnpj: Optional[str] = None
    """CNPJ com 14 dígitos. Sempre null para pessoas físicas."""

    kind: Literal["company", "person", "fund", "government", "foreign"]
    """
    Tipo do participante: empresa, pessoa física, fundo (inclui fundos de pensão),
    governo (União, estados, municípios, BNDES e BNDESPAR) ou empresa estrangeira.
    """

    name: str

    symbol: Optional[str] = None
    """Ticker principal, quando o participante é listado na B3."""


class ResultDataChainOwnerShareClass(BaseModel):
    percent: Optional[float] = None

    share_class: str = FieldInfo(alias="shareClass")

    shares: Optional[float] = None


class ResultDataChainOwner(BaseModel):
    id: str
    """Identificador estável do participante.

    Empresas e fundos: `cnpj:` e a raiz do CNPJ (8 dígitos). Pessoas: `person:` e o
    nome. Sem documento: `name:` e o nome.
    """

    cnpj: Optional[str] = None
    """CNPJ com 14 dígitos. Sempre null para pessoas físicas."""

    common_percent: Optional[float] = FieldInfo(alias="commonPercent", default=None)
    """Parte das ações ordinárias, em %. É a parte do voto."""

    common_shares: Optional[float] = FieldInfo(alias="commonShares", default=None)
    """Ações ordinárias (ON), com direito a voto."""

    date: Optional[str] = None
    """Data da última alteração da posição."""

    in_shareholder_agreement: bool = FieldInfo(alias="inShareholderAgreement")
    """O acionista participa do acordo de acionistas."""

    is_controller: bool = FieldInfo(alias="isController")
    """A empresa informa o acionista como controlador."""

    kind: Literal["company", "person", "fund", "government", "foreign"]
    """
    Tipo do participante: empresa, pessoa física, fundo (inclui fundos de pensão),
    governo (União, estados, municípios, BNDES e BNDESPAR) ou empresa estrangeira.
    """

    name: str

    nationality: Optional[str] = None

    preferred_percent: Optional[float] = FieldInfo(alias="preferredPercent", default=None)
    """Parte das ações preferenciais, em %."""

    preferred_shares: Optional[float] = FieldInfo(alias="preferredShares", default=None)

    share_classes: List[ResultDataChainOwnerShareClass] = FieldInfo(alias="shareClasses")
    """Divisão por classe de ação, quando informada."""

    symbol: Optional[str] = None
    """Ticker principal, quando o participante é listado na B3."""

    total_percent: Optional[float] = FieldInfo(alias="totalPercent", default=None)
    """Parte de todas as ações, em %."""

    total_shares: Optional[float] = FieldInfo(alias="totalShares", default=None)


class ResultDataChain(BaseModel):
    level: int
    """1: acionista de um acionista; 2: um nível acima."""

    owned: ResultDataChainOwned

    owner: ResultDataChainOwner


class ResultDataFiling(BaseModel):
    archive_year: int = FieldInfo(alias="archiveYear")

    filed_at: Optional[str] = FieldInfo(alias="filedAt", default=None)
    """Data de entrega desta versão."""

    reference_date: str = FieldInfo(alias="referenceDate")

    source_url: Optional[str] = FieldInfo(alias="sourceUrl", default=None)

    version: int
    """Versão do Formulário de Referência.

    A empresa entrega nova versão quando o controle ou um acionista com 5% ou mais
    muda.
    """


class ResultDataFreeFloat(BaseModel):
    """
    Ações em circulação: fora das mãos de controladores, administradores e da tesouraria.
    """

    common_percent: Optional[float] = FieldInfo(alias="commonPercent", default=None)
    """Parte das ações ordinárias, em %. É a parte do voto."""

    common_shares: Optional[float] = FieldInfo(alias="commonShares", default=None)
    """Ações ordinárias (ON), com direito a voto."""

    preferred_percent: Optional[float] = FieldInfo(alias="preferredPercent", default=None)
    """Parte das ações preferenciais, em %."""

    preferred_shares: Optional[float] = FieldInfo(alias="preferredShares", default=None)

    total_percent: Optional[float] = FieldInfo(alias="totalPercent", default=None)
    """Parte de todas as ações, em %."""

    total_shares: Optional[float] = FieldInfo(alias="totalShares", default=None)


class ResultDataHolderCounts(BaseModel):
    companies: Optional[float] = None

    individuals: Optional[float] = None

    institutions: Optional[float] = None


class ResultDataOthers(BaseModel):
    """Demais acionistas, cada um com menos de 5%."""

    common_percent: Optional[float] = FieldInfo(alias="commonPercent", default=None)
    """Parte das ações ordinárias, em %. É a parte do voto."""

    common_shares: Optional[float] = FieldInfo(alias="commonShares", default=None)
    """Ações ordinárias (ON), com direito a voto."""

    preferred_percent: Optional[float] = FieldInfo(alias="preferredPercent", default=None)
    """Parte das ações preferenciais, em %."""

    preferred_shares: Optional[float] = FieldInfo(alias="preferredShares", default=None)

    total_percent: Optional[float] = FieldInfo(alias="totalPercent", default=None)
    """Parte de todas as ações, em %."""

    total_shares: Optional[float] = FieldInfo(alias="totalShares", default=None)


class ResultDataShareholderShareClass(BaseModel):
    percent: Optional[float] = None

    share_class: str = FieldInfo(alias="shareClass")

    shares: Optional[float] = None


class ResultDataShareholder(BaseModel):
    id: str
    """Identificador estável do participante.

    Empresas e fundos: `cnpj:` e a raiz do CNPJ (8 dígitos). Pessoas: `person:` e o
    nome. Sem documento: `name:` e o nome.
    """

    cnpj: Optional[str] = None
    """CNPJ com 14 dígitos. Sempre null para pessoas físicas."""

    common_percent: Optional[float] = FieldInfo(alias="commonPercent", default=None)
    """Parte das ações ordinárias, em %. É a parte do voto."""

    common_shares: Optional[float] = FieldInfo(alias="commonShares", default=None)
    """Ações ordinárias (ON), com direito a voto."""

    date: Optional[str] = None
    """Data da última alteração da posição."""

    in_shareholder_agreement: bool = FieldInfo(alias="inShareholderAgreement")
    """O acionista participa do acordo de acionistas."""

    is_controller: bool = FieldInfo(alias="isController")
    """A empresa informa o acionista como controlador."""

    kind: Literal["company", "person", "fund", "government", "foreign"]
    """
    Tipo do participante: empresa, pessoa física, fundo (inclui fundos de pensão),
    governo (União, estados, municípios, BNDES e BNDESPAR) ou empresa estrangeira.
    """

    name: str

    nationality: Optional[str] = None

    preferred_percent: Optional[float] = FieldInfo(alias="preferredPercent", default=None)
    """Parte das ações preferenciais, em %."""

    preferred_shares: Optional[float] = FieldInfo(alias="preferredShares", default=None)

    share_classes: List[ResultDataShareholderShareClass] = FieldInfo(alias="shareClasses")
    """Divisão por classe de ação, quando informada."""

    symbol: Optional[str] = None
    """Ticker principal, quando o participante é listado na B3."""

    total_percent: Optional[float] = FieldInfo(alias="totalPercent", default=None)
    """Parte de todas as ações, em %."""

    total_shares: Optional[float] = FieldInfo(alias="totalShares", default=None)


class ResultDataStakeCompany(BaseModel):
    id: str
    """Identificador estável do participante.

    Empresas e fundos: `cnpj:` e a raiz do CNPJ (8 dígitos). Pessoas: `person:` e o
    nome. Sem documento: `name:` e o nome.
    """

    cnpj: Optional[str] = None
    """CNPJ com 14 dígitos. Sempre null para pessoas físicas."""

    kind: Literal["company", "person", "fund", "government", "foreign"]
    """
    Tipo do participante: empresa, pessoa física, fundo (inclui fundos de pensão),
    governo (União, estados, municípios, BNDES e BNDESPAR) ou empresa estrangeira.
    """

    name: str

    symbol: Optional[str] = None
    """Ticker principal, quando o participante é listado na B3."""


class ResultDataStake(BaseModel):
    company: ResultDataStakeCompany

    date: Optional[str] = None

    is_controller: bool = FieldInfo(alias="isController")

    source: Literal["shareholderTable", "subsidiaryList"]
    """`shareholderTable`: quadro de acionistas da empresa detida.

    `subsidiaryList`: lista de controladas e coligadas da própria empresa.
    """

    total_percent: Optional[float] = FieldInfo(alias="totalPercent", default=None)

    voting_percent: Optional[float] = FieldInfo(alias="votingPercent", default=None)


class ResultDataTreasury(BaseModel):
    """Ações em tesouraria."""

    common_percent: Optional[float] = FieldInfo(alias="commonPercent", default=None)
    """Parte das ações ordinárias, em %. É a parte do voto."""

    common_shares: Optional[float] = FieldInfo(alias="commonShares", default=None)
    """Ações ordinárias (ON), com direito a voto."""

    preferred_percent: Optional[float] = FieldInfo(alias="preferredPercent", default=None)
    """Parte das ações preferenciais, em %."""

    preferred_shares: Optional[float] = FieldInfo(alias="preferredShares", default=None)

    total_percent: Optional[float] = FieldInfo(alias="totalPercent", default=None)
    """Parte de todas as ações, em %."""

    total_shares: Optional[float] = FieldInfo(alias="totalShares", default=None)


class ResultDataUltimateController(BaseModel):
    id: str
    """Identificador estável do participante.

    Empresas e fundos: `cnpj:` e a raiz do CNPJ (8 dígitos). Pessoas: `person:` e o
    nome. Sem documento: `name:` e o nome.
    """

    cnpj: Optional[str] = None
    """CNPJ com 14 dígitos. Sempre null para pessoas físicas."""

    kind: Literal["company", "person", "fund", "government", "foreign"]
    """
    Tipo do participante: empresa, pessoa física, fundo (inclui fundos de pensão),
    governo (União, estados, municípios, BNDES e BNDESPAR) ou empresa estrangeira.
    """

    name: str

    symbol: Optional[str] = None
    """Ticker principal, quando o participante é listado na B3."""


class ResultData(BaseModel):
    chain: List[ResultDataChain]
    """Quem detém os acionistas, até onde o formulário informa.

    Os percentuais referem-se à empresa detida (`owned`).
    """

    cnpj: str

    company_name: str = FieldInfo(alias="companyName")

    filing: ResultDataFiling

    free_float: ResultDataFreeFloat = FieldInfo(alias="freeFloat")
    """
    Ações em circulação: fora das mãos de controladores, administradores e da
    tesouraria.
    """

    holder_counts: ResultDataHolderCounts = FieldInfo(alias="holderCounts")

    others: Optional[ResultDataOthers] = None
    """Demais acionistas, cada um com menos de 5%."""

    shareholders: List[ResultDataShareholder]
    """
    Controladores e acionistas com 5% ou mais de uma espécie de ação, do maior para
    o menor.
    """

    stakes: List[ResultDataStake]
    """Participações desta empresa em outras empresas. Empresas listadas primeiro."""

    treasury: Optional[ResultDataTreasury] = None
    """Ações em tesouraria."""

    ultimate_controllers: List[ResultDataUltimateController] = FieldInfo(alias="ultimateControllers")
    """Entidades no topo da cadeia de controle.

    A busca segue controladores com 10% ou mais e para antes de pessoas físicas. Uma
    holding com mais de 2 controladores é o topo. Vazio quando não há controle
    definido.
    """


class Result(BaseModel):
    changed: bool

    data: ResultData

    requested_symbol: str = FieldInfo(alias="requestedSymbol")

    symbol: str


class StockShareholdersResponse(BaseModel):
    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    results: List[Result]

    took: int
    """Tempo de processamento, em milissegundos."""
