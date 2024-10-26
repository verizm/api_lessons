import pytest
import allure
from checkers.http_checkers import check_status_code_http
from data.data_helpers.user_creator import UserCreator
from dm_api_accounts.models.registration import Registration


class TestPostV1Accounts:

    @allure.title("Check register user")
    def test_post_v1_account(self, account_helper):
        user = UserCreator.make_user()

        with allure.step("Register new user"):
            with check_status_code_http(expected_status_code=200):
                account_helper.dm_account_api.account_api.post_v1_account(user)


    @allure.title("Check validation incorrect user creation data")
    @pytest.mark.parametrize(
        'model, status_code, field, msg',
        [
            (Registration(login="vera", password="12345", email="vera@mail.ru"), 400, "Password", ["Short"]),
            (Registration(login="vera", password="", email="vera@mail.ru"), 400, "Password", ["Empty", "Short"]),
            (Registration(login="", password="123456", email="vera@mail.ru"), 400, "Login", ["Empty", "Short"]),
            (Registration(login="vera", password="123456", email="@mail.ru"), 400, "Email", ["Invalid"]),
            (Registration(login="vera", password="123456", email="veramail.ru"), 400, "Email", ["Invalid"]),
            (Registration(login="vera", password="123456", email="vera@"), 400, "Email", ["Invalid"]),
        ]
    )
    def test_validation_for_incorrect_user_data(self, account_helper, model, status_code, field, msg):
        with allure.step("Check status code and response message after validation"):
            with check_status_code_http(status_code, field, msg):
                account_helper.dm_account_api.account_api.post_v1_account(model)
