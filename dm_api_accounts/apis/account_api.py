import requests
from models.api_models.api_account_models.post_v1_accounts_models import PostV1AccountsRequest


class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers

    def post_v1_account(self, json_data: PostV1AccountsRequest) -> requests.Response:
        """
        Register new user.
        :param json_data: user model data
        :return: status code
        """
        response = requests.post(url=f"{self.host}/v1/account", json=json_data.model_dump())
        return response

    def put_v1_account_token(self, token: str) -> requests.Response:
        """
        Activate reqister user.
        :param token: account token
        :return: status code
        """
        response = requests.put(url=f"{self.host}/v1/account/{token}")
        return response

    def put_v1_account_email(self, json_data: PostV1AccountsRequest) -> requests.Response:
        """
        Change user email.
        :param json_data: user model data
        :return: status code
        """
        response = requests.put(url=f"{self.host}/v1/account/email", json=json_data.model_dump())
        return response
