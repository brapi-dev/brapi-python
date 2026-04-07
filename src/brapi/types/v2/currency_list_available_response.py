# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["CurrencyListAvailableResponse", "Currency"]


class Currency(BaseModel):
    currency: str

    name: str


class CurrencyListAvailableResponse(BaseModel):
    currencies: List[Currency]
