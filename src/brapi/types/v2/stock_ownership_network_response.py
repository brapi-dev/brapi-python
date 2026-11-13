# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["StockOwnershipNetworkResponse", "Cycle", "CycleEdge", "Edge", "Node", "Root", "TopController"]


class CycleEdge(BaseModel):
    date: Optional[str] = None

    from_: str = FieldInfo(alias="from")
    """Quem detém."""

    is_controller: bool = FieldInfo(alias="isController")

    preferred_percent: Optional[float] = FieldInfo(alias="preferredPercent", default=None)

    source_cnpj: str = FieldInfo(alias="sourceCnpj")
    """CNPJ da empresa cujo formulário informa a ligação."""

    source_symbol: Optional[str] = FieldInfo(alias="sourceSymbol", default=None)

    to: str
    """Empresa detida."""

    total_percent: Optional[float] = FieldInfo(alias="totalPercent", default=None)

    voting_percent: Optional[float] = FieldInfo(alias="votingPercent", default=None)
    """Parte das ações ordinárias."""


class Cycle(BaseModel):
    edges: List[CycleEdge]

    nodes: List[str]


class Edge(BaseModel):
    date: Optional[str] = None

    from_: str = FieldInfo(alias="from")
    """Quem detém."""

    is_controller: bool = FieldInfo(alias="isController")

    preferred_percent: Optional[float] = FieldInfo(alias="preferredPercent", default=None)

    source_cnpj: str = FieldInfo(alias="sourceCnpj")
    """CNPJ da empresa cujo formulário informa a ligação."""

    source_symbol: Optional[str] = FieldInfo(alias="sourceSymbol", default=None)

    to: str
    """Empresa detida."""

    total_percent: Optional[float] = FieldInfo(alias="totalPercent", default=None)

    voting_percent: Optional[float] = FieldInfo(alias="votingPercent", default=None)
    """Parte das ações ordinárias."""


class Node(BaseModel):
    id: str
    """Identificador estável do participante.

    Empresas e fundos: `cnpj:` e a raiz do CNPJ (8 dígitos). Pessoas: `person:` e o
    nome. Sem documento: `name:` e o nome.
    """

    cnpj: Optional[str] = None
    """CNPJ com 14 dígitos. Sempre null para pessoas físicas."""

    is_filer: bool = FieldInfo(alias="isFiler")
    """A empresa entrega o próprio quadro de acionistas."""

    kind: Literal["company", "person", "fund", "government", "foreign"]
    """
    Tipo do participante: empresa, pessoa física, fundo (inclui fundos de pensão),
    governo (União, estados, municípios, BNDES e BNDESPAR) ou empresa estrangeira.
    """

    market_cap: Optional[float] = FieldInfo(alias="marketCap", default=None)
    """Valor de mercado em R$, para empresas listadas."""

    name: str

    symbol: Optional[str] = None
    """Ticker principal, quando o participante é listado na B3."""


class Root(BaseModel):
    id: str

    requested_symbol: str = FieldInfo(alias="requestedSymbol")

    symbol: str


class TopController(BaseModel):
    id: str
    """Identificador estável do participante.

    Empresas e fundos: `cnpj:` e a raiz do CNPJ (8 dígitos). Pessoas: `person:` e o
    nome. Sem documento: `name:` e o nome.
    """

    cnpj: Optional[str] = None
    """CNPJ com 14 dígitos. Sempre null para pessoas físicas."""

    companies: List[str]

    kind: Literal["company", "person", "fund", "government", "foreign"]
    """
    Tipo do participante: empresa, pessoa física, fundo (inclui fundos de pensão),
    governo (União, estados, municípios, BNDES e BNDESPAR) ou empresa estrangeira.
    """

    market_value_controlled: float = FieldInfo(alias="marketValueControlled")
    """
    Soma do valor de mercado, em R$, das empresas listadas que a entidade controla
    no topo da cadeia. Controle conjunto conta para cada controlador.
    """

    name: str

    symbol: Optional[str] = None
    """Ticker principal, quando o participante é listado na B3."""


class StockOwnershipNetworkResponse(BaseModel):
    cycles: List[Cycle]
    """
    Participações cruzadas: grupos em que cada empresa detém, direta ou
    indiretamente, as outras.
    """

    depth: Optional[int] = None

    edges: List[Edge]

    min_percent: float = FieldInfo(alias="minPercent")

    nodes: List[Node]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    root: Optional[Root] = None

    took: int
    """Tempo de processamento, em milissegundos."""

    top_controllers: List[TopController] = FieldInfo(alias="topControllers")
    """Até 20 controladores, pelo valor de mercado controlado.

    Com ticker, só os que estão na rede.
    """

    truncated: bool
    """A rede passou de `limit` e foi cortada."""
