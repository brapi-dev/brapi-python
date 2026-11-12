# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from brapi import Brapi, AsyncBrapi
from tests.utils import assert_matches_type
from brapi.types.v2.funds import HoldingHistoryResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHoldings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_history(self, client: Brapi) -> None:
        holding = client.v2.funds.holdings.history()
        assert_matches_type(HoldingHistoryResponse, holding, path=["response"])

    @parametrize
    def test_method_history_with_all_params(self, client: Brapi) -> None:
        holding = client.v2.funds.holdings.history(
            asset="PETR4",
            asset_cnpj="x",
            cnpj="x",
            end_date="endDate",
            sort_order="asc",
            start_date="2026-09-01",
            symbol="BOVA11",
        )
        assert_matches_type(HoldingHistoryResponse, holding, path=["response"])

    @parametrize
    def test_raw_response_history(self, client: Brapi) -> None:
        response = client.v2.funds.holdings.with_raw_response.history()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        holding = response.parse()
        assert_matches_type(HoldingHistoryResponse, holding, path=["response"])

    @parametrize
    def test_streaming_response_history(self, client: Brapi) -> None:
        with client.v2.funds.holdings.with_streaming_response.history() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            holding = response.parse()
            assert_matches_type(HoldingHistoryResponse, holding, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHoldings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_history(self, async_client: AsyncBrapi) -> None:
        holding = await async_client.v2.funds.holdings.history()
        assert_matches_type(HoldingHistoryResponse, holding, path=["response"])

    @parametrize
    async def test_method_history_with_all_params(self, async_client: AsyncBrapi) -> None:
        holding = await async_client.v2.funds.holdings.history(
            asset="PETR4",
            asset_cnpj="x",
            cnpj="x",
            end_date="endDate",
            sort_order="asc",
            start_date="2026-09-01",
            symbol="BOVA11",
        )
        assert_matches_type(HoldingHistoryResponse, holding, path=["response"])

    @parametrize
    async def test_raw_response_history(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.funds.holdings.with_raw_response.history()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        holding = await response.parse()
        assert_matches_type(HoldingHistoryResponse, holding, path=["response"])

    @parametrize
    async def test_streaming_response_history(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.funds.holdings.with_streaming_response.history() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            holding = await response.parse()
            assert_matches_type(HoldingHistoryResponse, holding, path=["response"])

        assert cast(Any, response.is_closed) is True
