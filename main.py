import requests


def get_hero_intelligence(name):
    files_url = f'https://superheroapi.com/api/2619421814940190/search/{name}'
    response = requests.get(files_url)
    return response.json()['results'][0]['powerstats']['intelligence']

def best_hero():
    hero_intelligence = {}
    for hero in input().split(', '):
        hero_intelligence[hero] = int(get_hero_intelligence(hero))
    best_intelligence = max(hero_intelligence.values())
    for key, value in hero_intelligence.items():
        if value == best_intelligence:
            return key


if __name__ == '__main__':
    print(get_hero_intelligence('Hulk'))
    print(get_hero_intelligence('Captain America'))
    print(get_hero_intelligence('Thanos'))

    print(best_hero())
# Hulk, Captain America, Thanos

