import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='annif_client',
    version='0.2.0',
    url='https://github.com/NatLibFi/Annif-client',
    author='Osma Suominen',
    author_email='osma.suominen@helsinki.fi',
    description='Python client library for accessing Annif REST API',
    long_description=read('README.md'),
    py_modules=['annif_client'],
    install_requires=['requests'],
    extras_require={
        'dev': ['bumpversion']
    })
