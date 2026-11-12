# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from brapi import Brapi, AsyncBrapi
from tests.utils import assert_matches_type
from brapi.types.v2 import IndexListResponse, IndexCompositionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIndexes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Brapi) -> None:
        index = client.v2.indexes.list()
        assert_matches_type(IndexListResponse, index, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Brapi) -> None:
        index = client.v2.indexes.list(
            search="ibov",
        )
        assert_matches_type(IndexListResponse, index, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Brapi) -> None:
        response = client.v2.indexes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(IndexListResponse, index, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Brapi) -> None:
        with client.v2.indexes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(IndexListResponse, index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_composition(self, client: Brapi) -> None:
        index = client.v2.indexes.composition(
            symbols="IBOV",
        )
        assert_matches_type(IndexCompositionResponse, index, path=["response"])

    @parametrize
    def test_method_composition_with_all_params(self, client: Brapi) -> None:
        index = client.v2.indexes.composition(
            symbols="IBOV",
            limit=2,
            page=1,
        )
        assert_matches_type(IndexCompositionResponse, index, path=["response"])

    @parametrize
    def test_raw_response_composition(self, client: Brapi) -> None:
        response = client.v2.indexes.with_raw_response.composition(
            symbols="IBOV",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(IndexCompositionResponse, index, path=["response"])

    @parametrize
    def test_streaming_response_composition(self, client: Brapi) -> None:
        with client.v2.indexes.with_streaming_response.composition(
            symbols="IBOV",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(IndexCompositionResponse, index, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIndexes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncBrapi) -> None:
        index = await async_client.v2.indexes.list()
        assert_matches_type(IndexListResponse, index, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBrapi) -> None:
        index = await async_client.v2.indexes.list(
            search="ibov",
        )
        assert_matches_type(IndexListResponse, index, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.indexes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(IndexListResponse, index, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.indexes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(IndexListResponse, index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_composition(self, async_client: AsyncBrapi) -> None:
        index = await async_client.v2.indexes.composition(
            symbols="IBOV",
        )
        assert_matches_type(IndexCompositionResponse, index, path=["response"])

    @parametrize
    async def test_method_composition_with_all_params(self, async_client: AsyncBrapi) -> None:
        index = await async_client.v2.indexes.composition(
            symbols="IBOV",
            limit=2,
            page=1,
        )
        assert_matches_type(IndexCompositionResponse, index, path=["response"])

    @parametrize
    async def test_raw_response_composition(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.indexes.with_raw_response.composition(
            symbols="IBOV",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(IndexCompositionResponse, index, path=["response"])

    @parametrize
    async def test_streaming_response_composition(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.indexes.with_streaming_response.composition(
            symbols="IBOV",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(IndexCompositionResponse, index, path=["response"])

        assert cast(Any, response.is_closed) is True
