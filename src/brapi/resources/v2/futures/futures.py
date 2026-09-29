# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.v2 import (
    future_list_params,
    future_quote_params,
    future_specs_params,
    future_historical_params,
    future_term_structure_params,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from .options.options import (
    OptionsResource,
    AsyncOptionsResource,
    OptionsResourceWithRawResponse,
    AsyncOptionsResourceWithRawResponse,
    OptionsResourceWithStreamingResponse,
    AsyncOptionsResourceWithStreamingResponse,
)
from ....types.v2.future_list_response import FutureListResponse
from ....types.v2.future_quote_response import FutureQuoteResponse
from ....types.v2.future_specs_response import FutureSpecsResponse
from ....types.v2.future_historical_response import FutureHistoricalResponse
from ....types.v2.future_term_structure_response import FutureTermStructureResponse

__all__ = ["FuturesResource", "AsyncFuturesResource"]


class FuturesResource(SyncAPIResource):
    @cached_property
    def options(self) -> OptionsResource:
        return OptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> FuturesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return FuturesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FuturesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return FuturesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        asset: str | Omit = omit,
        include_expired: Literal["true", "false"] | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        segment: Literal["financial", "agribusiness"] | Omit = omit,
        sort_by: Literal["symbol", "expirationDate", "underlyingAsset"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FutureListResponse:
        """Contratos futuros com vencimento, multiplicador, lote e ISIN, sem preço.

        Filtre
        por ativo, segmento e contratos vencidos.

        Use para achar o código exato de um contrato, listar os vencimentos de um ativo
        ou montar um seletor de contratos.

        Um ativo tem vários contratos ao mesmo tempo, um por vencimento. `WINJ26` e
        `WINM26` são o mesmo mini Ibovespa em meses diferentes. Veja como ler o código
        em [futuros](https://brapi.dev/docs/futuros).

        Por padrão, a lista traz só contratos com vencimento a partir de hoje. Plano
        Pro. Sem token, aceita só `asset=WIN` ou `asset=WDO`.

        Args:
          asset: Código do ativo. Ex.: `WIN`, `BGI`, `DI1`.

          include_expired: `true` inclui contratos vencidos.

          limit: Itens por página. Máximo: 100.

          page: Número da página, a partir de 1.

          segment: Segmento do contrato.

          sort_by: Campo usado na ordenação.

          sort_order: Direção da ordenação.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/futures/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asset": asset,
                        "include_expired": include_expired,
                        "limit": limit,
                        "page": page,
                        "segment": segment,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                    },
                    future_list_params.FutureListParams,
                ),
            ),
            cast_to=FutureListResponse,
        )

    def historical(
        self,
        *,
        symbol: str,
        end_date: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FutureHistoricalResponse:
        """
        Série diária de um contrato futuro: máxima, mínima, fechamento, preço de ajuste,
        taxa de ajuste em contratos de juros, variação e volume.

        Use para gráficos, backtests ou para estudar o ajuste diário de um vencimento.

        Sem `startDate`, a série começa 12 meses antes de hoje. Sem `endDate`, termina
        hoje. O histórico cobre cerca de 1 ano. `open` vem sempre `null`, porque os
        dados de fim de dia não trazem abertura.

        A série termina no vencimento do contrato. Para seguir um ativo por mais tempo,
        junte contratos seguidos e trate o salto de preço na troca. Para vários
        contratos, use a [cotação](https://brapi.dev/docs/futuros/cotacao) ou a
        [curva de vencimentos](https://brapi.dev/docs/futuros/curva-de-vencimentos).

        Plano Pro. Sem token, aceita só `symbol` que começa com `WIN` ou `WDO`.

        Args:
          symbol: Código do contrato. Ex.: `WINM26`.

          end_date: Data final no formato YYYY-MM-DD. Padrão: hoje.

          sort_order: Ordem das datas. `desc` traz o pregão mais recente primeiro.

          start_date: Data inicial no formato YYYY-MM-DD. Padrão: 12 meses antes de hoje.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/futures/historical",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "symbol": symbol,
                        "end_date": end_date,
                        "sort_order": sort_order,
                        "start_date": start_date,
                    },
                    future_historical_params.FutureHistoricalParams,
                ),
            ),
            cast_to=FutureHistoricalResponse,
        )

    def quote(
        self,
        *,
        symbols: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FutureQuoteResponse:
        """
        Dados do último pregão de até 20 contratos futuros: máxima, mínima, fechamento,
        preço de ajuste, variação e volume.

        Use para mostrar o ajuste do dia, marcar posições a mercado ou montar um painel
        de futuros.

        `settlement` é o preço de ajuste. A bolsa usa esse preço para acertar as
        posições todo dia. `close` é o último negócio. Em contrato com pouca negociação,
        `close`, `high` e `low` podem vir `null`, e `settlement` continua preenchido.

        Em contratos de juros, como DI1 e DAP (`quotationType=rate`), `close`, `high`,
        `low` e `average` vêm em % a.a. `settlement` vem em reais, e a taxa do ajuste
        fica em `settlementRate`.

        Os dados são de fim de dia. Código desconhecido fica fora de `quotes`. Plano
        Pro. Sem token, aceita só `symbols` que começam com `WIN` ou `WDO`.

        Args:
          symbols: Contratos separados por vírgula, até 20. Ex.: WINM26,DI1F27.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/futures/quote",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"symbols": symbols}, future_quote_params.FutureQuoteParams),
            ),
            cast_to=FutureQuoteResponse,
        )

    def specs(
        self,
        *,
        symbols: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FutureSpecsResponse:
        """
        Dados fixos de até 20 contratos futuros, sem preço: vencimento, primeiro e
        último pregão, multiplicador, lote, tipo de entrega, ISIN e código CFI.

        Use para calcular o valor financeiro de uma posição, conferir vencimentos ou
        cadastrar contratos no seu sistema.

        `contractMultiplier` converte pontos em reais. Exemplos: `WIN` vale 0,2 por
        ponto, `WDO` vale 10 e `BGI` vale 330. Para o preço do dia, use a
        [cotação de futuros](https://brapi.dev/docs/futuros/cotacao).

        Plano Pro. Sem token, aceita só `symbols` que começam com `WIN` ou `WDO`.

        Args:
          symbols: Contratos separados por vírgula, até 20. Ex.: WINM26,DI1F27.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/futures/specs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"symbols": symbols}, future_specs_params.FutureSpecsParams),
            ),
            cast_to=FutureSpecsResponse,
        )

    def term_structure(
        self,
        *,
        asset: str,
        include_expired: Literal["true", "false"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FutureTermStructureResponse:
        """
        Todos os contratos futuros de um ativo com vencimento a partir de hoje, do mais
        próximo ao mais distante, cada um com os dados do último pregão.

        Use para montar a curva de juros do DI, ver a curva de preço de commodities ou
        comparar vencimentos do mini Ibovespa.

        Em `DI1`, a taxa de cada prazo fica em `settlementRate`. Nos contratos cotados
        em preço, use `settlement`. Com `includeExpired=true`, a resposta inclui
        contratos vencidos.

        Ativos comuns: `DI1` (DI), `WIN` (mini Ibovespa), `WDO` (mini dólar), `BGI` (boi
        gordo), `ICF` (café), `CCM` (milho) e `SJC` (soja).

        Plano Pro. Sem token, aceita só `asset=WIN` ou `asset=WDO`.

        Args:
          asset: Código do ativo. Ex.: `DI1`, `WIN`, `BGI`.

          include_expired: `true` inclui contratos vencidos.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/futures/term-structure",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asset": asset,
                        "include_expired": include_expired,
                    },
                    future_term_structure_params.FutureTermStructureParams,
                ),
            ),
            cast_to=FutureTermStructureResponse,
        )


class AsyncFuturesResource(AsyncAPIResource):
    @cached_property
    def options(self) -> AsyncOptionsResource:
        return AsyncOptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFuturesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFuturesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFuturesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncFuturesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        asset: str | Omit = omit,
        include_expired: Literal["true", "false"] | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        segment: Literal["financial", "agribusiness"] | Omit = omit,
        sort_by: Literal["symbol", "expirationDate", "underlyingAsset"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FutureListResponse:
        """Contratos futuros com vencimento, multiplicador, lote e ISIN, sem preço.

        Filtre
        por ativo, segmento e contratos vencidos.

        Use para achar o código exato de um contrato, listar os vencimentos de um ativo
        ou montar um seletor de contratos.

        Um ativo tem vários contratos ao mesmo tempo, um por vencimento. `WINJ26` e
        `WINM26` são o mesmo mini Ibovespa em meses diferentes. Veja como ler o código
        em [futuros](https://brapi.dev/docs/futuros).

        Por padrão, a lista traz só contratos com vencimento a partir de hoje. Plano
        Pro. Sem token, aceita só `asset=WIN` ou `asset=WDO`.

        Args:
          asset: Código do ativo. Ex.: `WIN`, `BGI`, `DI1`.

          include_expired: `true` inclui contratos vencidos.

          limit: Itens por página. Máximo: 100.

          page: Número da página, a partir de 1.

          segment: Segmento do contrato.

          sort_by: Campo usado na ordenação.

          sort_order: Direção da ordenação.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/futures/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asset": asset,
                        "include_expired": include_expired,
                        "limit": limit,
                        "page": page,
                        "segment": segment,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                    },
                    future_list_params.FutureListParams,
                ),
            ),
            cast_to=FutureListResponse,
        )

    async def historical(
        self,
        *,
        symbol: str,
        end_date: str | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FutureHistoricalResponse:
        """
        Série diária de um contrato futuro: máxima, mínima, fechamento, preço de ajuste,
        taxa de ajuste em contratos de juros, variação e volume.

        Use para gráficos, backtests ou para estudar o ajuste diário de um vencimento.

        Sem `startDate`, a série começa 12 meses antes de hoje. Sem `endDate`, termina
        hoje. O histórico cobre cerca de 1 ano. `open` vem sempre `null`, porque os
        dados de fim de dia não trazem abertura.

        A série termina no vencimento do contrato. Para seguir um ativo por mais tempo,
        junte contratos seguidos e trate o salto de preço na troca. Para vários
        contratos, use a [cotação](https://brapi.dev/docs/futuros/cotacao) ou a
        [curva de vencimentos](https://brapi.dev/docs/futuros/curva-de-vencimentos).

        Plano Pro. Sem token, aceita só `symbol` que começa com `WIN` ou `WDO`.

        Args:
          symbol: Código do contrato. Ex.: `WINM26`.

          end_date: Data final no formato YYYY-MM-DD. Padrão: hoje.

          sort_order: Ordem das datas. `desc` traz o pregão mais recente primeiro.

          start_date: Data inicial no formato YYYY-MM-DD. Padrão: 12 meses antes de hoje.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/futures/historical",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "symbol": symbol,
                        "end_date": end_date,
                        "sort_order": sort_order,
                        "start_date": start_date,
                    },
                    future_historical_params.FutureHistoricalParams,
                ),
            ),
            cast_to=FutureHistoricalResponse,
        )

    async def quote(
        self,
        *,
        symbols: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FutureQuoteResponse:
        """
        Dados do último pregão de até 20 contratos futuros: máxima, mínima, fechamento,
        preço de ajuste, variação e volume.

        Use para mostrar o ajuste do dia, marcar posições a mercado ou montar um painel
        de futuros.

        `settlement` é o preço de ajuste. A bolsa usa esse preço para acertar as
        posições todo dia. `close` é o último negócio. Em contrato com pouca negociação,
        `close`, `high` e `low` podem vir `null`, e `settlement` continua preenchido.

        Em contratos de juros, como DI1 e DAP (`quotationType=rate`), `close`, `high`,
        `low` e `average` vêm em % a.a. `settlement` vem em reais, e a taxa do ajuste
        fica em `settlementRate`.

        Os dados são de fim de dia. Código desconhecido fica fora de `quotes`. Plano
        Pro. Sem token, aceita só `symbols` que começam com `WIN` ou `WDO`.

        Args:
          symbols: Contratos separados por vírgula, até 20. Ex.: WINM26,DI1F27.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/futures/quote",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"symbols": symbols}, future_quote_params.FutureQuoteParams),
            ),
            cast_to=FutureQuoteResponse,
        )

    async def specs(
        self,
        *,
        symbols: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FutureSpecsResponse:
        """
        Dados fixos de até 20 contratos futuros, sem preço: vencimento, primeiro e
        último pregão, multiplicador, lote, tipo de entrega, ISIN e código CFI.

        Use para calcular o valor financeiro de uma posição, conferir vencimentos ou
        cadastrar contratos no seu sistema.

        `contractMultiplier` converte pontos em reais. Exemplos: `WIN` vale 0,2 por
        ponto, `WDO` vale 10 e `BGI` vale 330. Para o preço do dia, use a
        [cotação de futuros](https://brapi.dev/docs/futuros/cotacao).

        Plano Pro. Sem token, aceita só `symbols` que começam com `WIN` ou `WDO`.

        Args:
          symbols: Contratos separados por vírgula, até 20. Ex.: WINM26,DI1F27.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/futures/specs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"symbols": symbols}, future_specs_params.FutureSpecsParams),
            ),
            cast_to=FutureSpecsResponse,
        )

    async def term_structure(
        self,
        *,
        asset: str,
        include_expired: Literal["true", "false"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FutureTermStructureResponse:
        """
        Todos os contratos futuros de um ativo com vencimento a partir de hoje, do mais
        próximo ao mais distante, cada um com os dados do último pregão.

        Use para montar a curva de juros do DI, ver a curva de preço de commodities ou
        comparar vencimentos do mini Ibovespa.

        Em `DI1`, a taxa de cada prazo fica em `settlementRate`. Nos contratos cotados
        em preço, use `settlement`. Com `includeExpired=true`, a resposta inclui
        contratos vencidos.

        Ativos comuns: `DI1` (DI), `WIN` (mini Ibovespa), `WDO` (mini dólar), `BGI` (boi
        gordo), `ICF` (café), `CCM` (milho) e `SJC` (soja).

        Plano Pro. Sem token, aceita só `asset=WIN` ou `asset=WDO`.

        Args:
          asset: Código do ativo. Ex.: `DI1`, `WIN`, `BGI`.

          include_expired: `true` inclui contratos vencidos.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/futures/term-structure",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "asset": asset,
                        "include_expired": include_expired,
                    },
                    future_term_structure_params.FutureTermStructureParams,
                ),
            ),
            cast_to=FutureTermStructureResponse,
        )


class FuturesResourceWithRawResponse:
    def __init__(self, futures: FuturesResource) -> None:
        self._futures = futures

        self.list = to_raw_response_wrapper(
            futures.list,
        )
        self.historical = to_raw_response_wrapper(
            futures.historical,
        )
        self.quote = to_raw_response_wrapper(
            futures.quote,
        )
        self.specs = to_raw_response_wrapper(
            futures.specs,
        )
        self.term_structure = to_raw_response_wrapper(
            futures.term_structure,
        )

    @cached_property
    def options(self) -> OptionsResourceWithRawResponse:
        return OptionsResourceWithRawResponse(self._futures.options)


class AsyncFuturesResourceWithRawResponse:
    def __init__(self, futures: AsyncFuturesResource) -> None:
        self._futures = futures

        self.list = async_to_raw_response_wrapper(
            futures.list,
        )
        self.historical = async_to_raw_response_wrapper(
            futures.historical,
        )
        self.quote = async_to_raw_response_wrapper(
            futures.quote,
        )
        self.specs = async_to_raw_response_wrapper(
            futures.specs,
        )
        self.term_structure = async_to_raw_response_wrapper(
            futures.term_structure,
        )

    @cached_property
    def options(self) -> AsyncOptionsResourceWithRawResponse:
        return AsyncOptionsResourceWithRawResponse(self._futures.options)


class FuturesResourceWithStreamingResponse:
    def __init__(self, futures: FuturesResource) -> None:
        self._futures = futures

        self.list = to_streamed_response_wrapper(
            futures.list,
        )
        self.historical = to_streamed_response_wrapper(
            futures.historical,
        )
        self.quote = to_streamed_response_wrapper(
            futures.quote,
        )
        self.specs = to_streamed_response_wrapper(
            futures.specs,
        )
        self.term_structure = to_streamed_response_wrapper(
            futures.term_structure,
        )

    @cached_property
    def options(self) -> OptionsResourceWithStreamingResponse:
        return OptionsResourceWithStreamingResponse(self._futures.options)


class AsyncFuturesResourceWithStreamingResponse:
    def __init__(self, futures: AsyncFuturesResource) -> None:
        self._futures = futures

        self.list = async_to_streamed_response_wrapper(
            futures.list,
        )
        self.historical = async_to_streamed_response_wrapper(
            futures.historical,
        )
        self.quote = async_to_streamed_response_wrapper(
            futures.quote,
        )
        self.specs = async_to_streamed_response_wrapper(
            futures.specs,
        )
        self.term_structure = async_to_streamed_response_wrapper(
            futures.term_structure,
        )

    @cached_property
    def options(self) -> AsyncOptionsResourceWithStreamingResponse:
        return AsyncOptionsResourceWithStreamingResponse(self._futures.options)
