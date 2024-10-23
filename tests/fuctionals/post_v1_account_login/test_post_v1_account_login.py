from datetime import datetime

from hamcrest import (
    assert_that, has_property, has_properties, starts_with, all_of, instance_of, equal_to,
)
import random
import allure
from models.data_models.registration import Registration
from models.data_models.login_credentials import LoginCredentials


class TestPostV1AccountLogin:

    @allure.title("Check register user")
    def test_post_v1_account_login(self, account_helper):
        login = f"vera{random.randrange(1000, 2000)}"
        user = Registration(login=login, email=f"{login}@mail.ru", password="1234567889")
        login_data = LoginCredentials(login=user.login, password=user.password)

        account_helper.register_new_user(user)
        with allure.step(f"Check login new user: {user}"):
            login_response = account_helper.login_user(login_data, validate_response=False)
            assert login_response.status_code == 200, f"Incorrect status code: {login_response.status_code}"

