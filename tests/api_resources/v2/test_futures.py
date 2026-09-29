# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from brapi import Brapi, AsyncBrapi
from tests.utils import assert_matches_type
from brapi.types.v2 import (
    FutureListResponse,
    FutureQuoteResponse,
    FutureSpecsResponse,
    FutureHistoricalResponse,
    FutureTermStructureResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFutures:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Brapi) -> None:
        future = client.v2.futures.list()
        assert_matches_type(FutureListResponse, future, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Brapi) -> None:
        future = client.v2.futures.list(
            asset="BGI",
            include_expired="true",
            limit=1,
            page=1,
            segment="financial",
            sort_by="symbol",
            sort_order="asc",
        )
        assert_matches_type(FutureListResponse, future, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Brapi) -> None:
        response = client.v2.futures.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        future = response.parse()
        assert_matches_type(FutureListResponse, future, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Brapi) -> None:
        with client.v2.futures.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            future = response.parse()
            assert_matches_type(FutureListResponse, future, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_historical(self, client: Brapi) -> None:
        future = client.v2.futures.historical(
            symbol="WINM26",
        )
        assert_matches_type(FutureHistoricalResponse, future, path=["response"])

    @parametrize
    def test_method_historical_with_all_params(self, client: Brapi) -> None:
        future = client.v2.futures.historical(
            symbol="WINM26",
            end_date="endDate",
            sort_order="asc",
            start_date="startDate",
        )
        assert_matches_type(FutureHistoricalResponse, future, path=["response"])

    @parametrize
    def test_raw_response_historical(self, client: Brapi) -> None:
        response = client.v2.futures.with_raw_response.historical(
            symbol="WINM26",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        future = response.parse()
        assert_matches_type(FutureHistoricalResponse, future, path=["response"])

    @parametrize
    def test_streaming_response_historical(self, client: Brapi) -> None:
        with client.v2.futures.with_streaming_response.historical(
            symbol="WINM26",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            future = response.parse()
            assert_matches_type(FutureHistoricalResponse, future, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_quote(self, client: Brapi) -> None:
        future = client.v2.futures.quote(
            symbols="WINM26,BGIF27,DI1F27",
        )
        assert_matches_type(FutureQuoteResponse, future, path=["response"])

    @parametrize
    def test_raw_response_quote(self, client: Brapi) -> None:
        response = client.v2.futures.with_raw_response.quote(
            symbols="WINM26,BGIF27,DI1F27",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        future = response.parse()
        assert_matches_type(FutureQuoteResponse, future, path=["response"])

    @parametrize
    def test_streaming_response_quote(self, client: Brapi) -> None:
        with client.v2.futures.with_streaming_response.quote(
            symbols="WINM26,BGIF27,DI1F27",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            future = response.parse()
            assert_matches_type(FutureQuoteResponse, future, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_specs(self, client: Brapi) -> None:
        future = client.v2.futures.specs(
            symbols="WINM26,BGIF27,DI1F27",
        )
        assert_matches_type(FutureSpecsResponse, future, path=["response"])

    @parametrize
    def test_raw_response_specs(self, client: Brapi) -> None:
        response = client.v2.futures.with_raw_response.specs(
            symbols="WINM26,BGIF27,DI1F27",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        future = response.parse()
        assert_matches_type(FutureSpecsResponse, future, path=["response"])

    @parametrize
    def test_streaming_response_specs(self, client: Brapi) -> None:
        with client.v2.futures.with_streaming_response.specs(
            symbols="WINM26,BGIF27,DI1F27",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            future = response.parse()
            assert_matches_type(FutureSpecsResponse, future, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_term_structure(self, client: Brapi) -> None:
        future = client.v2.futures.term_structure(
            asset="BGI",
        )
        assert_matches_type(FutureTermStructureResponse, future, path=["response"])

    @parametrize
    def test_method_term_structure_with_all_params(self, client: Brapi) -> None:
        future = client.v2.futures.term_structure(
            asset="BGI",
            include_expired="true",
        )
        assert_matches_type(FutureTermStructureResponse, future, path=["response"])

    @parametrize
    def test_raw_response_term_structure(self, client: Brapi) -> None:
        response = client.v2.futures.with_raw_response.term_structure(
            asset="BGI",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        future = response.parse()
        assert_matches_type(FutureTermStructureResponse, future, path=["response"])

    @parametrize
    def test_streaming_response_term_structure(self, client: Brapi) -> None:
        with client.v2.futures.with_streaming_response.term_structure(
            asset="BGI",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            future = response.parse()
            assert_matches_type(FutureTermStructureResponse, future, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFutures:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncBrapi) -> None:
        future = await async_client.v2.futures.list()
        assert_matches_type(FutureListResponse, future, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBrapi) -> None:
        future = await async_client.v2.futures.list(
            asset="BGI",
            include_expired="true",
            limit=1,
            page=1,
            segment="financial",
            sort_by="symbol",
            sort_order="asc",
        )
        assert_matches_type(FutureListResponse, future, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.futures.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        future = await response.parse()
        assert_matches_type(FutureListResponse, future, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.futures.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            future = await response.parse()
            assert_matches_type(FutureListResponse, future, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_historical(self, async_client: AsyncBrapi) -> None:
        future = await async_client.v2.futures.historical(
            symbol="WINM26",
        )
        assert_matches_type(FutureHistoricalResponse, future, path=["response"])

    @parametrize
    async def test_method_historical_with_all_params(self, async_client: AsyncBrapi) -> None:
        future = await async_client.v2.futures.historical(
            symbol="WINM26",
            end_date="endDate",
            sort_order="asc",
            start_date="startDate",
        )
        assert_matches_type(FutureHistoricalResponse, future, path=["response"])

    @parametrize
    async def test_raw_response_historical(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.futures.with_raw_response.historical(
            symbol="WINM26",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        future = await response.parse()
        assert_matches_type(FutureHistoricalResponse, future, path=["response"])

    @parametrize
    async def test_streaming_response_historical(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.futures.with_streaming_response.historical(
            symbol="WINM26",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            future = await response.parse()
            assert_matches_type(FutureHistoricalResponse, future, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_quote(self, async_client: AsyncBrapi) -> None:
        future = await async_client.v2.futures.quote(
            symbols="WINM26,BGIF27,DI1F27",
        )
        assert_matches_type(FutureQuoteResponse, future, path=["response"])

    @parametrize
    async def test_raw_response_quote(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.futures.with_raw_response.quote(
            symbols="WINM26,BGIF27,DI1F27",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        future = await response.parse()
        assert_matches_type(FutureQuoteResponse, future, path=["response"])

    @parametrize
    async def test_streaming_response_quote(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.futures.with_streaming_response.quote(
            symbols="WINM26,BGIF27,DI1F27",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            future = await response.parse()
            assert_matches_type(FutureQuoteResponse, future, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_specs(self, async_client: AsyncBrapi) -> None:
        future = await async_client.v2.futures.specs(
            symbols="WINM26,BGIF27,DI1F27",
        )
        assert_matches_type(FutureSpecsResponse, future, path=["response"])

    @parametrize
    async def test_raw_response_specs(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.futures.with_raw_response.specs(
            symbols="WINM26,BGIF27,DI1F27",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        future = await response.parse()
        assert_matches_type(FutureSpecsResponse, future, path=["response"])

    @parametrize
    async def test_streaming_response_specs(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.futures.with_streaming_response.specs(
            symbols="WINM26,BGIF27,DI1F27",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            future = await response.parse()
            assert_matches_type(FutureSpecsResponse, future, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_term_structure(self, async_client: AsyncBrapi) -> None:
        future = await async_client.v2.futures.term_structure(
            asset="BGI",
        )
        assert_matches_type(FutureTermStructureResponse, future, path=["response"])

    @parametrize
    async def test_method_term_structure_with_all_params(self, async_client: AsyncBrapi) -> None:
        future = await async_client.v2.futures.term_structure(
            asset="BGI",
            include_expired="true",
        )
        assert_matches_type(FutureTermStructureResponse, future, path=["response"])

    @parametrize
    async def test_raw_response_term_structure(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.futures.with_raw_response.term_structure(
            asset="BGI",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        future = await response.parse()
        assert_matches_type(FutureTermStructureResponse, future, path=["response"])

    @parametrize
    async def test_streaming_response_term_structure(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.futures.with_streaming_response.term_structure(
            asset="BGI",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            future = await response.parse()
            assert_matches_type(FutureTermStructureResponse, future, path=["response"])

        assert cast(Any, response.is_closed) is True
