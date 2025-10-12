# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["InflationRetrieveResponse", "Inflation"]


class Inflation(BaseModel):
    date: Optional[str] = None
    """Data da medição da inflação, no formato `DD/MM/YYYY`."""

    epoch_date: Optional[int] = FieldInfo(alias="epochDate", default=None)
    """
    Timestamp UNIX (número de segundos desde 1970-01-01 UTC) correspondente à
    `date`.
    """

    value: Optional[str] = None
    """
    Valor do índice de inflação para a data especificada (formato string, pode
    conter `%` ou ser apenas numérico).
    """


class InflationRetrieveResponse(BaseModel):
    inflation: Optional[List[Inflation]] = None
    """
    Array contendo os registros históricos de inflação para o país e período
    solicitados.
    """
