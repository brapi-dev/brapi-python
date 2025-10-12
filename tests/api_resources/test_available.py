# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from brapi import Brapi, AsyncBrapi
from brapi.types import AvailableListResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAvailable:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Brapi) -> None:
        available = client.available.list()
        assert_matches_type(AvailableListResponse, available, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Brapi) -> None:
        available = client.available.list(
            token="token",
            search="search",
        )
        assert_matches_type(AvailableListResponse, available, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Brapi) -> None:
        response = client.available.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        available = response.parse()
        assert_matches_type(AvailableListResponse, available, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Brapi) -> None:
        with client.available.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            available = response.parse()
            assert_matches_type(AvailableListResponse, available, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAvailable:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBrapi) -> None:
        available = await async_client.available.list()
        assert_matches_type(AvailableListResponse, available, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBrapi) -> None:
        available = await async_client.available.list(
            token="token",
            search="search",
        )
        assert_matches_type(AvailableListResponse, available, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBrapi) -> None:
        response = await async_client.available.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        available = await response.parse()
        assert_matches_type(AvailableListResponse, available, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBrapi) -> None:
        async with async_client.available.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            available = await response.parse()
            assert_matches_type(AvailableListResponse, available, path=["response"])

        assert cast(Any, response.is_closed) is True
