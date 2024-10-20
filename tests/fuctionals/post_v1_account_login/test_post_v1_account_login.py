import json
import random
from http import HTTPStatus
import pytest
import allure
from models.api_models.api_account_models.post_v1_accounts_models import PostV1AccountsRequest
from models.api_models.api_login_models.post_v1_login_models import PostV1LoginRequest


class TestPostV1AccountLogin:

    @allure.title("Check register user")
    def test_post_v1_account_login(self, account_helper):
        login = f"vera{random.randrange(1000)}"
        user = PostV1AccountsRequest(login=login, email=f"{login}@mail.ru", password="1234567889")
        login_data = PostV1LoginRequest(login=user.login, password=user.password)

        account_helper.register_new_user(user)
        with allure.step(f"Check login new user: {user}"):
            login_response = account_helper.login_user(login_data)
            status_code = login_response.status_code
            assert status_code == HTTPStatus.OK, f"Error status code after login user: {status_code}"
