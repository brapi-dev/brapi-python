# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["PrimeRateListAvailableResponse"]


class PrimeRateListAvailableResponse(BaseModel):
    """
    Resposta do endpoint `/api/v2/prime-rate/available` que lista os países disponíveis para consulta de taxa básica de juros (SELIC).
    """

    countries: Optional[List[str]] = None
    """
    Lista de países com dados de taxa básica de juros (SELIC) disponíveis para
    consulta.
    """
