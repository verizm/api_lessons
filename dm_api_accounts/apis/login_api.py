import requests
from models.data_models.login_credentials import LoginCredentials
from restclient.client import RestClient


class LoginApi(RestClient):

    def post_v1_account_login(self, json_data: LoginCredentials) -> requests.Response:
        """
        Authenticate via credentials.
        :param json_data:
        :return: requests.Response
        """
        response = self.post(path="/v1/account/login", json=json_data.model_dump(exclude_none=True, by_alias=True))
        return response

    def delete_v1_account_login(self) -> requests.Response:
        """
        Relogin user via token.
        :return: requests.Response
        """
        response = self.delete(path="/v1/account/login")
        return response

    def delete_v1_account_login_all(self) -> requests.Response:
        """
        Relogin user via token from all devices.
        :return: requests.Response
        """
        response = self.delete(path="/v1/account/login/all")
        return response
