# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from brapi import Brapi, AsyncBrapi
from tests.utils import assert_matches_type
from brapi.types.v2 import UserUsageResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUser:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_usage(self, client: Brapi) -> None:
        user = client.v2.user.usage()
        assert_matches_type(UserUsageResponse, user, path=["response"])

    @parametrize
    def test_method_usage_with_all_params(self, client: Brapi) -> None:
        user = client.v2.user.usage(
            format="json",
        )
        assert_matches_type(UserUsageResponse, user, path=["response"])

    @parametrize
    def test_raw_response_usage(self, client: Brapi) -> None:
        response = client.v2.user.with_raw_response.usage()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserUsageResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_usage(self, client: Brapi) -> None:
        with client.v2.user.with_streaming_response.usage() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserUsageResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUser:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_usage(self, async_client: AsyncBrapi) -> None:
        user = await async_client.v2.user.usage()
        assert_matches_type(UserUsageResponse, user, path=["response"])

    @parametrize
    async def test_method_usage_with_all_params(self, async_client: AsyncBrapi) -> None:
        user = await async_client.v2.user.usage(
            format="json",
        )
        assert_matches_type(UserUsageResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_usage(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.user.with_raw_response.usage()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserUsageResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_usage(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.user.with_streaming_response.usage() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserUsageResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True
