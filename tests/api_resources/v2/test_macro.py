# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from brapi import Brapi, AsyncBrapi
from tests.utils import assert_matches_type
from brapi.types.v2 import (
    MacroLatestResponse,
    MacroRetrieveResponse,
    MacroListAvailableResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMacro:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Brapi) -> None:
        macro = client.v2.macro.retrieve(
            symbols="selic,ipca",
        )
        assert_matches_type(MacroRetrieveResponse, macro, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Brapi) -> None:
        macro = client.v2.macro.retrieve(
            symbols="selic,ipca",
            end_date="2026-04-30",
            limit=20,
            sort_order="desc",
            start_date="2025-01-01",
        )
        assert_matches_type(MacroRetrieveResponse, macro, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Brapi) -> None:
        response = client.v2.macro.with_raw_response.retrieve(
            symbols="selic,ipca",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        macro = response.parse()
        assert_matches_type(MacroRetrieveResponse, macro, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Brapi) -> None:
        with client.v2.macro.with_streaming_response.retrieve(
            symbols="selic,ipca",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            macro = response.parse()
            assert_matches_type(MacroRetrieveResponse, macro, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_latest(self, client: Brapi) -> None:
        macro = client.v2.macro.latest()
        assert_matches_type(MacroLatestResponse, macro, path=["response"])

    @parametrize
    def test_method_latest_with_all_params(self, client: Brapi) -> None:
        macro = client.v2.macro.latest(
            symbols="selic,cdi,ipca",
        )
        assert_matches_type(MacroLatestResponse, macro, path=["response"])

    @parametrize
    def test_raw_response_latest(self, client: Brapi) -> None:
        response = client.v2.macro.with_raw_response.latest()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        macro = response.parse()
        assert_matches_type(MacroLatestResponse, macro, path=["response"])

    @parametrize
    def test_streaming_response_latest(self, client: Brapi) -> None:
        with client.v2.macro.with_streaming_response.latest() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            macro = response.parse()
            assert_matches_type(MacroLatestResponse, macro, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_available(self, client: Brapi) -> None:
        macro = client.v2.macro.list_available()
        assert_matches_type(MacroListAvailableResponse, macro, path=["response"])

    @parametrize
    def test_method_list_available_with_all_params(self, client: Brapi) -> None:
        macro = client.v2.macro.list_available(
            category="interestRate",
            q="juros",
        )
        assert_matches_type(MacroListAvailableResponse, macro, path=["response"])

    @parametrize
    def test_raw_response_list_available(self, client: Brapi) -> None:
        response = client.v2.macro.with_raw_response.list_available()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        macro = response.parse()
        assert_matches_type(MacroListAvailableResponse, macro, path=["response"])

    @parametrize
    def test_streaming_response_list_available(self, client: Brapi) -> None:
        with client.v2.macro.with_streaming_response.list_available() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            macro = response.parse()
            assert_matches_type(MacroListAvailableResponse, macro, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMacro:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBrapi) -> None:
        macro = await async_client.v2.macro.retrieve(
            symbols="selic,ipca",
        )
        assert_matches_type(MacroRetrieveResponse, macro, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncBrapi) -> None:
        macro = await async_client.v2.macro.retrieve(
            symbols="selic,ipca",
            end_date="2026-04-30",
            limit=20,
            sort_order="desc",
            start_date="2025-01-01",
        )
        assert_matches_type(MacroRetrieveResponse, macro, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.macro.with_raw_response.retrieve(
            symbols="selic,ipca",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        macro = await response.parse()
        assert_matches_type(MacroRetrieveResponse, macro, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.macro.with_streaming_response.retrieve(
            symbols="selic,ipca",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            macro = await response.parse()
            assert_matches_type(MacroRetrieveResponse, macro, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_latest(self, async_client: AsyncBrapi) -> None:
        macro = await async_client.v2.macro.latest()
        assert_matches_type(MacroLatestResponse, macro, path=["response"])

    @parametrize
    async def test_method_latest_with_all_params(self, async_client: AsyncBrapi) -> None:
        macro = await async_client.v2.macro.latest(
            symbols="selic,cdi,ipca",
        )
        assert_matches_type(MacroLatestResponse, macro, path=["response"])

    @parametrize
    async def test_raw_response_latest(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.macro.with_raw_response.latest()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        macro = await response.parse()
        assert_matches_type(MacroLatestResponse, macro, path=["response"])

    @parametrize
    async def test_streaming_response_latest(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.macro.with_streaming_response.latest() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            macro = await response.parse()
            assert_matches_type(MacroLatestResponse, macro, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_available(self, async_client: AsyncBrapi) -> None:
        macro = await async_client.v2.macro.list_available()
        assert_matches_type(MacroListAvailableResponse, macro, path=["response"])

    @parametrize
    async def test_method_list_available_with_all_params(self, async_client: AsyncBrapi) -> None:
        macro = await async_client.v2.macro.list_available(
            category="interestRate",
            q="juros",
        )
        assert_matches_type(MacroListAvailableResponse, macro, path=["response"])

    @parametrize
    async def test_raw_response_list_available(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.macro.with_raw_response.list_available()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        macro = await response.parse()
        assert_matches_type(MacroListAvailableResponse, macro, path=["response"])

    @parametrize
    async def test_streaming_response_list_available(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.macro.with_streaming_response.list_available() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            macro = await response.parse()
            assert_matches_type(MacroListAvailableResponse, macro, path=["response"])

        assert cast(Any, response.is_closed) is True
