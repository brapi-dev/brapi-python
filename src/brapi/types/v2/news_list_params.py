# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["NewsListParams"]


class NewsListParams(TypedDict, total=False):
    cursor: str
    """Cursor da próxima página.

    Use o valor de `nextCursor` da resposta anterior, com os mesmos filtros.
    """

    event_types: Annotated[
        Literal[
            "earnings",
            "dividends",
            "guidance",
            "mna",
            "financing",
            "buyback",
            "rating",
            "analyst",
            "management",
            "legal_regulatory",
            "operations",
            "market_move",
            "macro",
            "other",
        ],
        PropertyInfo(alias="eventTypes"),
    ]
    """
    Tipos de evento separados por vírgula: `earnings` (resultados), `dividends`
    (proventos), `guidance` (projeções), `mna` (fusões e aquisições), `financing`
    (captações e dívida), `buyback` (recompra), `rating` (nota de crédito),
    `analyst` (recomendações), `management` (gestão), `legal_regulatory` (jurídico e
    regulação), `operations` (operações), `market_move` (movimento de mercado),
    `macro` (macroeconomia), `other` (outros).
    """

    from_: Annotated[str, PropertyInfo(alias="from")]
    """Publicadas a partir desta data (`YYYY-MM-DD`) ou data e hora ISO 8601.

    Sem fuso, vale o horário de Brasília.
    """

    include_article: Annotated[Literal["true", "false"], PropertyInfo(alias="includeArticle")]
    """`true` inclui a matéria completa em Markdown no campo `article`.

    Padrão: `false`.
    """

    limit: int
    """Máximo de notícias por página. Padrão: 20."""

    min_importance: Annotated[int, PropertyInfo(alias="minImportance")]
    """Importância mínima, de 1 (pequena) a 5 (move o mercado). Padrão: 1."""

    sentiment: Literal["positive", "negative", "neutral", "mixed"]
    """
    Sentimento da notícia, separado por vírgula: `positive`, `negative`, `neutral`
    ou `mixed`.
    """

    tickers: str
    """Tickers separados por vírgula.

    Máximo de 20. Um ticker de ação também traz as notícias das outras classes da
    mesma empresa (PETR4 inclui PETR3). Sem `tickers`, traz notícias de todas as
    empresas.
    """

    to: str
    """Publicadas até esta data (inclui o dia inteiro) ou até esta data e hora
    ISO 8601.

    Sem fuso, vale o horário de Brasília.
    """
