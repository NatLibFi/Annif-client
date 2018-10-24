# Annif-client

This is a minimal Python 3.x client library for accessing the
[Annif](http://annif.org) REST API which can be used for automated subject
indexing and classification of text documents.

## Installation

The easiest way to install is via pip:

    pip3 install annif-client

## Dependencies

The library depends on the
[requests](http://docs.python-requests.org/en/master/#) module which is used
for HTTP/REST access. If you install this via pip, the dependencies will be
handled automatically.

## How to use

The client library comes with examples demonstrating its usage. You can invoke
the example by running the [annif_client.py](annif_client.py) script.

In your own code, you can use the AnnifClient class like this:

    from annif_client import AnnifClient

    # then you can create your own client
    annif = AnnifClient()

## Example invocation

Here is the output from a typical example session:

    $ python3 annif_client.py
    Demonstrating usage of AnnifClient

    * Creating an AnnifClient object
    Now we have an AnnifClient object: AnnifClient(api_base='http://api.annif.org/v1/')

    * Finding the available projects
    Project id: yso-fi           lang: fi  name: YSO ensemble Finnish
    Project id: yso-sv           lang: sv  name: YSO ensemble Swedish
    Project id: yso-en           lang: en  name: YSO ensemble English
    Project id: tfidf-fi         lang: fi  name: TF-IDF Finnish
    Project id: tfidf-sv         lang: sv  name: TF-IDF Swedish
    Project id: tfidf-en         lang: en  name: TF-IDF English
    Project id: fasttext-fi      lang: fi  name: fastText Finnish
    Project id: fasttext-sv      lang: sv  name: fastText Swedish
    Project id: fasttext-en      lang: en  name: fastText English
    Project id: maui-fi          lang: fi  name: Maui Finnish
    Project id: maui-sv          lang: sv  name: Maui Swedish
    Project id: maui-en          lang: en  name: Maui English
    Project id: annif-api-fi     lang: fi  name: Annif prototype API Finnish
    Project id: annif-api-sv     lang: sv  name: Annif prototype API Swedish
    Project id: annif-api-en     lang: en  name: Annif prototype API English
    Project id: ykl-fasttext-fi  lang: fi  name: YKL fastText Finnish

    * Looking up information about a specific project
    Project id: yso-en           lang: en  name: YSO ensemble English

    * Analyzing a short text from a string
    <http://www.yso.fi/onto/yso/p2228>	0.2595	red fox
    <http://www.yso.fi/onto/yso/p5319>	0.2039	dog
    <http://www.yso.fi/onto/yso/p8122>	0.1946	laziness
    <http://www.yso.fi/onto/yso/p25726>	0.1285	brown
    <http://www.yso.fi/onto/yso/p4760>	0.1220	triple jump
    <http://www.yso.fi/onto/yso/p4758>	0.1194	long jump
    <http://www.yso.fi/onto/yso/p2229>	0.1109	canines
    <http://www.yso.fi/onto/yso/p10636>	0.1094	blue fox
    <http://www.yso.fi/onto/yso/p4759>	0.1068	high jump
    <http://www.yso.fi/onto/yso/p28336>	0.0911	animal training

    * Analyzing a longer text from a file, with a limit on number of results
    <http://www.yso.fi/onto/yso/p16495>	0.3651	licences (permits)
    <http://www.yso.fi/onto/yso/p2346>	0.1656	copyright
    <http://www.yso.fi/onto/yso/p11657>	0.1566	national libraries
    <http://www.yso.fi/onto/yso/p6068>	0.1461	Apache
    <http://www.yso.fi/onto/yso/p14833>	0.1220	copies

## License

The code is published under the [Apache 2.0](LICENSE.txt) license.
