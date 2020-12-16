import json
from collections import Counter

def get_json():
    with open("newsafr.json", encoding="utf-8") as f:
        json_data=json.load(f)
    all = []
    new_list = json_data['rss']['channel']['items']

    for item in new_list:
        news = item['description']
        news = news.split()
        # print(news)

        for words in news:
            if len(words.lower()) >= 6:
                all.append(words.lower())

    stat = Counter(all)
    sort_stat = stat.most_common(10)
    print("Наиболее частые слова: ", sort_stat)
get_json()