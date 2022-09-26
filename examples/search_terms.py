from smatter.api import APIWrapper
import argparse
import json
import time
import pandas as pd
#rumble_video,rumble_comment,bitchute_video,bitchute_comment,rutube_video,rutube_comment,tiktok_video,tiktok_comment,lbry_video,lbry_comment,
parser = argparse.ArgumentParser()
parser.add_argument('--sites', type=str, default='8kun,4chan,gab,parler,win,poal,telegram,kiwifarms,gettr,wimkin,mewe,minds,vk,truth_social', required=False)
parser.add_argument('--terms', type=str, default='qanon,heil', required=False)
#parser.add_argument('--fileType', type=str, default='json', required=False)
parser.add_argument('--filetype', type=str, default='wide-csv', required=False)

#TODO add range args 
args = parser.parse_args()

#TODO add validation for sites and terms
sites_list = args.sites.split(',')
terms_list = args.terms.split(',')

posts = {}

def setParamsAndQueryAPI(api, site, term):
    api.set_site(site)
    api.set_term(term)
    response = api.query_api()
    #5s is an estimate, TODO figure out the actual limit

    time.sleep(5)
    if(response.status_code == 200):    
        #todo treat this as a stream? this is a bottleneck
        return json.loads(response.text)
    else:
        return {}
    # TODO deal with non 200 codes

def postsToPandas(posts):
    postsDF = pd.DataFrame()
    for site, siteDict in posts.items():
        for term, termDict in siteDict.items():
            for hit in termDict['hits']['hits']:
                hit['_source']['site'] = site
                hit['_source']['term'] = term
                postsDF = pd.concat([postsDF, pd.DataFrame.from_records([hit['_source']])])

    return postsDF

#def ontologizeAndNormalizePosts():
    #define columns to join based on whats present in the dataframe the ...
    #cols = ['foo', 'bar', 'new']
    #df['combined'] = df[cols].apply(lambda row: '_'.join(row.values.astype(str)), axis=1)


if __name__ == '__main__':
    #TODO get rid of one APIWRAPPER
    apiContent = APIWrapper.ApiWrapper('content')
    apiActivity = APIWrapper.ApiWrapper('activity')

    for site in sites_list:
        posts[site] = {}
        for term in terms_list:
            posts[site][term] = {}
            print("Querying SMAT API for",site, "-", term)
            activityResults = setParamsAndQueryAPI(apiActivity, site, term)
            # TODO maybe instead of just warning adjust dates automatically to fit standard size chunks using the timeserries call 
            postLimitForContent = activityResults['hits']['total']['value']
            apiContent.set_limit(postLimitForContent)
            posts[site][term] = setParamsAndQueryAPI(apiContent, site, term)

    if(args.fileType == 'json'):
        with open('result.json', 'w') as fp:
            json.dump(posts, fp)
    elif(args.fileType == 'wide-csv'):
        postsToPandas(posts).to_csv('result.csv', index=False)
    elif(args.fileType == 'norm-csv'):
        wide_csv = postsToPandas(posts)
        print(wide_csv.columns)
