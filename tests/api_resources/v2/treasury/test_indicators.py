# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from brapi import Brapi, AsyncBrapi
from tests.utils import assert_matches_type
from brapi.types.v2.treasury import (
    IndicatorHistoryResponse,
    IndicatorRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIndicators:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Brapi) -> None:
        indicator = client.v2.treasury.indicators.retrieve(
            symbols="tesouro-selic-01032031,tesouro-ipca-15052035",
        )
        assert_matches_type(IndicatorRetrieveResponse, indicator, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Brapi) -> None:
        response = client.v2.treasury.indicators.with_raw_response.retrieve(
            symbols="tesouro-selic-01032031,tesouro-ipca-15052035",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator = response.parse()
        assert_matches_type(IndicatorRetrieveResponse, indicator, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Brapi) -> None:
        with client.v2.treasury.indicators.with_streaming_response.retrieve(
            symbols="tesouro-selic-01032031,tesouro-ipca-15052035",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator = response.parse()
            assert_matches_type(IndicatorRetrieveResponse, indicator, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_history(self, client: Brapi) -> None:
        indicator = client.v2.treasury.indicators.history(
            symbols="tesouro-selic-01032031,tesouro-ipca-15052035",
        )
        assert_matches_type(IndicatorHistoryResponse, indicator, path=["response"])

    @parametrize
    def test_method_history_with_all_params(self, client: Brapi) -> None:
        indicator = client.v2.treasury.indicators.history(
            symbols="tesouro-selic-01032031,tesouro-ipca-15052035",
            end_date="2026-05-15",
            sort_by="baseDate",
            sort_order="desc",
            start_date="2025-01-01",
        )
        assert_matches_type(IndicatorHistoryResponse, indicator, path=["response"])

    @parametrize
    def test_raw_response_history(self, client: Brapi) -> None:
        response = client.v2.treasury.indicators.with_raw_response.history(
            symbols="tesouro-selic-01032031,tesouro-ipca-15052035",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator = response.parse()
        assert_matches_type(IndicatorHistoryResponse, indicator, path=["response"])

    @parametrize
    def test_streaming_response_history(self, client: Brapi) -> None:
        with client.v2.treasury.indicators.with_streaming_response.history(
            symbols="tesouro-selic-01032031,tesouro-ipca-15052035",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator = response.parse()
            assert_matches_type(IndicatorHistoryResponse, indicator, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIndicators:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBrapi) -> None:
        indicator = await async_client.v2.treasury.indicators.retrieve(
            symbols="tesouro-selic-01032031,tesouro-ipca-15052035",
        )
        assert_matches_type(IndicatorRetrieveResponse, indicator, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.treasury.indicators.with_raw_response.retrieve(
            symbols="tesouro-selic-01032031,tesouro-ipca-15052035",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator = await response.parse()
        assert_matches_type(IndicatorRetrieveResponse, indicator, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.treasury.indicators.with_streaming_response.retrieve(
            symbols="tesouro-selic-01032031,tesouro-ipca-15052035",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator = await response.parse()
            assert_matches_type(IndicatorRetrieveResponse, indicator, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_history(self, async_client: AsyncBrapi) -> None:
        indicator = await async_client.v2.treasury.indicators.history(
            symbols="tesouro-selic-01032031,tesouro-ipca-15052035",
        )
        assert_matches_type(IndicatorHistoryResponse, indicator, path=["response"])

    @parametrize
    async def test_method_history_with_all_params(self, async_client: AsyncBrapi) -> None:
        indicator = await async_client.v2.treasury.indicators.history(
            symbols="tesouro-selic-01032031,tesouro-ipca-15052035",
            end_date="2026-05-15",
            sort_by="baseDate",
            sort_order="desc",
            start_date="2025-01-01",
        )
        assert_matches_type(IndicatorHistoryResponse, indicator, path=["response"])

    @parametrize
    async def test_raw_response_history(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.treasury.indicators.with_raw_response.history(
            symbols="tesouro-selic-01032031,tesouro-ipca-15052035",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator = await response.parse()
        assert_matches_type(IndicatorHistoryResponse, indicator, path=["response"])

    @parametrize
    async def test_streaming_response_history(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.treasury.indicators.with_streaming_response.history(
            symbols="tesouro-selic-01032031,tesouro-ipca-15052035",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator = await response.parse()
            assert_matches_type(IndicatorHistoryResponse, indicator, path=["response"])

        assert cast(Any, response.is_closed) is True
