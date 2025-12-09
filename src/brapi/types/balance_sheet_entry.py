# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["BalanceSheetEntry"]


class BalanceSheetEntry(BaseModel):
    """
    Representa os dados de um Balanço Patrimonial para um período específico (anual ou trimestral).
    """

    accounts_payable: Optional[float] = FieldInfo(alias="accountsPayable", default=None)
    """Contas a pagar (fornecedores)."""

    accounts_receivable_from_clients: Optional[float] = FieldInfo(alias="accountsReceivableFromClients", default=None)
    """Contas a receber de clientes (bruto)."""

    accumulated_profits_or_losses: Optional[float] = FieldInfo(alias="accumulatedProfitsOrLosses", default=None)
    """Lucros ou prejuízos acumulados."""

    advance_for_future_capital_increase: Optional[float] = FieldInfo(
        alias="advanceForFutureCapitalIncrease", default=None
    )
    """Adiantamento para futuro aumento de capital (AFAC)."""

    biological_assets: Optional[float] = FieldInfo(alias="biologicalAssets", default=None)
    """Ativos biológicos."""

    capitalization: Optional[float] = None
    """Obrigações de capitalização."""

    capital_reserves: Optional[float] = FieldInfo(alias="capitalReserves", default=None)
    """Reservas de capital (sinônimo de `capitalSurplus`)."""

    capital_surplus: Optional[float] = FieldInfo(alias="capitalSurplus", default=None)
    """Reservas de capital."""

    cash: Optional[float] = None
    """Caixa e equivalentes de caixa."""

    central_bank_compulsory_deposit: Optional[float] = FieldInfo(alias="centralBankCompulsoryDeposit", default=None)
    """Depósitos compulsórios no Banco Central."""

    common_stock: Optional[float] = FieldInfo(alias="commonStock", default=None)
    """Capital social realizado."""

    complementary_pension: Optional[float] = FieldInfo(alias="complementaryPension", default=None)
    """Obrigações de previdência complementar."""

    compulsory_loans_and_deposits: Optional[float] = FieldInfo(alias="compulsoryLoansAndDeposits", default=None)
    """Empréstimos e depósitos compulsórios."""

    controller_shareholders_equity: Optional[float] = FieldInfo(alias="controllerShareholdersEquity", default=None)
    """Patrimônio líquido atribuível aos controladores."""

    credits_from_operations: Optional[float] = FieldInfo(alias="creditsFromOperations", default=None)
    """Créditos oriundos de operações (instituições financeiras/seguradoras)."""

    credits_with_related_parties: Optional[float] = FieldInfo(alias="creditsWithRelatedParties", default=None)
    """Créditos com partes relacionadas."""

    cumulative_conversion_adjustments: Optional[float] = FieldInfo(
        alias="cumulativeConversionAdjustments", default=None
    )
    """Ajustes acumulados de conversão."""

    current_and_deferred_taxes: Optional[float] = FieldInfo(alias="currentAndDeferredTaxes", default=None)
    """Tributos correntes e diferidos no ativo."""

    current_liabilities: Optional[float] = FieldInfo(alias="currentLiabilities", default=None)
    """Total do passivo circulante (sinônimo de `totalCurrentLiabilities`)."""

    debentures: Optional[float] = None
    """Debêntures (passivo circulante)."""

    debits_from_capitalization: Optional[float] = FieldInfo(alias="debitsFromCapitalization", default=None)
    """Débitos de operações de capitalização."""

    debits_from_complementary_pension: Optional[float] = FieldInfo(alias="debitsFromComplementaryPension", default=None)
    """Débitos de operações de previdência complementar."""

    debits_from_insurance_and_reinsurance: Optional[float] = FieldInfo(
        alias="debitsFromInsuranceAndReinsurance", default=None
    )
    """Débitos de operações de seguros e resseguros."""

    debits_from_operations: Optional[float] = FieldInfo(alias="debitsFromOperations", default=None)
    """Débitos oriundos de operações."""

    debits_from_other_operations: Optional[float] = FieldInfo(alias="debitsFromOtherOperations", default=None)
    """Débitos de outras operações."""

    deferred_long_term_asset_charges: Optional[float] = FieldInfo(alias="deferredLongTermAssetCharges", default=None)
    """Encargos diferidos de ativos de longo prazo."""

    deferred_long_term_liab: Optional[float] = FieldInfo(alias="deferredLongTermLiab", default=None)
    """Passivos fiscais diferidos (longo prazo)."""

    deferred_selling_expenses: Optional[float] = FieldInfo(alias="deferredSellingExpenses", default=None)
    """Despesas de comercialização diferidas."""

    deferred_taxes: Optional[float] = FieldInfo(alias="deferredTaxes", default=None)
    """Tributos diferidos no ativo."""

    end_date: Optional[date] = FieldInfo(alias="endDate", default=None)
    """Data de término do período fiscal ao qual o balanço se refere (YYYY-MM-DD)."""

    equity_valuation_adjustments: Optional[float] = FieldInfo(alias="equityValuationAdjustments", default=None)
    """Ajustes de avaliação patrimonial."""

    financial_assets: Optional[float] = FieldInfo(alias="financialAssets", default=None)
    """Ativos financeiros (agregado de instrumentos financeiros no ativo)."""

    financial_assets_at_amortized_cost: Optional[float] = FieldInfo(
        alias="financialAssetsAtAmortizedCost", default=None
    )
    """Ativos financeiros ao custo amortizado."""

    financial_assets_measured_at_fair_value_through_other_comprehensive_income: Optional[float] = FieldInfo(
        alias="financialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncome", default=None
    )
    """
    Ativos financeiros mensurados a valor justo por outros resultados abrangentes
    (FVOCI).
    """

    financial_assets_measured_at_fair_value_through_profit_or_loss: Optional[float] = FieldInfo(
        alias="financialAssetsMeasuredAtFairValueThroughProfitOrLoss", default=None
    )
    """Ativos financeiros mensurados a valor justo por meio do resultado (FVTPL)."""

    financial_investments_measured_at_amortized_cost: Optional[float] = FieldInfo(
        alias="financialInvestmentsMeasuredAtAmortizedCost", default=None
    )
    """Investimentos financeiros mensurados ao custo amortizado."""

    financial_investments_measured_at_fair_value_through_other_comprehensive_income: Optional[float] = FieldInfo(
        alias="financialInvestmentsMeasuredAtFairValueThroughOtherComprehensiveIncome", default=None
    )
    """
    Investimentos financeiros mensurados a valor justo por outros resultados
    abrangentes.
    """

    financial_liabilities_at_amortized_cost: Optional[float] = FieldInfo(
        alias="financialLiabilitiesAtAmortizedCost", default=None
    )
    """Passivos financeiros ao custo amortizado."""

    financial_liabilities_measured_at_fair_value_through_income: Optional[float] = FieldInfo(
        alias="financialLiabilitiesMeasuredAtFairValueThroughIncome", default=None
    )
    """Passivos financeiros mensurados a valor justo por meio do resultado."""

    foreign_suppliers: Optional[float] = FieldInfo(alias="foreignSuppliers", default=None)
    """Fornecedores estrangeiros."""

    good_will: Optional[float] = FieldInfo(alias="goodWill", default=None)
    """Ágio por expectativa de rentabilidade futura (Goodwill)."""

    insurance_and_reinsurance: Optional[float] = FieldInfo(alias="insuranceAndReinsurance", default=None)
    """Provisões/obrigações de seguros e resseguros."""

    intangible_asset: Optional[float] = FieldInfo(alias="intangibleAsset", default=None)
    """Ativo intangível (valor agregado)."""

    intangible_assets: Optional[float] = FieldInfo(alias="intangibleAssets", default=None)
    """Ativos intangíveis (marcas, patentes, etc.)."""

    inventory: Optional[float] = None
    """Estoques."""

    investment_properties: Optional[float] = FieldInfo(alias="investmentProperties", default=None)
    """Propriedades para investimento."""

    investments: Optional[float] = None
    """Investimentos (participações e outros)."""

    lease_financing: Optional[float] = FieldInfo(alias="leaseFinancing", default=None)
    """Financiamento por arrendamento mercantil (circulante)."""

    loans_and_financing: Optional[float] = FieldInfo(alias="loansAndFinancing", default=None)
    """Empréstimos e financiamentos (circulante)."""

    loans_and_financing_in_foreign_currency: Optional[float] = FieldInfo(
        alias="loansAndFinancingInForeignCurrency", default=None
    )
    """Empréstimos e financiamentos em moeda estrangeira (circulante)."""

    loans_and_financing_in_national_currency: Optional[float] = FieldInfo(
        alias="loansAndFinancingInNationalCurrency", default=None
    )
    """Empréstimos e financiamentos em moeda nacional (circulante)."""

    long_term_accounts_payable: Optional[float] = FieldInfo(alias="longTermAccountsPayable", default=None)
    """Fornecedores/contas a pagar de longo prazo."""

    long_term_accounts_receivable_from_clients: Optional[float] = FieldInfo(
        alias="longTermAccountsReceivableFromClients", default=None
    )
    """Contas a receber de clientes - longo prazo."""

    long_term_assets: Optional[float] = FieldInfo(alias="longTermAssets", default=None)
    """Total do ativo não circulante (agregado)."""

    long_term_biological_assets: Optional[float] = FieldInfo(alias="longTermBiologicalAssets", default=None)
    """Ativos biológicos de longo prazo."""

    long_term_capitalization: Optional[float] = FieldInfo(alias="longTermCapitalization", default=None)
    """Obrigações de capitalização de longo prazo."""

    long_term_complementary_pension: Optional[float] = FieldInfo(alias="longTermComplementaryPension", default=None)
    """Obrigações de previdência complementar de longo prazo."""

    long_term_debentures: Optional[float] = FieldInfo(alias="longTermDebentures", default=None)
    """Debêntures (passivo não circulante)."""

    long_term_debits_from_operations: Optional[float] = FieldInfo(alias="longTermDebitsFromOperations", default=None)
    """Débitos de operações (longo prazo)."""

    long_term_debt: Optional[float] = FieldInfo(alias="longTermDebt", default=None)
    """Dívida de longo prazo (empréstimos e financiamentos não circulantes)."""

    long_term_deferred_taxes: Optional[float] = FieldInfo(alias="longTermDeferredTaxes", default=None)
    """Tributos diferidos (Ativo Não Circulante)."""

    long_term_financial_investments_measured_at_fair_value_through_income: Optional[float] = FieldInfo(
        alias="longTermFinancialInvestmentsMeasuredAtFairValueThroughIncome", default=None
    )
    """
    Investimentos financeiros de longo prazo mensurados a valor justo por meio do
    resultado.
    """

    long_term_insurance_and_reinsurance: Optional[float] = FieldInfo(
        alias="longTermInsuranceAndReinsurance", default=None
    )
    """Obrigações de seguros e resseguros de longo prazo."""

    long_term_inventory: Optional[float] = FieldInfo(alias="longTermInventory", default=None)
    """Estoques de longo prazo."""

    long_term_investments: Optional[float] = FieldInfo(alias="longTermInvestments", default=None)
    """Investimentos de longo prazo."""

    long_term_lease_financing: Optional[float] = FieldInfo(alias="longTermLeaseFinancing", default=None)
    """Financiamento por arrendamento mercantil (não circulante)."""

    long_term_liabilities: Optional[float] = FieldInfo(alias="longTermLiabilities", default=None)
    """Total do passivo de longo prazo."""

    long_term_loans_and_financing: Optional[float] = FieldInfo(alias="longTermLoansAndFinancing", default=None)
    """Empréstimos e financiamentos (não circulante)."""

    long_term_loans_and_financing_in_foreign_currency: Optional[float] = FieldInfo(
        alias="longTermLoansAndFinancingInForeignCurrency", default=None
    )
    """Empréstimos e financiamentos em moeda estrangeira (não circulante)."""

    long_term_loans_and_financing_in_national_currency: Optional[float] = FieldInfo(
        alias="longTermLoansAndFinancingInNationalCurrency", default=None
    )
    """Empréstimos e financiamentos em moeda nacional (não circulante)."""

    long_term_prepaid_expenses: Optional[float] = FieldInfo(alias="longTermPrepaidExpenses", default=None)
    """Despesas antecipadas de longo prazo."""

    long_term_provisions: Optional[float] = FieldInfo(alias="longTermProvisions", default=None)
    """Provisões (passivo não circulante)."""

    long_term_realizable_assets: Optional[float] = FieldInfo(alias="longTermRealizableAssets", default=None)
    """Ativo realizável a longo prazo."""

    long_term_receivables: Optional[float] = FieldInfo(alias="longTermReceivables", default=None)
    """Contas a receber de longo prazo."""

    long_term_technical_provisions: Optional[float] = FieldInfo(alias="longTermTechnicalProvisions", default=None)
    """Provisões técnicas de longo prazo."""

    minority_interest: Optional[float] = FieldInfo(alias="minorityInterest", default=None)
    """Participação de não controladores (no patrimônio líquido)."""

    national_suppliers: Optional[float] = FieldInfo(alias="nationalSuppliers", default=None)
    """Fornecedores nacionais."""

    net_receivables: Optional[float] = FieldInfo(alias="netReceivables", default=None)
    """Contas a receber líquidas (clientes)."""

    net_tangible_assets: Optional[float] = FieldInfo(alias="netTangibleAssets", default=None)
    """Ativos tangíveis líquidos (Ativo Total - Intangíveis - Passivo Total)."""

    non_controlling_shareholders_equity: Optional[float] = FieldInfo(
        alias="nonControllingShareholdersEquity", default=None
    )
    """Participação dos não controladores no patrimônio líquido."""

    non_current_assets: Optional[float] = FieldInfo(alias="nonCurrentAssets", default=None)
    """Total do ativo não circulante (sinônimo de `longTermAssets`)."""

    non_current_liabilities: Optional[float] = FieldInfo(alias="nonCurrentLiabilities", default=None)
    """Total do passivo não circulante."""

    other_accounts_receivable: Optional[float] = FieldInfo(alias="otherAccountsReceivable", default=None)
    """Outras contas a receber."""

    other_assets: Optional[float] = FieldInfo(alias="otherAssets", default=None)
    """Outros ativos não circulantes."""

    other_comprehensive_results: Optional[float] = FieldInfo(alias="otherComprehensiveResults", default=None)
    """Outros resultados abrangentes."""

    other_current_assets: Optional[float] = FieldInfo(alias="otherCurrentAssets", default=None)
    """Outros ativos circulantes."""

    other_current_liab: Optional[float] = FieldInfo(alias="otherCurrentLiab", default=None)
    """Outros passivos circulantes."""

    other_current_liabilities: Optional[float] = FieldInfo(alias="otherCurrentLiabilities", default=None)
    """Outros passivos circulantes (sinônimo de `otherCurrentLiab`)."""

    other_debits: Optional[float] = FieldInfo(alias="otherDebits", default=None)
    """Outros débitos."""

    other_liab: Optional[float] = FieldInfo(alias="otherLiab", default=None)
    """Outros passivos não circulantes."""

    other_liabilities: Optional[float] = FieldInfo(alias="otherLiabilities", default=None)
    """Outros passivos."""

    other_long_term_obligations: Optional[float] = FieldInfo(alias="otherLongTermObligations", default=None)
    """Outras obrigações (passivo não circulante)."""

    other_long_term_provisions: Optional[float] = FieldInfo(alias="otherLongTermProvisions", default=None)
    """Outras provisões de longo prazo."""

    other_long_term_receivables: Optional[float] = FieldInfo(alias="otherLongTermReceivables", default=None)
    """Outros créditos/recebíveis de longo prazo."""

    other_non_current_assets: Optional[float] = FieldInfo(alias="otherNonCurrentAssets", default=None)
    """Outros ativos não circulantes (detalhamento)."""

    other_non_current_liabilities: Optional[float] = FieldInfo(alias="otherNonCurrentLiabilities", default=None)
    """Outros passivos não circulantes."""

    other_obligations: Optional[float] = FieldInfo(alias="otherObligations", default=None)
    """Outras obrigações (circulante)."""

    other_operations: Optional[float] = FieldInfo(alias="otherOperations", default=None)
    """Outras contas operacionais no ativo."""

    other_provisions: Optional[float] = FieldInfo(alias="otherProvisions", default=None)
    """Outras provisões (diversas)."""

    other_stockholder_equity: Optional[float] = FieldInfo(alias="otherStockholderEquity", default=None)
    """Outros componentes do patrimônio líquido."""

    other_values_and_assets: Optional[float] = FieldInfo(alias="otherValuesAndAssets", default=None)
    """Outros valores e bens."""

    prepaid_expenses: Optional[float] = FieldInfo(alias="prepaidExpenses", default=None)
    """Despesas antecipadas."""

    profit_reserves: Optional[float] = FieldInfo(alias="profitReserves", default=None)
    """Reservas de lucros."""

    profits_and_revenues_to_be_appropriated: Optional[float] = FieldInfo(
        alias="profitsAndRevenuesToBeAppropriated", default=None
    )
    """Lucros e receitas a apropriar."""

    property_plant_equipment: Optional[float] = FieldInfo(alias="propertyPlantEquipment", default=None)
    """Imobilizado (propriedades, instalações e equipamentos)."""

    providers: Optional[float] = None
    """Fornecedores (sinônimo de `accountsPayable`)."""

    provisions: Optional[float] = None
    """Provisões (passivo)."""

    realized_share_capital: Optional[float] = FieldInfo(alias="realizedShareCapital", default=None)
    """Capital social realizado (sinônimo de `commonStock`)."""

    retained_earnings: Optional[float] = FieldInfo(alias="retainedEarnings", default=None)
    """Lucros/Prejuízos acumulados."""

    revaluation_reserves: Optional[float] = FieldInfo(alias="revaluationReserves", default=None)
    """Reservas de reavaliação."""

    securities_and_credits_receivable: Optional[float] = FieldInfo(alias="securitiesAndCreditsReceivable", default=None)
    """Títulos e créditos a receber."""

    shareholders_equity: Optional[float] = FieldInfo(alias="shareholdersEquity", default=None)
    """Patrimônio líquido (sinônimo de `totalStockholderEquity`)."""

    shareholdings: Optional[float] = None
    """Participações societárias."""

    short_long_term_debt: Optional[float] = FieldInfo(alias="shortLongTermDebt", default=None)
    """Dívida de curto prazo (empréstimos e financiamentos circulantes)."""

    short_term_investments: Optional[float] = FieldInfo(alias="shortTermInvestments", default=None)
    """Aplicações financeiras de curto prazo."""

    social_and_labor_obligations: Optional[float] = FieldInfo(alias="socialAndLaborObligations", default=None)
    """Obrigações sociais e trabalhistas."""

    symbol: Optional[str] = None
    """Ticker do ativo ao qual o balanço se refere."""

    taxes_to_recover: Optional[float] = FieldInfo(alias="taxesToRecover", default=None)
    """Impostos a recuperar."""

    tax_liabilities: Optional[float] = FieldInfo(alias="taxLiabilities", default=None)
    """Obrigações fiscais (passivo)."""

    tax_obligations: Optional[float] = FieldInfo(alias="taxObligations", default=None)
    """Obrigações fiscais (passivo circulante)."""

    technical_provisions: Optional[float] = FieldInfo(alias="technicalProvisions", default=None)
    """Provisões técnicas (seguradoras/previdência)."""

    third_party_deposits: Optional[float] = FieldInfo(alias="thirdPartyDeposits", default=None)
    """Depósitos de terceiros."""

    total_assets: Optional[float] = FieldInfo(alias="totalAssets", default=None)
    """Total do ativo."""

    total_current_assets: Optional[float] = FieldInfo(alias="totalCurrentAssets", default=None)
    """Total do ativo circulante."""

    total_current_liabilities: Optional[float] = FieldInfo(alias="totalCurrentLiabilities", default=None)
    """Total do passivo circulante."""

    total_liab: Optional[float] = FieldInfo(alias="totalLiab", default=None)
    """Total do passivo (circulante + não circulante)."""

    total_liabilities: Optional[float] = FieldInfo(alias="totalLiabilities", default=None)
    """Total do passivo."""

    total_stockholder_equity: Optional[float] = FieldInfo(alias="totalStockholderEquity", default=None)
    """Total do patrimônio líquido."""

    treasury_stock: Optional[float] = FieldInfo(alias="treasuryStock", default=None)
    """Ações em tesouraria."""

    type: Optional[Literal["yearly", "quarterly"]] = None
    """
    Indica a periodicidade do balanço: `yearly` (anual) ou `quarterly` (trimestral).
    """

    updated_at: Optional[date] = FieldInfo(alias="updatedAt", default=None)
    """Data da última atualização deste registro (YYYY-MM-DD)."""
