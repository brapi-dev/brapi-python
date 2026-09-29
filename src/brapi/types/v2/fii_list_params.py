# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FiiListParams"]


class FiiListParams(TypedDict, total=False):
    cnpjs: str
    """CNPJs de FIIs separados por vírgula, até 20. Aceita com ou sem pontuação."""

    limit: int
    """Itens por página. Não há limite máximo."""

    mandate: str
    """Mandato do fundo. Ex.: Renda, Híbrido, Títulos e Valores Mobiliários."""

    page: int
    """Número da página, a partir de 1."""

    search: str
    """Texto buscado no nome, no ticker ou no CNPJ."""

    segmento_atuacao: Annotated[str, PropertyInfo(alias="segmentoAtuacao")]
    """Setor de atuação. Ex.: Logística, Shoppings, Escritórios."""

    segment_type: Annotated[Literal["papel", "tijolo", "hibrido", "fof"], PropertyInfo(alias="segmentType")]
    """Tipo do fundo: papel, tijolo, hibrido ou fof."""

    sort_by: Annotated[str, PropertyInfo(alias="sortBy")]
    """Campo de ordenação."""

    sort_order: Annotated[Literal["asc", "desc"], PropertyInfo(alias="sortOrder")]
    """Direção da ordenação."""

    symbols: str
    """Tickers de FIIs separados por vírgula, até 20."""

    tipo_gestao: Annotated[str, PropertyInfo(alias="tipoGestao")]
    """Tipo de gestão: Ativa ou Definida."""
