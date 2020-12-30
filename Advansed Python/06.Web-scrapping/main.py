import requests
from bs4 import BeautifulSoup


KEYWORDS = ['дизайн', 'фото', 'web', 'python']

ret = requests.get('https://habr.com/ru/all/')
soup = BeautifulSoup(ret.text, 'html.parser')

posts = soup.find_all('article', class_='post')

for post in posts:
    hubs = post.find_all('div', class_='post__text')
    hubs_texts = list(map(lambda hub: hub.text.strip().lower(), hubs))
    for preview in hubs_texts:
        preview_lower = preview.lower()

        if any((desired in preview_lower for desired in KEYWORDS)):
            data = post.find('span', class_='post__time').text
            link = post.find('a', class_='post__title_link')
            link_link = link.attrs.get('href')
            link_text = link.text.strip()
            print(data, link_text, link_link)
            break
