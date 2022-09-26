# smatter
`smatter` is an API wrapper and Python client for the [SMAT API](https://smat-app.com/). 

Per the [SMAT](https://www.smat-app.com/) website:
> The Social Media Analysis Toolkit (SMAT) was designed to help facilitate activists, journalists, researchers, and other social good organizations to analyze and visualize harmful online trends such as hate, mis-, and disinformation online.

## Installing smatter

If you're developing, you may install the package in your local directly like so:
```
pip install -e .
```

## Using smatter in a script
After installing, using `smatter` in your Python program is easy:
```
# import library
from smatter.api import SMAT

# create API client
s = SMAT()

# search the content API for term 'qanon'
results = s.content(term='qanon')

# print the raw API output from SMAT
print(results)
```

There are many parameters for search customization, as well as `pandas` integration.

See the `examples` directory for more scripts and usage demonstrations.

## Using smatter as a CLI [WIP]
The example [`smatter-cli.py`](./examples/smatter-cli.py) is a command line client for this SMAT Python wrapper. It can be run using the default settings following command from the project directory.
```
python3 examples/smatter-cli.py
```
It takes 3 arguments: *sites*, *terms*, and *filetype*
- sites: a list of comma seperated sites, any subset of (rumble_video,rumble_comment,bitchute_video,bitchute_comment,rutube_video,rutube_comment,tiktok_video,tiktok_comment,lbry_video,lbry_comment,8kun,4chan,gab,parler,win,poal,telegram,kiwifarms,gettr,wimkin,mewe,minds,vk,truth_social)
- terms: a list of comma seperated terms to be searched e.g. 'qanon,stopthesteal'
- filetype: determines the output type, currently any single option of wide-csv or json 
