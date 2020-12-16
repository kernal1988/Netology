import json

class Iterator:
    def __init__(self,data):
        self.data = data.__iter__()

    def __iter__(self):
        return self

    def __next__(self):
        dict = {}
        item = self.data.__next__()
        item = item['name']['common']
        dict[item] = 'https://ru.wikipedia.org/wiki/' + item
        return dict

with open('countries.json', encoding = 'utf-8') as f:
    data = json.load(f)

country_list = []
with open('country.txt', 'w', encoding='utf-8') as f:
    for country in Iterator(data):
        country_list.append(country)
    json.dump(country_list, f, indent=8)
