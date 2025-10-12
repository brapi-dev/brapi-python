# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ValueAddedEntry"]


class ValueAddedEntry(BaseModel):
    added_value_received_by_transfer: Optional[float] = FieldInfo(alias="addedValueReceivedByTransfer", default=None)
    """
    Valor Adicionado Recebido em Transferência (Resultado de Equivalência
    Patrimonial, Receitas Financeiras, etc.). Item 6 da DVA.
    """

    added_value_received_on_transfer: Optional[float] = FieldInfo(alias="addedValueReceivedOnTransfer", default=None)
    """
    Valor Adicionado Recebido em Transferência (sinônimo de
    `addedValueReceivedByTransfer`).
    """

    added_value_to_distribute: Optional[float] = FieldInfo(alias="addedValueToDistribute", default=None)
    """
    Valor Adicionado Total a Distribuir (Líquido Produzido + Recebido em
    Transferência). Item 7 da DVA.
    """

    claims_and_benefits: Optional[float] = FieldInfo(alias="claimsAndBenefits", default=None)
    """Sinistros Retidos e Benefícios."""

    complementary_pension_operations_revenue: Optional[float] = FieldInfo(
        alias="complementaryPensionOperationsRevenue", default=None
    )
    """Receita com Operações de Previdência Complementar."""

    construction_of_own_assets: Optional[float] = FieldInfo(alias="constructionOfOwnAssets", default=None)
    """Construção de Ativos Próprios."""

    costs_with_products_sold: Optional[float] = FieldInfo(alias="costsWithProductsSold", default=None)
    """Custos dos Produtos, Mercadorias e Serviços Vendidos (detalhamento)."""

    depreciation_and_amortization: Optional[float] = FieldInfo(alias="depreciationAndAmortization", default=None)
    """Depreciação e Amortização."""

    distribution_of_added_value: Optional[float] = FieldInfo(alias="distributionOfAddedValue", default=None)
    """Distribuição do Valor Adicionado (Soma dos itens seguintes). Item 8 da DVA."""

    dividends: Optional[float] = None
    """Dividendos Distribuídos."""

    end_date: Optional[date] = FieldInfo(alias="endDate", default=None)
    """Data de término do período fiscal ao qual a DVA se refere (YYYY-MM-DD)."""

    equity_income_result: Optional[float] = FieldInfo(alias="equityIncomeResult", default=None)
    """Resultado de Equivalência Patrimonial (como receita na DVA)."""

    equity_remuneration: Optional[float] = FieldInfo(alias="equityRemuneration", default=None)
    """Remuneração de Capitais Próprios (JCP, Dividendos, Lucros Retidos)."""

    federal_taxes: Optional[float] = FieldInfo(alias="federalTaxes", default=None)
    """Impostos Federais (IRPJ, CSLL, PIS, COFINS, IPI)."""

    fees_revenue: Optional[float] = FieldInfo(alias="feesRevenue", default=None)
    """Receita com Taxas e Comissões."""

    financial_income: Optional[float] = FieldInfo(alias="financialIncome", default=None)
    """Receitas Financeiras (como valor recebido em transferência)."""

    financial_intermediation_expenses: Optional[float] = FieldInfo(
        alias="financialIntermediationExpenses", default=None
    )
    """Despesas de Intermediação Financeira (específico para bancos)."""

    financial_intermediation_revenue: Optional[float] = FieldInfo(alias="financialIntermediationRevenue", default=None)
    """Receita de Intermediação Financeira (específico para bancos)."""

    gross_added_value: Optional[float] = FieldInfo(alias="grossAddedValue", default=None)
    """Valor Adicionado Bruto (Receitas - Insumos). Item 3 da DVA."""

    insurance_operations_revenue: Optional[float] = FieldInfo(alias="insuranceOperationsRevenue", default=None)
    """Receita com Operações de Seguros (específico para Seguradoras)."""

    insurance_operations_variations: Optional[float] = FieldInfo(alias="insuranceOperationsVariations", default=None)
    """Variações de Operações de Seguros."""

    interest_on_own_equity: Optional[float] = FieldInfo(alias="interestOnOwnEquity", default=None)
    """Juros sobre o Capital Próprio (JCP)."""

    loss_or_recovery_of_assets: Optional[float] = FieldInfo(alias="lossOrRecoveryOfAssets", default=None)
    """Perda/Recuperação de Valores de Ativos (Impairment - como custo/receita)."""

    loss_or_recovery_of_asset_values: Optional[float] = FieldInfo(alias="lossOrRecoveryOfAssetValues", default=None)
    """Perda / Recuperação de Valores de Ativos (Impairment)."""

    materials_energy_and_others: Optional[float] = FieldInfo(alias="materialsEnergyAndOthers", default=None)
    """Custos com Materiais, Energia, Serviços de Terceiros e Outros."""

    municipal_taxes: Optional[float] = FieldInfo(alias="municipalTaxes", default=None)
    """Impostos Municipais (ISS)."""

    net_added_value: Optional[float] = FieldInfo(alias="netAddedValue", default=None)
    """Valor Adicionado Líquido Produzido pela Entidade (Bruto - Retenções).

    Item 5 da DVA.
    """

    net_added_value_produced: Optional[float] = FieldInfo(alias="netAddedValueProduced", default=None)
    """Valor Adicionado Líquido Produzido (sinônimo de `netAddedValue`)."""

    net_operating_revenue: Optional[float] = FieldInfo(alias="netOperatingRevenue", default=None)
    """Receita Operacional Líquida (detalhamento)."""

    non_controlling_share_of_retained_earnings: Optional[float] = FieldInfo(
        alias="nonControllingShareOfRetainedEarnings", default=None
    )
    """Participação dos Não Controladores nos Lucros Retidos."""

    other_distributions: Optional[float] = FieldInfo(alias="otherDistributions", default=None)
    """Outras Distribuições."""

    other_retentions: Optional[float] = FieldInfo(alias="otherRetentions", default=None)
    """Outras Retenções (Exaustão, etc.)."""

    other_revenues: Optional[float] = FieldInfo(alias="otherRevenues", default=None)
    """Outras Receitas."""

    other_supplies: Optional[float] = FieldInfo(alias="otherSupplies", default=None)
    """Outros Insumos."""

    other_values_received_by_transfer: Optional[float] = FieldInfo(alias="otherValuesReceivedByTransfer", default=None)
    """Outros Valores Recebidos (Receitas Financeiras, Aluguéis, etc.)."""

    other_variations: Optional[float] = FieldInfo(alias="otherVariations", default=None)
    """Outras Variações."""

    own_equity_remuneration: Optional[float] = FieldInfo(alias="ownEquityRemuneration", default=None)
    """Remuneração de Capitais Próprios (sinônimo de `equityRemuneration`)."""

    pension_operations_variations: Optional[float] = FieldInfo(alias="pensionOperationsVariations", default=None)
    """Variações de Operações de Previdência."""

    product_sales: Optional[float] = FieldInfo(alias="productSales", default=None)
    """Venda de Produtos e Serviços (detalhamento)."""

    provision_or_reversal_of_doubtful_accounts: Optional[float] = FieldInfo(
        alias="provisionOrReversalOfDoubtfulAccounts", default=None
    )
    """
    Provisão/Reversão para Créditos de Liquidação Duvidosa (PCLD - como
    receita/despesa na DVA).
    """

    provision_or_reversal_of_expected_credit_risk_losses: Optional[float] = FieldInfo(
        alias="provisionOrReversalOfExpectedCreditRiskLosses", default=None
    )
    """Provisão/Reversão de Perdas com Risco de Crédito (PCLD)."""

    remuneration_of_third_party_capitals: Optional[float] = FieldInfo(
        alias="remunerationOfThirdPartyCapitals", default=None
    )
    """Remuneração de Capitais de Terceiros (Juros, Aluguéis)."""

    result_of_coinsurance_operations_assigned: Optional[float] = FieldInfo(
        alias="resultOfCoinsuranceOperationsAssigned", default=None
    )
    """Resultado de Operações de Cosseguros Cedidos."""

    results_of_ceded_reinsurance_operations: Optional[float] = FieldInfo(
        alias="resultsOfCededReinsuranceOperations", default=None
    )
    """Resultados de Operações de Resseguros Cedidos."""

    retained_earnings_or_loss: Optional[float] = FieldInfo(alias="retainedEarningsOrLoss", default=None)
    """Lucros Retidos ou Prejuízo do Exercício."""

    retentions: Optional[float] = None
    """Retenções (Depreciação, Amortização e Exaustão). Item 4 da DVA."""

    revenue: Optional[float] = None
    """Receitas (Venda de Mercadorias, Produtos e Serviços, etc.). Item 1 da DVA."""

    revenue_from_the_provision_of_services: Optional[float] = FieldInfo(
        alias="revenueFromTheProvisionOfServices", default=None
    )
    """Receita da Prestação de Serviços (detalhamento)."""

    services: Optional[float] = None
    """Serviços de Terceiros (detalhamento)."""

    state_taxes: Optional[float] = FieldInfo(alias="stateTaxes", default=None)
    """Impostos Estaduais (ICMS)."""

    supplies_purchased_from_third_parties: Optional[float] = FieldInfo(
        alias="suppliesPurchasedFromThirdParties", default=None
    )
    """Insumos Adquiridos de Terceiros (Custo de Mercadorias, Matérias-Primas).

    Item 2 da DVA.
    """

    symbol: Optional[str] = None
    """Ticker do ativo ao qual a DVA se refere."""

    taxes: Optional[float] = None
    """Impostos, Taxas e Contribuições (Federais, Estaduais, Municipais)."""

    team_remuneration: Optional[float] = FieldInfo(alias="teamRemuneration", default=None)
    """Pessoal e Encargos (Salários, Benefícios, FGTS)."""

    third_party_materials_and_services: Optional[float] = FieldInfo(
        alias="thirdPartyMaterialsAndServices", default=None
    )
    """Materiais, Energia, Serviços de Terceiros."""

    total_added_value_to_distribute: Optional[float] = FieldInfo(alias="totalAddedValueToDistribute", default=None)
    """Valor Adicionado Total a Distribuir (sinônimo de `addedValueToDistribute`)."""

    type: Optional[Literal["yearly", "quarterly"]] = None
    """Indica a periodicidade da DVA: `yearly` (anual) ou `quarterly` (trimestral)."""

    updated_at: Optional[date] = FieldInfo(alias="updatedAt", default=None)
    """
    Data da última atualização deste registro específico na fonte de dados
    (YYYY-MM-DD).
    """

    variation_in_deferred_selling_expenses: Optional[float] = FieldInfo(
        alias="variationInDeferredSellingExpenses", default=None
    )
    """Variação nas Despesas de Comercialização Diferidas."""

    variations_of_technical_provisions: Optional[float] = FieldInfo(
        alias="variationsOfTechnicalProvisions", default=None
    )
    """Variações das Provisões Técnicas (específico para Seguradoras)."""
