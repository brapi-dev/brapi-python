# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FundExposureParams"]


class FundExposureParams(TypedDict, total=False):
    positions: Required[str]
    """
    Itens separados por vírgula, até 200: ticker ou CNPJ, com o valor em reais
    (`WRLD11:10000`) ou o peso (`WRLD11:30%`). Sem valor, o item recebe a média dos
    outros; sem nenhum valor, todos têm o mesmo peso. Use ponto como separador
    decimal.
    """

    limit: int
    """Empresas por página. Padrão 50, máximo 500."""

    page: int
    """Página, a partir de 1."""

    reference_date: Annotated[str, PropertyInfo(alias="referenceDate")]
    """Data no formato YYYY-MM-DD.

    Traz o mês mais recente até esta data. Sem ela, traz o mês mais recente.
    """
