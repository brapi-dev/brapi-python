# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from brapi import Brapi, AsyncBrapi
from tests.utils import assert_matches_type
from brapi.types.v2.fii import (
    IndicatorHistoryResponse,
    IndicatorRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIndicators:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Brapi) -> None:
        indicator = client.v2.fii.indicators.retrieve(
            symbols="HGLG11,MXRF11",
        )
        assert_matches_type(IndicatorRetrieveResponse, indicator, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Brapi) -> None:
        response = client.v2.fii.indicators.with_raw_response.retrieve(
            symbols="HGLG11,MXRF11",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator = response.parse()
        assert_matches_type(IndicatorRetrieveResponse, indicator, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Brapi) -> None:
        with client.v2.fii.indicators.with_streaming_response.retrieve(
            symbols="HGLG11,MXRF11",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator = response.parse()
            assert_matches_type(IndicatorRetrieveResponse, indicator, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_history(self, client: Brapi) -> None:
        indicator = client.v2.fii.indicators.history(
            symbols="HGLG11,MXRF11",
        )
        assert_matches_type(IndicatorHistoryResponse, indicator, path=["response"])

    @parametrize
    def test_method_history_with_all_params(self, client: Brapi) -> None:
        indicator = client.v2.fii.indicators.history(
            symbols="HGLG11,MXRF11",
            end_date="2025-12-31",
            sort_by="referenceDate",
            sort_order="desc",
            start_date="2024-01-01",
        )
        assert_matches_type(IndicatorHistoryResponse, indicator, path=["response"])

    @parametrize
    def test_raw_response_history(self, client: Brapi) -> None:
        response = client.v2.fii.indicators.with_raw_response.history(
            symbols="HGLG11,MXRF11",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator = response.parse()
        assert_matches_type(IndicatorHistoryResponse, indicator, path=["response"])

    @parametrize
    def test_streaming_response_history(self, client: Brapi) -> None:
        with client.v2.fii.indicators.with_streaming_response.history(
            symbols="HGLG11,MXRF11",
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
        indicator = await async_client.v2.fii.indicators.retrieve(
            symbols="HGLG11,MXRF11",
        )
        assert_matches_type(IndicatorRetrieveResponse, indicator, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.fii.indicators.with_raw_response.retrieve(
            symbols="HGLG11,MXRF11",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator = await response.parse()
        assert_matches_type(IndicatorRetrieveResponse, indicator, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.fii.indicators.with_streaming_response.retrieve(
            symbols="HGLG11,MXRF11",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator = await response.parse()
            assert_matches_type(IndicatorRetrieveResponse, indicator, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_history(self, async_client: AsyncBrapi) -> None:
        indicator = await async_client.v2.fii.indicators.history(
            symbols="HGLG11,MXRF11",
        )
        assert_matches_type(IndicatorHistoryResponse, indicator, path=["response"])

    @parametrize
    async def test_method_history_with_all_params(self, async_client: AsyncBrapi) -> None:
        indicator = await async_client.v2.fii.indicators.history(
            symbols="HGLG11,MXRF11",
            end_date="2025-12-31",
            sort_by="referenceDate",
            sort_order="desc",
            start_date="2024-01-01",
        )
        assert_matches_type(IndicatorHistoryResponse, indicator, path=["response"])

    @parametrize
    async def test_raw_response_history(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.fii.indicators.with_raw_response.history(
            symbols="HGLG11,MXRF11",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator = await response.parse()
        assert_matches_type(IndicatorHistoryResponse, indicator, path=["response"])

    @parametrize
    async def test_streaming_response_history(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.fii.indicators.with_streaming_response.history(
            symbols="HGLG11,MXRF11",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator = await response.parse()
            assert_matches_type(IndicatorHistoryResponse, indicator, path=["response"])

        assert cast(Any, response.is_closed) is True
