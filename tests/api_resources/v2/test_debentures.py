# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from brapi import Brapi, AsyncBrapi
from tests.utils import assert_matches_type
from brapi.types.v2 import (
    DebentureListResponse,
    DebentureProfileResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDebentures:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Brapi) -> None:
        debenture = client.v2.debentures.list()
        assert_matches_type(DebentureListResponse, debenture, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Brapi) -> None:
        debenture = client.v2.debentures.list(
            cnpjs="02421421000111",
            incentivized="true",
            index="ipca",
            limit=50,
            maturity_from="2027-01-01",
            maturity_to="2030-12-31",
            page=1,
            search="tim",
            sort_by="symbol",
            sort_order="asc",
            status="active",
            symbols="TIMS12",
        )
        assert_matches_type(DebentureListResponse, debenture, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Brapi) -> None:
        response = client.v2.debentures.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        debenture = response.parse()
        assert_matches_type(DebentureListResponse, debenture, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Brapi) -> None:
        with client.v2.debentures.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            debenture = response.parse()
            assert_matches_type(DebentureListResponse, debenture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_profile(self, client: Brapi) -> None:
        debenture = client.v2.debentures.profile(
            symbols="TIMS12",
        )
        assert_matches_type(DebentureProfileResponse, debenture, path=["response"])

    @parametrize
    def test_raw_response_profile(self, client: Brapi) -> None:
        response = client.v2.debentures.with_raw_response.profile(
            symbols="TIMS12",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        debenture = response.parse()
        assert_matches_type(DebentureProfileResponse, debenture, path=["response"])

    @parametrize
    def test_streaming_response_profile(self, client: Brapi) -> None:
        with client.v2.debentures.with_streaming_response.profile(
            symbols="TIMS12",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            debenture = response.parse()
            assert_matches_type(DebentureProfileResponse, debenture, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDebentures:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncBrapi) -> None:
        debenture = await async_client.v2.debentures.list()
        assert_matches_type(DebentureListResponse, debenture, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBrapi) -> None:
        debenture = await async_client.v2.debentures.list(
            cnpjs="02421421000111",
            incentivized="true",
            index="ipca",
            limit=50,
            maturity_from="2027-01-01",
            maturity_to="2030-12-31",
            page=1,
            search="tim",
            sort_by="symbol",
            sort_order="asc",
            status="active",
            symbols="TIMS12",
        )
        assert_matches_type(DebentureListResponse, debenture, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.debentures.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        debenture = await response.parse()
        assert_matches_type(DebentureListResponse, debenture, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.debentures.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            debenture = await response.parse()
            assert_matches_type(DebentureListResponse, debenture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_profile(self, async_client: AsyncBrapi) -> None:
        debenture = await async_client.v2.debentures.profile(
            symbols="TIMS12",
        )
        assert_matches_type(DebentureProfileResponse, debenture, path=["response"])

    @parametrize
    async def test_raw_response_profile(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.debentures.with_raw_response.profile(
            symbols="TIMS12",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        debenture = await response.parse()
        assert_matches_type(DebentureProfileResponse, debenture, path=["response"])

    @parametrize
    async def test_streaming_response_profile(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.debentures.with_streaming_response.profile(
            symbols="TIMS12",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            debenture = await response.parse()
            assert_matches_type(DebentureProfileResponse, debenture, path=["response"])

        assert cast(Any, response.is_closed) is True
