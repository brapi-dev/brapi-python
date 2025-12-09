# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PrimeRateRetrieveResponse", "PrimeRate"]


class PrimeRate(BaseModel):
    """
    Representa um registro individual de taxa básica de juros (SELIC) para uma data específica.
    """

    date: Optional[str] = None
    """Data do registro no formato DD/MM/YYYY."""

    epoch_date: Optional[int] = FieldInfo(alias="epochDate", default=None)
    """Timestamp em milissegundos (formato epoch) correspondente à data do registro."""

    value: Optional[str] = None
    """Valor da taxa básica de juros (SELIC) para a data correspondente."""


class PrimeRateRetrieveResponse(BaseModel):
    """Resposta principal do endpoint `/api/v2/prime-rate`."""

    prime_rate: Optional[List[PrimeRate]] = FieldInfo(alias="prime-rate", default=None)
    """
    Array contendo os registros históricos de taxa básica de juros (SELIC) para o
    país e período solicitados.
    """
