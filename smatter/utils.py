import json
import requests

######################################################
# CONSTANTS
######################################################
# integration specifics
INTEGRATION_NAME = 'smatter - SMAT Python wrapper'
INTEGRATION_VERSION = '0.1.0'
INTEGRATION_URL = 'https://github.com/cabalcx/smatter'
# domain for SMAT API
SMAT_API_HOSTNAME = 'api.smat-app.com'
# base url derived from hostname
SMAT_API_BASE_URL = f'https://{SMAT_API_HOSTNAME}/'
# SMAT API ENDPOINTS
SMAT_API_ENDPOINT_CONTENT = 'content/'
SMAT_API_ENDPOINT_TIMESERIES = 'timeseries/'
SMAT_API_ENDPOINT_ACTIVITY = 'activity/'


SMAT_TARGET_SITES = [
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

######################################################
# FUNCTIONS
######################################################
def makeRequestToSMAT(method: str = 'GET', target_url: str = 'SMAT_API_BASE_URL', params: dict = None, SMAT_API_KEY: str = None):
    if not SMAT_API_KEY:
        headers = {
            'user-agent': f'{INTEGRATION_NAME} v{INTEGRATION_VERSION} - {INTEGRATION_URL}'
        }
        return requests.request(method, url=target_url, params=params)
    else:
        return