import requests


class UserService:
    endpoint = 'http://users-ms:8000/api/'

    @staticmethod
    def get(path: str, **kwargs):
        headers = kwargs.get('headers', [])
        return requests.get(UserService.endpoint + path, headers=headers).json()

    @staticmethod
    def post(path: str, **kwargs):
        headers = kwargs.get('headers', [])
        data = kwargs.get('data', [])
        return requests.post(UserService.endpoint + path, headers=headers, data=data).json()

    @staticmethod
    def put(path: str, **kwargs):
        headers = kwargs.get('headers', [])
        data = kwargs.get('data', [])
        return requests.put(UserService.endpoint + path, headers=headers, data=data).json()
