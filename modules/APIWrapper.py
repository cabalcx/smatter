import requests

validSites = [
    'rumble_video',
    'rumble_comment',
    'bitchute_video',
    'bitchute_comment',
    'rutube_video',
    'rutube_comment',
    'tiktok_video',
    'tiktok_comment',
    'lbry_video',
    'lbry_comment',
    '8kun',
    '4chan',
    'gab',
    'parler',
    'win',
    'poal',
    'telegram',
    'kiwifarms',
    'gettr',
    'wimkin',
    'mewe',
    'minds',
    'vk',
    'truth_social'
]

#TODO Add each path (currently content, timeseries, activity) as a child class, something like
# class contentPathApiWrapper(ApiWrapper):
#     def __init__(self,
#                 path):
#         super().__init__(path)

class ApiWrapper:
    def __init__(self, path):
        #Should always be smat but might as well let people change it
        self.domain = 'https://api.smat-app.com/' 
        #TODO Throw error if invalid path enum (content, timeseries, activity) 
        self.path = path
        #Maybe shouldn't have defaults?
        #todo change to switch once I bother to update to python 3.10
        if path == 'content':
                #TODO dynamic default dates
                self.params = {
                    'term': 'qanon',
                    'limit': 10,
                    'site': 'win',
                    'since': '2022-07-23T05:58:30.252063',
                    'until': '2022-09-23T05:58:30.252063',
                    'esquery': 'false',
                    'sortdesc': 'true'
                }
            #case _:
                #throw an error?

    #TODO Add validation logic
    def set_path(self, path):
        #TODO Alert that this resets params
        self.path = path
        #todo change to switch once I bother to update to python 3.10
        if path == 'content':
                #TODO dynamic default dates
                self.params = {
                    'term': 'qanon',
                    'limit': 10,
                    'site': 'win',
                    'since': '2022-07-23T05:58:30.252063',
                    'until': '2022-09-23T05:58:30.252063',
                    'esquery': 'false',
                    'sortdesc': 'true'
                }
        
    def set_site(self, site):
        if site not in validSites:
            raise ValueError("Site must be one of %r." % validSites)
        else:
            self.params['site'] = site

    def set_term(self, term):
        if len(term) > 0:
            self.params['term'] = term
        else:
            raise ValueError("Empty strings may not be searched")

    def get_valid_sites(self):
        return validSites
        
    def query_api(self):
        return requests.get(self.domain + self.path, params=self.params)

#test
#api = ApiWrapper('content')
#print(api.query_endpoint().status_code)