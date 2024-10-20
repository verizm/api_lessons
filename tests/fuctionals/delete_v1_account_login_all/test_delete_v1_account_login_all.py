import allure
import random
from models.api_models.api_account_models.post_v1_accounts_models import PostV1AccountsRequest


class TestDeleteV1AccountLoginAll:

    def test_delete_v1_account_login(self, auth_account_helper):
        login = f"vera{random.randrange(1000)}"
        user = PostV1AccountsRequest(login=login, email=f"{login}@mail.ru", password="1234567889")
        auth_account_helper = auth_account_helper(user)
        with allure.step("Check user relogin from all devices"):
            response = auth_account_helper.dm_account_api.login_api.delete_v1_account_login_all()
            assert response.status_code == 204, f"Incorrect status code after relogin {response.status_code}"