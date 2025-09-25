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
    * The client uses Annif API at https://api.annif.org/v1/
    * The version of Annif serving the API is 1.4.0

    * Detecting the language of text: 'The quick brown fox jumped over the lazy dog' (candidates: en, fi, sv)
    Language: en    score: 1.0
    Language: sv    score: 0.25
    Language: fi    score: 0.0
    Language: None  score: 0.0

    * Finding the available projects
    Project id: yso-fi           lang: fi  name: YSO NN ensemble Finnish
    Project id: yso-sv           lang: sv  name: YSO NN ensemble Swedish
    Project id: yso-en           lang: en  name: YSO NN ensemble English
    Project id: yso-mllm-fi      lang: fi  name: YSO MLLM Finnish
    Project id: yso-mllm-en      lang: en  name: YSO MLLM English
    Project id: yso-mllm-sv      lang: sv  name: YSO MLLM Swedish
    Project id: yso-bonsai-fi    lang: fi  name: YSO Omikuji Bonsai Finnish
    Project id: yso-bonsai-sv    lang: sv  name: YSO Omikuji Bonsai Swedish
    Project id: yso-bonsai-en    lang: en  name: YSO Omikuji Bonsai English
    Project id: yso-fasttext-fi  lang: fi  name: YSO fastText Finnish
    Project id: yso-fasttext-sv  lang: sv  name: YSO fastText Swedish
    Project id: yso-fasttext-en  lang: en  name: YSO fastText English

    * Looking up information about a specific project
    Project id: yso-en           lang: en  name: YSO NN ensemble English

    * Analyzing a short text from a string
    <http://www.yso.fi/onto/yso/p5319>	0.2852	dog
    <http://www.yso.fi/onto/yso/p8122>	0.1401	laziness
    <http://www.yso.fi/onto/yso/p2228>	0.1052	red fox
    <http://www.yso.fi/onto/yso/p2352>	0.0914	singers
    <http://www.yso.fi/onto/yso/p675>	0.0679	pets
    <http://www.yso.fi/onto/yso/p27825>	0.0651	jumping
    <http://www.yso.fi/onto/yso/p25726>	0.0631	brown
    <http://www.yso.fi/onto/yso/p2023>	0.0584	animals
    <http://www.yso.fi/onto/yso/p4484>	0.0453	jazz
    <http://www.yso.fi/onto/yso/p22993>	0.0357	clicker training

    * Analyzing a longer text from a file, with a limit on number of results
    <http://www.yso.fi/onto/yso/p2346>	0.6324	copyright
    <http://www.yso.fi/onto/yso/p16495>	0.4211	licences (permits)
    <http://www.yso.fi/onto/yso/p26592>	0.1882	computer programmes
    <http://www.yso.fi/onto/yso/p3069>	0.1434	patents
    <http://www.yso.fi/onto/yso/p3068>	0.1044	intellectual property law

    * Analyzing a batch of text documents
    doc-0
    <http://www.yso.fi/onto/yso/p5319>	0.2852	dog
    <http://www.yso.fi/onto/yso/p8122>	0.1401	laziness
    <http://www.yso.fi/onto/yso/p2228>	0.1052	red fox
    <http://www.yso.fi/onto/yso/p2352>	0.0914	singers
    <http://www.yso.fi/onto/yso/p675>	0.0679	pets
    <http://www.yso.fi/onto/yso/p27825>	0.0651	jumping
    <http://www.yso.fi/onto/yso/p25726>	0.0631	brown
    <http://www.yso.fi/onto/yso/p2023>	0.0584	animals
    <http://www.yso.fi/onto/yso/p4484>	0.0453	jazz
    <http://www.yso.fi/onto/yso/p22993>	0.0357	clicker training
    doc-1
    <http://www.yso.fi/onto/yso/p1780>	0.7189	history
    <http://www.yso.fi/onto/yso/p2787>	0.7167	libraries
    <http://www.yso.fi/onto/yso/p11657>	0.6425	national libraries
    <http://www.yso.fi/onto/yso/p94426>	0.3903	Finland
    <http://www.yso.fi/onto/yso/p12676>	0.3430	collections
    <http://www.yso.fi/onto/yso/p8025>	0.2621	architecture
    <http://www.yso.fi/onto/yso/p4860>	0.2586	library buildings
    <http://www.yso.fi/onto/yso/p19136>	0.2577	scientific libraries
    <http://www.yso.fi/onto/yso/p1778>	0.2208	histories (literary works)
    <http://www.yso.fi/onto/yso/p10184>	0.2120	university libraries
    doc-2
    <http://www.yso.fi/onto/yso/p4934>	0.5751	museums
    <http://www.yso.fi/onto/yso/p2787>	0.5510	libraries
    <http://www.yso.fi/onto/yso/p2336>	0.4488	archives (memory organisations)
    <http://www.yso.fi/onto/yso/p26984>	0.4123	subject indexing
    <http://www.yso.fi/onto/yso/p11477>	0.2768	automation
    <http://www.yso.fi/onto/yso/p13380>	0.2394	subject cataloging
    <http://www.yso.fi/onto/yso/p39257>	0.1884	indexing (information technology)
    <http://www.yso.fi/onto/yso/p1140>	0.0799	data storage
    <http://www.yso.fi/onto/yso/p5521>	0.0771	information management
    <http://www.yso.fi/onto/yso/p21192>	0.0749	long-term preservation

## License

The code is published under the [Apache 2.0](LICENSE.txt) license.
