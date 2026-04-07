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
        """
        Obtenha cotações em tempo real e dados históricos de criptomoedas, disponíveis em diversas moedas de referência.
        """
        return CryptoResource(self._client)

    @cached_property
    def currency(self) -> CurrencyResource:
        """
        Monitore taxas de câmbio entre moedas fiduciárias de todo o mundo, com atualizações frequentes e dados históricos.
        """
        return CurrencyResource(self._client)

    @cached_property
    def inflation(self) -> InflationResource:
        """
        Acompanhe os principais indicadores econômicos do Brasil, incluindo inflação (IPCA, IGP-M) e Taxa Selic.
        """
        return InflationResource(self._client)

    @cached_property
    def prime_rate(self) -> PrimeRateResource:
        """
        Acompanhe os principais indicadores econômicos do Brasil, incluindo inflação (IPCA, IGP-M) e Taxa Selic.
        """
        return PrimeRateResource(self._client)

    @cached_property
    def with_raw_response(self) -> V2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return V2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return V2ResourceWithStreamingResponse(self)


class AsyncV2Resource(AsyncAPIResource):
    @cached_property
    def crypto(self) -> AsyncCryptoResource:
        """
        Obtenha cotações em tempo real e dados históricos de criptomoedas, disponíveis em diversas moedas de referência.
        """
        return AsyncCryptoResource(self._client)

    @cached_property
    def currency(self) -> AsyncCurrencyResource:
        """
        Monitore taxas de câmbio entre moedas fiduciárias de todo o mundo, com atualizações frequentes e dados históricos.
        """
        return AsyncCurrencyResource(self._client)

    @cached_property
    def inflation(self) -> AsyncInflationResource:
        """
        Acompanhe os principais indicadores econômicos do Brasil, incluindo inflação (IPCA, IGP-M) e Taxa Selic.
        """
        return AsyncInflationResource(self._client)

    @cached_property
    def prime_rate(self) -> AsyncPrimeRateResource:
        """
        Acompanhe os principais indicadores econômicos do Brasil, incluindo inflação (IPCA, IGP-M) e Taxa Selic.
        """
        return AsyncPrimeRateResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brapi-dev/brapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brapi-dev/brapi-python#with_streaming_response
        """
        return AsyncV2ResourceWithStreamingResponse(self)


class V2ResourceWithRawResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

    @cached_property
    def crypto(self) -> CryptoResourceWithRawResponse:
        """
        Obtenha cotações em tempo real e dados históricos de criptomoedas, disponíveis em diversas moedas de referência.
        """
        return CryptoResourceWithRawResponse(self._v2.crypto)

    @cached_property
    def currency(self) -> CurrencyResourceWithRawResponse:
        """
        Monitore taxas de câmbio entre moedas fiduciárias de todo o mundo, com atualizações frequentes e dados históricos.
        """
        return CurrencyResourceWithRawResponse(self._v2.currency)

    @cached_property
    def inflation(self) -> InflationResourceWithRawResponse:
        """
        Acompanhe os principais indicadores econômicos do Brasil, incluindo inflação (IPCA, IGP-M) e Taxa Selic.
        """
        return InflationResourceWithRawResponse(self._v2.inflation)

    @cached_property
    def prime_rate(self) -> PrimeRateResourceWithRawResponse:
        """
        Acompanhe os principais indicadores econômicos do Brasil, incluindo inflação (IPCA, IGP-M) e Taxa Selic.
        """
        return PrimeRateResourceWithRawResponse(self._v2.prime_rate)


class AsyncV2ResourceWithRawResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

    @cached_property
    def crypto(self) -> AsyncCryptoResourceWithRawResponse:
        """
        Obtenha cotações em tempo real e dados históricos de criptomoedas, disponíveis em diversas moedas de referência.
        """
        return AsyncCryptoResourceWithRawResponse(self._v2.crypto)

    @cached_property
    def currency(self) -> AsyncCurrencyResourceWithRawResponse:
        """
        Monitore taxas de câmbio entre moedas fiduciárias de todo o mundo, com atualizações frequentes e dados históricos.
        """
        return AsyncCurrencyResourceWithRawResponse(self._v2.currency)

    @cached_property
    def inflation(self) -> AsyncInflationResourceWithRawResponse:
        """
        Acompanhe os principais indicadores econômicos do Brasil, incluindo inflação (IPCA, IGP-M) e Taxa Selic.
        """
        return AsyncInflationResourceWithRawResponse(self._v2.inflation)

    @cached_property
    def prime_rate(self) -> AsyncPrimeRateResourceWithRawResponse:
        """
        Acompanhe os principais indicadores econômicos do Brasil, incluindo inflação (IPCA, IGP-M) e Taxa Selic.
        """
        return AsyncPrimeRateResourceWithRawResponse(self._v2.prime_rate)


class V2ResourceWithStreamingResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

    @cached_property
    def crypto(self) -> CryptoResourceWithStreamingResponse:
        """
        Obtenha cotações em tempo real e dados históricos de criptomoedas, disponíveis em diversas moedas de referência.
        """
        return CryptoResourceWithStreamingResponse(self._v2.crypto)

    @cached_property
    def currency(self) -> CurrencyResourceWithStreamingResponse:
        """
        Monitore taxas de câmbio entre moedas fiduciárias de todo o mundo, com atualizações frequentes e dados históricos.
        """
        return CurrencyResourceWithStreamingResponse(self._v2.currency)

    @cached_property
    def inflation(self) -> InflationResourceWithStreamingResponse:
        """
        Acompanhe os principais indicadores econômicos do Brasil, incluindo inflação (IPCA, IGP-M) e Taxa Selic.
        """
        return InflationResourceWithStreamingResponse(self._v2.inflation)

    @cached_property
    def prime_rate(self) -> PrimeRateResourceWithStreamingResponse:
        """
        Acompanhe os principais indicadores econômicos do Brasil, incluindo inflação (IPCA, IGP-M) e Taxa Selic.
        """
        return PrimeRateResourceWithStreamingResponse(self._v2.prime_rate)


class AsyncV2ResourceWithStreamingResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

    @cached_property
    def crypto(self) -> AsyncCryptoResourceWithStreamingResponse:
        """
        Obtenha cotações em tempo real e dados históricos de criptomoedas, disponíveis em diversas moedas de referência.
        """
        return AsyncCryptoResourceWithStreamingResponse(self._v2.crypto)

    @cached_property
    def currency(self) -> AsyncCurrencyResourceWithStreamingResponse:
        """
        Monitore taxas de câmbio entre moedas fiduciárias de todo o mundo, com atualizações frequentes e dados históricos.
        """
        return AsyncCurrencyResourceWithStreamingResponse(self._v2.currency)

    @cached_property
    def inflation(self) -> AsyncInflationResourceWithStreamingResponse:
        """
        Acompanhe os principais indicadores econômicos do Brasil, incluindo inflação (IPCA, IGP-M) e Taxa Selic.
        """
        return AsyncInflationResourceWithStreamingResponse(self._v2.inflation)

    @cached_property
    def prime_rate(self) -> AsyncPrimeRateResourceWithStreamingResponse:
        """
        Acompanhe os principais indicadores econômicos do Brasil, incluindo inflação (IPCA, IGP-M) e Taxa Selic.
        """
        return AsyncPrimeRateResourceWithStreamingResponse(self._v2.prime_rate)
