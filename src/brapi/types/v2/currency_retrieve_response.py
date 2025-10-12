# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CurrencyRetrieveResponse", "Currency"]


class Currency(BaseModel):
    ask_price: str = FieldInfo(alias="askPrice")
    """
    **Preço de Venda (Ask):** Preço atual pelo qual o mercado está disposto a vender
    a moeda de origem (`fromCurrency`) recebendo a moeda de destino (`toCurrency`).
    Formato String.
    """

    bid_price: str = FieldInfo(alias="bidPrice")
    """
    **Preço de Compra (Bid):** Preço atual pelo qual o mercado está disposto a
    comprar a moeda de origem (`fromCurrency`) pagando com a moeda de destino
    (`toCurrency`). Formato String.
    """

    bid_variation: str = FieldInfo(alias="bidVariation")
    """
    **Variação Absoluta (Bid):** Mudança absoluta no preço de compra (bid) desde o
    último fechamento ou período de referência. Formato String.
    """

    from_currency: str = FieldInfo(alias="fromCurrency")
    """**Moeda de Origem:** Sigla da moeda base do par (ex: `USD` em `USD-BRL`)."""

    high: str
    """
    **Máxima:** Preço mais alto atingido pelo par no período recente (geralmente
    diário). Formato String.
    """

    low: str
    """
    **Mínima:** Preço mais baixo atingido pelo par no período recente (geralmente
    diário). Formato String.
    """

    name: str
    """
    **Nome do Par:** Nome descritivo do par de moedas (ex:
    `Dólar Americano/Real Brasileiro`).
    """

    percentage_change: str = FieldInfo(alias="percentageChange")
    """
    **Variação Percentual:** Mudança percentual no preço do par desde o último
    fechamento ou período de referência. Formato String.
    """

    to_currency: str = FieldInfo(alias="toCurrency")
    """
    **Moeda de Destino:** Sigla da moeda de cotação do par (ex: `BRL` em `USD-BRL`).
    """

    updated_at_date: str = FieldInfo(alias="updatedAtDate")
    """
    **Data da Atualização:** Data e hora da última atualização da cotação, formatada
    de forma legível (`YYYY-MM-DD HH:MM:SS`).
    """

    updated_at_timestamp: str = FieldInfo(alias="updatedAtTimestamp")
    """
    **Timestamp da Atualização:** Data e hora da última atualização da cotação,
    representada como um **timestamp UNIX** (string contendo o número de segundos
    desde 1970-01-01 UTC).
    """


class CurrencyRetrieveResponse(BaseModel):
    currency: List[Currency]
    """
    Array contendo os objetos `CurrencyQuote`, um para cada par de moeda válido
    solicitado no parâmetro `currency`.
    """
