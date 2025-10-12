# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from brapi import Brapi, AsyncBrapi
from tests.utils import assert_matches_type
from brapi.types.v2 import (
    CryptoRetrieveResponse,
    CryptoListAvailableResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCrypto:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Brapi) -> None:
        crypto = client.v2.crypto.retrieve(
            coin="coin",
        )
        assert_matches_type(CryptoRetrieveResponse, crypto, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Brapi) -> None:
        crypto = client.v2.crypto.retrieve(
            coin="coin",
            token="token",
            currency="currency",
            interval="1m",
            range="1d",
        )
        assert_matches_type(CryptoRetrieveResponse, crypto, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Brapi) -> None:
        response = client.v2.crypto.with_raw_response.retrieve(
            coin="coin",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crypto = response.parse()
        assert_matches_type(CryptoRetrieveResponse, crypto, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Brapi) -> None:
        with client.v2.crypto.with_streaming_response.retrieve(
            coin="coin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crypto = response.parse()
            assert_matches_type(CryptoRetrieveResponse, crypto, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_available(self, client: Brapi) -> None:
        crypto = client.v2.crypto.list_available()
        assert_matches_type(CryptoListAvailableResponse, crypto, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_available_with_all_params(self, client: Brapi) -> None:
        crypto = client.v2.crypto.list_available(
            token="token",
            search="search",
        )
        assert_matches_type(CryptoListAvailableResponse, crypto, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_available(self, client: Brapi) -> None:
        response = client.v2.crypto.with_raw_response.list_available()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crypto = response.parse()
        assert_matches_type(CryptoListAvailableResponse, crypto, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_available(self, client: Brapi) -> None:
        with client.v2.crypto.with_streaming_response.list_available() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crypto = response.parse()
            assert_matches_type(CryptoListAvailableResponse, crypto, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCrypto:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBrapi) -> None:
        crypto = await async_client.v2.crypto.retrieve(
            coin="coin",
        )
        assert_matches_type(CryptoRetrieveResponse, crypto, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncBrapi) -> None:
        crypto = await async_client.v2.crypto.retrieve(
            coin="coin",
            token="token",
            currency="currency",
            interval="1m",
            range="1d",
        )
        assert_matches_type(CryptoRetrieveResponse, crypto, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.crypto.with_raw_response.retrieve(
            coin="coin",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crypto = await response.parse()
        assert_matches_type(CryptoRetrieveResponse, crypto, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.crypto.with_streaming_response.retrieve(
            coin="coin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crypto = await response.parse()
            assert_matches_type(CryptoRetrieveResponse, crypto, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_available(self, async_client: AsyncBrapi) -> None:
        crypto = await async_client.v2.crypto.list_available()
        assert_matches_type(CryptoListAvailableResponse, crypto, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_available_with_all_params(self, async_client: AsyncBrapi) -> None:
        crypto = await async_client.v2.crypto.list_available(
            token="token",
            search="search",
        )
        assert_matches_type(CryptoListAvailableResponse, crypto, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_available(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.crypto.with_raw_response.list_available()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crypto = await response.parse()
        assert_matches_type(CryptoListAvailableResponse, crypto, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_available(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.crypto.with_streaming_response.list_available() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crypto = await response.parse()
            assert_matches_type(CryptoListAvailableResponse, crypto, path=["response"])

        assert cast(Any, response.is_closed) is True
