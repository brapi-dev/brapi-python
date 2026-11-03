# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .debenture import Debenture

__all__ = ["DebentureProfile", "DebentureProfileAgents", "DebentureProfileAmortization", "DebentureProfileInterest"]


class DebentureProfileAgents(BaseModel):
    depositary: Optional[str] = None
    """Instituição depositária."""

    lead_underwriter: Optional[str] = FieldInfo(alias="leadUnderwriter", default=None)
    """Coordenador líder."""

    payment_agent: Optional[str] = FieldInfo(alias="paymentAgent", default=None)
    """Banco mandatário."""

    trustee: Optional[str] = None
    """Agente fiduciário."""


class DebentureProfileAmortization(BaseModel):
    """Amortização. Campos nulos quando o valor é pago no vencimento."""

    every: Optional[int] = None
    """Intervalo entre os pagamentos."""

    method: Optional[str] = None
    """Forma de amortização, como no registro."""

    percent: Optional[float] = None
    """Percentual amortizado em cada pagamento."""

    unit: Optional[Literal["month", "day"]] = None
    """Unidade do intervalo."""


class DebentureProfileInterest(BaseModel):
    """Pagamento de juros."""

    day_count: Optional[int] = FieldInfo(alias="dayCount", default=None)
    """Base de dias por ano: 252 (dias úteis), 360 ou 365."""

    every: Optional[int] = None
    """Intervalo entre os pagamentos."""

    unit: Optional[Literal["month", "day"]] = None
    """Unidade do intervalo."""


class DebentureProfile(Debenture):
    agents: DebentureProfileAgents

    amortization: DebentureProfileAmortization
    """Amortização. Campos nulos quando o valor é pago no vencimento."""

    cvm_registration: Optional[str] = FieldInfo(alias="cvmRegistration", default=None)
    """Registro da oferta na CVM, ou o tipo de dispensa de registro."""

    cvm_registration_date: Optional[str] = FieldInfo(alias="cvmRegistrationDate", default=None)
    """Data do registro na CVM."""

    early_redemption_allowed: Optional[bool] = FieldInfo(alias="earlyRedemptionAllowed", default=None)
    """A escritura permite resgate antecipado pela empresa."""

    interest: DebentureProfileInterest
    """Pagamento de juros."""

    profitability_start_date: Optional[str] = FieldInfo(alias="profitabilityStartDate", default=None)
    """Data de início da rentabilidade."""

    quantity_cancelled: Optional[float] = FieldInfo(alias="quantityCancelled", default=None)
    """Quantidade cancelada."""

    quantity_in_treasury: Optional[float] = FieldInfo(alias="quantityInTreasury", default=None)
    """Quantidade na tesouraria da empresa."""

    quantity_redeemed: Optional[float] = FieldInfo(alias="quantityRedeemed", default=None)
    """Quantidade resgatada."""
