# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["StockInsiderTransactionsParams"]


class StockInsiderTransactionsParams(TypedDict, total=False):
    symbols: Required[str]
    """Tickers separados por vírgula.

    Máximo de 20. Cada ticker identifica a empresa que apresenta o relatório.
    """

    all_versions: Annotated[Literal["true", "false"], PropertyInfo(alias="allVersions")]
    """Inclui versões anteriores dos relatórios.

    Padrão: false. Versões anteriores podem repetir movimentações.
    """

    company_relation: Annotated[
        Literal["company", "parent", "subsidiary", "all"], PropertyInfo(alias="companyRelation")
    ]
    """
    Empresa que emite o valor mobiliário: a própria empresa, sua controladora ou sua
    controlada.
    """

    direction: Literal["credit", "debit"]
    """Entrada ou saída da posição. Inclui transferências e outras movimentações."""

    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """Data final da movimentação. Padrão: hoje."""

    limit: int
    """Máximo de movimentações por empresa e página."""

    movement_type: Annotated[str, PropertyInfo(alias="movementType")]
    """Tipo de movimentação, com o texto exato do relatório."""

    page: int
    """Página de cada empresa."""

    role_group: Annotated[
        Literal["controller", "board", "director", "fiscalCouncil", "statutoryBody"], PropertyInfo(alias="roleGroup")
    ]
    """Grupo de cargos. Cada grupo inclui pessoas vinculadas."""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """Data inicial da movimentação. Padrão: 365 dias antes de endDate."""
