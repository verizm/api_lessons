import random
import allure
from models.data_models.registration import Registration


class TestGetV1Account:

    def test_get_v1_account(self, auth_account_helper):
        login = f"vera{random.randrange(1000)}"
        user = Registration(login=login, email=f"{login}@mail.ru", password="1234567889")

        auth_account_helper = auth_account_helper(user)
        response = auth_account_helper.dm_account_api.account_api.get_v1_account()
        with allure.step("Check user data"):
            assert response.status_code == 200, f"Incorrect status code after get user data {response.status_code}"
