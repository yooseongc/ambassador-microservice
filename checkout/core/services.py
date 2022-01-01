import os
import requests


class UserService:
    endpoint = os.getenv('USERS_MS') + '/api/'

    @staticmethod
    def get(path: str, **kwargs):
        headers = kwargs.get('headers', [])
        return requests.get(UserService.endpoint + path, headers=headers).json()
