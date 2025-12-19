# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import BrapiError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import v2, quote, available
    from .resources.quote import QuoteResource, AsyncQuoteResource
    from .resources.v2.v2 import V2Resource, AsyncV2Resource
    from .resources.available import AvailableResource, AsyncAvailableResource

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Brapi",
    "AsyncBrapi",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://brapi.dev",
    "environment_1": "http://localhost:3000",
}


class Brapi(SyncAPIClient):
    # client options
    api_key: str

    _environment: Literal["production", "environment_1"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "environment_1"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Brapi client instance.

        This automatically infers the `api_key` argument from the `BRAPI_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("BRAPI_API_KEY")
        if api_key is None:
            raise BrapiError(
                "The api_key client option must be set either by passing api_key to the client or by setting the BRAPI_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("BRAPI_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `BRAPI_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def quote(self) -> QuoteResource:
        from .resources.quote import QuoteResource

        return QuoteResource(self)

    @cached_property
    def available(self) -> AvailableResource:
        from .resources.available import AvailableResource

        return AvailableResource(self)

    @cached_property
    def v2(self) -> V2Resource:
        from .resources.v2 import V2Resource

        return V2Resource(self)

    @cached_property
    def with_raw_response(self) -> BrapiWithRawResponse:
        return BrapiWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrapiWithStreamedResponse:
        return BrapiWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "environment_1"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncBrapi(AsyncAPIClient):
    # client options
    api_key: str

    _environment: Literal["production", "environment_1"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "environment_1"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncBrapi client instance.

        This automatically infers the `api_key` argument from the `BRAPI_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("BRAPI_API_KEY")
        if api_key is None:
            raise BrapiError(
                "The api_key client option must be set either by passing api_key to the client or by setting the BRAPI_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("BRAPI_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `BRAPI_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def quote(self) -> AsyncQuoteResource:
        from .resources.quote import AsyncQuoteResource

        return AsyncQuoteResource(self)

    @cached_property
    def available(self) -> AsyncAvailableResource:
        from .resources.available import AsyncAvailableResource

        return AsyncAvailableResource(self)

    @cached_property
    def v2(self) -> AsyncV2Resource:
        from .resources.v2 import AsyncV2Resource

        return AsyncV2Resource(self)

    @cached_property
    def with_raw_response(self) -> AsyncBrapiWithRawResponse:
        return AsyncBrapiWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrapiWithStreamedResponse:
        return AsyncBrapiWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "environment_1"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class BrapiWithRawResponse:
    _client: Brapi

    def __init__(self, client: Brapi) -> None:
        self._client = client

    @cached_property
    def quote(self) -> quote.QuoteResourceWithRawResponse:
        from .resources.quote import QuoteResourceWithRawResponse

        return QuoteResourceWithRawResponse(self._client.quote)

    @cached_property
    def available(self) -> available.AvailableResourceWithRawResponse:
        from .resources.available import AvailableResourceWithRawResponse

        return AvailableResourceWithRawResponse(self._client.available)

    @cached_property
    def v2(self) -> v2.V2ResourceWithRawResponse:
        from .resources.v2 import V2ResourceWithRawResponse

        return V2ResourceWithRawResponse(self._client.v2)


class AsyncBrapiWithRawResponse:
    _client: AsyncBrapi

    def __init__(self, client: AsyncBrapi) -> None:
        self._client = client

    @cached_property
    def quote(self) -> quote.AsyncQuoteResourceWithRawResponse:
        from .resources.quote import AsyncQuoteResourceWithRawResponse

        return AsyncQuoteResourceWithRawResponse(self._client.quote)

    @cached_property
    def available(self) -> available.AsyncAvailableResourceWithRawResponse:
        from .resources.available import AsyncAvailableResourceWithRawResponse

        return AsyncAvailableResourceWithRawResponse(self._client.available)

    @cached_property
    def v2(self) -> v2.AsyncV2ResourceWithRawResponse:
        from .resources.v2 import AsyncV2ResourceWithRawResponse

        return AsyncV2ResourceWithRawResponse(self._client.v2)


class BrapiWithStreamedResponse:
    _client: Brapi

    def __init__(self, client: Brapi) -> None:
        self._client = client

    @cached_property
    def quote(self) -> quote.QuoteResourceWithStreamingResponse:
        from .resources.quote import QuoteResourceWithStreamingResponse

        return QuoteResourceWithStreamingResponse(self._client.quote)

    @cached_property
    def available(self) -> available.AvailableResourceWithStreamingResponse:
        from .resources.available import AvailableResourceWithStreamingResponse

        return AvailableResourceWithStreamingResponse(self._client.available)

    @cached_property
    def v2(self) -> v2.V2ResourceWithStreamingResponse:
        from .resources.v2 import V2ResourceWithStreamingResponse

        return V2ResourceWithStreamingResponse(self._client.v2)


class AsyncBrapiWithStreamedResponse:
    _client: AsyncBrapi

    def __init__(self, client: AsyncBrapi) -> None:
        self._client = client

    @cached_property
    def quote(self) -> quote.AsyncQuoteResourceWithStreamingResponse:
        from .resources.quote import AsyncQuoteResourceWithStreamingResponse

        return AsyncQuoteResourceWithStreamingResponse(self._client.quote)

    @cached_property
    def available(self) -> available.AsyncAvailableResourceWithStreamingResponse:
        from .resources.available import AsyncAvailableResourceWithStreamingResponse

        return AsyncAvailableResourceWithStreamingResponse(self._client.available)

    @cached_property
    def v2(self) -> v2.AsyncV2ResourceWithStreamingResponse:
        from .resources.v2 import AsyncV2ResourceWithStreamingResponse

        return AsyncV2ResourceWithStreamingResponse(self._client.v2)


Client = Brapi

AsyncClient = AsyncBrapi
