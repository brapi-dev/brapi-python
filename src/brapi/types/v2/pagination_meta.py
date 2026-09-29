# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PaginationMeta"]


class PaginationMeta(BaseModel):
    has_next_page: bool = FieldInfo(alias="hasNextPage")

    limit: float

    page: float

    total_items: float = FieldInfo(alias="totalItems")

    total_pages: float = FieldInfo(alias="totalPages")
