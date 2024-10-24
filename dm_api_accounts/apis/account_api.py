import requests
from restclient.client import RestClient
from models.data_models.registration import Registration
from models.data_models.reset_password import ResetPassword
from models.data_models.change_password import ChangePassword
from models.data_models.change_email import ChangeEmail
from models.response_models.user_envelope import UserEnvelope
from models.response_models.user_details_envelope import UserDetailsEnvelope


class AccountApi(RestClient):

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

    def post_v1_account(self, json_data: Registration) -> requests.Response:
        """
        Register new user.
        :param json_data: user model data
        :return: requests.Response object
        """
        response = self.post(path="/v1/account", json=json_data.model_dump(exclude_none=True, by_alias=True))
        return response

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

    def post_v1_account_password(
            self, json_data: ResetPassword,
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
