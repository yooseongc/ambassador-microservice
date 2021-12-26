import requests


class UserService:
    endpoint = 'http://users-ms:8000/api/'

    @staticmethod
    def get(path: str, **kwargs):
        headers = kwargs.get('headers', [])
        return requests.get(UserService.endpoint + path, headers=headers).json()
