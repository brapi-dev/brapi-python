# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v2 import news_list_params, news_market_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v2.news_list_response import NewsListResponse
from ...types.v2.news_market_response import NewsMarketResponse
from ...types.v2.news_retrieve_response import NewsRetrieveResponse

__all__ = ["NewsResource", "AsyncNewsResource"]


class NewsResource(SyncAPIResource):
    """
    Notícias de empresas da B3 e do mercado, com resumo, sentimento, importância e ativos citados.
    """

    @cached_property
    def with_raw_response(self) -> NewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return NewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return NewsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewsRetrieveResponse:
        """
        Uma notícia pelo ID ou pelo slug, com a matéria completa em Markdown e até 6
        notícias relacionadas. Os títulos, resumos e matérias são escritos por
        inteligência artificial a partir das matérias listadas em `sources`. Cada
        notícia junta as matérias de vários veículos sobre o mesmo fato. Disponível no
        plano Pro.

        Args:
          id: ID (uuid) ou slug da notícia.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/api/v2/news/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NewsRetrieveResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        event_types: Literal[
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
        ]
        | Omit = omit,
        from_: str | Omit = omit,
        include_article: Literal["true", "false"] | Omit = omit,
        limit: int | Omit = omit,
        min_importance: int | Omit = omit,
        sentiment: Literal["positive", "negative", "neutral", "mixed"] | Omit = omit,
        tickers: str | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewsListResponse:
        """
        Notícias sobre empresas e ativos da B3: resultados, proventos, fusões,
        captações, recomendações e outros fatos. Os títulos, resumos e matérias são
        escritos por inteligência artificial a partir das matérias listadas em
        `sources`. Cada notícia junta as matérias de vários veículos sobre o mesmo fato.

        Use `tickers` para ver as notícias de ativos específicos. Um ticker de ação
        também traz as notícias das outras classes da mesma empresa. As notícias vêm da
        mais recente para a mais antiga. Para a próxima página, envie `nextCursor` no
        parâmetro `cursor`. Disponível no plano Pro.

        Args:
          cursor: Cursor da próxima página. Use o valor de `nextCursor` da resposta anterior, com
              os mesmos filtros.

          event_types: Tipos de evento separados por vírgula: `earnings` (resultados), `dividends`
              (proventos), `guidance` (projeções), `mna` (fusões e aquisições), `financing`
              (captações e dívida), `buyback` (recompra), `rating` (nota de crédito),
              `analyst` (recomendações), `management` (gestão), `legal_regulatory` (jurídico e
              regulação), `operations` (operações), `market_move` (movimento de mercado),
              `macro` (macroeconomia), `other` (outros).

          from_: Publicadas a partir desta data (`YYYY-MM-DD`) ou data e hora ISO 8601. Sem fuso,
              vale o horário de Brasília.

          include_article:
              `true` inclui a matéria completa em Markdown no campo `article`. Padrão:
              `false`.

          limit: Máximo de notícias por página. Padrão: 20.

          min_importance: Importância mínima, de 1 (pequena) a 5 (move o mercado). Padrão: 1.

          sentiment: Sentimento da notícia, separado por vírgula: `positive`, `negative`, `neutral`
              ou `mixed`.

          tickers: Tickers separados por vírgula. Máximo de 20. Um ticker de ação também traz as
              notícias das outras classes da mesma empresa (PETR4 inclui PETR3). Sem
              `tickers`, traz notícias de todas as empresas.

          to: Publicadas até esta data (inclui o dia inteiro) ou até esta data e hora
              ISO 8601. Sem fuso, vale o horário de Brasília.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/news",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "event_types": event_types,
                        "from_": from_,
                        "include_article": include_article,
                        "limit": limit,
                        "min_importance": min_importance,
                        "sentiment": sentiment,
                        "tickers": tickers,
                        "to": to,
                    },
                    news_list_params.NewsListParams,
                ),
            ),
            cast_to=NewsListResponse,
        )

    def market(
        self,
        *,
        cursor: str | Omit = omit,
        event_types: Literal[
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
        ]
        | Omit = omit,
        from_: str | Omit = omit,
        include_article: Literal["true", "false"] | Omit = omit,
        limit: int | Omit = omit,
        min_importance: int | Omit = omit,
        sentiment: Literal["positive", "negative", "neutral", "mixed"] | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewsMarketResponse:
        """
        Notícias de economia e mercado: juros, Selic, inflação, câmbio, contas públicas,
        política e o Ibovespa, no Brasil e na América Latina. Os títulos, resumos e
        matérias são escritos por inteligência artificial a partir das matérias listadas
        em `sources`. Cada notícia junta as matérias de vários veículos sobre o mesmo
        fato.

        As notícias vêm da mais recente para a mais antiga. Para a próxima página, envie
        `nextCursor` no parâmetro `cursor`. Disponível no plano Pro.

        Args:
          cursor: Cursor da próxima página. Use o valor de `nextCursor` da resposta anterior, com
              os mesmos filtros.

          event_types: Tipos de evento separados por vírgula: `earnings` (resultados), `dividends`
              (proventos), `guidance` (projeções), `mna` (fusões e aquisições), `financing`
              (captações e dívida), `buyback` (recompra), `rating` (nota de crédito),
              `analyst` (recomendações), `management` (gestão), `legal_regulatory` (jurídico e
              regulação), `operations` (operações), `market_move` (movimento de mercado),
              `macro` (macroeconomia), `other` (outros).

          from_: Publicadas a partir desta data (`YYYY-MM-DD`) ou data e hora ISO 8601. Sem fuso,
              vale o horário de Brasília.

          include_article:
              `true` inclui a matéria completa em Markdown no campo `article`. Padrão:
              `false`.

          limit: Máximo de notícias por página. Padrão: 20.

          min_importance: Importância mínima, de 1 (pequena) a 5 (move o mercado). Padrão: 1.

          sentiment: Sentimento da notícia, separado por vírgula: `positive`, `negative`, `neutral`
              ou `mixed`.

          to: Publicadas até esta data (inclui o dia inteiro) ou até esta data e hora
              ISO 8601. Sem fuso, vale o horário de Brasília.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/news/market",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "event_types": event_types,
                        "from_": from_,
                        "include_article": include_article,
                        "limit": limit,
                        "min_importance": min_importance,
                        "sentiment": sentiment,
                        "to": to,
                    },
                    news_market_params.NewsMarketParams,
                ),
            ),
            cast_to=NewsMarketResponse,
        )


class AsyncNewsResource(AsyncAPIResource):
    """
    Notícias de empresas da B3 e do mercado, com resumo, sentimento, importância e ativos citados.
    """

    @cached_property
    def with_raw_response(self) -> AsyncNewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncNewsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewsRetrieveResponse:
        """
        Uma notícia pelo ID ou pelo slug, com a matéria completa em Markdown e até 6
        notícias relacionadas. Os títulos, resumos e matérias são escritos por
        inteligência artificial a partir das matérias listadas em `sources`. Cada
        notícia junta as matérias de vários veículos sobre o mesmo fato. Disponível no
        plano Pro.

        Args:
          id: ID (uuid) ou slug da notícia.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/api/v2/news/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NewsRetrieveResponse,
        )

    async def list(
        self,
        *,
        cursor: str | Omit = omit,
        event_types: Literal[
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
        ]
        | Omit = omit,
        from_: str | Omit = omit,
        include_article: Literal["true", "false"] | Omit = omit,
        limit: int | Omit = omit,
        min_importance: int | Omit = omit,
        sentiment: Literal["positive", "negative", "neutral", "mixed"] | Omit = omit,
        tickers: str | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewsListResponse:
        """
        Notícias sobre empresas e ativos da B3: resultados, proventos, fusões,
        captações, recomendações e outros fatos. Os títulos, resumos e matérias são
        escritos por inteligência artificial a partir das matérias listadas em
        `sources`. Cada notícia junta as matérias de vários veículos sobre o mesmo fato.

        Use `tickers` para ver as notícias de ativos específicos. Um ticker de ação
        também traz as notícias das outras classes da mesma empresa. As notícias vêm da
        mais recente para a mais antiga. Para a próxima página, envie `nextCursor` no
        parâmetro `cursor`. Disponível no plano Pro.

        Args:
          cursor: Cursor da próxima página. Use o valor de `nextCursor` da resposta anterior, com
              os mesmos filtros.

          event_types: Tipos de evento separados por vírgula: `earnings` (resultados), `dividends`
              (proventos), `guidance` (projeções), `mna` (fusões e aquisições), `financing`
              (captações e dívida), `buyback` (recompra), `rating` (nota de crédito),
              `analyst` (recomendações), `management` (gestão), `legal_regulatory` (jurídico e
              regulação), `operations` (operações), `market_move` (movimento de mercado),
              `macro` (macroeconomia), `other` (outros).

          from_: Publicadas a partir desta data (`YYYY-MM-DD`) ou data e hora ISO 8601. Sem fuso,
              vale o horário de Brasília.

          include_article:
              `true` inclui a matéria completa em Markdown no campo `article`. Padrão:
              `false`.

          limit: Máximo de notícias por página. Padrão: 20.

          min_importance: Importância mínima, de 1 (pequena) a 5 (move o mercado). Padrão: 1.

          sentiment: Sentimento da notícia, separado por vírgula: `positive`, `negative`, `neutral`
              ou `mixed`.

          tickers: Tickers separados por vírgula. Máximo de 20. Um ticker de ação também traz as
              notícias das outras classes da mesma empresa (PETR4 inclui PETR3). Sem
              `tickers`, traz notícias de todas as empresas.

          to: Publicadas até esta data (inclui o dia inteiro) ou até esta data e hora
              ISO 8601. Sem fuso, vale o horário de Brasília.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/news",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "event_types": event_types,
                        "from_": from_,
                        "include_article": include_article,
                        "limit": limit,
                        "min_importance": min_importance,
                        "sentiment": sentiment,
                        "tickers": tickers,
                        "to": to,
                    },
                    news_list_params.NewsListParams,
                ),
            ),
            cast_to=NewsListResponse,
        )

    async def market(
        self,
        *,
        cursor: str | Omit = omit,
        event_types: Literal[
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
        ]
        | Omit = omit,
        from_: str | Omit = omit,
        include_article: Literal["true", "false"] | Omit = omit,
        limit: int | Omit = omit,
        min_importance: int | Omit = omit,
        sentiment: Literal["positive", "negative", "neutral", "mixed"] | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NewsMarketResponse:
        """
        Notícias de economia e mercado: juros, Selic, inflação, câmbio, contas públicas,
        política e o Ibovespa, no Brasil e na América Latina. Os títulos, resumos e
        matérias são escritos por inteligência artificial a partir das matérias listadas
        em `sources`. Cada notícia junta as matérias de vários veículos sobre o mesmo
        fato.

        As notícias vêm da mais recente para a mais antiga. Para a próxima página, envie
        `nextCursor` no parâmetro `cursor`. Disponível no plano Pro.

        Args:
          cursor: Cursor da próxima página. Use o valor de `nextCursor` da resposta anterior, com
              os mesmos filtros.

          event_types: Tipos de evento separados por vírgula: `earnings` (resultados), `dividends`
              (proventos), `guidance` (projeções), `mna` (fusões e aquisições), `financing`
              (captações e dívida), `buyback` (recompra), `rating` (nota de crédito),
              `analyst` (recomendações), `management` (gestão), `legal_regulatory` (jurídico e
              regulação), `operations` (operações), `market_move` (movimento de mercado),
              `macro` (macroeconomia), `other` (outros).

          from_: Publicadas a partir desta data (`YYYY-MM-DD`) ou data e hora ISO 8601. Sem fuso,
              vale o horário de Brasília.

          include_article:
              `true` inclui a matéria completa em Markdown no campo `article`. Padrão:
              `false`.

          limit: Máximo de notícias por página. Padrão: 20.

          min_importance: Importância mínima, de 1 (pequena) a 5 (move o mercado). Padrão: 1.

          sentiment: Sentimento da notícia, separado por vírgula: `positive`, `negative`, `neutral`
              ou `mixed`.

          to: Publicadas até esta data (inclui o dia inteiro) ou até esta data e hora
              ISO 8601. Sem fuso, vale o horário de Brasília.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/news/market",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "event_types": event_types,
                        "from_": from_,
                        "include_article": include_article,
                        "limit": limit,
                        "min_importance": min_importance,
                        "sentiment": sentiment,
                        "to": to,
                    },
                    news_market_params.NewsMarketParams,
                ),
            ),
            cast_to=NewsMarketResponse,
        )


class NewsResourceWithRawResponse:
    def __init__(self, news: NewsResource) -> None:
        self._news = news

        self.retrieve = to_raw_response_wrapper(
            news.retrieve,
        )
        self.list = to_raw_response_wrapper(
            news.list,
        )
        self.market = to_raw_response_wrapper(
            news.market,
        )


class AsyncNewsResourceWithRawResponse:
    def __init__(self, news: AsyncNewsResource) -> None:
        self._news = news

        self.retrieve = async_to_raw_response_wrapper(
            news.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            news.list,
        )
        self.market = async_to_raw_response_wrapper(
            news.market,
        )


class NewsResourceWithStreamingResponse:
    def __init__(self, news: NewsResource) -> None:
        self._news = news

        self.retrieve = to_streamed_response_wrapper(
            news.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            news.list,
        )
        self.market = to_streamed_response_wrapper(
            news.market,
        )


class AsyncNewsResourceWithStreamingResponse:
    def __init__(self, news: AsyncNewsResource) -> None:
        self._news = news

        self.retrieve = async_to_streamed_response_wrapper(
            news.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            news.list,
        )
        self.market = async_to_streamed_response_wrapper(
            news.market,
        )
