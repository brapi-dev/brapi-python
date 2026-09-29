# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from brapi import Brapi, AsyncBrapi
from tests.utils import assert_matches_type
from brapi.types.v2 import DictionaryRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDictionary:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Brapi) -> None:
        dictionary = client.v2.dictionary.retrieve()
        assert_matches_type(DictionaryRetrieveResponse, dictionary, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Brapi) -> None:
        dictionary = client.v2.dictionary.retrieve(
            category="treasury",
            search="patrimônio",
        )
        assert_matches_type(DictionaryRetrieveResponse, dictionary, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Brapi) -> None:
        response = client.v2.dictionary.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dictionary = response.parse()
        assert_matches_type(DictionaryRetrieveResponse, dictionary, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Brapi) -> None:
        with client.v2.dictionary.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dictionary = response.parse()
            assert_matches_type(DictionaryRetrieveResponse, dictionary, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDictionary:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBrapi) -> None:
        dictionary = await async_client.v2.dictionary.retrieve()
        assert_matches_type(DictionaryRetrieveResponse, dictionary, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncBrapi) -> None:
        dictionary = await async_client.v2.dictionary.retrieve(
            category="treasury",
            search="patrimônio",
        )
        assert_matches_type(DictionaryRetrieveResponse, dictionary, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBrapi) -> None:
        response = await async_client.v2.dictionary.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dictionary = await response.parse()
        assert_matches_type(DictionaryRetrieveResponse, dictionary, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBrapi) -> None:
        async with async_client.v2.dictionary.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dictionary = await response.parse()
            assert_matches_type(DictionaryRetrieveResponse, dictionary, path=["response"])

        assert cast(Any, response.is_closed) is True
