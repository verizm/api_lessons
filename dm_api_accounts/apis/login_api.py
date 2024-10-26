import requests
from dm_api_accounts.models.login_credentials import LoginCredentials
from dm_api_accounts.models.user_envelope import UserEnvelope
from restclient.client import RestClient


class LoginApi(RestClient):

    def post_v1_account_login(self, json_data: LoginCredentials, validate_response: bool = True) -> requests.Response | UserEnvelope:
        """
        Authenticate via credentials.
        :param: json_data LoginCredentials model
        :param: bool validate_response
        :return: requests.Response or UserEnvelope
        """
        response = self.post(path="/v1/account/login", json=json_data.model_dump(exclude_none=True, by_alias=True))
        if validate_response:
            return UserEnvelope(**response.json())
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
