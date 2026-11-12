# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .news import (
    NewsResource,
    AsyncNewsResource,
    NewsResourceWithRawResponse,
    AsyncNewsResourceWithRawResponse,
    NewsResourceWithStreamingResponse,
    AsyncNewsResourceWithStreamingResponse,
)
from .user import (
    UserResource,
    AsyncUserResource,
    UserResourceWithRawResponse,
    AsyncUserResourceWithRawResponse,
    UserResourceWithStreamingResponse,
    AsyncUserResourceWithStreamingResponse,
)
from .macro import (
    MacroResource,
    AsyncMacroResource,
    MacroResourceWithRawResponse,
    AsyncMacroResourceWithRawResponse,
    MacroResourceWithStreamingResponse,
    AsyncMacroResourceWithStreamingResponse,
)
from .crypto import (
    CryptoResource,
    AsyncCryptoResource,
    CryptoResourceWithRawResponse,
    AsyncCryptoResourceWithRawResponse,
    CryptoResourceWithStreamingResponse,
    AsyncCryptoResourceWithStreamingResponse,
)
from .stocks import (
    StocksResource,
    AsyncStocksResource,
    StocksResourceWithRawResponse,
    AsyncStocksResourceWithRawResponse,
    StocksResourceWithStreamingResponse,
    AsyncStocksResourceWithStreamingResponse,
)
from .fii.fii import (
    FiiResource,
    AsyncFiiResource,
    FiiResourceWithRawResponse,
    AsyncFiiResourceWithRawResponse,
    FiiResourceWithStreamingResponse,
    AsyncFiiResourceWithStreamingResponse,
)
from .indexes import (
    IndexesResource,
    AsyncIndexesResource,
    IndexesResourceWithRawResponse,
    AsyncIndexesResourceWithRawResponse,
    IndexesResourceWithStreamingResponse,
    AsyncIndexesResourceWithStreamingResponse,
)
from .tickers import (
    TickersResource,
    AsyncTickersResource,
    TickersResourceWithRawResponse,
    AsyncTickersResourceWithRawResponse,
    TickersResourceWithStreamingResponse,
    AsyncTickersResourceWithStreamingResponse,
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
from .debentures import (
    DebenturesResource,
    AsyncDebenturesResource,
    DebenturesResourceWithRawResponse,
    AsyncDebenturesResourceWithRawResponse,
    DebenturesResourceWithStreamingResponse,
    AsyncDebenturesResourceWithStreamingResponse,
)
from .dictionary import (
    DictionaryResource,
    AsyncDictionaryResource,
    DictionaryResourceWithRawResponse,
    AsyncDictionaryResourceWithRawResponse,
    DictionaryResourceWithStreamingResponse,
    AsyncDictionaryResourceWithStreamingResponse,
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
from .funds.funds import (
    FundsResource,
    AsyncFundsResource,
    FundsResourceWithRawResponse,
    AsyncFundsResourceWithRawResponse,
    FundsResourceWithStreamingResponse,
    AsyncFundsResourceWithStreamingResponse,
)
from .futures.futures import (
    FuturesResource,
    AsyncFuturesResource,
    FuturesResourceWithRawResponse,
    AsyncFuturesResourceWithRawResponse,
    FuturesResourceWithStreamingResponse,
    AsyncFuturesResourceWithStreamingResponse,
)
from .options.options import (
    OptionsResource,
    AsyncOptionsResource,
    OptionsResourceWithRawResponse,
    AsyncOptionsResourceWithRawResponse,
    OptionsResourceWithStreamingResponse,
    AsyncOptionsResourceWithStreamingResponse,
)
from .revenue_sources import (
    RevenueSourcesResource,
    AsyncRevenueSourcesResource,
    RevenueSourcesResourceWithRawResponse,
    AsyncRevenueSourcesResourceWithRawResponse,
    RevenueSourcesResourceWithStreamingResponse,
    AsyncRevenueSourcesResourceWithStreamingResponse,
)
from .treasury.treasury import (
    TreasuryResource,
    AsyncTreasuryResource,
    TreasuryResourceWithRawResponse,
    AsyncTreasuryResourceWithRawResponse,
    TreasuryResourceWithStreamingResponse,
    AsyncTreasuryResourceWithStreamingResponse,
)

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
        return InflationResource(self._client)

    @cached_property
    def prime_rate(self) -> PrimeRateResource:
        return PrimeRateResource(self._client)

    @cached_property
    def dictionary(self) -> DictionaryResource:
        """
        Ferramentas auxiliares para descobrir ativos disponíveis e verificar a saúde da API.
        """
        return DictionaryResource(self._client)

    @cached_property
    def stocks(self) -> StocksResource:
        return StocksResource(self._client)

    @cached_property
    def revenue_sources(self) -> RevenueSourcesResource:
        return RevenueSourcesResource(self._client)

    @cached_property
    def tickers(self) -> TickersResource:
        """Descubra, filtre e valide tickers B3 disponíveis na brapi.

        Use como camada de identidade antes dos endpoints de dados de mercado.
        """
        return TickersResource(self._client)

    @cached_property
    def fii(self) -> FiiResource:
        """
        Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
        """
        return FiiResource(self._client)

    @cached_property
    def funds(self) -> FundsResource:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return FundsResource(self._client)

    @cached_property
    def indexes(self) -> IndexesResource:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return IndexesResource(self._client)

    @cached_property
    def options(self) -> OptionsResource:
        """Consulte contratos, cadeias EOD negociadas e histórico de opções."""
        return OptionsResource(self._client)

    @cached_property
    def futures(self) -> FuturesResource:
        return FuturesResource(self._client)

    @cached_property
    def macro(self) -> MacroResource:
        """
        Acompanhe os principais indicadores macroeconômicos do Brasil, incluindo inflação (IPCA, IGP-M), Taxa Selic, agregados monetários e atividade.
        """
        return MacroResource(self._client)

    @cached_property
    def treasury(self) -> TreasuryResource:
        """
        Consulte dados de títulos públicos e outros instrumentos de renda fixa brasileira.
        """
        return TreasuryResource(self._client)

    @cached_property
    def debentures(self) -> DebenturesResource:
        """
        Consulte dados de títulos públicos e outros instrumentos de renda fixa brasileira.
        """
        return DebenturesResource(self._client)

    @cached_property
    def news(self) -> NewsResource:
        """
        Notícias de empresas da B3 e do mercado, com resumo, sentimento, importância e ativos citados.
        """
        return NewsResource(self._client)

    @cached_property
    def user(self) -> UserResource:
        """Dados da conta autenticada, como plano atual e uso da janela vigente."""
        return UserResource(self._client)

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
        return AsyncInflationResource(self._client)

    @cached_property
    def prime_rate(self) -> AsyncPrimeRateResource:
        return AsyncPrimeRateResource(self._client)

    @cached_property
    def dictionary(self) -> AsyncDictionaryResource:
        """
        Ferramentas auxiliares para descobrir ativos disponíveis e verificar a saúde da API.
        """
        return AsyncDictionaryResource(self._client)

    @cached_property
    def stocks(self) -> AsyncStocksResource:
        return AsyncStocksResource(self._client)

    @cached_property
    def revenue_sources(self) -> AsyncRevenueSourcesResource:
        return AsyncRevenueSourcesResource(self._client)

    @cached_property
    def tickers(self) -> AsyncTickersResource:
        """Descubra, filtre e valide tickers B3 disponíveis na brapi.

        Use como camada de identidade antes dos endpoints de dados de mercado.
        """
        return AsyncTickersResource(self._client)

    @cached_property
    def fii(self) -> AsyncFiiResource:
        """
        Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
        """
        return AsyncFiiResource(self._client)

    @cached_property
    def funds(self) -> AsyncFundsResource:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return AsyncFundsResource(self._client)

    @cached_property
    def indexes(self) -> AsyncIndexesResource:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return AsyncIndexesResource(self._client)

    @cached_property
    def options(self) -> AsyncOptionsResource:
        """Consulte contratos, cadeias EOD negociadas e histórico de opções."""
        return AsyncOptionsResource(self._client)

    @cached_property
    def futures(self) -> AsyncFuturesResource:
        return AsyncFuturesResource(self._client)

    @cached_property
    def macro(self) -> AsyncMacroResource:
        """
        Acompanhe os principais indicadores macroeconômicos do Brasil, incluindo inflação (IPCA, IGP-M), Taxa Selic, agregados monetários e atividade.
        """
        return AsyncMacroResource(self._client)

    @cached_property
    def treasury(self) -> AsyncTreasuryResource:
        """
        Consulte dados de títulos públicos e outros instrumentos de renda fixa brasileira.
        """
        return AsyncTreasuryResource(self._client)

    @cached_property
    def debentures(self) -> AsyncDebenturesResource:
        """
        Consulte dados de títulos públicos e outros instrumentos de renda fixa brasileira.
        """
        return AsyncDebenturesResource(self._client)

    @cached_property
    def news(self) -> AsyncNewsResource:
        """
        Notícias de empresas da B3 e do mercado, com resumo, sentimento, importância e ativos citados.
        """
        return AsyncNewsResource(self._client)

    @cached_property
    def user(self) -> AsyncUserResource:
        """Dados da conta autenticada, como plano atual e uso da janela vigente."""
        return AsyncUserResource(self._client)

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
        return InflationResourceWithRawResponse(self._v2.inflation)

    @cached_property
    def prime_rate(self) -> PrimeRateResourceWithRawResponse:
        return PrimeRateResourceWithRawResponse(self._v2.prime_rate)

    @cached_property
    def dictionary(self) -> DictionaryResourceWithRawResponse:
        """
        Ferramentas auxiliares para descobrir ativos disponíveis e verificar a saúde da API.
        """
        return DictionaryResourceWithRawResponse(self._v2.dictionary)

    @cached_property
    def stocks(self) -> StocksResourceWithRawResponse:
        return StocksResourceWithRawResponse(self._v2.stocks)

    @cached_property
    def revenue_sources(self) -> RevenueSourcesResourceWithRawResponse:
        return RevenueSourcesResourceWithRawResponse(self._v2.revenue_sources)

    @cached_property
    def tickers(self) -> TickersResourceWithRawResponse:
        """Descubra, filtre e valide tickers B3 disponíveis na brapi.

        Use como camada de identidade antes dos endpoints de dados de mercado.
        """
        return TickersResourceWithRawResponse(self._v2.tickers)

    @cached_property
    def fii(self) -> FiiResourceWithRawResponse:
        """
        Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
        """
        return FiiResourceWithRawResponse(self._v2.fii)

    @cached_property
    def funds(self) -> FundsResourceWithRawResponse:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return FundsResourceWithRawResponse(self._v2.funds)

    @cached_property
    def indexes(self) -> IndexesResourceWithRawResponse:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return IndexesResourceWithRawResponse(self._v2.indexes)

    @cached_property
    def options(self) -> OptionsResourceWithRawResponse:
        """Consulte contratos, cadeias EOD negociadas e histórico de opções."""
        return OptionsResourceWithRawResponse(self._v2.options)

    @cached_property
    def futures(self) -> FuturesResourceWithRawResponse:
        return FuturesResourceWithRawResponse(self._v2.futures)

    @cached_property
    def macro(self) -> MacroResourceWithRawResponse:
        """
        Acompanhe os principais indicadores macroeconômicos do Brasil, incluindo inflação (IPCA, IGP-M), Taxa Selic, agregados monetários e atividade.
        """
        return MacroResourceWithRawResponse(self._v2.macro)

    @cached_property
    def treasury(self) -> TreasuryResourceWithRawResponse:
        """
        Consulte dados de títulos públicos e outros instrumentos de renda fixa brasileira.
        """
        return TreasuryResourceWithRawResponse(self._v2.treasury)

    @cached_property
    def debentures(self) -> DebenturesResourceWithRawResponse:
        """
        Consulte dados de títulos públicos e outros instrumentos de renda fixa brasileira.
        """
        return DebenturesResourceWithRawResponse(self._v2.debentures)

    @cached_property
    def news(self) -> NewsResourceWithRawResponse:
        """
        Notícias de empresas da B3 e do mercado, com resumo, sentimento, importância e ativos citados.
        """
        return NewsResourceWithRawResponse(self._v2.news)

    @cached_property
    def user(self) -> UserResourceWithRawResponse:
        """Dados da conta autenticada, como plano atual e uso da janela vigente."""
        return UserResourceWithRawResponse(self._v2.user)


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
        return AsyncInflationResourceWithRawResponse(self._v2.inflation)

    @cached_property
    def prime_rate(self) -> AsyncPrimeRateResourceWithRawResponse:
        return AsyncPrimeRateResourceWithRawResponse(self._v2.prime_rate)

    @cached_property
    def dictionary(self) -> AsyncDictionaryResourceWithRawResponse:
        """
        Ferramentas auxiliares para descobrir ativos disponíveis e verificar a saúde da API.
        """
        return AsyncDictionaryResourceWithRawResponse(self._v2.dictionary)

    @cached_property
    def stocks(self) -> AsyncStocksResourceWithRawResponse:
        return AsyncStocksResourceWithRawResponse(self._v2.stocks)

    @cached_property
    def revenue_sources(self) -> AsyncRevenueSourcesResourceWithRawResponse:
        return AsyncRevenueSourcesResourceWithRawResponse(self._v2.revenue_sources)

    @cached_property
    def tickers(self) -> AsyncTickersResourceWithRawResponse:
        """Descubra, filtre e valide tickers B3 disponíveis na brapi.

        Use como camada de identidade antes dos endpoints de dados de mercado.
        """
        return AsyncTickersResourceWithRawResponse(self._v2.tickers)

    @cached_property
    def fii(self) -> AsyncFiiResourceWithRawResponse:
        """
        Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
        """
        return AsyncFiiResourceWithRawResponse(self._v2.fii)

    @cached_property
    def funds(self) -> AsyncFundsResourceWithRawResponse:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return AsyncFundsResourceWithRawResponse(self._v2.funds)

    @cached_property
    def indexes(self) -> AsyncIndexesResourceWithRawResponse:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return AsyncIndexesResourceWithRawResponse(self._v2.indexes)

    @cached_property
    def options(self) -> AsyncOptionsResourceWithRawResponse:
        """Consulte contratos, cadeias EOD negociadas e histórico de opções."""
        return AsyncOptionsResourceWithRawResponse(self._v2.options)

    @cached_property
    def futures(self) -> AsyncFuturesResourceWithRawResponse:
        return AsyncFuturesResourceWithRawResponse(self._v2.futures)

    @cached_property
    def macro(self) -> AsyncMacroResourceWithRawResponse:
        """
        Acompanhe os principais indicadores macroeconômicos do Brasil, incluindo inflação (IPCA, IGP-M), Taxa Selic, agregados monetários e atividade.
        """
        return AsyncMacroResourceWithRawResponse(self._v2.macro)

    @cached_property
    def treasury(self) -> AsyncTreasuryResourceWithRawResponse:
        """
        Consulte dados de títulos públicos e outros instrumentos de renda fixa brasileira.
        """
        return AsyncTreasuryResourceWithRawResponse(self._v2.treasury)

    @cached_property
    def debentures(self) -> AsyncDebenturesResourceWithRawResponse:
        """
        Consulte dados de títulos públicos e outros instrumentos de renda fixa brasileira.
        """
        return AsyncDebenturesResourceWithRawResponse(self._v2.debentures)

    @cached_property
    def news(self) -> AsyncNewsResourceWithRawResponse:
        """
        Notícias de empresas da B3 e do mercado, com resumo, sentimento, importância e ativos citados.
        """
        return AsyncNewsResourceWithRawResponse(self._v2.news)

    @cached_property
    def user(self) -> AsyncUserResourceWithRawResponse:
        """Dados da conta autenticada, como plano atual e uso da janela vigente."""
        return AsyncUserResourceWithRawResponse(self._v2.user)


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
        return InflationResourceWithStreamingResponse(self._v2.inflation)

    @cached_property
    def prime_rate(self) -> PrimeRateResourceWithStreamingResponse:
        return PrimeRateResourceWithStreamingResponse(self._v2.prime_rate)

    @cached_property
    def dictionary(self) -> DictionaryResourceWithStreamingResponse:
        """
        Ferramentas auxiliares para descobrir ativos disponíveis e verificar a saúde da API.
        """
        return DictionaryResourceWithStreamingResponse(self._v2.dictionary)

    @cached_property
    def stocks(self) -> StocksResourceWithStreamingResponse:
        return StocksResourceWithStreamingResponse(self._v2.stocks)

    @cached_property
    def revenue_sources(self) -> RevenueSourcesResourceWithStreamingResponse:
        return RevenueSourcesResourceWithStreamingResponse(self._v2.revenue_sources)

    @cached_property
    def tickers(self) -> TickersResourceWithStreamingResponse:
        """Descubra, filtre e valide tickers B3 disponíveis na brapi.

        Use como camada de identidade antes dos endpoints de dados de mercado.
        """
        return TickersResourceWithStreamingResponse(self._v2.tickers)

    @cached_property
    def fii(self) -> FiiResourceWithStreamingResponse:
        """
        Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
        """
        return FiiResourceWithStreamingResponse(self._v2.fii)

    @cached_property
    def funds(self) -> FundsResourceWithStreamingResponse:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return FundsResourceWithStreamingResponse(self._v2.funds)

    @cached_property
    def indexes(self) -> IndexesResourceWithStreamingResponse:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return IndexesResourceWithStreamingResponse(self._v2.indexes)

    @cached_property
    def options(self) -> OptionsResourceWithStreamingResponse:
        """Consulte contratos, cadeias EOD negociadas e histórico de opções."""
        return OptionsResourceWithStreamingResponse(self._v2.options)

    @cached_property
    def futures(self) -> FuturesResourceWithStreamingResponse:
        return FuturesResourceWithStreamingResponse(self._v2.futures)

    @cached_property
    def macro(self) -> MacroResourceWithStreamingResponse:
        """
        Acompanhe os principais indicadores macroeconômicos do Brasil, incluindo inflação (IPCA, IGP-M), Taxa Selic, agregados monetários e atividade.
        """
        return MacroResourceWithStreamingResponse(self._v2.macro)

    @cached_property
    def treasury(self) -> TreasuryResourceWithStreamingResponse:
        """
        Consulte dados de títulos públicos e outros instrumentos de renda fixa brasileira.
        """
        return TreasuryResourceWithStreamingResponse(self._v2.treasury)

    @cached_property
    def debentures(self) -> DebenturesResourceWithStreamingResponse:
        """
        Consulte dados de títulos públicos e outros instrumentos de renda fixa brasileira.
        """
        return DebenturesResourceWithStreamingResponse(self._v2.debentures)

    @cached_property
    def news(self) -> NewsResourceWithStreamingResponse:
        """
        Notícias de empresas da B3 e do mercado, com resumo, sentimento, importância e ativos citados.
        """
        return NewsResourceWithStreamingResponse(self._v2.news)

    @cached_property
    def user(self) -> UserResourceWithStreamingResponse:
        """Dados da conta autenticada, como plano atual e uso da janela vigente."""
        return UserResourceWithStreamingResponse(self._v2.user)


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
        return AsyncInflationResourceWithStreamingResponse(self._v2.inflation)

    @cached_property
    def prime_rate(self) -> AsyncPrimeRateResourceWithStreamingResponse:
        return AsyncPrimeRateResourceWithStreamingResponse(self._v2.prime_rate)

    @cached_property
    def dictionary(self) -> AsyncDictionaryResourceWithStreamingResponse:
        """
        Ferramentas auxiliares para descobrir ativos disponíveis e verificar a saúde da API.
        """
        return AsyncDictionaryResourceWithStreamingResponse(self._v2.dictionary)

    @cached_property
    def stocks(self) -> AsyncStocksResourceWithStreamingResponse:
        return AsyncStocksResourceWithStreamingResponse(self._v2.stocks)

    @cached_property
    def revenue_sources(self) -> AsyncRevenueSourcesResourceWithStreamingResponse:
        return AsyncRevenueSourcesResourceWithStreamingResponse(self._v2.revenue_sources)

    @cached_property
    def tickers(self) -> AsyncTickersResourceWithStreamingResponse:
        """Descubra, filtre e valide tickers B3 disponíveis na brapi.

        Use como camada de identidade antes dos endpoints de dados de mercado.
        """
        return AsyncTickersResourceWithStreamingResponse(self._v2.tickers)

    @cached_property
    def fii(self) -> AsyncFiiResourceWithStreamingResponse:
        """
        Acesse dados completos de FIIs: cotações, indicadores fundamentalistas (P/VP, DY), relatórios gerenciais e histórico de proventos.
        """
        return AsyncFiiResourceWithStreamingResponse(self._v2.fii)

    @cached_property
    def funds(self) -> AsyncFundsResourceWithStreamingResponse:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return AsyncFundsResourceWithStreamingResponse(self._v2.funds)

    @cached_property
    def indexes(self) -> AsyncIndexesResourceWithStreamingResponse:
        """
        Descubra e consulte fundos brasileiros listados e estruturados, incluindo FIIs, FIAGROs, FI-Infra/FIFs, FIDCs e FIPs.
        """
        return AsyncIndexesResourceWithStreamingResponse(self._v2.indexes)

    @cached_property
    def options(self) -> AsyncOptionsResourceWithStreamingResponse:
        """Consulte contratos, cadeias EOD negociadas e histórico de opções."""
        return AsyncOptionsResourceWithStreamingResponse(self._v2.options)

    @cached_property
    def futures(self) -> AsyncFuturesResourceWithStreamingResponse:
        return AsyncFuturesResourceWithStreamingResponse(self._v2.futures)

    @cached_property
    def macro(self) -> AsyncMacroResourceWithStreamingResponse:
        """
        Acompanhe os principais indicadores macroeconômicos do Brasil, incluindo inflação (IPCA, IGP-M), Taxa Selic, agregados monetários e atividade.
        """
        return AsyncMacroResourceWithStreamingResponse(self._v2.macro)

    @cached_property
    def treasury(self) -> AsyncTreasuryResourceWithStreamingResponse:
        """
        Consulte dados de títulos públicos e outros instrumentos de renda fixa brasileira.
        """
        return AsyncTreasuryResourceWithStreamingResponse(self._v2.treasury)

    @cached_property
    def debentures(self) -> AsyncDebenturesResourceWithStreamingResponse:
        """
        Consulte dados de títulos públicos e outros instrumentos de renda fixa brasileira.
        """
        return AsyncDebenturesResourceWithStreamingResponse(self._v2.debentures)

    @cached_property
    def news(self) -> AsyncNewsResourceWithStreamingResponse:
        """
        Notícias de empresas da B3 e do mercado, com resumo, sentimento, importância e ativos citados.
        """
        return AsyncNewsResourceWithStreamingResponse(self._v2.news)

    @cached_property
    def user(self) -> AsyncUserResourceWithStreamingResponse:
        """Dados da conta autenticada, como plano atual e uso da janela vigente."""
        return AsyncUserResourceWithStreamingResponse(self._v2.user)
