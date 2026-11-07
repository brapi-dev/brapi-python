# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from brapi import Brapi, AsyncBrapi
from tests.utils import assert_matches_type
from brapi.types.v2 import (
    NewsListResponse,
    NewsMarketResponse,
    NewsRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNews:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Brapi) -> None:
        news = client.v2.news.retrieve(
            "petrobras-aprova-dividendos-de-r-20-bilhoes-a3f9c1",
        )
        assert_matches_type(NewsRetrieveResponse, news, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Brapi) -> None:
        response = client.v2.news.with_raw_response.retrieve(
            "petrobras-aprova-dividendos-de-r-20-bilhoes-a3f9c1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news = response.parse()
        assert_matches_type(NewsRetrieveResponse, news, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Brapi) -> None:
        with client.v2.news.with_streaming_response.retrieve(
            "petrobras-aprova-dividendos-de-r-20-bilhoes-a3f9c1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news = response.parse()
            assert_matches_type(NewsRetrieveResponse, news, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Brapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v2.news.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Brapi) -> None:
        news = client.v2.news.list()
        assert_matches_type(NewsListResponse, news, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Brapi) -> None:
        news = client.v2.news.list(
            cursor="x",
            event_types="earnings",
            from_="2026-11-01",
            include_article="true",
            limit=20,
            min_importance=3,
            sentiment="positive",
            tickers="PETR4,VALE3",
            to="2026-11-06",
        )
        assert_matches_type(NewsListResponse, news, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Brapi) -> None:
        response = client.v2.news.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news = response.parse()
        assert_matches_type(NewsListResponse, news, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Brapi) -> None:
        with client.v2.news.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news = response.parse()
            assert_matches_type(NewsListResponse, news, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_market(self, client: Brapi) -> None:
        news = client.v2.news.market()
        assert_matches_type(NewsMarketResponse, news, path=["response"])

    @parametrize
    def test_method_market_with_all_params(self, client: Brapi) -> None:
        news = client.v2.news.market(
            cursor="x",
            event_types="earnings",
            from_="2026-11-01",
            include_article="true",
            limit=20,
            min_importance=3,
            sentiment="positive",
            to="2026-11-06",
        )
        assert_matches_type(NewsMarketResponse, news, path=["response"])

    @parametrize
    def test_raw_response_market(self, client: Brapi) -> None:
        response = client.v2.news.with_raw_response.market()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news = response.parse()
        assert_matches_type(NewsMarketResponse, news, path=["response"])

    @parametrize
    def test_streaming_response_market(self, client: Brapi) -> None:
        with client.v2.news.with_streaming_response.market() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news = response.parse()
            assert_matches_type(NewsMarketResponse, news, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNews:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBrapi) -> None:
        news = await async_client.v2.news.retrieve(
            "petrobras-aprova-dividendos-de-r-20-bilhoes-a3f9c1",
        )
        assert_matches_type(NewsRetrieveResponse, news, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.news.with_raw_response.retrieve(
            "petrobras-aprova-dividendos-de-r-20-bilhoes-a3f9c1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news = await response.parse()
        assert_matches_type(NewsRetrieveResponse, news, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.news.with_streaming_response.retrieve(
            "petrobras-aprova-dividendos-de-r-20-bilhoes-a3f9c1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news = await response.parse()
            assert_matches_type(NewsRetrieveResponse, news, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBrapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v2.news.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncBrapi) -> None:
        news = await async_client.v2.news.list()
        assert_matches_type(NewsListResponse, news, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBrapi) -> None:
        news = await async_client.v2.news.list(
            cursor="x",
            event_types="earnings",
            from_="2026-11-01",
            include_article="true",
            limit=20,
            min_importance=3,
            sentiment="positive",
            tickers="PETR4,VALE3",
            to="2026-11-06",
        )
        assert_matches_type(NewsListResponse, news, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.news.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news = await response.parse()
        assert_matches_type(NewsListResponse, news, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.news.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news = await response.parse()
            assert_matches_type(NewsListResponse, news, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_market(self, async_client: AsyncBrapi) -> None:
        news = await async_client.v2.news.market()
        assert_matches_type(NewsMarketResponse, news, path=["response"])

    @parametrize
    async def test_method_market_with_all_params(self, async_client: AsyncBrapi) -> None:
        news = await async_client.v2.news.market(
            cursor="x",
            event_types="earnings",
            from_="2026-11-01",
            include_article="true",
            limit=20,
            min_importance=3,
            sentiment="positive",
            to="2026-11-06",
        )
        assert_matches_type(NewsMarketResponse, news, path=["response"])

    @parametrize
    async def test_raw_response_market(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.news.with_raw_response.market()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news = await response.parse()
        assert_matches_type(NewsMarketResponse, news, path=["response"])

    @parametrize
    async def test_streaming_response_market(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.news.with_streaming_response.market() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news = await response.parse()
            assert_matches_type(NewsMarketResponse, news, path=["response"])

        assert cast(Any, response.is_closed) is True
