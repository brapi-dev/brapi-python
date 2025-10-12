# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["IncomeStatementEntry"]


class IncomeStatementEntry(BaseModel):
    id: Optional[str] = None
    """Identificador único deste registro de DRE (interno)."""

    administrative_costs: Optional[float] = FieldInfo(alias="administrativeCosts", default=None)
    """Despesas Administrativas (detalhamento, pode estar contido em SG&A)."""

    basic_earnings_per_common_share: Optional[float] = FieldInfo(alias="basicEarningsPerCommonShare", default=None)
    """Lucro Básico por Ação Ordinária (ON)."""

    basic_earnings_per_preferred_share: Optional[float] = FieldInfo(
        alias="basicEarningsPerPreferredShare", default=None
    )
    """Lucro Básico por Ação Preferencial (PN)."""

    basic_earnings_per_share: Optional[float] = FieldInfo(alias="basicEarningsPerShare", default=None)
    """Lucro Básico por Ação (LPA Básico) - Geral."""

    capitalization_operations: Optional[float] = FieldInfo(alias="capitalizationOperations", default=None)
    """Resultado de Operações de Capitalização (específico para Seguradoras)."""

    claims_and_operations_costs: Optional[float] = FieldInfo(alias="claimsAndOperationsCosts", default=None)
    """Custos com Sinistros e Operações (específico para Seguradoras)."""

    complementary_pension_operations: Optional[float] = FieldInfo(alias="complementaryPensionOperations", default=None)
    """
    Resultado de Operações de Previdência Complementar (específico para
    Seguradoras/Previdência).
    """

    cost_of_revenue: Optional[float] = FieldInfo(alias="costOfRevenue", default=None)
    """Custo dos Produtos Vendidos (CPV) ou Custo dos Serviços Prestados (CSP)."""

    current_taxes: Optional[float] = FieldInfo(alias="currentTaxes", default=None)
    """Imposto de Renda e Contribuição Social Correntes."""

    deferred_taxes: Optional[float] = FieldInfo(alias="deferredTaxes", default=None)
    """Imposto de Renda e Contribuição Social Diferidos."""

    diluted_earnings_per_common_share: Optional[float] = FieldInfo(alias="dilutedEarningsPerCommonShare", default=None)
    """Lucro Diluído por Ação Ordinária (ON)."""

    diluted_earnings_per_preferred_share: Optional[float] = FieldInfo(
        alias="dilutedEarningsPerPreferredShare", default=None
    )
    """Lucro Diluído por Ação Preferencial (PN)."""

    diluted_earnings_per_share: Optional[float] = FieldInfo(alias="dilutedEarningsPerShare", default=None)
    """Lucro Diluído por Ação (LPA Diluído) - Geral."""

    discontinued_operations: Optional[float] = FieldInfo(alias="discontinuedOperations", default=None)
    """Resultado Líquido das Operações Descontinuadas."""

    earnings_per_share: Optional[float] = FieldInfo(alias="earningsPerShare", default=None)
    """Lucro por Ação (LPA) - Geral (pode ser básico ou diluído, verificar contexto)."""

    ebit: Optional[float] = None
    """Lucro Antes dos Juros e Impostos (LAJIR ou EBIT).

    Geralmente igual a `operatingIncome`.
    """

    effect_of_accounting_charges: Optional[float] = FieldInfo(alias="effectOfAccountingCharges", default=None)
    """Efeito de Mudanças Contábeis."""

    end_date: Optional[date] = FieldInfo(alias="endDate", default=None)
    """Data de término do período fiscal ao qual a DRE se refere (YYYY-MM-DD)."""

    equity_income_result: Optional[float] = FieldInfo(alias="equityIncomeResult", default=None)
    """Resultado de Equivalência Patrimonial."""

    extraordinary_items: Optional[float] = FieldInfo(alias="extraordinaryItems", default=None)
    """Itens Extraordinários."""

    financial_expenses: Optional[float] = FieldInfo(alias="financialExpenses", default=None)
    """Despesas Financeiras (valor positivo aqui, diferente de `interestExpense`)."""

    financial_income: Optional[float] = FieldInfo(alias="financialIncome", default=None)
    """Receitas Financeiras."""

    financial_result: Optional[float] = FieldInfo(alias="financialResult", default=None)
    """Resultado Financeiro Líquido."""

    gross_profit: Optional[float] = FieldInfo(alias="grossProfit", default=None)
    """Lucro Bruto (Receita Líquida - CPV/CSP)."""

    income_before_statutory_participations_and_contributions: Optional[float] = FieldInfo(
        alias="incomeBeforeStatutoryParticipationsAndContributions", default=None
    )
    """Resultado Antes das Participações Estatutárias."""

    income_before_tax: Optional[float] = FieldInfo(alias="incomeBeforeTax", default=None)
    """Lucro Antes do Imposto de Renda e Contribuição Social (LAIR).

    EBIT + Resultado Financeiro.
    """

    income_tax_expense: Optional[float] = FieldInfo(alias="incomeTaxExpense", default=None)
    """Imposto de Renda e Contribuição Social sobre o Lucro."""

    insurance_operations: Optional[float] = FieldInfo(alias="insuranceOperations", default=None)
    """Resultado de Operações de Seguros (específico para Seguradoras)."""

    interest_expense: Optional[float] = FieldInfo(alias="interestExpense", default=None)
    """Despesas Financeiras (Juros pagos). Note que este campo é negativo."""

    losses_due_to_non_recoverability_of_assets: Optional[float] = FieldInfo(
        alias="lossesDueToNonRecoverabilityOfAssets", default=None
    )
    """Perdas por Não Recuperabilidade de Ativos (Impairment)."""

    minority_interest: Optional[float] = FieldInfo(alias="minorityInterest", default=None)
    """Participação de Acionistas Não Controladores (no Lucro Líquido)."""

    net_income: Optional[float] = FieldInfo(alias="netIncome", default=None)
    """Lucro Líquido Consolidado do Período."""

    net_income_applicable_to_common_shares: Optional[float] = FieldInfo(
        alias="netIncomeApplicableToCommonShares", default=None
    )
    """Lucro Líquido Atribuível aos Acionistas Controladores (Ações Ordinárias)."""

    net_income_from_continuing_ops: Optional[float] = FieldInfo(alias="netIncomeFromContinuingOps", default=None)
    """Lucro Líquido das Operações Continuadas."""

    non_recurring: Optional[float] = FieldInfo(alias="nonRecurring", default=None)
    """Itens Não Recorrentes (pode incluir outras despesas/receitas operacionais)."""

    operating_income: Optional[float] = FieldInfo(alias="operatingIncome", default=None)
    """Lucro Operacional (EBIT - Earnings Before Interest and Taxes).

    Lucro Bruto - Despesas Operacionais.
    """

    other_items: Optional[float] = FieldInfo(alias="otherItems", default=None)
    """Outros Itens."""

    other_operating_expenses: Optional[float] = FieldInfo(alias="otherOperatingExpenses", default=None)
    """Outras Despesas Operacionais."""

    other_operating_income: Optional[float] = FieldInfo(alias="otherOperatingIncome", default=None)
    """Outras Receitas Operacionais (detalhamento)."""

    other_operating_income_and_expenses: Optional[float] = FieldInfo(
        alias="otherOperatingIncomeAndExpenses", default=None
    )
    """Outras Receitas e Despesas Operacionais (agregado)."""

    profit_sharing_and_statutory_contributions: Optional[float] = FieldInfo(
        alias="profitSharingAndStatutoryContributions", default=None
    )
    """Participações nos Lucros e Contribuições Estatutárias."""

    reinsurance_operations: Optional[float] = FieldInfo(alias="reinsuranceOperations", default=None)
    """Resultado de Operações de Resseguros (específico para Seguradoras)."""

    research_development: Optional[float] = FieldInfo(alias="researchDevelopment", default=None)
    """Despesas com Pesquisa e Desenvolvimento."""

    sales_expenses: Optional[float] = FieldInfo(alias="salesExpenses", default=None)
    """Despesas com Vendas (detalhamento, pode estar contido em SG&A)."""

    selling_general_administrative: Optional[float] = FieldInfo(alias="sellingGeneralAdministrative", default=None)
    """Despesas com Vendas, Gerais e Administrativas."""

    symbol: Optional[str] = None
    """Ticker do ativo ao qual a DRE se refere."""

    total_operating_expenses: Optional[float] = FieldInfo(alias="totalOperatingExpenses", default=None)
    """Total das Despesas Operacionais (P&D + SG&A + Outras)."""

    total_other_income_expense_net: Optional[float] = FieldInfo(alias="totalOtherIncomeExpenseNet", default=None)
    """Resultado Financeiro Líquido + Outras Receitas/Despesas."""

    total_revenue: Optional[float] = FieldInfo(alias="totalRevenue", default=None)
    """Receita Operacional Líquida."""

    type: Optional[Literal["yearly", "quarterly"]] = None
    """Indica a periodicidade da DRE: `yearly` (anual) ou `quarterly` (trimestral)."""

    updated_at: Optional[date] = FieldInfo(alias="updatedAt", default=None)
    """
    Data da última atualização deste registro específico na fonte de dados
    (YYYY-MM-DD).
    """
