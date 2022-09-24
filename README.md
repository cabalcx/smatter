# smatter
API wrapper and python client for the SMAT API

##Using it
Currently, smatter is a command line client. It can be run using the default settings following command from the project directory
```
python3 search_terms.py
```

###Arguments
It takes 3 arguments: *sites*, *terms*, and *filetype*
-sites: a list of comma seperated sites, any subset of (rumble_video,rumble_comment,bitchute_video,bitchute_comment,rutube_video,rutube_comment,tiktok_video,tiktok_comment,lbry_video,lbry_comment,8kun,4chan,gab,parler,win,poal,telegram,kiwifarms,gettr,wimkin,mewe,minds,vk,truth_social)
-terms: a list of comma seperated terms to be searched e.g. 'qanon,stopthesteal'
-filetype: determines the output type, currently any single option of wide-csv or json 
