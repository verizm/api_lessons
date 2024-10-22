import random
from http import HTTPStatus
import allure
from models.data_models.registration import Registration
from models.data_models.login_credentials import LoginCredentials


class TestPostV1AccountLogin:

    @allure.title("Check register user")
    def test_post_v1_account_login(self, account_helper):
        login = f"vera{random.randrange(1000)}"
        user = Registration(login=login, email=f"{login}@mail.ru", password="1234567889")
        login_data = LoginCredentials(login=user.login, password=user.password)

        account_helper.register_new_user(user)
        with allure.step(f"Check login new user: {user}"):
            login_response = account_helper.login_user(login_data)
            status_code = login_response.status_code
            assert status_code == HTTPStatus.OK, f"Error status code after login user: {status_code}"
