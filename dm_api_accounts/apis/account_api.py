import requests
from restclient.client import RestClient
from models.data_models.registration import Registration
from models.data_models.reset_password import ResetPassword
from models.data_models.change_password import ChangePassword
from models.data_models.change_email import ChangeEmail


class AccountApi(RestClient):

    def get_v1_account(self, **kwargs) -> requests.Response:
        """
        Get current user.
        :return: requests.Response object
        """
        response = self.get(path="/v1/account", **kwargs)
        return response

    def post_v1_account(self, json_data: Registration) -> requests.Response:
        """
        Register new user.
        :param json_data: user model data
        :return: requests.Response object
        """
        response = self.post(path="/v1/account", json=json_data.model_dump(exclude_none=True, by_alias=True))
        return response

    def put_v1_account_token(self, token: str) -> requests.Response:
        """
        Activate reqister user.
        :param token: account token
        :return: requests.Response object
        """
        response = self.put(path=f"/v1/account/{token}")
        return response

    def put_v1_account_email(self, json_data: ChangeEmail) -> requests.Response:
        """
        Change user email.
        :param json_data: user model data
        :return: requests.Response object
        """
        response = self.put(path="/v1/account/email", json=json_data.model_dump(exclude_none=True, by_alias=True))
        return response

    def put_v1_account_password(self, json_data: ChangePassword) -> requests.Response:
        """
        Change user password.
        :param json_data: password change model data
        :return: requests.Response object
        """
        response = self.put(path="/v1/account/password", json=json_data.model_dump(exclude_none=True, by_alias=True))
        return response

    def post_v1_account_password(self, json_data: ResetPassword) -> requests.Response:
        """
        Reset user password.
        :param json_data: password reset model data
        :return: requests.Response object
        """
        response = self.post(path="/v1/account/password", json=json_data.model_dump(exclude_none=True, by_alias=True))
        return response
