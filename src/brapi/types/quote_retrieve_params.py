# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["QuoteRetrieveParams"]


class QuoteRetrieveParams(TypedDict, total=False):
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

    dividends: bool
    """**Opcional.** Booleano (`true` ou `false`).

    Se `true`, inclui informações sobre dividendos e JCP (Juros sobre Capital
    Próprio) pagos historicamente pelo ativo na chave `dividendsData`.
    """

    fundamental: bool
    """**Opcional.** Booleano (`true` ou `false`).

    Se `true`, inclui dados fundamentalistas básicos na resposta, como Preço/Lucro
    (P/L) e Lucro Por Ação (LPA).

    **Nota:** Para dados fundamentalistas mais completos, utilize o parâmetro
    `modules`.
    """

    interval: Literal["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
    """
    **Opcional.** Define a granularidade (intervalo) dos dados históricos de preço
    (`historicalDataPrice`). Requer que `range` também seja especificado.

    **Valores Possíveis:**

    - `1m`, `2m`, `5m`, `15m`, `30m`, `60m`, `90m`, `1h`: Intervalos intraday
      (minutos/horas). **Atenção:** Disponibilidade pode variar conforme o `range` e
      o ativo.
    - `1d`: Diário (padrão se `range` for especificado e `interval` omitido).
    - `5d`: 5 dias.
    - `1wk`: Semanal.
    - `1mo`: Mensal.
    - `3mo`: Trimestral.
    """

    modules: List[
        Literal[
            "summaryProfile",
            "balanceSheetHistory",
            "defaultKeyStatistics",
            "balanceSheetHistoryQuarterly",
            "incomeStatementHistory",
            "incomeStatementHistoryQuarterly",
            "financialData",
            "financialDataHistory",
            "financialDataHistoryQuarterly",
            "defaultKeyStatisticsHistory",
            "defaultKeyStatisticsHistoryQuarterly",
            "valueAddedHistory",
            "valueAddedHistoryQuarterly",
            "cashflowHistory",
            "cashflowHistoryQuarterly",
        ]
    ]
    """
    **Opcional.** Uma lista de módulos de dados adicionais, separados por vírgula
    (`,`), para incluir na resposta. Permite buscar dados financeiros detalhados.

    **Exemplos:**

    - `modules=summaryProfile` (retorna perfil da empresa)
    - `modules=balanceSheetHistory,incomeStatementHistory` (retorna histórico anual
      do BP e DRE)

    Veja a descrição principal do endpoint para a lista completa de módulos e seus
    conteúdos.
    """

    range: Literal["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]
    """
    **Opcional.** Define o período para os dados históricos de preço
    (`historicalDataPrice`). Se omitido, apenas a cotação mais recente é retornada
    (a menos que `interval` seja usado).

    **Valores Possíveis:**

    - `1d`: Último dia de pregão (intraday se `interval` for minutos/horas).
    - `5d`: Últimos 5 dias.
    - `1mo`: Último mês.
    - `3mo`: Últimos 3 meses.
    - `6mo`: Últimos 6 meses.
    - `1y`: Último ano.
    - `2y`: Últimos 2 anos.
    - `5y`: Últimos 5 anos.
    - `10y`: Últimos 10 anos.
    - `ytd`: Desde o início do ano atual (Year-to-Date).
    - `max`: Todo o período histórico disponível.
    """
