# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v2.funds import crowding_history_params, crowding_retrieve_params
from ....types.v2.funds.crowding_history_response import CrowdingHistoryResponse
from ....types.v2.funds.crowding_retrieve_response import CrowdingRetrieveResponse

__all__ = ["CrowdingResource", "AsyncCrowdingResource"]


class CrowdingResource(SyncAPIResource):
    """
    Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
    """

    @cached_property
    def with_raw_response(self) -> CrowdingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return CrowdingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CrowdingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return CrowdingResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        reference_date: str | Omit = omit,
        region: Literal["all", "brazil", "foreign"] | Omit = omit,
        sort_by: Literal["value", "flow", "funds"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CrowdingRetrieveResponse:
        """
        Quanto dinheiro todos os fundos têm em cada empresa em um mês, e o saldo do mês:
        quanto compraram menos quanto venderam. Os dados vêm da carteira mensal que os
        fundos entregam à CVM.

        Use para ver as empresas onde os fundos mais concentram dinheiro, as que mais
        compraram ou venderam no mês e o saldo de cada setor.

        Cada empresa junta as classes de ações, as units e os BDRs e ADRs dela. `value`
        conta cada posição uma vez: as posições dos próprios fundos (`directValue`) e a
        parte dos fundos do exterior, como os ETFs por trás dos BDRs de ETF, que os
        fundos brasileiros têm (`foreignFundsValue`). Um fundo de fundos não soma de
        novo o dinheiro dos fundos que ele tem.

        Os fundos entregam a carteira ao longo de semanas. Um fundo que ainda não
        entregou a carteira do mês entra com a carteira do mês anterior
        (`lateFilersValue`), porque a falta de um arquivo não é dinheiro que saiu. Sem
        essa parte, `value` é o mesmo total de `summary.totalValue` em
        `/api/v2/funds/holders` com `scope=all` e `issuer=true`.

        O saldo (`flowValue`) segue as regras de `change` em `/api/v2/funds/holders`: a
        diferença de quantidade, ajustada por desdobramentos, grupamentos e
        bonificações, vezes o preço do mês. Uma posição nova conta como compra e uma
        posição zerada como venda. Um fundo que ainda não entregou a carteira do mês não
        conta como venda. Um fundo sem carteira no mês anterior, ou com ações em
        posições confidenciais em um dos dois meses, fica fora do saldo. Quando um
        evento muda a quantidade de ações sem fator conhecido, `flowValue` vem `null`.

        `sectors` traz o dinheiro e o saldo de cada setor: `boughtValue` soma as
        empresas com saldo de compra, `soldValue` as com saldo de venda.

        `summary` traz a concentração: a parte do dinheiro nas 5 e nas 10 maiores
        empresas e o número efetivo de empresas. Posições confidenciais não entram em
        nenhum total; `summary.confidentialEquityValue` mostra quanto dinheiro em ações
        fica de fora.

        Só entram meses que a maioria dos fundos já entregou. A CVM publica a carteira
        cerca de 10 dias depois do fim do mês.

        Plano Pro.

        Args:
          limit: Empresas por página. Padrão 20, máximo 500.

          page: Página, a partir de 1.

          reference_date: Data no formato YYYY-MM-DD. Traz o mês mais recente até esta data. Sem ela, traz
              o mês mais recente que a maioria dos fundos já entregou.

          region: `all` (padrão): todas as empresas. `brazil`: empresas da B3. `foreign`: empresas
              do exterior, por BDRs, ações no exterior e fundos do exterior.

          sort_by: `value` (padrão): dinheiro dos fundos. `flow`: saldo do mês (com
              `sortOrder=asc`, as maiores vendas). `funds`: número de fundos com posição
              direta.

          sort_order: Ordem: `desc` (padrão) ou `asc`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/funds/crowding",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                        "reference_date": reference_date,
                        "region": region,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                    },
                    crowding_retrieve_params.CrowdingRetrieveParams,
                ),
            ),
            cast_to=CrowdingRetrieveResponse,
        )

    def history(
        self,
        *,
        region: Literal["all", "brazil", "foreign"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CrowdingHistoryResponse:
        """
        Para cada mês: quanto dinheiro todos os fundos têm em ações, a parte nas 5 e nas
        10 maiores empresas, o número efetivo de empresas e o saldo do mês. Os valores
        seguem as regras de `/api/v2/funds/crowding`.

        Use para ver se o dinheiro dos fundos se concentra em poucas empresas ou se
        espalha.

        `confidentialEquityValue` traz as ações em posições confidenciais, que não
        entram nos totais.

        Plano Pro.

        Args:
          region: `all` (padrão): todas as empresas. `brazil`: empresas da B3. `foreign`: empresas
              do exterior, por BDRs, ações no exterior e fundos do exterior.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/funds/crowding/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"region": region}, crowding_history_params.CrowdingHistoryParams),
            ),
            cast_to=CrowdingHistoryResponse,
        )


class AsyncCrowdingResource(AsyncAPIResource):
    """
    Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
    """

    @cached_property
    def with_raw_response(self) -> AsyncCrowdingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCrowdingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCrowdingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncCrowdingResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        reference_date: str | Omit = omit,
        region: Literal["all", "brazil", "foreign"] | Omit = omit,
        sort_by: Literal["value", "flow", "funds"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CrowdingRetrieveResponse:
        """
        Quanto dinheiro todos os fundos têm em cada empresa em um mês, e o saldo do mês:
        quanto compraram menos quanto venderam. Os dados vêm da carteira mensal que os
        fundos entregam à CVM.

        Use para ver as empresas onde os fundos mais concentram dinheiro, as que mais
        compraram ou venderam no mês e o saldo de cada setor.

        Cada empresa junta as classes de ações, as units e os BDRs e ADRs dela. `value`
        conta cada posição uma vez: as posições dos próprios fundos (`directValue`) e a
        parte dos fundos do exterior, como os ETFs por trás dos BDRs de ETF, que os
        fundos brasileiros têm (`foreignFundsValue`). Um fundo de fundos não soma de
        novo o dinheiro dos fundos que ele tem.

        Os fundos entregam a carteira ao longo de semanas. Um fundo que ainda não
        entregou a carteira do mês entra com a carteira do mês anterior
        (`lateFilersValue`), porque a falta de um arquivo não é dinheiro que saiu. Sem
        essa parte, `value` é o mesmo total de `summary.totalValue` em
        `/api/v2/funds/holders` com `scope=all` e `issuer=true`.

        O saldo (`flowValue`) segue as regras de `change` em `/api/v2/funds/holders`: a
        diferença de quantidade, ajustada por desdobramentos, grupamentos e
        bonificações, vezes o preço do mês. Uma posição nova conta como compra e uma
        posição zerada como venda. Um fundo que ainda não entregou a carteira do mês não
        conta como venda. Um fundo sem carteira no mês anterior, ou com ações em
        posições confidenciais em um dos dois meses, fica fora do saldo. Quando um
        evento muda a quantidade de ações sem fator conhecido, `flowValue` vem `null`.

        `sectors` traz o dinheiro e o saldo de cada setor: `boughtValue` soma as
        empresas com saldo de compra, `soldValue` as com saldo de venda.

        `summary` traz a concentração: a parte do dinheiro nas 5 e nas 10 maiores
        empresas e o número efetivo de empresas. Posições confidenciais não entram em
        nenhum total; `summary.confidentialEquityValue` mostra quanto dinheiro em ações
        fica de fora.

        Só entram meses que a maioria dos fundos já entregou. A CVM publica a carteira
        cerca de 10 dias depois do fim do mês.

        Plano Pro.

        Args:
          limit: Empresas por página. Padrão 20, máximo 500.

          page: Página, a partir de 1.

          reference_date: Data no formato YYYY-MM-DD. Traz o mês mais recente até esta data. Sem ela, traz
              o mês mais recente que a maioria dos fundos já entregou.

          region: `all` (padrão): todas as empresas. `brazil`: empresas da B3. `foreign`: empresas
              do exterior, por BDRs, ações no exterior e fundos do exterior.

          sort_by: `value` (padrão): dinheiro dos fundos. `flow`: saldo do mês (com
              `sortOrder=asc`, as maiores vendas). `funds`: número de fundos com posição
              direta.

          sort_order: Ordem: `desc` (padrão) ou `asc`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/funds/crowding",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                        "reference_date": reference_date,
                        "region": region,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                    },
                    crowding_retrieve_params.CrowdingRetrieveParams,
                ),
            ),
            cast_to=CrowdingRetrieveResponse,
        )

    async def history(
        self,
        *,
        region: Literal["all", "brazil", "foreign"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CrowdingHistoryResponse:
        """
        Para cada mês: quanto dinheiro todos os fundos têm em ações, a parte nas 5 e nas
        10 maiores empresas, o número efetivo de empresas e o saldo do mês. Os valores
        seguem as regras de `/api/v2/funds/crowding`.

        Use para ver se o dinheiro dos fundos se concentra em poucas empresas ou se
        espalha.

        `confidentialEquityValue` traz as ações em posições confidenciais, que não
        entram nos totais.

        Plano Pro.

        Args:
          region: `all` (padrão): todas as empresas. `brazil`: empresas da B3. `foreign`: empresas
              do exterior, por BDRs, ações no exterior e fundos do exterior.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/funds/crowding/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"region": region}, crowding_history_params.CrowdingHistoryParams),
            ),
            cast_to=CrowdingHistoryResponse,
        )


class CrowdingResourceWithRawResponse:
    def __init__(self, crowding: CrowdingResource) -> None:
        self._crowding = crowding

        self.retrieve = to_raw_response_wrapper(
            crowding.retrieve,
        )
        self.history = to_raw_response_wrapper(
            crowding.history,
        )


class AsyncCrowdingResourceWithRawResponse:
    def __init__(self, crowding: AsyncCrowdingResource) -> None:
        self._crowding = crowding

        self.retrieve = async_to_raw_response_wrapper(
            crowding.retrieve,
        )
        self.history = async_to_raw_response_wrapper(
            crowding.history,
        )


class CrowdingResourceWithStreamingResponse:
    def __init__(self, crowding: CrowdingResource) -> None:
        self._crowding = crowding

        self.retrieve = to_streamed_response_wrapper(
            crowding.retrieve,
        )
        self.history = to_streamed_response_wrapper(
            crowding.history,
        )


class AsyncCrowdingResourceWithStreamingResponse:
    def __init__(self, crowding: AsyncCrowdingResource) -> None:
        self._crowding = crowding

        self.retrieve = async_to_streamed_response_wrapper(
            crowding.retrieve,
        )
        self.history = async_to_streamed_response_wrapper(
            crowding.history,
        )
