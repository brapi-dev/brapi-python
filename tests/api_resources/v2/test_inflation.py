# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from brapi import Brapi, AsyncBrapi
from tests.utils import assert_matches_type
from brapi._utils import parse_date
from brapi.types.v2 import (
    InflationRetrieveResponse,
    InflationListAvailableResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInflation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Brapi) -> None:
        inflation = client.v2.inflation.retrieve()
        assert_matches_type(InflationRetrieveResponse, inflation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Brapi) -> None:
        inflation = client.v2.inflation.retrieve(
            token="token",
            country="country",
            end=parse_date("2019-12-27"),
            historical=True,
            sort_by="date",
            sort_order="asc",
            start=parse_date("2019-12-27"),
        )
        assert_matches_type(InflationRetrieveResponse, inflation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Brapi) -> None:
        response = client.v2.inflation.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inflation = response.parse()
        assert_matches_type(InflationRetrieveResponse, inflation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Brapi) -> None:
        with client.v2.inflation.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inflation = response.parse()
            assert_matches_type(InflationRetrieveResponse, inflation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_available(self, client: Brapi) -> None:
        inflation = client.v2.inflation.list_available()
        assert_matches_type(InflationListAvailableResponse, inflation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_available_with_all_params(self, client: Brapi) -> None:
        inflation = client.v2.inflation.list_available(
            token="token",
            search="search",
        )
        assert_matches_type(InflationListAvailableResponse, inflation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_available(self, client: Brapi) -> None:
        response = client.v2.inflation.with_raw_response.list_available()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inflation = response.parse()
        assert_matches_type(InflationListAvailableResponse, inflation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_available(self, client: Brapi) -> None:
        with client.v2.inflation.with_streaming_response.list_available() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inflation = response.parse()
            assert_matches_type(InflationListAvailableResponse, inflation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInflation:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBrapi) -> None:
        inflation = await async_client.v2.inflation.retrieve()
        assert_matches_type(InflationRetrieveResponse, inflation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncBrapi) -> None:
        inflation = await async_client.v2.inflation.retrieve(
            token="token",
            country="country",
            end=parse_date("2019-12-27"),
            historical=True,
            sort_by="date",
            sort_order="asc",
            start=parse_date("2019-12-27"),
        )
        assert_matches_type(InflationRetrieveResponse, inflation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.inflation.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inflation = await response.parse()
        assert_matches_type(InflationRetrieveResponse, inflation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.inflation.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inflation = await response.parse()
            assert_matches_type(InflationRetrieveResponse, inflation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_available(self, async_client: AsyncBrapi) -> None:
        inflation = await async_client.v2.inflation.list_available()
        assert_matches_type(InflationListAvailableResponse, inflation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_available_with_all_params(self, async_client: AsyncBrapi) -> None:
        inflation = await async_client.v2.inflation.list_available(
            token="token",
            search="search",
        )
        assert_matches_type(InflationListAvailableResponse, inflation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_available(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.inflation.with_raw_response.list_available()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inflation = await response.parse()
        assert_matches_type(InflationListAvailableResponse, inflation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_available(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.inflation.with_streaming_response.list_available() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inflation = await response.parse()
            assert_matches_type(InflationListAvailableResponse, inflation, path=["response"])

        assert cast(Any, response.is_closed) is True
