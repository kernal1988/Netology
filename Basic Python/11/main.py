import requests
import json

BASE_URL = "https://oauth.vk.com/authorize"
TOKEN = "10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c"

class Vk_Friends:
    def __init__(self, id=None):
        self.id = id

    def friends_list(self):
        response = requests.get(
            "https://api.vk.com/method/friends.get",
            params={
                "access_token": TOKEN,
                "v": 5.21,
                "user_id": self.id,
                "order": "random",
                "scope": "friends",
            }
        )
        data_json = response.json()
        # print(data_json)
        return data_json["response"]["items"]

    def __str__(self):
        url = "https://vk.com/id" + str(self.id)
        return url

    def __and__(self, other):
        user1_friends = self.friends_list()
        user2_friends = other.friends_list()
        mutual_friends = set(user1_friends) & set(user2_friends)
        print(mutual_friends)


user1 = Vk_Friends(id = 993976)
user2 = Vk_Friends(id = 32066666)

print("Задание 1-2:Общие друзья")
friends = user1 & user2

print("Задание 3:Ссылка на профиль")
print("Юзер 1:", user1)
print("Юзер 2:", user2)
