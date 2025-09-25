"""Unit tests for AnnifClient class"""

from annif_client import AnnifClient, API_BASE
import os.path
import pytest
import responses
import requests
import importlib
import unittest


@pytest.fixture(scope='module')
def client():
    return AnnifClient()


def test_create_client_default():
    client = AnnifClient()
    assert isinstance(client, AnnifClient)
    assert client.api_base == API_BASE


def test_create_client_api_base():
    client = AnnifClient('http://localhost:5000/v1/')
    assert isinstance(client, AnnifClient)
    assert client.api_base == 'http://localhost:5000/v1/'


@responses.activate
def test_api_info(client):
    datafile = os.path.join(os.path.dirname(__file__), 'data/api-info.json')
    responses.add(responses.GET,
                  'https://api.annif.org/v1/',
                  body=open(datafile).read())
    result = client.api_info
    assert result['title'] == 'Annif REST API'
    assert result['version'] == '0.12.3'


@responses.activate
def test_projects(client):
    datafile = os.path.join(os.path.dirname(__file__), 'data/projects.json')
    responses.add(responses.GET,
                  'https://api.annif.org/v1/projects',
                  body=open(datafile).read())
    result = client.projects
    assert len(result) == 2


def test_headers(client):
    with unittest.mock.patch("requests.get"):
        client.api_info

        version = importlib.metadata.version("annif-client")
        assert requests.get.call_args.kwargs["headers"] == {
            "User-Agent": f"Annif-client/{version}"
        }


@responses.activate
def test_detect_language(client):
    # Mocked response for language detection
    responses.add(
        responses.POST,
        'https://api.annif.org/v1/detect-language',
        json={
            "results": [
                {
                    "language": "en",
                    "score": 0.99
                }
            ]
        },
        status=200
    )
    result = client.detect_language(
        "This is a test sentence.", languages=['en', 'fi'])
    assert isinstance(result["results"], list)
    assert result["results"][0]["language"] == "en"
    assert result["results"][0]["score"] == 0.99
