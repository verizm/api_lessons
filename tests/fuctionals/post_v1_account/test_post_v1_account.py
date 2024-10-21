import random
from http import HTTPStatus

import allure
from models.api_models.api_account_models.post_v1_accounts_models import PostV1AccountsRequest


class TestPostV1Accounts:

    @allure.title("Check register user")
    def test_post_v1_account(self, account_helper):
        login = f"vera{random.randrange(1000)}"
        user = PostV1AccountsRequest(login=login, email=f"{login}@mail.ru", password="1234567889")
        response = account_helper.dm_account_api.account_api.post_v1_account(user)
        with allure.step("Register new user"):
            assert response.status_code == HTTPStatus.CREATED, f"Error status code after reqister user: {response.status_code}"
