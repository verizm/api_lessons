import json
import time
import allure
from typing import Callable
from requests import Response
from http import HTTPStatus
from logger import log
from services.mailhog_api import MailhogApiFacade
from services.dm_api_account import DmApiAccountFacade
from models.api_models.api_account_models.post_v1_accounts_models import PostV1AccountsRequest
from models.api_models.api_login_models.post_v1_login_models import PostV1LoginRequest
from models.api_models.api_account_models.put_v1_account_password_models import PutV1AccountsPasswordRequest
from models.api_models.api_account_models.post_v1_account_password import PostV1AccountsPasswordRequest


def token_retrier(function: Callable):
    def wrapper(*args, **kwargs) -> str:
        token = None
        count = 0
        while token is None:
            log.msg(f"Try to get token count: {count}")
            token = function(*args, **kwargs)
            count += 1

            if count == 5:
                raise AssertionError("Count retries more when 5")
            if token:
                return token
        time.sleep(1)

    return wrapper


class AccountHelper:
    AUTH_HEADER = "x-dm-auth-token"

    def __init__(self, dm_account_api: DmApiAccountFacade, mailhog: MailhogApiFacade):
        self.dm_account_api = dm_account_api
        self.mailhog = mailhog

    @token_retrier
    def get_activation_token_by_login(self, login: str) -> str:
        """
        Get access token by user login.
        """
        mails = self.mailhog.mailhog_api.get_api_v2_messages().json()
        for item in mails['items']:
            user_content = json.loads(item['Content']['Body'])
            if user_content["Login"] == login:
                token = user_content["ConfirmationLinkUrl"].split("/")[-1]
                return token

    @token_retrier
    def get_reset_password_token(self, login: str) -> str:
        """
        Get reset password by user login.
        """
        mails = self.mailhog.mailhog_api.get_api_v2_messages().json()
        for item in mails['items']:
            user_content = json.loads(item['Content']['Body'])
            link = user_content["ConfirmationLinkUri"].split("/")
            if user_content["Login"] == login and "password" in link:  # todo create sorting by time
                token = link[-1]
                return token

    def auth_client(self, user: PostV1AccountsRequest) -> Response:
        """
        Auth user in services.
        :param user: PostV1AccountsRequest data
        :return:  None
        """
        with allure.step("Create user session"):
            response = self.login_user(PostV1LoginRequest(login=user.login, password=user.password))
            token = {self.AUTH_HEADER: response.headers[self.AUTH_HEADER]}
            self.dm_account_api.account_api.set_headers(token)
            self.dm_account_api.login_api.set_headers(token)
            return response

    def change_password(self, user: PostV1AccountsRequest, new_password: str) -> Response:
        """
        Change password for authorized user.
        :param user: PostV1AccountsRequest data
        :param new_password: new user password str
        :return:  Response
        """
        self.auth_client(user)
        self.dm_account_api.account_api.post_v1_account_password(PostV1AccountsPasswordRequest(login=user.login, email=user.email))
        token = self.get_reset_password_token(user.login)
        data = PutV1AccountsPasswordRequest(login=user.login, token=token, old_password=user.password, new_password=new_password)
        response = self.dm_account_api.account_api.put_v1_account_password(data)
        return response

    def register_new_user(self, user: PostV1AccountsRequest) -> Response:
        with allure.step("Register new user"):
            register_response = self.dm_account_api.account_api.post_v1_account(user)
            status_code = register_response.status_code
            assert status_code == HTTPStatus.CREATED, f"Error status code after reqister user: {status_code}"

        with allure.step("Get user account token from email"):
            token = self.get_activation_token_by_login(user.login)

        with allure.step("Authorize under user"):
            authorize_response = self.dm_account_api.account_api.put_v1_account_token(token)
            status_code = authorize_response.status_code
            assert status_code == HTTPStatus.OK, f"Error status code after authorize user: {status_code}"
        return authorize_response

    def login_user(self, user: PostV1LoginRequest) -> Response:
        login_response = self.dm_account_api.login_api.post_v1_account_login(user)
        status_code = login_response.status_code
        assert status_code == HTTPStatus.OK, f"Error status code after login user: {status_code}"
        return login_response
