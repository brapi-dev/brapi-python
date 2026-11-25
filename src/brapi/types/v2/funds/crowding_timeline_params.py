# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CrowdingTimelineParams"]


class CrowdingTimelineParams(TypedDict, total=False):
    limit: int
    """Entram as empresas que ficaram entre as `limit` maiores em algum mês.

    Padrão 100, máximo 300.
    """

    region: Literal["all", "brazil", "foreign"]
    """`all` (padrão): todas as empresas.

    `brazil`: empresas da B3. `foreign`: empresas do exterior, por BDRs, ações no
    exterior e fundos do exterior.
    """
