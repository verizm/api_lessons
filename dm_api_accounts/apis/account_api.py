import requests
from restclient.client import RestClient
from models.api_models.api_account_models.post_v1_accounts_models import PostV1AccountsRequest


class AccountApi(RestClient):

    def post_v1_account(self, json_data: PostV1AccountsRequest) -> requests.Response:
        """
        Register new user.
        :param json_data: user model data
        :return: status code
        """
        response = self.post(path="/v1/account", json=json_data.model_dump())
        return response

    def put_v1_account_token(self, token: str) -> requests.Response:
        """
        Activate reqister user.
        :param token: account token
        :return: status code
        """
        response = self.put(path=f"/v1/account/{token}")
        return response

    def put_v1_account_email(self, json_data: PostV1AccountsRequest) -> requests.Response:
        """
        Change user email.
        :param json_data: user model data
        :return: status code
        """
        response = self.put(path="/v1/account/email", json=json_data.model_dump())
        return response
