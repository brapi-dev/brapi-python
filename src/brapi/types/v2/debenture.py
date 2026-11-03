# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Debenture"]


class Debenture(BaseModel):
    guarantee: Optional[str] = None
    """Garantia: Quirografária, Real, Subordinada ou Flutuante, como no registro."""

    incentivized: Optional[bool] = None
    """Debênture incentivada (Lei 12.431), com benefício de imposto de renda."""

    index: Optional[str] = None
    """
    Indexador: `di`, `ipca`, `pre` (prefixado), `igp-m`, `inpc`, `tr`, `usd`, `eur`
    ou `none`.
    """

    index_percent: Optional[float] = FieldInfo(alias="indexPercent", default=None)
    """Percentual do indexador. Ex.: 110 para 110% do DI."""

    interest_rate: Optional[float] = FieldInfo(alias="interestRate", default=None)
    """Taxa de juros em % ao ano, além do indexador. Ex.: IPCA + 3,9182%."""

    isin: Optional[str] = None

    issue_date: Optional[str] = FieldInfo(alias="issueDate", default=None)

    issue_number: Optional[str] = FieldInfo(alias="issueNumber", default=None)
    """Número da emissão da empresa."""

    issuer_cnpj: str = FieldInfo(alias="issuerCnpj")
    """CNPJ da empresa emissora."""

    issuer_name: str = FieldInfo(alias="issuerName")

    maturity_date: Optional[str] = FieldInfo(alias="maturityDate", default=None)
    """Data de vencimento, já com prorrogações."""

    nominal_value: Optional[float] = FieldInfo(alias="nominalValue", default=None)
    """Valor nominal unitário atualizado, em reais, já descontadas as amortizações."""

    nominal_value_at_issue: Optional[float] = FieldInfo(alias="nominalValueAtIssue", default=None)
    """Valor nominal unitário na emissão, em reais."""

    nominal_value_date: Optional[str] = FieldInfo(alias="nominalValueDate", default=None)
    """Data do valor nominal atualizado."""

    quantity_issued: Optional[float] = FieldInfo(alias="quantityIssued", default=None)

    quantity_outstanding: Optional[float] = FieldInfo(alias="quantityOutstanding", default=None)
    """Quantidade em circulação no mercado."""

    removed_date: Optional[str] = FieldInfo(alias="removedDate", default=None)
    """Data de saída de circulação."""

    removed_reason: Optional[
        Literal["matured", "accelerated", "early-redemption", "cancelled", "converted", "other"]
    ] = FieldInfo(alias="removedReason", default=None)
    """
    Motivo da saída: `matured` (vencimento), `accelerated` (vencimento antecipado),
    `early-redemption` (resgate antecipado), `cancelled` (cancelamento), `converted`
    (conversão em ações) ou `other`.
    """

    series: Optional[str] = None
    """Série. `UNI` quando a emissão tem série única."""

    status: Literal["active", "inactive"]
    """`active` quando a debênture está em circulação e não venceu.

    `inactive` nos demais casos.
    """

    symbol: str
    """Código da debênture."""
