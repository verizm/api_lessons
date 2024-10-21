import random
import allure
from models.api_models.api_account_models.post_v1_accounts_models import PostV1AccountsRequest


class TestPutV1AccountPassword:

    def test_put_v1_account_password(self, auth_account_helper):
        login = f"vera{random.randrange(1000)}"
        user = PostV1AccountsRequest(login=login, email=f"{login}@mail.ru", password="1234567889")
        new_password = "12341111"
        auth_account_helper = auth_account_helper(user)
        response = auth_account_helper.change_password(user, new_password)

        with allure.step("Check password changed succesfully"):
            assert response.status_code == 200, f"Incorrect status code after change password {response.status_code}"

        with allure.step("Check that user authorized with new password"):
            user.password = new_password
            response = auth_account_helper.auth_client(user)
            assert response.status_code == 200, f"Incorrect status code auth user {response.status_code}"