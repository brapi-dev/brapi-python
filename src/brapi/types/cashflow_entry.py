# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CashflowEntry"]


class CashflowEntry(BaseModel):
    """
    Representa os dados de uma Demonstração do Fluxo de Caixa (DFC) para um período específico (anual ou trimestral).
    """

    adjustments_to_profit_or_loss: Optional[float] = FieldInfo(alias="adjustmentsToProfitOrLoss", default=None)
    """
    Ajustes ao lucro/prejuízo (depreciação, amortização, equivalência patrimonial,
    variações não caixa).
    """

    cash_generated_in_operations: Optional[float] = FieldInfo(alias="cashGeneratedInOperations", default=None)
    """Caixa gerado nas operações (após variações no capital de giro)."""

    changes_in_assets_and_liabilities: Optional[float] = FieldInfo(alias="changesInAssetsAndLiabilities", default=None)
    """
    Variações em Ativos e Passivos Operacionais (Clientes, Estoques, Fornecedores,
    etc.).
    """

    end_date: Optional[date] = FieldInfo(alias="endDate", default=None)
    """Data de término do período fiscal ao qual a DFC se refere (YYYY-MM-DD)."""

    exchange_variation_without_cash: Optional[float] = FieldInfo(alias="exchangeVariationWithoutCash", default=None)
    """Variação cambial sem efeito caixa (ajuste de conversão)."""

    final_cash_balance: Optional[float] = FieldInfo(alias="finalCashBalance", default=None)
    """Saldo Final de Caixa e Equivalentes no final do período."""

    financing_cash_flow: Optional[float] = FieldInfo(alias="financingCashFlow", default=None)
    """
    Fluxo de Caixa das Atividades de Financiamento (FCF) (Captação/Pagamento de
    Empréstimos, Emissão/Recompra de Ações, Dividendos pagos).
    """

    foreign_exchange_rate_without_cash: Optional[float] = FieldInfo(
        alias="foreignExchangeRateWithoutCash", default=None
    )
    """Efeito da Variação Cambial sobre o Caixa e Equivalentes."""

    income_from_operations: Optional[float] = FieldInfo(alias="incomeFromOperations", default=None)
    """Caixa Gerado nas Operações (antes das variações de ativos/passivos)."""

    increase_or_decrease_in_cash: Optional[float] = FieldInfo(alias="increaseOrDecreaseInCash", default=None)
    """
    Aumento ou Redução Líquida de Caixa e Equivalentes (FCO + FCI + FCF + Variação
    Cambial).
    """

    initial_cash_balance: Optional[float] = FieldInfo(alias="initialCashBalance", default=None)
    """Saldo Inicial de Caixa e Equivalentes no início do período."""

    investment_cash_flow: Optional[float] = FieldInfo(alias="investmentCashFlow", default=None)
    """
    Fluxo de Caixa das Atividades de Investimento (FCI) (Compra/Venda de
    Imobilizado, Investimentos).
    """

    net_income_before_taxes: Optional[float] = FieldInfo(alias="netIncomeBeforeTaxes", default=None)
    """
    Lucro líquido antes dos impostos (base para reconciliação pelo método indireto).
    """

    operating_cash_flow: Optional[float] = FieldInfo(alias="operatingCashFlow", default=None)
    """Fluxo de Caixa das Atividades Operacionais (FCO)."""

    other_operating_activities: Optional[float] = FieldInfo(alias="otherOperatingActivities", default=None)
    """Outras Atividades Operacionais (Juros pagos/recebidos, Impostos pagos, etc.)."""

    symbol: Optional[str] = None
    """Ticker do ativo ao qual a DFC se refere."""

    type: Optional[Literal["yearly", "quarterly"]] = None
    """Indica a periodicidade da DFC: `yearly` (anual) ou `quarterly` (trimestral)."""

    updated_at: Optional[date] = FieldInfo(alias="updatedAt", default=None)
    """
    Data da última atualização deste registro específico na fonte de dados
    (YYYY-MM-DD).
    """
