# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from brapi import Brapi, AsyncBrapi
from tests.utils import assert_matches_type
from brapi.types.v2 import (
    FiiListResponse,
    FiiReportsResponse,
    FiiDividendsResponse,
    FiiFinancialsResponse,
    FiiHistoricalResponse,
    FiiAnnualReportsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFii:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Brapi) -> None:
        fii = client.v2.fii.list()
        assert_matches_type(FiiListResponse, fii, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Brapi) -> None:
        fii = client.v2.fii.list(
            cnpjs="11728688000147",
            limit=20,
            mandate="mandate",
            page=1,
            search="hglg",
            segmento_atuacao="segmentoAtuacao",
            segment_type="papel",
            sort_by="referenceDate",
            sort_order="desc",
            symbols="HGLG11,MXRF11",
            tipo_gestao="tipoGestao",
        )
        assert_matches_type(FiiListResponse, fii, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Brapi) -> None:
        response = client.v2.fii.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fii = response.parse()
        assert_matches_type(FiiListResponse, fii, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Brapi) -> None:
        with client.v2.fii.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fii = response.parse()
            assert_matches_type(FiiListResponse, fii, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_annual_reports(self, client: Brapi) -> None:
        fii = client.v2.fii.annual_reports()
        assert_matches_type(FiiAnnualReportsResponse, fii, path=["response"])

    @parametrize
    def test_method_annual_reports_with_all_params(self, client: Brapi) -> None:
        fii = client.v2.fii.annual_reports(
            cnpjs="11728688000147",
            end_date="2025-12-31",
            include="summary,governance",
            limit=1,
            page=1,
            sort_by="referenceDate",
            sort_order="asc",
            start_date="2025-01-01",
            symbols="HGLG11,MXRF11",
            year=2025,
        )
        assert_matches_type(FiiAnnualReportsResponse, fii, path=["response"])

    @parametrize
    def test_raw_response_annual_reports(self, client: Brapi) -> None:
        response = client.v2.fii.with_raw_response.annual_reports()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fii = response.parse()
        assert_matches_type(FiiAnnualReportsResponse, fii, path=["response"])

    @parametrize
    def test_streaming_response_annual_reports(self, client: Brapi) -> None:
        with client.v2.fii.with_streaming_response.annual_reports() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fii = response.parse()
            assert_matches_type(FiiAnnualReportsResponse, fii, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_dividends(self, client: Brapi) -> None:
        fii = client.v2.fii.dividends(
            symbols="HGLG11,MXRF11",
        )
        assert_matches_type(FiiDividendsResponse, fii, path=["response"])

    @parametrize
    def test_method_dividends_with_all_params(self, client: Brapi) -> None:
        fii = client.v2.fii.dividends(
            symbols="HGLG11,MXRF11",
            end_date="2025-12-31",
            sort_by="referenceDate",
            sort_order="desc",
            start_date="2024-01-01",
        )
        assert_matches_type(FiiDividendsResponse, fii, path=["response"])

    @parametrize
    def test_raw_response_dividends(self, client: Brapi) -> None:
        response = client.v2.fii.with_raw_response.dividends(
            symbols="HGLG11,MXRF11",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fii = response.parse()
        assert_matches_type(FiiDividendsResponse, fii, path=["response"])

    @parametrize
    def test_streaming_response_dividends(self, client: Brapi) -> None:
        with client.v2.fii.with_streaming_response.dividends(
            symbols="HGLG11,MXRF11",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fii = response.parse()
            assert_matches_type(FiiDividendsResponse, fii, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_financials(self, client: Brapi) -> None:
        fii = client.v2.fii.financials()
        assert_matches_type(FiiFinancialsResponse, fii, path=["response"])

    @parametrize
    def test_method_financials_with_all_params(self, client: Brapi) -> None:
        fii = client.v2.fii.financials(
            cnpjs="11728688000147",
            end_date="2025-12-31",
            limit=1,
            page=1,
            sort_by="referenceDate",
            sort_order="asc",
            start_date="2025-01-01",
            symbols="HGLG11,MXRF11",
            year=2025,
        )
        assert_matches_type(FiiFinancialsResponse, fii, path=["response"])

    @parametrize
    def test_raw_response_financials(self, client: Brapi) -> None:
        response = client.v2.fii.with_raw_response.financials()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fii = response.parse()
        assert_matches_type(FiiFinancialsResponse, fii, path=["response"])

    @parametrize
    def test_streaming_response_financials(self, client: Brapi) -> None:
        with client.v2.fii.with_streaming_response.financials() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fii = response.parse()
            assert_matches_type(FiiFinancialsResponse, fii, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_historical(self, client: Brapi) -> None:
        fii = client.v2.fii.historical(
            symbols="HGLG11,MXRF11",
        )
        assert_matches_type(FiiHistoricalResponse, fii, path=["response"])

    @parametrize
    def test_method_historical_with_all_params(self, client: Brapi) -> None:
        fii = client.v2.fii.historical(
            symbols="HGLG11,MXRF11",
            end_date="2025-12-31",
            sort_order="desc",
            start_date="2024-01-01",
        )
        assert_matches_type(FiiHistoricalResponse, fii, path=["response"])

    @parametrize
    def test_raw_response_historical(self, client: Brapi) -> None:
        response = client.v2.fii.with_raw_response.historical(
            symbols="HGLG11,MXRF11",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fii = response.parse()
        assert_matches_type(FiiHistoricalResponse, fii, path=["response"])

    @parametrize
    def test_streaming_response_historical(self, client: Brapi) -> None:
        with client.v2.fii.with_streaming_response.historical(
            symbols="HGLG11,MXRF11",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fii = response.parse()
            assert_matches_type(FiiHistoricalResponse, fii, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_reports(self, client: Brapi) -> None:
        fii = client.v2.fii.reports(
            symbols="HGLG11,MXRF11",
        )
        assert_matches_type(FiiReportsResponse, fii, path=["response"])

    @parametrize
    def test_method_reports_with_all_params(self, client: Brapi) -> None:
        fii = client.v2.fii.reports(
            symbols="HGLG11,MXRF11",
            all_versions="false",
            end_date="2025-12-31",
            limit=20,
            page=1,
            sort_by="referenceDate",
            sort_order="desc",
            start_date="2024-01-01",
        )
        assert_matches_type(FiiReportsResponse, fii, path=["response"])

    @parametrize
    def test_raw_response_reports(self, client: Brapi) -> None:
        response = client.v2.fii.with_raw_response.reports(
            symbols="HGLG11,MXRF11",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fii = response.parse()
        assert_matches_type(FiiReportsResponse, fii, path=["response"])

    @parametrize
    def test_streaming_response_reports(self, client: Brapi) -> None:
        with client.v2.fii.with_streaming_response.reports(
            symbols="HGLG11,MXRF11",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fii = response.parse()
            assert_matches_type(FiiReportsResponse, fii, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFii:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncBrapi) -> None:
        fii = await async_client.v2.fii.list()
        assert_matches_type(FiiListResponse, fii, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBrapi) -> None:
        fii = await async_client.v2.fii.list(
            cnpjs="11728688000147",
            limit=20,
            mandate="mandate",
            page=1,
            search="hglg",
            segmento_atuacao="segmentoAtuacao",
            segment_type="papel",
            sort_by="referenceDate",
            sort_order="desc",
            symbols="HGLG11,MXRF11",
            tipo_gestao="tipoGestao",
        )
        assert_matches_type(FiiListResponse, fii, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.fii.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fii = await response.parse()
        assert_matches_type(FiiListResponse, fii, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.fii.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fii = await response.parse()
            assert_matches_type(FiiListResponse, fii, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_annual_reports(self, async_client: AsyncBrapi) -> None:
        fii = await async_client.v2.fii.annual_reports()
        assert_matches_type(FiiAnnualReportsResponse, fii, path=["response"])

    @parametrize
    async def test_method_annual_reports_with_all_params(self, async_client: AsyncBrapi) -> None:
        fii = await async_client.v2.fii.annual_reports(
            cnpjs="11728688000147",
            end_date="2025-12-31",
            include="summary,governance",
            limit=1,
            page=1,
            sort_by="referenceDate",
            sort_order="asc",
            start_date="2025-01-01",
            symbols="HGLG11,MXRF11",
            year=2025,
        )
        assert_matches_type(FiiAnnualReportsResponse, fii, path=["response"])

    @parametrize
    async def test_raw_response_annual_reports(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.fii.with_raw_response.annual_reports()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fii = await response.parse()
        assert_matches_type(FiiAnnualReportsResponse, fii, path=["response"])

    @parametrize
    async def test_streaming_response_annual_reports(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.fii.with_streaming_response.annual_reports() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fii = await response.parse()
            assert_matches_type(FiiAnnualReportsResponse, fii, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_dividends(self, async_client: AsyncBrapi) -> None:
        fii = await async_client.v2.fii.dividends(
            symbols="HGLG11,MXRF11",
        )
        assert_matches_type(FiiDividendsResponse, fii, path=["response"])

    @parametrize
    async def test_method_dividends_with_all_params(self, async_client: AsyncBrapi) -> None:
        fii = await async_client.v2.fii.dividends(
            symbols="HGLG11,MXRF11",
            end_date="2025-12-31",
            sort_by="referenceDate",
            sort_order="desc",
            start_date="2024-01-01",
        )
        assert_matches_type(FiiDividendsResponse, fii, path=["response"])

    @parametrize
    async def test_raw_response_dividends(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.fii.with_raw_response.dividends(
            symbols="HGLG11,MXRF11",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fii = await response.parse()
        assert_matches_type(FiiDividendsResponse, fii, path=["response"])

    @parametrize
    async def test_streaming_response_dividends(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.fii.with_streaming_response.dividends(
            symbols="HGLG11,MXRF11",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fii = await response.parse()
            assert_matches_type(FiiDividendsResponse, fii, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_financials(self, async_client: AsyncBrapi) -> None:
        fii = await async_client.v2.fii.financials()
        assert_matches_type(FiiFinancialsResponse, fii, path=["response"])

    @parametrize
    async def test_method_financials_with_all_params(self, async_client: AsyncBrapi) -> None:
        fii = await async_client.v2.fii.financials(
            cnpjs="11728688000147",
            end_date="2025-12-31",
            limit=1,
            page=1,
            sort_by="referenceDate",
            sort_order="asc",
            start_date="2025-01-01",
            symbols="HGLG11,MXRF11",
            year=2025,
        )
        assert_matches_type(FiiFinancialsResponse, fii, path=["response"])

    @parametrize
    async def test_raw_response_financials(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.fii.with_raw_response.financials()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fii = await response.parse()
        assert_matches_type(FiiFinancialsResponse, fii, path=["response"])

    @parametrize
    async def test_streaming_response_financials(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.fii.with_streaming_response.financials() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fii = await response.parse()
            assert_matches_type(FiiFinancialsResponse, fii, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_historical(self, async_client: AsyncBrapi) -> None:
        fii = await async_client.v2.fii.historical(
            symbols="HGLG11,MXRF11",
        )
        assert_matches_type(FiiHistoricalResponse, fii, path=["response"])

    @parametrize
    async def test_method_historical_with_all_params(self, async_client: AsyncBrapi) -> None:
        fii = await async_client.v2.fii.historical(
            symbols="HGLG11,MXRF11",
            end_date="2025-12-31",
            sort_order="desc",
            start_date="2024-01-01",
        )
        assert_matches_type(FiiHistoricalResponse, fii, path=["response"])

    @parametrize
    async def test_raw_response_historical(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.fii.with_raw_response.historical(
            symbols="HGLG11,MXRF11",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fii = await response.parse()
        assert_matches_type(FiiHistoricalResponse, fii, path=["response"])

    @parametrize
    async def test_streaming_response_historical(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.fii.with_streaming_response.historical(
            symbols="HGLG11,MXRF11",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fii = await response.parse()
            assert_matches_type(FiiHistoricalResponse, fii, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_reports(self, async_client: AsyncBrapi) -> None:
        fii = await async_client.v2.fii.reports(
            symbols="HGLG11,MXRF11",
        )
        assert_matches_type(FiiReportsResponse, fii, path=["response"])

    @parametrize
    async def test_method_reports_with_all_params(self, async_client: AsyncBrapi) -> None:
        fii = await async_client.v2.fii.reports(
            symbols="HGLG11,MXRF11",
            all_versions="false",
            end_date="2025-12-31",
            limit=20,
            page=1,
            sort_by="referenceDate",
            sort_order="desc",
            start_date="2024-01-01",
        )
        assert_matches_type(FiiReportsResponse, fii, path=["response"])

    @parametrize
    async def test_raw_response_reports(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.fii.with_raw_response.reports(
            symbols="HGLG11,MXRF11",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fii = await response.parse()
        assert_matches_type(FiiReportsResponse, fii, path=["response"])

    @parametrize
    async def test_streaming_response_reports(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.fii.with_streaming_response.reports(
            symbols="HGLG11,MXRF11",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fii = await response.parse()
            assert_matches_type(FiiReportsResponse, fii, path=["response"])

        assert cast(Any, response.is_closed) is True
