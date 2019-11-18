#!/usr/bin/env python3
"""Module for accessing Annif REST API"""

import requests

# Default API base URL
API_BASE = 'http://api.annif.org/v1/'


class AnnifClient:
    """Client class for accessing Annif REST API"""

    def __init__(self, api_base=API_BASE):
        self.api_base = api_base

    @property
    def projects(self):
        """Get a list of projects available on the API endpoint"""
        req = requests.get(self.api_base + 'projects')
        req.raise_for_status()
        return req.json()['projects']

    def get_project(self, project_id):
        """Get a single project by project ID"""
        req = requests.get(self.api_base + 'projects/{}'.format(project_id))
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
        req = requests.post(url, data=payload)
        if req.status_code == 404:
            raise ValueError(req.json()['detail'])
        req.raise_for_status()
        return req.json()['results']

    def learn(self, project_id, documents):
        """Further train an existing project on a text with given subjects."""

        url = self.api_base + 'projects/{}/learn'.format(project_id)
        req = requests.post(url, json=documents)
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
    print("Now we have an AnnifClient object:", annif)
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

    print("* Learning on a document")
    documents = [
        {"subjects":
            [{"uri": "http://example.org/fox", "label": "fox"}],
        "text":
            "the quick brown fox"
        }
    ]
    req = annif.learn(project_id='dummy-en', documents=documents)
    print(req)
