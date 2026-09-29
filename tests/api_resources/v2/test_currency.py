# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from brapi import Brapi, AsyncBrapi
from tests.utils import assert_matches_type
from brapi.types.v2 import (
    CurrencyRetrieveResponse,
    CurrencyHistoricalResponse,
    CurrencyListAvailableResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCurrency:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Brapi) -> None:
        currency = client.v2.currency.retrieve()
        assert_matches_type(CurrencyRetrieveResponse, currency, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Brapi) -> None:
        currency = client.v2.currency.retrieve(
            currency="USD-BRL",
        )
        assert_matches_type(CurrencyRetrieveResponse, currency, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Brapi) -> None:
        response = client.v2.currency.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(CurrencyRetrieveResponse, currency, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Brapi) -> None:
        with client.v2.currency.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(CurrencyRetrieveResponse, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_historical(self, client: Brapi) -> None:
        currency = client.v2.currency.historical(
            currency="USD-BRL,EUR-BRL",
        )
        assert_matches_type(CurrencyHistoricalResponse, currency, path=["response"])

    @parametrize
    def test_method_historical_with_all_params(self, client: Brapi) -> None:
        currency = client.v2.currency.historical(
            currency="USD-BRL,EUR-BRL",
            end_date="2024-12-31",
            limit=365,
            sort_order="desc",
            start_date="2024-01-01",
        )
        assert_matches_type(CurrencyHistoricalResponse, currency, path=["response"])

    @parametrize
    def test_raw_response_historical(self, client: Brapi) -> None:
        response = client.v2.currency.with_raw_response.historical(
            currency="USD-BRL,EUR-BRL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(CurrencyHistoricalResponse, currency, path=["response"])

    @parametrize
    def test_streaming_response_historical(self, client: Brapi) -> None:
        with client.v2.currency.with_streaming_response.historical(
            currency="USD-BRL,EUR-BRL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(CurrencyHistoricalResponse, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_available(self, client: Brapi) -> None:
        currency = client.v2.currency.list_available()
        assert_matches_type(CurrencyListAvailableResponse, currency, path=["response"])

    @parametrize
    def test_method_list_available_with_all_params(self, client: Brapi) -> None:
        currency = client.v2.currency.list_available(
            search="USD",
        )
        assert_matches_type(CurrencyListAvailableResponse, currency, path=["response"])

    @parametrize
    def test_raw_response_list_available(self, client: Brapi) -> None:
        response = client.v2.currency.with_raw_response.list_available()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(CurrencyListAvailableResponse, currency, path=["response"])

    @parametrize
    def test_streaming_response_list_available(self, client: Brapi) -> None:
        with client.v2.currency.with_streaming_response.list_available() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(CurrencyListAvailableResponse, currency, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCurrency:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBrapi) -> None:
        currency = await async_client.v2.currency.retrieve()
        assert_matches_type(CurrencyRetrieveResponse, currency, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncBrapi) -> None:
        currency = await async_client.v2.currency.retrieve(
            currency="USD-BRL",
        )
        assert_matches_type(CurrencyRetrieveResponse, currency, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.currency.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(CurrencyRetrieveResponse, currency, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.currency.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(CurrencyRetrieveResponse, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_historical(self, async_client: AsyncBrapi) -> None:
        currency = await async_client.v2.currency.historical(
            currency="USD-BRL,EUR-BRL",
        )
        assert_matches_type(CurrencyHistoricalResponse, currency, path=["response"])

    @parametrize
    async def test_method_historical_with_all_params(self, async_client: AsyncBrapi) -> None:
        currency = await async_client.v2.currency.historical(
            currency="USD-BRL,EUR-BRL",
            end_date="2024-12-31",
            limit=365,
            sort_order="desc",
            start_date="2024-01-01",
        )
        assert_matches_type(CurrencyHistoricalResponse, currency, path=["response"])

    @parametrize
    async def test_raw_response_historical(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.currency.with_raw_response.historical(
            currency="USD-BRL,EUR-BRL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(CurrencyHistoricalResponse, currency, path=["response"])

    @parametrize
    async def test_streaming_response_historical(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.currency.with_streaming_response.historical(
            currency="USD-BRL,EUR-BRL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(CurrencyHistoricalResponse, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_available(self, async_client: AsyncBrapi) -> None:
        currency = await async_client.v2.currency.list_available()
        assert_matches_type(CurrencyListAvailableResponse, currency, path=["response"])

    @parametrize
    async def test_method_list_available_with_all_params(self, async_client: AsyncBrapi) -> None:
        currency = await async_client.v2.currency.list_available(
            search="USD",
        )
        assert_matches_type(CurrencyListAvailableResponse, currency, path=["response"])

    @parametrize
    async def test_raw_response_list_available(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.currency.with_raw_response.list_available()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(CurrencyListAvailableResponse, currency, path=["response"])

    @parametrize
    async def test_streaming_response_list_available(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.currency.with_streaming_response.list_available() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(CurrencyListAvailableResponse, currency, path=["response"])

        assert cast(Any, response.is_closed) is True
