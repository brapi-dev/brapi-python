# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CryptoRetrieveParams"]


class CryptoRetrieveParams(TypedDict, total=False):
    coin: Required[str]
    """
    **Obrigatório.** Uma ou mais siglas (tickers) de criptomoedas que você deseja
    consultar. Separe múltiplas siglas por vírgula (`,`).

    - **Exemplos:** `BTC`, `ETH,ADA`, `SOL`.
    """

    token: str
    """
    **Obrigatório caso não esteja adicionado como header "Authorization".** Seu
    token de autenticação pessoal da API Brapi.

    **Formas de Envio:**

    1.  **Query Parameter:** Adicione `?token=SEU_TOKEN` ao final da URL.
    2.  **HTTP Header:** Inclua o header `Authorization: Bearer SEU_TOKEN` na sua
        requisição.

    Ambos os métodos são aceitos, mas pelo menos um deles deve ser utilizado.
    Obtenha seu token em [brapi.dev/dashboard](https://brapi.dev/dashboard).
    """

    currency: str
    """
    **Opcional.** A sigla da moeda fiduciária na qual a cotação da(s) criptomoeda(s)
    deve ser retornada. Se omitido, o padrão é `BRL` (Real Brasileiro).
    """

    interval: Literal["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
    """
    **Opcional.** Define a granularidade (intervalo) dos dados históricos de preço
    (`historicalDataPrice`). Requer que `range` também seja especificado. Funciona
    de forma análoga ao endpoint de ações.

    - Valores: `1m`, `2m`, `5m`, `15m`, `30m`, `60m`, `90m`, `1h`, `1d`, `5d`,
      `1wk`, `1mo`, `3mo`.
    """

    range: Literal["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]
    """
    **Opcional.** Define o período para os dados históricos de preço
    (`historicalDataPrice`). Funciona de forma análoga ao endpoint de ações. Se
    omitido, apenas a cotação mais recente é retornada (a menos que `interval` seja
    usado).

    - Valores: `1d`, `5d`, `1mo`, `3mo`, `6mo`, `1y`, `2y`, `5y`, `10y`, `ytd`,
      `max`.
    """
