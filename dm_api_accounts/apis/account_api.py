import requests
import json
from models.api_models.api_account_models.post_v1_accounts_models import PostV1AccountsRequest


class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers

    def post_v1_account(self, json_data: PostV1AccountsRequest) -> int:
        """
        Register new user.
        :param json_data: user model data
        :return: status code
        """
        response = requests.post(url=f"{self.host}/v1/account", json=json_data.model_dump())
        return response.status_code

    def put_v1_account_token(self, token: str) -> int:
        """
        Activate reqister user.
        :param token: account token
        :return: status code
        """
        response = requests.put(url=f"{self.host}/v1/account/{token}")
        return response.status_code
