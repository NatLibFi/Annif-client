# Annif-client

This is a minimal Python 3.x client library for accessing the Annif REST API
which can be used for automated subject indexing and classification of text
documents.

## Dependencies

The library depends on the
[requests](http://docs.python-requests.org/en/master/#) module which is used
for HTTP/REST access. The easiest way to install requests is via pip:

    pip install requests

or in some cases (e.g. Ubuntu systems with both Python 2 and 3):

    pip3 install requests

## How to use

The client library comes with examples demonstrating its usage. You can invoke
the example simply by running the [annif_client.py](annif_client.py) script.

In your own code, you can import the AnnifClient class like this:

    from annif_client import AnnifClient

    # then you can create your own client
    annif = AnnifClient()

## Example invocation

Here is the output from a typical examploe session:

    $ python3 annif_client.py
    Demonstrating usage of AnnifClient

    * Creating an AnnifClient object
    Now we have an AnnifClient object: AnnifClient(api_base='http://dev.annif.org/v1/')

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
    <http://www.yso.fi/onto/yso/p11910>	0.2918	related rights
    <http://www.yso.fi/onto/yso/p152>	0.1810	rights
    <http://www.yso.fi/onto/yso/p1810>	0.1621	work
    <http://www.yso.fi/onto/yso/p2346>	0.1589	copyright
    <http://www.yso.fi/onto/yso/p15650>	0.1526	Works

## License

The code is published under the [CC0](LICENSE) license. You can do whatever
you want with it.
