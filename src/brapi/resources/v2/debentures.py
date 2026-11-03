# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v2 import debenture_list_params, debenture_profile_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v2.debenture_list_response import DebentureListResponse
from ...types.v2.debenture_profile_response import DebentureProfileResponse

__all__ = ["DebenturesResource", "AsyncDebenturesResource"]


class DebenturesResource(SyncAPIResource):
    """
    Consulte dados de títulos públicos e outros instrumentos de renda fixa brasileira.
    """

    @cached_property
    def with_raw_response(self) -> DebenturesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return DebenturesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DebenturesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return DebenturesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cnpjs: str | Omit = omit,
        incentivized: Literal["true", "false"] | Omit = omit,
        index: Literal["di", "ipca", "pre", "igp-m", "inpc", "tr", "usd", "eur", "none"] | Omit = omit,
        limit: int | Omit = omit,
        maturity_from: str | Omit = omit,
        maturity_to: str | Omit = omit,
        page: int | Omit = omit,
        search: str | Omit = omit,
        sort_by: Literal["symbol", "maturityDate", "issueDate"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        status: Literal["active", "inactive"] | Omit = omit,
        symbols: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DebentureListResponse:
        """
        Lista as debêntures registradas, com emissora, indexador, taxa, vencimento e
        valor nominal atualizado. Os dados vêm do registro público de debêntures e são
        atualizados uma vez por dia.

        Sem filtros, traz só as debêntures em circulação (`status` = `active`). Use
        `cnpjs` para ver as debêntures de uma empresa, inclusive empresas sem ações
        listadas.

        Plano Pro.

        Args:
          cnpjs: CNPJs das empresas emissoras separados por vírgula, com ou sem pontuação. Máximo
              de 20.

          incentivized: `true` traz só debêntures incentivadas (Lei 12.431), com benefício de imposto de
              renda.

          index: Indexador. Para mais de um, separe por vírgula. `pre` é prefixado, `none` é sem
              indexador.

          limit: Máximo de debêntures por página.

          maturity_from: Vencimento a partir desta data.

          maturity_to: Vencimento até esta data.

          page: Página.

          search: Busca pelo código da debênture ou pelo nome da emissora. Cada palavra deve estar
              no início do código ou de uma palavra do nome.

          sort_by: Campo de ordenação.

          sort_order: Ordem crescente (`asc`) ou decrescente (`desc`).

          status: `active` (em circulação) ou `inactive` (vencida, resgatada ou cancelada).
              Padrão: `active`, ou as duas quando `symbols` é informado.

          symbols: Códigos das debêntures separados por vírgula. Máximo de 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/debentures/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cnpjs": cnpjs,
                        "incentivized": incentivized,
                        "index": index,
                        "limit": limit,
                        "maturity_from": maturity_from,
                        "maturity_to": maturity_to,
                        "page": page,
                        "search": search,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "status": status,
                        "symbols": symbols,
                    },
                    debenture_list_params.DebentureListParams,
                ),
            ),
            cast_to=DebentureListResponse,
        )

    def profile(
        self,
        *,
        symbols: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DebentureProfileResponse:
        """
        Características completas de cada debênture: os campos da listagem, mais
        registro na CVM, resgate antecipado, pagamento de juros, amortização,
        quantidades e agentes da emissão. Os dados vêm do registro público de debêntures
        e são atualizados uma vez por dia.

        Plano Pro.

        Args:
          symbols: Códigos das debêntures separados por vírgula. Máximo de 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/debentures/profile",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"symbols": symbols}, debenture_profile_params.DebentureProfileParams),
            ),
            cast_to=DebentureProfileResponse,
        )


class AsyncDebenturesResource(AsyncAPIResource):
    """
    Consulte dados de títulos públicos e outros instrumentos de renda fixa brasileira.
    """

    @cached_property
    def with_raw_response(self) -> AsyncDebenturesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDebenturesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDebenturesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncDebenturesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        cnpjs: str | Omit = omit,
        incentivized: Literal["true", "false"] | Omit = omit,
        index: Literal["di", "ipca", "pre", "igp-m", "inpc", "tr", "usd", "eur", "none"] | Omit = omit,
        limit: int | Omit = omit,
        maturity_from: str | Omit = omit,
        maturity_to: str | Omit = omit,
        page: int | Omit = omit,
        search: str | Omit = omit,
        sort_by: Literal["symbol", "maturityDate", "issueDate"] | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        status: Literal["active", "inactive"] | Omit = omit,
        symbols: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DebentureListResponse:
        """
        Lista as debêntures registradas, com emissora, indexador, taxa, vencimento e
        valor nominal atualizado. Os dados vêm do registro público de debêntures e são
        atualizados uma vez por dia.

        Sem filtros, traz só as debêntures em circulação (`status` = `active`). Use
        `cnpjs` para ver as debêntures de uma empresa, inclusive empresas sem ações
        listadas.

        Plano Pro.

        Args:
          cnpjs: CNPJs das empresas emissoras separados por vírgula, com ou sem pontuação. Máximo
              de 20.

          incentivized: `true` traz só debêntures incentivadas (Lei 12.431), com benefício de imposto de
              renda.

          index: Indexador. Para mais de um, separe por vírgula. `pre` é prefixado, `none` é sem
              indexador.

          limit: Máximo de debêntures por página.

          maturity_from: Vencimento a partir desta data.

          maturity_to: Vencimento até esta data.

          page: Página.

          search: Busca pelo código da debênture ou pelo nome da emissora. Cada palavra deve estar
              no início do código ou de uma palavra do nome.

          sort_by: Campo de ordenação.

          sort_order: Ordem crescente (`asc`) ou decrescente (`desc`).

          status: `active` (em circulação) ou `inactive` (vencida, resgatada ou cancelada).
              Padrão: `active`, ou as duas quando `symbols` é informado.

          symbols: Códigos das debêntures separados por vírgula. Máximo de 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/debentures/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cnpjs": cnpjs,
                        "incentivized": incentivized,
                        "index": index,
                        "limit": limit,
                        "maturity_from": maturity_from,
                        "maturity_to": maturity_to,
                        "page": page,
                        "search": search,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "status": status,
                        "symbols": symbols,
                    },
                    debenture_list_params.DebentureListParams,
                ),
            ),
            cast_to=DebentureListResponse,
        )

    async def profile(
        self,
        *,
        symbols: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DebentureProfileResponse:
        """
        Características completas de cada debênture: os campos da listagem, mais
        registro na CVM, resgate antecipado, pagamento de juros, amortização,
        quantidades e agentes da emissão. Os dados vêm do registro público de debêntures
        e são atualizados uma vez por dia.

        Plano Pro.

        Args:
          symbols: Códigos das debêntures separados por vírgula. Máximo de 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/debentures/profile",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"symbols": symbols}, debenture_profile_params.DebentureProfileParams
                ),
            ),
            cast_to=DebentureProfileResponse,
        )


class DebenturesResourceWithRawResponse:
    def __init__(self, debentures: DebenturesResource) -> None:
        self._debentures = debentures

        self.list = to_raw_response_wrapper(
            debentures.list,
        )
        self.profile = to_raw_response_wrapper(
            debentures.profile,
        )


class AsyncDebenturesResourceWithRawResponse:
    def __init__(self, debentures: AsyncDebenturesResource) -> None:
        self._debentures = debentures

        self.list = async_to_raw_response_wrapper(
            debentures.list,
        )
        self.profile = async_to_raw_response_wrapper(
            debentures.profile,
        )


class DebenturesResourceWithStreamingResponse:
    def __init__(self, debentures: DebenturesResource) -> None:
        self._debentures = debentures

        self.list = to_streamed_response_wrapper(
            debentures.list,
        )
        self.profile = to_streamed_response_wrapper(
            debentures.profile,
        )


class AsyncDebenturesResourceWithStreamingResponse:
    def __init__(self, debentures: AsyncDebenturesResource) -> None:
        self._debentures = debentures

        self.list = async_to_streamed_response_wrapper(
            debentures.list,
        )
        self.profile = async_to_streamed_response_wrapper(
            debentures.profile,
        )
