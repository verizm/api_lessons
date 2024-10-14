import json
import random
from http import HTTPStatus
import pytest
import allure
from models.api_models.api_account_models.post_v1_accounts_models import PostV1AccountsRequest


def get_token_by_login(login: str, mails: dict) -> str:
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

        with allure.step("Register new user"):
            register_response = self.account_api.post_v1_account(user)
            status_code = register_response.status_code
            assert status_code == HTTPStatus.CREATED, f"Error status code after reqister user: {status_code}"
