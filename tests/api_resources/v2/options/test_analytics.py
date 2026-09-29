# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from brapi import Brapi, AsyncBrapi
from tests.utils import assert_matches_type
from brapi.types.v2.options import (
    AnalyticsHistoryResponse,
    AnalyticsRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnalytics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Brapi) -> None:
        analytics = client.v2.options.analytics.retrieve(
            expiration_date="2026-12-18",
            underlying="PETR4",
        )
        assert_matches_type(AnalyticsRetrieveResponse, analytics, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Brapi) -> None:
        analytics = client.v2.options.analytics.retrieve(
            expiration_date="2026-12-18",
            underlying="PETR4",
            date="2026-06-01",
            limit=50,
            max_strike=0,
            min_strike=0,
            side="call",
        )
        assert_matches_type(AnalyticsRetrieveResponse, analytics, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Brapi) -> None:
        response = client.v2.options.analytics.with_raw_response.retrieve(
            expiration_date="2026-12-18",
            underlying="PETR4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(AnalyticsRetrieveResponse, analytics, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Brapi) -> None:
        with client.v2.options.analytics.with_streaming_response.retrieve(
            expiration_date="2026-12-18",
            underlying="PETR4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(AnalyticsRetrieveResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_history(self, client: Brapi) -> None:
        analytics = client.v2.options.analytics.history(
            expiration_date="2026-12-18",
            symbol="PETRF783",
        )
        assert_matches_type(AnalyticsHistoryResponse, analytics, path=["response"])

    @parametrize
    def test_method_history_with_all_params(self, client: Brapi) -> None:
        analytics = client.v2.options.analytics.history(
            expiration_date="2026-12-18",
            symbol="PETRF783",
            end_date="2026-06-01",
            sort_order="asc",
            start_date="2026-05-01",
            strike=7.29,
        )
        assert_matches_type(AnalyticsHistoryResponse, analytics, path=["response"])

    @parametrize
    def test_raw_response_history(self, client: Brapi) -> None:
        response = client.v2.options.analytics.with_raw_response.history(
            expiration_date="2026-12-18",
            symbol="PETRF783",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(AnalyticsHistoryResponse, analytics, path=["response"])

    @parametrize
    def test_streaming_response_history(self, client: Brapi) -> None:
        with client.v2.options.analytics.with_streaming_response.history(
            expiration_date="2026-12-18",
            symbol="PETRF783",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(AnalyticsHistoryResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAnalytics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBrapi) -> None:
        analytics = await async_client.v2.options.analytics.retrieve(
            expiration_date="2026-12-18",
            underlying="PETR4",
        )
        assert_matches_type(AnalyticsRetrieveResponse, analytics, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncBrapi) -> None:
        analytics = await async_client.v2.options.analytics.retrieve(
            expiration_date="2026-12-18",
            underlying="PETR4",
            date="2026-06-01",
            limit=50,
            max_strike=0,
            min_strike=0,
            side="call",
        )
        assert_matches_type(AnalyticsRetrieveResponse, analytics, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.options.analytics.with_raw_response.retrieve(
            expiration_date="2026-12-18",
            underlying="PETR4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(AnalyticsRetrieveResponse, analytics, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.options.analytics.with_streaming_response.retrieve(
            expiration_date="2026-12-18",
            underlying="PETR4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(AnalyticsRetrieveResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_history(self, async_client: AsyncBrapi) -> None:
        analytics = await async_client.v2.options.analytics.history(
            expiration_date="2026-12-18",
            symbol="PETRF783",
        )
        assert_matches_type(AnalyticsHistoryResponse, analytics, path=["response"])

    @parametrize
    async def test_method_history_with_all_params(self, async_client: AsyncBrapi) -> None:
        analytics = await async_client.v2.options.analytics.history(
            expiration_date="2026-12-18",
            symbol="PETRF783",
            end_date="2026-06-01",
            sort_order="asc",
            start_date="2026-05-01",
            strike=7.29,
        )
        assert_matches_type(AnalyticsHistoryResponse, analytics, path=["response"])

    @parametrize
    async def test_raw_response_history(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.options.analytics.with_raw_response.history(
            expiration_date="2026-12-18",
            symbol="PETRF783",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(AnalyticsHistoryResponse, analytics, path=["response"])

    @parametrize
    async def test_streaming_response_history(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.options.analytics.with_streaming_response.history(
            expiration_date="2026-12-18",
            symbol="PETRF783",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(AnalyticsHistoryResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True
