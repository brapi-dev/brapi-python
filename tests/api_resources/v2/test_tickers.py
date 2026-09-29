# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from brapi import Brapi, AsyncBrapi
from tests.utils import assert_matches_type
from brapi.types.v2 import (
    TickerListResponse,
    TickerRenamesResponse,
    TickerResolveResponse,
    TickerCoverageResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTickers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Brapi) -> None:
        ticker = client.v2.tickers.list()
        assert_matches_type(TickerListResponse, ticker, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Brapi) -> None:
        ticker = client.v2.tickers.list(
            limit=20,
            page=1,
            search="PETR",
            sector="Finance",
            sort_by="volume",
            sort_order="desc",
            subsector="Comércio",
            sub_type="fii",
            type="stock",
        )
        assert_matches_type(TickerListResponse, ticker, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Brapi) -> None:
        response = client.v2.tickers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticker = response.parse()
        assert_matches_type(TickerListResponse, ticker, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Brapi) -> None:
        with client.v2.tickers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticker = response.parse()
            assert_matches_type(TickerListResponse, ticker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_coverage(self, client: Brapi) -> None:
        ticker = client.v2.tickers.coverage(
            symbols="PETR4,MXRF11,VVAR3",
        )
        assert_matches_type(TickerCoverageResponse, ticker, path=["response"])

    @parametrize
    def test_raw_response_coverage(self, client: Brapi) -> None:
        response = client.v2.tickers.with_raw_response.coverage(
            symbols="PETR4,MXRF11,VVAR3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticker = response.parse()
        assert_matches_type(TickerCoverageResponse, ticker, path=["response"])

    @parametrize
    def test_streaming_response_coverage(self, client: Brapi) -> None:
        with client.v2.tickers.with_streaming_response.coverage(
            symbols="PETR4,MXRF11,VVAR3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticker = response.parse()
            assert_matches_type(TickerCoverageResponse, ticker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_renames(self, client: Brapi) -> None:
        ticker = client.v2.tickers.renames()
        assert_matches_type(TickerRenamesResponse, ticker, path=["response"])

    @parametrize
    def test_method_renames_with_all_params(self, client: Brapi) -> None:
        ticker = client.v2.tickers.renames(
            end_date="2026-12-31",
            search="BHIA",
            start_date="2024-01-01",
            symbols="VVAR3,BHIA3",
        )
        assert_matches_type(TickerRenamesResponse, ticker, path=["response"])

    @parametrize
    def test_raw_response_renames(self, client: Brapi) -> None:
        response = client.v2.tickers.with_raw_response.renames()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticker = response.parse()
        assert_matches_type(TickerRenamesResponse, ticker, path=["response"])

    @parametrize
    def test_streaming_response_renames(self, client: Brapi) -> None:
        with client.v2.tickers.with_streaming_response.renames() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticker = response.parse()
            assert_matches_type(TickerRenamesResponse, ticker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_resolve(self, client: Brapi) -> None:
        ticker = client.v2.tickers.resolve(
            symbols="VVAR3,PETR4",
        )
        assert_matches_type(TickerResolveResponse, ticker, path=["response"])

    @parametrize
    def test_raw_response_resolve(self, client: Brapi) -> None:
        response = client.v2.tickers.with_raw_response.resolve(
            symbols="VVAR3,PETR4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticker = response.parse()
        assert_matches_type(TickerResolveResponse, ticker, path=["response"])

    @parametrize
    def test_streaming_response_resolve(self, client: Brapi) -> None:
        with client.v2.tickers.with_streaming_response.resolve(
            symbols="VVAR3,PETR4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticker = response.parse()
            assert_matches_type(TickerResolveResponse, ticker, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTickers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncBrapi) -> None:
        ticker = await async_client.v2.tickers.list()
        assert_matches_type(TickerListResponse, ticker, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBrapi) -> None:
        ticker = await async_client.v2.tickers.list(
            limit=20,
            page=1,
            search="PETR",
            sector="Finance",
            sort_by="volume",
            sort_order="desc",
            subsector="Comércio",
            sub_type="fii",
            type="stock",
        )
        assert_matches_type(TickerListResponse, ticker, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.tickers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticker = await response.parse()
        assert_matches_type(TickerListResponse, ticker, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.tickers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticker = await response.parse()
            assert_matches_type(TickerListResponse, ticker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_coverage(self, async_client: AsyncBrapi) -> None:
        ticker = await async_client.v2.tickers.coverage(
            symbols="PETR4,MXRF11,VVAR3",
        )
        assert_matches_type(TickerCoverageResponse, ticker, path=["response"])

    @parametrize
    async def test_raw_response_coverage(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.tickers.with_raw_response.coverage(
            symbols="PETR4,MXRF11,VVAR3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticker = await response.parse()
        assert_matches_type(TickerCoverageResponse, ticker, path=["response"])

    @parametrize
    async def test_streaming_response_coverage(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.tickers.with_streaming_response.coverage(
            symbols="PETR4,MXRF11,VVAR3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticker = await response.parse()
            assert_matches_type(TickerCoverageResponse, ticker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_renames(self, async_client: AsyncBrapi) -> None:
        ticker = await async_client.v2.tickers.renames()
        assert_matches_type(TickerRenamesResponse, ticker, path=["response"])

    @parametrize
    async def test_method_renames_with_all_params(self, async_client: AsyncBrapi) -> None:
        ticker = await async_client.v2.tickers.renames(
            end_date="2026-12-31",
            search="BHIA",
            start_date="2024-01-01",
            symbols="VVAR3,BHIA3",
        )
        assert_matches_type(TickerRenamesResponse, ticker, path=["response"])

    @parametrize
    async def test_raw_response_renames(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.tickers.with_raw_response.renames()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticker = await response.parse()
        assert_matches_type(TickerRenamesResponse, ticker, path=["response"])

    @parametrize
    async def test_streaming_response_renames(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.tickers.with_streaming_response.renames() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticker = await response.parse()
            assert_matches_type(TickerRenamesResponse, ticker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_resolve(self, async_client: AsyncBrapi) -> None:
        ticker = await async_client.v2.tickers.resolve(
            symbols="VVAR3,PETR4",
        )
        assert_matches_type(TickerResolveResponse, ticker, path=["response"])

    @parametrize
    async def test_raw_response_resolve(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.tickers.with_raw_response.resolve(
            symbols="VVAR3,PETR4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticker = await response.parse()
        assert_matches_type(TickerResolveResponse, ticker, path=["response"])

    @parametrize
    async def test_streaming_response_resolve(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.tickers.with_streaming_response.resolve(
            symbols="VVAR3,PETR4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticker = await response.parse()
            assert_matches_type(TickerResolveResponse, ticker, path=["response"])

        assert cast(Any, response.is_closed) is True
