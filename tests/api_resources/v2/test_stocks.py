# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from brapi import Brapi, AsyncBrapi
from tests.utils import assert_matches_type
from brapi.types.v2 import (
    StockQuoteResponse,
    StockProfileResponse,
    StockCashFlowResponse,
    StockDividendsResponse,
    StockHistoricalResponse,
    StockStatisticsResponse,
    StockValueAddedResponse,
    StockBalanceSheetResponse,
    StockFinancialDataResponse,
    StockIncomeStatementResponse,
    StockInsiderTransactionsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStocks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_balance_sheet(self, client: Brapi) -> None:
        stock = client.v2.stocks.balance_sheet(
            symbols="PETR4,VALE3",
        )
        assert_matches_type(StockBalanceSheetResponse, stock, path=["response"])

    @parametrize
    def test_method_balance_sheet_with_all_params(self, client: Brapi) -> None:
        stock = client.v2.stocks.balance_sheet(
            symbols="PETR4,VALE3",
            end_date="2024-12-31",
            period="annual",
            start_date="2024-01-01",
        )
        assert_matches_type(StockBalanceSheetResponse, stock, path=["response"])

    @parametrize
    def test_raw_response_balance_sheet(self, client: Brapi) -> None:
        response = client.v2.stocks.with_raw_response.balance_sheet(
            symbols="PETR4,VALE3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock = response.parse()
        assert_matches_type(StockBalanceSheetResponse, stock, path=["response"])

    @parametrize
    def test_streaming_response_balance_sheet(self, client: Brapi) -> None:
        with client.v2.stocks.with_streaming_response.balance_sheet(
            symbols="PETR4,VALE3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock = response.parse()
            assert_matches_type(StockBalanceSheetResponse, stock, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_cash_flow(self, client: Brapi) -> None:
        stock = client.v2.stocks.cash_flow(
            symbols="PETR4,VALE3",
        )
        assert_matches_type(StockCashFlowResponse, stock, path=["response"])

    @parametrize
    def test_method_cash_flow_with_all_params(self, client: Brapi) -> None:
        stock = client.v2.stocks.cash_flow(
            symbols="PETR4,VALE3",
            end_date="2024-12-31",
            period="annual",
            start_date="2024-01-01",
        )
        assert_matches_type(StockCashFlowResponse, stock, path=["response"])

    @parametrize
    def test_raw_response_cash_flow(self, client: Brapi) -> None:
        response = client.v2.stocks.with_raw_response.cash_flow(
            symbols="PETR4,VALE3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock = response.parse()
        assert_matches_type(StockCashFlowResponse, stock, path=["response"])

    @parametrize
    def test_streaming_response_cash_flow(self, client: Brapi) -> None:
        with client.v2.stocks.with_streaming_response.cash_flow(
            symbols="PETR4,VALE3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock = response.parse()
            assert_matches_type(StockCashFlowResponse, stock, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_dividends(self, client: Brapi) -> None:
        stock = client.v2.stocks.dividends(
            symbols="PETR4,VALE3",
        )
        assert_matches_type(StockDividendsResponse, stock, path=["response"])

    @parametrize
    def test_method_dividends_with_all_params(self, client: Brapi) -> None:
        stock = client.v2.stocks.dividends(
            symbols="PETR4,VALE3",
            end_date="2024-12-31",
            include_raw="true",
            sort_by="paymentDate",
            sort_order="desc",
            start_date="2024-01-01",
        )
        assert_matches_type(StockDividendsResponse, stock, path=["response"])

    @parametrize
    def test_raw_response_dividends(self, client: Brapi) -> None:
        response = client.v2.stocks.with_raw_response.dividends(
            symbols="PETR4,VALE3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock = response.parse()
        assert_matches_type(StockDividendsResponse, stock, path=["response"])

    @parametrize
    def test_streaming_response_dividends(self, client: Brapi) -> None:
        with client.v2.stocks.with_streaming_response.dividends(
            symbols="PETR4,VALE3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock = response.parse()
            assert_matches_type(StockDividendsResponse, stock, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_financial_data(self, client: Brapi) -> None:
        stock = client.v2.stocks.financial_data(
            symbols="PETR4,VALE3",
        )
        assert_matches_type(StockFinancialDataResponse, stock, path=["response"])

    @parametrize
    def test_method_financial_data_with_all_params(self, client: Brapi) -> None:
        stock = client.v2.stocks.financial_data(
            symbols="PETR4,VALE3",
            end_date="2024-12-31",
            mode="current",
            period="annual",
            start_date="2024-01-01",
        )
        assert_matches_type(StockFinancialDataResponse, stock, path=["response"])

    @parametrize
    def test_raw_response_financial_data(self, client: Brapi) -> None:
        response = client.v2.stocks.with_raw_response.financial_data(
            symbols="PETR4,VALE3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock = response.parse()
        assert_matches_type(StockFinancialDataResponse, stock, path=["response"])

    @parametrize
    def test_streaming_response_financial_data(self, client: Brapi) -> None:
        with client.v2.stocks.with_streaming_response.financial_data(
            symbols="PETR4,VALE3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock = response.parse()
            assert_matches_type(StockFinancialDataResponse, stock, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_historical(self, client: Brapi) -> None:
        stock = client.v2.stocks.historical(
            symbols="PETR4,VALE3",
        )
        assert_matches_type(StockHistoricalResponse, stock, path=["response"])

    @parametrize
    def test_method_historical_with_all_params(self, client: Brapi) -> None:
        stock = client.v2.stocks.historical(
            symbols="PETR4,VALE3",
            end_date="2024-12-31",
            include_raw="true",
            interval="1d",
            range="1y",
            sort_order="desc",
            start_date="2024-01-01",
        )
        assert_matches_type(StockHistoricalResponse, stock, path=["response"])

    @parametrize
    def test_raw_response_historical(self, client: Brapi) -> None:
        response = client.v2.stocks.with_raw_response.historical(
            symbols="PETR4,VALE3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock = response.parse()
        assert_matches_type(StockHistoricalResponse, stock, path=["response"])

    @parametrize
    def test_streaming_response_historical(self, client: Brapi) -> None:
        with client.v2.stocks.with_streaming_response.historical(
            symbols="PETR4,VALE3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock = response.parse()
            assert_matches_type(StockHistoricalResponse, stock, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_income_statement(self, client: Brapi) -> None:
        stock = client.v2.stocks.income_statement(
            symbols="PETR4,VALE3",
        )
        assert_matches_type(StockIncomeStatementResponse, stock, path=["response"])

    @parametrize
    def test_method_income_statement_with_all_params(self, client: Brapi) -> None:
        stock = client.v2.stocks.income_statement(
            symbols="PETR4,VALE3",
            end_date="2024-12-31",
            period="annual",
            start_date="2024-01-01",
        )
        assert_matches_type(StockIncomeStatementResponse, stock, path=["response"])

    @parametrize
    def test_raw_response_income_statement(self, client: Brapi) -> None:
        response = client.v2.stocks.with_raw_response.income_statement(
            symbols="PETR4,VALE3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock = response.parse()
        assert_matches_type(StockIncomeStatementResponse, stock, path=["response"])

    @parametrize
    def test_streaming_response_income_statement(self, client: Brapi) -> None:
        with client.v2.stocks.with_streaming_response.income_statement(
            symbols="PETR4,VALE3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock = response.parse()
            assert_matches_type(StockIncomeStatementResponse, stock, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_insider_transactions(self, client: Brapi) -> None:
        stock = client.v2.stocks.insider_transactions(
            symbols="PETR4,VALE3",
        )
        assert_matches_type(StockInsiderTransactionsResponse, stock, path=["response"])

    @parametrize
    def test_method_insider_transactions_with_all_params(self, client: Brapi) -> None:
        stock = client.v2.stocks.insider_transactions(
            symbols="PETR4,VALE3",
            all_versions="true",
            company_relation="company",
            direction="credit",
            end_date="2026-08-31",
            limit=1,
            movement_type="Compra à vista",
            page=1,
            role_group="controller",
            start_date="2026-01-01",
        )
        assert_matches_type(StockInsiderTransactionsResponse, stock, path=["response"])

    @parametrize
    def test_raw_response_insider_transactions(self, client: Brapi) -> None:
        response = client.v2.stocks.with_raw_response.insider_transactions(
            symbols="PETR4,VALE3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock = response.parse()
        assert_matches_type(StockInsiderTransactionsResponse, stock, path=["response"])

    @parametrize
    def test_streaming_response_insider_transactions(self, client: Brapi) -> None:
        with client.v2.stocks.with_streaming_response.insider_transactions(
            symbols="PETR4,VALE3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock = response.parse()
            assert_matches_type(StockInsiderTransactionsResponse, stock, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_profile(self, client: Brapi) -> None:
        stock = client.v2.stocks.profile(
            symbols="PETR4,VALE3",
        )
        assert_matches_type(StockProfileResponse, stock, path=["response"])

    @parametrize
    def test_raw_response_profile(self, client: Brapi) -> None:
        response = client.v2.stocks.with_raw_response.profile(
            symbols="PETR4,VALE3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock = response.parse()
        assert_matches_type(StockProfileResponse, stock, path=["response"])

    @parametrize
    def test_streaming_response_profile(self, client: Brapi) -> None:
        with client.v2.stocks.with_streaming_response.profile(
            symbols="PETR4,VALE3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock = response.parse()
            assert_matches_type(StockProfileResponse, stock, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_quote(self, client: Brapi) -> None:
        stock = client.v2.stocks.quote(
            symbols="PETR4,VALE3",
        )
        assert_matches_type(StockQuoteResponse, stock, path=["response"])

    @parametrize
    def test_raw_response_quote(self, client: Brapi) -> None:
        response = client.v2.stocks.with_raw_response.quote(
            symbols="PETR4,VALE3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock = response.parse()
        assert_matches_type(StockQuoteResponse, stock, path=["response"])

    @parametrize
    def test_streaming_response_quote(self, client: Brapi) -> None:
        with client.v2.stocks.with_streaming_response.quote(
            symbols="PETR4,VALE3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock = response.parse()
            assert_matches_type(StockQuoteResponse, stock, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_statistics(self, client: Brapi) -> None:
        stock = client.v2.stocks.statistics(
            symbols="PETR4,VALE3",
        )
        assert_matches_type(StockStatisticsResponse, stock, path=["response"])

    @parametrize
    def test_method_statistics_with_all_params(self, client: Brapi) -> None:
        stock = client.v2.stocks.statistics(
            symbols="PETR4,VALE3",
            end_date="2024-12-31",
            mode="current",
            period="annual",
            start_date="2024-01-01",
        )
        assert_matches_type(StockStatisticsResponse, stock, path=["response"])

    @parametrize
    def test_raw_response_statistics(self, client: Brapi) -> None:
        response = client.v2.stocks.with_raw_response.statistics(
            symbols="PETR4,VALE3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock = response.parse()
        assert_matches_type(StockStatisticsResponse, stock, path=["response"])

    @parametrize
    def test_streaming_response_statistics(self, client: Brapi) -> None:
        with client.v2.stocks.with_streaming_response.statistics(
            symbols="PETR4,VALE3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock = response.parse()
            assert_matches_type(StockStatisticsResponse, stock, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_value_added(self, client: Brapi) -> None:
        stock = client.v2.stocks.value_added(
            symbols="PETR4,VALE3",
        )
        assert_matches_type(StockValueAddedResponse, stock, path=["response"])

    @parametrize
    def test_method_value_added_with_all_params(self, client: Brapi) -> None:
        stock = client.v2.stocks.value_added(
            symbols="PETR4,VALE3",
            end_date="2024-12-31",
            period="annual",
            start_date="2024-01-01",
        )
        assert_matches_type(StockValueAddedResponse, stock, path=["response"])

    @parametrize
    def test_raw_response_value_added(self, client: Brapi) -> None:
        response = client.v2.stocks.with_raw_response.value_added(
            symbols="PETR4,VALE3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock = response.parse()
        assert_matches_type(StockValueAddedResponse, stock, path=["response"])

    @parametrize
    def test_streaming_response_value_added(self, client: Brapi) -> None:
        with client.v2.stocks.with_streaming_response.value_added(
            symbols="PETR4,VALE3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock = response.parse()
            assert_matches_type(StockValueAddedResponse, stock, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStocks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_balance_sheet(self, async_client: AsyncBrapi) -> None:
        stock = await async_client.v2.stocks.balance_sheet(
            symbols="PETR4,VALE3",
        )
        assert_matches_type(StockBalanceSheetResponse, stock, path=["response"])

    @parametrize
    async def test_method_balance_sheet_with_all_params(self, async_client: AsyncBrapi) -> None:
        stock = await async_client.v2.stocks.balance_sheet(
            symbols="PETR4,VALE3",
            end_date="2024-12-31",
            period="annual",
            start_date="2024-01-01",
        )
        assert_matches_type(StockBalanceSheetResponse, stock, path=["response"])

    @parametrize
    async def test_raw_response_balance_sheet(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.stocks.with_raw_response.balance_sheet(
            symbols="PETR4,VALE3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock = await response.parse()
        assert_matches_type(StockBalanceSheetResponse, stock, path=["response"])

    @parametrize
    async def test_streaming_response_balance_sheet(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.stocks.with_streaming_response.balance_sheet(
            symbols="PETR4,VALE3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock = await response.parse()
            assert_matches_type(StockBalanceSheetResponse, stock, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_cash_flow(self, async_client: AsyncBrapi) -> None:
        stock = await async_client.v2.stocks.cash_flow(
            symbols="PETR4,VALE3",
        )
        assert_matches_type(StockCashFlowResponse, stock, path=["response"])

    @parametrize
    async def test_method_cash_flow_with_all_params(self, async_client: AsyncBrapi) -> None:
        stock = await async_client.v2.stocks.cash_flow(
            symbols="PETR4,VALE3",
            end_date="2024-12-31",
            period="annual",
            start_date="2024-01-01",
        )
        assert_matches_type(StockCashFlowResponse, stock, path=["response"])

    @parametrize
    async def test_raw_response_cash_flow(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.stocks.with_raw_response.cash_flow(
            symbols="PETR4,VALE3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock = await response.parse()
        assert_matches_type(StockCashFlowResponse, stock, path=["response"])

    @parametrize
    async def test_streaming_response_cash_flow(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.stocks.with_streaming_response.cash_flow(
            symbols="PETR4,VALE3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock = await response.parse()
            assert_matches_type(StockCashFlowResponse, stock, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_dividends(self, async_client: AsyncBrapi) -> None:
        stock = await async_client.v2.stocks.dividends(
            symbols="PETR4,VALE3",
        )
        assert_matches_type(StockDividendsResponse, stock, path=["response"])

    @parametrize
    async def test_method_dividends_with_all_params(self, async_client: AsyncBrapi) -> None:
        stock = await async_client.v2.stocks.dividends(
            symbols="PETR4,VALE3",
            end_date="2024-12-31",
            include_raw="true",
            sort_by="paymentDate",
            sort_order="desc",
            start_date="2024-01-01",
        )
        assert_matches_type(StockDividendsResponse, stock, path=["response"])

    @parametrize
    async def test_raw_response_dividends(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.stocks.with_raw_response.dividends(
            symbols="PETR4,VALE3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock = await response.parse()
        assert_matches_type(StockDividendsResponse, stock, path=["response"])

    @parametrize
    async def test_streaming_response_dividends(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.stocks.with_streaming_response.dividends(
            symbols="PETR4,VALE3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock = await response.parse()
            assert_matches_type(StockDividendsResponse, stock, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_financial_data(self, async_client: AsyncBrapi) -> None:
        stock = await async_client.v2.stocks.financial_data(
            symbols="PETR4,VALE3",
        )
        assert_matches_type(StockFinancialDataResponse, stock, path=["response"])

    @parametrize
    async def test_method_financial_data_with_all_params(self, async_client: AsyncBrapi) -> None:
        stock = await async_client.v2.stocks.financial_data(
            symbols="PETR4,VALE3",
            end_date="2024-12-31",
            mode="current",
            period="annual",
            start_date="2024-01-01",
        )
        assert_matches_type(StockFinancialDataResponse, stock, path=["response"])

    @parametrize
    async def test_raw_response_financial_data(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.stocks.with_raw_response.financial_data(
            symbols="PETR4,VALE3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock = await response.parse()
        assert_matches_type(StockFinancialDataResponse, stock, path=["response"])

    @parametrize
    async def test_streaming_response_financial_data(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.stocks.with_streaming_response.financial_data(
            symbols="PETR4,VALE3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock = await response.parse()
            assert_matches_type(StockFinancialDataResponse, stock, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_historical(self, async_client: AsyncBrapi) -> None:
        stock = await async_client.v2.stocks.historical(
            symbols="PETR4,VALE3",
        )
        assert_matches_type(StockHistoricalResponse, stock, path=["response"])

    @parametrize
    async def test_method_historical_with_all_params(self, async_client: AsyncBrapi) -> None:
        stock = await async_client.v2.stocks.historical(
            symbols="PETR4,VALE3",
            end_date="2024-12-31",
            include_raw="true",
            interval="1d",
            range="1y",
            sort_order="desc",
            start_date="2024-01-01",
        )
        assert_matches_type(StockHistoricalResponse, stock, path=["response"])

    @parametrize
    async def test_raw_response_historical(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.stocks.with_raw_response.historical(
            symbols="PETR4,VALE3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock = await response.parse()
        assert_matches_type(StockHistoricalResponse, stock, path=["response"])

    @parametrize
    async def test_streaming_response_historical(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.stocks.with_streaming_response.historical(
            symbols="PETR4,VALE3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock = await response.parse()
            assert_matches_type(StockHistoricalResponse, stock, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_income_statement(self, async_client: AsyncBrapi) -> None:
        stock = await async_client.v2.stocks.income_statement(
            symbols="PETR4,VALE3",
        )
        assert_matches_type(StockIncomeStatementResponse, stock, path=["response"])

    @parametrize
    async def test_method_income_statement_with_all_params(self, async_client: AsyncBrapi) -> None:
        stock = await async_client.v2.stocks.income_statement(
            symbols="PETR4,VALE3",
            end_date="2024-12-31",
            period="annual",
            start_date="2024-01-01",
        )
        assert_matches_type(StockIncomeStatementResponse, stock, path=["response"])

    @parametrize
    async def test_raw_response_income_statement(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.stocks.with_raw_response.income_statement(
            symbols="PETR4,VALE3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock = await response.parse()
        assert_matches_type(StockIncomeStatementResponse, stock, path=["response"])

    @parametrize
    async def test_streaming_response_income_statement(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.stocks.with_streaming_response.income_statement(
            symbols="PETR4,VALE3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock = await response.parse()
            assert_matches_type(StockIncomeStatementResponse, stock, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_insider_transactions(self, async_client: AsyncBrapi) -> None:
        stock = await async_client.v2.stocks.insider_transactions(
            symbols="PETR4,VALE3",
        )
        assert_matches_type(StockInsiderTransactionsResponse, stock, path=["response"])

    @parametrize
    async def test_method_insider_transactions_with_all_params(self, async_client: AsyncBrapi) -> None:
        stock = await async_client.v2.stocks.insider_transactions(
            symbols="PETR4,VALE3",
            all_versions="true",
            company_relation="company",
            direction="credit",
            end_date="2026-08-31",
            limit=1,
            movement_type="Compra à vista",
            page=1,
            role_group="controller",
            start_date="2026-01-01",
        )
        assert_matches_type(StockInsiderTransactionsResponse, stock, path=["response"])

    @parametrize
    async def test_raw_response_insider_transactions(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.stocks.with_raw_response.insider_transactions(
            symbols="PETR4,VALE3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock = await response.parse()
        assert_matches_type(StockInsiderTransactionsResponse, stock, path=["response"])

    @parametrize
    async def test_streaming_response_insider_transactions(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.stocks.with_streaming_response.insider_transactions(
            symbols="PETR4,VALE3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock = await response.parse()
            assert_matches_type(StockInsiderTransactionsResponse, stock, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_profile(self, async_client: AsyncBrapi) -> None:
        stock = await async_client.v2.stocks.profile(
            symbols="PETR4,VALE3",
        )
        assert_matches_type(StockProfileResponse, stock, path=["response"])

    @parametrize
    async def test_raw_response_profile(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.stocks.with_raw_response.profile(
            symbols="PETR4,VALE3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock = await response.parse()
        assert_matches_type(StockProfileResponse, stock, path=["response"])

    @parametrize
    async def test_streaming_response_profile(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.stocks.with_streaming_response.profile(
            symbols="PETR4,VALE3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock = await response.parse()
            assert_matches_type(StockProfileResponse, stock, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_quote(self, async_client: AsyncBrapi) -> None:
        stock = await async_client.v2.stocks.quote(
            symbols="PETR4,VALE3",
        )
        assert_matches_type(StockQuoteResponse, stock, path=["response"])

    @parametrize
    async def test_raw_response_quote(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.stocks.with_raw_response.quote(
            symbols="PETR4,VALE3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock = await response.parse()
        assert_matches_type(StockQuoteResponse, stock, path=["response"])

    @parametrize
    async def test_streaming_response_quote(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.stocks.with_streaming_response.quote(
            symbols="PETR4,VALE3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock = await response.parse()
            assert_matches_type(StockQuoteResponse, stock, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_statistics(self, async_client: AsyncBrapi) -> None:
        stock = await async_client.v2.stocks.statistics(
            symbols="PETR4,VALE3",
        )
        assert_matches_type(StockStatisticsResponse, stock, path=["response"])

    @parametrize
    async def test_method_statistics_with_all_params(self, async_client: AsyncBrapi) -> None:
        stock = await async_client.v2.stocks.statistics(
            symbols="PETR4,VALE3",
            end_date="2024-12-31",
            mode="current",
            period="annual",
            start_date="2024-01-01",
        )
        assert_matches_type(StockStatisticsResponse, stock, path=["response"])

    @parametrize
    async def test_raw_response_statistics(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.stocks.with_raw_response.statistics(
            symbols="PETR4,VALE3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock = await response.parse()
        assert_matches_type(StockStatisticsResponse, stock, path=["response"])

    @parametrize
    async def test_streaming_response_statistics(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.stocks.with_streaming_response.statistics(
            symbols="PETR4,VALE3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock = await response.parse()
            assert_matches_type(StockStatisticsResponse, stock, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_value_added(self, async_client: AsyncBrapi) -> None:
        stock = await async_client.v2.stocks.value_added(
            symbols="PETR4,VALE3",
        )
        assert_matches_type(StockValueAddedResponse, stock, path=["response"])

    @parametrize
    async def test_method_value_added_with_all_params(self, async_client: AsyncBrapi) -> None:
        stock = await async_client.v2.stocks.value_added(
            symbols="PETR4,VALE3",
            end_date="2024-12-31",
            period="annual",
            start_date="2024-01-01",
        )
        assert_matches_type(StockValueAddedResponse, stock, path=["response"])

    @parametrize
    async def test_raw_response_value_added(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.stocks.with_raw_response.value_added(
            symbols="PETR4,VALE3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock = await response.parse()
        assert_matches_type(StockValueAddedResponse, stock, path=["response"])

    @parametrize
    async def test_streaming_response_value_added(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.stocks.with_streaming_response.value_added(
            symbols="PETR4,VALE3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock = await response.parse()
            assert_matches_type(StockValueAddedResponse, stock, path=["response"])

        assert cast(Any, response.is_closed) is True
