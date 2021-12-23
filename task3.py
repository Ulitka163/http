import requests


def quest(tag):
    url = f'https://api.stackexchange.com/2.3/questions'
    params = {'tagged': f'{tag}', 'fromdate': '1640044800', 'site': 'stackoverflow'}
    response = requests.get(url=url, params=params)
    for i in response.json().get('items'):
        print(i.get('title'))
    return


quest('python')
