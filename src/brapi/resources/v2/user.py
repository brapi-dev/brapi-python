# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v2 import user_usage_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v2.user_usage_response import UserUsageResponse

__all__ = ["UserResource", "AsyncUserResource"]


class UserResource(SyncAPIResource):
    """Dados da conta autenticada, como plano atual e uso da janela vigente."""

    @cached_property
    def with_raw_response(self) -> UserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return UserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return UserResourceWithStreamingResponse(self)

    def usage(
        self,
        *,
        format: Literal["json"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserUsageResponse:
        """
        Quanto da sua cota você já gastou na janela atual.

        A resposta traz `planName` (`free`, `startup` ou `pro`), `planLimit` com o
        limite do plano, `currentUsage` com o consumo registrado, `remainingUsage` com o
        saldo, `usageWindow` indicando se a contagem é por ciclo de cobrança ou por 30
        dias móveis, e `subscriptionPeriod` com o período atual da assinatura.

        A contagem vem do mesmo cache que o limitador usa, então ela pode ficar alguns
        segundos atrás do consumo real.

        ```bash
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/user/usage"
        ```

        Args:
          format: Formato da resposta. JSON é o formato suportado.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/user/usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"format": format}, user_usage_params.UserUsageParams),
            ),
            cast_to=UserUsageResponse,
        )


class AsyncUserResource(AsyncAPIResource):
    """Dados da conta autenticada, como plano atual e uso da janela vigente."""

    @cached_property
    def with_raw_response(self) -> AsyncUserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncUserResourceWithStreamingResponse(self)

    async def usage(
        self,
        *,
        format: Literal["json"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserUsageResponse:
        """
        Quanto da sua cota você já gastou na janela atual.

        A resposta traz `planName` (`free`, `startup` ou `pro`), `planLimit` com o
        limite do plano, `currentUsage` com o consumo registrado, `remainingUsage` com o
        saldo, `usageWindow` indicando se a contagem é por ciclo de cobrança ou por 30
        dias móveis, e `subscriptionPeriod` com o período atual da assinatura.

        A contagem vem do mesmo cache que o limitador usa, então ela pode ficar alguns
        segundos atrás do consumo real.

        ```bash
        curl -H "Authorization: Bearer SEU_TOKEN" "https://brapi.dev/api/v2/user/usage"
        ```

        Args:
          format: Formato da resposta. JSON é o formato suportado.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/user/usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"format": format}, user_usage_params.UserUsageParams),
            ),
            cast_to=UserUsageResponse,
        )


class UserResourceWithRawResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.usage = to_raw_response_wrapper(
            user.usage,
        )


class AsyncUserResourceWithRawResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.usage = async_to_raw_response_wrapper(
            user.usage,
        )


class UserResourceWithStreamingResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.usage = to_streamed_response_wrapper(
            user.usage,
        )


class AsyncUserResourceWithStreamingResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.usage = async_to_streamed_response_wrapper(
            user.usage,
        )
