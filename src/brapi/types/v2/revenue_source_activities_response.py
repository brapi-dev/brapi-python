# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RevenueSourceActivitiesResponse", "Activity"]


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


class RevenueSourceActivitiesResponse(BaseModel):
    activities: List[Activity]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
