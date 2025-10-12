# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["PrimeRateListAvailableResponse"]


class PrimeRateListAvailableResponse(BaseModel):
    countries: Optional[List[str]] = None
    """
    Lista de países com dados de taxa básica de juros (SELIC) disponíveis para
    consulta.
    """
