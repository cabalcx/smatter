from modules import APIWrapper
import argparse
import json
import time
import pandas as pd
#rumble_video,rumble_comment,bitchute_video,bitchute_comment,rutube_video,rutube_comment,tiktok_video,tiktok_comment,lbry_video,lbry_comment,
parser = argparse.ArgumentParser()
parser.add_argument('--sites', type=str, default='8kun,4chan,gab,parler,win,poal,telegram,kiwifarms,gettr,wimkin,mewe,minds,vk,truth_social', required=False)
parser.add_argument('--terms', type=str, default='qanon', required=False)
#parser.add_argument('--fileType', type=str, default='json', required=False)
parser.add_argument('--fileType', type=str, default='wide-csv', required=False)
#TODO add range args 
args = parser.parse_args()

#TODO add validation for sites and terms
sites_list = args.sites.split(',')
terms_list = args.terms.split(',')

posts = {}

def postsToPandas(posts):
    postsDF = pd.DataFrame(columns=['Site', 'Term'])
    for site, siteDict in posts.items():
        for term, termDict in siteDict.items():
            for hit in termDict['hits']['hits']:
                hit['_source']['site'] = site
                hit['_source']['site'] = term
                postsDF = postsDF.append(hit['_source'], ignore_index = True)

    return postsDF
        

if __name__ == '__main__':
    #TODO get rid of one APIWRAPPER
    api = APIWrapper.ApiWrapper('content')
    for site in sites_list:
        posts[site] = {}
        for term in terms_list:
            posts[site][term] = {}
            print("Querying SMAT API for",site, "-", term)
            api.set_site(site)
            api.set_term(term)
            response = api.query_api()
            if(response.status_code == 200):                
                posts[site][term] = json.loads(response.text)
            #5s is an estimate, TODO figure out the actual limit
            time.sleep(5)

    if(args.fileType == 'json'):
        with open('result.json', 'w') as fp:
            json.dump(posts, fp)
    elif(args.fileType == 'wide-csv'):
        postsToPandas(posts).to_csv('result.csv', index=False)
