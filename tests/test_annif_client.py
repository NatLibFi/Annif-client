"""Unit tests for AnnifClient class"""

from annif_client import AnnifClient, API_BASE
import os.path
import pytest
import responses


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
def test_projects(client):
    datafile = os.path.join(os.path.dirname(__file__), 'data/projects.json')
    responses.add(responses.GET,
                  'http://api.annif.org/v1/projects',
                  body=open(datafile).read())
    result = client.projects
    assert len(result) == 2
