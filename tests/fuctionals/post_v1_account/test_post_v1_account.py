import json
import random
from http import HTTPStatus
import pytest
import allure
from models.api_models.api_account_models.post_v1_accounts_models import PostV1AccountsRequest


@pytest.mark.usefixtures("init_api_clients")
class TestPostV1Accounts:

    @allure.title("Check register user")
    def test_post_v1_account(self):
        login = f"vera{random.randrange(1000)}"
        user = PostV1AccountsRequest(login=login, email=f"{login}@mail.ru",
            password="1234567889")  #  # with allure.step("Register new user"):  #  #  #     assert status_code == HTTPStatus.CREATED, f"Error status code after reqister user: {status_code}"
