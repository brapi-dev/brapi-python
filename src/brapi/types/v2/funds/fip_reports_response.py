# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ..fund_pagination_meta import FundPaginationMeta

__all__ = [
    "FipReportsResponse",
    "Report",
    "ReportCapital",
    "ReportInvestorComposition",
    "ReportInvestorCompositionByType",
    "ReportInvestorCompositionByTypeBrokersAndDistributors",
    "ReportInvestorCompositionByTypeCapitalizationAndLeasingCompanies",
    "ReportInvestorCompositionByTypeClosedPensionFunds",
    "ReportInvestorCompositionByTypeCommercialBanks",
    "ReportInvestorCompositionByTypeFinancialCompanies",
    "ReportInvestorCompositionByTypeFundDistributors",
    "ReportInvestorCompositionByTypeIndividuals",
    "ReportInvestorCompositionByTypeInsuranceCompanies",
    "ReportInvestorCompositionByTypeInvestmentFunds",
    "ReportInvestorCompositionByTypeNonFinancialCompanies",
    "ReportInvestorCompositionByTypeNonResidents",
    "ReportInvestorCompositionByTypeOpenPensionFunds",
    "ReportInvestorCompositionByTypeOtherInvestors",
    "ReportInvestorCompositionByTypePublicPensionFunds",
    "ReportInvestorCompositionByTypeRealEstateFunds",
    "ReportQuotaClass",
    "ReportQuotas",
]


class ReportCapital(BaseModel):
    committed: Optional[float] = None

    paid_in: Optional[float] = FieldInfo(alias="paidIn", default=None)

    subscribed: Optional[float] = None


class ReportInvestorCompositionByTypeBrokersAndDistributors(BaseModel):
    investors: Optional[float] = None

    subscribed_quota_percent: Optional[float] = FieldInfo(alias="subscribedQuotaPercent", default=None)


class ReportInvestorCompositionByTypeCapitalizationAndLeasingCompanies(BaseModel):
    investors: Optional[float] = None

    subscribed_quota_percent: Optional[float] = FieldInfo(alias="subscribedQuotaPercent", default=None)


class ReportInvestorCompositionByTypeClosedPensionFunds(BaseModel):
    investors: Optional[float] = None

    subscribed_quota_percent: Optional[float] = FieldInfo(alias="subscribedQuotaPercent", default=None)


class ReportInvestorCompositionByTypeCommercialBanks(BaseModel):
    investors: Optional[float] = None

    subscribed_quota_percent: Optional[float] = FieldInfo(alias="subscribedQuotaPercent", default=None)


class ReportInvestorCompositionByTypeFinancialCompanies(BaseModel):
    investors: Optional[float] = None

    subscribed_quota_percent: Optional[float] = FieldInfo(alias="subscribedQuotaPercent", default=None)


class ReportInvestorCompositionByTypeFundDistributors(BaseModel):
    investors: Optional[float] = None

    subscribed_quota_percent: Optional[float] = FieldInfo(alias="subscribedQuotaPercent", default=None)


class ReportInvestorCompositionByTypeIndividuals(BaseModel):
    investors: Optional[float] = None

    subscribed_quota_percent: Optional[float] = FieldInfo(alias="subscribedQuotaPercent", default=None)


class ReportInvestorCompositionByTypeInsuranceCompanies(BaseModel):
    investors: Optional[float] = None

    subscribed_quota_percent: Optional[float] = FieldInfo(alias="subscribedQuotaPercent", default=None)


class ReportInvestorCompositionByTypeInvestmentFunds(BaseModel):
    investors: Optional[float] = None

    subscribed_quota_percent: Optional[float] = FieldInfo(alias="subscribedQuotaPercent", default=None)


class ReportInvestorCompositionByTypeNonFinancialCompanies(BaseModel):
    investors: Optional[float] = None

    subscribed_quota_percent: Optional[float] = FieldInfo(alias="subscribedQuotaPercent", default=None)


class ReportInvestorCompositionByTypeNonResidents(BaseModel):
    investors: Optional[float] = None

    subscribed_quota_percent: Optional[float] = FieldInfo(alias="subscribedQuotaPercent", default=None)


class ReportInvestorCompositionByTypeOpenPensionFunds(BaseModel):
    investors: Optional[float] = None

    subscribed_quota_percent: Optional[float] = FieldInfo(alias="subscribedQuotaPercent", default=None)


class ReportInvestorCompositionByTypeOtherInvestors(BaseModel):
    investors: Optional[float] = None

    subscribed_quota_percent: Optional[float] = FieldInfo(alias="subscribedQuotaPercent", default=None)


class ReportInvestorCompositionByTypePublicPensionFunds(BaseModel):
    investors: Optional[float] = None

    subscribed_quota_percent: Optional[float] = FieldInfo(alias="subscribedQuotaPercent", default=None)


class ReportInvestorCompositionByTypeRealEstateFunds(BaseModel):
    investors: Optional[float] = None

    subscribed_quota_percent: Optional[float] = FieldInfo(alias="subscribedQuotaPercent", default=None)


class ReportInvestorCompositionByType(BaseModel):
    brokers_and_distributors: Optional[ReportInvestorCompositionByTypeBrokersAndDistributors] = FieldInfo(
        alias="brokersAndDistributors", default=None
    )

    capitalization_and_leasing_companies: Optional[ReportInvestorCompositionByTypeCapitalizationAndLeasingCompanies] = (
        FieldInfo(alias="capitalizationAndLeasingCompanies", default=None)
    )

    closed_pension_funds: Optional[ReportInvestorCompositionByTypeClosedPensionFunds] = FieldInfo(
        alias="closedPensionFunds", default=None
    )

    commercial_banks: Optional[ReportInvestorCompositionByTypeCommercialBanks] = FieldInfo(
        alias="commercialBanks", default=None
    )

    financial_companies: Optional[ReportInvestorCompositionByTypeFinancialCompanies] = FieldInfo(
        alias="financialCompanies", default=None
    )

    fund_distributors: Optional[ReportInvestorCompositionByTypeFundDistributors] = FieldInfo(
        alias="fundDistributors", default=None
    )

    individuals: Optional[ReportInvestorCompositionByTypeIndividuals] = None

    insurance_companies: Optional[ReportInvestorCompositionByTypeInsuranceCompanies] = FieldInfo(
        alias="insuranceCompanies", default=None
    )

    investment_funds: Optional[ReportInvestorCompositionByTypeInvestmentFunds] = FieldInfo(
        alias="investmentFunds", default=None
    )

    non_financial_companies: Optional[ReportInvestorCompositionByTypeNonFinancialCompanies] = FieldInfo(
        alias="nonFinancialCompanies", default=None
    )

    non_residents: Optional[ReportInvestorCompositionByTypeNonResidents] = FieldInfo(alias="nonResidents", default=None)

    open_pension_funds: Optional[ReportInvestorCompositionByTypeOpenPensionFunds] = FieldInfo(
        alias="openPensionFunds", default=None
    )

    other_investors: Optional[ReportInvestorCompositionByTypeOtherInvestors] = FieldInfo(
        alias="otherInvestors", default=None
    )

    public_pension_funds: Optional[ReportInvestorCompositionByTypePublicPensionFunds] = FieldInfo(
        alias="publicPensionFunds", default=None
    )

    real_estate_funds: Optional[ReportInvestorCompositionByTypeRealEstateFunds] = FieldInfo(
        alias="realEstateFunds", default=None
    )


class ReportInvestorComposition(BaseModel):
    by_type: ReportInvestorCompositionByType = FieldInfo(alias="byType")

    total_investors: Optional[float] = FieldInfo(alias="totalInvestors", default=None)

    total_subscribed_quota_percent: Optional[float] = FieldInfo(alias="totalSubscribedQuotaPercent", default=None)


class ReportQuotaClass(BaseModel):
    fund_type: Optional[str] = FieldInfo(alias="fundType", default=None)

    has_distinct_economic_rights: Optional[bool] = FieldInfo(alias="hasDistinctEconomicRights", default=None)

    has_special_political_rights: Optional[bool] = FieldInfo(alias="hasSpecialPoliticalRights", default=None)

    investors: Optional[float] = None

    name: Optional[str] = None

    paid_in_quotas: Optional[float] = FieldInfo(alias="paidInQuotas", default=None)

    quota_value: Optional[float] = FieldInfo(alias="quotaValue", default=None)

    subscribed_quotas: Optional[float] = FieldInfo(alias="subscribedQuotas", default=None)


class ReportQuotas(BaseModel):
    paid_in: Optional[float] = FieldInfo(alias="paidIn", default=None)

    subscribed: Optional[float] = None


class Report(BaseModel):
    capital: Optional[ReportCapital] = None

    cnpj: str

    invested_in_other_fips: Optional[float] = FieldInfo(alias="investedInOtherFips", default=None)

    investor_composition: Optional[ReportInvestorComposition] = FieldInfo(alias="investorComposition", default=None)

    is_investment_entity: Optional[bool] = FieldInfo(alias="isInvestmentEntity", default=None)

    name: Optional[str] = None

    net_equity: Optional[float] = FieldInfo(alias="netEquity", default=None)

    quota_class: Optional[ReportQuotaClass] = FieldInfo(alias="quotaClass", default=None)

    quotas: Optional[ReportQuotas] = None

    reference_date: str = FieldInfo(alias="referenceDate")

    report_type: Literal["trimestral", "quadrimestral"] = FieldInfo(alias="reportType")

    symbol: Optional[str] = None

    target_audience: Optional[str] = FieldInfo(alias="targetAudience", default=None)


class FipReportsResponse(BaseModel):
    pagination: FundPaginationMeta

    reports: List[Report]

    requested_at: datetime = FieldInfo(alias="requestedAt")
    """Data e hora da requisição em ISO 8601."""

    took: int
    """Tempo de processamento, em milissegundos."""
