# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .news_story import NewsStory

__all__ = ["NewsListResponse"]


class NewsListResponse(BaseModel):
    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
    """Cursor da próxima página, para o parâmetro `cursor`. `null` na última página."""

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    results: List[NewsStory]

    took: int
    """Tempo de processamento, em milissegundos."""
