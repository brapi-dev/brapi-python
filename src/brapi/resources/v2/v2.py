# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .crypto import (
    CryptoResource,
    AsyncCryptoResource,
    CryptoResourceWithRawResponse,
    AsyncCryptoResourceWithRawResponse,
    CryptoResourceWithStreamingResponse,
    AsyncCryptoResourceWithStreamingResponse,
)
from .currency import (
    CurrencyResource,
    AsyncCurrencyResource,
    CurrencyResourceWithRawResponse,
    AsyncCurrencyResourceWithRawResponse,
    CurrencyResourceWithStreamingResponse,
    AsyncCurrencyResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .inflation import (
    InflationResource,
    AsyncInflationResource,
    InflationResourceWithRawResponse,
    AsyncInflationResourceWithRawResponse,
    InflationResourceWithStreamingResponse,
    AsyncInflationResourceWithStreamingResponse,
)
from .prime_rate import (
    PrimeRateResource,
    AsyncPrimeRateResource,
    PrimeRateResourceWithRawResponse,
    AsyncPrimeRateResourceWithRawResponse,
    PrimeRateResourceWithStreamingResponse,
    AsyncPrimeRateResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["V2Resource", "AsyncV2Resource"]


class V2Resource(SyncAPIResource):
    @cached_property
    def crypto(self) -> CryptoResource:
        return CryptoResource(self._client)

    @cached_property
    def currency(self) -> CurrencyResource:
        return CurrencyResource(self._client)

    @cached_property
    def inflation(self) -> InflationResource:
        return InflationResource(self._client)

    @cached_property
    def prime_rate(self) -> PrimeRateResource:
        return PrimeRateResource(self._client)

    @cached_property
    def with_raw_response(self) -> V2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/brapi-python#accessing-raw-response-data-eg-headers
        """
        return V2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/brapi-python#with_streaming_response
        """
        return V2ResourceWithStreamingResponse(self)


class AsyncV2Resource(AsyncAPIResource):
    @cached_property
    def crypto(self) -> AsyncCryptoResource:
        return AsyncCryptoResource(self._client)

    @cached_property
    def currency(self) -> AsyncCurrencyResource:
        return AsyncCurrencyResource(self._client)

    @cached_property
    def inflation(self) -> AsyncInflationResource:
        return AsyncInflationResource(self._client)

    @cached_property
    def prime_rate(self) -> AsyncPrimeRateResource:
        return AsyncPrimeRateResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/brapi-python#with_streaming_response
        """
        return AsyncV2ResourceWithStreamingResponse(self)


class V2ResourceWithRawResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

    @cached_property
    def crypto(self) -> CryptoResourceWithRawResponse:
        return CryptoResourceWithRawResponse(self._v2.crypto)

    @cached_property
    def currency(self) -> CurrencyResourceWithRawResponse:
        return CurrencyResourceWithRawResponse(self._v2.currency)

    @cached_property
    def inflation(self) -> InflationResourceWithRawResponse:
        return InflationResourceWithRawResponse(self._v2.inflation)

    @cached_property
    def prime_rate(self) -> PrimeRateResourceWithRawResponse:
        return PrimeRateResourceWithRawResponse(self._v2.prime_rate)


class AsyncV2ResourceWithRawResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

    @cached_property
    def crypto(self) -> AsyncCryptoResourceWithRawResponse:
        return AsyncCryptoResourceWithRawResponse(self._v2.crypto)

    @cached_property
    def currency(self) -> AsyncCurrencyResourceWithRawResponse:
        return AsyncCurrencyResourceWithRawResponse(self._v2.currency)

    @cached_property
    def inflation(self) -> AsyncInflationResourceWithRawResponse:
        return AsyncInflationResourceWithRawResponse(self._v2.inflation)

    @cached_property
    def prime_rate(self) -> AsyncPrimeRateResourceWithRawResponse:
        return AsyncPrimeRateResourceWithRawResponse(self._v2.prime_rate)


class V2ResourceWithStreamingResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

    @cached_property
    def crypto(self) -> CryptoResourceWithStreamingResponse:
        return CryptoResourceWithStreamingResponse(self._v2.crypto)

    @cached_property
    def currency(self) -> CurrencyResourceWithStreamingResponse:
        return CurrencyResourceWithStreamingResponse(self._v2.currency)

    @cached_property
    def inflation(self) -> InflationResourceWithStreamingResponse:
        return InflationResourceWithStreamingResponse(self._v2.inflation)

    @cached_property
    def prime_rate(self) -> PrimeRateResourceWithStreamingResponse:
        return PrimeRateResourceWithStreamingResponse(self._v2.prime_rate)


class AsyncV2ResourceWithStreamingResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

    @cached_property
    def crypto(self) -> AsyncCryptoResourceWithStreamingResponse:
        return AsyncCryptoResourceWithStreamingResponse(self._v2.crypto)

    @cached_property
    def currency(self) -> AsyncCurrencyResourceWithStreamingResponse:
        return AsyncCurrencyResourceWithStreamingResponse(self._v2.currency)

    @cached_property
    def inflation(self) -> AsyncInflationResourceWithStreamingResponse:
        return AsyncInflationResourceWithStreamingResponse(self._v2.inflation)

    @cached_property
    def prime_rate(self) -> AsyncPrimeRateResourceWithStreamingResponse:
        return AsyncPrimeRateResourceWithStreamingResponse(self._v2.prime_rate)
