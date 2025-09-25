import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='annif-client',
    version='0.5.0',
    url='https://github.com/NatLibFi/Annif-client',
    author='Osma Suominen',
    author_email='osma.suominen@helsinki.fi',
    description='Python client library for accessing Annif REST API',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    py_modules=['annif_client'],
    install_requires=['requests'],
    extras_require={
        'dev': ['bumpversion','pytest','responses']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ]
)
