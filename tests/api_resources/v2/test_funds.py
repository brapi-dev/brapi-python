# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from brapi import Brapi, AsyncBrapi
from tests.utils import assert_matches_type
from brapi.types.v2 import (
    FundListResponse,
    FundProfileResponse,
    FundScreenerResponse,
    FundDividendsResponse,
    FundPortfolioResponse,
    FundIndicatorsResponse,
    FundScreenerCnpjResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFunds:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Brapi) -> None:
        fund = client.v2.funds.list()
        assert_matches_type(FundListResponse, fund, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Brapi) -> None:
        fund = client.v2.funds.list(
            asset_type="fii",
            cnpjs="42730834000100",
            etf_category="fixed-income",
            limit=20,
            page=1,
            search="search",
            sort_by="sortBy",
            sort_order="desc",
            status="status",
            symbols="JURO11",
        )
        assert_matches_type(FundListResponse, fund, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Brapi) -> None:
        response = client.v2.funds.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fund = response.parse()
        assert_matches_type(FundListResponse, fund, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Brapi) -> None:
        with client.v2.funds.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fund = response.parse()
            assert_matches_type(FundListResponse, fund, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_dividends(self, client: Brapi) -> None:
        fund = client.v2.funds.dividends()
        assert_matches_type(FundDividendsResponse, fund, path=["response"])

    @parametrize
    def test_method_dividends_with_all_params(self, client: Brapi) -> None:
        fund = client.v2.funds.dividends(
            asset_type="fiagro",
            cnpjs="42730834000100",
            end_date="2026-06-30",
            limit=20,
            page=1,
            sort_by="lastDatePrior",
            sort_order="desc",
            start_date="2026-01-01",
            symbols="JURO11",
        )
        assert_matches_type(FundDividendsResponse, fund, path=["response"])

    @parametrize
    def test_raw_response_dividends(self, client: Brapi) -> None:
        response = client.v2.funds.with_raw_response.dividends()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fund = response.parse()
        assert_matches_type(FundDividendsResponse, fund, path=["response"])

    @parametrize
    def test_streaming_response_dividends(self, client: Brapi) -> None:
        with client.v2.funds.with_streaming_response.dividends() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fund = response.parse()
            assert_matches_type(FundDividendsResponse, fund, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_indicators(self, client: Brapi) -> None:
        fund = client.v2.funds.indicators()
        assert_matches_type(FundIndicatorsResponse, fund, path=["response"])

    @parametrize
    def test_method_indicators_with_all_params(self, client: Brapi) -> None:
        fund = client.v2.funds.indicators(
            asset_type="fii",
            cnpjs="42730834000100",
            symbols="JURO11",
        )
        assert_matches_type(FundIndicatorsResponse, fund, path=["response"])

    @parametrize
    def test_raw_response_indicators(self, client: Brapi) -> None:
        response = client.v2.funds.with_raw_response.indicators()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fund = response.parse()
        assert_matches_type(FundIndicatorsResponse, fund, path=["response"])

    @parametrize
    def test_streaming_response_indicators(self, client: Brapi) -> None:
        with client.v2.funds.with_streaming_response.indicators() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fund = response.parse()
            assert_matches_type(FundIndicatorsResponse, fund, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_portfolio(self, client: Brapi) -> None:
        fund = client.v2.funds.portfolio()
        assert_matches_type(FundPortfolioResponse, fund, path=["response"])

    @parametrize
    def test_method_portfolio_with_all_params(self, client: Brapi) -> None:
        fund = client.v2.funds.portfolio(
            cnpjs="42730834000100",
            include="include",
            limit=20,
            page=1,
            reference_date="referenceDate",
            symbols="JURO11",
        )
        assert_matches_type(FundPortfolioResponse, fund, path=["response"])

    @parametrize
    def test_raw_response_portfolio(self, client: Brapi) -> None:
        response = client.v2.funds.with_raw_response.portfolio()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fund = response.parse()
        assert_matches_type(FundPortfolioResponse, fund, path=["response"])

    @parametrize
    def test_streaming_response_portfolio(self, client: Brapi) -> None:
        with client.v2.funds.with_streaming_response.portfolio() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fund = response.parse()
            assert_matches_type(FundPortfolioResponse, fund, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_profile(self, client: Brapi) -> None:
        fund = client.v2.funds.profile()
        assert_matches_type(FundProfileResponse, fund, path=["response"])

    @parametrize
    def test_method_profile_with_all_params(self, client: Brapi) -> None:
        fund = client.v2.funds.profile(
            cnpjs="42730834000100",
            end_date="2026-06-30",
            include="include",
            reference_date="referenceDate",
            start_date="2026-01-01",
            symbols="JURO11",
        )
        assert_matches_type(FundProfileResponse, fund, path=["response"])

    @parametrize
    def test_raw_response_profile(self, client: Brapi) -> None:
        response = client.v2.funds.with_raw_response.profile()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fund = response.parse()
        assert_matches_type(FundProfileResponse, fund, path=["response"])

    @parametrize
    def test_streaming_response_profile(self, client: Brapi) -> None:
        with client.v2.funds.with_streaming_response.profile() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fund = response.parse()
            assert_matches_type(FundProfileResponse, fund, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_screener(self, client: Brapi) -> None:
        fund = client.v2.funds.screener()
        assert_matches_type(FundScreenerResponse, fund, path=["response"])

    @parametrize
    def test_method_screener_with_all_params(self, client: Brapi) -> None:
        fund = client.v2.funds.screener(
            asset_type="fii",
            average_daily_traded_value_max=0,
            average_daily_traded_value_min=0,
            change_percent_max=0,
            change_percent_min=0,
            dividend_yield_max=0,
            dividend_yield_min=0,
            equity_max=0,
            equity_min=0,
            etf_category="fixed-income",
            income_months12m_max=0,
            income_months12m_min=0,
            last_dividend_max=0,
            last_dividend_min=0,
            last_dividend_yield_max=0,
            last_dividend_yield_min=0,
            last_price_max=0,
            last_price_min=0,
            limit=20,
            market_cap_max=0,
            market_cap_min=0,
            nav_per_share_max=0,
            nav_per_share_min=0,
            page=1,
            price_change12m_max=0,
            price_change12m_min=0,
            price_to_nav_max=0,
            price_to_nav_min=0,
            search="KINEA",
            segment="Logística",
            segment_type="papel",
            sort_by="dividendYield",
            sort_order="desc",
            total_fee_percent_max=0,
            total_fee_percent_min=0,
            total_investors_max=0,
            total_investors_min=0,
            volume_max=0,
            volume_min=0,
        )
        assert_matches_type(FundScreenerResponse, fund, path=["response"])

    @parametrize
    def test_raw_response_screener(self, client: Brapi) -> None:
        response = client.v2.funds.with_raw_response.screener()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fund = response.parse()
        assert_matches_type(FundScreenerResponse, fund, path=["response"])

    @parametrize
    def test_streaming_response_screener(self, client: Brapi) -> None:
        with client.v2.funds.with_streaming_response.screener() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fund = response.parse()
            assert_matches_type(FundScreenerResponse, fund, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_screener_cnpj(self, client: Brapi) -> None:
        fund = client.v2.funds.screener_cnpj()
        assert_matches_type(FundScreenerCnpjResponse, fund, path=["response"])

    @parametrize
    def test_method_screener_cnpj_with_all_params(self, client: Brapi) -> None:
        fund = client.v2.funds.screener_cnpj(
            anbima_classification="Previdência",
            classification="renda-fixa",
            equity_max=0,
            equity_min=0,
            limit=20,
            manager="Itaú",
            nav_per_share_max=0,
            nav_per_share_min=0,
            net_flow1m_max=0,
            net_flow1m_min=0,
            page=1,
            return12m_max=0,
            return12m_min=0,
            return1m_max=0,
            return1m_min=0,
            return36m_max=0,
            return36m_min=0,
            return_day_max=0,
            return_day_min=0,
            return_ytd_max=0,
            return_ytd_min=0,
            search="Itaú Previdência",
            sort_by="return12m",
            sort_order="desc",
            total_investors_max=0,
            total_investors_min=0,
        )
        assert_matches_type(FundScreenerCnpjResponse, fund, path=["response"])

    @parametrize
    def test_raw_response_screener_cnpj(self, client: Brapi) -> None:
        response = client.v2.funds.with_raw_response.screener_cnpj()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fund = response.parse()
        assert_matches_type(FundScreenerCnpjResponse, fund, path=["response"])

    @parametrize
    def test_streaming_response_screener_cnpj(self, client: Brapi) -> None:
        with client.v2.funds.with_streaming_response.screener_cnpj() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fund = response.parse()
            assert_matches_type(FundScreenerCnpjResponse, fund, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFunds:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncBrapi) -> None:
        fund = await async_client.v2.funds.list()
        assert_matches_type(FundListResponse, fund, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBrapi) -> None:
        fund = await async_client.v2.funds.list(
            asset_type="fii",
            cnpjs="42730834000100",
            etf_category="fixed-income",
            limit=20,
            page=1,
            search="search",
            sort_by="sortBy",
            sort_order="desc",
            status="status",
            symbols="JURO11",
        )
        assert_matches_type(FundListResponse, fund, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.funds.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fund = await response.parse()
        assert_matches_type(FundListResponse, fund, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.funds.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fund = await response.parse()
            assert_matches_type(FundListResponse, fund, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_dividends(self, async_client: AsyncBrapi) -> None:
        fund = await async_client.v2.funds.dividends()
        assert_matches_type(FundDividendsResponse, fund, path=["response"])

    @parametrize
    async def test_method_dividends_with_all_params(self, async_client: AsyncBrapi) -> None:
        fund = await async_client.v2.funds.dividends(
            asset_type="fiagro",
            cnpjs="42730834000100",
            end_date="2026-06-30",
            limit=20,
            page=1,
            sort_by="lastDatePrior",
            sort_order="desc",
            start_date="2026-01-01",
            symbols="JURO11",
        )
        assert_matches_type(FundDividendsResponse, fund, path=["response"])

    @parametrize
    async def test_raw_response_dividends(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.funds.with_raw_response.dividends()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fund = await response.parse()
        assert_matches_type(FundDividendsResponse, fund, path=["response"])

    @parametrize
    async def test_streaming_response_dividends(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.funds.with_streaming_response.dividends() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fund = await response.parse()
            assert_matches_type(FundDividendsResponse, fund, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_indicators(self, async_client: AsyncBrapi) -> None:
        fund = await async_client.v2.funds.indicators()
        assert_matches_type(FundIndicatorsResponse, fund, path=["response"])

    @parametrize
    async def test_method_indicators_with_all_params(self, async_client: AsyncBrapi) -> None:
        fund = await async_client.v2.funds.indicators(
            asset_type="fii",
            cnpjs="42730834000100",
            symbols="JURO11",
        )
        assert_matches_type(FundIndicatorsResponse, fund, path=["response"])

    @parametrize
    async def test_raw_response_indicators(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.funds.with_raw_response.indicators()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fund = await response.parse()
        assert_matches_type(FundIndicatorsResponse, fund, path=["response"])

    @parametrize
    async def test_streaming_response_indicators(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.funds.with_streaming_response.indicators() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fund = await response.parse()
            assert_matches_type(FundIndicatorsResponse, fund, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_portfolio(self, async_client: AsyncBrapi) -> None:
        fund = await async_client.v2.funds.portfolio()
        assert_matches_type(FundPortfolioResponse, fund, path=["response"])

    @parametrize
    async def test_method_portfolio_with_all_params(self, async_client: AsyncBrapi) -> None:
        fund = await async_client.v2.funds.portfolio(
            cnpjs="42730834000100",
            include="include",
            limit=20,
            page=1,
            reference_date="referenceDate",
            symbols="JURO11",
        )
        assert_matches_type(FundPortfolioResponse, fund, path=["response"])

    @parametrize
    async def test_raw_response_portfolio(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.funds.with_raw_response.portfolio()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fund = await response.parse()
        assert_matches_type(FundPortfolioResponse, fund, path=["response"])

    @parametrize
    async def test_streaming_response_portfolio(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.funds.with_streaming_response.portfolio() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fund = await response.parse()
            assert_matches_type(FundPortfolioResponse, fund, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_profile(self, async_client: AsyncBrapi) -> None:
        fund = await async_client.v2.funds.profile()
        assert_matches_type(FundProfileResponse, fund, path=["response"])

    @parametrize
    async def test_method_profile_with_all_params(self, async_client: AsyncBrapi) -> None:
        fund = await async_client.v2.funds.profile(
            cnpjs="42730834000100",
            end_date="2026-06-30",
            include="include",
            reference_date="referenceDate",
            start_date="2026-01-01",
            symbols="JURO11",
        )
        assert_matches_type(FundProfileResponse, fund, path=["response"])

    @parametrize
    async def test_raw_response_profile(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.funds.with_raw_response.profile()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fund = await response.parse()
        assert_matches_type(FundProfileResponse, fund, path=["response"])

    @parametrize
    async def test_streaming_response_profile(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.funds.with_streaming_response.profile() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fund = await response.parse()
            assert_matches_type(FundProfileResponse, fund, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_screener(self, async_client: AsyncBrapi) -> None:
        fund = await async_client.v2.funds.screener()
        assert_matches_type(FundScreenerResponse, fund, path=["response"])

    @parametrize
    async def test_method_screener_with_all_params(self, async_client: AsyncBrapi) -> None:
        fund = await async_client.v2.funds.screener(
            asset_type="fii",
            average_daily_traded_value_max=0,
            average_daily_traded_value_min=0,
            change_percent_max=0,
            change_percent_min=0,
            dividend_yield_max=0,
            dividend_yield_min=0,
            equity_max=0,
            equity_min=0,
            etf_category="fixed-income",
            income_months12m_max=0,
            income_months12m_min=0,
            last_dividend_max=0,
            last_dividend_min=0,
            last_dividend_yield_max=0,
            last_dividend_yield_min=0,
            last_price_max=0,
            last_price_min=0,
            limit=20,
            market_cap_max=0,
            market_cap_min=0,
            nav_per_share_max=0,
            nav_per_share_min=0,
            page=1,
            price_change12m_max=0,
            price_change12m_min=0,
            price_to_nav_max=0,
            price_to_nav_min=0,
            search="KINEA",
            segment="Logística",
            segment_type="papel",
            sort_by="dividendYield",
            sort_order="desc",
            total_fee_percent_max=0,
            total_fee_percent_min=0,
            total_investors_max=0,
            total_investors_min=0,
            volume_max=0,
            volume_min=0,
        )
        assert_matches_type(FundScreenerResponse, fund, path=["response"])

    @parametrize
    async def test_raw_response_screener(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.funds.with_raw_response.screener()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fund = await response.parse()
        assert_matches_type(FundScreenerResponse, fund, path=["response"])

    @parametrize
    async def test_streaming_response_screener(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.funds.with_streaming_response.screener() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fund = await response.parse()
            assert_matches_type(FundScreenerResponse, fund, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_screener_cnpj(self, async_client: AsyncBrapi) -> None:
        fund = await async_client.v2.funds.screener_cnpj()
        assert_matches_type(FundScreenerCnpjResponse, fund, path=["response"])

    @parametrize
    async def test_method_screener_cnpj_with_all_params(self, async_client: AsyncBrapi) -> None:
        fund = await async_client.v2.funds.screener_cnpj(
            anbima_classification="Previdência",
            classification="renda-fixa",
            equity_max=0,
            equity_min=0,
            limit=20,
            manager="Itaú",
            nav_per_share_max=0,
            nav_per_share_min=0,
            net_flow1m_max=0,
            net_flow1m_min=0,
            page=1,
            return12m_max=0,
            return12m_min=0,
            return1m_max=0,
            return1m_min=0,
            return36m_max=0,
            return36m_min=0,
            return_day_max=0,
            return_day_min=0,
            return_ytd_max=0,
            return_ytd_min=0,
            search="Itaú Previdência",
            sort_by="return12m",
            sort_order="desc",
            total_investors_max=0,
            total_investors_min=0,
        )
        assert_matches_type(FundScreenerCnpjResponse, fund, path=["response"])

    @parametrize
    async def test_raw_response_screener_cnpj(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.funds.with_raw_response.screener_cnpj()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fund = await response.parse()
        assert_matches_type(FundScreenerCnpjResponse, fund, path=["response"])

    @parametrize
    async def test_streaming_response_screener_cnpj(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.funds.with_streaming_response.screener_cnpj() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fund = await response.parse()
            assert_matches_type(FundScreenerCnpjResponse, fund, path=["response"])

        assert cast(Any, response.is_closed) is True
