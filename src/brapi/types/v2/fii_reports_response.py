# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["FiiReportsResponse", "Report"]


class Report(BaseModel):
    admin_fee_rate: Optional[float] = FieldInfo(alias="adminFeeRate", default=None)

    admin_fees_payable: Optional[float] = FieldInfo(alias="adminFeesPayable", default=None)

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

    amortization_rate: Optional[float] = FieldInfo(alias="amortizationRate", default=None)

    cash: Optional[float] = None

    cnpj: str

    cri: Optional[float] = None

    distributions_payable: Optional[float] = FieldInfo(alias="distributionsPayable", default=None)

    equity: Optional[float] = None

    fii_holdings: Optional[float] = FieldInfo(alias="fiiHoldings", default=None)

    fixed_income_funds: Optional[float] = FieldInfo(alias="fixedIncomeFunds", default=None)

    government_bonds: Optional[float] = FieldInfo(alias="governmentBonds", default=None)

    lci: Optional[float] = None

    liquidity_needs: Optional[float] = FieldInfo(alias="liquidityNeeds", default=None)

    monthly_dividend_yield: Optional[float] = FieldInfo(alias="monthlyDividendYield", default=None)

    monthly_patrimonial_return: Optional[float] = FieldInfo(alias="monthlyPatrimonialReturn", default=None)

    monthly_return: Optional[float] = FieldInfo(alias="monthlyReturn", default=None)

    name: Optional[str] = None

    nav_per_share: Optional[float] = FieldInfo(alias="navPerShare", default=None)

    other_receivables: Optional[float] = FieldInfo(alias="otherReceivables", default=None)

    private_bonds: Optional[float] = FieldInfo(alias="privateBonds", default=None)

    real_estate_assets: Optional[float] = FieldInfo(alias="realEstateAssets", default=None)

    real_estate_company_shares: Optional[float] = FieldInfo(alias="realEstateCompanyShares", default=None)

    real_estate_company_units: Optional[float] = FieldInfo(alias="realEstateCompanyUnits", default=None)

    real_estate_obligations: Optional[float] = FieldInfo(alias="realEstateObligations", default=None)

    receivables: Optional[float] = None

    reference_date: str = FieldInfo(alias="referenceDate")

    rental_receivables: Optional[float] = FieldInfo(alias="rentalReceivables", default=None)

    shares_outstanding: Optional[float] = FieldInfo(alias="sharesOutstanding", default=None)

    symbol: Optional[str] = None

    total_assets: Optional[float] = FieldInfo(alias="totalAssets", default=None)

    total_invested: Optional[float] = FieldInfo(alias="totalInvested", default=None)

    total_investors: Optional[float] = FieldInfo(alias="totalInvestors", default=None)

    total_liabilities: Optional[float] = FieldInfo(alias="totalLiabilities", default=None)

    version: float


class FiiReportsResponse(BaseModel):
    pagination: PaginationMeta

    reports: List[Report]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
