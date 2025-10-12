# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["CurrencyListAvailableResponse", "Currency"]


class Currency(BaseModel):
    currency: Optional[str] = None
    """
    Nome da moeda ou par de moedas suportado (ex: `Dólar Americano/Real Brasileiro`,
    `Euro/Real Brasileiro`). A sigla pode ser extraída deste nome ou consultada em
    documentação adicional.
    """


class CurrencyListAvailableResponse(BaseModel):
    currencies: Optional[List[Currency]] = None
    """
    Lista de objetos, cada um contendo o nome de uma moeda fiduciária ou par
    suportado pela API.
    """
