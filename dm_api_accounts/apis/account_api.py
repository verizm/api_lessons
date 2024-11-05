import allure
import requests
from restclient.client import RestClient
from dm_api_accounts.models.registration import Registration
from dm_api_accounts.models.reset_password import ResetPassword
from dm_api_accounts.models.change_password import ChangePassword
from dm_api_accounts.models.change_email import ChangeEmail
from dm_api_accounts.models.user_envelope import UserEnvelope
from dm_api_accounts.models.user_details_envelope import UserDetailsEnvelope


class AccountApi(RestClient):

    @allure.step("Get user account data")
    def get_v1_account(self, validate_response: bool = True, **kwargs) -> requests.Response | UserDetailsEnvelope:
        """
        Get current user.
        :param  validate_response: bool
        :return: requests.Response object or UserDetailsEnvelope
        """
        response = self.get(path="/v1/account", **kwargs)
        if validate_response:
            return UserDetailsEnvelope(**response.json())
        return response

    @allure.step("Register user")
    def post_v1_account(self, json_data: Registration) -> requests.Response:
        """
        Register new user.
        :param json_data: user model data
        :return: requests.Response object
        """
        response = self.post(path="/v1/account", json=json_data.model_dump(exclude_none=True, by_alias=True))
        return response

    @allure.step("Activate user by token from email")
    def put_v1_account_token(self, token: str, validate_response: bool = True) -> requests.Response | UserEnvelope:
        """
        Activate reqister user.
        :param token: account token
        :param  validate_response: bool
        :return: requests.Response object
        """
        response = self.put(path=f"/v1/account/{token}")
        if validate_response:
            return UserEnvelope(**response.json())
        return response

    @allure.step("Change user email")
    def put_v1_account_email(self, json_data: ChangeEmail, validate_response: bool = True) -> requests.Response | UserEnvelope:
        """
        Change user email.
        :param json_data: user model data
        :param  validate_response: bool
        :return: requests.Response object
        """
        response = self.put(path="/v1/account/email", json=json_data.model_dump(exclude_none=True, by_alias=True))
        if validate_response:
            return UserEnvelope(**response.json())
        return response

    @allure.step("Set new password")
    def put_v1_account_password(self, json_data: ChangePassword, validate_response: bool = True) -> requests.Response | UserEnvelope:
        """
        Change user password.
        :param json_data: password change model data
        :param  validate_response: bool
        :return: requests.Response object
        """
        response = self.put(path="/v1/account/password", json=json_data.model_dump(exclude_none=True, by_alias=True))
        if validate_response:
            return UserEnvelope(**response.json())
        return response

    @allure.step("Reset user password")
    def post_v1_account_password(
            self,
            json_data: ResetPassword,
            validate_response: bool = True,
    ) -> requests.Response | UserEnvelope:
        """
        Reset user password.
        :param json_data: password reset model data
        :param validate_response: bool
        :return: requests.Response object
        """
        response = self.post(path="/v1/account/password", json=json_data.model_dump(exclude_none=True, by_alias=True))
        if validate_response:
            return UserEnvelope(**response.json())
        return response
