from smatter.utils import *

#TODO Add each path (currently content, timeseries, activity) as a child class, something like
# class contentPathApiWrapper(ApiWrapper):
#     def __init__(self,
#                 path):
#         super().__init__(path)

class SMAT:
    
    def __init__(self, SMAT_API_KEY: str = None):
        # set class version
        #self.VERSION = self.__version__()

        # set class base url
        self.BASE_URL = SMAT_API_BASE_URL

        # set in-scope sites
        self.SMAT_SITES = SMAT_TARGET_SITES

        # set api endpoints
        self.ENDPOINT_CONTENT = SMAT_API_ENDPOINT_CONTENT
        self.ENDPOINT_TIMESERIES = SMAT_API_ENDPOINT_TIMESERIES
        self.ENDPOINT_ACTIVITY = SMAT_API_ENDPOINT_ACTIVITY

        #set target URLs
        self.SMAT_CONTENT_TARGET_URL = f'{self.BASE_URL}{self.ENDPOINT_CONTENT}'
        self.SMAT_TIMESERIES_TARGET_URL = f'{self.BASE_URL}{self.ENDPOINT_TIMESERIES}'
        self.SMAT_ACTIVITY_TARGET_URL = f'{self.BASE_URL}{self.ENDPOINT_ACTIVITY}'

        # if passed, set API key (not needed)
        if SMAT_API_KEY:
            self.API_KEY = SMAT_API_KEY
        else:
            self.API_KEY = None

    def __str__(self) -> str:
        returnData = {
            'name': 'SMAT',
            'base_url': self.BASE_URL,
            'api_key' : self.API_KEY
        }
        returnData = vars(self)
        return json.dumps(returnData,indent=4)

    def content(
            self,
            term: str = 'qanon',
            limit: int = 10,
            site: str = ['win','gab','parler'],
            since: str = '2021-01-01T00:00:00.000000',
            until: str = '2022-01-01T00:00:00.000000',
            esquery: bool = False,
            sortdesc: bool = False
        ):
        """
        SMAT Content: Get the post content for a given query on a given site.
        Parameters:
        term: the search keyword or keywords. Default = "qanon".
        limit: Maximum records to return. Default = 10.
        site: the site or sites in scope for the query. See list of valid sites. Default = ['win','gab','parler']
        since: Datetime starting point for the query. Default = "2021-01-01T00:00:00.000000"
        until: Datetime ending point for the query. Default = "2022-01-01T00:00:00.000000"
        esquery: Default = False. ??? TODO
        sortdesc: Order to present results, oldest->newest or newest->oldest. Default = False.
        """
        params = {
            'term': term,
            'limit': limit,
            'site': site,
            'since': since,
            'until': until,
            'esquery': esquery,
            'sortdesc': sortdesc
        }
        response = makeRequestToSMAT(
            target_url=self.SMAT_CONTENT_TARGET_URL,
            params=params
        )
        return response.json()

    def timeseries(
            self,
            term: str = 'qanon',
            interval: str = 'day',
            site: str = ['win','gab','parler'],
            since: str = '2021-01-01T00:00:00.000000',
            until: str = '2022-01-01T00:00:00.000000',
            changepoint: bool = False,
            esquery: bool = False,
            sortdesc: bool = False
        ):
        """
        SMAT Timeseries: Simple volume aggregation over time for a given query on a given site.
        Parameters:
        term: the search keyword or keywords. Default = "qanon".
        interval: the time interval to group the timeseries, such as "second", "minute", "hour", "day", "week". Default = "day".
        site: the site or sites in scope for the query. See list of valid sites. Default = ['win','gab','parler']
        since: Datetime starting point for the query. Default = "2021-01-01T00:00:00.000000"
        until: Datetime ending point for the query. Default = "2022-01-01T00:00:00.000000"
        changepoint: Default = False. ??? TODO 
        esquery: Default = False. ??? TODO
        sortdesc: Order to present results, oldest->newest or newest->oldest. Default = False.
        """
        params = {
            'term': term,
            'interval': interval,
            'site': site,
            'since': since,
            'until': until,
            'changepoint': changepoint,
            'esquery': esquery,
            'sortdesc': sortdesc
        }
        response = makeRequestToSMAT(
            target_url=self.SMAT_TIMESERIES_TARGET_URL,
            params=params
        )
        return response.json()

    def activity(
            self,
            term: str = 'qanon',
            aggby: str = 'community',
            site: str = ['win','gab','parler'],
            since: str = '2021-01-01T00:00:00.000000',
            until: str = '2022-01-01T00:00:00.000000',
            changepoint: bool = False,
            esquery: bool = False
        ):
        """
        SMAT ACTIVITY: Get the user activity for a given query on a given site.
        Parameters:
        term: the search keyword or keywords. Default = "qanon".
        limit: Maximum records to return. Default = 10.
        site: the site or sites in scope for the query. See list of valid sites. Default = ['win','gab','parler']
        since: Datetime starting point for the query. Default = "2021-01-01T00:00:00.000000"
        until: Datetime ending point for the query. Default = "2022-01-01T00:00:00.000000"
        changepoint: Default = False. ??? TODO 
        esquery: Default = False. ??? TODO
        """
        params = {
            'term': term,
            'aggby': aggby,
            'site': site,
            'since': since,
            'until': until,
            'changepoint': changepoint,
            'esquery': esquery
        }
        response = makeRequestToSMAT(
            target_url=self.SMAT_ACTIVITY_TARGET_URL,
            params=params
        )
        return response.json()
    
    

    #TODO Add validation logic
    def set_path(self, path):
        #TODO Alert that this resets params
        self.path = path

        #Maybe shouldn't have defaults?
        #todo change to switch once I bother to update to python 3.10
        if path == 'content':
                #TODO dynamic default dates
                self.params = {
                    'term': 'qanon',
                    'limit': 100,
                    'site': 'win',
                    'since': '2022-07-23T05:58:30.252063',
                    'until': '2022-09-23T05:58:30.252063',
                    'esquery': 'false',
                    'sortdesc': 'true'
                }
        elif(path == 'activity'):
                #TODO dynamic default dates
                self.params = {
                    'term': 'qanon',
                    'site': 'win',
                    'since': '2022-07-23T05:58:30.252063',
                    'until': '2022-09-23T05:58:30.252063',
                    'esquery': 'false',
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


    def set_limit(self, limit):
        if self.path == 'content':
            #todo a better limit? this one is arbitray
            if(limit <= 1000):
                self.params['limit'] = limit
            else:
                self.params['limit'] = 1000
                print("WARNING - Limit maxes at 1000, falling please narrow your search window or youtre results will be truncated")
        else:
            raise ValueError("limit is only valid for content")


    def get_valid_sites(self):
        return validSites
        
    def query_api(self):
        return requests.get(self.domain + self.path, params=self.params)

#test
#api = ApiWrapper('content')
#print(api.query_endpoint().status_code)