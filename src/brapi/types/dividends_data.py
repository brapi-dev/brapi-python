# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DividendsData", "CashDividend", "CashDividendBdr", "StockDividend"]


class CashDividendBdr(BaseModel):
    """Só em BDRs: o provento no exterior e os descontos até chegar em `rate`.

    Campos não informados no aviso vêm nulos.
    """

    currency: Optional[str] = None
    """Moeda do provento no exterior. Ex.: USD."""

    depositary_fee_percent: Optional[float] = FieldInfo(alias="depositaryFeePercent", default=None)
    """Taxa da instituição depositária, em % do provento."""

    final: Optional[bool] = None
    """`false` enquanto o valor é uma estimativa. `true` quando é o valor definitivo."""

    fx_date: Optional[str] = FieldInfo(alias="fxDate", default=None)
    """Data do câmbio (AAAA-MM-DD)."""

    fx_rate: Optional[float] = FieldInfo(alias="fxRate", default=None)
    """Câmbio usado na conversão para reais."""

    gross_brl_per_bdr: Optional[float] = FieldInfo(alias="grossBrlPerBdr", default=None)
    """Valor por BDR em reais, antes dos descontos no Brasil."""

    gross_per_bdr: Optional[float] = FieldInfo(alias="grossPerBdr", default=None)
    """Valor bruto por BDR, na moeda do provento."""

    gross_per_share: Optional[float] = FieldInfo(alias="grossPerShare", default=None)
    """Valor bruto por ação no exterior, na moeda do provento."""

    iof_percent: Optional[float] = FieldInfo(alias="iofPercent", default=None)
    """IOF sobre o câmbio, em %."""

    ratio: Optional[str] = None
    """Ações no exterior para BDRs. Ex.: "1:4" quando 1 ação equivale a 4 BDRs."""

    withholding_tax_percent: Optional[float] = FieldInfo(alias="withholdingTaxPercent", default=None)
    """Imposto retido no exterior, em %."""


class CashDividend(BaseModel):
    approved_on: Optional[str] = FieldInfo(alias="approvedOn", default=None)
    """Data de aprovação."""

    asset_issued: str = FieldInfo(alias="assetIssued")
    """Código ISIN do ativo que dá direito ao provento."""

    ex_date: Optional[str] = FieldInfo(alias="exDate", default=None)
    """Data ex, o primeiro dia sem direito ao provento. Pode ser nulo."""

    isin_code: str = FieldInfo(alias="isinCode")
    """Código ISIN."""

    label: str
    """Tipo do provento: DIVIDENDO ou JCP."""

    last_date_prior: Optional[str] = FieldInfo(alias="lastDatePrior", default=None)
    """Data-com, o último dia para comprar o ativo e ter direito ao provento."""

    payment_date: Optional[str] = FieldInfo(alias="paymentDate", default=None)
    """Data de pagamento."""

    payment_date_is_deadline: bool = FieldInfo(alias="paymentDateIsDeadline")
    """
    `true` quando a empresa informou só o prazo máximo do pagamento ("até
    31/12/2026"). Nesse caso, `paymentDate` é o prazo e muda quando a empresa
    divulgar a data.
    """

    rate: float
    """Valor por ação, em reais.

    Em BDRs, o valor líquido por BDR, já sem o imposto no exterior, o IOF e a taxa
    da instituição depositária.
    """

    related_to: str = FieldInfo(alias="relatedTo")
    """Período a que o provento se refere. Ex.: 1º Trimestre/2024."""

    remarks: str
    """Observações."""

    verified: bool
    """
    `true` quando o provento foi conferido em um documento publicado pela empresa ou
    pelo fundo. `false` quando vem de dados históricos que ainda não têm esse
    documento.
    """

    bdr: Optional[CashDividendBdr] = None
    """Só em BDRs: o provento no exterior e os descontos até chegar em `rate`.

    Campos não informados no aviso vêm nulos.
    """

    raw_rate: Optional[float] = FieldInfo(alias="rawRate", default=None)
    """Valor por ação na escala dos preços sem ajuste. Vem com `includeRaw=true`."""


class StockDividend(BaseModel):
    approved_on: Optional[str] = FieldInfo(alias="approvedOn", default=None)
    """Data de aprovação."""

    asset_issued: str = FieldInfo(alias="assetIssued")
    """Código ISIN do ativo que dá direito ao provento."""

    complete_factor: str = FieldInfo(alias="completeFactor")
    """Fator em texto. Ex.: 2 para 1."""

    ex_date: Optional[str] = FieldInfo(alias="exDate", default=None)
    """Data ex, o primeiro dia sem direito ao evento. Pode ser nulo."""

    factor: float
    """Fator do evento. Ex.: 2 em um desdobramento de 2 para 1."""

    isin_code: str = FieldInfo(alias="isinCode")
    """Código ISIN."""

    label: str
    """Tipo do evento: DESDOBRAMENTO, GRUPAMENTO ou BONIFICAÇÃO."""

    last_date_prior: Optional[str] = FieldInfo(alias="lastDatePrior", default=None)
    """Data-com, o último dia para comprar o ativo e ter direito ao evento."""

    remarks: str
    """Observações."""


class DividendsData(BaseModel):
    """Proventos.

    Na rota `/api/quote/{tickers}`, vem com `dividends=true`. Na rota `/api/v2/stocks/dividends`, não exige esse parâmetro.
    """

    cash_dividends: List[CashDividend] = FieldInfo(alias="cashDividends")
    """Dividendos e JCP pagos em dinheiro."""

    stock_dividends: List[StockDividend] = FieldInfo(alias="stockDividends")
    """Eventos em ações: desdobramentos, grupamentos e bonificações."""

    subscriptions: List[Optional[object]]
    """Direitos de subscrição."""
