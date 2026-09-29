# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["FiiListResponse", "Fii"]


class Fii(BaseModel):
    administrator_address: Optional[str] = FieldInfo(alias="administratorAddress", default=None)

    administrator_address_complement: Optional[str] = FieldInfo(alias="administratorAddressComplement", default=None)

    administrator_address_number: Optional[str] = FieldInfo(alias="administratorAddressNumber", default=None)

    administrator_city: Optional[str] = FieldInfo(alias="administratorCity", default=None)

    administrator_cnpj: Optional[str] = FieldInfo(alias="administratorCnpj", default=None)

    administrator_district: Optional[str] = FieldInfo(alias="administratorDistrict", default=None)

    administrator_email: Optional[str] = FieldInfo(alias="administratorEmail", default=None)

    administrator_name: Optional[str] = FieldInfo(alias="administratorName", default=None)

    administrator_phone1: Optional[str] = FieldInfo(alias="administratorPhone1", default=None)

    administrator_phone2: Optional[str] = FieldInfo(alias="administratorPhone2", default=None)

    administrator_phone3: Optional[str] = FieldInfo(alias="administratorPhone3", default=None)

    administrator_state: Optional[str] = FieldInfo(alias="administratorState", default=None)

    administrator_website: Optional[str] = FieldInfo(alias="administratorWebsite", default=None)

    administrator_zip_code: Optional[str] = FieldInfo(alias="administratorZipCode", default=None)

    cnpj: Optional[str] = None

    dividend_yield12m: Optional[float] = FieldInfo(alias="dividendYield12m", default=None)

    mandate: Optional[str] = None

    name: Optional[str] = None

    nav_per_share: Optional[float] = FieldInfo(alias="navPerShare", default=None)

    price: Optional[float] = None

    price_to_nav: Optional[float] = FieldInfo(alias="priceToNav", default=None)

    segmento_atuacao: Optional[str] = FieldInfo(alias="segmentoAtuacao", default=None)

    segment_type: Optional[str] = FieldInfo(alias="segmentType", default=None)

    symbol: Optional[str] = None

    tipo_gestao: Optional[str] = FieldInfo(alias="tipoGestao", default=None)

    total_investors: Optional[float] = FieldInfo(alias="totalInvestors", default=None)


class FiiListResponse(BaseModel):
    fiis: List[Fii]

    pagination: PaginationMeta

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
