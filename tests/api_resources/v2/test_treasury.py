# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from brapi import Brapi, AsyncBrapi
from tests.utils import assert_matches_type
from brapi.types.v2 import TreasuryListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTreasury:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Brapi) -> None:
        treasury = client.v2.treasury.list()
        assert_matches_type(TreasuryListResponse, treasury, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Brapi) -> None:
        treasury = client.v2.treasury.list(
            coupon_type="zero",
            indexer="selic",
            limit=20,
            page=1,
            search="tesouro-selic-01032031",
            sort_by="maturityDate",
            sort_order="asc",
        )
        assert_matches_type(TreasuryListResponse, treasury, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Brapi) -> None:
        response = client.v2.treasury.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        treasury = response.parse()
        assert_matches_type(TreasuryListResponse, treasury, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Brapi) -> None:
        with client.v2.treasury.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            treasury = response.parse()
            assert_matches_type(TreasuryListResponse, treasury, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTreasury:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncBrapi) -> None:
        treasury = await async_client.v2.treasury.list()
        assert_matches_type(TreasuryListResponse, treasury, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBrapi) -> None:
        treasury = await async_client.v2.treasury.list(
            coupon_type="zero",
            indexer="selic",
            limit=20,
            page=1,
            search="tesouro-selic-01032031",
            sort_by="maturityDate",
            sort_order="asc",
        )
        assert_matches_type(TreasuryListResponse, treasury, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.treasury.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        treasury = await response.parse()
        assert_matches_type(TreasuryListResponse, treasury, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.treasury.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            treasury = await response.parse()
            assert_matches_type(TreasuryListResponse, treasury, path=["response"])

        assert cast(Any, response.is_closed) is True
