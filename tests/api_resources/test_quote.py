# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from brapi import Brapi, AsyncBrapi
from brapi.types import QuoteListResponse, QuoteRetrieveResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQuote:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Brapi) -> None:
        quote = client.quote.retrieve(
            tickers="PETR4,MGLU3",
        )
        assert_matches_type(QuoteRetrieveResponse, quote, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Brapi) -> None:
        quote = client.quote.retrieve(
            tickers="PETR4,MGLU3",
            token="token",
            dividends=True,
            fundamental=True,
            interval="1d",
            modules=["summaryProfile", "balanceSheetHistory", "financialData"],
            range="5d",
        )
        assert_matches_type(QuoteRetrieveResponse, quote, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Brapi) -> None:
        response = client.quote.with_raw_response.retrieve(
            tickers="PETR4,MGLU3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = response.parse()
        assert_matches_type(QuoteRetrieveResponse, quote, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Brapi) -> None:
        with client.quote.with_streaming_response.retrieve(
            tickers="PETR4,MGLU3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = response.parse()
            assert_matches_type(QuoteRetrieveResponse, quote, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Brapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tickers` but received ''"):
            client.quote.with_raw_response.retrieve(
                tickers="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Brapi) -> None:
        quote = client.quote.list()
        assert_matches_type(QuoteListResponse, quote, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Brapi) -> None:
        quote = client.quote.list(
            token="token",
            limit=1,
            page=1,
            search="search",
            sector="Retail Trade",
            sort_by="name",
            sort_order="asc",
            type="stock",
        )
        assert_matches_type(QuoteListResponse, quote, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Brapi) -> None:
        response = client.quote.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = response.parse()
        assert_matches_type(QuoteListResponse, quote, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Brapi) -> None:
        with client.quote.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = response.parse()
            assert_matches_type(QuoteListResponse, quote, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncQuote:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBrapi) -> None:
        quote = await async_client.quote.retrieve(
            tickers="PETR4,MGLU3",
        )
        assert_matches_type(QuoteRetrieveResponse, quote, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncBrapi) -> None:
        quote = await async_client.quote.retrieve(
            tickers="PETR4,MGLU3",
            token="token",
            dividends=True,
            fundamental=True,
            interval="1d",
            modules=["summaryProfile", "balanceSheetHistory", "financialData"],
            range="5d",
        )
        assert_matches_type(QuoteRetrieveResponse, quote, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBrapi) -> None:
        response = await async_client.quote.with_raw_response.retrieve(
            tickers="PETR4,MGLU3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = await response.parse()
        assert_matches_type(QuoteRetrieveResponse, quote, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBrapi) -> None:
        async with async_client.quote.with_streaming_response.retrieve(
            tickers="PETR4,MGLU3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = await response.parse()
            assert_matches_type(QuoteRetrieveResponse, quote, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBrapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tickers` but received ''"):
            await async_client.quote.with_raw_response.retrieve(
                tickers="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBrapi) -> None:
        quote = await async_client.quote.list()
        assert_matches_type(QuoteListResponse, quote, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBrapi) -> None:
        quote = await async_client.quote.list(
            token="token",
            limit=1,
            page=1,
            search="search",
            sector="Retail Trade",
            sort_by="name",
            sort_order="asc",
            type="stock",
        )
        assert_matches_type(QuoteListResponse, quote, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBrapi) -> None:
        response = await async_client.quote.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = await response.parse()
        assert_matches_type(QuoteListResponse, quote, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBrapi) -> None:
        async with async_client.quote.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = await response.parse()
            assert_matches_type(QuoteListResponse, quote, path=["response"])

        assert cast(Any, response.is_closed) is True
