import requests
from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def url_disk(self, disk_file_path: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload/'
        headers = {'Authorization': f'OAuth {token}'}
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def upload(self, disk_file_path, filename):
        url = self.url_disk(disk_file_path=disk_file_path).get('href')
        response = requests.put(url, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Успешно")


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'text.txt'
    disk_file_path = 'task2/text.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(disk_file_path, path_to_file)


