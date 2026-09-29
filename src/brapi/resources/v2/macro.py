# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v2 import macro_latest_params, macro_retrieve_params, macro_list_available_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v2.macro_latest_response import MacroLatestResponse
from ...types.v2.macro_retrieve_response import MacroRetrieveResponse
from ...types.v2.macro_list_available_response import MacroListAvailableResponse

__all__ = ["MacroResource", "AsyncMacroResource"]


class MacroResource(SyncAPIResource):
    """
    Acompanhe os principais indicadores macroeconômicos do Brasil, incluindo inflação (IPCA, IGP-M), Taxa Selic, agregados monetários e atividade.
    """

    @cached_property
    def with_raw_response(self) -> MacroResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return MacroResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MacroResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return MacroResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        symbols: str,
        end_date: str | Omit = omit,
        limit: int | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MacroRetrieveResponse:
        """
        Histórico de indicadores macroeconômicos do Brasil, como Selic, CDI, IPCA,
        IGP-M, agregados monetários, atividade, emprego e setor externo. Cada série tem
        um slug.

        Use para gráficos de juros e inflação, modelos de renda fixa e análise de
        cenário.

        Peça até 20 séries por chamada em `symbols`, como `symbols=selic,ipca`. Sem
        datas, a janela é dos últimos 12 meses. `limit` corta os pontos de cada série e
        tem padrão 20. Com o padrão, uma série diária não cobre os 12 meses. Aumente
        `limit` para ver a janela toda.

        As séries têm frequências diferentes: a Selic e o CDI são diários, o IPCA e o
        PIB mensal são mensais. Leia `series.frequency` antes de juntar duas séries.

        Um alias no lugar do slug funciona e gera um aviso em `warnings`. Um slug
        desconhecido gera um item em `errors` e não derruba as outras séries. Pares de
        câmbio ficam no [histórico de câmbio](https://brapi.dev/docs/moedas/historico).

        Veja os slugs em [listar séries](https://brapi.dev/docs/macro/available). Planos
        Startup e Pro.

        Args:
          symbols: Slugs separados por vírgula, até 20. Slugs por categoria: interestRate: `selic`,
              `selicovernight`, `cdi`, `tr`; inflation: `ipca`, `ipca12m`, `inpc`, `igpm`,
              `igpdi`; activity: `ibcbr`, `pibmensal`; labor: `desemprego`; monetary: `m1`,
              `m4`; external: `reservas`.

          end_date: Data final no formato YYYY-MM-DD. Padrão: hoje.

          limit: Máximo de observações por série. Padrão: 20. Não há teto.

          sort_order: Ordem por data.

          start_date: Data inicial no formato YYYY-MM-DD. Padrão: 12 meses atrás.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/macro",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "symbols": symbols,
                        "end_date": end_date,
                        "limit": limit,
                        "sort_order": sort_order,
                        "start_date": start_date,
                    },
                    macro_retrieve_params.MacroRetrieveParams,
                ),
            ),
            cast_to=MacroRetrieveResponse,
        )

    def latest(
        self,
        *,
        symbols: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MacroLatestResponse:
        """O valor mais recente de cada série macroeconômica pedida em `symbols`.

        Sem
        `symbols`, devolve todas as séries.

        Use para painéis com Selic, CDI e IPCA atuais sem baixar o histórico.

        A data de cada valor segue a frequência da série. O IPCA mais recente pode ser
        de um mês atrás e a Selic de ontem. `latest` é nulo quando a série não tem
        dados.

        Planos Startup e Pro.

        Args:
          symbols:
              Slugs separados por vírgula, até 20. Sem valor, devolve todas as séries. Slugs:
              selic, selicovernight, cdi, tr, ipca, ipca12m, inpc, igpm, igpdi, ibcbr,
              pibmensal, desemprego, m1, m4, reservas.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/macro/latest",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"symbols": symbols}, macro_latest_params.MacroLatestParams),
            ),
            cast_to=MacroLatestResponse,
        )

    def list_available(
        self,
        *,
        category: str | Omit = omit,
        q: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MacroListAvailableResponse:
        """
        Lista as séries macroeconômicas com slug, nome, descrição, unidade, frequência,
        categoria e data de início do histórico.

        Use para achar o slug antes de chamar as
        [séries macroeconômicas](https://brapi.dev/docs/macro) ou o
        [último valor](https://brapi.dev/docs/macro/latest).

        `q` e `category` funcionam juntos. Endpoint público, sem token.

        Args:
          category: Categoria da série: `interestRate`, `inflation`, `monetary`, `activity`,
              `labor`, `external`.

          q: Texto buscado em slug, alias, nome e descrição. Ignora maiúsculas e aceita parte
              da palavra.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/macro/available",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "category": category,
                        "q": q,
                    },
                    macro_list_available_params.MacroListAvailableParams,
                ),
            ),
            cast_to=MacroListAvailableResponse,
        )


class AsyncMacroResource(AsyncAPIResource):
    """
    Acompanhe os principais indicadores macroeconômicos do Brasil, incluindo inflação (IPCA, IGP-M), Taxa Selic, agregados monetários e atividade.
    """

    @cached_property
    def with_raw_response(self) -> AsyncMacroResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMacroResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMacroResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncMacroResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        symbols: str,
        end_date: str | Omit = omit,
        limit: int | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MacroRetrieveResponse:
        """
        Histórico de indicadores macroeconômicos do Brasil, como Selic, CDI, IPCA,
        IGP-M, agregados monetários, atividade, emprego e setor externo. Cada série tem
        um slug.

        Use para gráficos de juros e inflação, modelos de renda fixa e análise de
        cenário.

        Peça até 20 séries por chamada em `symbols`, como `symbols=selic,ipca`. Sem
        datas, a janela é dos últimos 12 meses. `limit` corta os pontos de cada série e
        tem padrão 20. Com o padrão, uma série diária não cobre os 12 meses. Aumente
        `limit` para ver a janela toda.

        As séries têm frequências diferentes: a Selic e o CDI são diários, o IPCA e o
        PIB mensal são mensais. Leia `series.frequency` antes de juntar duas séries.

        Um alias no lugar do slug funciona e gera um aviso em `warnings`. Um slug
        desconhecido gera um item em `errors` e não derruba as outras séries. Pares de
        câmbio ficam no [histórico de câmbio](https://brapi.dev/docs/moedas/historico).

        Veja os slugs em [listar séries](https://brapi.dev/docs/macro/available). Planos
        Startup e Pro.

        Args:
          symbols: Slugs separados por vírgula, até 20. Slugs por categoria: interestRate: `selic`,
              `selicovernight`, `cdi`, `tr`; inflation: `ipca`, `ipca12m`, `inpc`, `igpm`,
              `igpdi`; activity: `ibcbr`, `pibmensal`; labor: `desemprego`; monetary: `m1`,
              `m4`; external: `reservas`.

          end_date: Data final no formato YYYY-MM-DD. Padrão: hoje.

          limit: Máximo de observações por série. Padrão: 20. Não há teto.

          sort_order: Ordem por data.

          start_date: Data inicial no formato YYYY-MM-DD. Padrão: 12 meses atrás.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/macro",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "symbols": symbols,
                        "end_date": end_date,
                        "limit": limit,
                        "sort_order": sort_order,
                        "start_date": start_date,
                    },
                    macro_retrieve_params.MacroRetrieveParams,
                ),
            ),
            cast_to=MacroRetrieveResponse,
        )

    async def latest(
        self,
        *,
        symbols: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MacroLatestResponse:
        """O valor mais recente de cada série macroeconômica pedida em `symbols`.

        Sem
        `symbols`, devolve todas as séries.

        Use para painéis com Selic, CDI e IPCA atuais sem baixar o histórico.

        A data de cada valor segue a frequência da série. O IPCA mais recente pode ser
        de um mês atrás e a Selic de ontem. `latest` é nulo quando a série não tem
        dados.

        Planos Startup e Pro.

        Args:
          symbols:
              Slugs separados por vírgula, até 20. Sem valor, devolve todas as séries. Slugs:
              selic, selicovernight, cdi, tr, ipca, ipca12m, inpc, igpm, igpdi, ibcbr,
              pibmensal, desemprego, m1, m4, reservas.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/macro/latest",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"symbols": symbols}, macro_latest_params.MacroLatestParams),
            ),
            cast_to=MacroLatestResponse,
        )

    async def list_available(
        self,
        *,
        category: str | Omit = omit,
        q: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MacroListAvailableResponse:
        """
        Lista as séries macroeconômicas com slug, nome, descrição, unidade, frequência,
        categoria e data de início do histórico.

        Use para achar o slug antes de chamar as
        [séries macroeconômicas](https://brapi.dev/docs/macro) ou o
        [último valor](https://brapi.dev/docs/macro/latest).

        `q` e `category` funcionam juntos. Endpoint público, sem token.

        Args:
          category: Categoria da série: `interestRate`, `inflation`, `monetary`, `activity`,
              `labor`, `external`.

          q: Texto buscado em slug, alias, nome e descrição. Ignora maiúsculas e aceita parte
              da palavra.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/macro/available",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "category": category,
                        "q": q,
                    },
                    macro_list_available_params.MacroListAvailableParams,
                ),
            ),
            cast_to=MacroListAvailableResponse,
        )


class MacroResourceWithRawResponse:
    def __init__(self, macro: MacroResource) -> None:
        self._macro = macro

        self.retrieve = to_raw_response_wrapper(
            macro.retrieve,
        )
        self.latest = to_raw_response_wrapper(
            macro.latest,
        )
        self.list_available = to_raw_response_wrapper(
            macro.list_available,
        )


class AsyncMacroResourceWithRawResponse:
    def __init__(self, macro: AsyncMacroResource) -> None:
        self._macro = macro

        self.retrieve = async_to_raw_response_wrapper(
            macro.retrieve,
        )
        self.latest = async_to_raw_response_wrapper(
            macro.latest,
        )
        self.list_available = async_to_raw_response_wrapper(
            macro.list_available,
        )


class MacroResourceWithStreamingResponse:
    def __init__(self, macro: MacroResource) -> None:
        self._macro = macro

        self.retrieve = to_streamed_response_wrapper(
            macro.retrieve,
        )
        self.latest = to_streamed_response_wrapper(
            macro.latest,
        )
        self.list_available = to_streamed_response_wrapper(
            macro.list_available,
        )


class AsyncMacroResourceWithStreamingResponse:
    def __init__(self, macro: AsyncMacroResource) -> None:
        self._macro = macro

        self.retrieve = async_to_streamed_response_wrapper(
            macro.retrieve,
        )
        self.latest = async_to_streamed_response_wrapper(
            macro.latest,
        )
        self.list_available = async_to_streamed_response_wrapper(
            macro.list_available,
        )
