import pytest
import responses
from main import get_random_cat_image


@responses.activate
def test_successful_request():
    responses.add(
        responses.GET,
        "https://api.thecatapi.com/v1/images/search",
        json=[{"id": "abc123", "url": "https://cdn2.thecatapi.com/images/abc123.jpg"}],
        status=200
    )

    url = get_random_cat_image()
    assert url == "https://cdn2.thecatapi.com/images/abc123.jpg"


@responses.activate
def test_failed_request():
    responses.add(
        responses.GET,
        "https://api.thecatapi.com/v1/images/search",
        status=404
    )

    url = get_random_cat_image()
    assert url is None