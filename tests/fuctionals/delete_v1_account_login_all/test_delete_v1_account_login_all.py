import allure
import random
from models.data_models.registration import Registration


class TestDeleteV1AccountLoginAll:

    def test_delete_v1_account_login(self, auth_account_helper):
        login = f"vera{random.randrange(1000, 2000)}"
        user = Registration(login=login, email=f"{login}@mail.ru", password="1234567889")
        auth_account_helper = auth_account_helper(user)
        with allure.step("Check user relogin from all devices"):
            response = auth_account_helper.dm_account_api.login_api.delete_v1_account_login_all()
            assert response.status_code == 204, f"Incorrect status code after relogin {response.status_code}"