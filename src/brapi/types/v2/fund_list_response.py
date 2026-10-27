# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .fund_pagination_meta import FundPaginationMeta

__all__ = ["FundListResponse", "Fund", "FundFees"]


class FundFees(BaseModel):
    """Taxas do regulamento mais recente do fundo que as informa.

    Por enquanto, só para ETFs.
    """

    admin_fee_percent: Optional[float] = FieldInfo(alias="adminFeePercent", default=None)

    conditions: Optional[str] = None
    """Condições da taxa, como valor mínimo mensal ou faixas por patrimônio."""

    custody_max_fee_percent: Optional[float] = FieldInfo(alias="custodyMaxFeePercent", default=None)

    effective_date: str = FieldInfo(alias="effectiveDate")
    """Data de entrega do regulamento com esta taxa."""

    management_fee_percent: Optional[float] = FieldInfo(alias="managementFeePercent", default=None)

    performance_fee: Optional[str] = FieldInfo(alias="performanceFee", default=None)

    total_fee_percent: Optional[float] = FieldInfo(alias="totalFeePercent", default=None)
    """Taxa total ao ano, em percentual (0.2 = 0,20% a.a.).

    Quando o regulamento informa só as taxas de administração e de gestão, é a soma
    delas.
    """


class Fund(BaseModel):
    administrator_cnpj: Optional[str] = FieldInfo(alias="administratorCnpj", default=None)

    administrator_name: Optional[str] = FieldInfo(alias="administratorName", default=None)

    anbima_classification: Optional[str] = FieldInfo(alias="anbimaClassification", default=None)

    asset_type: Literal["fii", "fiagro", "fiinfra", "fif", "fidc", "fip", "etf", "other"] = FieldInfo(alias="assetType")

    b3_classification: Optional[str] = FieldInfo(alias="b3Classification", default=None)

    cnpj: str

    cvm_classification: Optional[str] = FieldInfo(alias="cvmClassification", default=None)

    cvm_class_type: Optional[str] = FieldInfo(alias="cvmClassType", default=None)

    equity: Optional[float] = None

    etf_category: Optional[Literal["fixed-income", "equity", "crypto", "real-estate"]] = FieldInfo(
        alias="etfCategory", default=None
    )
    """
    Categoria do ETF pela lista de ETFs da bolsa: `fixed-income` (renda fixa),
    `equity` (renda variável), `crypto` (criptoativos) ou `real-estate`
    (imobiliário). É `null` para fundos que não são ETF e para ETFs que nenhuma
    lista da bolsa traz.
    """

    fees: Optional[FundFees] = None
    """Taxas do regulamento mais recente do fundo que as informa.

    Por enquanto, só para ETFs.
    """

    formatted_cnpj: Optional[str] = FieldInfo(alias="formattedCnpj", default=None)

    isin: Optional[str] = None

    legal_name: Optional[str] = FieldInfo(alias="legalName", default=None)

    manager_cnpj: Optional[str] = FieldInfo(alias="managerCnpj", default=None)

    manager_name: Optional[str] = FieldInfo(alias="managerName", default=None)

    name: Optional[str] = None

    nav_per_share: Optional[float] = FieldInfo(alias="navPerShare", default=None)

    price: Optional[float] = None

    price_date: Optional[str] = FieldInfo(alias="priceDate", default=None)
    """Data do preço de fechamento usado em `price` e `priceToNav`."""

    price_to_nav: Optional[float] = FieldInfo(alias="priceToNav", default=None)

    status: Optional[str] = None

    symbol: Optional[str] = None

    total_assets: Optional[float] = FieldInfo(alias="totalAssets", default=None)

    total_investors: Optional[float] = FieldInfo(alias="totalInvestors", default=None)

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)


class FundListResponse(BaseModel):
    funds: List[Fund]

    pagination: FundPaginationMeta

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
