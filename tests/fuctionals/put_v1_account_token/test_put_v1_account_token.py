import json
import random
import allure
import pytest
from http import HTTPStatus
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
class TestPutV1AccountToken:

    @allure.title("Put access token")
    def test_put_v1_account_token(self):
        login = f"vera{random.randrange(1000)}"
        user = PostV1AccountsRequest(login=login, email=f"{login}@mail.ru", password="1234567889")

        with allure.step("Register new user"):
            self.account_api.post_v1_account(user)

        with allure.step("Get user account token from email"):
            mails = self.mailhog_api.get_api_v2_messages()
            token = get_token_by_login(user.login, mails.json())

        with allure.step("Authorize user with new email"):
            authorize_response = self.account_api.put_v1_account_token(token)
            status_code = authorize_response.status_code
            assert status_code == HTTPStatus.OK, f"Error status code after authorize user: {status_code}"
