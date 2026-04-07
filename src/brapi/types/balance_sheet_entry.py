# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["BalanceSheetEntry"]


class BalanceSheetEntry(BaseModel):
    accounts_payable: Optional[float] = FieldInfo(alias="accountsPayable", default=None)
    """Fornecedores"""

    cash: Optional[float] = None
    """Caixa"""

    end_date: str = FieldInfo(alias="endDate")
    """Data de referência"""

    inventory: Optional[float] = None
    """Estoques"""

    long_term_debt: Optional[float] = FieldInfo(alias="longTermDebt", default=None)
    """Dívida de longo prazo"""

    long_term_investments: Optional[float] = FieldInfo(alias="longTermInvestments", default=None)
    """Investimentos de longo prazo"""

    net_receivables: Optional[float] = FieldInfo(alias="netReceivables", default=None)
    """Contas a receber"""

    other_assets: Optional[float] = FieldInfo(alias="otherAssets", default=None)
    """Outros ativos"""

    other_current_assets: Optional[float] = FieldInfo(alias="otherCurrentAssets", default=None)
    """Outros ativos circulantes"""

    property_plant_equipment: Optional[float] = FieldInfo(alias="propertyPlantEquipment", default=None)
    """Imobilizado"""

    short_long_term_debt: Optional[float] = FieldInfo(alias="shortLongTermDebt", default=None)
    """Dívida de curto/longo prazo"""

    short_term_investments: Optional[float] = FieldInfo(alias="shortTermInvestments", default=None)
    """Investimentos de curto prazo"""

    symbol: str
    """Ticker do ativo"""

    total_assets: Optional[float] = FieldInfo(alias="totalAssets", default=None)
    """Total de ativos"""

    total_current_assets: Optional[float] = FieldInfo(alias="totalCurrentAssets", default=None)
    """Total ativo circulante"""

    total_current_liabilities: Optional[float] = FieldInfo(alias="totalCurrentLiabilities", default=None)
    """Passivo circulante total"""

    total_liab: Optional[float] = FieldInfo(alias="totalLiab", default=None)
    """Passivo total"""

    total_stockholder_equity: Optional[float] = FieldInfo(alias="totalStockholderEquity", default=None)
    """Patrimônio líquido"""

    type: str
    """Tipo (yearly, quarterly)"""

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)
    """Data de atualização"""
