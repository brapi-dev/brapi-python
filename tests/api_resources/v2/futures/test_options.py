# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from brapi import Brapi, AsyncBrapi
from tests.utils import assert_matches_type
from brapi.types.v2.futures import (
    OptionChainResponse,
    OptionStrikesResponse,
    OptionHistoricalResponse,
    OptionExpirationsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_chain(self, client: Brapi) -> None:
        option = client.v2.futures.options.chain(
            expiration_date="2027-08-31",
            underlying="BGI",
        )
        assert_matches_type(OptionChainResponse, option, path=["response"])

    @parametrize
    def test_method_chain_with_all_params(self, client: Brapi) -> None:
        option = client.v2.futures.options.chain(
            expiration_date="2027-08-31",
            underlying="BGI",
            date="date",
            max_strike=0,
            min_strike=0,
            side="call",
        )
        assert_matches_type(OptionChainResponse, option, path=["response"])

    @parametrize
    def test_raw_response_chain(self, client: Brapi) -> None:
        response = client.v2.futures.options.with_raw_response.chain(
            expiration_date="2027-08-31",
            underlying="BGI",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option = response.parse()
        assert_matches_type(OptionChainResponse, option, path=["response"])

    @parametrize
    def test_streaming_response_chain(self, client: Brapi) -> None:
        with client.v2.futures.options.with_streaming_response.chain(
            expiration_date="2027-08-31",
            underlying="BGI",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option = response.parse()
            assert_matches_type(OptionChainResponse, option, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_expirations(self, client: Brapi) -> None:
        option = client.v2.futures.options.expirations(
            underlying="BGI",
        )
        assert_matches_type(OptionExpirationsResponse, option, path=["response"])

    @parametrize
    def test_method_expirations_with_all_params(self, client: Brapi) -> None:
        option = client.v2.futures.options.expirations(
            underlying="BGI",
            include_expired="true",
        )
        assert_matches_type(OptionExpirationsResponse, option, path=["response"])

    @parametrize
    def test_raw_response_expirations(self, client: Brapi) -> None:
        response = client.v2.futures.options.with_raw_response.expirations(
            underlying="BGI",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option = response.parse()
        assert_matches_type(OptionExpirationsResponse, option, path=["response"])

    @parametrize
    def test_streaming_response_expirations(self, client: Brapi) -> None:
        with client.v2.futures.options.with_streaming_response.expirations(
            underlying="BGI",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option = response.parse()
            assert_matches_type(OptionExpirationsResponse, option, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_historical(self, client: Brapi) -> None:
        option = client.v2.futures.options.historical(
            symbol="BGIM26C028000",
        )
        assert_matches_type(OptionHistoricalResponse, option, path=["response"])

    @parametrize
    def test_method_historical_with_all_params(self, client: Brapi) -> None:
        option = client.v2.futures.options.historical(
            symbol="BGIM26C028000",
            end_date="2026-06-01",
            sort_order="asc",
            start_date="2026-05-01",
        )
        assert_matches_type(OptionHistoricalResponse, option, path=["response"])

    @parametrize
    def test_raw_response_historical(self, client: Brapi) -> None:
        response = client.v2.futures.options.with_raw_response.historical(
            symbol="BGIM26C028000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option = response.parse()
        assert_matches_type(OptionHistoricalResponse, option, path=["response"])

    @parametrize
    def test_streaming_response_historical(self, client: Brapi) -> None:
        with client.v2.futures.options.with_streaming_response.historical(
            symbol="BGIM26C028000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option = response.parse()
            assert_matches_type(OptionHistoricalResponse, option, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_strikes(self, client: Brapi) -> None:
        option = client.v2.futures.options.strikes(
            expiration_date="2027-08-31",
            underlying="BGI",
        )
        assert_matches_type(OptionStrikesResponse, option, path=["response"])

    @parametrize
    def test_method_strikes_with_all_params(self, client: Brapi) -> None:
        option = client.v2.futures.options.strikes(
            expiration_date="2027-08-31",
            underlying="BGI",
            side="call",
        )
        assert_matches_type(OptionStrikesResponse, option, path=["response"])

    @parametrize
    def test_raw_response_strikes(self, client: Brapi) -> None:
        response = client.v2.futures.options.with_raw_response.strikes(
            expiration_date="2027-08-31",
            underlying="BGI",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option = response.parse()
        assert_matches_type(OptionStrikesResponse, option, path=["response"])

    @parametrize
    def test_streaming_response_strikes(self, client: Brapi) -> None:
        with client.v2.futures.options.with_streaming_response.strikes(
            expiration_date="2027-08-31",
            underlying="BGI",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option = response.parse()
            assert_matches_type(OptionStrikesResponse, option, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOptions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_chain(self, async_client: AsyncBrapi) -> None:
        option = await async_client.v2.futures.options.chain(
            expiration_date="2027-08-31",
            underlying="BGI",
        )
        assert_matches_type(OptionChainResponse, option, path=["response"])

    @parametrize
    async def test_method_chain_with_all_params(self, async_client: AsyncBrapi) -> None:
        option = await async_client.v2.futures.options.chain(
            expiration_date="2027-08-31",
            underlying="BGI",
            date="date",
            max_strike=0,
            min_strike=0,
            side="call",
        )
        assert_matches_type(OptionChainResponse, option, path=["response"])

    @parametrize
    async def test_raw_response_chain(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.futures.options.with_raw_response.chain(
            expiration_date="2027-08-31",
            underlying="BGI",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option = await response.parse()
        assert_matches_type(OptionChainResponse, option, path=["response"])

    @parametrize
    async def test_streaming_response_chain(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.futures.options.with_streaming_response.chain(
            expiration_date="2027-08-31",
            underlying="BGI",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option = await response.parse()
            assert_matches_type(OptionChainResponse, option, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_expirations(self, async_client: AsyncBrapi) -> None:
        option = await async_client.v2.futures.options.expirations(
            underlying="BGI",
        )
        assert_matches_type(OptionExpirationsResponse, option, path=["response"])

    @parametrize
    async def test_method_expirations_with_all_params(self, async_client: AsyncBrapi) -> None:
        option = await async_client.v2.futures.options.expirations(
            underlying="BGI",
            include_expired="true",
        )
        assert_matches_type(OptionExpirationsResponse, option, path=["response"])

    @parametrize
    async def test_raw_response_expirations(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.futures.options.with_raw_response.expirations(
            underlying="BGI",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option = await response.parse()
        assert_matches_type(OptionExpirationsResponse, option, path=["response"])

    @parametrize
    async def test_streaming_response_expirations(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.futures.options.with_streaming_response.expirations(
            underlying="BGI",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option = await response.parse()
            assert_matches_type(OptionExpirationsResponse, option, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_historical(self, async_client: AsyncBrapi) -> None:
        option = await async_client.v2.futures.options.historical(
            symbol="BGIM26C028000",
        )
        assert_matches_type(OptionHistoricalResponse, option, path=["response"])

    @parametrize
    async def test_method_historical_with_all_params(self, async_client: AsyncBrapi) -> None:
        option = await async_client.v2.futures.options.historical(
            symbol="BGIM26C028000",
            end_date="2026-06-01",
            sort_order="asc",
            start_date="2026-05-01",
        )
        assert_matches_type(OptionHistoricalResponse, option, path=["response"])

    @parametrize
    async def test_raw_response_historical(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.futures.options.with_raw_response.historical(
            symbol="BGIM26C028000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option = await response.parse()
        assert_matches_type(OptionHistoricalResponse, option, path=["response"])

    @parametrize
    async def test_streaming_response_historical(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.futures.options.with_streaming_response.historical(
            symbol="BGIM26C028000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option = await response.parse()
            assert_matches_type(OptionHistoricalResponse, option, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_strikes(self, async_client: AsyncBrapi) -> None:
        option = await async_client.v2.futures.options.strikes(
            expiration_date="2027-08-31",
            underlying="BGI",
        )
        assert_matches_type(OptionStrikesResponse, option, path=["response"])

    @parametrize
    async def test_method_strikes_with_all_params(self, async_client: AsyncBrapi) -> None:
        option = await async_client.v2.futures.options.strikes(
            expiration_date="2027-08-31",
            underlying="BGI",
            side="call",
        )
        assert_matches_type(OptionStrikesResponse, option, path=["response"])

    @parametrize
    async def test_raw_response_strikes(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.futures.options.with_raw_response.strikes(
            expiration_date="2027-08-31",
            underlying="BGI",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option = await response.parse()
        assert_matches_type(OptionStrikesResponse, option, path=["response"])

    @parametrize
    async def test_streaming_response_strikes(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.futures.options.with_streaming_response.strikes(
            expiration_date="2027-08-31",
            underlying="BGI",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option = await response.parse()
            assert_matches_type(OptionStrikesResponse, option, path=["response"])

        assert cast(Any, response.is_closed) is True
