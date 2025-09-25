#!/usr/bin/env python3
"""Module for accessing Annif REST API"""

import requests
from importlib import metadata


# Default API base URL
API_BASE = 'https://api.annif.org/v1/'


class AnnifClient:
    """Client class for accessing Annif REST API"""

    def __init__(self, api_base=API_BASE):
        self.api_base = api_base
        version = metadata.version("annif-client")
        self._headers = {
            "User-Agent": f"Annif-client/{version}",
        }

    @property
    def api_info(self):
        """Get basic information of the API endpoint"""
        req = requests.get(self.api_base, headers=self._headers)
        req.raise_for_status()
        return req.json()

    @property
    def projects(self):
        """Get a list of projects available on the API endpoint"""
        req = requests.get(self.api_base + 'projects', headers=self._headers)
        req.raise_for_status()
        return req.json()['projects']

    def detect_language(self, text, languages):
        """Detect the language of the given text using the Annif REST API.
        :param text: The text to analyze (str or file-like object)
        :param languages: List of candidate language codes (e.g., ['en', 'fi'])
        """
        if not isinstance(text, str):
            text = text.read()

        payload = {'text': text, 'languages': languages}
        url = self.api_base + 'detect-language'
        req = requests.post(url, json=payload, headers=self._headers)
        if req.status_code == 404:
            raise ValueError(req.json().get('detail', 'Not found'))
        req.raise_for_status()
        return req.json()

    def get_project(self, project_id):
        """Get a single project by project ID"""
        req = requests.get(
            self.api_base + 'projects/{}'.format(project_id),
            headers=self._headers
        )
        if req.status_code == 404:
            raise ValueError(req.json()['detail'])
        req.raise_for_status()
        return req.json()

    def suggest(self, project_id, text, limit=None, threshold=None):
        """Suggest subjects for a text (either a string or a file-like object)
        using a specified project and optional limit and/or threshold settings.
        """
        if not isinstance(text, str):
            text = text.read()

        payload = {'text': text}

        if limit is not None:
            payload['limit'] = limit

        if threshold is not None:
            payload['threshold'] = threshold

        url = self.api_base + 'projects/{}/suggest'.format(project_id)
        req = requests.post(url, data=payload, headers=self._headers)
        if req.status_code == 404:
            raise ValueError(req.json()['detail'])
        req.raise_for_status()
        return req.json()['results']

    def suggest_batch(self, project_id, documents, limit=None, threshold=None):
        """Suggest subjects for a batch of text documents (a list of
        dictionaries; each dictionary contains a text and optionally an
        identifier string for the document). The specified project is used with
        the optional limit and/or threshold settings.
        """

        payload = {'documents': documents}
        params = {}
        if limit is not None:
            params['limit'] = limit

        if threshold is not None:
            params['threshold'] = threshold

        url = self.api_base + 'projects/{}/suggest-batch'.format(project_id)
        req = requests.post(
            url, json=payload, params=params, headers=self._headers)
        if req.status_code == 404:
            raise ValueError(req.json()['detail'])
        req.raise_for_status()
        return req.json()

    def learn(self, project_id, documents):
        """Further train an existing project on a text with given subjects."""

        url = self.api_base + 'projects/{}/learn'.format(project_id)
        req = requests.post(url, json=documents, headers=self._headers)
        if req.status_code == 404:
            raise ValueError(req.json()['detail'])
        req.raise_for_status()
        return req

    analyze = suggest  # Alias for backwards compatibility

    def __str__(self):
        """Return a string representation of this object"""
        return "AnnifClient(api_base='{}')".format(self.api_base)


if __name__ == '__main__':
    print("Demonstrating usage of AnnifClient")

    print()

    print("* Creating an AnnifClient object")
    annif = AnnifClient()
    print(f"* The client uses Annif API at {annif.api_base}")
    print(f"* The version of Annif serving the API is {annif.api_info['version']}")

    print()
    print(
        "* Detecting the language of text: "
        "'The quick brown fox jumped over the lazy dog' "
        "(candidates: en, fi, sv)"
    )
    lang_result = annif.detect_language(
        'The quick brown fox jumped over the lazy dog',
        languages=['en', 'fi', 'sv']
    )
    for res in lang_result['results']:
        print(
            f"Language: {str(res['language']):<6}score: {res['score']}"
    )

    print()
    print("* Finding the available projects")
    for project in annif.projects:
        print("Project id: {:<16} lang: {}  name: {}".format(
            project['project_id'], project['language'], project['name']))

    print()

    print("* Looking up information about a specific project")
    project = annif.get_project('yso-en')
    print("Project id: {:<16} lang: {}  name: {}".format(
        project['project_id'], project['language'], project['name']))

    print()

    print("* Analyzing a short text from a string")
    results = annif.suggest(project_id='yso-en',
                            text='The quick brown fox jumped over the lazy dog')
    for result in results:
        print("<{}>\t{:.4f}\t{}".format(
            result['uri'], result['score'], result['label']))

    print()

    print("* Analyzing a longer text from a file, with a limit on number of results")
    with open('LICENSE.txt') as license_file:
        results = annif.suggest(project_id='yso-en',
                                text=license_file, limit=5)
        for result in results:
            print("<{}>\t{:.4f}\t{}".format(
                result['uri'], result['score'], result['label']))

    print()

    print("* Analyzing a batch of text documents")
    documents = [
        {"document_id":
            "doc-0",
         "text":
            "The quick brown fox jumped over the lazy dog"},
        {"document_id":
            "doc-1",
        "text":
            "The National Library of Finland is the "
            "oldest scholarly library in Finland."},
        {"document_id":
            "doc-2",
        "text":
            "Annif is a multi-algorithm automated subject indexing "
            "tool for libraries, archives and museums."},
    ]
    results = annif.suggest_batch(project_id='yso-en',
                                  documents=documents)
    for document in results:
        print(document['document_id'])
        for result in document["results"]:
            print("<{}>\t{:.4f}\t{}".format(
                result['uri'], result['score'], result['label']))
