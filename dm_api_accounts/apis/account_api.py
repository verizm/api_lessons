import requests
from restclient.client import RestClient
from models.api_models.api_account_models.post_v1_accounts_models import PostV1AccountsRequest
from models.api_models.api_account_models.put_v1_account_password_models import PutV1AccountsPasswordRequest


class AccountApi(RestClient):

    def get_v1_account(self, **kwargs) -> requests.Response:
        """
        Get current user.
        :return: requests.Response object
        """
        response = self.get(path="/v1/account", **kwargs)
        return response

    def post_v1_account(self, json_data: PostV1AccountsRequest) -> requests.Response:
        """
        Register new user.
        :param json_data: user model data
        :return: requests.Response object
        """
        response = self.post(path="/v1/account", json=json_data.model_dump())
        return response

    def put_v1_account_token(self, token: str) -> requests.Response:
        """
        Activate reqister user.
        :param token: account token
        :return: requests.Response object
        """
        response = self.put(path=f"/v1/account/{token}")
        return response

    def put_v1_account_email(self, json_data: PostV1AccountsRequest) -> requests.Response:
        """
        Change user email.
        :param json_data: user model data
        :return: requests.Response object
        """
        response = self.put(path="/v1/account/email", json=json_data.model_dump())
        return response

    def put_v1_account_password(self, json_data: PutV1AccountsPasswordRequest) -> requests.Response:
        """
        Change user password.
        :param json_data: password change model data
        :return: requests.Response object
        """
        response = self.put(path="/v1/account/password", json=json_data.model_dump(by_alias=True))
        return response

    def post_v1_account_password(self, json_data) -> requests.Response:
        """
        Reset user password.
        :param json_data: password reset model data
        :return: requests.Response object
        """
        response = self.post(path="/v1/account/password", json=json_data.model_dump())
        return response

