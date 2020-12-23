import os
import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""
        files = os.path.basename(self.token)
        with open(self.token, 'r') as f:
            file = f.read()
        header = {'Authorization': 'OAuth ' + file_path}
        response = requests.get(f'https://cloud-api.yandex.net:443/v1/disk/resources/upload?path={files}',headers=header)
        url = response.json()['href']
        print(url)
        requests.put(url, data=file)
        return f'Файл {files} загружен.'


if __name__ == '__main__':
    uploader = YaUploader('C:/1/test.txt')
    result = uploader.upload('XXX')
    print(result)










