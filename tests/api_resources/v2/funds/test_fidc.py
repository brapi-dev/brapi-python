# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from brapi import Brapi, AsyncBrapi
from tests.utils import assert_matches_type
from brapi.types.v2.funds import FidcReportsResponse, FidcPortfolioResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFidc:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_portfolio(self, client: Brapi) -> None:
        fidc = client.v2.funds.fidc.portfolio()
        assert_matches_type(FidcPortfolioResponse, fidc, path=["response"])

    @parametrize
    def test_method_portfolio_with_all_params(self, client: Brapi) -> None:
        fidc = client.v2.funds.fidc.portfolio(
            cnpjs="05754060000113",
            include="include",
            reference_date="referenceDate",
            symbols="symbols",
        )
        assert_matches_type(FidcPortfolioResponse, fidc, path=["response"])

    @parametrize
    def test_raw_response_portfolio(self, client: Brapi) -> None:
        response = client.v2.funds.fidc.with_raw_response.portfolio()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fidc = response.parse()
        assert_matches_type(FidcPortfolioResponse, fidc, path=["response"])

    @parametrize
    def test_streaming_response_portfolio(self, client: Brapi) -> None:
        with client.v2.funds.fidc.with_streaming_response.portfolio() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fidc = response.parse()
            assert_matches_type(FidcPortfolioResponse, fidc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_reports(self, client: Brapi) -> None:
        fidc = client.v2.funds.fidc.reports()
        assert_matches_type(FidcReportsResponse, fidc, path=["response"])

    @parametrize
    def test_method_reports_with_all_params(self, client: Brapi) -> None:
        fidc = client.v2.funds.fidc.reports(
            cnpjs="05754060000113",
            end_date="2026-06-30",
            limit=20,
            page=1,
            sort_by="sortBy",
            sort_order="desc",
            start_date="2026-01-01",
            symbols="symbols",
        )
        assert_matches_type(FidcReportsResponse, fidc, path=["response"])

    @parametrize
    def test_raw_response_reports(self, client: Brapi) -> None:
        response = client.v2.funds.fidc.with_raw_response.reports()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fidc = response.parse()
        assert_matches_type(FidcReportsResponse, fidc, path=["response"])

    @parametrize
    def test_streaming_response_reports(self, client: Brapi) -> None:
        with client.v2.funds.fidc.with_streaming_response.reports() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fidc = response.parse()
            assert_matches_type(FidcReportsResponse, fidc, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFidc:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_portfolio(self, async_client: AsyncBrapi) -> None:
        fidc = await async_client.v2.funds.fidc.portfolio()
        assert_matches_type(FidcPortfolioResponse, fidc, path=["response"])

    @parametrize
    async def test_method_portfolio_with_all_params(self, async_client: AsyncBrapi) -> None:
        fidc = await async_client.v2.funds.fidc.portfolio(
            cnpjs="05754060000113",
            include="include",
            reference_date="referenceDate",
            symbols="symbols",
        )
        assert_matches_type(FidcPortfolioResponse, fidc, path=["response"])

    @parametrize
    async def test_raw_response_portfolio(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.funds.fidc.with_raw_response.portfolio()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fidc = await response.parse()
        assert_matches_type(FidcPortfolioResponse, fidc, path=["response"])

    @parametrize
    async def test_streaming_response_portfolio(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.funds.fidc.with_streaming_response.portfolio() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fidc = await response.parse()
            assert_matches_type(FidcPortfolioResponse, fidc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_reports(self, async_client: AsyncBrapi) -> None:
        fidc = await async_client.v2.funds.fidc.reports()
        assert_matches_type(FidcReportsResponse, fidc, path=["response"])

    @parametrize
    async def test_method_reports_with_all_params(self, async_client: AsyncBrapi) -> None:
        fidc = await async_client.v2.funds.fidc.reports(
            cnpjs="05754060000113",
            end_date="2026-06-30",
            limit=20,
            page=1,
            sort_by="sortBy",
            sort_order="desc",
            start_date="2026-01-01",
            symbols="symbols",
        )
        assert_matches_type(FidcReportsResponse, fidc, path=["response"])

    @parametrize
    async def test_raw_response_reports(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.funds.fidc.with_raw_response.reports()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fidc = await response.parse()
        assert_matches_type(FidcReportsResponse, fidc, path=["response"])

    @parametrize
    async def test_streaming_response_reports(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.funds.fidc.with_streaming_response.reports() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fidc = await response.parse()
            assert_matches_type(FidcReportsResponse, fidc, path=["response"])

        assert cast(Any, response.is_closed) is True
