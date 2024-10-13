import json
import random
from http import HTTPStatus
import pytest
import allure
from models.api_models.api_account_models.post_v1_accounts_models import PostV1AccountsRequest
from models.api_models.api_login_models.post_v1_login_models import PostV1LoginRequest


def get_token_by_login(login: str, mails) -> str:
    """
    Get access token by user login.
     """
    for item in mails['items']:
        user_content = json.loads(item['Content']['Body'])
        if user_content["Login"] == login:
            token = user_content["ConfirmationLinkUrl"].split("/")[-1]
            return token
        else:
            raise Exception(f"Access token not found by login {login}")


@pytest.mark.usefixtures("init_api_clients")
class TestPostV1Accounts:

    @allure.title("Check register user")
    def test_post_v1_account(self):
        login = f"vera{random.randrange(1000)}"
        user = PostV1AccountsRequest(login=login, email=f"{login}@mail.ru", password="1234567889")
        login_data = PostV1LoginRequest(login=user.login, password=user.password)

        with allure.step("Register new user"):
            register_response = self.account_api.post_v1_account(user)
            assert register_response == HTTPStatus.CREATED, f"Error status code after reqister user: {register_response}"

        with allure.step("Get user account token from email"):
            mails = self.mailhog_api.get_api_v2_messages()
            token = get_token_by_login(user.login, mails)

        with (allure.step("Authorize under user")):
            authorize_response = self.account_api.put_v1_account_token(token)
            assert authorize_response == HTTPStatus.OK, f"Error status code after authorize user: {authorize_response}"

        with allure.step("Login under user"):
            login_response = self.login_api.post_v1_account_login(login_data)
            assert login_response == HTTPStatus.OK, f"Error status code after login user: {login_response}"
