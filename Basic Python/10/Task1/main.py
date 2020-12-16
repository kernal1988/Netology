import requests

heroes_list = ['Hulk', 'Captain America', 'Thanos']

def get_data(heroes_list):
    heroes_dict = dict.fromkeys(heroes_list)
    # print(heroes_dict)
    for hero in heroes_list:
        url = (f'https://www.superheroapi.com/api.php/2619421814940190/search/{hero}')
        heroes_dict[hero] = int(requests.get(url).json()['results'][0]['powerstats']['intelligence'])
    # print(heroes_dict)
    intelligence = 0
    max_intelligence = 0
    for hero in heroes_dict:
        if intelligence < heroes_dict[hero]:
            intelligence = heroes_dict[hero]
            max_intelligence = hero

    print(f'Герой с максимальным уровнем интеллекта {intelligence} - {max_intelligence}')

get_data(heroes_list)