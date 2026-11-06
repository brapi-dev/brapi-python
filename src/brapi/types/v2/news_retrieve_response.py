# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .news_story import NewsStory

__all__ = ["NewsRetrieveResponse"]


class NewsRetrieveResponse(BaseModel):
    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    results: List[NewsStory]
    """A notícia encontrada, com a matéria completa."""

    took: int
    """Tempo de processamento, em milissegundos."""
