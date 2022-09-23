import requests

params = {
    'term': 'qanon',
    'interval': 'day',
    'site': 'win',
    'since': '2022-07-23T05:58:30.252063',
    'until': '2022-09-23T05:58:30.252063',
    'changepoint': False,
    'esquery': False,
    'sortdesc': False
}

sites = [
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

base_url = 'https://api.smat-app.com/timeseries'

r = requests.get(base_url, params=params)

print(r.json())