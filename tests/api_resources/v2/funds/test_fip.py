# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from brapi import Brapi, AsyncBrapi
from tests.utils import assert_matches_type
from brapi.types.v2.funds import FipReportsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFip:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_reports(self, client: Brapi) -> None:
        fip = client.v2.funds.fip.reports()
        assert_matches_type(FipReportsResponse, fip, path=["response"])

    @parametrize
    def test_method_reports_with_all_params(self, client: Brapi) -> None:
        fip = client.v2.funds.fip.reports(
            cnpjs="06033235000166",
            end_date="2026-06-30",
            limit=20,
            page=1,
            report_type="trimestral",
            sort_by="sortBy",
            sort_order="desc",
            start_date="2026-01-01",
            symbols="symbols",
        )
        assert_matches_type(FipReportsResponse, fip, path=["response"])

    @parametrize
    def test_raw_response_reports(self, client: Brapi) -> None:
        response = client.v2.funds.fip.with_raw_response.reports()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fip = response.parse()
        assert_matches_type(FipReportsResponse, fip, path=["response"])

    @parametrize
    def test_streaming_response_reports(self, client: Brapi) -> None:
        with client.v2.funds.fip.with_streaming_response.reports() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fip = response.parse()
            assert_matches_type(FipReportsResponse, fip, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFip:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_reports(self, async_client: AsyncBrapi) -> None:
        fip = await async_client.v2.funds.fip.reports()
        assert_matches_type(FipReportsResponse, fip, path=["response"])

    @parametrize
    async def test_method_reports_with_all_params(self, async_client: AsyncBrapi) -> None:
        fip = await async_client.v2.funds.fip.reports(
            cnpjs="06033235000166",
            end_date="2026-06-30",
            limit=20,
            page=1,
            report_type="trimestral",
            sort_by="sortBy",
            sort_order="desc",
            start_date="2026-01-01",
            symbols="symbols",
        )
        assert_matches_type(FipReportsResponse, fip, path=["response"])

    @parametrize
    async def test_raw_response_reports(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.funds.fip.with_raw_response.reports()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fip = await response.parse()
        assert_matches_type(FipReportsResponse, fip, path=["response"])

    @parametrize
    async def test_streaming_response_reports(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.funds.fip.with_streaming_response.reports() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fip = await response.parse()
            assert_matches_type(FipReportsResponse, fip, path=["response"])

        assert cast(Any, response.is_closed) is True
